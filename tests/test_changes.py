import copy

from scripts import changes


def e(id_, meeting="RAN1#125", text="Support X.", type_="Agreement", scope="agenda"):
    return {"id": id_, "meeting": meeting, "agenda_item": "9.2", "agenda_title": "NR MIMO Phase 6", "type": type_,
            "text": text, "scope": scope, "topic": "srs", "source": {"url": "https://www.3gpp.org/x.docx"}}


def test_diff_classifies_new_meeting_old_meeting_changes_and_renumbering():
    prev = [e("RAN1#125:9.2:001"), e("RAN1#125:9.2:002", text="Old text."), e("RAN1#125:9.2:003", text="Gone."),
            e("RAN1#125:9.2:004", text="Same text, new id.")]
    cur = [e("RAN1#125:9.2:001"),
           e("RAN1#125:9.2:002", text="New text."),                     # 원문 변경
           e("RAN1#125:9.2:005", text="Same text, new id."),            # id만 바뀜
           e("RAN1#125:9.2:009", text="Newly parsed."),                 # 과거 회의에 추가
           e("RAN1#126:9.2:001", meeting="RAN1#126"), e("RAN1#126:9.2:002", meeting="RAN1#126", text="Y")]  # 새 회의
    new_meetings, items, renumbered = changes.diff(prev, cur)
    assert new_meetings == [{"meeting": "RAN1#126", "count": 2}]
    assert renumbered == 1
    got = {(x["id"], x["what"], tuple(x["fields"])) for x in items}
    assert got == {("RAN1#125:9.2:002", "changed", ("text",)), ("RAN1#125:9.2:009", "added", ()),
                   ("RAN1#125:9.2:003", "removed", ())}


def test_scope_change_is_a_change():
    prev = [e("RAN1#125:9.2:001", scope="candidate")]
    cur = [e("RAN1#125:9.2:001", scope="agenda")]
    _, items, _ = changes.diff(prev, cur)
    assert items[0]["what"] == "changed" and items[0]["fields"] == ["scope"]


def test_record_baseline_unchanged_and_reason():
    cur = {"source_updated_at": "B", "entries": [e("RAN1#125:9.2:001")]}
    assert changes.record([], None, cur, "t0") == ([], None)            # 첫 실행: 기준만
    assert changes.record([], copy.deepcopy(cur), cur, "t1") == ([], None)  # 변화 없음
    prev = {"source_updated_at": "A", "entries": []}
    hist, change = changes.record([{"at": "old"}], prev, cur, "t2")
    assert change["reason"] == "원본 DB 갱신" and hist[0] is change and hist[1] == {"at": "old"}
    _, change = changes.record([], {"source_updated_at": "B", "entries": []}, cur, "t3")
    assert change["reason"].startswith("설정 변경")


def test_history_is_capped():
    prev = {"source_updated_at": "A", "entries": []}
    cur = {"source_updated_at": "B", "entries": [e("RAN1#125:9.2:001")]}
    hist = [{"at": str(i)} for i in range(changes.KEEP)]
    new, _ = changes.record(hist, prev, cur, "now")
    assert len(new) == changes.KEEP and new[0]["at"] == "now"
