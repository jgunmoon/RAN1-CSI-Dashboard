import pytest

from scripts.build import load_config


def entry(id_, meeting, path, text, type_="Agreement", ffs=()):
    """path: [(번호, 제목), ...] 최상위부터."""
    return {
        "id": id_, "meeting": meeting, "agenda_item": path[-1][0], "agenda_title": path[-1][1],
        "agenda_path": [{"number": n, "title": t} for n, t in path], "type": type_, "text": text, "ffs": list(ffs),
        "source": {"doc": f"Chair notes {meeting}_eom", "kind": "chairman_note",
                   "url": f"https://www.3gpp.org/ftp/x/{meeting.replace('#', '%23')}.docx",
                   "tdoc": "R1-2600001", "tdoc_url": "https://www.3gpp.org/ftp/x/R1-2600001.zip"},
    }


SIXG = ("10", "Rel-20 Study of 6GR")
MAS = ("10.5", "Multi-antenna system")


@pytest.fixture
def config():
    return load_config()


@pytest.fixture
def db():
    return {
        "schema_version": 1,
        "updated_at": "2026-10-19T11:12:42+00:00",
        "meetings": {"RAN1#125": {}, "RAN1#126": {"provisional": {"doc": "Draft Chair notes RAN1#126_v03.docx", "reason": "x"}}},
        "entries": [
            # 6GR Beam management: #125는 MIMO operation 아래 10.5.2.4, #126은 CSI acquisition and report 아래 10.5.3.4
            entry("RAN1#125:10.5.2.4:001", "RAN1#125",
                  [SIXG, MAS, ("10.5.2", "MIMO operation"), ("10.5.2.4", "Beam management for downlink and uplink")],
                  "Study unified TCI framework for 6GR."),
            entry("RAN1#126:10.5.3.4:001", "RAN1#126",
                  [SIXG, MAS, ("10.5.3", "CSI acquisition and report"), ("10.5.3.4", "Beam management for downlink and uplink")],
                  "Support beam reporting with SRS-based measurement.", ffs=["FFS: details"]),
            # DL CSI: 주제는 키워드로
            entry("RAN1#126:10.5.3.1:001", "RAN1#126",
                  [SIXG, MAS, ("10.5.3", "CSI acquisition and report"), ("10.5.3.1", "Aspects of downlink-based CSI acquisition")],
                  "Support Type-II codebook with PMI reporting.", type_="Working Assumption"),
            entry("RAN1#126:10.5.3.1:002", "RAN1#126",
                  [SIXG, MAS, ("10.5.3", "CSI acquisition and report"), ("10.5.3.1", "Aspects of downlink-based CSI acquisition")],
                  "Study NZP CSI-RS port aggregation."),
            entry("RAN1#126:10.5.3.1:003", "RAN1#126",
                  [SIXG, MAS, ("10.5.3", "CSI acquisition and report"), ("10.5.3.1", "Aspects of downlink-based CSI acquisition")],
                  "Adopt the evaluation assumptions in the table.", type_="Conclusion"),
            # CSI acquisition and report > Other aspects (포함) vs 다른 'Other aspects' (불포함)
            entry("RAN1#126:10.5.3.3:001", "RAN1#126",
                  [SIXG, MAS, ("10.5.3", "CSI acquisition and report"), ("10.5.3.3", "Other aspects")],
                  "Study TRS design."),
            entry("RAN1#126:10.8.9:001", "RAN1#126", [SIXG, ("10.8", "ISAC"), ("10.8.9", "Other aspects")],
                  "Study sensing waveform."),
            # HARQ-ACK codebook은 CSI 키워드가 아님
            entry("RAN1#126:10.5.4.3:001", "RAN1#126",
                  [SIXG, MAS, ("10.5.4", "Downlink control channel, scheduling and HARQ operation"), ("10.5.4.3", "HARQ related Aspects")],
                  "Support Type-2 HARQ-ACK codebook and HARQ-ACK codebook for multi-PDSCH."),
            # 키워드 후보 (포함 Agenda 밖)
            entry("RAN1#126:10.5.2.3:001", "RAN1#126",
                  [SIXG, MAS, ("10.5.2", "MIMO operation"), ("10.5.2.3", "Uplink transmission scheme(s) for uplink channels")],
                  "Support SRS for codebook based UL transmission."),
            # 하위 포함(children): AI/ML CSI compression > Inference related aspects
            entry("RAN1#125:9.1.1.1:001", "RAN1#125",
                  [("9", "Release 20 NR"), ("9.1", "Artificial Intelligence (AI)/Machine Learning (ML) for NR air interface enhancements"),
                   ("9.1.1", "CSI spatial/frequency compression without temporal aspects (“Case 0”)"), ("9.1.1.1", "Inference related aspects")],
                  "Support CSI report via two-sided model."),
            # NR MIMO Phase 6 상위 Agenda는 포함, 목록에 없는 하위 Agenda는 불포함
            entry("RAN1#126:9.2:001", "RAN1#126", [("9", "Release 20 NR"), ("9.2", "NR MIMO Phase 6")],
                  "Support aperiodic SRS trigger in MSG4."),
            entry("RAN1#126:9.2.9:001", "RAN1#126", [("9", "Release 20 NR"), ("9.2", "NR MIMO Phase 6"), ("9.2.9", "Something new")],
                  "Study a new feature </script> <!-- x."),
        ],
    }
