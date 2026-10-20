"""원본 DB의 결정 중 CSI 범위를 고르고 주제를 붙입니다 (규칙은 config/csi_scope.yaml).

결정마다 scope 하나가 붙습니다.
  agenda    : 포함 Agenda에 기록된 결정 (확정)
  manual    : include_ids로 사람이 올린 결정 (확정)
  candidate : 포함 Agenda 밖이지만 보조 키워드나 사양 조항 번호가 원문에 있는 결정 (후보)
exclude_ids에 있거나 어디에도 해당하지 않는 결정은 빠집니다.

주제는 '주된 주제'(topic) 하나와 '관련 주제'(tags) 여러 개입니다. tags에는 주된 주제도 들어 있습니다.

Agenda 번호는 회의마다 바뀌므로 '섹션 제목 + Agenda 제목'으로 매칭합니다 (원본 scripts/agenda.py와 같은 정규화).
"""
import re

CONFIRMED = ("agenda", "manual")

# 사양 번호: 'TS 38.214', 'TS38.214', '38.214'
SPEC_RE = re.compile(r"(?<![\d.])(?:T[SR]\s?)?(3[678]\.\d{3})(?![\d])")
# 조항 번호: 'Clause 5.2.5', 'Section 5.2.1.6', 'Clauses 5.2.1.4.6 and 5.2.1.4.2', 'sub-clause 6'
CLAUSE_RE = re.compile(r"(?i)\b(?:sub-?)?(?:clause|section)s?\s+(\d+(?:\.\d+)*(?:\s*(?:,|and|&)\s*\d+(?:\.\d+)*)*)")
# 사양 바로 뒤의 번호: 'TS38.214 5.2.1.4.6 CSI-PAI reporting'
SPEC_NUMBER_RE = re.compile(r"(?<![\d.])T[SR]\s?(3[678]\.\d{3})\s+(\d+\.\d+(?:\.\d+)*)(?![\d.])")
# 'Section 2 of R1-2508774'처럼 TDoc 안의 절은 사양 조항이 아님
TDOC_SECTION_RE = re.compile(r"\s*(?:of|in)\s+(?:the\s+)?R1-\d")
# 조항 번호 바로 뒤에 붙은 사양: 'Clause 5.2.1.6 of TS 38.214', 'section 5.2.1.6, TS 38.214', '… in Rel-19 TS38.214'
SPEC_AFTER_RE = re.compile(r"\s*,?\s*(?:(?:of|in|for|to)\s+)?(?:the\s+)?(?:Rel-\d+\s*,?\s*)?T[SR]\s?(3[678]\.\d{3})")
# 조항 번호 바로 앞에 붙은 사양: 'TS 38.214 Clause 5.2.2.5', 'TS38.214, Clause 5.2.5'
SPEC_BEFORE_RE = re.compile(r"T[SR]\s?(3[678]\.\d{3})[\s,]*$")


def norm(title):
    title = title.replace("“", '"').replace("”", '"').replace("’", "'")
    return " ".join(title.lower().split()).rstrip(" .:")


def meeting_sort_key(meeting_id):
    m = re.fullmatch(r"RAN1#(\d+)(.*)", meeting_id)
    if not m:
        raise ValueError(f"meeting id must look like 'RAN1#118': {meeting_id!r}")
    return int(m.group(1)), m.group(2)


def clause_mentions(text):
    """원문에서 (사양, 조항) 쌍을 찾습니다. 같은 줄 안에서만 짝짓습니다.

    조항 번호 바로 뒤('… in TS 38.214')나 바로 앞('TS 38.214 Clause …')에 붙은 사양을 먼저 쓰고,
    없으면 그 줄에서 가장 가까운 사양을 씁니다.
    """
    found = []
    for line in text.split("\n"):
        specs = [(m.start(), m.end(), m.group(1)) for m in SPEC_RE.finditer(line)]
        if not specs:
            continue
        for m in CLAUSE_RE.finditer(line):
            if TDOC_SECTION_RE.match(line, m.end()):
                continue
            after, before = SPEC_AFTER_RE.match(line, m.end()), SPEC_BEFORE_RE.search(line[:m.start()])
            if after:
                spec = after.group(1)
            elif before:
                spec = before.group(1)
            else:
                gap = lambda s: m.start() - s[1] if s[1] <= m.start() else s[0] - m.end()  # noqa: E731
                spec = min(specs, key=gap)[2]
            found += [(spec, n) for n in re.findall(r"\d+(?:\.\d+)*", m.group(1))]
        found += [(m.group(1), m.group(2)) for m in SPEC_NUMBER_RE.finditer(line)]
    return list(dict.fromkeys(found))


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
        self.clauses = [{"spec": str(c["spec"]), "clause": str(c["clause"]), "topic": c.get("topic"), "exact": bool(c.get("exact"))}
                        for c in config.get("spec_clauses") or []]
        self.topics = [{"id": t["id"], "label": t["label"], "patterns": [re.compile(p) for p in t.get("patterns") or []]}
                       for t in config.get("topics") or []]
        fb = config.get("fallback_topic") or {"id": "other", "label": "기타 CSI"}
        self.fallback = {"id": fb["id"], "label": fb["label"], "patterns": []}
        ids = [t["id"] for t in self.topics] + [self.fallback["id"]]
        if len(set(ids)) != len(ids):
            raise ValueError(f"topics id가 중복됩니다: {ids}")
        for where, topic in ([(f"agendas[{a['index']}]", a["topic"]) for a in self.agendas]
                             + [(f"spec_clauses[{i}]", c["topic"]) for i, c in enumerate(self.clauses)]):
            if topic and topic not in ids:
                raise ValueError(f"{where}: 알 수 없는 topic {topic!r} (가능: {ids})")
        self.include_ids = set(config.get("include_ids") or [])
        self.exclude_ids = set(config.get("exclude_ids") or [])

    def topic_list(self):
        return [{"id": t["id"], "label": t["label"]} for t in self.topics + [self.fallback]]

    def match_agenda(self, entry):
        """(포함 목록 항목, 그 항목에 해당하는 Agenda 번호) 또는 (None, None). 먼저 적힌 항목이 우선합니다.

        children 항목에 하위 Agenda 결정이 걸리면 번호는 하위가 아니라 그 항목(상위 Agenda)의 번호입니다.
        """
        nodes = entry["agenda_path"]
        path = [norm(n["title"]) for n in nodes]
        section, below = path[0], path[1:]
        for a in self.agendas:
            if a["section"] != section:
                continue
            p, n = a["path"], len(a["path"])
            for start in range(len(below) - n + 1):
                if below[start:start + n] == p and (a["children"] or start + n == len(below)):
                    return a, nodes[start + n]["number"]
        return None, None

    def _text(self, entry):
        text = "\n".join([entry.get("text") or ""] + list(entry.get("ffs") or []))
        for r in self.ignore:
            text = r.sub(" ", text)
        return text

    def _clause_hits(self, text):
        """설정의 spec_clauses에 해당하는 조항 언급: [(표시 문자열, topic)]."""
        hits = []
        for spec, number in clause_mentions(text):
            for c in self.clauses:
                if spec == c["spec"] and (number == c["clause"] or (not c["exact"] and number.startswith(c["clause"] + "."))):
                    hits.append((f"TS {spec} {number}", c["topic"]))
                    break
        return hits

    def _pattern_topics(self, text):
        return [t["id"] for t in self.topics if any(r.search(text) for r in t["patterns"])]

    def topics_for(self, entry, agenda=None):
        """(주된 주제, 관련 주제 목록). 관련 주제는 config topics 순서이며 주된 주제를 포함합니다."""
        text = self._text(entry)
        by_pattern = self._pattern_topics(text)
        by_clause = [t for _, t in self._clause_hits(text) if t]
        if agenda and agenda["topic"]:
            primary = agenda["topic"]
        else:
            primary = (by_pattern or by_clause or [self.fallback["id"]])[0]
        tags = {primary, *by_pattern, *by_clause}
        order = [t["id"] for t in self.topic_list()]
        return primary, [t for t in order if t in tags]

    def keyword_hits(self, entry):
        """후보 판정에 쓰는 일치 표시: 실제로 일치한 단어(대소문자 무시 중복 제거)와 'TS 38.214 5.2.5' 같은 조항."""
        text = self._text(entry)
        words = {}
        for r in self.keywords:
            m = r.search(text)
            if m:
                words.setdefault(m.group(0).lower(), m.group(0))
        clauses = dict.fromkeys(label for label, _ in self._clause_hits(text))
        return list(words.values()) + list(clauses)

    def classify(self, entry):
        """{"scope", "topic", "tags", "agenda_rule", "agenda_number", "keywords"} 또는 범위 밖이면 None."""
        if entry["id"] in self.exclude_ids:
            return None
        agenda, number = self.match_agenda(entry)
        if agenda:
            topic, tags = self.topics_for(entry, agenda)
            return {"scope": "agenda", "topic": topic, "tags": tags, "agenda_rule": agenda["index"],
                    "agenda_number": number, "keywords": []}
        hits = self.keyword_hits(entry)
        if entry["id"] in self.include_ids:
            scope = "manual"
        elif hits:
            scope = "candidate"
        else:
            return None
        topic, tags = self.topics_for(entry)
        return {"scope": scope, "topic": topic, "tags": tags, "agenda_rule": None,
                "agenda_number": entry["agenda_item"], "keywords": hits}


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
