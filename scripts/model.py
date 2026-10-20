"""고른 CSI 결정으로 리포트에 쓰는 표 데이터를 만듭니다 (HTML·마크다운 공용)."""
from collections import defaultdict
from datetime import datetime, timedelta, timezone

from scripts import scope as scope_mod

TYPES = ("Agreement", "Working Assumption", "Conclusion")
TYPE_SHORT = {"Agreement": "Agreement", "Working Assumption": "WA", "Conclusion": "Conclusion"}
SCOPE_LABEL = {"agenda": "확정", "manual": "확정(수동)", "candidate": "후보"}


def format_kst(iso):
    """'2026-10-17T01:52:52+00:00' → '2026-10-17 10:52 KST'. 값이 없으면 None."""
    if not iso:
        return None
    return datetime.fromisoformat(iso).astimezone(timezone(timedelta(hours=9))).strftime("%Y-%m-%d %H:%M KST")


def short(meeting):
    return meeting.replace("RAN1#", "#")


def provisional(db, meeting):
    return (db.get("meetings") or {}).get(meeting, {}).get("provisional")


def count(entries, key, meetings, pred=lambda e: True):
    """{key(e): {meeting: n}}"""
    out = defaultdict(lambda: dict.fromkeys(meetings, 0))
    for e in entries:
        if pred(e):
            out[key(e)][e["meeting"]] += 1
    return out


def build(db, config):
    sel = scope_mod.select(db, config)
    sc, entries, meetings = sel["scope"], sel["entries"], sel["meetings"]
    topics = sc.topic_list()
    topic_label = {t["id"]: t["label"] for t in topics}
    agendas = []
    for a in sc.agendas:
        mine = [e for e in entries if e["agenda_rule"] == a["index"]]
        numbers = {}
        for e in mine:
            numbers[e["meeting"]] = e["agenda_number"]  # children 항목이면 하위가 아니라 그 Agenda 자체의 번호
        # 섹션 이름은 설정값(정규식일 수 있음)이 아니라 실제로 걸린 가장 최근 결정의 섹션 제목
        section = mine[-1]["agenda_path"][0]["title"] if mine else a["section_title"].removeprefix("re:")
        agendas.append({"index": a["index"], "label": a["label"], "section": section, "topic": a["topic"],
                        "numbers": numbers, "last_number": numbers[max(numbers, key=scope_mod.meeting_sort_key)] if numbers else "",
                        "entries": mine})
    latest = meetings[-1] if meetings else None
    prev = meetings[-2] if len(meetings) > 1 else None
    return {
        "alerts": agenda_alerts(db, entries, agendas, meetings),
        "db": db, "config": config, "entries": entries, "meetings": meetings, "topics": topics, "topic_label": topic_label,
        "agendas": agendas, "latest": latest, "prev": prev, "unknown_manual_ids": sel["unknown_manual_ids"],
        "updated_kst": format_kst(db.get("updated_at")),
        "provisional": [m for m in meetings if provisional(db, m)],
    }


def confirmed(e):
    return e["scope"] in scope_mod.CONFIRMED


def agreement(e):
    return e["type"] == "Agreement"


def candidate_agendas(m):
    """후보 결정이 기록된 Agenda (섹션 > Agenda 제목) 별 건수, 많은 순."""
    per = defaultdict(lambda: {"count": 0, "numbers": set()})
    for e in m["entries"]:
        if e["scope"] == "candidate":
            p = e["agenda_path"]
            k = (p[0]["title"], p[-1]["title"])
            per[k]["count"] += 1
            per[k]["numbers"].add(p[-1]["number"])
    return sorted(((s, t, v["count"], sorted(v["numbers"], key=lambda n: [int(x) for x in n.split(".") if x.isdigit()]))
                   for (s, t), v in per.items()), key=lambda r: (-r[2], r[0], r[1]))


def agenda_alerts(db, entries, agendas, meetings):
    """최신 회의에서 Agenda 구성이 바뀐 곳. 결정이 조용히 빠지지 않도록 대시보드·README·실행 요약에 경고로 보여줍니다.

    dropped: 직전 회의에는 결정이 있던 포함 Agenda가 최신 회의에는 없음 (제목·섹션이 바뀌었거나 끝난 Agenda).
    new    : 이전 회의에 없던 Agenda(섹션 제목 + Agenda 제목)가 최신 회의에 생겼고, CSI 결정(확정·후보)이 있음.
    """
    if len(meetings) < 2:
        return {"dropped": [], "new": []}
    latest, prev = meetings[-1], meetings[-2]
    dropped = []
    for a in agendas:
        per = {}
        for e in a["entries"]:
            per[e["meeting"]] = per.get(e["meeting"], 0) + 1
        if per.get(prev) and not per.get(latest):
            dropped.append({"label": a["label"], "section": a["section"], "prev_count": per[prev],
                            "prev_number": a["numbers"].get(prev, "")})

    # 회의 간 연결은 '섹션 + Agenda 제목'(번호·상위가 바뀌어도 같은 Agenda). 같은 회의에 같은 제목이 여러 번 나오면
    # (예: 'Other aspects') 상위 제목 전체 경로로 구분합니다 (원본 scripts/agenda.py와 같은 방식).
    numbers = {}
    for e in db["entries"]:
        p = e["agenda_path"]
        numbers.setdefault((e["meeting"], scope_mod.norm(p[0]["title"]), scope_mod.norm(p[-1]["title"])), set()).add(p[-1]["number"])

    def key(e):
        p = e["agenda_path"]
        sec, leaf = scope_mod.norm(p[0]["title"]), scope_mod.norm(p[-1]["title"])
        if len(numbers[(e["meeting"], sec, leaf)]) > 1:
            return sec, " > ".join(scope_mod.norm(n["title"]) for n in p[1:])
        return sec, leaf

    earlier = {key(e) for e in db["entries"] if e["meeting"] != latest}
    earlier_sections = {k[0] for k in earlier}
    picked = {e["id"]: e for e in entries if e["meeting"] == latest}
    new = {}
    for e in db["entries"]:
        if e["meeting"] != latest or key(e) in earlier:
            continue
        p = e["agenda_path"]
        row = new.setdefault(key(e), {"section": p[0]["title"], "title": p[-1]["title"], "number": p[-1]["number"],
                                      "new_section": key(e)[0] not in earlier_sections,
                                      "total": 0, "confirmed": 0, "candidate": 0})
        row["total"] += 1
        c = picked.get(e["id"])
        if c:
            row["confirmed" if confirmed(c) else "candidate"] += 1
    rows = [r for r in new.values() if r["confirmed"] or r["candidate"]]
    rows.sort(key=lambda r: (-r["candidate"] - r["confirmed"], r["number"]))
    return {"dropped": dropped, "new": rows}
