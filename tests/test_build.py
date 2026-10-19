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
    assert "후보 1건" in srs


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
