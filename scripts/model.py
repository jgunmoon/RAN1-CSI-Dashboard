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
        agendas.append({"index": a["index"], "label": a["label"], "section": a["section_title"], "topic": a["topic"],
                        "numbers": numbers, "last_number": numbers[max(numbers, key=scope_mod.meeting_sort_key)] if numbers else "",
                        "entries": mine})
    latest = meetings[-1] if meetings else None
    prev = meetings[-2] if len(meetings) > 1 else None
    return {
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
