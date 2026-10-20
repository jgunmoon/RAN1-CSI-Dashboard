"""결정마다 실무 확인용 정보를 덧붙입니다 (원문은 그대로 두고 표시용 필드만 추가).

  clauses : 원문에 나온 사양 조항 ('TS 38.214 5.2.2.5') — 설계 문서와 대조용
  stage   : 진행 단계 (Study / 규격 작업 / 유지보수 CR / UE features) — config stages
  impact  : 구현 영향 태그 (처리 타임라인·CPU, UE capability, 포트·자원 수 등) — config impact_tags
  warn    : 원문만으로는 부족한 결정 (수식 누락 의심, 색 표시 변경 손실, 실제 변경이 TDoc에만 있음)
  tdocs   : 원문에 나온 R1- 번호 → FTP 링크 (회의 폴더는 원본 DB의 근거 TDoc 번호 범위로 추정)
그 밖에 UE feature(FG) 목록과 FFS 줄별 후속 결정 후보를 만듭니다.
"""
import re
from bisect import bisect_right

from scripts import scope as scope_mod

FTP = "https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/"
R1_RE = re.compile(r"\bR1-(\d{7})\b")
# Word 수식이 추출되지 않아 생긴 흔적: 단어 사이 공백 2개 이상, '( ,', ', ,', '{ ,', '= ,', 'of ,'
MATH_GAP_RE = re.compile(r"(?<=[A-Za-z,(=])[ ]{2,}(?=[A-Za-z,)=])|\(\s*[,)]|,\s*,|\{\s*[,}]|=\s*[,;.)]|\bof\s*,")
COLOR_RE = re.compile(r"(?i)highlighted in chromatic fonts|chromatic font")
TP_RE = re.compile(r"(?i)\b(TP|CR|text proposal|proposal \d+)\b.*\b(endorsed|agreed)\b|\badopt the following (TP|TPs|changes)\b")
FG_ID_RE = re.compile(r"^\d{2}-\d+[a-z]?(?:-\d+[a-z]?)*$")


class TdocLinker:
    """R1 번호 → 그 TDoc이 있는 회의 폴더. 원본 DB의 근거 TDoc(tdoc_url)에서 회의별 번호 범위를 만듭니다.

    범위 안이면 그 회의, 회의 사이 빈 구간이면 그 번호를 인용한 결정의 회의(앞·뒤 회의 중 하나일 때), 아니면 앞 회의
    (회의 중 늦게 등록된 문서). 알 수 없으면 None.
    """

    def __init__(self, db):
        spans = {}
        for e in db["entries"]:
            m = re.search(r"/(TSGR1_[^/]+)/Docs/R1-(\d{7})", e["source"].get("tdoc_url") or "")
            if m:
                lo, hi = spans.get(m.group(1), (10 ** 8, 0))
                n = int(m.group(2))
                spans[m.group(1)] = (min(lo, n), max(hi, n))
        self.spans = sorted((lo, hi, f) for f, (lo, hi) in spans.items())
        self.los = [s[0] for s in self.spans]
        self.folder_of = {m: v.get("ftp_dir") for m, v in (db.get("meetings") or {}).items()}

    def folder(self, number, meeting=None):
        i = bisect_right(self.los, number) - 1
        if i < 0:
            return None
        lo, hi, f = self.spans[i]
        if number <= hi:
            return f
        nxt = self.spans[i + 1] if i + 1 < len(self.spans) else None
        if nxt and str(nxt[0])[:2] != str(number)[:2]:
            nxt = None
        own = self.folder_of.get(meeting)
        if nxt is None:  # 마지막 회의 뒤: 인용한 결정의 회의가 이 회의 이후면 그 회의
            return own if own and own != f and str(number)[:2] == str(hi)[:2] else f
        return own if own in (f, nxt[2]) else f

    def url(self, number, meeting=None):
        f = self.folder(number, meeting)
        return f"{FTP}{f}/Docs/R1-{number}.zip" if f else None


def _title_match(specs):
    ms = [scope_mod.title_matcher(s) for s in specs]
    return lambda t: any(m(t) for m in ms)


class Enricher:
    def __init__(self, config, db):
        self.stages = [{"id": s["id"], "label": s["label"], "match": _title_match(s["match"])}
                       for s in config.get("stages") or []]
        fb = config.get("fallback_stage") or {"id": "other", "label": "기타"}
        self.fallback_stage = {"id": fb["id"], "label": fb["label"]}
        self.impacts = [{"id": t["id"], "label": t["label"], "patterns": [re.compile(p) for p in t["patterns"]]}
                        for t in config.get("impact_tags") or []]
        self.linker = TdocLinker(db)

    def stage_list(self):
        return [{"id": s["id"], "label": s["label"]} for s in self.stages] + [self.fallback_stage]

    def impact_list(self):
        return [{"id": t["id"], "label": t["label"]} for t in self.impacts]

    def stage(self, entry):
        titles = [scope_mod.norm(n["title"]) for n in entry["agenda_path"]]
        for s in self.stages:
            if any(s["match"](t) for t in titles):
                return s["id"]
        return self.fallback_stage["id"]

    def enrich(self, e):
        text = e["text"]
        full = "\n".join([text] + list(e.get("ffs") or []))
        warn = []
        if MATH_GAP_RE.search(full):
            warn.append("math")
        if COLOR_RE.search(text):
            warn.append("color")
        if TP_RE.search(text) and len(text) < 300 and R1_RE.search(text):
            warn.append("tdoc")
        tdocs = {}
        for n in dict.fromkeys(int(x) for x in R1_RE.findall(full)):
            u = self.linker.url(n, e["meeting"])
            if u:
                tdocs[f"R1-{n}"] = u
        return {
            "clauses": [f"TS {s} {n}" for s, n in scope_mod.clause_mentions(full)],
            "stage": self.stage(e),
            "impact": [t["id"] for t in self.impacts if any(r.search(full) for r in t["patterns"])],
            "warn": warn,
            "tdocs": tdocs,
        }


def feature_groups(entries):
    """UE feature 표 줄('| 58. NR_AIML_Air | 58-1-2 | 이름 | 구성 요소 … |')에서 FG 목록을 만듭니다.

    FG마다 이름(가장 최근 결정 기준), 이 FG를 정의·수정한 결정 id들(회의 순)을 돌려줍니다.
    원문 추출에서 색 표시(추가·삭제)가 사라졌으므로 내용은 참고용이며 정확한 정의는 TDoc을 봐야 합니다.
    """
    fgs = {}
    for e in entries:
        for line in e["text"].split("\n"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")] if line.lstrip().startswith("|") else []
            if len(cells) < 3 or not FG_ID_RE.match(cells[1]):
                continue
            fg = fgs.setdefault(cells[1], {"id": cells[1], "item": cells[0], "name": cells[2], "ids": [], "meetings": [],
                                           "row": cells})
            fg.update(item=cells[0], name=cells[2], row=cells)
            if e["id"] not in fg["ids"]:
                fg["ids"].append(e["id"])
                fg["meetings"].append(e["meeting"])
    def key(f):  # '58-2-15a' → [(58, ''), (2, ''), (15, 'a')]
        return [(int(re.match(r"\d+", p).group()), p.lstrip("0123456789")) for p in f["id"].split("-")]
    return sorted(fgs.values(), key=key)


STOP = set("""ffs the for and with from that this which whether how what are not can may also any all each other such
than into over per via its their between both following support supported study studied consider considered including
include based case cases details detail further discuss discussed value values use used using one two set sets e.g etc
up down only same new legacy rel ue nw gnb least at in on of to by or as be is if it an a""".split())


def _tokens(text):
    return {w for w in re.findall(r"[A-Za-z][A-Za-z0-9_\-/]{2,}", text.lower()) if w not in STOP}


def ffs_followups(entries, key, limit=3, threshold=0.5):
    """FFS 줄마다 같은 Agenda(key)의 이후 회의 결정 중 단어가 많이 겹치는 '후속 결정 후보'.

    해소 여부를 판정하지 않습니다. 겹치는 단어 비율(FFS 줄 기준) ≥ threshold, 겹치는 단어 2개 이상만 고릅니다.
    """
    order = {}
    for e in entries:
        order.setdefault(e["meeting"], len(order))
    by_key = {}
    for e in entries:
        by_key.setdefault(key(e), []).append(e)
    out = []
    for e in entries:
        for line in e.get("ffs") or []:
            toks = _tokens(re.sub(r"(?i)^\s*-?\s*FFS\s*:?", "", line))
            cands = []
            if toks:
                for later in by_key[key(e)]:
                    if order[later["meeting"]] <= order[e["meeting"]]:
                        continue
                    common = toks & _tokens(later["text"])
                    score = len(common) / len(toks)
                    if len(common) >= 2 and score >= threshold:
                        cands.append((score, later["id"]))
            cands.sort(key=lambda c: (-c[0], c[1]))
            out.append({"id": e["id"], "meeting": e["meeting"], "line": line.strip(), "followups": [i for _, i in cands[:limit]]})
    return out
