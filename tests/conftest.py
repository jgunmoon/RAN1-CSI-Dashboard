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
MAINT = ("8", "Maintenance on Rel-19 NR and E-UTRA")


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
            # 여러 주제에 걸친 결정: 주된 주제는 규칙 순서상 CSI 보고, CSI-RS는 관련 주제
            entry("RAN1#126:10.5.3.1:004", "RAN1#126",
                  [SIXG, MAS, ("10.5.3", "CSI acquisition and report"), ("10.5.3.1", "Aspects of downlink-based CSI acquisition")],
                  "Support aperiodic CSI reporting associated with aperiodic NZP CSI-RS."),
            # 하위 포함 Agenda: #125는 하위 8.2.2, #126은 상위 8.2에 기록 → 번호 변경이 아님
            entry("RAN1#125:8.2.2:001", "RAN1#125",
                  [MAINT, ("8.2", "Maintenance on NR MIMO Phase 5"), ("8.2.2", "CSI enhancements")],
                  "The TP in R1-2505555 for TS 38.214 is endorsed."),
            entry("RAN1#126:8.2:001", "RAN1#126", [MAINT, ("8.2", "Maintenance on NR MIMO Phase 5")],
                  "The TP in R1-2606666 for TS 38.213 is endorsed."),
            # 통합 유지보수 Agenda: 기술 키워드 없이 조항 번호만 → 후보
            entry("RAN1#126:8.1:001", "RAN1#126", [MAINT, ("8.1", "Maintenance on AI/ML for NR Air interface, NR MIMO Phase 5, NES and NTN for NR and IoT")],
                  "The draft CR in R1-2607797 for Rel-19 TS38.214, Clause 5.2.2.5 is endorsed."),
            entry("RAN1#126:8.1:002", "RAN1#126", [MAINT, ("8.1", "Maintenance on AI/ML for NR Air interface, NR MIMO Phase 5, NES and NTN for NR and IoT")],
                  "Adopt the following TP in section 6.2.1.4, TS 38.214.\n| 6.2.1.4 ... TS38.214 5.1.6.1.2 is unchanged."),
            # 통합 유지보수 Agenda(require_keywords): CSI 키워드가 없는 RACH 결정은 확정에서 빠짐 (rootSequenceIndex-BFR은 BFR 아님)
            entry("RAN1#126:8.1:004", "RAN1#126", [MAINT, ("8.1", "Maintenance on AI/ML for NR Air interface, NR MIMO Phase 5,  NES and NTN for NR and IoT")],
                  "The following TP for TS 38.211 Clause 6.3.3.1 is endorsed: rootSequenceIndex-BFR is used."),
            entry("RAN1#126:8.1:005", "RAN1#126", [MAINT, ("8.1", "Maintenance on AI/ML for NR Air interface, NR MIMO Phase 5,  NES and NTN for NR and IoT")],
                  "If a UE multiplexes aperiodic CSI in a PUSCH, the UE follows clause 9."),
            # Rel-19 AI/ML UE features: positioning FG(58-2)는 exclude, CSI 예측 FG는 확정
            entry("RAN1#125:9.1:001", "RAN1#125", [("9", "Rel-19 UE Features"), ("9.1", "UE features for AI/ML for NR Air Interface")],
                  "Adopt the following changes\n| 58. NR_AIML_Air | 58-3-1 | CSI prediction | FFS: CPU/AIMLPU related information |"),
            entry("RAN1#125:9.1:002", "RAN1#125", [("9", "Rel-19 UE Features"), ("9.1", "UE features for AI/ML for NR Air Interface")],
                  "Introduce the following FGs\n| 58. NR_AIML_Air | 58-2-9 | DL PRS measurement for AI/ML positioning |"),
            # 단독 CSI 표현은 후보, SP-CSI-RNTI는 아님
            entry("RAN1#126:8.8:001", "RAN1#126", [MAINT, ("8.8", "Maintenance on others")],
                  "There is no consensus on the definition of CSI reference resource for LBCA."),
            entry("RAN1#126:8.8:002", "RAN1#126", [MAINT, ("8.8", "Maintenance on others")],
                  "For PUSCH scheduled by DCI scrambled with SP-CSI-RNTI, the valid symbol type is the first symbol."),
            # TDoc 안의 절, CSI와 무관한 조항, 38.213 6.x 오인용은 후보가 아님
            entry("RAN1#126:8.1:003", "RAN1#126", [MAINT, ("8.1", "Maintenance on AI/ML for NR Air interface, NR MIMO Phase 5, NES and NTN for NR and IoT")],
                  "Proposal 1 in Section 5.2 of R1-2608699 for Rel-19 TS38.213 Clause 4.1 is endorsed.\n"
                  "Adopt the following TPs in principle to Clause 6.3.2.4.1.1, TS 38.213."),
        ],
    }
