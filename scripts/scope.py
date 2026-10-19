"""원본 DB의 결정 중 CSI 범위를 고르고 주제를 붙입니다 (규칙은 config/csi_scope.yaml).

결정마다 scope 하나가 붙습니다.
  agenda    : 포함 Agenda에 기록된 결정 (확정)
  manual    : include_ids로 사람이 올린 결정 (확정)
  candidate : 포함 Agenda 밖이지만 보조 키워드가 원문에 있는 결정 (후보)
exclude_ids에 있거나 어디에도 해당하지 않는 결정은 빠집니다.

Agenda 번호는 회의마다 바뀌므로 '섹션 제목 + Agenda 제목'으로 매칭합니다 (원본 scripts/agenda.py와 같은 정규화).
"""
import re

CONFIRMED = ("agenda", "manual")


def norm(title):
    title = title.replace("“", '"').replace("”", '"').replace("’", "'")
    return " ".join(title.lower().split()).rstrip(" .:")


def meeting_sort_key(meeting_id):
    m = re.fullmatch(r"RAN1#(\d+)(.*)", meeting_id)
    if not m:
        raise ValueError(f"meeting id must look like 'RAN1#118': {meeting_id!r}")
    return int(m.group(1)), m.group(2)


class Scope:
    def __init__(self, config):
        self.agendas = []
        for i, a in enumerate(config.get("agendas") or []):
            path = [norm(t) for t in a["path"]]
            if not path:
                raise ValueError(f"agendas[{i}]: path가 비어 있습니다")
            self.agendas.append({"index": i, "section": norm(a["section"]), "path": path,
                                 "children": bool(a.get("children")), "topic": a.get("topic"),
                                 "label": a.get("label") or a["path"][-1], "section_title": a["section"]})
        self.ignore = [re.compile(p) for p in config.get("ignore_phrases") or []]
        self.keywords = [re.compile(p) for p in config.get("candidate_keywords") or []]
        self.topics = [{"id": t["id"], "label": t["label"], "patterns": [re.compile(p) for p in t.get("patterns") or []]}
                       for t in config.get("topics") or []]
        fb = config.get("fallback_topic") or {"id": "other", "label": "기타 CSI"}
        self.fallback = {"id": fb["id"], "label": fb["label"], "patterns": []}
        ids = [t["id"] for t in self.topics] + [self.fallback["id"]]
        if len(set(ids)) != len(ids):
            raise ValueError(f"topics id가 중복됩니다: {ids}")
        for a in self.agendas:
            if a["topic"] and a["topic"] not in ids:
                raise ValueError(f"agendas[{a['index']}]: 알 수 없는 topic {a['topic']!r} (가능: {ids})")
        self.include_ids = set(config.get("include_ids") or [])
        self.exclude_ids = set(config.get("exclude_ids") or [])

    def topic_list(self):
        return [{"id": t["id"], "label": t["label"]} for t in self.topics + [self.fallback]]

    def match_agenda(self, entry):
        """결정이 기록된 Agenda가 포함 목록의 몇 번째 항목인지 (없으면 None). 먼저 적힌 항목이 우선합니다."""
        path = [norm(n["title"]) for n in entry["agenda_path"]]
        section, below = path[0], path[1:]
        for a in self.agendas:
            if a["section"] != section:
                continue
            p, n = a["path"], len(a["path"])
            for start in range(len(below) - n + 1):
                if below[start:start + n] == p and (a["children"] or start + n == len(below)):
                    return a
        return None

    def _text(self, entry):
        text = "\n".join([entry.get("text") or ""] + list(entry.get("ffs") or []))
        for r in self.ignore:
            text = r.sub(" ", text)
        return text

    def topic_for(self, entry, agenda=None):
        if agenda and agenda["topic"]:
            return agenda["topic"]
        text = self._text(entry)
        for t in self.topics:
            if any(r.search(text) for r in t["patterns"]):
                return t["id"]
        return self.fallback["id"]

    def keyword_hits(self, entry):
        text = self._text(entry)
        return [r.pattern for r in self.keywords if r.search(text)]

    def classify(self, entry):
        """{"scope", "topic", "agenda_rule", "keywords"} 또는 범위 밖이면 None."""
        if entry["id"] in self.exclude_ids:
            return None
        agenda = self.match_agenda(entry)
        if agenda:
            return {"scope": "agenda", "topic": self.topic_for(entry, agenda), "agenda_rule": agenda["index"], "keywords": []}
        hits = self.keyword_hits(entry)
        if entry["id"] in self.include_ids:
            return {"scope": "manual", "topic": self.topic_for(entry), "agenda_rule": None, "keywords": hits}
        if hits:
            return {"scope": "candidate", "topic": self.topic_for(entry), "agenda_rule": None, "keywords": hits}
        return None


def select(db, config):
    """원본 DB → CSI 결정 목록 (회의 순, 같은 회의 안에서는 원본 순서). 각 결정에 classify 결과를 덧붙입니다."""
    scope = Scope(config)
    known = {e["id"] for e in db["entries"]}
    missing = sorted((scope.include_ids | scope.exclude_ids) - known)
    out = []
    for order, e in enumerate(db["entries"]):
        c = scope.classify(e)
        if c:
            out.append({**e, **c, "_order": order})
    out.sort(key=lambda e: (meeting_sort_key(e["meeting"]), e["_order"]))
    for e in out:
        del e["_order"]
    meetings = sorted({e["meeting"] for e in db["entries"]}, key=meeting_sort_key)
    return {"scope": scope, "entries": out, "meetings": meetings, "unknown_manual_ids": missing}
