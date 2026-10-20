import json
import re

import pytest

from scripts import build, source


def test_build_writes_reports(tmp_path, db, config):
    m = build.build(config, db, tmp_path)
    assert m["latest"] == "RAN1#126" and m["prev"] == "RAN1#125"
    html = (tmp_path / "index.html").read_text(encoding="utf-8")
    readme = (tmp_path / "README.md").read_text(encoding="utf-8")
    assert {p.name for p in (tmp_path / "by_topic").iterdir()} == {f"{t['id']}.md" for t in m["topics"]}

    # 결정 원문의 '</script>'가 스크립트 태그를 끝내지 않음
    blob = re.search(r'<script type="application/json" id="csi-data">(.*?)</script>', html, re.S).group(1)
    data = json.loads(blob)
    assert len(data["entries"]) == len(m["entries"])
    assert all(e["source"]["url"].startswith("https://") for e in data["entries"])
    # 기본 표시는 Agreement만, 후보는 꺼짐
    assert re.search(r'data-type value="Agreement" checked', html)
    assert not re.search(r'value="Working Assumption" checked', html)
    assert not re.search(r'id="g-cand" value="candidate" checked', html)
    assert "__CHECKED_AT__" in html  # Pages 게시 단계가 채우는 자리

    assert "직전 회의 대비 (RAN1#125 → RAN1#126)" in readme
    assert "RAN1#126는 '잠정'" in readme
    assert "```mermaid" in readme
    beam = (tmp_path / "by_topic" / "beam.md").read_text(encoding="utf-8")
    assert "Study unified TCI framework" in beam and "R1-2600001" in beam
    srs = (tmp_path / "by_topic" / "srs.md").read_text(encoding="utf-8")
    assert "후보 2건" in srs and "TS 38.214 6.2.1.4" not in srs.split("후보 2건")[0]
    csirs = (tmp_path / "by_topic" / "csirs.md").read_text(encoding="utf-8")
    assert "관련 결정 1건" in csirs and "Support aperiodic CSI reporting associated" in csirs
    assert "| 주된 주제 |" in readme and "관련 포함 |" in readme
    assert all("tags" in e for e in data["entries"])


def test_build_is_deterministic(tmp_path, db, config):
    build.build(config, db, tmp_path / "a")
    build.build(config, db, tmp_path / "b")
    for name in ("index.html", "README.md", "csi_decisions.json", "by_topic/report.md"):
        assert (tmp_path / "a" / name).read_bytes() == (tmp_path / "b" / name).read_bytes()


def test_source_url_uses_configured_branch(config):
    config = {**config, "source": {**config["source"], "branch": "main"}}
    assert source.db_url(config) == ("https://raw.githubusercontent.com/jgunmoon/RAN1-Decision-Tracker/main/"
                                     "data/agreements_db.json")


def test_source_check_rejects_unexpected_schema(db):
    with pytest.raises(ValueError, match="schema_version"):
        source.check({**db, "schema_version": 2})
    broken = {**db, "entries": [{**db["entries"][0], "source": {"doc": "x"}}]}
    with pytest.raises(ValueError, match="필수 필드"):
        source.check(broken)


def test_main_with_local_db(tmp_path, db, capsys):
    path = tmp_path / "db.json"
    path.write_text(json.dumps(db), encoding="utf-8")
    build.main(["--db", str(path), "--out", str(tmp_path / "out")])
    out = capsys.readouterr().out
    assert "확정" in out and (tmp_path / "out" / "index.html").exists()


def test_change_history_and_notification(tmp_path, db, config):
    import copy
    old = copy.deepcopy(db)
    old["updated_at"] = "2026-10-01T00:00:00+00:00"
    old["entries"] = [x for x in old["entries"] if x["meeting"] != "RAN1#126" and x["id"] != "RAN1#125:8.2.2:001"]
    note = tmp_path / "notify.md"
    build.build(config, old, tmp_path, now="2026-10-02T00:00+00:00", notify_file=note)
    assert json.loads((tmp_path / "changes.json").read_text(encoding="utf-8")) == [] and not note.exists()  # 첫 실행은 기준만

    m = build.build(config, db, tmp_path, now="2026-10-20T01:20+00:00", notify_file=note)
    hist = json.loads((tmp_path / "changes.json").read_text(encoding="utf-8"))
    assert len(hist) == 1 and hist[0]["new_meetings"][0]["meeting"] == "RAN1#126"
    assert [(x["id"], x["what"]) for x in hist[0]["items"]] == [("RAN1#125:8.2.2:001", "added")]
    body = note.read_text(encoding="utf-8")
    assert body.startswith("CSI 결정 업데이트: RAN1#126 신규") and "기존 회의 추가 1" in body.splitlines()[0]
    assert "RAN1#125:8.2.2:001" in body
    assert "최근 변경 이력" in (tmp_path / "README.md").read_text(encoding="utf-8")
    assert "변경 이력 추가 (원본 DB 갱신)" in build.summary(m)

    note.unlink()
    build.build(config, db, tmp_path, now="2026-10-21T01:20+00:00", notify_file=note)  # 같은 DB → 변화 없음
    assert len(json.loads((tmp_path / "changes.json").read_text(encoding="utf-8"))) == 1 and not note.exists()


def test_agenda_alerts_dropped_and_new(tmp_path, db, config):
    # #126의 Beam management 결정을 빼면, #125에 있던 포함 Agenda가 최신 회의에서 사라진 것으로 경고
    db = {**db, "entries": [x for x in db["entries"] if x["id"] != "RAN1#126:10.5.3.4:001"]}
    m = build.build(config, db, tmp_path)
    # 합성 DB의 AI/ML Case 0도 #125에만 결정이 있어 함께 잡힘
    assert [d["label"] for d in m["alerts"]["dropped"]] == [
        "Beam management for downlink and uplink", "AI/ML CSI compression Case 0 (Inference related aspects 등 하위 포함)"]
    new = {r["title"]: r for r in m["alerts"]["new"]}
    assert new["Uplink transmission scheme(s) for uplink channels"]["candidate"] == 1
    assert all(r["confirmed"] or r["candidate"] for r in m["alerts"]["new"])  # CSI 결정 없는 새 Agenda(ISAC 등)는 경고 안 함
    # 같은 회의의 ISAC 'Other aspects'(CSI 결정 없음)와 섞이지 않고, CSI 쪽만 1건으로 잡힘
    assert [(r["number"], r["total"]) for r in m["alerts"]["new"] if r["title"] == "Other aspects"] == [("10.5.3.3", 1)]
    summary = build.summary(m)
    assert "::warning::포함 Agenda 'Beam management for downlink and uplink'가 RAN1#125에는 1건" in summary
    html = (tmp_path / "index.html").read_text(encoding="utf-8")
    assert "Agenda 확인 필요 (RAN1#125 → RAN1#126)" in html


def test_regex_title_rules_match_future_agendas(config, db):
    from scripts import scope
    future = {**db["entries"][0], "id": "RAN1#130:9.4:001", "meeting": "RAN1#130", "agenda_item": "9.4",
              "agenda_path": [{"number": "9", "title": "Rel-20 UE Features"},
                              {"number": "9.4", "title": "UE features for NR MIMO Phase 6"}]}
    agenda, number = scope.Scope(config).match_agenda(future)
    assert agenda and agenda["label"] == "UE features for NR MIMO Phase N" and number == "9.4"
