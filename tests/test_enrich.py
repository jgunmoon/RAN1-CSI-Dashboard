from scripts import enrich
from tests.conftest import entry


def _db(*tdocs):
    """tdocs: (회의, 폴더, 번호) — 근거 TDoc 링크가 있는 결정으로 회의별 번호 범위를 만듭니다."""
    entries, meetings = [], {}
    for i, (meeting, folder, n) in enumerate(tdocs):
        e = entry(f"{meeting}:9.2:{i:03}", meeting, [("9", "Release 20 NR"), ("9.2", "NR MIMO Phase 6")], "x")
        e["source"]["tdoc_url"] = f"https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/{folder}/Docs/R1-{n}.zip"
        entries.append(e)
        meetings[meeting] = {"ftp_dir": folder}
    return {"entries": entries, "meetings": meetings}


def test_tdoc_linker_ranges_and_gaps():
    db = _db(("RAN1#125", "TSGR1_125", 2603635), ("RAN1#125", "TSGR1_125", 2605125),
             ("RAN1#126", "TSGR1_126", 2605362), ("RAN1#126", "TSGR1_126", 2606883))
    L = enrich.TdocLinker(db)
    assert L.folder(2604000) == "TSGR1_125"                       # 범위 안
    assert L.folder(2605200, "RAN1#126") == "TSGR1_126"           # 빈 구간: 인용한 결정의 회의(뒤 회의)
    assert L.folder(2605200, "RAN1#125") == "TSGR1_125"           # 빈 구간: 인용한 결정의 회의(앞 회의)
    assert L.folder(2605200, "RAN1#124") == "TSGR1_125"           # 빈 구간, 무관한 회의 → 앞 회의(회의 중 늦게 등록)
    assert L.folder(2500001) is None                              # 알 수 없는 앞 번호
    assert L.url(2604000).endswith("/TSGR1_125/Docs/R1-2604000.zip")


def test_enrich_stage_impact_warn_clauses(config, db):
    en = enrich.Enricher(config, db)
    e = entry("RAN1#126:8.1:009", "RAN1#126", [("8", "Maintenance on Rel-19 NR and E-UTRA"), ("8.1", "Maintenance on others")],
              "The TP in R1-2606870 for TS 38.214 Clause 5.2.1.6 is endorsed.")
    x = en.enrich(e)
    assert x["stage"] == "maint" and x["clauses"] == ["TS 38.214 5.2.1.6"] and x["warn"] == ["tdoc"]
    fg = entry("RAN1#122:9.2:001", "RAN1#122", [("9", "Rel-19 UE Features"), ("9.2", "UE features for NR MIMO Phase 5")],
               "Adopt the following changes highlighted in chromatic fonts\n| 59. NR_MIMO_Ph5 | 59-2-1 | Up to 128 CSI-RS ports | UE capability |")
    x = en.enrich(fg)
    assert x["stage"] == "fg" and "color" in x["warn"] and {"capability", "dimension"} <= set(x["impact"])
    study = entry("RAN1#126:10.5.3.1:001", "RAN1#126", [("10", "Rel-20 Study of 6GR"), ("10.5.3.1", "Aspects of downlink-based CSI acquisition")],
                  "For PMI assumption on SGCS calculation of  and  ,support Rel-16 eType II CSI.")
    x = en.enrich(study)
    assert x["stage"] == "study" and x["warn"] == ["math"] and "measure" in x["impact"]
    wi = entry("RAN1#126:9.2:001", "RAN1#126", [("9", "Release 20 NR"), ("9.2", "NR MIMO Phase 6")], "Support X.")
    assert en.enrich(wi)["stage"] == "wi" and en.enrich(wi)["warn"] == []


def test_feature_groups_take_fg_from_second_cell():
    a = entry("RAN1#122:9.2:001", "RAN1#122", [("9", "Rel-19 UE Features")], "| 59. NR_MIMO_Ph5 | 59-2-1a | Old name | x |")
    b = entry("RAN1#122bis:9.2:001", "RAN1#122bis", [("9", "Rel-19 UE Features")],
              "| 59. NR_MIMO_Ph5 | 59-2-1a | New name | prerequisite 59-1-1 |\n| 59. NR_MIMO_Ph5 | 59-10-1 | Ten | y |")
    c = entry("RAN1#122bis:9.2:002", "RAN1#122bis", [("9", "Rel-19 UE Features")], "| 59. NR_MIMO_Ph5 | 59-2-1 | Base | z |")
    fgs = enrich.feature_groups([a, b, c])
    assert [f["id"] for f in fgs] == ["59-2-1", "59-2-1a", "59-10-1"]   # 숫자 순 (문자 접미사는 뒤)
    f = fgs[1]
    assert f["name"] == "New name" and f["ids"] == [a["id"], b["id"]]   # 이름은 가장 최근, 결정은 회의 순
    assert "59-1-1" not in [x["id"] for x in fgs]                       # 전제 조건 칸의 FG 번호는 목록에 넣지 않음


def test_ffs_followups_same_agenda_later_meeting_only():
    path = [("9", "Release 20 NR"), ("9.2", "NR MIMO Phase 6")]
    a = entry("RAN1#125:9.2:001", "RAN1#125", path, "Support early CSI.", ffs=["FFS: aperiodic CSI-RS triggering offset for SCell"])
    same = entry("RAN1#125:9.2:002", "RAN1#125", path, "Aperiodic CSI-RS triggering offset for SCell is 4 slots.")
    later = entry("RAN1#126:9.2:001", "RAN1#126", path, "The aperiodic CSI-RS triggering offset for SCell activation is 4 slots.")
    other = entry("RAN1#126:9.3:001", "RAN1#126", [("9", "Release 20 NR"), ("9.3", "Other")], "Aperiodic CSI-RS triggering offset SCell.")
    out = enrich.ffs_followups([a, same, later, other], key=lambda e: e["agenda_title"])
    assert out == [{"id": a["id"], "meeting": "RAN1#125", "line": "FFS: aperiodic CSI-RS triggering offset for SCell",
                    "followups": [later["id"]]}]
