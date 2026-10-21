"""직전 생성 결과(reports/csi_decisions.json)와 비교해 CSI 결정의 변경 이력(reports/changes.json)을 남깁니다.

'신규' 표시는 최신 회의 결정만 가리키므로, 원본이 과거 회의를 다시 처리해 생긴 변화
(파서 개선으로 새로 읽힌 결정, 잠정 → 종료본 교체, 범위·키워드 설정 변경)는 이력으로만 알 수 있습니다.

변경 묶음(change set) 하나는 한 번의 실행에서 달라진 것입니다.
  new_meetings : 새로 들어온 회의와 그 회의 결정 수 (결정 자체는 대시보드에서 '신규'로 보임)
  items        : 기존 회의에서 추가(added)·변경(changed)·삭제(removed)된 결정
  renumbered   : 원문은 같고 id만 바뀐 결정 수 (원본 순번 재계산. 변경으로 보지 않음)
처음 실행(비교할 이전 결과가 없음)에는 기준만 잡고 이력을 남기지 않습니다.
"""
from scripts.scope import meeting_sort_key

FIELDS = ("meeting", "type", "text", "scope")
FIELD_LABEL = {"meeting": "회의", "type": "구분", "text": "원문", "scope": "범위"}
KEEP = 30  # 보관할 변경 묶음 수


def _first_line(text, n=140):
    line = (text or "").strip().split("\n")[0].strip()
    return line if len(line) <= n else line[:n - 1] + "…"


def _item(e, what, fields=()):
    return {"id": e["id"], "what": what, "fields": list(fields), "meeting": e["meeting"], "type": e["type"],
            "scope": e["scope"], "topic": e.get("topic"), "agenda": f"{e['agenda_item']} {e['agenda_title']}",
            "line": _first_line(e["text"]), "url": e["source"]["url"]}


def is_source(change):
    """원본(회의록) DB가 바뀌어 생긴 변경인지. 아니면 이 대시보드의 범위·키워드·주제 설정을 바꾼 결과입니다."""
    return change["reason"].startswith("원본")


def reason_label(change):
    """팀원에게 보이는 이유. 설정 변경은 RAN1 회의록 변화로 오해하지 않도록 분명히 적습니다."""
    return "원본 회의록 갱신" if is_source(change) else "대시보드 범위 조정 (RAN1 회의록 변화 아님)"


def item_label(item):
    """결정 목록 카드에 붙일 짧은 표시."""
    if item["what"] == "added":
        return "과거 회의에 추가"
    if item["what"] == "removed":
        return "삭제"
    f = item["fields"]
    if "text" in f:
        return "원문 변경"
    if "type" in f:
        return "구분 변경"
    if "meeting" in f:
        return "회의 변경"
    return "CSI 범위 변경"


def latest_source(history):
    """가장 최근의 원본(회의록) 변경 묶음. 없으면 None."""
    return next((c for c in history if is_source(c)), None)


def diff(prev_entries, cur_entries):
    """이전·현재 결정 목록 → (new_meetings, items, renumbered)."""
    prev = {e["id"]: e for e in prev_entries}
    cur = {e["id"]: e for e in cur_entries}
    prev_meetings = {e["meeting"] for e in prev_entries}
    added = [cur[i] for i in cur if i not in prev]
    removed = [prev[i] for i in prev if i not in cur]
    # id만 바뀐 결정(같은 회의, 같은 원문·구분·범위)은 짝지어 변경에서 뺍니다.
    pool = {}
    for e in removed:
        pool.setdefault((e["meeting"], e["type"], e["scope"], e["text"]), []).append(e)
    renumbered, still_added = 0, []
    for e in added:
        same = pool.get((e["meeting"], e["type"], e["scope"], e["text"]))
        if same:
            same.pop()
            renumbered += 1
        else:
            still_added.append(e)
    still_removed = [e for group in pool.values() for e in group]

    new_meetings = {}
    items = []
    for e in still_added:
        if e["meeting"] in prev_meetings:
            items.append(_item(e, "added"))
        else:
            new_meetings[e["meeting"]] = new_meetings.get(e["meeting"], 0) + 1
    for i in cur:
        if i in prev:
            changed = [f for f in FIELDS if prev[i].get(f) != cur[i].get(f)]
            if changed:
                items.append(_item(cur[i], "changed", changed))
    items += [_item(e, "removed") for e in still_removed]
    items.sort(key=lambda x: (meeting_sort_key(x["meeting"]), x["id"]))
    return ([{"meeting": k, "count": v} for k, v in sorted(new_meetings.items(), key=lambda kv: meeting_sort_key(kv[0]))],
            items, renumbered)


def record(history, prev_export, cur_export, now):
    """이전 결과와 비교해 변화가 있으면 history 맨 앞에 변경 묶음을 추가합니다. (새 history, 추가된 묶음 또는 None)"""
    if not prev_export:
        return history, None
    new_meetings, items, renumbered = diff(prev_export["entries"], cur_export["entries"])
    if not new_meetings and not items:
        return history, None
    source_changed = prev_export.get("source_updated_at") != cur_export.get("source_updated_at")
    change = {
        "at": now,
        "source_updated_at": cur_export.get("source_updated_at"),
        "reason": "원본 DB 갱신" if source_changed else "설정 변경 (범위·키워드·주제 규칙)",
        "new_meetings": new_meetings,
        "counts": {w: sum(1 for x in items if x["what"] == w) for w in ("added", "changed", "removed")},
        "renumbered": renumbered,
        "items": items,
    }
    return [change] + history[:KEEP - 1], change
