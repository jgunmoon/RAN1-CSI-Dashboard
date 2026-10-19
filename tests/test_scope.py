import pytest

from scripts import scope


def by_id(sel):
    return {e["id"]: e for e in sel["entries"]}


def test_agenda_matched_by_title_across_number_and_parent_change(db, config):
    got = by_id(scope.select(db, config))
    a, b = got["RAN1#125:10.5.2.4:001"], got["RAN1#126:10.5.3.4:001"]
    assert a["scope"] == b["scope"] == "agenda"
    assert a["agenda_rule"] == b["agenda_rule"]
    assert a["topic"] == b["topic"] == "beam"  # Agenda에 고정된 주제가 SRS 키워드보다 우선


def test_topic_from_keywords_in_rule_order(db, config):
    got = by_id(scope.select(db, config))
    assert got["RAN1#126:10.5.3.1:001"]["topic"] == "report"
    assert got["RAN1#126:10.5.3.1:002"]["topic"] == "csirs"
    assert got["RAN1#126:10.5.3.1:003"]["topic"] == "other"  # 키워드 없음 → fallback
    assert got["RAN1#126:9.2:001"]["topic"] == "srs"


def test_path_segment_and_children(db, config):
    got = by_id(scope.select(db, config))
    assert got["RAN1#126:10.5.3.3:001"]["scope"] == "agenda"      # CSI acquisition and report > Other aspects
    assert "RAN1#126:10.8.9:001" not in got                       # ISAC > Other aspects
    assert got["RAN1#125:9.1.1.1:001"]["scope"] == "agenda"       # children: true
    assert got["RAN1#125:9.1.1.1:001"]["topic"] == "aiml"
    assert got["RAN1#126:9.2:001"]["scope"] == "agenda"           # 상위 Agenda 자체
    assert "RAN1#126:9.2.9:001" not in got                        # 목록에 없는 하위 Agenda (키워드도 없음)


def test_candidates_and_ignored_phrases(db, config):
    got = by_id(scope.select(db, config))
    cand = got["RAN1#126:10.5.2.3:001"]
    assert cand["scope"] == "candidate" and cand["topic"] == "srs" and cand["keywords"]
    assert "RAN1#126:10.5.4.3:001" not in got  # HARQ-ACK codebook만 있음


def test_manual_include_exclude(db, config):
    config = {**config, "include_ids": ["RAN1#126:10.8.9:001", "RAN1#999:1:001"],
              "exclude_ids": ["RAN1#126:10.5.3.1:002", "RAN1#126:10.5.2.3:001"]}
    sel = scope.select(db, config)
    got = by_id(sel)
    assert got["RAN1#126:10.8.9:001"]["scope"] == "manual"
    assert "RAN1#126:10.5.3.1:002" not in got and "RAN1#126:10.5.2.3:001" not in got
    assert sel["unknown_manual_ids"] == ["RAN1#999:1:001"]


def test_entries_sorted_by_meeting(db, config):
    sel = scope.select(db, config)
    meetings = [e["meeting"] for e in sel["entries"]]
    assert meetings == sorted(meetings, key=scope.meeting_sort_key)
    assert sel["meetings"] == ["RAN1#125", "RAN1#126"]


def test_unknown_topic_rejected(config):
    bad = {**config, "agendas": [{"section": "X", "path": ["Y"], "topic": "nope"}]}
    with pytest.raises(ValueError, match="알 수 없는 topic"):
        scope.Scope(bad)


def test_config_agendas_all_match_something(config):
    """설정의 포함 Agenda 제목이 정규화 후에도 유효한 형태인지 (빈 경로·중복 없음)."""
    sc = scope.Scope(config)
    keys = [(a["section"], tuple(a["path"])) for a in sc.agendas]
    assert len(keys) == len(set(keys)) and all(a["path"] for a in sc.agendas)
    assert [t["id"] for t in sc.topic_list()][-1] == "other"
