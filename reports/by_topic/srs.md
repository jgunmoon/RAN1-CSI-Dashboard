# SRS — RAN1 CSI 결정

> 원본 DB 마지막 업데이트 **2026-10-19 20:12 KST** · [요약으로 돌아가기](../README.md)

주된 주제가 SRS인 확정 178건 (Agreement 166 · WA 1 · Conclusion 11), 후보 56건. 결정 본문은 Chair notes 원문 그대로입니다(요약 없음). 최신 회의부터 보여줍니다.
주된 주제가 다른 결정 중 이 주제가 관련 주제로 붙은 것은 맨 아래 '관련 결정'에 모았습니다.

## RAN1#126bis — 25건

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#126bis:9.2:002` · 🆕 신규 · 관련 주제: CSI 보고/codebook, CSI-RS

> The first slot as the reference slot in the following agreement is determined based on the numerology of the SCell where the aperiodic SRS/CSI-RS is located.
> | Agreement: To determine the transmission/reception slot of the DL/UL signalling triggered/scheduled based on a legacy SCell activation command (i.e., aperiodic SRS-AS, aperiodic CSI-RS and the PUSCH scheduled for aperiodic CSI reporting), for applying a slot offset between a reference slot and a transmission/reception slot of the DL/UL signalling triggered/scheduled based on the legacy SCell activation command, the reference slot is the first slot that is 3ms after UE transmits HARQ-ACK for the PDSCH carrying the SCell activation command |

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · [R1-2607052](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2607052.zip) · `[126bis-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#126bis:9.2:003` · 🆕 신규 · 관련 주제: CSI 보고/codebook, CSI-RS

> Support a per-cell new RRC parameter to disable/enable Rel-20 early SRS triggering for a SCell switching out of dormancy
> - FFS: Whether the same RRC parameter is also used to disable/enable Rel-20 early CSI/CSI-RS triggering for the SCell

남은 FFS 1건

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · [R1-2607052](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2607052.zip) · `[126bis-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#126bis:9.2:005` · 🆕 신규 · 관련 주제: CSI 보고/codebook, CSI-RS

> For early aperiodic SRS/CSI/CSI-RS triggered via SCell activation command or DCI indicating switching out of dormancy, support the followings only:
> - Rel-15 SRS antenna switching pattern (i.e., 1T1R, 1T2R, 1T4R, 2T2R, 2T4R, and 4T4R) for aperiodic SRS-AS
> - Up to 32 CSI-RS ports for aperiodic CSI-RS associated with aperiodic CSI reporting

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · [R1-2607054](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2607054.zip) · `[126bis-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#126bis:9.2:006` · 🆕 신규 · 관련 주제: CSI 보고/codebook, CSI-RS

> To determine the transmission/reception slot of the DL/UL signalling triggered/scheduled via the DCI indicating switching out of SCell dormancy  (i.e., aperiodic SRS-AS, aperiodic CSI-RS and the PUSCH scheduled for aperiodic CSI reporting), for applying a slot offset between a reference slot and a transmission/reception slot of the DL/UL signalling triggered/scheduled via the DCI indicating switching out of SCell dormancy, the reference slot is the first slot after BWP switching to non-dormant BWP is completed.

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · [R1-2607055](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2607055.zip) · `[126bis-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#126bis:9.2:007` · 🆕 신규 · 관련 주제: CSI 보고/codebook, CSI-RS

> MSG4-triggered CSI/TRS/SRS must be in the initial BWP.

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · [R1-2607055](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2607055.zip) · `[126bis-R20-MIMO]`

**Conclusion** · `9.2` NR MIMO Phase 6 · `RAN1#126bis:9.2:008` · 🆕 신규 · 관련 주제: CSI 보고/codebook, CSI-RS

> There is no consensus to support Rel-20 early CSI/SRS/CSI-RS for the case that BWP switching is configured in RRCSetup/RRCResume message contained in MSG4 PDSCH.

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · [R1-2607055](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2607055.zip) · `[126bis-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#126bis:9.2:009` · 🆕 신규

> For PF = K (i.e., PF = 2, K = 2 and PF = 4, K = 4):
> - Simultaneous enabling of (i)pseudo-random RPFS start RB hopping across different SRS frequency hopping period groups and (ii)Rel-17 deterministic RPFS start RB hopping is not supported.

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · [R1-2607397](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2607397.zip) · `[126bis-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#126bis:9.2:010` · 🆕 신규

> When the parameter hoppingWithRepetition is set to repetition, for a repetition spanning two consecutive slots within a cross-slot SRS resource
> - It is concluded that no spec change is needed (i.e., legacy equation is used without update).
>   - Note: Comb offset hopping of cross-slot SRS is applied across the slot boundaries.
>   - Note: Comb offset value may change at slot boundaries for cross-slot SRS repetition.

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · [R1-2607398](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2607398.zip) · `[126bis-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#126bis:9.2:011` · 🆕 신규

> Regarding the RPFS start RB index hopping across multiple legacy SRS frequency hopping periods determined by pseudo-random sequence for intra-repetition hopping, the following is supported by RRC configuraiton:
>   - For , available start RB indexes can be configured by a bitmap as a subset of {0, 1, 2, 3}
>     - If the bitmap is not configured,
>   - For PF = 2 (i.e., PF = K = 2),

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · [R1-2607398](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2607398.zip) · `[126bis-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#126bis:9.2:012` · 🆕 신규

> Regarding the RPFS start RB index hopping across multiple legacy SRS frequency hopping periods determined by pseudo-random sequence for intra-repetition hopping with ,
> - Hopping granularity  can be configured as 1 or 2 adjacent frequency hopping period(s)

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · [R1-2607398](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2607398.zip) · `[126bis-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#126bis:9.2:013` · 🆕 신규

> For PF = K (i.e., PF = 2, K = 2 and PF = 4, K = 4), update  as follows:
>   - is given by the following table, wherein  when pseudo-random RPFS start RB hopping across different SRS frequency hopping period groups is enabled and Rel-17 deterministic RPFS start RB hopping is not enabled;  when pseudo-random RPFS start RB hopping across different SRS frequency hopping period groups is not enabled and Rel-17 deterministic RPFS start RB hopping is enabled
> The quantity  as a function of
> |  |  |  |  |
> |  | = K = 2 | = 4 and K =2 | = K = 4 |
> | 0 | 0 | 0 | 0 |
> | 1 | 1 | 1 | 2 |
> | 2 | - | - | 1 |
> | 3 | - | - | 3 |

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · [R1-2607398](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2607398.zip) · `[126bis-R20-MIMO]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126bis:10.5.3.1:013` · 🆕 신규 · 관련 주제: CSI 보고/codebook, CSI-RS

> For the study/evaluation of early CSI triggering/reporting, the following is considered:
> - CSI-RS based CSI reporting
>   - Companies to report the report quantity(ies), e.g., RI/PMI/CQI, wideband or subband CSI
>   - Companies to report the CSI-RS assumption, e.g., periodic or aperiodic CSI-RS
> - DMRS based CSI reporting at least for the use cases UE transition from RRC_IDLE/RRC_INACTIVE to RRC_CONNECTED, and RRC_CONNECTED mode mobility
>   - Companies to report the report quantity(ies), e.g., CQI
>   - Companies to report the DMRS assumption, e.g., whether the DMRS used for channel measurement is the Msg2 DMRS
> - Benchmark: UE transition from RRC_IDLE/RRC_INACTIVE to RRC_CONNECTED, activation of serving cells/carriers, or RRC_CONNECTED mode mobility, without early CSI reporting (e.g., SSB-based, when applicable)
> - KPI: UPT/latency/interruption time/packet loss/coverage during the time period in which the early CSI is utilized
>   - Companies report the appliable KPI for the use case
> - Companies to report when to report of the early CSI /reporting
> - Companies report the traffic/load assumption for each scenario
> - Note: the evaluation on SRS triggering for early CSI acquisition is to be handled in 10.5.3.2.

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#126bis:10.5.3.2:001` · 🆕 신규

> For multiplexing of SRS ports per resource,
> - Cyclic-shift (CS) based port is supported without TDM multiplexing for 2-, 3-, 4- and 8-port SRS
> - Comb-based port multiplexing is supported without TDM multiplexing for 3-, 4- and 8-port SRS
> - FFS the necessity of TDM multiplexing of cyclic-shift (CS) based port and comb-based port for supporting different number of SRS ports

남은 FFS 1건

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#126bis:10.5.3.2:002` · 🆕 신규

> For xTyR antenna switching SRS in 6GR,
> - Prioritize cases where y/x=integer
> - At least the combinations of x and y as supported in NR shall be supported

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#126bis:10.5.3.2:003` · 🆕 신규

> For 6GR, support SRS resource sets, each with one or multiple SRS resources.
> - An SRS resource can be associated with multiple SRS resource sets.
> - At least for the following SRS parameters, study whether each parameter shall be common to all SRS resources within the same SRS resource set or resource-specific:
>   - Time domain behavior (i.e., aperiodic, periodic and semi-persistent)
>   - Number of ports per SRS resource
>   - Usage type
>   - Power control related parameters

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#126bis:10.5.3.2:004` · 🆕 신규

> Study the following combinations of comb value and cyclic shift for comb values less than or equal to 8 (assuming the minimum bandwidth = 4 PRBs for SRS in 6GR)
> - The maximum number of cyclic shifts up to 24 for comb-2
> - The maximum number of cyclic shifts up to 12 for comb-4
> - The maximum number of cyclic shifts up to 6 for comb-8

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#126bis:10.5.3.2:005` · 🆕 신규 · 관련 주제: CSI 보고/codebook

> Study at least the following aspects of TD-OCC:
> - Candidate covering codes: e.g., Hadamard code, and non-Hadamard codes such as DFT code.
> - How to design TD-OCC to support all repetition factors.
> - The performance under partial dropping, and the feasibility of retaining orthogonality-preserved SRS ports under partial dropping, instead of dropping all ports. That is, only the SRS ports that lose orthogonality due to the dropped symbol(s) are discarded, while the remaining SRS ports that can still maintain orthogonality using the surviving symbols are retained for CSI acquisition.
> - TD-OCC hopping for interference randomization

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#126bis:10.5.3.2:006` · 🆕 신규

> For the evaluation of 6GR SRS sequence designs, adopt the following for PAPR/IAPR/CM and XC calculations of baseline NR sequences
> - CP is not taken into account
> - value of v and number of sequences
> - Alt 1: v=0 and 1, all 60 sequences
>   - All combinations from v=0 and 1 between different sequence groups (u) are measured for XC.
>   - XC between v=0 and 1 within a sequence group (u) are not measured.
> - Alt 2: v=0, 30 sequences
> - IFFT size=8L, where L is the total length considering sequence length and comb structure.
> - E.g. Msc=96 and comb2 => L=192 (96*2)
> - Consider Comb=2 only
> - Adding an NR baseline column to the template for evaluation results collection
> XC is measured over all delay lags in over sampling domain

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#126bis:10.5.3.2:007` · 🆕 신규

> Study the following combinations of  comb value and cyclic shift for comb values greater than 8 (assuming the following minimum SRS bandwidths for each comb value), including feasibility
> - For comb-16,
>   - Option 1: Assuming the minimum bandwidth =8 RBs, CS lengths up to 6 [or 4 or 3]
>   - Option 2: No cyclic shift applied.
>   - Option 3: Assuming the minimum bandwidth =40 RBs, CS lengths up to 6 [or 4 or 3]
> - For comb-12,
>   - Option 1: Assuming the minimum bandwidth =8 RBs, CS lengths up to 8 [or 6 or 4]
>   - Option 2: Assuming the minimum bandwidth =6 RBs, CS lengths up to 6 [or 4 or 3]
>   - Option 3: Assuming the minimum bandwidth =4 RBs, CS lengths up to 4 [or 3]
>   - Option 4: No cyclic shift applied.
>   - Option 5: Assuming the minimum bandwidth =32 RBs, CS lengths up to 8 [or 6 or 4]
> - other values of min SRS BW can be reported

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#126bis:10.5.3.2:008` · 🆕 신규

> Two-level frequency hopping of 6GR SRS, study the following hopping patterns for each level:
> - First level: hopping over BW with one or multiple frequency hops
>   - Option 1: SRS subband nested tree-like frequency hopping pattern as in NR
>   - Option 2: Hopping pattern defined by RB offsets which are derived based on NW indication, details of NW indication is FFS
>   - Option 3: Sequential hopping patterns
> - Second level: hopping within each frequency hop of the first-level hopping
>   - Option 1: SRS subband nested tree-like frequency hopping pattern as in NR
>   - Option 2: Partial SRS subband sounding with/without intra-repetition hopping (with PF=2 and 4 as baseline)
> ◦            FFS: PF beyond the NR Rel-17 values, e.g., 8 and 16
>   - Option 3: Subband or partial SRS subband Sequential hopping patterns
> Note: this does not mean that two-level hopping is supported and single-level hopping is precluded.

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#126bis:10.5.3.2:009` · 🆕 신규

> For the evaluation of 6GR SRS sequence designs, adopt the following for PAPR/IAPR/CM and XC calculations of sequences,
> - FFT size=max(8192, 8*sequence length*Comb size).

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#126bis:10.5.3.2:010` · 🆕 신규

> For evaluation of 6GR SRS sequence designs, adopt the following assumption on XC calculations for sequences of the same length
> - XC is measured in time domain over all delay lags
> - For M number of sequences of the same length, frequency-domain overlapping assumption 1(full overlapping) is used
> - The magnitude of normalized periodic cross-correlation between distinct sequences  and  at shift   (where ) is computed as
> where
> - Paring of M sequences of the same length, M(M-1)/2 pairs in total are taken into account
> - For each pair of sequences, the cross-correlation metric is defined as the maximum value of the normalized delay cross-correlation spectrum
> - For M sequences of the same length, collect the mean values of the normalized delay cross-correlation spectrum for all pairs and derive the following statistics: maximum, average, CDF@10%, 50%, 90%.

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#126bis:10.5.3.2:011` · 🆕 신규

> For evaluation of 6GR SRS sequence designs, adopt the following assumption on XC calculations for sequences with lengths
> - The position of the desired SRS(victim) sliding in the granularity of 1 RB level within the range of the interfering SRS.

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#126bis:10.5.3.2:012` · 🆕 신규 · 관련 주제: AI/ML CSI, CSI 보고/codebook

> For the study of AI based receiver for SRS overhead reduction, the following template is used as a starting point to collect companies’ results via LLS:
> | Parameters | Value |
> | #1 sub-case | AI/ML for low-overhead SRS (Sub-Case A): low-overhead SRS with AI/ML at the network side for CSI reconstruction Note: low-overhead SRS may include overhead reduction schemes in the time and/or frequency domains. |
> | #2 Model input | Reported by company, including input content and input dimension |
> | #3 Model output | Reported by company, including output content and output dimension |
> | #4 Label | If applicable, reported by company, including label acquisition method and label error (e.g., zero for ideal label, or non-zero for realistic label) (Labelling error model can be reported optionally) (Cost function can be reported optionally) |
> | #5 Training type | Offline |
> | #6 Number of SRS ports | Reported by company |
> | #7 Number of FLOPs (for receiver block replaced by AIML model) | Reported by company Company also reports inference related parameters for SRS (e.g., number of RBs, symbols, SRS ports) |
> | [#7-1 Number of FLOPs (for receiver block not replaced by AIML model)] | Number of FLOPs of non-AI receiver blocks corresponding to the candidate receiver assumption(s) in #1 can be reported by company (optional). (if reported, companies to report how to calculate Number of FLOPs of non-AI receiver blocks as well) Note: Non-AI receiver blocks can be: channel estimation, channel interpolation. (FLOPs of additional pre/post processing can be reported optionally, if any) |
> | #8 Number of parameters of AI Model | Reported by company (Backbone of AI model can be reported optionally) |
> | #9 Benchmark | Receiver: non-AI based receiver with realistic assumption The candidate benchmarks can be set as follow: Benchmark 1: Same candidate pattern of overhead-reduced SRS for sub-case-A (e.g., SRS with reduced overhead in the time and/or frequency domains) Benchmark 2: Non-overhead-reduced SRS pattern Note: For sub-case A, companies report at least one of two Benchmarks with the correspondent complexity. Note: Companies to optionally report an approximate upper bound in performance, e.g. using ideal channel information, when reporting evaluation results. |
> | #9-1 SRS assumption for AI receiver | reported by company |
> | #10 Aspects to consider for generalization and scalability performance | Evaluation Methodologies & Frameworks Evaluation cases 1, 2, 3 in TR 38.843 Case 1: The AI model is trained based on training dataset from one Scenario #A/Configuration #A, and then the AI model performs inference/test on a dataset from the same Scenario #A/Configuration #A. Case 2: The AI model is trained based on training dataset from one Scenario #A/Configuration #A, and then the AI model performs inference/test on a different dataset than Scenario #A/Configuration #A, e.g., Scenario #B/Configuration #B, Scenario #A/Configuration #B. Case 3: The AI model is trained based on training dataset constructed by mixing datasets from multiple scenarios/configurations including Scenario #A/Configuration #A and a different dataset than Scenario #A/Configuration #A, e.g., Scenario #B/Configuration #B, Scenario #A/Configuration #B, and then the AI model performs inference/test on a dataset from a single Scenario/Configuration from the multiple scenarios/configurations, e.g., Scenario #A/Configuration #A, Scenario #B/Configuration #B, Scenario #A/Configuration #B. Companies to report the scenarios/configurations for generalization and scalability verification, e.g., Scenario #A/Configuration #A Scenario #B/Configuration #B Generalization case Dataset mixing method (for Case 3) Note: Companies to highlight the parameter(s) to vary for generalization analysis Channel generation: considering Link Level channel and/or System Level channel (e.g., UMi, UMa) Link Level channel, if used for generating training data, shall be generated with diversified Channel & Environmental Conditions Companies can also use System Level channel to generate training data set Channel & Environmental Conditions Various Channel Types Various Channel parameters, such as various Delay Spread, various Doppler spread, various Angular Distributions Various UE speed Various SNR/SINR range Various interference level FFS: how to model interference in LLS Scheduling & System Configurations Various antenna configurations, e.g., SRS ports, UE Tx port number, UE Tx port layout, number of gNB Rx antennas Various time/frequency domain factors, e.g., various frequency allocations / RPFS / hopping patterns, various time domain allocations, various SRS bandwidth Other aspect, e.g., power of SRS transmission Other aspects are not precluded, and reported by company (if needed) |
> | #11a (Without considering generalization and scalability) parameters for inference | Reported by company, considering the following aspects aNB antenna configuration UE antenna configuration Channel type Delay spread UE speed SNR range Other aspects are not precluded, and reported by company (if needed) |
> | #11b-1 SNR gain at BLER target | Reported by company Note: Companies should also report the corresponding benchmark. Note: Gain in terms of SNR at the BLER target of PUSCH or PDSCH (i.e., 10%) based on UL/DL CSI acquisition from SRS |
> | #11b-2 Tput gain | Reported by company Note: Companies should also report the corresponding benchmark. Note: Gain in terms of Tput of PUSCH or PDSCH based on UL/DL CSI acquisition from SRS |
> | #11b-3 NMSE/SGCS gain | Reported by company (optional) Note: Companies should also report the corresponding benchmark. Note: NMSE is evaluated on the channel estimation/interpolation output of the SRS receiver. Note: SGCS can be evaluated on the estimated channel and/or on the selected precoder (precoder SGCS). |

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.3` Other aspects · `RAN1#126bis:10.5.3.3:006` · 🆕 신규

> Study and evaluate the following assistance information for sub use case 1C
> - Option 1: Precoding matrix information with NW-sided model for fusing
>   - ompanies report the details
> - Option 2: Explicit channel matrix information with NW-sided model for fusing
>   - Companies report the details
> - The precoding matrix or channel matrix may correspond all the Rx/Tx ports or partial Rx/Tx ports
> - FFS: Whether to report the association between SRS ports and the corresponding parts of the reported assistance information

남은 FFS 1건

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Other Aspects related to CSI]`

## RAN1#126 — 27건

**Agreement** · `8.1` Maintenance on AI/ML for NR Air interface, NR MIMO Phase 5,  NES and NTN for NR and IoT · `RAN1#126:8.1:003` · 관련 주제: Beam management, CSI 보고/codebook

> The following TP for TS 38.214 Clause 6.2.1.3 is endorsed.
> The corresponding CR for Rel-19, TS 38.214 Clause 6.2.1.3 in R1-2606870 is endorsed.
> | Reason for change | 1. When the collision between the SRS for carrier switching and the CSI report happens, UE should follow a priority rule defined. However, the priority rule for the SRS and CSI-PAI report is unclear. 2. To ensure consistent priority rule for two types of PAI reports, i.e., CSI-PAI report and RS-PAI report. |
> | Summary of change | 1. Reuse the same dropping rule for collision handling between PMI and SRS for the collision handling between CSI-PAI and SRS 2. Revert following agreement made in RAN1#122bis, and apply the same priority rules to collision between RS-PAI and SRS as to collision between CSI-PAI and SRS. |
> | Consequences if not approved | 1. The collision handling between the SRS for carrier switching and the CSI-PAI report is unclear 2. Inconsistency in collision handling between CSI-PAI/SRS and RS-PAI/SRS. |
> | 6.2.1.3 UE sounding procedure between component carriers ============================= unchanged parts are omitted ============================ The following prioritization rules shall be applied in case of collision between a transmission of SRS over carrier and transmission of a physical signal/channel over a carrier of a serving cell in set - the UE shall not transmit SRS whenever SRS transmission (including any interruption due to uplink or downlink RF retuning time [11, TS 38.133] as defined by higher layer parameters switchingTimeUL and switchingTimeDL of SRS-SwitchingTimeNR) on the carrier of the serving cell and PUSCH/PUCCH transmission carrying HARQ-ACK/positive SR/RI/CRI/SSBRI/UEIRI/P-CRI/P-SSBRI/RS-PAI and/or PRACH on a carrier of a serving cell in set happen to overlap in the same symbol - the UE shall not transmit a periodic/semi-persistent SRS whenever periodic/semi-persistent SRS transmission (including any interruption due to uplink or downlink RF retuning time [11, TS 38.133] as defined by higher layer parameters switchingTimeUL and switchingTimeDL of SRS-SwitchingTimeNR) on the carrier of the serving cell and PUSCH transmission carrying aperiodic CSI on a carrier of a serving cell in set happen to overlap in the same symbol - the UE shall drop PUCCH/PUSCH transmission carrying periodic/semi-persistent CSI comprising only CQI/PMI/L1-RSRP/L1-SINR/P-L1-RSRP/CSI-PAI/RS-PAI and/or Type 1 configured grant PUSCH transmission carrying UE initiated CSI report, and/or SRS transmission on a carrier of a serving cell in set configured for PUSCH/PUCCH transmission whenever the transmission and SRS transmission (including any interruption due to uplink or downlink RF retuning time [11, TS 38.133] as defined by higher layer parameters switchingTimeUL and switchingTimeDL of SRS-SwitchingTimeNR) on the carrier of the serving cell happen to overlap in the same symbol - the UE shall drop PUSCH transmission carrying aperiodic CSI comprising only CQI/PMI/L1-RSRP/L1-SINR/TDCP/cjtc-Dd/cjtc-F/cjtc-Dd-F/cjtc-P/P-L1-RSRP/CSI-PAI/RS-PAI on a carrier of a serving cell in set whenever the transmission and aperiodic SRS transmission (including any interruption due to uplink or downlink RF retuning time [11, TS 38.133]) as defined by higher layer parameters switchingTimeUL and switchingTimeDL of SRS-SwitchingTimeNR) on the carrier of the serving cell happen to overlap in the same symbol. ============================= unchanged parts are omitted ============================ |

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606795](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606795.zip) · `[126-R19-AI 8.1]`

**Agreement** · `8.1` Maintenance on AI/ML for NR Air interface, NR MIMO Phase 5,  NES and NTN for NR and IoT · `RAN1#126:8.1:013` · 관련 주제: Beam management, CSI 보고/codebook, CSI-RS

> The following TP for TS 38.213 Clause 11.1 is endorsed.
> The corresponding CR for Rel-19, TS 38.213 in R1-2606850 is endorsed.
> | Reason for change: The slot configuration for on demand SIB1 is unclear due to missing IE sib1-tdd-UL-DL-ConfigurationCommon. Summary of change: Add missing IE sib1-tdd-UL-DL-ConfigurationCommon for slot configuration for on demand SIB1. The SSB symbols indicated by OD-SIB1-Config cannot be indicated as uplink by sib1-tdd-UL-DL-ConfigurationCommon, and the PRACH symbols indicated by OD-SIB1-Config cannot be indicated as downlink by sib1-tdd-UL-DL-ConfigurationCommon. Consequence if not approved: Ambiguity occurs for the slot configuration for on demand SIB1. 11.1 Slot configuration A slot format includes downlink symbols, uplink symbols, and flexible symbols. The following are applicable for each serving cell. If a UE is provided tdd-UL-DL-ConfigurationCommon, the UE sets the slot format per slot over a number of slots as indicated by tdd-UL-DL-ConfigurationCommon. The tdd-UL-DL-ConfigurationCommon provides - a reference SCS configuration by referenceSubcarrierSpacing - a pattern1. The pattern1 provides - a slot configuration period of msec by dl-UL-TransmissionPeriodicity - a number of slots with only downlink symbols by nrofDownlinkSlots - a number of downlink symbols by nrofDownlinkSymbols - a number of slots with only uplink symbols by nrofUplinkSlots - a number of uplink symbols by nrofUplinkSymbols A value msec is valid only for , . A value msec is valid only for , . A value msec is valid only for,. A value msec is valid only for , or . A slot configuration period of msec includes slots with SCS configuration . From the slots, a first slots include only downlink symbols and a last slots include only uplink symbols. The symbols after the first slots are downlink symbols. The symbols before the last slots are uplink symbols. The remaining are flexible symbols. The first symbol every periods is a first symbol in an even frame. If tdd-UL-DL-ConfigurationCommon provides both pattern1 and pattern2, the UE sets the slot format per slot over a first number of slots as indicated by pattern1 and the UE sets the slot format per slot over a second number of slots as indicated by pattern2. The pattern2 provides - a slot configuration period of msec by dl-UL-TransmissionPeriodicity - a number of slots with only downlink symbols by nrofDownlinkSlots - a number of downlink symbols by nrofDownlinkSymbols - a number of slots with only uplink symbols by nrofUplinkSlots - a number of uplink symbols by nrofUplinkSymbols The applicable values of are same as the applicable values for . A slot configuration period of msec includes first slots and second slots. From the slots, a first slots include only downlink symbols and a last include only uplink symbols. The symbols after the first slots are downlink symbols. The symbols before the last slots are uplink symbols. The remaining are flexible symbols. A UE expects that divides 20 msec. The first symbol every periods is a first symbol in an even frame. A UE expects that the reference SCS configuration is smaller than or equal to a SCS configuration for any configured DL BWP or UL BWP. Each slot provided by pattern1 or pattern2 is applicable to consecutive slots in the active DL BWP or the active UL BWP where the first slot starts at a same time as a first slot for the reference SCS configuration and each downlink or flexible or uplink symbol for the reference SCS configuration corresponds to consecutive downlink or flexible or uplink symbols for the SCS configuration . A downlink or flexible symbol provided by tdd-UL-DL-ConfigurationCommon can include an UL sub-band provided by ul-SubbandlocationAndBandwidth, a first DL sub-band provided by firstDL-SubbandlocationAndBandwidth and may additionally include a second DL sub-band provided by secondDL-SubbandlocationAndBandwidth, for a SCS configuration of any configured UL BWP or DL BWP, respectively, as provided by scs-SpecificCarrierList [4, TS 38.211]. The downlink or flexible symbol is then referred to as an SBFD symbol; otherwise, it is referred to as a non-SBFD symbol. Unless otherwise stated, the UE considers symbols in a slot indicated as downlink and as SBFD by tdd-UL-DL-ConfigurationCommon to be available for transmissions. Uplink symbols by tdd-UL-DL-ConfigurationCommon are non-SBFD symbols. An SBFD symbol or a non-SBFD symbol provided by tdd-UL-DL-ConfigurationCommon cannot change to a non-SBFD symbol or to an SBFD symbol, respectively, by other information. The UE is not provided coresetPoolIndex and is not configured to receive PDSCH according to more than one TCI states mapped to one TCI codepoint [6, TS 38.214] for a serving cell where the UE is provided SBFD symbols. For a PUCCH or a PUSCH transmission in flexible symbols indicated as SBFD by tdd-UL-DL-ConfigurationCommon and associated with PRACH transmission in first PRACH occasions, the UE assumes the flexible symbols as non-SBFD symbols in this RACH attempt. The frequency location of an UL sub-band, or a first DL sub-band, or a second DL sub-band, starts at RB and includes a number of contiguous RBs provided by ul-SubbandlocationAndBandwidth, or firstDL-SubbandlocationAndBandwidth or secondDL-SubbandlocationAndBandwidth, respectively, that indicates an offset and a length as RIV according to [6, TS 38.214], setting , and a value provided by offsetToCarrier for the subcarrierSpacing. SBFD symbols are consecutive, start from a first slot provided by SBFD-StartingSlotIndex and from a first symbol in the first slot provided by SBFD-StartingSymbolIndex, and end in a second slot provided by SBFD-EndingSlotIndex and in a second symbol in the second slot provided by SBFD-EndingSymbolIndex. SBFD symbols can be provided in any of pattern1 and, if provided, pattern2. A configuration period for SBFD symbols is msec when only pattern1 is provided, or when pattern2 is additionally provided. Except for a PRACH transmission in a PRACH occasion determined based on a second RACH configuration provided by sbfd-RACHDualConfig as described in clause 8, the UE transmits or receives a physical channel or signal either only in SBFD symbols or only in non-SBFD symbols. For a PUCCH transmission with SP-CSI reports, or for a PUCCH with SR, LRR, UEIRI, UE doesn’t transmit the PUCCH transmission occasion that is mapped to SBFD symbols and non-SBFD symbols. When the UE is provided sbfd-Config2-Transmission, the UE can - transmit a first PUCCH or PUSCH or a first repetition of a PUCCH or PUSCH in non-SBFD symbols, and - transmit a second PUCCH or PUSCH or a second repetition of the PUCCH or PUSCH, in SBFD symbols When the UE is provided sbfd-Config2-Reception, the UE can - receive a first PDSCH or a first repetition of a PDSCH in non-SBFD symbols, and - receive a second PDSCH or a second repetition of the PDSCH in SBFD symbols When a UE is not provided sbfd-Config2-Transmission - for a PUCCH or PUSCH transmission with repetitions, if the first repetition is either in SBFD symbols or in non-SBFD symbols, the remaining repetitions are also either in SBFD symbols or in non-SBFD symbols, respectively - for a Type 2 CG PUSCH transmission, or for a PUSCH transmission with SP-CSI reports, if the first transmission after a latest activation is either in SBFD symbols or in non-SBFD symbols, the remaining transmissions associated with the latest activation are also either in SBFD symbols or in non-SBFD symbols, respectively - for a Type 1 CG PUSCH, or for a PUCCH transmission with SP-CSI reports, or for a PUCCH with SR, LRR, UEIRI, or P-CSI, or SRS, all respective transmissions are either only in SBFD symbols or only in non-SBFD symbols as indicated by the respective configurations [12, TS 38.331] When a UE is not provided sbfd-Config2-Reception, - for a PDSCH reception with repetitions, if the first repetition is either in SBFD symbols or in non-SBFD symbols, the remaining repetitions are also either in SBFD symbols or in non-SBFD symbols, respectively - for a SPS PDSCH reception, if the first reception after a latest activation is either in SBFD symbols or in non-SBFD symbols, the remaining receptions associated with the latest activation are also either in SBFD symbols or in non-SBFD symbols, respectively In an SBFD symbol, and except for cross-link interference measurements [6, TS 38.214], the UE transmits or receives only in RBs that are both in the active UL BWP and in the UL sub-band, or both in the active DL BWP and the DL sub-band(s), respectively. The UE does not transmit in SBFD symbols indicated for presence of SS/PBCH blocks within the active DL BWP by ssb-PositionsInBurst in SIB1 or in ServingCellConfigCommon. If the UE is additionally provided tdd-UL-DL-ConfigurationDedicated, the parameter tdd-UL-DL-ConfigurationDedicated overrides only flexible symbols per slot over the number of slots as provided by tdd-UL-DL-ConfigurationCommon. The tdd-UL-DL-ConfigurationDedicated provides - a set of slot configurations by slotSpecificConfigurationsToAddModList - for each slot configuration from the set of slot configurations - a slot index for a slot provided by slotIndex - a set of symbols for a slot by symbols where - if symbols = allDownlink, all symbols in the slot are downlink - if symbols = allUplink, all symbols in the slot are uplink - if symbols = explicit, nrofDownlinkSymbols provides a number of downlink first symbols in the slot and nrofUplinkSymbols provides a number of uplink last symbols in the slot. If nrofDownlinkSymbols is not provided, there are no downlink first symbols in the slot and if nrofUplinkSymbols is not provided, there are no uplink last symbols in the slot. The remaining symbols in the slot are flexible For each slot having a corresponding index provided by slotIndex, the UE applies a format provided by a corresponding symbols. The UE does not expect tdd-UL-DL-ConfigurationDedicated to indicate as uplink or as downlink a symbol that tdd-UL-DL-ConfigurationCommon indicates as a downlink or as an uplink symbol, respectively. For a set of symbols of a slot that are indicated as SBFD by tdd-UL-DL-ConfigurationCommon, the UE ignores symbols provided by tdd-UL-DL-ConfigurationDedicated, if any. For each slot configuration provided by tdd-UL-DL-ConfigurationDedicated, a reference SCS configuration is the reference SCS configuration provided by tdd-UL-DL-ConfigurationCommon. A slot configuration period and a number of downlink symbols, uplink symbols, and flexible symbols in each slot of the slot configuration period are determined from tdd-UL-DL-ConfigurationCommon and tdd-UL-DL-ConfigurationDedicated and are common to each configured BWP. A UE considers symbols in a slot indicated as downlink by tdd-UL-DL-ConfigurationCommon, or tdd-UL-DL-ConfigurationDedicated to be available for receptions and considers symbols in a slot indicated as uplink by tdd-UL-DL-ConfigurationCommon, or by tdd-UL-DL-ConfigurationDedicated to be available for transmissions. If a UE is not configured to monitor PDCCH for DCI format 2_0, for a set of symbols of a slot that are indicated as flexible by tdd-UL-DL-ConfigurationCommon and tdd-UL-DL-ConfigurationDedicated if provided, or when tdd-UL-DL-ConfigurationCommon and tdd-UL-DL-ConfigurationDedicated are not provided to the UE - the UE receives PDSCH or CSI-RS in the set of symbols of the slot if the UE receives a corresponding indication by a DCI format - the UE transmits PUSCH, PUCCH, PRACH, or SRS in the set of symbols of the slot if the UE receives a corresponding indication by a DCI format, a RAR UL grant, fallbackRAR UL grant, or successRAR For operation on a single carrier in unpaired spectrum, if a UE is configured by higher layers to receive a PDCCH, or a PDSCH, or a CSI-RS, or a DL PRS in a set of symbols of a slot, the UE receives the PDCCH, the PDSCH, the CSI-RS, or the DL PRS if the UE does not detect a DCI format that indicates to the UE to transmit a PUSCH, a PUCCH, a PRACH, or a SRS in at least one symbol of the set of symbols of the slot; otherwise, the UE does not receive the PDCCH, or the PDSCH, or the CSI-RS, or the DL PRS in the set of symbols of the slot. For a UE operation with shared spectrum channel access in FR1, or in FR2-2 when the UE is provided ChannelAccessMode2 = 'enabled', if the UE is provided csi-RS-ValidationWithDCI, is not provided CO-DurationsPerCell, and is not provided SlotFormatCombinationsPerCell, and if the UE is configured by higher layers to receive a CSI-RS in a set of symbols of a slot, the UE cancels the CSI-RS reception in the set of symbols of the slot if the UE does not detect a DCI format indicating an aperiodic CSI-RS reception or scheduling a PDSCH reception in the set of symbols of the slot. If a UE is provided channelAccessMode ='dynamic' and is provided availableRB-SetsToAddModList and availableRB-SetsToReleaseList, the UE expects to be provided co-DurationsPerCellToAddModList and co-DurationsPerCellToReleaseList and/or slotFormatCombToAddModList and slotFormatCombToReleaseList. For operation on a single carrier in unpaired spectrum, if a UE is configured by higher layers to transmit SRS, or PUCCH, or PUSCH, or PRACH in a set of symbols of a slot and the UE detects a DCI format indicating to the UE to receive CSI-RS or PDSCH in a subset of symbols from the set of symbols, then - If the UE does not indicate the capability of partialCancellationPUCCH-PUSCH-PRACH-TX, the UE does not expect to cancel the transmission of the PUCCH or PUSCH or PRACH in the set of symbols if the first symbol in the set occurs within relative to a last symbol of a PDCCH reception where the UE detects the DCI format; otherwise, the UE cancels the PUCCH, or the PUSCH, or an actual repetition of the PUSCH [6, TS 38.214], determined from clauses 9, 9.2.5 and 9.2.6 or clause 6.1 of [6, TS 38.214], or the PRACH transmission in the set of symbols. - If the UE indicates the capability of partialCancellationPUCCH-PUSCH-PRACH-TX, the UE does not expect to cancel the transmission of the PUCCH or PUSCH or PRACH in symbols from the set of symbols that occur within relative to a last symbol of a PDCCH reception where the UE detects the DCI format. The UE cancels the PUCCH, or the PUSCH, or an actual repetition of the PUSCH [6, TS 38.214], determined from clauses 9, 9.2.5 and 9.2.6 or clause 6.1 of [6, TS 38.214], or the PRACH transmission in remaining symbols from the set of symbols. - The UE does not expect to cancel the transmission of SRS in symbols from the subset of symbols that occur within relative to a last symbol of a PDCCH reception where the UE detects the DCI format. The UE cancels the SRS transmission in remaining symbols from the subset of symbols. is the PUSCH preparation time for the corresponding UE processing capability [6, TS 38.214] assuming and corresponds to the smallest SCS configuration between the SCS configuration of the PDCCH carrying the DCI format and the SCS configuration of the SRS, PUCCH, PUSCH or , where corresponds to the SCS configuration of the PRACH if it is 15kHz or higher; otherwise . For a set of symbols of a slot that are indicated to a UE as uplink by tdd-UL-DL-ConfigurationCommon, or tdd-UL-DL-ConfigurationDedicated, the UE does not receive PDCCH, PDSCH, or CSI-RS when the PDCCH, PDSCH, or CSI-RS overlaps, even partially, with the set of symbols of the slot. For a set of symbols of a slot that are indicated to a UE as uplink by tdd-UL-DL-ConfigurationCommon, or tdd-UL-DL-ConfigurationDedicated, the UE does not receive DL PRS in the set of symbols of the slot, if the UE is not provided with a measurement gap. For a set of symbols of a slot that are indicated to a UE as downlink by tdd-UL-DL-ConfigurationCommon, or tdd-UL-DL-ConfigurationDedicated and, when applicable, are indicated as non-SBFD by tdd-UL-DL-ConfigurationCommon, the UE does not transmit PUSCH, PUCCH, PRACH, or SRS when the PUSCH, PUCCH, PRACH, or SRS overlaps, even partially, with the set of symbols of the slot. For a set of symbols of a slot that are indicated to a UE as flexible by tdd-UL-DL-ConfigurationCommon, and tdd-UL-DL-ConfigurationDedicated if provided, or are indicated as SBFD by tdd-UL-DL-ConfigurationCommon, the UE does not expect to receive both dedicated higher layer parameters configuring transmission from the UE in the set of symbols of the slot and dedicated higher layer parameters configuring reception by the UE in the set of symbols of the slot. For operation on a single carrier in unpaired spectrum, for a set of symbols of a slot indicated to a UE for reception of SS/PBCH blocks by ssb-PositionsInBurst in SIB1 or by ssb-PositionsInBurst in ServingCellConfigCommon or as described in Clause 4.4 or, if the UE is not provided dl-OrJointTCI-StateList, by ssb-PositionsInBurst in SSB-MTCAdditionalPCI associated to physical cell ID with active TCI states for PDCCH or PDSCH, or for a set of symbols of a slot corresponding to SS/PBCH blocks configured for L1 beam measurement/reporting, the UE does not transmit PUSCH, PUCCH, PRACH in the slot if a transmission would overlap with any symbol from the set of symbols and the UE does not transmit SRS in the set of symbols of the slot. The UE does not expect the set of symbols of the slot to be indicated as uplink by tdd-UL-DL-ConfigurationCommon, or tdd-UL-DL-ConfigurationDedicated, when provided to the UE. < Unchanged Text Omitted > |

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606825](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606825.zip) · `[126-R19-AI 8.1]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#126:9.2:002`

> In SIBx configuration for early SRS when UE transition from IDLE/INACTIVE to CONNECTED mode, up to two SRS resource sets can be provided in an SRS configuration, configured in SIBx.
> - Configuration of one or two SRS resource set(s) is the same as SRS antenna switching configuration rule supported in Rel-15.
> - Note: Each SRS configuration corresponds to one xTyR assumption.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606464](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606464.zip) · `[126-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#126:9.2:003` · 관련 주제: CSI 보고/codebook, CSI-RS

> On MAC-CE triggering indication in MSG4 for early SRS/CSI/CSI-RS when UE transition from IDLE/INACTIVE to CONNECTED mode,
> - For SRS-AS triggering, a MAC-CE in MSG4 includes an SRS configuration ID of an SRS configuration provided in SIBx and supported by the UE.
>   - All the SRS resource set(s) configured in the SRS configuration indicated by the  SRS configuration ID will be triggered.
> - For CSI and CSI-RS triggering, a MAC-CE in MSG4 includes an CSI report configuration ID of a CSI report configuration provided in SIBx and supported by the UE.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606464](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606464.zip) · `[126-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#126:9.2:006` · 관련 주제: CSI 보고/codebook, CSI-RS

> RAN1 conclude that which SIB is used to carry the resource/reporting configuration(s) for early SRS-AS/CSI/CSI-RS triggering when UE transition from IDLE/INACTIVE to CONNECTED mode is up to RAN2 decision, where RAN2 considers that RAN1 has agreed that UE receives the SIB containing configuration(s) for early SRS-AS/CSI-RS/CSI triggering before MSG3 as follows:
> | Agreement: For a UE transition from IDLE to CONNECTED mode, support the following procedure at least for early aperiodic SRS-AS/CSI-RS/CSI triggering (i.e., early triggering of aperiodic SRS-AS transmission, aperiodic CSI-RS reception, aperiodic CSI reporting): Step-1: The UE receives the resource/reporting configuration(s) for early SRS-AS/CSI-RS/CSI triggering provided in the system information before MSG3. FFS: Which SIB is used to carry the resource/reporting configuration(s) for early SRS-AS/CSI/CSI-RS triggering Step-2: The UE reports its capability on early SRS/CSI-RS/CSI triggering through MSG3 Step-3: The UE receives MSG4 that triggers early SRS-AS/CSI-RS/CSI based on the capability reported by the UE. Step-4: The UE performs aperiodic SRS-AS transmission, aperiodic CSI-RS reception, and/or aperiodic CSI reporting. FFS: Timeline of the aperiodic SRS-AS transmission, aperiodic CSI-RS reception, aperiodic CSI reporting Note: The term “capability” above does not mean legacy RRC based UE capability. FFS: For a UE transition from INACTIVE to CONNECTED mode, whether above procedure can be reused at least for early aperiodic SRS-AS/CSI-RS/CSI triggering Note: Whether the aperiodic SRS-AS transmission, aperiodic CSI-RS reception, and/or aperiodic CSI reporting can be configured/triggered simultaneously will be discussed separately |
> - Send a LS to RAN2 to inform the above

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606466](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606466.zip) · `[126-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#126:9.2:007` · 관련 주제: CSI 보고/codebook, CSI-RS

> RAN1 conclude that how UE report through MSG3 which/whether the configuration(s), provided in SIB, for early CSI/CSI-RS/SRS is/are supported by UE is up to RAN2 decision, where RAN2 considers the following RAN1 agreements:
> | Agreement For early triggering of SRS-AS when UE transition from IDLE/INACTIVE to CONNECTED mode, support Option-2 as follows: In Step-1, SIBx provides one or multiple SRS configurations based on one or multiple ‘xTyR’ UE capability assumptions. At least one SRS configuration(s) resource sets for SRS-AS in an SRS configuration is provided for a same ‘xTyR’ FFS: Information to be provided in SRS configuration(s) FFS: Whether Configuration information could be SRS configuration or the CSI report configuration for PMI-free report. FFS: Whether SRS configuration can be associated with CSI report configuration for PMI-free report. In Step-2, UE reports through MSG3 which/whether the SRS configuration(s) provided in SIBx is/are supported. FFS: How to report which/whether the SRS configuration(s) provided in SIBx is/are supported. Agreement: For early triggering of aperiodic CSI reporting and the associated CSI-RS for CSI when UE transition from IDLE/INACTIVE to CONNECTED mode, support Option-2 as follows: In Step-1, SIBx provides one or multiple CSI report configurations based on one or multiple UE capability assumptions Each CSI reporting configuration is associated with a CSI resource configuration for channel measurement. The CSI-RS resource set(s) in the CSI resource configuration for channel measurement is provided with a same number of CSI-RS ports Each CSI reporting configuration is associated with a CSI resource configuration for CSI-IM based interference measurement. FFS: Support of NZP CSI-RS based interference measurement FFS: Information to be provided in a CSI report/resource configuration In Step-2, UE reports through MSG3 which/whether the CSI report configuration(s) provided in SIBx is/are supported. FFS: How to report which/whether the CSI report configuration(s) provided in SIBx is/are supported. Agreement: For early triggering of aperiodic TRS when UE transition from IDLE/INACTIVE to CONNECTED mode, support Option-1, i.e., In Step-1, SIBx provides one CSI resource configuration for aperiodic TRS FFS: Whether to support more than one TRS resource sets provided in one CSI resource configuration (e.g., TRS resource sets can be provided with different triggering offsets, numbers of TRS bursts and/or gap between TRS bursts, etc) In Step-2, UE reports through MSG3 whether the CSI resource configuration for aperiodic TRS provided in SIBx is supported. FFS: Whether/How UE additionally reports via MSG3 the number of TRS bursts that the UE needs |
> - Send a LS to RAN2 to inform the above

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606466](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606466.zip) · `[126-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#126:9.2:011` · 관련 주제: CSI 보고/codebook

> On how to indicate the slot offset of MSG4-scheduled PUSCH for aperiodic CSI reporting when UE transition from IDLE/INACTIVE to CONNECTED mode, support Alt-1, i.e.,
> - Alt-1: A separate field in the MAC-CE indicates the slot offset for MSG4-scheduled PUSCH, and UE ignores the K2 indicated by PUSCH TDRA field in UL grant content.
> - Note: The new field has the same functionality as K2 obtained from TDRA field.
> Improvement of SRS capacity and coverage

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606467](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606467.zip) · `[126-R20-MIMO]`

**Conclusion** · `9.2` NR MIMO Phase 6 · `RAN1#126:9.2:012`

> Regarding whether an SRS resource set spans two slots or is confined within one slot,
> - If the offset values of all the SRS resources within the SRS resource set are k' = 0,
>   - when all the SRS resources are entirely contained within the S slot, the SRS resource set is confined within one slot
>   - when at least one SRS resource crosses a slot boundary, the SRS resource set spans two slots.
> - If the SRS resources within the SRS resource set have different k' values (both 0 and 1), the SRS resource set spans two slots.
> - If the offset values of all the SRS resources within the SRS resource set are k' = 1, the SRS resource set is confined within one slot.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606467](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606467.zip) · `[126-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#126:9.2:013`

> The pseudo-random sequence  for start RB hopping across different SRS FH period groups is generated using the Gold sequence adopted in NR.
> - For SRS FH period group , the pseudo-random sequence is given by
>     - Where  is the SRS counter,  is the  entry of the set  and  is the cardinality of the set . The hopping granularity is  adjacent frequency hopping period(s)
>     - Note: the set  and the hopping granularity  can be discussed separately. If there is no further agreement,
>       - For  and ,
>       - For ,
>   - FFS: X=2 or 8
> - The initialization ID is determined by
>   - A newly introduced RRC configured ID with value range [0,1023]
> - The sequence is initialized
>   - At the beginning of radio frame

남은 FFS 1건

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606467](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606467.zip) · `[126-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#126:9.2:014`

> The definition of SRS transmission occasion for cross-slot SRS resource is as the following:
> a SRS transmission occasion is defined by two consecutive S and U slots, a first symbol s within S slot and a number of consecutive symbols L where the last symbol is within U slot.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606467](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606467.zip) · `[126-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#126:9.2:015`

> Support adding a single aperiodic SRS resource set configuration for 1T8R via cross-slot, where eight SRS resources are transmitted in different symbols of two consecutive S and U slots, each mapped to a different UE antenna port.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606467](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606467.zip) · `[126-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#126:9.2:016`

> Regarding the value of X in the pseudo-random sequence  for start RB hopping across different SRS FH period groups, X=8 is supported.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2605712](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2605712.zip) · `[126-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#126:9.2:017`

> When intra-repetition hopping for SRS repetition symbols within each SRS frequency hop is enabled, support the following formula to determine the start RB hopping pattern:
> where
> - determines the exact patterns for starting position hopping within a hop across repetition symbols, and
> - is given by the following table, wherein K
> The quantity  as a function of
> |  |  |  |  |
> |  | = K = 2 | = 4 and K =2 | = K = 4 |
> | 0 | 0 | 0 | 0 |
> | 1 | 1 | 2 | 2 |
> | 2 | - | - | 1 |
> | 3 | - | - | 3 |
> - determines the new starting RB index hopping pattern {0,1} within each SRS FH period group for PF=4 and K=2, and R17 RPFS start RB index hopping pattern across SRS FH periods for = K = 2 and = K = 4
> - is given by the following table, wherein
> The quantity  as a function of
> |  |  |  |  |
> |  | = K = 2 | = 4 and K =2 | = K = 4 |
> | 0 | 0 | 0 | 0 |
> | 1 | 1 | 1 | 2 |
> | 2 | - | - | 1 |
> | 3 | - | - | 3 |
> - determines the pattern generated by pseudo-random sequence and is discussed separately

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606880](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606880.zip) · `[126-R20-MIMO]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126:10.5.3.1:008` · 관련 주제: CSI 보고/codebook

> For 6GR codebook design for CSI report, study whether/how to address near-field (NF) propagation as follows:
> - Evaluation scenario:
>   - 7GHz band scenarios
>   - Same SLS methodology is assumed as agreed EVM for CSI evaluation, with NF channel modeling
>   - Centralized TXRU array (single TRP) architecture
> - Assess the following:
>   - Regular UPT stats
>   - Percentage of UEs impacted by NF and its impact on UPT
>     - Companies to report how to define NF UEs, e.g., UEs within Rayleigh distance or scaling of Rayleigh distance for calibration purpose
>   - Whether/how the NF transmission issue (if identified) needs be addressed:
>     - SRS-based CSI acquisition
>     - via fixed codebook design
>       - with NR fixed DFT basis or port-selection basis (e.g., large-array into multiple sub-arrays analogous to CJT extension/multiple-panel)
>       - with new fixed basis (e.g., SD basis utilizing distance domain or other)
>       - with basis combined from DFT beams/port selection
>     - via DLable codebook/basis
>     - via AI-based CSI compression

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126:10.5.3.1:016` · 관련 주제: CSI 보고/codebook

> For the evaluation of stand-alone reporting for CJT calibration report, consider the following aspects:
> - Reporting quantities of Rel-19 CJTC-Dd/F/P can be candidates
> - xTRP delay offset report
>   - Study dynamic range ADO and resolution MFO
>     - Rel-19 CJTC-Dd dynamic range and resolution can be considered as a starting point
>     - FFS: other candidate values of ADO and MDO
> - xTRP frequency offset report
>   - Study dynamic range AFO and resolution MFO
>     - Rel-19 CJTC-F dynamic range and resolution can be considered as a starting point
>     - FFS: other candidate values of AFO and MFO
> - xTRP phase offset report
>   - Study resolution MP and frequency granularity (WB, SB)
>     - Rel-19 CJTC-P resolution can be considered as a starting point
>     - FFS: other candidate values of MP
> - Companies to report how to acquire mTRP CSI for evaluation, e.g., SRS-based CSI acquisition or CJT CSI report
> - Companies to report the modeling of CJT calibration report, including reporting periodicity, residual offset and fluctuation, all under realistic assumption
> - Companies to report assumption of measurement accuracy error levels
> - FFS on measurement RS requirement, e.g., frequency density and bandwidth, # of RS symbols, the gap between RS symbols
> - Assumption on algorithms to determine delay/frequency/phase offset report

남은 FFS 4건

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#126:10.5.3.2:001`

> For SRS, at least cyclic-shift and/or comb-offset are supported.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#126:10.5.3.2:002`

> Study whether/how TD-OCC can be supported together with SRS repetition to enable multiplexing of SRS ports, and at least take the following aspects into consideration:
> - OCC lengths: e.g., TD-OCC2, TD-OCC4, other lengths
> - Whether it is applicable to intra- and inter-UE multiplexing of SRS ports
> - TD-OCC related interference randomization scheme
> - The non-orthogonality incurred by partial dropping
> - Channel variation in time domain

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#126:10.5.3.2:003`

> For at least increasing SRS capacity/reducing overhead/improve coverage purposes sparse SRS patterns with comb values larger than 8, study at least comb 12 and 16 with consideration of at least the following aspects.
>   - SRS sequences
>   - MPR and PAPR/CM impact
>   - Max number of cyclic shifts for the corresponding comb value
>   - Minimum available bandwidth and its corresponding sequence
>   - Channel estimation performance
>   - Applicable RB sizes (e.g., RB size >= 8)
>   - Any other performance impacts
> - FFS other comb values.
> - Note: RAN4 input on maximum power boosting is needed

남은 FFS 1건

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#126:10.5.3.2:004`

> Support cross-slot SRS transmission at least for consecutive S+U slots
> - FFS: whether to support cross-slot SRS transmission spanning any two consecutive slots, e.g., U+U slots.

남은 FFS 1건

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#126:10.5.3.2:005` · 관련 주제: CSI 보고/codebook

> Study at least the following aspects of precoded SRS
> - Intended usage (e.g., for UL CSI and/or DL CSI)
> - Feasibility under specific UE architectures (e.g., xTyR configurations for DL CSI)
> - Gain compared to non-precoded SRS, accounting for practical impairments (e.g., PAPR/CM loss, realistic UE reciprocity, and UE coherency assumptions)
> - Methods for precoder derivation of precoded SRS:
> - Method-1: Determined by NW (e.g., derived from the measurements of SRS and indications from NW)
> - Method-2: Determined (with/without reported) by UE via DL measurement
> - FFS: UE UL/DL reciprocity calibration

남은 FFS 1건

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#126:10.5.3.2:006`

> For SRS of 6GR, study the following frequency hopping aspects
> - A single-level frequency hopping
>   - hopping over bandwidth with one or multiple frequency hops
> - Two-level frequency hopping
>   - First level: hopping over BW with one or multiple frequency hops
>   - Second level: hopping within each frequency hop of the first-level hopping
> - For single or two levels, consider at least the following options
>   - Nested tree-like frequency hopping pattern
>   - Sequential hopping pattern
>   - Pattern following RB offset provided by NW
>   - With/without Intra-repetition hopping in the second level
> Note: the case with larger DL BW than UL BW will be discussed separately

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#126:10.5.3.2:007`

> To support maximum SRS bandwidth beyond 272 PRBs in a carrier, consider the following options:
> - Option 1: Table based approach (similar to NR)
>   - Option 1-1:
>     - Refer to the bandwidth entries for up to 272 PRBs in the table from NR
>     - Introduce new SRS bandwidth entries from 272 to [544] PRBs
>   - Option 1-2:
>     - Scale up the SRS bandwidth entries in the table from NR by integer factor, e.g. value of 2 or 4
>   - Option 1-3:
>     - The overall SRS bandwidth is divided into more than one part, in which each part can reuse SRS bandwidth entries in the table from NR.
> - Option 2: Flexible SRS bandwidth determination and frequency hopping
>   - Replace the existing table-based SRS bandwidth determination with parameter-based frequency hopping pattern determination provided by NW

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.3` Other aspects · `RAN1#126:10.5.3.3:002` · 관련 주제: CSI 보고/codebook, CSI-RS

> For the evaluation of joint DL/UL based CSI acquisition, at least take the following baseline for use case 1
> - Baseline#1: DL CSI acquisition based on SRS only
> - Baseline#2: DL CSI acquisition based on CSI-RS only
> - Additionally consider the Rel-19 UE antenna model defined in TR 38.901.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Other Aspects related to CSI]`

**Agreement** · `10.5.3.3` Other aspects · `RAN1#126:10.5.3.3:004` · 관련 주제: CSI 보고/codebook, CSI-RS

> Use the following template to collect the simulation results for use case 1:
> | Simulation assumptions on scenario, MIMO scheme, e.g., carrier frequency, channel model, antenna port layouts at aNB and antenna port layouts at UE, etc. |  |
> | Assistance information |  |
> | How to obtain and report, e.g., format and quantization, the assistance information |  |
> | How to use the assistance information |  |
> | CSI-RS and CSI report configuration, if any |  |
> | SRS configuration |  |
> | Performance gain compared with baseline schemes |  |
> | Observations in terms of the agreed KPIs |  |

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Other Aspects related to CSI]`

**Agreement** · `10.5.3.3` Other aspects · `RAN1#126:10.5.3.3:005` · 관련 주제: CSI 보고/codebook, CSI-RS

> Use the following template to collect the simulation results for use case 2:
> | Simulation assumptions on scenario, MIMO scheme, e.g., carrier frequency, channel model, antenna port layouts at aNB and UE etc. |  |
> | Assistance information |  |
> | How to obtain and report the assistance information |  |
> | How to use the assistance information for MCS and RI selection. |  |
> | CSI-RS and CSI report configuration, if any |  |
> | SRS configuration |  |
> | Performance gain compared with baseline schemes |  |
> | Observations in terms of the agreed KPIs |  |

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Other Aspects related to CSI]`

**Agreement** · `10.5.3.3` Other aspects · `RAN1#126:10.5.3.3:006` · 관련 주제: CSI 보고/codebook, CSI-RS

> For the evaluation of joint DL/UL based CSI acquisition, at least take the following baseline for use case 2
> - Baseline #1: DL CSI acquisition based on precoded CSI-RS and SRS, where PDSCH precoder is determined based on SRS, and rank and MCS follows the non-PMI report based on precoded CSI-RS.
>   - Companies to report details about how the network determines the CSI-RS precoder
> - Baseline#2: DL CSI acquisition based on both SRS and CSI-RS, where UE reports CRI/PMI/RI/CQI based on CSI-RS, and network determines rank and MCS based on the SRS channel estimation and the reported CRI/PMI/RI/CQI
>   - Companies to report details about how network determines rank and MCS based on the SRS channel estimation and the reported CRI/PMI/RI/CQI
> - It does not mean that CRI-RI-CQI report is supported.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Other Aspects related to CSI]`

**Agreement** · `10.5.3.3` Other aspects · `RAN1#126:10.5.3.3:008` · 관련 주제: CSI 보고/codebook

> On top of agreement in RAN1#125, further study and evaluate the following sub use cases for joint DL/UL CSI acquisition use case 1
> - Use case 1A: Assisting SRS channel estimation, e.g., interference mitigation and channel interpolation
> Use case 1B: Assisting aNB side compensation for SRS reception with SRS power imbalance
> Use case 1C: CSI feedback and SRS fusion for full dimension channel matrix acquisition
> Use case 1D: Assisting SRS configuration

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Other Aspects related to CSI]`

## RAN1#125 — 22건

**Agreement** · `8.1` Maintenance on AI/ML for NR Air interface, NR MIMO Phase 5,  NES and NTN for NR and IoT · `RAN1#125:8.1:003` · 관련 주제: Beam management, CSI 보고/codebook, CSI-RS

> The following TP for TS 38.214 Clause 5.4 is endorsed.
> The corresponding CR for Rel-19 TS 38.214 in R1-2605124 is endorsed.
> Reason for change: CSI computation time for the CSI report of RS-PAI has not been discussed or defined yet in current specification. Furthermore, the current specification would cause the RS-PAI report to fall under the branch of the “ of table 5.4-2 otherwise”, which would mistakenly apply high latency CSI computation time  to the RS-PAI report.
> Summary of change: Reuse CSI computation time of legacy beam management, i.e. () for model monitoring CSI report of RS-PAI.
> Consequences if not approved: UE may be unable to determine the appropriate CSI computation time for RS-PAI report and could erroneously use the high latency CSI computation time  for the RS-PAI report.
> | 5.4 UE CSI computation time <omitted texts> Z, Z' and µ are defined as: and , where M is the number of updated CSI report(s) according to Clause 5.2.1.6, corresponds to the m-th updated CSI report and is defined as - of the table 5.4-1 if max{ µPDCCH, µCSI-RS, µUL} ≤ 3 and if the CSI is triggered without a PUSCH with either transport block or HARQ-ACK or both when L = 0 CPUs are occupied (according to Clause 5.2.1.6) and the CSI to be transmitted is a single CSI and corresponds to wideband frequency-granularity where the CSI corresponds to at most 4 CSI-RS ports in a single resource without CRI report and where CodebookType is set to 'typeI-SinglePanel' or where reportQuantity is set to 'cri-RI-CQI', or - of the table 5.4-2 if the CSI to be transmitted corresponds to wideband frequency-granularity where the CSI corresponds to at most 4 CSI-RS ports in a single resource without CRI report and where CodebookType is set to 'typeI-SinglePanel' or where reportQuantity is set to 'cri-RI-CQI', or - of the table 5.4-2 if the CSI to be transmitted corresponds to wideband frequency-granularity where the reportQuantity is set to 'ssb-Index-SINR', 'cri-SINR', 'ssb-Index-SINR- Index ', or 'cri-SINR- Index ', or - of the table 5.4-2 if reportQuantity is set to 'cri-RSRP', 'ssb-Index-RSRP', 'cri-RSRP- Index', 'L1-SRS-RSRP', 'L1-CLI-RSSI' or, 'ssb-Index-RSRP- Index ' or 'rs-pai-r19', is according to UE reported capability beamReportTiming and KBl is according to UE reported capability beamSwitchTiming as defined in [13, TS 38.306], or if the CSI report is configured with ltm-CSI-ReportConfig for L1-RSRP measurement, or if the CSI report is configured with eventType, or - , with of the table 5.4-2 if reportQuantity is set to 'p-cri-r19', 'p-cri-RSRP-r19', 'p-ssb-index-r19', or 'p-ssb-index-RSRP-r19', where and are according to UE reported capability as defined in [13, TS 38.306] and different values for and may be reported by UE capability based on whether nroftimeinstance-r19 is configured or not within the CSI report, or <omitted texts> |

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2604995](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2604995.zip)

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#125:9.2:001` · 관련 주제: CSI 보고/codebook, CSI-RS

> For early aperiodic SRS-AS/CSI-RS/CSI triggering when UE transition from IDLE/INACTIVE to CONNECTED mode, in Step-4, the UE performs aperiodic SRS-AS transmission, aperiodic CSI-RS reception, and/or aperiodic CSI reporting, if the UE Contention Resolution Identity in the MAC CE of MSG4 matches the CCCH SDU transmitted in Msg3.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2603720](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2603720.zip) · `[125-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#125:9.2:002` · 관련 주제: CSI 보고/codebook

> When UE transition from IDLE/INACTIVE to CONNECTED mode, the pathloss RS for the MSG4-triggered UL signal (i.e., aperiodic SRS-AS and PUSCH for aperiodic CSI reporting) is the SSB the UE identified during the random-access procedure when UE transition from IDLE/INACTIVE to CONNECTED mode.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2603720](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2603720.zip) · `[125-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#125:9.2:003` · 관련 주제: CSI 보고/codebook

> For a MSG4-triggered UL signal (i.e., aperiodic SRS-AS and PUSCH for aperiodic CSI reporting) when UE transition from IDLE/INACTIVE to CONNECTED mode, support the followings:
> - The open-loop power control parameters p0 and alpha for a MSG4-triggered UL signal the are configured in SIBx
> - FFS: Whether/how to support close-loop power control (CLPC) for the MSG4-triggered UL signal
> - FFS: Whether/How to determine UL TX spatial filter of MSG4-triggered UL signal if applicable

남은 FFS 2건

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2603720](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2603720.zip) · `[125-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#125:9.2:007`

> For MSG4-triggered aperiodic SRS-AS when UE transition from IDLE/INACTIVE to CONNECTED mode, a same number of SRS symbol(s) for all the triggered SRS resource(s) is indicated via MAC-CE in MSG4.
> - The starting position, repetition factor and frequency hopping parameters of each SRS resource is configured in SIBx.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2605114](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2605114.zip) · `[125-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#125:9.2:012`

> The number of starting positions for SRS repetition symbols within each SRS frequency hop (i.e. K) is configured by higher layer signaling per resource configuration.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2603898](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2603898.zip) · `[125-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#125:9.2:013`

> Reusing of a SRS resource configured with per resource slot offset k' in more than one SRS resource sets is supported.
> - FFS:  How to determine SRS resource set is spanned over two slots or confined within one slot

남은 FFS 1건

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2605073](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2605073.zip) · `[125-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#125:9.2:014`

> For the per-resource offset k’ of an AP SRS resource,
>     - If the SRS resource set is spanned over two slots:
>   - When k' = 0 or 1, the first slot of the SRS resource is the first or second of the two slots spanned by the SRS resource set, respectively
>     - If the SRS resource set is confined within one slot:
>   - When k' = 0 or 1, the slot of the SRS resource is the slot of the SRS resource set
>     - k' = 0 by default, if k' is not configured for an SRS resource
> Note: The first slot of the SRS resource set is determined by slot offset k and available slot offset t configured per SRS resource set.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2605073](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2605073.zip) · `[125-R20-MIMO]`

**Conclusion** · `9.2` NR MIMO Phase 6 · `RAN1#125:9.2:015`

> Simultaneous enabling of the R17 RPFS start RB index hopping across multiple legacy SRS frequency hopping periods and intra-repetition hopping for SRS repetition symbols within each SRS frequency hop for all the allowed combinations of PF and K (i.e.,PF=4/K=2, / and /) is supported.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2605086](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2605086.zip) · `[125-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#125:9.2:016`

> Support RPFS start RB index hopping across multiple legacy SRS frequency hopping periods with the following patterns for intra-repetition hopping for SRS repetition symbols within each SRS frequency hop:
>   - For , , and , , start RB hopping across different SRS FH periods is determined by pseudo random sequence.
>   - For PF=4 and K=2, start RB hopping in each SRS FH period group including two adjacent periods is used to probe all subbands, and start RB hopping across different SRS FH period groups is determined by pseudo random sequence.
> FFS how the pseudo random sequence(s) are generated and indicated/configured

남은 FFS 1건

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2605086](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2605086.zip) · `[125-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#125:9.2:017`

> Allow SRS resource(s) in a non-cross-slot resource set to be transmitted in a serving cell before the same-slot transmission of PUSCH and corresponding DMRS in the serving cell.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2605086](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2605086.zip) · `[125-R20-MIMO]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#125:10.5.3.1:002` · 관련 주제: CSI 보고/codebook

> For the study on configurable/downloadable codebook/basis/bases, consider at least the following:
> - The information for NW to determine the configurable/downloadable codebook/basis/bases, e.g., reported CPI, SRS, previous reported CSI
>   - Companies report the detail assumptions for obtaining such information in the evaluation, at least including
>     - Additional signaling overhead for information collection, if applicable
>     - The assumptions of the information, e.g., the SRS related assumption, CPI reporting related assumption, time domain relationship with the target CSI report
>     - Additional measurement overhead, if applicable
> - Companies report
>   - BS antenna configuration, subband configuration
>   - signalling overhead, representing format of configurable/downloadable basis/codebook, updated frequency of the configurable/downloadable basis or configurable/downloadable codebook, how to determinate when to update
>   - whether the configurable/downloadable codebook or basis is UE- specific or UE-common (Cell-specific), rank/layer- common or specific
>   - codebook structure assumption for configurable/downloadable codebook/basis, e.g., eType-II-like, Type-I-like
>   - complexity at UE side for CSI feedback with configurable/ downloadable basis/codebook for CSI feedback: e.g., number of complex operations for CSI computation and memory requirement for basis storage
>   - whether NW-sided model is assumed
>     - If NW-sided model is assumed, companies report the input/output, labeling.
> - UE speed assumption follows the general EVM section 10.1 and other EVM follows the assumption agreed in RAN1#124.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#125:10.5.3.1:003` · 관련 주제: CSI 보고/codebook, CSI-RS

> For study of DMRS-based CSI, considering at least the following aspects:
> - Potential use cases, including e.g., increased CSI accuracy including inter-layer imbalance information, CSI-RS overhead reduction, CSI acquisition for TDD.
> - Benchmark:
>   - CSI-RS based
>     - P CSI-RS and/or AP CSI-RS based (precoded or non-precoded)
>   - SRS based
> - Company to report CSI-RS/SRS assumption for benchmark
> - Company to report the assumptions for DMRS resources and how DMRS is used for CSI measurement, e.g., only for channel measurement or both channel and interference measurement.
> - Companies to report the OLLA assumption details, if applicable
> - KPI:
>   - Throughput (average and edge UPT) vs total CSI feedback overhead (averaged over UEs, over simulation time (per time unit)), where the total CSI feedback overhead includes both DMRS based feedback, and other necessary CSI feedback (if applicable)
>   - Note: DL RS overhead is included in throughput calculation.
> - DMRS based report quantity:
>   - at least CQI, companies report CQI calculation assumption
>   - companies can report other quantities, e.g., PMI (e.g., refinement), RI, RSRP/SINR, DMRS port selection indication if assumed, including the detailed assumption
> - UE speed assumption follows the general EVM section 10.1 and other EVM follows the assumption agreed in RAN1#124.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#125:10.5.3.2:001` · 관련 주제: AI/ML CSI, CSI 보고/codebook

> Study the following cases for AI/ML UL-based CSI, and strive to support the unified SRS patterns/designs/framework that work for both AI/ML and non-AI/ML schemes.
> - AI/ML for low-overhead SRS (Sub-Case A): low-overhead SRS with AI/ML at the network side for CSI reconstruction
>   - Note: low-overhead SRS may include overhead reduction schemes in the time and/or frequency domains.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#125:10.5.3.2:002` · 관련 주제: AI/ML CSI, CSI 보고/codebook

> For the evaluation of AI/ML-based UL-based CSI acquisition,
>   - Support to reuse the assumption for evaluation of UL-based CSI
>   - FLOPs and number of parameters of AI/ML model are reported by company

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#125:10.5.3.2:003` · 관련 주제: AI/ML CSI, CSI 보고/codebook

> For the evaluation of scalability/generalization of AI/ML-based UL-based CSI acquisition, the evaluation methodology in NR (as in TR 38.843) can be considered as the starting point. The set of configurations are considered focusing on one or more of the following aspects:
> - Various antenna configurations, e.g., UE Tx port number, UE Tx port layout
> - Various channel and link conditions, e.g., SNR/SINR ranges
> - Various time/frequency domain factors, e.g., various frequency allocations/RPFS/hopping patterns, time domain allocations, UE speeds
> - Other aspects, e.g., power of SRS transmission, deployment scenarios, channel models
> Note: Companies are encouraged to evaluate generalization/scalability performance across multiple scenario/configuration combinations.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#125:10.5.3.2:004`

> Consider SRS repetition and cross-slot SRS transmission mechanisms specified in NR as a starting point for 6GR.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#125:10.5.3.2:005`

> For multiplexing of multiple SRS ports, study at least the following options:
>   - TDM
>   - CDM in frequency domains (at least include CS)
>   - TD-OCC
>   - FDM (at least include comb and comb offset)
>   - Combinations of above options
>   - Note: other schemes are not precluded
> - Strive for a unified design framework for different numbers of ports.
> - FFS whether/how to support dynamic/flexible adaptation of multiplexing parameters(e.g., comb and CS).
>   - Whether/how dynamic/flexible adaptation of multiplexing parameters can be achieved beyond resource/resource-set level indication can be discussed separately

남은 FFS 1건

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#125:10.5.3.2:006` · 관련 주제: CSI 보고/codebook

> Study at least the following aspects of SRS antenna switching for DL CSI acquisition
> - Guard Period (GP) between consecutive SRS resources for antenna switching
> - Whether and how to define the GP between consecutive SRS resources for antenna switching, considering the practical RF chain switching times of UEs
> - GP between SRS and other proceeding/following UL signal/channel transmission, if different antennas are used for SRS and other proceeding/following UL signal/channel transmission,
> - Whether/how to define GP between SRS and other proceeding/following UL signal/channel transmission
> - Allowed combinations of x (number of Tx antennas at UE) and y (number of Rx antennas at UE)
> - Impact of realistic UE antenna layouts (both symmetric and asymmetric number of antenna ports across RF chains)
> - Whether/how to handle power imbalance among SRS antenna ports due to insertion loss
> Note: regarding the practical RF chain switching times of UEs, and power imbalance, studies/conclusions from RAN4 should be considered by RAN1

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#125:10.5.3.2:007` · 관련 주제: CSI 보고/codebook

> For UL-based CSI in 6GR, study carrier switching and consider at least the following aspects
> - Take SRS carrier switching mechanisms in NR as the starting point for 6GR carrier switching study.
> - Strive to simplify the SRS carrier switching framework compared to NR, e.g.,
>   - By converging the redundant triggering alternatives to reduce UE complexity and standardization overhead
>   - By simplifying the collision handling rules when SRS for carrier switching collides with other UL signals/channels
>   - By reducing/eliminating unnecessary switching-back

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#125:10.5.3.2:008`

> For 6GR SRS sequence design,
>   - candidate options including:
>   - ZC and CGS sequences in NR
>   - Enhanced ZC
>   - Enhanced CGS
>   - other directions are not precluded

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#125:10.5.3.2:009`

> - For SRS transmission procedure to facilitate sounding in the UL of all parts of the DL bandwidth where the DL CBW is larger than supported UL CBW, study at least the following aspects/solutions
> - UL sounding for all parts of the target bandwidth over multiple transmissions of SRS, at least consider the following for solutions
>   - with a single SRS resource
>   - with multiple SRS resources
> - Consider the impacts on other signals/channels (including at least interruption of data transmission, collision handling), required number of switching, switching gap, SRS overhead to sound all parts of the DL bandwidth, time to complete the sounding
> - Accommodating any location of UL BW, if supported
> - Other aspects/solutions are not excluded
> Note: studies/conclusions from RAN4 might be needed.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of UL based CSI acquisition]`

## RAN1#124bis — 29건

**Agreement** · `8.2` Maintenance on NR MIMO Phase 5 · `RAN1#124bis:8.2:002` · 관련 주제: CSI 보고/codebook

> The following changes in Section 7.5 in TS38.213 are endorsed.
> The corresponding CR for Rel-19 TS38.213 in R1-2603403 is endorsed.
> - Reason for change: For UL power prioritization, the case of multiplexing UEIRI in a PUSCH transmission is not captured in current specifications which lead to unclear UE behaviour.
> - Summary of change: Reuse the rule for multiplexing HARQ-ACK in a PUSCH transmission for the case of multiplexing UEIRI in a PUSCH transmission.
> - Consequences if not approved: Unclear UE behaviour.
> | 7.5 Prioritizations for transmission power reductions For single cell operation with two uplink carriers or for operation with carrier aggregation or for operation with a candidate cell configured by LTM-Config or for operation with a single cell configured with sTx-2Panel, if a total UE transmit power for PUSCH or PUCCH or PRACH or SRS transmissions on serving cell(s) or on a candidate cell, if any, in a frequency range in a respective transmission occasion would exceed , where is the linear value of in transmission occasion as defined in [8-1, TS 38.101-1] for FR1 and [8-2, TS 38.101-2] for FR2, the UE allocates power to PUSCH/PUCCH/PRACH/SRS transmissions according to the following priority order (in descending order) so that the total UE transmit power for transmissions on serving cell(s) or on a candidate cell, if any, in the frequency range is smaller than or equal to for that frequency range in every symbol of transmission occasion . If the UE transmits SRS on multiple SRS resources according to Clause 6.2.1.4 of [6, TS 38.214], the UE allocates power so that all REs of the SRS transmission have same power. For the purpose of power allocation in this clause, if a UE is provided uci-MuxWithDiffPrio and the UE multiplexes HARQ-ACK information in a PUSCH, a priority index of the PUSCH is the larger of (a) the priority index of the PUSCH according to clause 9 and (b) the larger priority index of the HARQ-ACK information. When determining a total transmit power for serving cells or a candidate cell, if any, as described in Clause 21 in a frequency range in a symbol of transmission occasion , the UE does not include power for transmissions starting after the symbol of transmission occasion . The total UE transmit power in a symbol of a slot is defined as the sum of the linear values of UE transmit powers for PUSCH, PUCCH, PRACH, and SRS in the symbol of the slot. - PRACH transmission on a candidate cell, if any, as described in Clause 21 - PRACH transmission on the PCell - PUCCH or PUSCH transmissions with larger priority index - For PUCCH or PUSCH transmissions with same priority index - PUCCH transmission with HARQ-ACK information, and/or SR, and/or LRR, and/or UEIRI, or PUSCH transmission with HARQ-ACK information and/or UEIRI of the priority index - PUCCH transmission with CSI or PUSCH transmission with CSI - PUSCH transmission without HARQ-ACK information and UEIRI of the priority index or CSI and, for Type-2 random access procedure, PUSCH transmission on the PCell - If the UE is configured with prioSCellPRACH-OverSP-PeriodicSRS-r17 - Aperiodic SRS transmission or PRACH transmission on a serving cell other than the PCell - Semi-persistent and/or periodic SRS transmission - otherwise, - SRS transmission, with aperiodic SRS having higher priority than semi-persistent and/or periodic SRS, or PRACH transmission on a serving cell other than the PCell <Unchanged parts are omitted> |

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2603249](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603249.zip) · `[124-R19b-MIMO]`

**Agreement** · `8.2` Maintenance on NR MIMO Phase 5 · `RAN1#124bis:8.2:007` · 관련 주제: CSI 보고/codebook

> Adopt the following correction in section 6.4.1.4.3 of TS 38.211.
> The corresponding final CR for Rel-19 TS38.211 in R1-2603373 is endorsed.
> - Reason for change: To clarify that the equation for determination of the number of SRS ports when fourPortSRS-3 is configured, is not applicable when the SRS usage is set to ‘noncodebook’.
> - Summary of change: Adding condition “with usage set to ‘codebook’ or ‘antennaSwitching’” for the SRS resource set to disable one port
> - Consequences if not approved: Ambiguous UE behaviour for determination of the number of SRS ports when the SRS usage is set to ‘noncodebook’.
> | 6.4.1.4.3 Mapping to physical resources Throughout this clause, when the higher layer parameter numberOfHops is provided for SRS-PosResource, the sounding reference signal sequence definitions applies to a given hop. When SRS is transmitted on a given SRS resource, the sequence for each OFDM symbol and for each of the antenna ports of the SRS resource shall be multiplied with the amplitude scaling factor in order to conform to the transmit power specified in [5, 38.213] and mapped in sequence starting with to resource elements in a slot for each of the antenna ports according to where - for an SRS resource in an SRS resource set with the higher-layer parameter fourPortSRS-3Tx is configured, - otherwise, -------------------------------------------Unchanged parts are omitted------------------------------------------ |

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2603256](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603256.zip) · `[124-R19b-MIMO]`

**Agreement** · `8.2` Maintenance on NR MIMO Phase 5 · `RAN1#124bis:8.2:008` · 관련 주제: CSI 보고/codebook

> Send LS to RAN2 to update description of parameter “fourPortSRS-3Tx” in TS 38.331, including,
> - Correct the description in section SRS-Config
> | fourPortSRS-3Tx Indicates whether port 1003 is disabled for all SRS resources in the SRS resource set with usage set to codebook or antennaSwitching, or whether 3Tx transmission is enabled for a configured SRS resource set with usage set to nonCodebook. ‘’‘’his field can only be configured if nrofSRS-Ports for each SRS resource in the SRS resource set is set to ports4. |
> The corresponding draft LS in R1-2603349 is endorsed. The final LS in R1-2603350 is endorsed.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2603256](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603256.zip) · `[124-R19b-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#124bis:9.2:001` · 관련 주제: CSI 보고/codebook, CSI-RS

> For early aperiodic SRS/CSI/CSI-RS when UE transition from IDLE/INACTIVE to CONNECTED mode, support the followings:
> - Rel-15 SRS antenna switching pattern (i.e., 1T1R, 1T2R, 1T4R, 2T2R, 2T4R, and 4T4R) for aperiodic SRS-AS
> - Up to 32 CSI-RS ports for aperiodic CSI-RS associated with aperiodic CSI reporting
> - Up to 2 TRS bursts for aperiodic TRS

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2602826](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2602826.zip) · `[124b-R20-MIMO]`

**Conclusion** · `9.2` NR MIMO Phase 6 · `RAN1#124bis:9.2:002` · 관련 주제: CSI 보고/codebook, CSI-RS

> For early aperiodic SRS/CSI/CSI-RS when UE transition from IDLE/INACTIVE to CONNECTED mode:
> - Aperiodic SRS-AS is not mandated to be triggered along with aperiodic CSI reporting and associated CSI-RS, via MAC-CE in MSG4
> - Aperiodic TRS is not mandated to be triggered along with aperiodic CSI reporting and associated CSI-RS, via MAC-CE in MSG4

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2602826](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2602826.zip) · `[124b-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#124bis:9.2:004`

> On how to determine the serving cell(s) triggered with aperiodic SRS via ‘SRS request’ field in a DCI indicating switching out of dormancy based on legacy DCI formats, support Alt-1 with modification, i.e.,
> - When Rel-20 SRS triggering for SCell switching out of dormancy is enabled, the SRS trigger state indicated in ‘SRS request’ field applies to,
>   - The SCell(s) which is indicated with switching out of dormancy and configured with aperiodic SRS resource set(s) for SRS-AS associated with the SRS trigger state.
>   - FFS: The cell(s) scheduled by legacy mechanism and configured with aperiodic SRS resource set(s) associated with the SRS trigger state;
>   - FFS: When DCI 0_1/1_1 is used for indicating switching out of dormancy, whether only one serving cell is triggered with SRS.
>     - Note: If only one serving cell is triggered with SRS, Alt 2 can be one of the candidate for DCI 0_1/1_1.
>   - FFS: How to enable Rel-20 SRS triggering for SCell switching out of dormancy

남은 FFS 3건

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2602828](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2602828.zip) · `[124b-R20-MIMO]`

**Conclusion** · `9.2` NR MIMO Phase 6 · `RAN1#124bis:9.2:007`

> For early aperiodic SRS when UE transition from IDLE/INACTIVE to CONNECTED mode, there is no RAN1 consensus to support the dynamic indication of the comb offset, cyclic shift via MAC-CE in MSG4, i.e., the comb offset, cyclic shift are configured in SRS configuration(s) provided by SIBx.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2602829](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2602829.zip) · `[124b-R20-MIMO]`

**Conclusion** · `9.2` NR MIMO Phase 6 · `RAN1#124bis:9.2:008` · 관련 주제: CSI-RS

> Decide in RAN1#125:
> - Whether to support dynamic indication of the repetition factor of a triggered SRS via MAC-CE in MSG4.
> - Whether to support dynamic indication of the number of TRS burst(s) via MAC-CE in MSG4.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2602829](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2602829.zip) · `[124b-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#124bis:9.2:009`

> For cross-slot SRS, support PUSCH transmission with a priority index 0 and corresponding DMRS in a serving cell after all the SRS resource(s) of the same resource set with time-domain resource allocation entirely in the U slot in the serving cell.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2602528](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2602528.zip) · `[124b-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#124bis:9.2:010`

> For the time-domain location determination of aperiodic SRS resources within the cross-slot resource set,
>   - per-resource slot offset of an AP SRS resource is included in the resource configuration.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2602528](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2602528.zip) · `[124b-R20-MIMO]`

**Conclusion** · `9.2` NR MIMO Phase 6 · `RAN1#124bis:9.2:011`

> For intra-repetition hopping for SRS repetition symbols within each SRS frequency hop, whether phase continuity can be maintained is up to UE implementation.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2602529](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2602529.zip) · `[124b-R20-MIMO]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#124bis:10.5.3.2:001`

> Study at least hierarchical structure of SRS resource set and SRS resource for 6GR.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#124bis:10.5.3.2:002`

> Study how to support multiple usages using a same SRS transmission.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#124bis:10.5.3.2:003`

> Study SRS sequence design considering at least the following aspects:
> - Coverage, capacity and measurement performance, e.g., PAPR, size of sequence pool, cross-correlation/auto-correlation
> - Length candidates of SRS sequence
> - SRS resource element mapping
> - Flexible adaptation of SRS frequency domain parameters (if supported)

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#124bis:10.5.3.2:004`

> ZC and CGS sequences in NR are the starting point for studying 6GR SRS design.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#124bis:10.5.3.2:005`

> {1, 2, 3, 4, 8} are supported as the numbers of SRS antenna ports
>   - FFS: Other number of UE antenna ports
> - Note: Separate discussion on the number of antenna ports of UE device(s)

남은 FFS 1건

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#124bis:10.5.3.2:006`

> Support P/AP-SRS as the baseline for 6GR. Further study
> - Whether it is necessary to support SP-SRS.
> - Note: UE initiated SRS can be discussed separately.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#124bis:10.5.3.2:007`

> For 6GR SRS frequency hopping mechanism, study the following
>   - SRS frequency hopping pattern
>   - Partial frequency sounding with/without intra-repetition hopping

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#124bis:10.5.3.2:008`

> 5G SRS pattern design per resource (in frequency domain) with regular comb values (comb values supported by NR), i.e., combs 2, 4 and 8 is taken as starting point for the 6GR SRS study, further study at least the following aspects.
> - Multiplexing of multiple SRS ports.
> - Sparse SRS patterns, such as larger comb values, non-uniform-based patterns.
> - Note 1: impact of SRS pattern design on at least complexity, coverage, capacity and performance is to be considered.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#124bis:10.5.3.2:009` · 관련 주제: CSI 보고/codebook

> For UL-based CSI acquisition, study the following aspects of SRS repetition
>   - Number of repetitions
>   - Cross-slot SRS transmission
>   - Others

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#124bis:10.5.3.2:010` · 관련 주제: CSI 보고/codebook

> For UL-based CSI acquisition, study at least the following mechanisms of SRS interference mitigation
>   - Interference randomization based on hopping of group/base sequence, start RB index, comb offset, and cyclic shift for SRS

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#124bis:10.5.3.2:011`

> - To support maximum SRS bandwidth beyond 272 PRBs within a carrier efficiently, study at least the following aspects:
> - Frequency hopping
> - Sparse SRS in frequency domain
> - Redefining or extending the existing SRS bandwidth configuration
> - SRS sequence design
> - Combinations of above schemes
> - Other approaches are not excluded
> Note1: Sounding for larger DL CBW is a separate issue to be studied.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#124bis:10.5.3.2:012`

> At least from the perspectives of benefit, complexity, and overhead, study the feasibility and necessity of introducing more dynamic/flexible adaptation of the following SRS parameters than that supported by NR.
> - Frequency domain parameters, such as SRS bandwidth, starting position in frequency domain, hopping related parameters, resource element mapping
> - Time domain parameters, such as slot offset, starting position in time domain, number of consecutive OFDM symbols, periodicity
> - Code domain parameters, such as cyclic shift
> - Number of SRS ports
> - Combinations of above schemes, such as adaptive combination of comb offset and cyclic shift
> - Spatial domain parameters, such as SRS precoding
> - Other schemes are not excluded
> Note 1: feasibility may be different for each of the parameters.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#124bis:10.5.3.2:013`

> For the inter-UE multiplexing of SRS and other uplink channels/signals (e.g., SRS/PUCCH/PUSCH), study at least the following aspects
>   - Whether/how to introduce unified hopping between SRS and other UL channels (i.e., PUCCH, PUSCH)
>   - PUSCH/PUCCH Rate matching for SRS.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#124bis:10.5.3.2:014` · 관련 주제: CSI 보고/codebook

> For UL-based CSI acquisition, study at least the following aspects of precoded SRS transmission.
>   - How the precoder is determined
>   - Whether it requires UE side reciprocity or not
>   - Coherency assumption on antenna ports
>   - Impact on PAPR

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.3` Other aspects · `RAN1#124bis:10.5.3.3:006` · 관련 주제: CSI 보고/codebook

> At least study the following use case for joint DL/UL CSI acquisition
> - Use case 1: SRS based CSI acquisition assisted by DL based measurement and reporting
>   - DL based measurement and reporting is reported by companies
>   - Note: Both AI and non-AI solutions can be considered
> - Use case 2: MCS and rank selection for DL transmission with SRS based CSI acquisition assisted by other assistant information reporting

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Other Aspects related to CSI]`

**Agreement** · `10.5.3.3` Other aspects · `RAN1#124bis:10.5.3.3:007` · 관련 주제: CSI 보고/codebook

> For the purpose of performance evaluation of joint DL/UL based CSI acquisition, consider the following SRS error model:
> - SRS error model
>   - is the estimated channel, is the channel response in frequency domain.  is the white complex Gaussian matrix with zero mean, and variance  is the scaling factor .
>   - The details of calculation on should be provided by each company and additional factors (e.g., SRS interference, non-perfect open loop power control, UE TX antenna gain imbalance modelling) may be considered.
>   - Examples on calculation of
>   - SINR refers to the underlying SINR of the SRS as received at the aNB
>     - for inter-cell SRS interference: UEs are randomly grouped to 4 groups in baseline cases, UEs in the same group (in different cells) would interfere with each other’s SRS
>     - Use pathloss for interference calculation
>   - Actual SRS transmission and estimation can be used instead of such modeling.
>   - Other models can be used by companies.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Other Aspects related to CSI]`

**Agreement** · `10.5.3.3` Other aspects · `RAN1#124bis:10.5.3.3:008` · 관련 주제: CSI 보고/codebook

> For the purpose of performance evaluation of joint DL/UL based CSI acquisition, consider the following antenna calibration error:
> - Antenna calibration error can be modeled as
>   - represents the downlink channel obtained using channel reciprocity at aNB side and has a dimension .
>   - is the uplink channel derived by SRS and has a dimension .
>   - is the number of antenna ports of UE,  is the number antenna ports of aNB.
>   - is the amplitude mismatch coefficient and could be modeled as subject to uniform or Gaussian distribution, e.g., Gaussian distribution with zero mean and variance X1=0.35 dB.
>   - is the phase mismatch coefficient and could be modeled as subject to uniform or Gaussian distribution, e.g., Gaussian distribution with zero mean and variance Y1=5 degrees.
>   - Other values on X1 and Y1 can be considered and reported by companies.
>   - is the amplitude mismatch coefficient and could be modeled as subject to uniform or Gaussian distribution, e.g., Gaussian distribution with zero mean and variance X2 dB.
>   - is the phase mismatch coefficient and could be modeled as subject to uniform or Gaussian distribution, e.g., Gaussian distribution with zero mean and variance Y2 degrees.
>   - Values on X2 and Y2 are reported by companies.
>   - The distribution of  and  can also be reported by companies.
>   - Both or either of aNB or UE-side antenna calibration error can be used in the simulation and is reported by companies.
>   - Note: For any scheme requiring UE DL/UL reciprocity, the feasibility of UE DL/UL reciprocity should be considered.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Other Aspects related to CSI]`

**Agreement** · `10.5.3.3` Other aspects · `RAN1#124bis:10.5.3.3:009` · 관련 주제: CSI 보고/codebook

> For the purpose of performance evaluation of joint DL/UL based CSI acquisition, study whether and how to model the uplink and downlink insertion loss difference. Example on uplink and downlink insertion loss difference model:
> - The uplink and downlink insertion loss difference by using the model , where  is a diagonal matrix with diagonal coefficient  representing the power ratio of the -th antenna with respect to the antenna that has highest power in dB scale. is the uplink channel derived by SRS and has a dimension .  The generation of  is reported by companies.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Other Aspects related to CSI]`

## RAN1#124 — 18건

**Agreement** · `8.2` Maintenance on NR MIMO Phase 5 · `RAN1#124:8.2:008` · 관련 주제: Beam management

> Adopt the following TPs for clause 7 and clause 7.4 for TS 38.213
> The corresponding CR for Rel-19 for TS 38.213 in R1-2601609 is endorsed.
> - Reason for change: (1) The RRC parameter for PL offset in 38.213 is not aligned with 38.331. (2) The text describing the determination of PL offset value for the case “if followUnifiedTCI-StateSRS is not provided for a SRS resource set…” is ambiguous. For example, regarding “when TCI-State or a TCI-UL-State includes pl-Offset”: it is not clear which of the TCI state or TCI-UL-State includes the pl-Offset. And furthermore, the pathlossOffset is included in but not associated with a TCI-State or a TCI-UL-State, which is the current description.
> - Summary of changes: (1) Update the RRC parameter name for PL offset to align with 38.331. (2) Update the text description for PL offset determination for the case “if followUnifiedTCI-StateSRS is not provided for a SRS resource set…”.
> - Consequences if not approved: (1) The RRC parameter in 38.213 is not aligned with 38.331 and (2) And the text describing the determination of PL offset value if followUnifiedTCI-StateSRS is not provided for a SRS resource set and for a SRS resource from the SRS resource set is not clear and there is a misalignment of whether the pathlossOffset is included in or associated with a TCI-State or a TCI-UL-State in the specification.
> | 7 Uplink Power control < Unchanged parts are omitted > - else, if followUnifiedTCI-StateSRS is not provided for a SRS resource set and for a SRS resource from the SRS resource set, the values of , , and SRS power control adjustment state are provided by p0AlphaSetforSRS or, if p0AlphaSetforSRS-SBFD is provided and for an SRS transmission in SBFD symbols, by p0AlphaSetforSRS-SBFD, associated with TCI-State or TCI-UL-State of an SRS resource with lowest SRS-ResourceId in the SRS resource set, a RS index for obtaining a pathloss estimate for the SRS transmission is provided by pathlossReferenceRS-Id-r17 associated with or included in the TCI-State or TCI-UL-State of an SRS resource with lowest SRS-ResourceId in the SRS resource set, and a value of a , when TCI-State or a TCI-UL-State includes pl-Offset, is provided by pl-Offset pathlossOffset, if any, associated with included in TCI-State or TCI-UL-State of an SRS resource with lowest SRS-ResourceId in the SRS resource set is the sum of the component and a component p0 provided by SRS-ResourceSet corresponding to the SRS resource set. In the remaining of this clause, except for clause 7.7.3, if in a PUSCH, PUCCH, or SRS transmission occasion a UE applies a TCI-State or a TCI-UL-State that includes pl-Offset pathlossOffset with value in dB, where can be updated by a MAC CE [11, TS 38.321], the UE sets . < Unchanged parts are omitted > 7.4 Physical random access channel < Unchanged parts are omitted > If a PRACH transmission from a UE is in response to a detection of a PDCCH order by the UE that triggers a contention-free random access procedure, and if a pathloss offset indicator field in the PDCCH order [5, TS 38.212] indicates to the UE to apply pl-Offset pathlossOffset that is included in an indicated TCI-State or a TCI-UL-State and has value in dB, where can be updated by a MAC CE [11, TS 38.321], the UE sets for the PRACH transmission. < Unchanged parts are omitted > |

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601519](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601519.zip) · `[124-R19-MIMO]`

**Agreement** · `9.2.1` Improvement of SRS capacity and coverage · `RAN1#124:9.2.1:001`

> For , the following exact patterns of starting position hopping within a hop across repetition symbols  can be supported for a given  according to the configured , as derived from the corresponding basic pattern and :
> - {0,…,0, 1,…,1} and {1,…,1, 0,…,0} when .
> - {0,…,0, 2,…,2}, {1,…,1, 3,…,3}, {2,…,2, 0,…,0} and {3,…,3, 1,…,1} when  and .
> - {0,…,0, 2,…,2, 1,…,1, 3,…,3}, {1,…,1, 3,…,3, 2,…,2, 0,…,0}, {2,…,2, 0,…,0, 3,…,3, 1,…,1} and {3,…,3, 1,…,1, 0,…,0, 2,…,2} when .

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2600321](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2600321.zip)

**Conclusion** · `9.2.1` Improvement of SRS capacity and coverage · `RAN1#124:9.2.1:002`

> For intra-repetition hopping for SRS repetition symbols within each SRS frequency hop, the case when R is not an integer multiple of K is not supported.

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2600321](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2600321.zip)

**Agreement** · `9.2.1` Improvement of SRS capacity and coverage · `RAN1#124:9.2.1:003`

> Support PUSCH transmission with a priority index 0 and corresponding DMRS after all the SRS resource(s) of the same resource set with time-domain resource allocation entirely in the U slot for scenario 1 and scenario 2 (if scenario 2 is agreed).

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2600321](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2600321.zip)

**Agreement** · `9.2.1` Improvement of SRS capacity and coverage · `RAN1#124:9.2.1:004`

> For the time-domain location determination of aperiodic SRS resources within the cross-slot resource set, introduce per-resource slot offset.
>     - FFS: whether offset is included in the resource configuration or resource set configuration
> The slot offset configured to an AP cross-slot SRS resource refers to the first of the two slots spanned by the SRS resource.

남은 FFS 1건

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2600322](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2600322.zip)

**Agreement** · `9.2.1` Improvement of SRS capacity and coverage · `RAN1#124:9.2.1:005`

> Scenario 2: an aperiodic SRS resource set which includes at least one SRS resource with time-domain resource transmitted in a first S slot, and at least one another SRS resource with time-domain resource transmitted in a second consecutive U slot.
>   - For an aperiodic cross-slot SRS resource set in scenario 2, the slot offset of the SRS resource set refers to the first of the two slots spanned by the SRS resource set.

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2600322](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2600322.zip)

**Agreement** · `9.2.1` Improvement of SRS capacity and coverage · `RAN1#124:9.2.1:006`

> Support Alt B from the agreement in RAN1 #123 meeting as follows:
> There is no restriction on simultaneous enabling of the R17 RPFS start RB index hopping across multiple legacy SRS frequency hopping periods and intra-repetition hopping for SRS repetition symbols within each SRS frequency hop.
> For PF=4 and K=2, support RPFS start RB index hopping across multiple legacy SRS frequency hopping periods with new pattern(s) for intra-repetition hopping for SRS repetition symbols within each SRS frequency hop.
> - support new starting RB hopping pattern {0, 1}
> Note: The cases , , and ,  can be discussed separately.

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2600322](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2600322.zip)

**Agreement** · `9.2.2` Enhancing DL CSI acquisition · `RAN1#124:9.2.2:002` · 관련 주제: CSI 보고/codebook, CSI-RS

> Support a MAC-CE in MSG4 PDSCH for triggering aperiodic SRS-AS/CSI-RS indicates at least
> - The slot offset used to determine the transmission slot of aperiodic SRS-AS if triggered,
> - The slot offset used to determine the transmission slot of aperiodic CSI-RS associated with AP CSI reporting if triggered, and
> - The slot offset used to determine the transmission slot of aperiodic CSI-RS of the first TRS burst, if triggered.
> - The slot offset used to determine the transmission slot of the PUSCH for aperiodic CSI reporting, if triggered, via the UL grant provided in the MAC-CE
>   - FFS: How to indicate the slot offset by the UL grant provided in the MAC-CE
> Note: Whether to indicate the other settings (i.e., comb offset, repetition factor, cyclic shift and the number of TRS bursts, the parameters (e.g., slot offset, time gap) to determine the Tx slot(s) of the TRS burst(s), if triggered, other than the first TRS burst) via MAC-CE in MSG4 are separately discussed.

남은 FFS 1건

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2600647](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2600647.zip)

**Agreement** · `9.2.2` Enhancing DL CSI acquisition · `RAN1#124:9.2.2:004` · 관련 주제: CSI 보고/codebook, CSI-RS

> To determine the transmission/reception slot of the DL/UL signalling triggered/scheduled based on a legacy SCell activation command (i.e., aperiodic SRS-AS, aperiodic CSI-RS and the PUSCH scheduled for aperiodic CSI reporting), for applying a slot offset between a reference slot and a transmission/reception slot of the DL/UL signalling triggered/scheduled based on the legacy SCell activation command, the reference slot is the first slot that is 3ms after UE transmits HARQ-ACK for the PDSCH carrying the SCell activation command

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2600647](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2600647.zip)

**Agreement** · `9.2.2` Enhancing DL CSI acquisition · `RAN1#124:9.2.2:005` · 관련 주제: CSI 보고/codebook, CSI-RS

> To determine the transmission/reception slot of a MSG4-triggered DL/UL signalling (i.e., aperiodic SRS-AS, aperiodic TRS, aperiodic CSI-RS and the PUSCH scheduled for aperiodic CSI reporting), for applying a slot offset between a reference slot and a transmission/reception slot of the MSG4-triggered DL/UL signalling, the reference slot is the first slot that is 3ms after UE transmits HARQ-ACK for the MSG4 PDSCH carrying the MAC-CE.

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2600647](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2600647.zip)

**Agreement** · `9.2.2` Enhancing DL CSI acquisition · `RAN1#124:9.2.2:006` · 관련 주제: CSI 보고/codebook

> For SCell transition from deactivation to activation, at least support triggering early aperiodic SRS and/or early aperiodic CSI reporting based on Rel-17 fast SCell activation MAC-CE.
> - FFS: Support of triggering early aperiodic SRS and/or early aperiodic CSI reporting based on Rel-15 SCell activation MAC-CE

남은 FFS 1건

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2600648](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2600648.zip)

**Agreement** · `9.2.2` Enhancing DL CSI acquisition · `RAN1#124:9.2.2:010` · 관련 주제: CSI 보고/codebook, CSI-RS

> On triggering mechanism for early SRS/CSI-RS/CSI, via a DCI indicating switching out of dormancy for an SCell(s) based on legacy UE-specific DCI formats (e.g., DCI format 0_1/0_3/1_1/1_3),
> - For triggering aperiodic SRS-AS, the SRS resource set(s) triggered for the SCell(s) is determined according to ‘SRS request’ field in the legacy DCI format 0_1/0_3/1_1/1_3 indicating switching out of dormancy for the SCell(s)
>   - FFS: How to determine the serving cell(s) triggered with aperiodic SRS
>   - FFS: How to coexist with legacy triggering mechanism for aperiodic SRS
> - For triggering aperiodic CSI reporting and associated CSI-RS for CSI, the CSI report configuration(s) triggered for the SCell(s) is determined according to ‘CSI request’ field in the DCI formats 0_1/0_3 indicating switching out of dormancy for the SCell(s)
>   - Note: UE determines the serving cell(s) which the associated CSI-RS is triggered for, via carrier configured in the CSI report configuration(s), where the CSI report configuration(s) is determined according to the ‘CSI request’ field.
>   - Note: No additional RAN1 spec enhancement is needed to support aperiodic CSI reporting
> Note: Legacy DCI format(s) for switching out of SCell dormancy is reused without introducing new DCI field or resizing the existing DCI field.

남은 FFS 2건

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2600649](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2600649.zip)

**Agreement** · `9.2.2` Enhancing DL CSI acquisition · `RAN1#124:9.2.2:011`

> On how to determine the serving cell(s) triggered with aperiodic SRS via ‘SRS request’ field in a DCI indicating switching out of dormancy based on legacy DCI formats 0_1/0_3/1_1/1_3, study the following alternatives:
> - Alt-1: The SRS trigger state indicated in ‘SRS request’ field applies to,
>   - The cell(s) scheduled by legacy mechanism and configured with aperiodic SRS resource set(s) associated with the SRS trigger state; and
>   - The SCell(s) which is indicated with switching out of dormancy and configured with aperiodic SRS resource set(s) for SRS-AS associated with the SRS trigger state.
> - Alt-2: For DCI format 0_1/1_1, support “Carrier Indicator” field in the DCI to indicate the serving cell(s) triggered with aperiodic SRS, if the “Carrier Indicator” field indicates non-zero value.
> Note: The other alternative(s) is not precluded.

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2600649](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2600649.zip)

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#124:10.5.3.2:001` · 관련 주제: CSI 보고/codebook

> Study at least the following aspects of SRS for uplink and downlink CSI acquisition:
> - Efficient support of larger channel bandwidth
> - Capacity enhancements
> - Coverage enhancements
> - Efficient resource utilization
> - Dynamic/flexible adaptation of SRS parameters
> - mTRP transmission/reception, FWA, HST and other high mobility scenarios
> - Interference mitigation
> - Energy efficiency

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · `[124-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#124:10.5.3.2:002` · 관련 주제: Beam management, CSI 보고/codebook

> For UL-based CSI acquisition, study at least the following SRS usages:
> - CSI acquisition for UL transmission
> - CSI acquisition for DL transmission
> - Beam management
> - Other usages are not precluded

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · `[124-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#124:10.5.3.2:003` · 관련 주제: CSI 보고/codebook

> Adopt the assumptions in the following table as the basic assumption of SLS for evaluation of UL-based CSI acquisition.
> Table: SLS assumption for DL CSI and UL CSI
> | Parameters | Assumptions for DL CSI | Assumptions for UL CSI |
> | #1 Carrier frequency | Reuse SLS assumptions of DL-based CSI(10.5.3.1) Around 700MHz (FDD) Around 2 GHz (FDD) Around 4 GHz (TDD) Around 7 GHz (TDD) Other carrier frequency is not precluded | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Around 0.7 GHz, FDD Around 2 GHz, FDD Around 4 GHz, TDD Around 7 GHz, TDD Around 30 GHz, TDD |
> | #2 Simulation bandwidth | Reuse SLS assumptions of DL-based CSI(10.5.3.1) 20MHz 100MHz (not applicable for 700MHz) Other BW is not precluded System/channel bandwidth assumption is reported by companies. | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) 20 MHz (baseline) 100 MHz (for 4—7 GHz) (optional) Other bandwidths are not precluded (companies to report) |
> | #3 Precoding granularity | Company report the precoder granularity | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Company can report |
> | #4 Scenario | Reuse SLS assumptions of DL-based CSI(10.5.3.1) Note: Reuse SLS assumption for PDSCH | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Suburban macro, 1732 m ISD (for around 0.7—4 GHz) Urban macro, 500 m ISD (for around 0.7—30 GHz) Dense urban, 200 m ISD (for around 4—30 GHz) Urban Macro (500m), one-layer deployment, two-layer deployment (Optional) Dense urban (200m), one-layer deployment, two-layer deployment (Optional) Urban Grid (Optional) Other scenarios are not precluded (companies to report) |
> | #5 UE number/cell | Reuse SLS assumptions of DL-based CSI(10.5.3.1) Other numbers is not precluded. | Company to report |
> | #6 Layout/deployment | Reuse SLS assumptions of DL-based CSI(10.5.3.1) 1-ring (7*3), 2-ring (19*3) Other layout/deployment are not precluded. | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) 7 x 3, single layer, hex grid (baseline) 7 x 3 two layers, macro layer: hex grid; micro layer: locations of micro sites are reported by company (optional) 19 x 3, single layer, hex grid (optional) |
> | #7 Channel model | Reuse SLS assumptions of DL-based CSI(10.5.3.1) Rel-19 TR 38.901 Note: spatial consistency could be considered, if applicable | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) |
> | #8 Numerology | Reuse SLS assumptions of DL-based CSI(10.5.3.1) OFDM, 15 kHz for FDD, 30 kHz for TDD | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) 15 kHz for FDD 30 kHz for TDD and around 2—7 GHz 120 kHz for TDD and around 30 GHz |
> | #9 Transmit power (per 20MHz) | Reuse SLS assumptions of DL-based CSI(10.5.3.1) Dense urban: 44dBm Urban macro: 46dBm Suburban Marco:49dBm Other values can be reported by companies. Note: For evaluation purpose, BS Tx power scales up with bandwidth proportionally under the limitation of the maximum BS Tx power is 56dBm for outdoor and 33dBmfor indoor for the above carrier frequencies. | NA |
> | #10 BS antenna configuration | Reuse the assumption under AI 10.5.3.1 when applicable, otherwise refer to AI 10.1 | Reuse the assumption under AI 10.5.2.3 when applicable, otherwise refer to AI 10.1 |
> | #11 UE power class | Reuse SLS assumptions of DL-based CSI(10.5.3.1) 23dBm, 26dBm[,29dBm] | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) 23dBm, 26dBm[,29dBm] |
> | #12 UE antenna configuration | Reuse SLS assumptions of DL-based CSI(10.5.3.1) Details follow corresponding agreements in Agenda 10.1 | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Details follow corresponding agreements in Agenda 10.1. Other antenna location/configuration are not precluded and can be considered. |
> | #13 UE Receiver | Reuse SLS assumptions of DL-based CSI(10.5.3.1) MMSE-IRC (baseline) R-ML (Reported by companies) | NA |
> | gNB receiver | NA | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Baseline: MMSE-IRC Other can be reported |
> | #14 Traffic model | Reuse SLS assumptions of DL-based CSI(10.5.3.1) FTP Model 1/3 (0.5 Mbyte packet sizes) Low RU about 30% Medium RU about 50% High RU about 70% Other model is not precluded. | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) |
> | #15 Scheduling | Reuse SLS assumptions of DL-based CSI(10.5.3.1) PF | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Proportional fair |
> | #16 Inter-cell interference model | Reuse SLS assumptions of DL-based CSI(10.5.3.1) Explicitly and realistically modelled | Explicitly and realistically modelled |
> | #17 Channel estimation assumption | Realistic as the baseline Companies to report the detailed SRS channel estimation error model | Realistic as the baseline Companies to report the detailed SRS channel estimation error model |
> | #18 SRS periodicity | 5ms, 10ms, 20ms, 40ms, 80ms, 160ms Companies to state the simulated SRS periodicity if other values are used. Note: SRS triggering may be aperiodic Scheduling delay: Minimum [4ms] from CSI measurement to CSI application. | 5ms, 10ms, 20ms, 40ms, 80ms, 160ms Companies to state the simulated SRS periodicity if other values are used. Note: SRS triggering may be aperiodic Scheduling delay: Minimum [4ms] from CSI measurement to CSI application. |
> | #19 MIMO scheme | Reuse SLS assumptions of DL-based CSI(10.5.3.1) SU-MIMO MU-MIMO with rank adaptation NR CW-to-layer mapping is used and other mapping is not precluded. | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Depending on PUSCH scheme Reported by company (e.g., SU/MU-MIMO, max rank) |
> | #21 Evaluation Metric | DL throughput as baseline metrics Other KPI is not precluded. | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Throughput Additional assumption of average UPT, 5%-tile UPT, 50%-tile UPT, 95%-tile UPT |
> | #24 Calibration error modeling for other antennas | Reuse SLS assumptions of DL-based CSI(10.5.3.1) FFS |  |
> | #25gNB noise figure | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Around 7 GHz and below: 5dB Around 15 GHz and above: 7dB | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Around 7 GHz and below: 5dB Around 15 GHz and above: 7dB |
> | #26UE noise figure | Reuse general assumption |  |
> | #27 Impairments | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Company can report (according to use case / scenario / scheme) e.g., UE coherence modeling, Tx power imbalance, relative phase error, DL&UL reciprocity | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Company can report (according to use case / scenario / scheme) e.g., UE coherence modeling, Tx power imbalance, relative phase error, DL&UL reciprocity |
> | #28 power control | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Company can report | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Company can report |
> | #29 UE speed | Reuse SLS assumptions of downlink transmission schemes(10.5.2.2) | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Urban macro and dense urban: indoor (3 km/h), outdoor (30km/h) Suburban macro: indoor (3 km/h), outdoor (40km/h) additional assumption of 0.3 km/h for FWA |
> - Note: EVM assumption for HST scenarios will be treated separately

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · `[124-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#124:10.5.3.2:004` · 관련 주제: CSI 보고/codebook

> Adopt the assumptions in the following table as the basic assumption of LLS for evaluation of UL-based DL CSI acquisition.
> | Parameters | Assumptions for DL CSI |
> | #1 Carrier frequency | Reuse assumptions of DL-based CSI(10.5.3.1) Around 700MHz (FDD) Around 2 GHz (FDD) Around 4 GHz (TDD) Around 7 GHz (TDD) |
> | #2 RB allocation for PDSCH | Reuse assumptions of DL-based CSI(10.5.3.1) 24RB, 48RB, others are not precluded |
> | #2a Channel BW | Reuse assumptions of DL-based CSI(10.5.3.1) Depend on carrier frequency. Companies to report the assumed channel BW. |
> | #3 Waveform and numerology for DL | Reuse assumptions of DL-based CSI(10.5.3.1) CP-OFDM, 15 kHz for FDD, 30 kHz for others |
> | #4 Channel model | Reuse assumptions of DL-based CSI(10.5.3.1) CDL-A/B/C/D/E in TR 38.901 Possible DS values = {10, 30, 100, 300, 1000} ns. ASA, ASD, ZSA, ZSD follow the values in sec 7.7.1 in TR 38.901 Companies to report how randomization is performed if considered |
> | #5 UE speed | Reuse assumptions of DL-based CSI(10.5.3.1) 3 km/h, 30 km/h, 120km/h, 350km/h, 500km/h |
> | #6 PRG | Reuse assumptions of DL-based CSI(10.5.3.1) 2 RBs, 4 RBs as start point for evaluation Other values are not precluded |
> | #7 BS antenna configuration | Reuse assumptions of DL-based CSI(10.5.3.1) |
> | #8 UE antenna configuration | Reuse assumptions of DL-based CSI(10.5.3.1) Follow agreements in agenda 10.1 |
> | #9 MIMO scheme | Reuse assumptions of DL-based CSI(10.5.3.1) SU-MIMO, MU-MIMO. |
> | #10 Receiver type | Reuse assumptions of DL-based CSI(10.5.3.1) MMSE-IRC or RML for DL |
> | #11 CW to layer mapping | Reuse assumptions of DL-based CSI(10.5.3.1) NR CW to layer mapping (baseline) Other codeword-to-layer mapping options are not precluded |
> | #12 Channel coding | Reuse assumptions of DL-based CSI(10.5.3.1) LDPC for PDSCH, Polar for CSI (for evaluation benchmark), when applicable |
> | #13 MCS | Reuse assumptions of DL-based CSI(10.5.3.1) For PDSCH: QPSK (1/5, 1/3), 16QAM (2/5, 1/2, 3/4), 64QAM (1/2, 2/3, 5/6), 256QAM (2/3, 5/6) |
> | #14 Channel estimation | Reuse assumptions of DL-based CSI(10.5.3.1) Realistic as baseline Companies to report the detailed SRS channel estimation. |
> | #15 Link adaptation | Reuse assumptions of DL-based CSI(10.5.3.1) AMC/fixed MCS |
> | #16 KPIs | Reuse assumptions of DL-based CSI(10.5.3.1) Intermediate KPIs: SGCS/NMSE BLER, SE/throughput |
> | #19 SRS periodicity | 5ms, 10ms, 20 ms, 40ms, 80ms, 160ms Company to report if other assumptions are used |
> | #20 Scheduling delay | Reuse assumptions of DL-based CSI(10.5.3.1) Minimum [4ms] from CSI measurement to CSI application Companies to report if other assumptions are used |
> | #23 SNR difference between DL and UL | Company to report the value of SNRDL-SNRUL |
> | #24 SRS transmission parameters | Company to report the SRS parameters such as comb, sequence, etc |
> | #25 Impairments | Reuse SLS assumptions of uplink transmission schemes(10.5.2.3) Company can report (according to use case / scenario / scheme) e.g., UE coherence modeling, Tx power imbalance, relative phase error, DL&UL reciprocity |

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · `[124-R20-6GR-Aspects of UL based CSI acquisition]`

**Agreement** · `10.5.3.2` Aspects of uplink-based CSI acquisition · `RAN1#124:10.5.3.2:005` · 관련 주제: CSI 보고/codebook

> For LLS for UL-based UL CSI acquisition, reuse the LLS assumption for uplink transmission schemes under AI 10.5.2.3.

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · `[124-R20-6GR-Aspects of UL based CSI acquisition]`

## RAN1#123 — 11건

**Agreement** · `10.2.1` Improvement of SRS capacity and coverage · `RAN1#123:10.2.1:001`

> For intra-repetition hopping for SRS repetition symbols within each SRS frequency hop with R>K, support Alt-1  :
> - when PF=K=2, select at least one of the following basic patterns:
>   - Alt 1 (consecutive mapping): {0,…,0,1,…,1}
>   - Alt 2 (non-consecutive mapping): {0,1,,…,0,1}
> - when PF=4 and K=2, down select from the following basic patterns:
>   - Alt 1 (consecutive mapping):{0,…,0,2,…,2}
>   - Alt 2 (non-consecutive mapping): {0,2,…,0,2}
> - when PF=K=4, down select from the following basic patterns:
>   - Alt 1 (consecutive mapping): {0,…,0,2,…,2,1,…,1,3,…,3}
>   - Alt 2 (non-consecutive mapping): {0,2,1,3,…,0,2,1,3}
> Intra-repetition hopping for SRS repetition symbols within each SRS frequency hop is supported when R is integer multiple of K.

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx)

**Agreement** · `10.2.1` Improvement of SRS capacity and coverage · `RAN1#123:10.2.1:002`

> For K=R, the following exact patterns of starting position hopping within a hop across repetition symbols can be supported for a given K according to the configured PF, as derived from the corresponding basic pattern and :
> -            {0, 1} and {1, 0} when
> -            {0, 2}, {1, 3}, {2, 0} and {3, 1} when   and
> -            {0, 2, 1, 3}, {1, 3, 2, 0}, {2, 0, 3, 1} and {3, 1, 0, 2} when
> Parameter   is given by legacy higher-layer parameter StartRBIndex if configured, otherwise
> Note: Which of the multiple patterns to use is determined at least by kF

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx)

**Agreement** · `10.2.1` Improvement of SRS capacity and coverage · `RAN1#123:10.2.1:003`

> Alt A:
> There is no restriction on simultaneous enabling of the R17 RPFS start RB index hopping across multiple legacy SRS frequency hopping periods and intra-repetition hopping for SRS repetition symbols within each SRS frequency hop.
> Note: There is no new pattern.
> Alt B:
> There is no restriction on simultaneous enabling of the R17 RPFS start RB index hopping across multiple legacy SRS frequency hopping periods and intra-repetition hopping for SRS repetition symbols within each SRS frequency hop.
> For PF=4 and K=2, support RPFS start RB index hopping across multiple legacy SRS frequency hopping periods with new pattern(s) for intra-repetition hopping for SRS repetition symbols within each SRS frequency hop.
> Select one alternative from the following alternatives:
> - Alt 1: support new starting RB hopping pattern {0, 1, 2, 3}
> - Alt 2: support new starting RB hopping pattern {0, 1}
> - Alt 3: start RB hopping in each SRS FH period group including two adjacent periods is used to probe all subbands, and start RB hopping across different SRS FH period groups is determined by pseudo random sequence.
> Note: The cases , , and ,  can be discussed separately.

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx)

**Agreement** · `10.2.1` Improvement of SRS capacity and coverage · `RAN1#123:10.2.1:004`

> 0 or more SRS resource with time-domain resource entirely in the second slot (i.e., U slot) can be supported in scenario 1.

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx)

**Agreement** · `10.2.1` Improvement of SRS capacity and coverage · `RAN1#123:10.2.1:005`

> For cross-slot SRS resource between one U slot and one adjacent S slot, the maximum number of repetition factor is limited to 14.

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx)

**Agreement** · `10.2.1` Improvement of SRS capacity and coverage · `RAN1#123:10.2.1:006`

> The maximum number of symbols per cross-slot SRS resource is limited to 14:

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx)

**Agreement** · `10.2.1` Improvement of SRS capacity and coverage · `RAN1#123:10.2.1:007`

> Support cross-slot SRS for SRS resource with repetition and without repetition.

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx)

**Agreement** · `10.2.1` Improvement of SRS capacity and coverage · `RAN1#123:10.2.1:008`

> Support the following regarding “available slot” determination of aperiodic SRS (i.e. Alt 0 from the agreement RAN1#122).
> - The available slot(s) can include one slot or two consecutive S and U slots satisfying there are UL or flexible symbol(s) for the time-domain location(s) for all the SRS resources in the resource set and it satisfies UE capability on the minimum timing requirement between triggering PDCCH and all the SRS resources in the resource set.

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx)

**Conclusion** · `10.2.2` Enhancing DL CSI acquisition · `RAN1#123:10.2.2:001` · 관련 주제: CSI 보고/codebook, CSI-RS

> For UE transition from IDLE/INACTIVE to CONNECTED mode, there is no RAN1 consensus to support the following cases triggered by MSG4 of 4-Step RACH:
> - Periodic and semi-persistent SRS-AS
> - Periodic and semi-persistent CSI-RS for CSI associated with aperiodic CSI reporting

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2508520](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2508520.zip)

**Conclusion** · `10.2.2` Enhancing DL CSI acquisition · `RAN1#123:10.2.2:002` · 관련 주제: CSI 보고/codebook, CSI-RS

> For SCell transition from deactivation to activation, there is no RAN1 consensus to support the following cases triggered based on legacy SCell activation command:
> - Periodic and semi-persistent SRS
> - Periodic and semi-persistent CSI-RS for CSI associated with aperiodic CSI reporting

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2508520](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2508520.zip)

**Agreement** · `10.2.2` Enhancing DL CSI acquisition · `RAN1#123:10.2.2:005` · 관련 주제: CSI 보고/codebook, CSI-RS

> On triggering mechanism for early aperiodic SRS-AS transmission on a SCell and early aperiodic CSI reporting and associated aperiodic CSI-RS for CSI for a SCell, based on the legacy SCell activation activating the SCell, support Alt-2, i.e.,
> - For early aperiodic SRS-AS transmission, the SRS resource set(s) triggered for the SCell is determined according to an indication in SCell activation command.
> - For early aperiodic CSI reporting and associated aperiodic CSI-RS for CSI, the CSI report configuration(s) triggered for the SCell is determined according to an indication in SCell activation command.

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2508520](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2508520.zip)

## RAN1#122bis — 17건

**Agreement** · `8.2` Maintenance on NR MIMO Phase 5 · `RAN1#122bis:8.2:014` · 관련 주제: CSI 보고/codebook

> Adopt the following corrections for TS 38.211, TS 38.213 and TS 38.214.
> Reason for change: Adapt to the agreed terminology.
> Summary of change: Correct the relevant RRC parameter to “fourPortSRS-3Tx”.
> Consequence if not changed: Incorrect/Incomplete referencing.
> | TS 38.211: 6.3.1.5 Precoding --------------------------------------------Unchanged parts are omitted------------------------------------------ For codebook-based transmission, the precoding matrix depends on the number of antenna ports used for the transmission: - for single-layer transmission on a single antenna port, ; - for transmissions using 2, or 4 antenna ports, is given by Tables 6.3.1.5-1 to 6.3.1.5-7; - for transmissions using 3 antenna ports when fourPortSRS-3Tx 4portSRS_3TX is configured, is given by Tables 6.3.1.5-48 to 6.3.1.5-50; --------------------------------------------Unchanged parts are omitted------------------------------------------ Table 6.3.1.5-48: Precoding matrix for single-layer transmission using three antenna ports with fourPortSRS-3Tx 4portSRS_3TX configured. --------------------------------------------Unchanged parts are omitted------------------------------------------ Table 6.3.1.5-49: Precoding matrix for two-layer transmission using three antenna ports with fourPortSRS-3Tx 4portSRS_3TX configured. --------------------------------------------Unchanged parts are omitted------------------------------------------ Table 6.3.1.5-50: Precoding matrix for three-layer transmission using three antenna ports with fourPortSRS-3Tx 4portSRS_3TX configured. --------------------------------------------Unchanged parts are omitted------------------------------------------ 6.4.1.4.3 Mapping to physical resources --------------------------------------------Unchanged parts are omitted------------------------------------------ - for an SRS resource in an SRS resource set with the higher-layer parameter fourPortSRS-3Tx 4portSRS_3TX is configured, - otherwise, --------------------------------------------Unchanged parts are omitted------------------------------------------ |
> | TS 38.213: 7.3 Sounding reference signals --------------------------------------------Unchanged parts are omitted------------------------------------------ For SRS, - if a UE is provided nrofSRS-Ports-n8 = 'ports8tdm' for an SRS resource with 8 ports in an SRS resource set with usage 'codebook' or 'antennaSwitching', the UE splits a linear value of the transmit power on active UL BWP of carrier of serving cell equally across the SRS ports of an SRS resource of an SRS resource set on each symbol for SRS transmission. - else if a UE is provided fourPortSRS-3Tx 4portSRS_3TX for an SRS resource set with usage ‘codebook’ or ‘antennaSwitching’, the UE splits a linear of the transmit power on active UL BWP of carrier of serving cell equally across the SRS ports without port 1003 of an SRS resource of an SRS resource set in a symbol for SRS transmission. --------------------------------------------Unchanged parts are omitted------------------------------------------ |
> | TS 38.214: 6.2.1 UE sounding procedure --------------------------------------------Unchanged parts are omitted------------------------------------------ The UE does not transmit SRS on antenna port 1003 if fourPortSRS-3Tx is configured., where fourPortSRS-3Tx [RRC parameter] is only applicable to 4-port SRS resource(s) in an SRS resource set with usage set to ‘codebook’ or ‘antennaSwitching’. --------------------------------------------Unchanged parts are omitted------------------------------------------ 6.2.1.2 UE sounding procedure for DL CSI acquisition --------------------------------------------Unchanged parts are omitted------------------------------------------ For 1T=1R, 2T=2R, 3T=3R, 4T=4R or 8T=8R, up to two SRS resource sets each with one SRS resource can be configured, where the number of SRS ports for each resource is equal to 1, 2, 4 with port 1003 disabled by configured higher layer parameter fourPortSRS-3Tx [RRC parameter], 4 or 8 if the UE is not indicating srs-AntennaSwitching2SP-1Periodic or [srs-AntennaSwitching3T3R2SP-1Periodic] or srs-AntennaSwitching8T8R2SP-1Periodic. Up to two SRS resource sets configured with resourceType in SRS-ResourceSet set to 'semi-persistent' and one SRS resource set configured with resourceType in SRS-ResourceSet set to 'periodic' can be configured and the two SRS resource sets configured with 'semi-persistent' are not activated at the same time, or up to two SRS resource sets can be configured, if the UE is indicating srs-AntennaSwitching2SP-1Periodic, srs-AntennaSwitching8T8R2SP-1Periodic, or [srs-AntennaSwitching3T3R2SP-1Periodic], where each SRS resource set has one SRS resource, the number of SRS ports for each resource is equal to 1, 2, 4 with port 1003 disabled by configured higher layer parameter fourPortSRS-3Tx, 4, or 8 or --------------------------------------------Unchanged parts are omitted------------------------------------------ |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2506791](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2506791.zip) · `[122bis-R19-MIMO]`

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122bis:9.2:022` · 관련 주제: CSI 보고/codebook, CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-4 | Association up to 128 CSI-RS ports and SRS for non-codebook-based PUSCH | 1. Support association between {48, 64, 128} CSI-RS ports and SRS resource set for non-codebook-based PUSCH 2. A list of supported combinations, each combination is {Max # of Tx ports in a set of aggregated resources, Max # of sets of aggregated resource, and total # of Tx ports} simultaneously | 2-15 | Yes | n/a | Association up to 128 CSI-RS ports and SRS for non-codebook-based PUSCH is not supported | Per FS | n/a | n/a | n/a | Component 2 candidate value: Maximum size of the list is 16. The candidate values for the max # of Tx port in in a set of aggregated resources is {48, 64, 128} The candidate value set of the max # of sets of aggregated resource is: {2, …, 64} The candidate value set of total # of ports is: {48, …, 256, 512, 768, 1024} Note: Component 2 is reported per BC | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508081](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508081.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122bis:9.2:032`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-3-3 | 3T6R Antenna switching | 1. Support of 3T6R SRS Tx port switching with port 1003 disabled when 4 port SRS resources with port 1003 disabled are configured to the UE 2. Report the entry number of the first-listed band with UL in the band combination that affects this DL 3. Report the entry number of the first-listed band with UL in the band combination that switches together with this UL |  | yes | n/a | 3TX 3T6R antenna switching is not supported | Per FS | n/a | n/a | n/a | Component 2 candidate value: {1,2, … 32} Component 3 candidate value: {1,2, … 32} Note: This UE feature can be signalled together with srs-AntennaSwitching8T8R-r18, srs-AntennaSwitchingBeyond4RX-r17, supportedSRS-TxPortSwitch-v1610, or supportedSRS-TxPortSwitch or 59-3-3a to indicate SRS antenna switching downgrading capability. | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508081](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508081.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122bis:9.2:034` · 관련 주제: Beam management

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-4-9a | DCI format 1_1 to indicate one of two separate SRS closed loop indexes under separate DL/UL TCI state mode | Support of DCI format 1_1 to indicate one or of two separate SRS closed loop index(es) under separate DL/UL TCI state mode | 59-4-8 | yes | n/a | DCI 1_1 indicating one of two separate SRS closed loop indexes under separate DL/UL TCI state mode is not supported | Per band | n/a | n/a | n/a |  | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-4-9b | DCI format 1_1 to indicate one of two separate SRS closed loop indexes under joint TCI state mode | Support of DCI format 1_1 to indicate one or of two separate SRS closed loop index(es) under joint TCI state mode | 59-4-8 | yes | n/a | DCI 1_1 indicating one of two separate SRS closed loop indexes under joint TCI state mode is not supported | Per band | n/a | FR1 only | n/a |  | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508081](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508081.zip)

**Agreement** · `10.2.1` Improvement of SRS capacity and coverage · `RAN1#122bis:10.2.1:001`

> For intra-repetition hopping for SRS repetition symbols within each SRS frequency hop and K=R (i.e., each subgroup includes  symbol (or 1 pair of consecutive symbols for 8-Tx SRS with ports8tdm))), the following configuration combinations and basic starting position patterns are supported
> - when PF=K=2, support pattern {0,1}
> - when PF=4 and K=2, select one of the following patterns:
>   - Alt 1: {0,2}
>   - Alt 2: {0,1}
> - when PF=K=4, select one of the following patterns:
>   - Alt 1: {0,2,1,3}
>   - Alt 2: {0,1,2,3}
> Note: exact pattern(s) are deduced from the basic patterns. FFS details.

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2507994](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2507994.zip)

**Agreement** · `10.2.1` Improvement of SRS capacity and coverage · `RAN1#122bis:10.2.1:002`

> For intra-repetition hopping for SRS repetition symbols within each SRS frequency hop and K<R (i.e., each subgroup includes  symbol (or >1 pair of consecutive symbols for 8-Tx SRS with ports8tdm)), support the following configuration combinations and basic starting position patterns
> - when PF=K=2, select at least one of the following basic patterns:
>   - Alt 1 (consecutive mapping): {0,…,0,1,…,1}
>   - Alt 2 (non-consecutive mapping): {0,1,,…,0,1}
> - when PF=4 and K=2, down select from the following basic patterns:
>   - Alt 1-1 (consecutive mapping):{0,…,0,2,…,2}
>   - Alt 1-2 (consecutive mapping):{0,...,0,1,…,1}
>   - Alt 2-1 (non-consecutive mapping):{0,2,…,0,2}
>   - Alt 2-2 (non-consecutive mapping): {0,1,…,0,1}
> - when PF=K=4, down select from the following basic patterns:
>   - Alt 1-1 (consecutive mapping): {0,…,0,2,…,2,1,…,1,3,…,3}
>   - Alt 1-2 (consecutive mapping): {0,…,0,1,…,1,2,…2,3,…,3}
>   - Alt 2-1 (non-consecutive mapping): {0,2,1,3,…,0,2,1,3}
>   - Alt 2-2 (non-consecutive mapping): {0,1,2,3,…,0,1,2,3}
> Note: exact patterns are deduced from the basic patterns. FFS details.

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2507994](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2507994.zip)

**Agreement** · `10.2.1` Improvement of SRS capacity and coverage · `RAN1#122bis:10.2.1:003`

> To determine the time-domain location of a cross-slot SRS resource,
> - ‘’ is interpreted as the starting symbol in the starting slot for an SRS resource.
> - ‘’ is interpreted as the symbol index in a slot or two consecutive S and U slots.
> - The restriction ‘’ is removed.

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508045](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508045.zip)

**Agreement** · `10.2.1` Improvement of SRS capacity and coverage · `RAN1#122bis:10.2.1:004` · 관련 주제: CSI 보고/codebook

> - For intra-repetition hopping for SRS repetition symbols within each SRS frequency, support periodic, semi-persistent and aperiodic SRS.
> - For intra-repetition hopping for SRS repetition symbols within each SRS frequency hop, support all SRS usages (i.e., codebook, nonCodebook, antennaSwitching and beamManagement)

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508045](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508045.zip)

**Agreement** · `10.2.1` Improvement of SRS capacity and coverage · `RAN1#122bis:10.2.1:005` · 관련 주제: Beam management, CSI 보고/codebook

> - Support cross-slot SRS for all SRS resource types, i.e., for periodic, semi-persistent, and aperiodic SRS.
> - Support cross-slot SRS for usages of codebook, non-codebook, antenna switching, beam management

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508045](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508045.zip)

**Agreement** · `10.2.1` Improvement of SRS capacity and coverage · `RAN1#122bis:10.2.1:006`

> For intra-repetition hopping for SRS repetition symbols within each SRS frequency hop, support Alt-1 from the agreement in RAN1#122bis as the following:
> - when PF=4 and K=2, select one of the following patterns:
>   - Alt 1: {0,2}
> - when PF=K=4, select one of the following patterns:
>   - Alt 1: {0,2,1,3}

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508087](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508087.zip)

**Agreement** · `10.2.1` Improvement of SRS capacity and coverage · `RAN1#122bis:10.2.1:007`

> - For an aperiodic cross-slot SRS resource set in scenario 1, the slot offset of the SRS resource set refers to the first of the two slots spanned by the SRS resource set.
> - Note 1: Whether 0 or more SRS resource with time-domain resource entirely in the second slot (i.e. U slot) can be supported in scenario 1 is discussed separately.
> - Note 2: If the transmission of 0 or more SRS resource with time-domain resource entirely in the second slot (i.e. U slot) is supported, for the resource(s) in the second slot, whether/how to utilize the slot offset configured for the SRS resource set is discussed separately.
> - Note 3: 0 or more SRS resource with time-domain resource entirely in the first slot (i.e. S slot) can be supported in scenario 1.

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508105](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508105.zip)

**WA** · `10.2.1` Improvement of SRS capacity and coverage · `RAN1#122bis:10.2.1:008`

> For intra-repetition hopping for SRS repetition symbols within each SRS frequency hop, support Alt-2:
> - when PF=K=2, select at least one of the following basic patterns:
>   - Alt 1 (consecutive mapping): {0,…,0,1,…,1}
>   - Alt 2 (non-consecutive mapping): {0,1,,…,0,1}
> - when PF=4 and K=2, down select from the following basic patterns:
>   - Alt 1 (consecutive mapping):{0,…,0,2,…,2}
>   - Alt 2 (non-consecutive mapping):{0,2,…,0,2}
> - when PF=K=4, down select from the following basic patterns:
>   - Alt 1 (consecutive mapping): {0,…,0,2,…,2,1,…,1,3,…,3}
>   - Alt 2 (non-consecutive mapping): {0,2,1,3,…,0,2,1,3}

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508105](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508105.zip)

**Agreement** · `10.2.2` Enhancing DL CSI acquisition · `RAN1#122bis:10.2.2:001`

> For early triggering of SRS-AS when SCell transition from a dormant BWP to a non-dormant BWP, support aperiodic SRS-AS transmission on the non-dormant BWP, triggered via a DCI indicating switching out of SCell dormancy.
> - Legacy DCI format(s) for switching out of SCell dormancy is reused without introducing new DCI field or resizing the existing DCI field
> - FFS: Which DCI format(s) from DCI format 0_1/0_3/1_1/1_3/2_6 is supported
> - FFS: Triggering mechanism(s)
> - FFS: Timeline of the aperiodic SRS-AS transmission (requirement is up to RAN4)

남은 FFS 3건

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2506838](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2506838.zip)

**Agreement** · `10.2.2` Enhancing DL CSI acquisition · `RAN1#122bis:10.2.2:005` · 관련 주제: CSI 보고/codebook, CSI-RS

> For UE transition from IDLE/INACTIVE to CONNECTED mode, using MAC-CE in the PDSCH for MSG4 to trigger early aperiodic SRS-AS/CSI-RS/CSI
> - Note: How to determine the PUSCH for aperiodic CSI reporting is separately discussed.

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2506839](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2506839.zip)

**Agreement** · `10.2.2` Enhancing DL CSI acquisition · `RAN1#122bis:10.2.2:008` · 관련 주제: CSI 보고/codebook, CSI-RS

> For early aperiodic SRS-AS/CSI-RS/CSI triggering (i.e., early triggering of aperiodic SRS-AS transmission, aperiodic CSI-RS reception, aperiodic CSI reporting) when UE transition from INACTIVE to CONNECTED mode, reuse the procedure for UE transition from IDLE to CONNECTED mode.

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2506839](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2506839.zip)

**Agreement** · `10.2.2` Enhancing DL CSI acquisition · `RAN1#122bis:10.2.2:009` · 관련 주제: CSI 보고/codebook

> For early triggering of SRS-AS when UE transition from IDLE/INACTIVE to CONNECTED mode, support Option-2 as follows:
> - In Step-1, SIBx provides one or multiple SRS configurations based on one or multiple ‘xTyR’ UE capability assumptions.
>   - At least one SRS configuration(s) resource sets for SRS-AS in an SRS configuration is provided for a same ‘xTyR’
>   - FFS: Information to be provided in SRS configuration(s)
>   - FFS: Whether Configuration information could be SRS configuration or the CSI report configuration for PMI-free report.
>   - FFS: Whether SRS configuration can be associated with CSI report configuration for PMI-free report.
> - In Step-2, UE reports through MSG3 which/whether the SRS configuration(s) provided in SIBx is/are supported.
>   - FFS: How to report which/whether the SRS configuration(s) provided in SIBx is/are supported.

남은 FFS 4건

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2506839](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2506839.zip)

**Agreement** · `10.2.2` Enhancing DL CSI acquisition · `RAN1#122bis:10.2.2:012` · 관련 주제: CSI 보고/codebook

> On triggering mechanism for early aperiodic SRS-AS transmission on a SCell and early aperiodic CSI reporting for a SCell, based on the legacy SCell activation activating the SCell, down-select one from the followings in RAN1#123 meeting:
> - Alt-1 (Implicit mechanism):
>   - For early aperiodic SRS-AS transmission, the SRS resource set(s) triggered for the SCell is determined according to RRC configuration.
>   - For early aperiodic CSI reporting, the CSI report configuration(s) triggered for the SCell is determined according to RRC configuration
> - Alt-2 (Explicit mechanism):
>   - For early aperiodic SRS-AS transmission, the SRS resource set(s) triggered for the SCell is determined according to an indication in SCell activation command.
>   - For early aperiodic CSI reporting, the CSI report configuration(s) triggered for the SCell is determined according to an indication in SCell activation command.

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508115](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508115.zip)

## RAN1#122 — 29건

**Agreement** · `8.2.1` Enhancements for UE-initiated/event-driven beam management · `RAN1#122:8.2.1:002` · 관련 주제: CSI 보고/codebook

> Adopt the following changes in TS38.213 Section 7.5:
> - Reason for change: When the transmission powers of multiple uplink transmissions exceed the UE’s maximum transmit power, TS 38.213 specifies a prioritization mechanism to determine which transmissions should be reduced or dropped. This prioritization covers all conventional UCI types, such as SR, CSI reports, and HARQ-ACK, ensuring consistent behavior across implementations when power reduction is needed. However, the UE-initiated CSI reporting indicator (UEIRI), introduced as a new UCI type to support UE-initiated CSI reporting, is not currently included in the priority order defined in TS 38.213.
> - Summary of change: Capture the priority rule for UEIRI, i.e., the same priority as LRR/SR.
> - Consequences if not approved: Without explicit prioritization, UE behavior may vary between implementations, potentially causing inconsistent reporting of UE-initiated CSI under power-limited conditions. This could result in the unintended suppression of UEIRI or, conversely, excessive reduction of other UCI types, impacting system performance and interoperability
> | 7.5 Prioritizations for transmission power reductions For single cell operation with two uplink carriers or for operation with carrier aggregation or for operation with a candidate cell configured by LTM-Config or for operation with a single cell configured with sTx-2Panel, if a total UE transmit power for PUSCH or PUCCH or PRACH or SRS transmissions on serving cell(s) or on a candidate cell, if any, in a frequency range in a respective transmission occasion would exceed , where is the linear value of in transmission occasion as defined in [8-1, TS 38.101-1] for FR1 and [8-2, TS 38.101-2] for FR2, the UE allocates power to PUSCH/PUCCH/PRACH/SRS transmissions according to the following priority order (in descending order) so that the total UE transmit power for transmissions on serving cell(s) or on a candidate cell, if any, in the frequency range is smaller than or equal to for that frequency range in every symbol of transmission occasion . If the UE transmits SRS on multiple SRS resources according to Clause 6.2.1.4 of [6, TS 38.214], the UE allocates power so that all REs of the SRS transmission have same power. For the purpose of power allocation in this clause, if a UE is provided uci-MuxWithDiffPrio and the UE multiplexes HARQ-ACK information in a PUSCH, a priority index of the PUSCH is the larger of (a) the priority index of the PUSCH according to clause 9 and (b) the larger priority index of the HARQ-ACK information. When determining a total transmit power for serving cells or a candidate cell, if any, as described in Clause 21 in a frequency range in a symbol of transmission occasion , the UE does not include power for transmissions starting after the symbol of transmission occasion . The total UE transmit power in a symbol of a slot is defined as the sum of the linear values of UE transmit powers for PUSCH, PUCCH, PRACH, and SRS in the symbol of the slot. - PRACH transmission on a candidate cell, if any, as described in Clause 21 - PRACH transmission on the PCell - PUCCH or PUSCH transmissions with larger priority index - For PUCCH or PUSCH transmissions with same priority index - PUCCH transmission with HARQ-ACK information, and/or SR, and/or LRR, and/or UEIRI, or PUSCH transmission with HARQ-ACK information of the priority index - PUCCH transmission with CSI or PUSCH transmission with CSI - PUSCH transmission without HARQ-ACK information of the priority index or CSI and, for Type-2 random access procedure, PUSCH transmission on the PCell - If the UE is configured with prioSCellPRACH-OverSP-PeriodicSRS-r17 - Aperiodic SRS transmission or PRACH transmission on a serving cell other than the PCell - Semi-persistent and/or periodic SRS transmission - otherwise, - SRS transmission, with aperiodic SRS having higher priority than semi-persistent and/or periodic SRS, or PRACH transmission on a serving cell other than the PCell =========unchanged omitted=========== |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506253](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506253.zip)

**Agreement** · `8.2.2` CSI enhancements · `RAN1#122:8.2.2:001` · 관련 주제: Beam management, CSI 보고/codebook

> Adopt the following changes to TS38.214 V19.0.0 Clause 6.2.1.3 on priority rules for UE sounding procedure as follows:
> | Reason for change: The newly agreed CSI reporting quantities in Rel-19 MIMO CSI has not been reflected in the current description of priority rules in TS38.214 |
> | Summary of the change: Added the new CSI reporting quantities for CJT calibration reporting |
> | Consequences if not approved: Incomplete description in TS38.214 |
> | 6.2.1.3 UE sounding procedure between component carriers < Unchanged part omitted > - the UE shall drop PUSCH transmission carrying aperiodic CSI comprising only CQI/PMI/L1-RSRP/L1-SINR/TDCP/cjtc-Dd/cjtc-F/cjtc-Dd-F/cjtc-P on a carrier of a serving cell in set whenever the transmission and aperiodic SRS transmission (including any interruption due to uplink or downlink RF retuning time [11, TS 38.133]) as defined by higher layer parameters switchingTimeUL and switchingTimeDL of SRS-SwitchingTimeNR) on the carrier of the serving cell happen to overlap in the same symbol. < Unchanged part omitted > |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2505535](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2505535.zip)

**Conclusion** · `8.2.2` CSI enhancements · `RAN1#122:8.2.2:008`

> For Rel-19 SRS port grouping, whether resources across multiple resource sets can be used follows the legacy principle, i.e. for periodic and semi-persistent SRS resource sets, it is not possible to have the grouped SRS ports resources across multiple SRS resource sets; but for aperiodic SRS resource sets, the grouped SRS ports can come from multiple SRS resource sets.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506513](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506513.zip)

**Agreement** · `8.2.3` Support for 3-antenna-port codebook-based transmissions · `RAN1#122:8.2.3:004` · 관련 주제: CSI 보고/codebook

> Adopt the following TP for TS 38.214 section 6.2.1.2.
> Reason for change: Reflect the agreement in UE feature.
> Summary of change: Include the cases of 3T3R and 3T6R antenna switching.
> Consequence if not changed: The 3T3R and 3T6R antenna switching feature will not be supported.
> | 6.2.1.2 UE sounding procedure for DL CSI acquisition -------------------------------------------Unchanged parts are omitted------------------------------------------ When the UE is configured with the higher layer parameter usage in SRS-ResourceSet set as 'antennaSwitching', the UE may be configured with only one of the following configurations depending on the indicated UE capability supportedSRS-TxPortSwitch ('t1r2' for 1T2R, 't1r1-t1r2' for 1T=1R/1T2R, 't2r4' for 2T4R, 't1r4' for 1T4R, 't1r1-t1r2-t1r4' for 1T=1R/1T2R/1T4R, 't1r4-t2r4' for 1T4R/2T4R, 't1r1-t1r2-t2r2-t2r4' for 1T=1R/1T2R/2T=2R/2T4R, 't1r1-t1r2-t2r2-t1r4-t2r4' for 1T=1R/1T2R/2T=2R/1T4R/2T4R, 't1r1' for 1T=1R, 't2r2' for 2T=2R, 't1r1-t2r2' for 1T=1R/2T=2R, 't4r4' for 4T=4R, or 't1r1-t2r2-t4r4' for 1T=1R/2T=2R/4T=4R or the UE may be configured with only one of the following configurations depending on the indicated UE capability supportedSRS-TxPortSwitchBeyond4Rx ('t1r1' for 1T=1R, 't2r2' for 2T=2R, 't1r2' for 1T2R, 't4r4' for 4T=4R, 't2r4' for 2T4R, 't1r4' for 1T4R, 't2r6' for 2T6R, 't1r6' for 1T6R, 't4r8' for 4T8R, 't2r8' for 2T8R, 't1r8' for 1T8R, or the UE may be configured with the following configurations depending on the indicated UE capability srs-AntennaSwitching8T8R ('t1r1' for 1T=1R, 't2r2' for 2T=2R, 't1r2' for 1T2R, 't4r4' for 4T=4R, 't2r4' for 2T4R, 't1r4' for 1T4R, 't2r6' for 2T6R, 't1r6' for 1T6R, 't4r8' for 4T8R, 't2r8' for 2T8R, 't1r8' for 1T8R, 'noTdm' or 'tdmAndNoTdm' for 8T8R): -------------------------------------------Unchanged parts are omitted------------------------------------------ |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2505237](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2505237.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:011`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-3-3 | 3T6R Antenna switching | 1. Support of 3T6R SRS Tx port switching with port 1003 disabled when 4 port SRS resources with port 1003 disabled are configured to the UE 2. Report the entry number of the first-listed band with UL in the band combination that affects this DL 3. Report the entry number of the first-listed band with UL in the band combination that switches together with this UL [4. Support of 3T6R antenna switching configuration(s) as an allowing downgrading configuration of 4T8R] | FFS 2-53 | yes | n/a | 3TX 3T6R antenna switching is not supported | Per FS | n/a | n/a | n/a | Component 2 candidate value: {1,2, … 32} Component 3 candidate value: {1,2, … 32} [FFS: New component for downgrade antenna switching configurations or a new Note: This UE feature can be signalled together with srs-AntennaSwitching8T8R-r18, srs-AntennaSwitchingBeyond4RX-r17, supportedSRS-TxPortSwitch-v1610, or supportedSRS-TxPortSwitch to indicate SRS antenna switching downgrading capability for a UE with 4Rx, 6Rx or 8Rx.] | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:018`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-8 | SRS Port Grouping | Support of SRS port grouping | FFS 23-8-3 | yes | n/a | SRS Port Grouping is not supported | Per FS | n/a | n/a | n/a | Candidate values: {xT8R, xT6R, both} Note: If a UE supports this FG, then the UE supports the corresponding antenna switching configurations and port groupings | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:028` · 관련 주제: CSI 보고/codebook

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-3-1 | Non-codebook based PUSCH transmission for 3TX for single TRP | 1. Maximal number of supported layers (non-codebook transmission scheme) 2. Maximum number of SRS resource per set (SRS set use is configured as for non-codebook transmission) 3. Maximum number of simultaneous transmitted SRS resources at one symbol | FFS | yes | n/a | Non-codebook based PUSCH transmission for 3TX is not supported | Per FSPC | n/a | n/a | n/a | Component 1 candidate values: {1, 2, 3} Component 2 candidate values: {1,2,3} Component 3 candidate values: {1,2,3} | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:029` · 관련 주제: CSI 보고/codebook

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-3-2 | Codebook based PUSCH transmission for 3TX for single TRP | 1. Maximal number of PUSCH MIMO layers for codebook-based PUSCH 2. Maximum number of 4-port SRS resources per SRS resource set with usage set to 'codebook’ for codebook-based 3Tx PUSCH 4. Codebook based PUSCH transmission with port 1003 disabled when 4 port SRS resources with port 1003 disabled are configured to the UE | FFS | yes | n/a | Codebook based PUSCH transmission for 3TX is not supported | Per FSPC | n/a | n/a | n/a | Component 1 candidate values: {1, 2,3} Component 2 candidate values: {1,2} Note: When configured according to Component 4, the number of ports supported by UE for transmission in an SRS resource is 3 | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:030`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-3-3a | 3T3R antenna switching | 1. Support of 3T3R SRS Tx port switching with port 1003 disabled when 4 port SRS resources with port 1003 disabled are configured to the UE 2. Report the entry number of the first-listed band with UL in the band combination that affects this DL 3. Report the entry number of the first-listed band with UL in the band combination that switches together with this UL | FFS 2-53 | yes | n/a | 3TX 3T3R antenna switching is not supported | Per FS | n/a | n/a | n/a | Component 2 candidate value: {1,2, … 32} Component 3 candidate value: {1,2, … 32} Note: This UE feature can be signalled together with srs-AntennaSwitching8T8R-r18, srs-AntennaSwitchingBeyond4RX-r17, supportedSRS-TxPortSwitch-v1610, supportedSRS-TxPortSwitch or 59-3-3 to indicate SRS antenna switching downgrading capability for a UE with 4Rx, 6Rx or 8Rx Note: ‘3T3R’ is only applicable for the UE equipped with 4Rx, 6Rx, or 8Rx antenna ports. | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:031` · 관련 주제: CSI 보고/codebook

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | NR MIMO Phase 5 | 59-3-4 | M-TRP PUSCH repetition (type A) of 3-antenna-port PUSCH transmission – codebook based | 1. Support of M-TRP PUSCH repetition for 3-antenna-port PUSCH transmission with type A for codebook based - sequential mapping for repetitions larger than 2 - cyclic mapping for 2 repetitions 2. Support of two SRS resource sets with usage set to 'codebook' 3. Supported number of SRS resources in one SRS resource set | FFS 59-3-2 | yes | n/a | M-TRP PUSCH repetition is not supported for 3TX PUSCH transmission with type A for codebook based | Per FS | n/a | n/a | n/a | Component 3 candidate values: {1,2} | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:032` · 관련 주제: CSI 보고/codebook

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | NR MIMO Phase 5 | 59-3-4a | M-TRP PUSCH repetition (type A) of 3-antenna-port PUSCH transmission – non-codebook based | Support of M-TRP PUSCH repetition for 3-antenna-port PUSCH transmission with type A for non-codebook based - sequential mapping for repetitions larger than 2 - cyclic mapping for 2 repetitions 2. Support of two SRS resource sets with usage set to 'non-codebook' 3. Supported number of SRS resources in one SRS resource set | FFS 59-3-1 | yes | n/a | M-TRP PUSCH repetition is not supported for 3TX PUSCH transmission with type A for non-codebook based | Per FS | n/a | n/a | n/a | Component 3 candidate values: {1,2,3} | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:033` · 관련 주제: CSI 보고/codebook

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | NR MIMO Phase 5 | 59-3-5 | M-TRP PUSCH repetition (type B) of 3-antenna-port PUSCH transmission – codebook based | Support of M-TRP PUSCH repetition for 3-antenna-port PUSCH transmission with type B for codebook based - sequential mapping for repetitions larger than 2 - cyclic mapping for 2 repetitions 2. Support of two SRS resource sets with usage set to 'codebook' 3. Supported number of SRS resources in one SRS resource set | FFS 59-3-2, 11-5 | yes | n/a | M-TRP PUSCH repetition is not supported for 3TX PUSCH transmission with type B for codebook based | Per FSPC | n/a | n/a | n/a | Component 3 candidate values: {1,2} | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:034` · 관련 주제: CSI 보고/codebook

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | NR MIMO Phase 5 | 59-3-5a | M-TRP PUSCH repetition (type B) of 3-antenna-port PUSCH transmission – non-codebook based | Support of M-TRP PUSCH repetition for 3-antenna-port PUSCH transmission with type B for non-codebook based - sequential mapping for repetitions larger than 2 - cyclic mapping for 2 repetitions 2. Support of two SRS resource sets with usage set to 'non-codebook' 3. Supported number of SRS resources in one SRS resource set | FFS 59-3-1, 11-5 | yes | n/a | M-TRP PUSCH repetition is not supported for 3TX PUSCH transmission with type B for non-codebook based | Per FSPC | n/a | n/a | n/a | Component 3 candidate values: {1,2,3} | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:036`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-4-3 | Two SRS closed-loop power control adjustment states separate from PUSCH | Support of two separate SRS closed loop indices separate from PUSCH | FFS | yes | n/a | Two separate SRS closed loop indexes is not supported | Per band | n/a | n/a | n/a |  | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:040`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-4-7b | DCI format 2_3 to indicate TPC for one of two separate SRS closed loop indexes | Support DCI format 2_3 to indicate TPC for one of two separate SRS closed loop indexes. | FFS 59-4-3 | yes | n/a | The function of DCI 2_3 indicating TPC command for one of two separate SRS closed loop indexes is not supported. | Per band | n/a | n/a | n/a |  | Optional with capability signaling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:041`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-4-8 | DCI format 1_1 to indicate TPC command for SRS associated with a separate SRS CLPC adjustment state | Support of DCI format 1_1 to indicate TPC command for SRS associated with a separate SRS CLPC adjustment state | FFS 59-4-3 | yes | n/a | DCI 1_1 indicating TPC command for SRS associated with a separate SRS CLPC adjustment state is not supported | Per band | n/a | n/a | n/a |  | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:042` · 관련 주제: Beam management

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-4-9a | DCI format 1_1 to indicate one of two separate SRS closed loop indexes under separate DL/UL TCI state mode | Support of DCI format 1_1 to indicate one or two separate SRS closed loop index(es) under separate DL/UL TCI state mode | FFS 59-4-8 | yes | n/a | DCI 1_1 indicating one of two separate SRS closed loop indexes under separate DL/UL TCI state mode is not supported | Per band | n/a | n/a | n/a |  | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:043` · 관련 주제: Beam management

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-4-9b | DCI format 1_1 to indicate one of two separate SRS closed loop indexes under joint TCI state mode | Support of DCI format 1_1 to indicate one or two separate SRS closed loop index(es) under joint TCI state mode | FFS 59-4-8 | yes | n/a | DCI 1_1 indicating one of two separate SRS closed loop indexes under joint TCI state mode is not supported | Per band | n/a | FR1 only | n/a |  | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `10.2.1` Improvement of SRS capacity and coverage · `RAN1#122:10.2.1:001`

> For a P/SP cross-slot SRS resource, the slot offset configured to the SRS resource refers to the first of the two slots spanned by the SRS resource.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506532](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506532.zip)

**Agreement** · `10.2.1` Improvement of SRS capacity and coverage · `RAN1#122:10.2.1:002`

> When there is a cross-slot SRS resource in the end of a S slot and the beginning of a U slot in a serving cell, support transmitting PUSCH with a priority index 0 and corresponding DMRS after this cross-slot SRS in the U slot in the serving cell.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506532](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506532.zip)

**Agreement** · `10.2.1` Improvement of SRS capacity and coverage · `RAN1#122:10.2.1:003`

> For SRS configured with RPFS (PF>1) and multiple repetitions (R > 1), support multiple frequency-domain starting positions across SRS repetition symbols within each SRS frequency hop based on the followings:
> - For SRS repetition symbols within each SRS frequency hop, the starting position patterns across the K different frequency locations are determined by network configuration
> - The R repetition symbols are equally divided into K subgroups
>   - K is number of starting positions for SRS repetition symbols within each SRS frequency hop
> - Within each subgroup of R/K symbols, the SRS is transmitted at the same starting position in frequency domain.
> - Start position pattern for SRS repetition symbols within each SRS frequency hop is the same during the legacy SRS frequency hopping period (for a same value of )
> FFS: whether/how to support enabling legacy RPFS start RB index hopping across multiple legacy SRS frequency hopping periods and intra-repetition hopping for SRS repetition symbols within each SRS frequency hop simultaneously.

남은 FFS 1건

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506532](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506532.zip)

**Agreement** · `10.2.1` Improvement of SRS capacity and coverage · `RAN1#122:10.2.1:004`

> Support at least the following scenarios for cross-slot SRS transmission:
> - Scenario 1: a periodic, semi-persistent, or aperiodic SRS resource set which includes at least one SRS resource with time-domain resource transmitted across a first S slot and a second consecutive U slot.
> - FFS whether Scenario 2 below is supported.
>   - Scenario 2: an aperiodic SRS resource set which includes at least one SRS resource with time-domain resource transmitted in a first S slot, and at least one another SRS resource with time-domain resource transmitted in a second consecutive U slot.

남은 FFS 1건

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506571](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506571.zip)

**Agreement** · `10.2.1` Improvement of SRS capacity and coverage · `RAN1#122:10.2.1:005`

> For a given AP-SRS resource set in case of SRS transmission across two adjacent S+U slots, study the following alternatives and down-select one to determine “available slot” in the next meeting:
> - Alt-0 (per SRS resource set): The available slot(s) can include one slot or two consecutive S and U slots satisfying there are UL or flexible symbol(s) for the time-domain location(s) for all the SRS resources in the resource set and it satisfies UE capability on the minimum timing requirement between triggering PDCCH and all the SRS resources in the resource set.
> - Alt-1 (per SRS resource): The available slot(s) can include one slot or two consecutive S and U slots satisfying there are UL or flexible symbol(s) for the time-domain location(s) for at least one of the SRS resources in the resource set and it satisfies UE capability on the minimum timing requirement between triggering PDCCH and all the SRS resources in the resource set.
> - Alt-2 (per slot): An available slot is a slot satisfying there are UL or flexible symbol(s) for the time-domain location(s) for a subset of SRS resource(s) with same slot offset in the SRS resource set, and it satisfies UE capability on the minimum timing requirement between triggering PDCCH and all the SRS resources in the resource set.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506585](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506585.zip)

**Agreement** · `10.2.1` Improvement of SRS capacity and coverage · `RAN1#122:10.2.1:006`

> To determine the time-domain location of cross-slot SRS,
> - One set of time-domain resource allocation related parameters (i.e., startPosition, nrofSymbols, and repetitionFactor) is configured for the SRS resource without restriction on “within a slot”.
>   - For the index of each SRS symbol , it is the same as legacy spec., i.e., .
>   - The offset counts symbols backwards from the end of the starting slot of the resource

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506585](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506585.zip)

**Agreement** · `10.2.1` Improvement of SRS capacity and coverage · `RAN1#122:10.2.1:007`

> For intra-repetition hopping for SRS repetition symbols within each SRS frequency hop, study the following configuration combinations:
> - PF=2 and K=2
> - PF =4 and K=2
> - PF =4 and K=4

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506585](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506585.zip)

**Agreement** · `10.2.2` Enhancing DL CSI acquisition · `RAN1#122:10.2.2:001`

> For UE transition from IDLE/INACTIVE to CONNECTED mode, support at least aperiodic SRS-AS transmission triggered via MSG4 of 4-Step RACH.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506539](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506539.zip)

**Agreement** · `10.2.2` Enhancing DL CSI acquisition · `RAN1#122:10.2.2:003` · 관련 주제: CSI 보고/codebook, CSI-RS

> For a UE transition from IDLE to CONNECTED mode, support the following procedure at least for early aperiodic SRS-AS/CSI-RS/CSI triggering (i.e., early triggering of aperiodic SRS-AS transmission, aperiodic CSI-RS reception, aperiodic CSI reporting):
> - Step-1: The UE receives the resource/reporting configuration(s) for early SRS-AS/CSI-RS/CSI triggering provided in the system information before MSG3.
>   - FFS: Which SIB is used to carry the resource/reporting configuration(s) for early SRS-AS/CSI/CSI-RS triggering
> - Step-2: The UE reports its capability on early SRS/CSI-RS/CSI triggering through MSG3
> - Step-3: The UE receives MSG4 that triggers early SRS-AS/CSI-RS/CSI based on  the capability reported by the UE.
> - Step-4: The UE performs aperiodic SRS-AS transmission, aperiodic CSI-RS reception, and/or aperiodic CSI reporting.
>   - FFS: Timeline of the aperiodic SRS-AS transmission, aperiodic CSI-RS reception, aperiodic CSI reporting
> Note: The term “capability” above does not mean legacy RRC based UE capability.
> FFS: For a UE transition from INACTIVE to CONNECTED mode, whether above procedure can be reused at least for early aperiodic SRS-AS/CSI-RS/CSI triggering
> Note: Whether the aperiodic SRS-AS transmission, aperiodic CSI-RS reception, and/or aperiodic CSI reporting can be configured/triggered simultaneously will be discussed separately

남은 FFS 3건

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506539](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506539.zip)

**Agreement** · `10.2.2` Enhancing DL CSI acquisition · `RAN1#122:10.2.2:006`

> For early triggering of SRS-AS when SCell transition from deactivation to activation, support at least aperiodic SRS-AS transmission on a SCell, triggered based on legacy SCell activation command activating the SCell.
> - FFS: Timeline of the aperiodic SRS-AS transmission (requirement is up to RAN4)
> - FFS: How to trigger the aperiodic SRS-AS transmission based on legacy SCell activation command
> - FFS: Whether/what new information is provided in SCell activation command?

남은 FFS 3건

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506583](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506583.zip)

**Agreement** · `10.2.2` Enhancing DL CSI acquisition · `RAN1#122:10.2.2:008` · 관련 주제: CSI 보고/codebook, CSI-RS

> For early triggering of SRS-AS/CSI-RS/CSI when UE transition from IDLE to CONNECTED mode, study the following at least three options for Step-1 and Step-2:
> - Option-1: NW can provide the resource/report configuration in SIBx based on only one UE capability assumption, and UE can report through MSG3 whether the resource/report configuration received in SIBx is supported.
> - Option-2: NW can provide the resource/report configuration(s) in SIBx based on one or multiple UE capability assumptions, and UE can report through MSG3 which resource/report configuration(s) received in SIBx is/are supported.
> - Option-3: NW can provide the resource/report configuration(s) in SIBx based on one or multiple UE capability assumptions, and UE can report through MSG3 the supported capability(s) of early SRS/CSI/CSI-RS triggering (e.g., whether to support this feature, max number of CSI-RS ports, xTyR for SRS-AS, max bandwidth of the CSI-RS/SRS-AS etc.).
> Note: The term “capability” or “UE capability” above does not mean legacy RRC based UE capability.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506583](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506583.zip)

---

## 관련 결정 12건 (주된 주제는 다른 주제)

원문에 SRS 관련 표현이 있지만 주된 주제가 다른 확정 결정입니다. 전문은 각 주된 주제 리포트에 있습니다.

| 회의 | 구분 | 주된 주제 | Agenda | 원문 첫 줄 | 출처 |
|---|---|---|---|---|---|
| RAN1#126 | Agreement | [Beam management](beam.md) | 10.5.3.4 Beam management for downlink and uplink | Regarding NW initiated beam indication, study transmission configuration indicator (TCI) framework involving … | [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Beam management]` |
| RAN1#126 | Agreement | [Beam management](beam.md) | 10.5.3.4 Beam management for downlink and uplink | Regarding UE initiated beam management, on a single-TRP operation, on UL transmission procedure, the followin… | [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Beam management]` |
| RAN1#126 | Agreement | [AI/ML CSI](aiml.md) | 8.1 Maintenance on AI/ML for NR Air interface, NR MIMO Phase 5,  NES and NTN for NR and IoT | The following TP for TS 38.214 Clause 5.2.3 is endorsed. | [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606794](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606794.zip) · `[126-R19-AI 8.1]` |
| RAN1#125 | Agreement | [AI/ML CSI](aiml.md) | 10.5.3.1 Aspects of downlink-based CSI acquisition | For the study on channel property information (CPI), the evaluation at least considering the following: | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of DL based CSI acquisition]` |
| RAN1#125 | Agreement | [Beam management](beam.md) | 10.5.2.4 Beam management for downlink and uplink | Study the following uplink signal and channels transmission in response to a triggered Event-1: | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Beam management]` |
| RAN1#125 | Agreement | [Beam management](beam.md) | 10.5.2.4 Beam management for downlink and uplink | Support the following table as the assumption of LLS for evaluation of 6GR beam management | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Beam management]` |
| RAN1#124bis | Agreement | [AI/ML CSI](aiml.md) | 10.5.3.1 Aspects of downlink-based CSI acquisition | For the study on channel property information (CPI), at least the following is considered. | [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of DL based CSI acquisition]` |
| RAN1#124bis | Agreement | [Beam management](beam.md) | 10.5.2.4 Beam management for downlink and uplink | Support the following table as the basic assumption of LLS for evaluation of 6GR beam management: | [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Beam management]` |
| RAN1#124 | Agreement | [Beam management](beam.md) | 10.5.2.4 Beam management for downlink and uplink | Regarding link-level evaluation of 6GR beam management, in RAN1#124b, to use the following template as starti… | [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · `[124-R20-6GR-Beam management]` |
| RAN1#122bis | Agreement | [AI/ML CSI](aiml.md) | 8.1 Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface | The following TP for 38.214 Clause 6.2.1 is endorsed. | [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2507998](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2507998.zip) · `[122bis-R19-AI/ML]` |
| RAN1#122bis | Agreement | [AI/ML CSI](aiml.md) | 8.1 Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface | The following TP for 38.214 Clause 6.2.1.3 is endorsed. | [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2507998](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2507998.zip) · `[122bis-R19-AI/ML]` |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 10.1.1 CSI spatial/frequency compression without temporal aspects (“Case 0”) | For CSI feedback via two-sided model, support at least precoding matrix as target CSI type. | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506496](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506496.zip) |

---

## 후보 56건 (키워드 일치 · 확인 필요)

포함 Agenda 밖에서 키워드로 잡힌 결정입니다. CSI 범위가 아닐 수 있습니다.

### RAN1#126bis — 6건

**Agreement** · `8.2` Maintenance on others · `RAN1#126bis:8.2:009` · 후보 · 🆕 신규 · 관련 주제: Beam management, CSI 보고/codebook, CSI-RS

> Adopt the following TP to TS 38.214 clause 5.1.5 in principle:
> | Reason for change: | RAN1 agreements supported Type C (and Type D if applicable) as the QCL type for WUS in RRC_CONNECTED mode, which is applicable when unified TCI framework is configured. TS 38.213 correctly reflected the agreements, while TS 38.214 is not consistent with TS 38.213 and the agreements. Also, several occasions with unified TCI framework also need to be clarified to be applicable to WUS. |
> |  |  |
> | Summary of change: | When applying the unified TCI framework, separate description for WUS to use Type C QCL type is added. |
> |  |  |
> | Consequences if not approved: | The UE behaviour in TS 38.214 is not consistent with TS 38.213 or the RAN1 agreements. |
> | =============================== Start of TP================================ 5.1.5 Antenna ports quasi co-location The UE can be configured with a list of up to M TCI-State configurations within the higher layer parameter PDSCH-Config to decode PDSCH according to a detected PDCCH with DCI intended for the UE and the given serving cell, where M depends on the UE capability maxNumberConfiguredTCIstatesPerCC. Each TCI-State contains parameters for configuring a quasi co-location relationship between one or two downlink reference signals and the DM-RS ports of the PDSCH, the DM-RS port of PDCCH or the CSI-RS port(s) of a CSI-RS resource. The quasi co-location relationship is configured by the higher layer parameter qcl-Type1 for the first DL RS, and qcl-Type2 for the second DL RS (if configured). For the case of two DL RSs, the QCL types shall not be the same, regardless of whether the references are to the same DL RS or different DL RSs. The quasi co-location types corresponding to each DL RS are given by the higher layer parameter qcl-Type in QCL-Info and may take one of the following values: - 'typeA': {Doppler shift, Doppler spread, average delay, delay spread} - 'typeB': {Doppler shift, Doppler spread} - 'typeC': {Doppler shift, average delay} - 'typeD': {Spatial Rx parameter} The UE can be configured with a list of up to 128 TCI-State configurations, within the higher layer parameter dl-OrJointTCI-StateList in PDSCH-Config for providing a reference signal for the quasi co-location for DM-RS of PDSCH and DM-RS of PDCCH in a BWP/CC, for CSI-RS, and to provide a reference signal with qcl-Type set to 'typeD', if applicable, for determining UL TX spatial filter for dynamic-grant and configured-grant based PUSCH and PUCCH resource in a BWP/CC, and SRS. If the TCI-State or TCI-UL-State configurations are absent in a BWP of the CC, the UE can apply the TCI-State or TCI-UL-State configurations from a reference BWP of a reference CC configured by unifiedTCI-StateRef. The UE is not expected to be configured with tci-StatesToAddModList, SpatialRelationInfo or PUCCH-SpatialRelationInfo, except SpatialRelationInfoPos in a CC in a band, if the UE is configured with dl-OrJointTCI-StateList or ul-TCI-StateList in any CC in the same band. The UE can assume that when the UE is configured with tci-StatesToAddModList in any CC in the CC list configured by simultaneousTCI-UpdateList1-r16, simultaneousTCI-UpdateList2-r16, simultaneousSpatial-UpdatedList1-r16, or simultaneousSpatial-UpdatedList2-r16, the UE is not configured with dl-OrJointTCI-StateList or ul-TCI-StateList in any CC within the same band in the CC list. The UE receives an activation command, as described in clause 6.1.3.14 of [10, TS 38.321], or 6.1.3.47 of [10, TS 38.321], used to map up to 8 TCI states and/or pairs of TCI states, with one TCI state for DL channels/signals and/or one TCI state for UL channels/signals to the codepoints of the DCI field 'Transmission Configuration Indication' for one or for a set of CCs/DL BWPs. When a set of TCI state IDs are activated for a set of CCs/DL BWPs and if applicable, for a set of CCs/UL BWPs, where the applicable list of CCs is determined by the indicated CC in the activation command, the same set of TCI state IDs are applied for all DL and/or UL BWPs in the indicated CCs. If the activation command maps TCI-State(s) and/or TCI-UL-State(s) to only one TCI codepoint, the UE shall apply the indicated TCI-State(s) and/or TCI-UL-State(s) to one or to a set of CCs /DL BWPs, and if applicable, to one or to a set of CCs /UL BWPs once the indicated mapping for the one single TCI codepoint is applied as described in [11, TS 38.133]. When the bwp-id or cell for QCL-TypeA/D source RS in a QCL-Info of the TCI state is not configured, the UE assumes that QCL-TypeA/D source RS is configured in the CC/DL BWP where TCI state applies. When tci-PresentInDCI is set as 'enabled' or tci-PresentDCI-1-2 is configured for the CORESET, a UE configured with dl-OrJointTCI-StateList with activated TCI-State or ul-TCI-StateList with activated TCI-UL-State receives DCI format 1_1/1_2/1_3 providing indicated TCI-State(s) and/or TCI-UL-State(s) for a CC or all CCs in the same CC list configured by simultaneousU-TCI-UpdateList1-r17, simultaneousU-TCI-UpdateList2-r17, simultaneousU-TCI-UpdateList3-r17, simultaneousU-TCI-UpdateList4-r17. The DCI format 1_3 provides indicated TCI state(s) and/or TCI-UL-State(s) for the CC(s) in a scheduledCellListDCI-1-3 if the UE is scheduled by the DCI format 1_3 to receive PDSCH at least on one serving cell in the scheduledCellListDCI-1-3. The DCI format 1_1/1_2 can be with or without, if applicable, DL assignment. If the DCI format 1_1/1_2 is without DL assignment, the UE can assume the following: - CS-RNTI is used to scramble the CRC for the DCI - The values of the following DCI fields are set as follows: - RV = all '1's - MCS = all '1's - NDI = 0 - Set to all '0's for FDRA Type 0, or all '1's for FDRA Type 1, or all '0's for dynamicSwitch (same as in Table 10.2-4 of [6, TS 38.213]). After a UE receives an initial higher layer configuration of dl-OrJointTCI-StateList where more than one TCI-State can be used as an indicated TCI state and before application of an indicated TCI state from the configured TCI states: - The UE assumes that DM-RS of PDSCH and DM-RS of PDCCH that are not received during the RACH procedure, and the CSI-RS applying the indicated TCI state are quasi co-located with the reference signal(s) in the CandidateTCI-State indicated in the LTM Cell Switch Command MAC CE [10, 38.321] if applicable. - The UE assumes that DM-RS of PDSCH and DM-RS of PDCCH and the CSI-RS applying the indicated TCI state are quasi co-located with the reference signal in the determined CandidateTCI-State for RACH-less conditional LTM cell switch [10, 38.321] if applicable. - The UE assumes that DM-RS of PDSCH and DM-RS of PDCCH and the CSI-RS applying the indicated TCI state are quasi co-located with the SS/PBCH block the UE identified during the random access procedure initiated by RACH-based conditional LTM cell switch if applicable. - Otherwise, the UE assumes that DM-RS of PDSCH and DM-RS of PDCCH, and the CSI-RS applying the indicated TCI state are quasi co-located with the SS/PBCH block the UE identified during the initial access procedure with respect to qcl-Type set to 'typeA', and when applicable, also with respect to qcl-Type set to 'typeD'. . After a UE receives an initial higher layer configuration of dl-OrJointTCI-StateList where more than one TCI-State can be used as an indicated TCI state or an initial higher layer configuration of ul-TCI-StateList where more than one TCI-UL-State can be used as an indicated TCI state and before application of an indicated TCI state from the configured TCI states: - The UE determines the UL TX spatial filter, if applicable, for dynamic-grant based PUSCH that is not transmitted during the RACH procedure and configured-grant based PUSCH and PUCCH that are not transmitted during the RACH procedure, and for SRS applying the indicated TCI state, from the CandidateTCI-State or CandidateTCI-UL-State indicated in the LTM Cell Switch Command MAC CE [10, 38.321] if applicable. - The UE determines the UL TX spatial filter, if applicable, for dynamic-grant and configured-grant based PUSCH and PUCCH, and for SRS applying the indicated TCI state, from the determined CandidateTCI-State or CandidateTCI-UL-State for RACH-less conditional LTM cell switch [10, 38.321] if applicable. - The UE determines the UL TX spatial filter, if applicable, for dynamic-grant and configured-grant based PUSCH and PUCCH, and for SRS applying the indicated TCI state, is the same as that for a PUSCH transmission scheduled by a RAR UL grant or a MsgA PUSCH transmission during the random access procedure initiated by RACH-based conditional LTM cell switch [10, 38.321] if applicable. - Otherwise, the UE assumes that the UL TX spatial filter, if applicable, for dynamic-grant and configured-grant based PUSCH and PUCCH, and for SRS applying the indicated TCI state, is the same as that for a PUSCH transmission scheduled by a RAR UL grant or a MsgA PUSCH transmission during the initial access procedure. After a UE receives a higher layer configuration of dl-OrJointTCI-StateList where more than one TCI-State can be used as an indicated TCI state as part of a Reconfiguration with sync procedure as described in [12, TS 38.331] and before applying an indicated TCI state from the configured TCI states: - The UE assumes that DM-RS of PDSCH and DM-RS of PDCCH, and the CSI-RS applying the indicated TCI state are quasi co-located with the SS/PBCH block or the CSI-RS resource the UE identified during the random access procedure initiated by the Reconfiguration with sync procedure as described in [12, TS 38.331] with respect to qcl-Type set to 'typeA', and when applicable, also with respect to qcl-Type set to 'typeD'. After a UE receives a higher layer configuration of dl-OrJointTCI-StateList where more than one TCI-State can be used as an indicated TCI state or a higher layer configuration of ul-TCI-StateList where more than one TCI-UL-State can be used as an indicated TCI state as part of a Reconfiguration with sync procedure as described in [12, TS 38.331] and before applying an indicated TCI state from the configured TCI states: - The UE assumes that the UL TX spatial filter, if applicable, for dynamic-grant and configured-grant based PUSCH and PUCCH, and for SRS applying the indicated TCI state, is the same as that for a PUSCH transmission scheduled by a RAR UL grant or a MsgA PUSCH transmission during random access procedure initiated by the Reconfiguration with sync procedure as described in [12, TS 38.331]. If a UE receives a higher layer configuration of dl-OrJointTCI-StateList where only one TCI-State can be used as an indicated TCI state, the UE obtains the QCL assumptions from that TCI state for DM-RS of PDSCH and DM-RS of PDCCH, and the CSI -RS applying the indicated TCI state. If a UE receives a higher layer configuration of dl-OrJointTCI-StateList where only one TCI-State can be used as an indicated TCI state or a higher layer configuration of ul-TCI-StateList where only one TCI-UL-State can be used as an indicated TCI state, the UE determines an UL TX spatial filter, if applicable, from that TCI state for dynamic-grant and configured-grant based PUSCH and PUCCH, and SRS applying the indicated TCI state. ============================= Unchanged Text Omitted ============================ ============================= End of TP |
> Final CR in R1-2608750 is agreed.
> LTM

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · [R1-2608726](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2608726.zip) · `[126bis-R19-AI 8.2]`

**Agreement** · `10.5.2.3` Uplink transmission scheme(s) for uplink channels · `RAN1#126bis:10.5.2.3:002` · 후보 · 🆕 신규

> For 6GR PUSCH transmission with DFTS-OFDM waveform, study DMRS sequence at least considering the followings:
> - ZC sequence and CGS in 5G NR as a starting point
> - Further considering enhancement(s) with the following directions
>   - Whether the DMRS sequence should depend on the PUSCH modulation order
>   - Whether/how to enhance ZC, Gold and CGS-based DMRS sequence design
>   - Whether a new/refined low-PAPR DMRS sequence is introduced
>   - Whether the DMRS sequence is independent of FDRA size/start for flexible MU-MIMO pairing
>   - Whether/how to mitigate inter-port interference
>   - Whether/how to mitigate inter-cell interference
> - Auto-/Cross-correlation property including cross-correlation with partially overlapping sequences
> - PAPR, cubic metric
> - Channel estimation accuracy
> - Note: DMRS sequence for the case of DMRS RE and PUSCH data RE in a same symbol by FDM manner can be separately discussed.
> - Consider possibly common design between PUSCH DMRS for DFTS-OFDM modulated by QPSK and above and SRS
>   - FFS: PUSCH DMRS for DFTS-OFDM modulated by pi/2 BPSK
> - Consider impact on receiver complexity

남은 FFS 1건

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Transmission scheme for UL channels]`

**Agreement** · `10.5.2.3` Uplink transmission scheme(s) for uplink channels · `RAN1#126bis:10.5.2.3:006` · 후보 · 🆕 신규 · 관련 주제: CSI 보고/codebook, CSI-RS

> For study on DL/UL reciprocity based PUSCH transmission for 6GR, further consider the following schemes only:
> - Scheme 1. CSI-RS based DL channel estimation by UE, UE calculates UL precoder, UE transmits (precoded) SRS, and NW indicates UE precoder information to schedule (e.g., analogous with non-codebook based PUSCH in NR)
>   - Companies report the assumption of precoded SRS (e.g., detail SRS configuration, precoder for SRS)
> - Scheme 2. CSI-RS-based DL channel acquisition by UE, UE reports channel information to NW, and NW selects an UL precoder to schedule UE
>   - Companies report the assumption of channel information UE reports and the associated reporting overhead
>   - Companies report how to perform UL link adaptation (e.g. RS based, or other methods that are not RS based)
>   - Companies compare the performance with SRS coverage enhancement alternatives, e.g., SRS repetition and narrowband SRS
> - For both above schemes, for RAN1 evaluation purpose, companies evaluate with considering DL/UL reciprocity error model

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Transmission scheme for UL channels]`

**Agreement** · `10.5.5` Other physical layer signals, channels and procedure · `RAN1#126bis:10.5.5:003` · 후보 · 🆕 신규

> For UE-to-UE CLI reporting in 6GR, support L1 network-controlled CLI reporting:
> - Down-select one from the following two options for reporting mechanism:
>   - Option 1: support aperiodic reporting only
>   - Option 2: support both periodic and aperiodic reporting
>     - FFS: which reporting mechanism(s) are applicable to SRS-RSRP measurement.
>     - FFS: which reporting mechanism(s) are applicable to CLI RSSI measurement.
> - Support the following Option 1 for reporting content:
>   - Option 1: N strongest RSRP or RSSI and corresponding resource indicators. The UE reports RSRP/RSSI for the strongest one and differential RSRP/RSSI for the other N-1.
>   - Further study option 2: a bit-map reporting with each bit corresponding each measurement resource, and bit value = 1 indicating the RSRP/RSSI measurement is above a configured threshold.

남은 FFS 2건

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Other signals, channels, and procedures]`

**Agreement** · `10.8.2` Aspects of integration with communication · `RAN1#126bis:10.8.2:003` · 후보 · 🆕 신규

> - Study at least the following aspects of open loop power control of UE as sensing transmitter using existing SRS power control framework as starting point, to identify whether sensing specific enhancement on power control for sensing is necessary or not
>   - P0/alpha
>   - PCMAX
>   - Power boosting
>   - Pathloss/Pathloss reference
>   - PH/PHR
>   - Association of the applicable power-control parameters for sensing purpose
>   - UE transmission power within CPI
>   - the impact/interference to communication and sensing
> - Companies are encouraged to bring up evaluation results on potential power control issues.

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · [R1-2607231](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2607231.zip) · `[126bis-R20-6GR-ISAC-Integration]`

**WA** · `10.8.3` Waveform and frame structure · `RAN1#126bis:10.8.3:009` · 후보 · 🆕 신규 · 관련 주제: CSI-RS

> - For waveform and frame structure evaluation, the following common parameters are used as baseline for comparison of the evaluation results across companies.
> - Other parameters not described below can be used from the agreed SLS simulation assumption in ISAC evaluation agenda and reported by company.
> - Note: As long as the parameters listed in the table are necessary for evaluation, the values of the parameters are recommended to be commonly used.
> - Note: Not all parameters listed in the table can be used for evaluation, depending on the evaluation methodologies (LLS, a simplified SLS, and waveform characteristics analysis).
> - Note: when the delay associated with target changes within a CPI, the metrics related to ambiguity function can be calculated according to a smaller CPI value with constant delay.
> | Evaluation case | Low-High Mobility, Long range | Low-Moderate Mobility, Moderate range | Low Mobility, Short range |
> | Carrier frequency (fc) | 7 GHz | 4 GHz | 30 GHz |
> | Bandwidth | 100 MHz | 100 MHz | 400 MHz |
> | Waveform | CP-OFDM | CP-OFDM | CP-OFDM |
> | SCS | 30 kHz | 30 kHz | 120 kHz |
> | CP length mode | Normal CP | Normal CP | Normal CP |
> | Number of sensing symbols within CPI | 256 | 64 | 64 |
> | Sensing RS comb size (RE) | 1 | 1 | 1 |
> | Freq. comb size for effective CP length extension (only for frame structure evaluation) | 4 | 4 | 4 |
> | Number of successive symbols for effective CP length extension (only for frame structure evaluation) Note: Combination of comb size and symbol repetition is not mandated. | 2 | 2 | 2 |
> | Sensing symbol periodicity | 3 symbols | 13 symbols | 40 symbols |
> | ISD | 1732 m | 500 m | 20 m |
> | Min. mono-/bi-static range | 20 m | 4 m | 2 m |
> | Max. mono-/bi-static range | 3504 m | 500 m | 20 m |
> | Min. Sensing Target radial velocity | 3 km/h | 3 km/h | 1 km/h |
> | Max. Sensing Target radial velocity | 320 km/h | 140 km/h | 3 km/h |
> | Sensing target RCS Note: Combination of RCS and other parameters should be aligned with the agreed SLS assumption in AI 10.8.1. | RCS based on Clause 7.9.2.1 in TR 38.901 | RCS based on Clause 7.9.2.1 in TR 38.901 | RCS based on Clause 7.9.2.1 in TR 38.901 |
> | Benchmark RS | Information | Information | Information |
> | RS for UE transmission | NR UL SRS (ZC sequence) | NR UL SRS (ZC sequence) | NR UL SRS (ZC sequence) |
> | RS for TRP transmission | NR DL CSI-RS (Gold sequence) | NR DL CSI-RS (Gold sequence) | NR DL CSI-RS (Gold sequence) |
> Note: as example, the source of parameters: first column from UAV, second column from vehicle, third column from human case.

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · [R1-2607997](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2607997.zip) · `[126bis-R20-6GR-ISAC-Waveform and FS]`

### RAN1#126 — 3건

**Conclusion** · `8.2` Maintenance on others · `RAN1#126:8.2:006` · 후보

> The following issues are not pursed for Rel-19 SBFD maintenance.
> | RAN1#126 Tdoc number | Issue |
> | R1-2605415 | Sub-band configuration |
> | R1-2605445 | HARQ-ACK codebook construction |
> | R1-2605671 | Valid symbol type for PUCCH for UEIRI and SRS for antenna switching |
> | R1-2605708 | SBFD configuration |
> | R1-2605804 | PUSCH transmission power by UL resource muting |
> | R1-2606717 | CLI measurement resource across both SBFD and non-SBFD symbols within a slot |

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2605539](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2605539.zip) · `[126-R19-AI 8.2]`

**Agreement** · `10.4.2` Operation in connected mode · `RAN1#126:10.4.2:001` · 후보 · 관련 주제: CSI 보고/codebook

> Study UL transmission switching across carriers in 6GR, at least considering the following:
> - Whether/how to achieve unified design for all UL signals/channels
> - Signaling for switching, e.g., dynamic and/or semi-static switching
> - Number of Tx chains
> - Number of carriers
> - Switching gap
> - Interaction with carrier aggregation operation
> - Coordination with other WG(s), e.g., RAN4 (as needed)
> - Note: SRS antenna switching is separately discussed under UL CSI agenda

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-MC-Operation in connected mode]`

**Agreement** · `10.5.5` Other physical layer signals, channels and procedure · `RAN1#126:10.5.5:007` · 후보

> For UE-to-UE CLI measurement in 6GR, the followings are recommended:
> - Support RSRP and RSSI as the measurement metrics
>   - Wideband RSSI measurement is supported.
>   - FFS on subband RSSI measurement.
> - Support to use SRS for RSRP measurement
> - Support to use CLI RSSI measurement resource for RSSI measurement
>   - For SBFD, UE measures the UE-to-UE CLI in UL subband
> - FFS: For SBFD, whether the UE can measure CLI in UL subband in the time duration of DL reception.
> - FFS: whether the UE measures the UE-to-UE CLI in DL subband in SBFD.

남은 FFS 3건

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Other signals, channels, and procedures]`

### RAN1#125 — 5건

**Conclusion** · `7` Pre-Rel-19 NR Maintenance · `RAN1#125:7:001` · 후보

> The issue raised in R1-2604674 is resolved by the following solution.
> - A UE does not expect NW triggering two aperiodic SRS resource sets with the same SRS trigger state for xTxR antenna switching.
> - No specification impact of the above.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2605101](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2605101.zip)

**Agreement** · `8.2` Maintenance on others · `RAN1#125:8.2:004` · 후보 · 관련 주제: CSI 보고/codebook

> Adopt the following TP for 38.214 as alignment CR.
> | Reason for change: | The parameter name ‘srs-ResourceSetToAddModListDCI-0-2-SBFD’ in Clause 6.2.1.5 is incorrect. |
> |  |  |
> | Summary of change: | Change ‘srs-ResourceSetToAddModListDCI-0-2-SBFD’ to ‘srs-ResourceSetToAddModListDCI-0-2’. |
> |  |  |
> | Consequences if not approved: | Incorrect parameter name |
> ---------------------------------------------------------- Start of the text proposal ----------------------------------------------
> 6.2.1.5	UE sounding procedure for SBFD
> <unchanged texts omitted>
> For a same usage of 'codebook', 'noncodebook', or ‘beamManagement’, for the SRS resource sets provided in srs-ResourceSetToAddModList or srs-ResourceSetToAddModListDCI-0-2-SBFD, the number of SRS resources in a SRS resource set where symbolType is set to ‘sbfd’ is the same as the number of SRS resources in a SRS resource set where symbolType is set to ‘non-sbfd’.
> <unchanged texts omitted>
> ---------------------------------------------------------- End of the text proposal ----------------------------------------------
> LP-WUS

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2605066](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2605066.zip)

**Agreement** · `10.5.2.3` Uplink transmission scheme(s) for uplink channels · `RAN1#125:10.5.2.3:007` · 후보

> Study whether/how to support closed-loop frequency selective precoding based PUSCH transmission for 6GR, considering at least following:
> - Wideband precoding as baseline for evaluation purpose
> - Applicable number of UE antenna port(s) and rank(s)
> - Applicable waveform(s)
> - Factors impacted on performance and complexity in UE/NW
>   - Frequency selective precoding granularity
>   - PAPR
>   - Realistic channel estimation
>   - UE antenna model
>   - SRS sounding overhead & channel aging
>   - Link budget
>   - UL Link adaptation
>   - UE TX coherency
>   - PUSCH frequency resource allocation per UE
>   - Number of BS RX antennas
>   - UL precoder design and indication method with signaling overhead & potential overhead reduction
>   - Other factors are not precluded

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Transmission scheme for UL channels]`

**Agreement** · `10.5.2.3` Uplink transmission scheme(s) for uplink channels · `RAN1#125:10.5.2.3:011` · 후보 · 관련 주제: CSI 보고/codebook, CSI-RS

> Study DL/UL reciprocity based PUSCH transmission for 6GR, considering at least following candidate schemes:
> - Scheme 1. CSI-RS based DL channel estimation by UE, UE calculates UL precoder, UE transmits (precoded) SRS, and NW indicates UE precoder information to schedule (e.g., analogous with non-codebook based PUSCH in NR)
> - Scheme 2. CSI-RS-based DL channel acquisition by UE, UE reports channel information to NW, and NW selects an UL precoder to schedule UE
>   - FFS: What channel information UE reports
>   - FFS: how to determine UL precoder
>   - FFS: UL link adaptation
> - Scheme 3. CSI-RS-based DL channel acquisition by UE, UE reports channel information to NW and/or send SRS, the NW indicates the information on the desired UL precoder, the UE calculates/selects the precoder
>   - FFS: What channel information UE reports
>   - FFS: How NW indicates the information on the desired UL precoder
>   - FFS: How to represent the information
>   - FFS: How the UE calculates/selects the precoder.
> - Other scheme(s) are not precluded.
> - Note: For any scheme(s) requiring DL/UL reciprocity at UE side, the feasibility of DL/UL reciprocity at UE side should be considered.
> - Potential benefit(s) & scenario(s) over codebook-based PUSCH transmission as baseline
> For the purpose of performance evaluation of DL/UL reciprocity based PUSCH transmission for 6GR, consider the following antenna calibration error:
> - Antenna calibration error can be modeled as
>   - represents the uplink channel obtained using DL/UL reciprocity at UE side and has a dimension .
>   - is the downlink channel derived by CSI-RS and has a dimension .
>   - is the number of antenna ports of UE,  is the number antenna ports of aNB.
>   - is the amplitude mismatch coefficient and could be modeled as subject to uniform or Gaussian distribution, e.g., Gaussian distribution with zero mean and variance X1=0.35 dB.
>   - is the phase mismatch coefficient and could be modeled as subject to uniform or Gaussian distribution, e.g., Gaussian distribution with zero mean and variance Y1=5 degrees.
>   - Other values on X1 and Y1 can be considered and reported by companies.
>   - is the amplitude mismatch coefficient and could be modeled as subject to uniform or Gaussian distribution, e.g., Gaussian distribution with zero mean and variance X2 dB.
>   - is the phase mismatch coefficient and could be modeled as subject to uniform or Gaussian distribution, e.g., Gaussian distribution with zero mean and variance Y2 degrees.
>   - Values on X2 and Y2 are reported by companies.
>   - The distribution of  and  can also be reported by companies.
>   - Both or either of aNB or UE-side antenna calibration error can be used in the simulation and is reported by companies.
>   - It is assumed that DL/UL reciprocity calibration error is constant in UL scheduled bandwidth.
>   - Companies report how DL/UL reciprocity calibration error behavior in time domain considering UL coherency is modeled.
> - Send LS to RAN4 to inform the above contents and ask for feedback on model assumption above, whether DL/UL reciprocity can be achieved at UE side considering different UE implementations
> - RAN1 continue to study, and after RAN1 sensitivity check, send an LS to RAN4 to inform the above and the outcome, with potential assessment/check from RAN4

남은 FFS 7건

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Transmission scheme for UL channels]`

**Agreement** · `10.5.5` Other physical layer signals, channels and procedure · `RAN1#125:10.5.5:003` · 후보

> For UE-to-UE CLI measurement and reporting in 6GR:
> - RAN1 to study the following metrics for UE-to-UE CLI measurements:
>   - RSSI and RSRP for direct interference, e.g., intra-band or intra-subband CLI.
>   - RSSI to measure the leakage of the interference, e.g., inter-subband CLI.
>   - The frequency domain granularity for measurement to be considered are: subband and wideband.
> - RAN1 to study the following methods of CLI measurement resources:
>   - CLI measurement based on explicit configuration of CLI RSSI measurement resource and/or SRS for RSRP measurement.
>   - CLI measurement/detection without explicit measurement resource configuration, e.g., exploit PDSCH reception to measure/detect CLI.
> - Study network-controlled CLI reporting.
>   - The benefits/drawbacks of network-controlled CLI reporting.
>   - The reporting signalling and triggering mechanisms.
>   - Study the following candidate reporting contents:
>     - Option 1: N strongest RSRP or RSSI and corresponding resource indicators.
>       - Report RSRP/RSSI for the strongest one and differential RSRP/RSSI for the other N-1.
>     - Option 2: indication of whether each measurement resource has RSRP or RSSI measurement larger than a threshold, for example one bitmap with each bit corresponding to one measurement resource.
>     - and any other options.
> - Study UE-initiated/event-triggering CLI reporting for overhead reduction and energy saving, at least considering the following aspects:
>   - The benefits over the network-controlled reporting.
>   - The definition of CLI event and study how to trigger the CLI reporting.
>   - The measurement resource/occasions for UE to detect the CLI event.
>   - The reporting contents and the UL reporting mechanism.
> - For the time alignment issue of CLI measurement resource:
>   - Study the reference timing that is used for each associated measurement occasions.
>   - Study whether/how the time alignment issue has impact on CLI measurement performance.
>   - Study the methods to handle the time alignment, if necessary

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Other signals, channels, and procedures]`

### RAN1#124bis — 3건

**Agreement** · `8.3` Maintenance on Evolution of NR duplex operation: Sub-band full duplex (SBFD) · `RAN1#124bis:8.3:002` · 후보 · 관련 주제: CSI 보고/codebook, CSI-RS

> Adopt the following TPs for TS38.214 and TS38.213.
> | 6.2.1.5 UE sounding procedure for SBFD *** Unchanged parts are omitted *** For a periodic or semi-persistent SRS resource, UE doesn’t transmit an SRS transmission occasion that is mapped to SBFD symbols and non-SBFD symbols. *** Unchanged parts are omitted *** |
> | Reason for change Current specification is missing the implementation of RAN1 agreement that UE should drop SRS transmission occasion that is mapped to SBFD and non-SBFD symbols. Without this correction, the specification gives a wrong understanding for UE transmission behavior for an SRS transmission occasion across mixed symbol type, in which UE should transmit SRS only in the valid symbol type. Summary of change Capture UE behavior for a periodic or semi-persistent SRS resource in which the UE doesn’t transmit the SRS transmission occasion that is mapped to SBFD symbols and non-SBFD symbols. |
> | 5.2.1.4.1 Resource Setting configuration *** Unchanged parts are omitted *** For a CSI report associated with semi-persistent or periodic CSI-RS, if a UE is configured with SBFD symbols and a CSI-ReportConfig with the higher layer parameter symbolType, the UE only considers the CSI-RS occasions within either SBFD symbol(s) or non-SBFD symbol(s) as indicated by symbolType for the CSI derivation for the CSI report. The symbolType configured in CSI-ReportConfig applies to NZP-CSI-RS resources that are associated with the CSI report and configured for both channel measurement and interference measurement. For a periodic or semi-persistent CSI-RS, UE doesn’t receive the CSI-RS reception occasion that is mapped to SBFD symbols and non-SBFD symbols. *** Unchanged parts are omitted *** |
> | Reason for change Current specification is missing the implementation of RAN1 agreement that UE should drop CSI-RS reception occasion that is mapped to SBFD and non-SBFD symbols. Summary of change Capture UE behavior for a periodic or semi-persistent CSI-RS resource in which the UE doesn’t receive the CSI-RS reception occasion that is mapped to SBFD symbols and non-SBFD symbols. |
> | 11.1 Slot configuration *** Unchanged parts are omitted *** Except for a PRACH transmission in a PRACH occasion determined based on a second RACH configuration provided by sbfd-RACHDualConfig as described in clause 8, the UE transmits or receives a physical channel or signal either only in SBFD symbols or only in non-SBFD symbols. For a PUCCH transmission with SP-CSI reports, or for a PUCCH with SR, LRR, UEIRI, UE doesn’t transmit the PUCCH transmission occasion that is mapped to SBFD symbols and non-SBFD symbols. *** Unchanged parts are omitted *** |
> | Reason for change Current specification is missing the implementation of RAN1 agreement that UE should drop P/SP PUCCH transmission occasion that is mapped to SBFD and non-SBFD symbols. Summary of change Capture UE behavior for a periodic or semi-persistent PUCCH transmission occasion in which the UE doesn’t transmit the PUCCH occasion that is mapped to SBFD symbols and non-SBFD symbols. |
> Final CRs in R1-2603431 and R1-2603468 are endorsed.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2603361](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603361.zip) · `[124b-R19-SBFD]`

**Agreement** · `10.5.2.3` Uplink transmission scheme(s) for uplink channels · `RAN1#124bis:10.5.2.3:003` · 후보 · 관련 주제: CSI 보고/codebook

> Support the following table as the assumption of LLS for evaluation of PUSCH and DMRS.
> | Parameters | Proposals |
> | #1 Carrier frequency | Around 0.7 GHz, FDD Around 2 GHz, FDD Around 4 GHz, TDD Around 7 GHz, TDD Around 30 GHz, TDD |
> | #2 SCS | 15 kHz for FDD 30 kHz for TDD and around 2 - 7 GHz 120 kHz for TDD and around 30 GHz |
> | #3 Waveform | CP-OFDM, DFTS-OFDM |
> | #4 System BW | 20 MHz 100 MHz Other bandwidths are not precluded (reported by company) |
> | #4-1 RB allocation | Small: 4, 8 RBs Medium: 24 RBs Large: 48 RBs Other values are not precluded (reported by company) |
> | #5 Channel model | CDL-A/C/D in TR 38.901 TDL-A/C in TR 38.901 (optional) Other channel models are not precluded (reported by company) |
> | #5-1 MU-MIMO interference model | FFS: How to model MU-MIMO channel (e.g., can emulate low correlation among MU scheduled UEs) FFS: same RB allocation among MU scheduled UEs |
> | #6 Delay spread | 30 ns 100 ns 300 ns 1000 ns (optional) |
> | #7 UE speed | 3 km/h, 30 km/h, 120 km/h, 350 km/h, 500 km/h Additional assumption of 0.3 km/h for FWA |
> | #8 UE antenna configuration | Align with SLS assumption for PUSCH |
> | #8-1 CPE antenna configuration | Align with SLS assumption for PUSCH |
> | #9 BS antenna configuration | Align with SLS assumption for PUSCH |
> | #10 Precoding granularity | Reported by company, wideband precoding is baseline |
> | #11 SRS configuration | Reported by company |
> | #12 Link adaptation | AMC or fixed MCS |
> | #12-1 HARQ | No HARQ as baseline HARQ retransmission as optional |
> | #13 Channel estimation | Realistic, Ideal (as the upper bound, optional) Note: This also includes noise and interference estimation |
> | #14 Receiver | Baseline: MMSE-IRC Other can be reported by company |
> | #15 DMRS specific assumptions | Rel-15 NR Type 1/2, Rel-18 NR eType 1/2 design as baseline used for comparison (reported by companies which type(s) is used) For 6G PUSCH DMRS design, the following(s) can be reported by company, e.g., DMRS pattern used (including mapping in time and frequency), DMRS overhead, port allocation strategies, DMRS sequence, power boosting / multiplexing with data in FDM manner, etc |
> | #16 MIMO scheme | Reported by company (e.g., SU/MU-MIMO, max rank, fixed rank/rank adaptation, UL codebook) |
> | #17 Performance metric | BLER, throughput, PAPR MSE (optional) Net gain (optional, if applicable) which the definition is aligned based agreement in RAN1#122bis 6GR waveform agenda |
> | #18 Impairments | Align with SLS assumption for PUSCH |
> | #19 TB size determination | Reported by company how TB size is determined |

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Transmission scheme for UL channels]`

**Agreement** · `10.5.2.3` Uplink transmission scheme(s) for uplink channels · `RAN1#124bis:10.5.2.3:008` · 후보 · 관련 주제: CSI 보고/codebook

> Support codebook based PUSCH transmission for 6GR, and study at least the following aspects:
> - UL precoder is selected from an UL codebook, based on UL CSI acquisition in NW to schedule UE
>   - As baseline, SRS is used for UL CSI acquisition
>   - FFS: Which RS/method can be used to obtain UL CSI, other than SRS
> - UL codebook design, at least considering
>   - Fixed codebook which is pre-defined in specification
>   - Configurable codebook which can be configured by NW
>   - Hybrid approach of fixed and configurable codebook
>   - performance, resolution, overhead, codebook size comparing to 5G NR
>   - Diverse UE coherency capabilities
>   - Diverse UE Tx antenna structures

남은 FFS 1건

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Transmission scheme for UL channels]`

### RAN1#124 — 6건

**Agreement** · `8.3` Maintenance on Evolution of NR duplex operation: Sub-band full duplex (SBFD) · `RAN1#124:8.3:001` · 후보 · 관련 주제: Beam management, CSI-RS

> Adopt the following TP to Clause 5.1 and 6.1, TS 38.214
> | Reason for change: | In the legacy, for multi-PUSCH scheduled by a single DCI and multi-PUSCH configured grant, PUSCH(s) not transmitted due to collision with legacy DL symbols indicated by tdd-UL-DL-ConfigurationCommon or tdd-UL-DL-ConfigurationDedicated or SSB symbols is not assigned with an HARQ process ID. However, if SBFD subbands is configured in legacy DL symbols, PUSCH transmission occasions in the SBFD-DL symbols should be valid and assigned with an HARQ process ID. In addition, PUSCH transmission occasion colliding with symbol(s) that is not the valid symbol type or across two symbol types should be invalid and not assigned with an HARQ process ID. For multi-PDSCH scheduled by a single DCI, PDSCH(s) not received due to collision with legacy UL symbols indicated by tdd-UL-DL-ConfigurationCommon or tdd-UL-DL-ConfigurationDedicated is not assigned with an HARQ process ID. However, with introduction of SBFD, PDSCH reception occasion colliding with symbol(s) that is not the valid symbol type or across two symbol types should be invalid and not assigned with an HARQ process ID. |
> |  |  |
> | Summary of change: | Clarify UE behavior for HARQ process ID determination for multi-PDSCH/PUSCH |
> |  |  |
> | Consequences if not approved: | PUSCH transmissions in SBFD-DL symbols cannot be assigned corresponding HARQ process IDs. PDSCH receptions colliding with symbol(s) that is not the valid symbol type or across two symbol types are unnecessary consuming HARQ process ID. |
> |  |  |
> | 5 Physical downlink shared channel related procedures 5.1 UE procedure for receiving the physical downlink shared channel <<omitted text>> A UE shall upon detection of a PDCCH with a configured DCI format 1_0, 1_1, 1_2, 1_3, 4_0, 4_1, or 4_2 decode the corresponding PDSCHs as indicated by that DCI. When the UE is scheduled with multiple PDSCHs on a serving cell by a DCI, HARQ process ID indicated by this DCI applies to the first PDSCH not overlapping with a UL symbol indicated by tdd-UL-DL-ConfigurationCommon or tdd-UL-DL-ConfigurationDedicated if provided, and, if applicable, not overlapping with a symbol that is not the valid symbol type and not across SBFD symbols and non-SBFD symbols according to clause 5.1.2.1a., HARQ process ID is then incremented by 1 for each subsequent PDSCH(s) in the scheduled order, with modulo operation of nrofHARQ-ProcessesForPDSCH applied if nrofHARQ-ProcessesForPDSCH is provided, or with modulo operation of nrofHARQ-ProcessesForPDSCH-v1700 applied if or nrofHARQ-ProcessesForPDSCH-v1700 is provided, or with modulo operation of 8 applied, otherwise. HARQ process ID is not incremented for PDSCH(s) not received if at least one of the symbols indicated by the indexed row of the used resource allocation table in the slot overlaps with a UL symbol indicated by tdd-UL-DL-ConfigurationCommon or tdd-UL-DL-ConfigurationDedicated if provided, or, if applicable, the symbols indicated by the indexed row of the used resource allocation table in the slot overlap with a symbol that is not the valid symbol type or include SBFD symbols and non-SBFD symbols according to clause 5.1.2.1a. When a UE is configured by the higher layer parameter repetitionScheme set to 'tdmSchemeA', the PDSCH includes two PDSCH transmission occasions. For each PDSCH, if either PDSCH occasion overlaps with a UL symbol indicated by tdd-UL-DL-ConfigurationCommon or tdd-UL-DL-ConfigurationDedicated if provided, the PDSCH is not received and HARQ process ID is not increment for the PDSCH. For any HARQ process ID(s) in a given scheduled cell, the UE is not expected to receive a PDSCH that overlaps in time with another PDSCH if the UE is not capable of receiving FDMed unicast and multicast PDSCH per slot per carrier. When HARQ feedback for the HARQ process ID is not disabled, or for the HARQ process associated with the first SPS PDSCH when HARQ-feedbackEnablingforSPSactive is provided and enabled, the UE is not expected to receive another PDSCH for a given HARQ process until after the end of the expected transmission of HARQ-ACK for that HARQ process, where the timing is given by Clause 9.2.3 of [6, TS 38.213]. For HARQ-ACK subject to HARQ-ACK deferral described in Clause 9.2.5.4 of [6 TS 38.213], the expected transmission of HARQ-ACK corresponds to the expected transmission HARQ-ACK in a first slot. When HARQ feedback for the HARQ process ID is disabled, the UE is not expected to receive another PDCCH carrying a DCI scheduling a PDSCH or set of slot-aggregated PDSCH scheduled for the given HARQ process or to receive another PDSCH without corresponding PDCCH for the given HARQ process that starts until Tproc,1 after the end of the reception of the last PDSCH or slot-aggregated PDSCH for that HARQ process. Except for the case when a UE is configured by higher layer parameter PDCCH-Config that contains two different values of coresetPoolIndex in ControlResourceSet and PDCCHs that schedule two PDSCHs are associated to different ControlResourceSets having different values of coresetPoolIndex and the UE reports its capability of outOfOrderOperationDL-r16, in a given scheduled cell, the UE is not expected to receive a first PDSCH and a second PDSCH, starting later than the first PDSCH, with its corresponding HARQ-ACK assigned to be transmitted on a resource ending before the start of a different resource for the HARQ-ACK assigned to be transmitted for the first PDSCH, where the two resources are in different slots for the associated HARQ-ACK transmissions, each slot is composed of symbols [4] or a number of symbols indicated by subslotLengthForPUCCH if provided, and the HARQ-ACK for the two PDSCHs are associated with the HARQ-ACK codebook of the same priority. Except for the case when a UE is configured by higher layer parameter PDCCH-Config that contains two different values of coresetPoolIndex in ControlResourceSet and PDCCHs that schedule two PDSCHs are associated to different ControlResourceSets having different values of coresetPoolIndex and the UE reports its capability of outOfOrderOperationDL-r16, in a given scheduled cell, the UE is not expected to receive a first PDSCH and a second PDSCH, starting later than the first PDSCH, with its corresponding HARQ-ACK assigned to be transmitted on a resource ending before the start of a different resource for the HARQ-ACK assigned to be transmitted for the first PDSCH if the HARQ-ACK for the two PDSCHs are associated with HARQ-ACK codebooks of different priorities. For any two HARQ process IDs in a given scheduled cell, if the UE is scheduled to start receiving a first PDSCH starting in symbol j by a PDCCH ending in symbol i on a scheduling cell, the UE is not expected to be scheduled to receive a PDSCH starting earlier than the end of the first PDSCH with a PDCCH that ends later than symbol i of a scheduling cell,. When the PDCCH reception includes two PDCCH candidates from two respective search space sets, as described in clause 10.1 of [6, TS 38.213], the PDCCH ending in symbol i is determined based on the PDCCH candidate that ends later in time. In a given scheduled cell, for any PDSCH corresponding to SI-RNTI, the UE is not expected to decode a re-transmission of an earlier PDSCH with a starting symbol less than N symbols after the last symbol of that PDSCH, where the value of N depends on the PDSCH subcarrier spacing configuration , with N=13 for =0, N=13 for =1, N=20 for =2, N=24 for =3, N=96 for =5, and N=192 for =6. <<omitted text>> 6 Physical uplink shared channel related procedure 6.1 UE procedure for transmitting the physical uplink shared channel <<omitted text>> When the UE is configured dl-OrJointTCI-StateList or ul-TCI-StateList, the UE shall perform PUSCH transmission corresponding to a Type 1 configured grant or a Type 2 configured grant or a dynamic grant according to the spatial relation, if applicable, with a reference to the RS for determining UL Tx spatial filter. The RS is determined based on an RS configured with qcl-Type set to 'typeD' of the indicated TCI-State or an RS in the indicated TCI-UL-State. The reference RS in the indicated TCI-State can be a CSI-RS resource in a NZP-CSI-RS-ResourceSet configured with higher layer parameter repetition, or a CSI-RS resource in an NZP-CSI-RS-ResourceSet configured with higher layer parameter trs-Info. The reference RS in the indicated TCI-UL-State can be a CSI-RS resource in a NZP-CSI-RS-ResourceSet configured with higher layer parameter repetition, a CSI-RS resource in an NZP-CSI-RS-ResourceSet configured with higher layer parameter trs-Info, an SRS resource in an SRS resource set with the higher layer parameter usage set to 'beamManagement', or SS/PBCH block associated with the same or different PCI from the PCI of the serving cell. When nrofSlotsInCG-Period is configured for Type 1 configured grant or Type 2 configured grant, HARQ process ID for the first configured PUSCH grant and each subsequent valid configured PUSCH grant within a periodicity of the configuration is determined as in clause 5.4.1 of [10, TS 38.321], where a valid configured PUSCH grant is the one not colliding with the DL symbol(s) indicated by tdd-UL-DL-ConfigurationCommon or tdd-UL-DL-ConfigurationDedicated if provided, and, when applicable, not indicated as SBFD by tdd-UL-DL-ConfigurationCommon, and not colliding with a symbol(s) of an SS/PBCH block with index provided by ssb-PositionsInBurst as described in clause 11.1 of [6, TS 38.213] and, if applicable, not colliding with a symbol that is not the valid symbol type and not across SBFD symbols and non-SBFD symbols according to clause 6.1.2.1a. <<omitted text>> When the UE is scheduled with multiple PUSCHs on a serving cell by a DCI, HARQ process ID indicated by this DCI applies to the first PUSCH not overlapping with a DL symbol indicated by tdd-UL-DL-ConfigurationCommon or tdd-UL-DL-ConfigurationDedicated if provided, and, when applicable, not indicated as SBFD by tdd-UL-DL-ConfigurationCommon, or a symbol of an SS/PBCH block with index provided by ssb-PositionsInBurst, or, if applicable, a symbol that is not the valid symbol type and not across SBFD symbols and non-SBFD symbols according to clause 6.1.2.1a., HARQ process ID is then incremented by 1 for each subsequent PUSCH(s) in the scheduled order, with modulo operation of nrofHARQ-ProcessesForPUSCH applied if nrofHARQ-ProcessesForPUSCH is provided, or with modulo operation of 16 applied, otherwise. HARQ process ID is not incremented for PUSCH(s) not transmitted if at least one of the symbols indicated by the indexed row of the used resource allocation table in the slot overlaps with a DL symbol indicated by tdd-UL-DL-ConfigurationCommon or tdd-UL-DL-ConfigurationDedicated if provided, and, when applicable, not indicated as SBFD by tdd-UL-DL-ConfigurationCommon, or a symbol of an SS/PBCH block with index provided by ssb-PositionsInBurst, or, if applicable, the symbols indicated by the indexed row of the used resource allocation table in the slot overlap with a symbol that is not the valid symbol type or include SBFD symbols and non-SBFD symbols according to clause 6.1.2.1a. For any HARQ process ID(s) in a given scheduled cell, the UE is not expected to transmit a PUSCH that overlaps in time with another PUSCH. Except for the case when a UE is configured by higher layer parameter PDCCH-Config that contains two different values of coresetPoolIndex in ControlResourceSet for the active BWP of a serving cell and PDCCHs that schedule two PUSCHs are associated to different ControlResourceSets having different values of coresetPoolIndex and the UE reports its capability of outOfOrderOperationUL-r16 or outOfOrderOperationUL-r18, for any two HARQ process IDs in a given scheduled cell, if the UE is scheduled to start a first PUSCH transmission starting in symbol j by a PDCCH ending in symbol i on a scheduling cell,, the UE is not expected to be scheduled to transmit a PUSCH starting earlier than the end of the first PUSCH by a PDCCH that ends later than symbol i of the scheduling cell. When the PDCCH reception includes two PDCCH candidates from two respective search space sets, as described in clause 10.1 of [6, TS 38.213], for the purpose of determining the PDCCH ending in symbol i, the PDCCH candidate that ends later in time is used. The UE is not expected to be scheduled to transmit another PUSCH by a DCI format 0_0 with CRC scrambled by TC-RNTI, for a given HARQ process with the DCI received before the end of the expected transmission of the last PUSCH for that HARQ process if the latter is scheduled by a DCI format 0_0 with CRC scrambled by TC-RNTI or by an UL grant in RA Response. The UE is not expected to be scheduled to transmit another PUSCH by DCI format 0_0, 0_1, 0_2 or 0_3 scrambled by C-RNTI, CS-RNTI or MCS-C-RNTI for a given HARQ process with the DCI received before the end of the expected transmission of the last PUSCH for that HARQ process if the latter is scheduled by a DCI with CRC scrambled by C-RNTI, CS-RNTI or MCS-C-RNTI. <<omitted text>> | 5 Physical downlink shared channel related procedures 5.1 UE procedure for receiving the physical downlink shared channel <<omitted text>> A UE shall upon detection of a PDCCH with a configured DCI format 1_0, 1_1, 1_2, 1_3, 4_0, 4_1, or 4_2 decode the corresponding PDSCHs as indicated by that DCI. When the UE is scheduled with multiple PDSCHs on a serving cell by a DCI, HARQ process ID indicated by this DCI applies to the first PDSCH not overlapping with a UL symbol indicated by tdd-UL-DL-ConfigurationCommon or tdd-UL-DL-ConfigurationDedicated if provided, and, if applicable, not overlapping with a symbol that is not the valid symbol type and not across SBFD symbols and non-SBFD symbols according to clause 5.1.2.1a., HARQ process ID is then incremented by 1 for each subsequent PDSCH(s) in the scheduled order, with modulo operation of nrofHARQ-ProcessesForPDSCH applied if nrofHARQ-ProcessesForPDSCH is provided, or with modulo operation of nrofHARQ-ProcessesForPDSCH-v1700 applied if or nrofHARQ-ProcessesForPDSCH-v1700 is provided, or with modulo operation of 8 applied, otherwise. HARQ process ID is not incremented for PDSCH(s) not received if at least one of the symbols indicated by the indexed row of the used resource allocation table in the slot overlaps with a UL symbol indicated by tdd-UL-DL-ConfigurationCommon or tdd-UL-DL-ConfigurationDedicated if provided, or, if applicable, the symbols indicated by the indexed row of the used resource allocation table in the slot overlap with a symbol that is not the valid symbol type or include SBFD symbols and non-SBFD symbols according to clause 5.1.2.1a. When a UE is configured by the higher layer parameter repetitionScheme set to 'tdmSchemeA', the PDSCH includes two PDSCH transmission occasions. For each PDSCH, if either PDSCH occasion overlaps with a UL symbol indicated by tdd-UL-DL-ConfigurationCommon or tdd-UL-DL-ConfigurationDedicated if provided, the PDSCH is not received and HARQ process ID is not increment for the PDSCH. For any HARQ process ID(s) in a given scheduled cell, the UE is not expected to receive a PDSCH that overlaps in time with another PDSCH if the UE is not capable of receiving FDMed unicast and multicast PDSCH per slot per carrier. When HARQ feedback for the HARQ process ID is not disabled, or for the HARQ process associated with the first SPS PDSCH when HARQ-feedbackEnablingforSPSactive is provided and enabled, the UE is not expected to receive another PDSCH for a given HARQ process until after the end of the expected transmission of HARQ-ACK for that HARQ process, where the timing is given by Clause 9.2.3 of [6, TS 38.213]. For HARQ-ACK subject to HARQ-ACK deferral described in Clause 9.2.5.4 of [6 TS 38.213], the expected transmission of HARQ-ACK corresponds to the expected transmission HARQ-ACK in a first slot. When HARQ feedback for the HARQ process ID is disabled, the UE is not expected to receive another PDCCH carrying a DCI scheduling a PDSCH or set of slot-aggregated PDSCH scheduled for the given HARQ process or to receive another PDSCH without corresponding PDCCH for the given HARQ process that starts until Tproc,1 after the end of the reception of the last PDSCH or slot-aggregated PDSCH for that HARQ process. Except for the case when a UE is configured by higher layer parameter PDCCH-Config that contains two different values of coresetPoolIndex in ControlResourceSet and PDCCHs that schedule two PDSCHs are associated to different ControlResourceSets having different values of coresetPoolIndex and the UE reports its capability of outOfOrderOperationDL-r16, in a given scheduled cell, the UE is not expected to receive a first PDSCH and a second PDSCH, starting later than the first PDSCH, with its corresponding HARQ-ACK assigned to be transmitted on a resource ending before the start of a different resource for the HARQ-ACK assigned to be transmitted for the first PDSCH, where the two resources are in different slots for the associated HARQ-ACK transmissions, each slot is composed of symbols [4] or a number of symbols indicated by subslotLengthForPUCCH if provided, and the HARQ-ACK for the two PDSCHs are associated with the HARQ-ACK codebook of the same priority. Except for the case when a UE is configured by higher layer parameter PDCCH-Config that contains two different values of coresetPoolIndex in ControlResourceSet and PDCCHs that schedule two PDSCHs are associated to different ControlResourceSets having different values of coresetPoolIndex and the UE reports its capability of outOfOrderOperationDL-r16, in a given scheduled cell, the UE is not expected to receive a first PDSCH and a second PDSCH, starting later than the first PDSCH, with its corresponding HARQ-ACK assigned to be transmitted on a resource ending before the start of a different resource for the HARQ-ACK assigned to be transmitted for the first PDSCH if the HARQ-ACK for the two PDSCHs are associated with HARQ-ACK codebooks of different priorities. For any two HARQ process IDs in a given scheduled cell, if the UE is scheduled to start receiving a first PDSCH starting in symbol j by a PDCCH ending in symbol i on a scheduling cell, the UE is not expected to be scheduled to receive a PDSCH starting earlier than the end of the first PDSCH with a PDCCH that ends later than symbol i of a scheduling cell,. When the PDCCH reception includes two PDCCH candidates from two respective search space sets, as described in clause 10.1 of [6, TS 38.213], the PDCCH ending in symbol i is determined based on the PDCCH candidate that ends later in time. In a given scheduled cell, for any PDSCH corresponding to SI-RNTI, the UE is not expected to decode a re-transmission of an earlier PDSCH with a starting symbol less than N symbols after the last symbol of that PDSCH, where the value of N depends on the PDSCH subcarrier spacing configuration , with N=13 for =0, N=13 for =1, N=20 for =2, N=24 for =3, N=96 for =5, and N=192 for =6. <<omitted text>> 6 Physical uplink shared channel related procedure 6.1 UE procedure for transmitting the physical uplink shared channel <<omitted text>> When the UE is configured dl-OrJointTCI-StateList or ul-TCI-StateList, the UE shall perform PUSCH transmission corresponding to a Type 1 configured grant or a Type 2 configured grant or a dynamic grant according to the spatial relation, if applicable, with a reference to the RS for determining UL Tx spatial filter. The RS is determined based on an RS configured with qcl-Type set to 'typeD' of the indicated TCI-State or an RS in the indicated TCI-UL-State. The reference RS in the indicated TCI-State can be a CSI-RS resource in a NZP-CSI-RS-ResourceSet configured with higher layer parameter repetition, or a CSI-RS resource in an NZP-CSI-RS-ResourceSet configured with higher layer parameter trs-Info. The reference RS in the indicated TCI-UL-State can be a CSI-RS resource in a NZP-CSI-RS-ResourceSet configured with higher layer parameter repetition, a CSI-RS resource in an NZP-CSI-RS-ResourceSet configured with higher layer parameter trs-Info, an SRS resource in an SRS resource set with the higher layer parameter usage set to 'beamManagement', or SS/PBCH block associated with the same or different PCI from the PCI of the serving cell. When nrofSlotsInCG-Period is configured for Type 1 configured grant or Type 2 configured grant, HARQ process ID for the first configured PUSCH grant and each subsequent valid configured PUSCH grant within a periodicity of the configuration is determined as in clause 5.4.1 of [10, TS 38.321], where a valid configured PUSCH grant is the one not colliding with the DL symbol(s) indicated by tdd-UL-DL-ConfigurationCommon or tdd-UL-DL-ConfigurationDedicated if provided, and, when applicable, not indicated as SBFD by tdd-UL-DL-ConfigurationCommon, and not colliding with a symbol(s) of an SS/PBCH block with index provided by ssb-PositionsInBurst as described in clause 11.1 of [6, TS 38.213] and, if applicable, not colliding with a symbol that is not the valid symbol type and not across SBFD symbols and non-SBFD symbols according to clause 6.1.2.1a. <<omitted text>> When the UE is scheduled with multiple PUSCHs on a serving cell by a DCI, HARQ process ID indicated by this DCI applies to the first PUSCH not overlapping with a DL symbol indicated by tdd-UL-DL-ConfigurationCommon or tdd-UL-DL-ConfigurationDedicated if provided, and, when applicable, not indicated as SBFD by tdd-UL-DL-ConfigurationCommon, or a symbol of an SS/PBCH block with index provided by ssb-PositionsInBurst, or, if applicable, a symbol that is not the valid symbol type and not across SBFD symbols and non-SBFD symbols according to clause 6.1.2.1a., HARQ process ID is then incremented by 1 for each subsequent PUSCH(s) in the scheduled order, with modulo operation of nrofHARQ-ProcessesForPUSCH applied if nrofHARQ-ProcessesForPUSCH is provided, or with modulo operation of 16 applied, otherwise. HARQ process ID is not incremented for PUSCH(s) not transmitted if at least one of the symbols indicated by the indexed row of the used resource allocation table in the slot overlaps with a DL symbol indicated by tdd-UL-DL-ConfigurationCommon or tdd-UL-DL-ConfigurationDedicated if provided, and, when applicable, not indicated as SBFD by tdd-UL-DL-ConfigurationCommon, or a symbol of an SS/PBCH block with index provided by ssb-PositionsInBurst, or, if applicable, the symbols indicated by the indexed row of the used resource allocation table in the slot overlap with a symbol that is not the valid symbol type or include SBFD symbols and non-SBFD symbols according to clause 6.1.2.1a. For any HARQ process ID(s) in a given scheduled cell, the UE is not expected to transmit a PUSCH that overlaps in time with another PUSCH. Except for the case when a UE is configured by higher layer parameter PDCCH-Config that contains two different values of coresetPoolIndex in ControlResourceSet for the active BWP of a serving cell and PDCCHs that schedule two PUSCHs are associated to different ControlResourceSets having different values of coresetPoolIndex and the UE reports its capability of outOfOrderOperationUL-r16 or outOfOrderOperationUL-r18, for any two HARQ process IDs in a given scheduled cell, if the UE is scheduled to start a first PUSCH transmission starting in symbol j by a PDCCH ending in symbol i on a scheduling cell,, the UE is not expected to be scheduled to transmit a PUSCH starting earlier than the end of the first PUSCH by a PDCCH that ends later than symbol i of the scheduling cell. When the PDCCH reception includes two PDCCH candidates from two respective search space sets, as described in clause 10.1 of [6, TS 38.213], for the purpose of determining the PDCCH ending in symbol i, the PDCCH candidate that ends later in time is used. The UE is not expected to be scheduled to transmit another PUSCH by a DCI format 0_0 with CRC scrambled by TC-RNTI, for a given HARQ process with the DCI received before the end of the expected transmission of the last PUSCH for that HARQ process if the latter is scheduled by a DCI format 0_0 with CRC scrambled by TC-RNTI or by an UL grant in RA Response. The UE is not expected to be scheduled to transmit another PUSCH by DCI format 0_0, 0_1, 0_2 or 0_3 scrambled by C-RNTI, CS-RNTI or MCS-C-RNTI for a given HARQ process with the DCI received before the end of the expected transmission of the last PUSCH for that HARQ process if the latter is scheduled by a DCI with CRC scrambled by C-RNTI, CS-RNTI or MCS-C-RNTI. <<omitted text>> |
> Final CR is endorsed in R1-2601719.

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601634](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601634.zip) · `[124-R19-SBFD]`

**Agreement** · `8.7.1` Maintenance for Rel-19 NR NTN · `RAN1#124:8.7.1:003` · 후보 · 관련 주제: CSI-RS

> Adopt the following TP for RRC parameters alignment in TS38.213.
> The corresponding final CR for Rel-19 TS38.213 in R1-2601695 is endorsed.
> |  |  |  |
> | Reason for change: | Reason for change: | RRC parameter alignment for UE feature group for supporting the HD-FDD (e)RedCap collision handling |
> |  |  |  |
> | Summary of change: | Summary of change: | Parameter CollisionHandlingOfHDFDDOperation in text is replaced by the correct UE feature name which is ntn-Collision-RedCap |
> |  |  |  |
> | Consequences if not approved: | Consequences if not approved: | Unclear specifications. |
> | 17.2 Half-Duplex UE in paired spectrum A half-duplex UE (HD-UE) in paired spectrum is not capable of simultaneous transmissions and receptions on a serving cell with paired spectrum. This clause is applicable for communication of a HD-UE on a serving cell with paired spectrum. Procedures for a HD-UE are same as described for a UE in all other clauses of this document unless stated otherwise. A HD-UE that operates on a non-NTN serving cell, or a HD-UE that operates on an NTN serving cell and does not indicate , does not expect to detect a DCI format scheduling a reception in a set of symbols and detect a DCI format scheduling a transmission in any symbol from the set of symbols. A HD-UE that operates on an NTN serving cell in the RRC_CONNECTED state, indicates , is scheduled to receive a PDSCH or CSI-RS in a set of symbols based on an indication by a first DCI format, and is scheduled to transmit a PUSCH, PUCCH, or PRACH that overlap with any symbol from the set of symbols based on an indication by a second DCI format, determines - to either receive the PDSCH or the CSI-RS or transmit the PRACH based on the HD-UE implementation; - to either receive the PDSCH or transmit the PUSCH or PUCCH based on the HD-UE implementation, if the first DCI format is provided by a PDCCH the HD-UE received according to a Type0/0A/1/2-PDCCH CSS set; - to receive the PDSCH or the CSI-RS if the first DCI format is not provided by a PDCCH the HD-UE received according to a Type0/0A/1/2-PDCCH CSS set, and the HD-UE is not provided ntn-RedcapPrioritizeUL-Dynamic, and the transmission of the PUCCH or the PUSCH would not start before after the last symbol of the PDCCH reception providing the first DCI format; - to transmit the PUSCH or PUCCH, if the first DCI format is not provided by a PDCCH the HD-UE received according to a Type0/0A/1/2-PDCCH CSS set, and - the HD-UE is provided ntn-RedcapPrioritizeUL-Dynamic, or - the HD-UE is not provided ntn-RedcapPrioritizeUL-Dynamic and the transmission of the PUCCH or the PUSCH would start before after the last symbol of the PDCCH reception providing the first DCI format. A HD-UE that operates on an NTN serving cell in the RRC_CONNECTED state, indicates , is scheduled to receive a PDSCH or CSI-RS based on an indication by a first DCI format, and is scheduled to transmit an SRS based on an indication by a second DCI format and the transmission of the SRS in a set of symbols overlaps with the PDSCH reception or CSI-RS reception, determines - to either receive the PDSCH or transmit the SRS based on the HD-UE implementation, if the first DCI format is provided by a PDCCH the HD-UE received according to a Type0/0A/1/2-PDCCH CSS set; - to receive the PDSCH or the CSI-RS if the first DCI format is not provided by a PDCCH the HD-UE received according to a Type0/0A/1/2-PDCCH CSS set, and the HD-UE is not provided ntn-RedcapPrioritizeUL-Dynamic, and the first symbol from the set of symbols is not before after the last symbol of the PDCCH reception providing the first DCI format; - to transmit the SRS if the first DCI format is not provided by a PDCCH the HD-UE received according to a Type0/0A/1/2-PDCCH CSS set, and - the HD-UE is provided ntn-RedcapPrioritizeUL-Dynamic, or - the HD-UE is not provided ntn-RedcapPrioritizeUL-Dynamic and any symbol from the set of symbols is before after the last symbol of the PDCCH reception providing the first DCI format When a PDCCH reception by a HD-UE includes two PDCCH candidates from corresponding search space sets, as described in clause 10.1, the end of the PDCCH reception is the end of the PDCCH candidate that ends later. If a HD-UE is configured by higher layers to receive a PDCCH, or PDSCH, or CSI-RS, or DL PRS in a set of symbols, the HD-UE receives the PDCCH, or PDSCH, or CSI-RS, or DL PRS if the HD-UE does not detect a DCI format that indicates to the HD-UE to transmit a PUSCH, or PUCCH, or PRACH, or SRS in at least one symbol of the set of symbols; otherwise, the HD-UE does not receive the PDCCH, or PDSCH, or CSI-RS, or DL PRS in the set of symbols. If a HD-UE is configured by higher layers to transmit SRS, or PUCCH, or PUSCH in a set of symbols and the HD-UE detects a DCI format indicating to the HD-UE to receive CSI-RS or PDSCH in a subset of symbols from the set of symbols, then - the HD-UE does not expect to cancel the transmission of the PUCCH or PUSCH in the set of symbols if the first symbol in the set occurs within relative to a last symbol of a PDCCH reception where the HD-UE detects the DCI format; otherwise, the HD-UE cancels the PUCCH, or the PUSCH, or an actual repetition of the PUSCH [6, TS 38.214], determined from clauses 9 and 9.2.5 or clause 6.1 of [6, TS 38.214]. - the HD-UE does not expect to cancel the transmission of SRS in symbols from the subset of symbols that occur within relative to a last symbol of a PDCCH reception where the HD-UE detects the DCI format. The HD-UE cancels the SRS transmission in remaining symbols from the subset of symbols. is the PUSCH preparation time for HD-UE processing capability 1 [6, TS 38.214] assuming and corresponds to the smallest SCS configuration between the SCS configuration of the PDCCH carrying the DCI format and the SCS configuration of the SRS, PUCCH, PUSCH. A HD-UE operating on a non-NTN serving cell, or a HD-UE that operates on an NTN serving cell and does not indicate , does not expect to receive both dedicated higher layer parameters configuring transmission in a set of symbols and dedicated higher layer parameters configuring reception in the set of symbols. The HD-UE does not expect to receive both a Type-0/0A/0B/1/2-PDCCH CSS set configuration for PDCCH reception in a set of symbols and dedicated higher layer parameters configuring transmission in the set of symbols, except a Type-2-PDCCH CSS set configuration for PDCCH reception in a set of symbols and dedicated higher layer parameters configuring configured-grant based PUSCH transmission as described in clause 19.1 in the set of symbols for which case the HD-UE follows the procedure as in clause 5.1B.2.6 of [10, TS 38.133]. The HD-UE expects to be configured with a Type-2-PDCCH CSS set configuration for PDCCH reception such that there is at least one paging occasion that does not overlap with configured-grant based PUSCH transmission as described in clause 19.1 per SI modification period. A HD-UE that operates on an NTN serving cell in the RRC_CONNECTED state, indicates , would receive a PDCCH or would receive a PDSCH or CSI-RS or PRS based on a configuration by higher layers in a set of symbols, and would transmit a PUSCH, PUCCH, or SRS based on a configuration by higher layers that overlap with any symbol from the set of symbols, determines - to either receive the PDCCH or transmit the PUSCH/PUCCH/SRS based on the HD-UE implementation, if the PDCCH reception is according to a Type0/0A/1/2-PDCCH CSS set - to receive the PDCCH, if the PDCCH reception is not according to a Type0/0A/1/2-PDCCH CSS set, or the PDSCH, or the CSI-RS, or the PRS if the HD-UE is not provided ntn-RedcapPrioritizeUL-Semistatic - to transmit the PUSCH, the PUCCH, or the SRS, if the PDCCH reception is not according to a Type0/0A/1/2-PDCCH CSS set, and the HD-UE is provided ntn-RedcapPrioritizeUL-Semistatic A HD-UE that operates on an NTN serving cell in the RRC_INACTIVE state, would receive a PDCCH in a set of symbols and would transmit a PUSCH or SRS that overlap with any symbol from the set of symbols, determines to either receive the PDCCH or transmit the PUSCH or SRS based on the HD-UE implementation. < Unchanged text omitted > | 17.2 Half-Duplex UE in paired spectrum A half-duplex UE (HD-UE) in paired spectrum is not capable of simultaneous transmissions and receptions on a serving cell with paired spectrum. This clause is applicable for communication of a HD-UE on a serving cell with paired spectrum. Procedures for a HD-UE are same as described for a UE in all other clauses of this document unless stated otherwise. A HD-UE that operates on a non-NTN serving cell, or a HD-UE that operates on an NTN serving cell and does not indicate , does not expect to detect a DCI format scheduling a reception in a set of symbols and detect a DCI format scheduling a transmission in any symbol from the set of symbols. A HD-UE that operates on an NTN serving cell in the RRC_CONNECTED state, indicates , is scheduled to receive a PDSCH or CSI-RS in a set of symbols based on an indication by a first DCI format, and is scheduled to transmit a PUSCH, PUCCH, or PRACH that overlap with any symbol from the set of symbols based on an indication by a second DCI format, determines - to either receive the PDSCH or the CSI-RS or transmit the PRACH based on the HD-UE implementation; - to either receive the PDSCH or transmit the PUSCH or PUCCH based on the HD-UE implementation, if the first DCI format is provided by a PDCCH the HD-UE received according to a Type0/0A/1/2-PDCCH CSS set; - to receive the PDSCH or the CSI-RS if the first DCI format is not provided by a PDCCH the HD-UE received according to a Type0/0A/1/2-PDCCH CSS set, and the HD-UE is not provided ntn-RedcapPrioritizeUL-Dynamic, and the transmission of the PUCCH or the PUSCH would not start before after the last symbol of the PDCCH reception providing the first DCI format; - to transmit the PUSCH or PUCCH, if the first DCI format is not provided by a PDCCH the HD-UE received according to a Type0/0A/1/2-PDCCH CSS set, and - the HD-UE is provided ntn-RedcapPrioritizeUL-Dynamic, or - the HD-UE is not provided ntn-RedcapPrioritizeUL-Dynamic and the transmission of the PUCCH or the PUSCH would start before after the last symbol of the PDCCH reception providing the first DCI format. A HD-UE that operates on an NTN serving cell in the RRC_CONNECTED state, indicates , is scheduled to receive a PDSCH or CSI-RS based on an indication by a first DCI format, and is scheduled to transmit an SRS based on an indication by a second DCI format and the transmission of the SRS in a set of symbols overlaps with the PDSCH reception or CSI-RS reception, determines - to either receive the PDSCH or transmit the SRS based on the HD-UE implementation, if the first DCI format is provided by a PDCCH the HD-UE received according to a Type0/0A/1/2-PDCCH CSS set; - to receive the PDSCH or the CSI-RS if the first DCI format is not provided by a PDCCH the HD-UE received according to a Type0/0A/1/2-PDCCH CSS set, and the HD-UE is not provided ntn-RedcapPrioritizeUL-Dynamic, and the first symbol from the set of symbols is not before after the last symbol of the PDCCH reception providing the first DCI format; - to transmit the SRS if the first DCI format is not provided by a PDCCH the HD-UE received according to a Type0/0A/1/2-PDCCH CSS set, and - the HD-UE is provided ntn-RedcapPrioritizeUL-Dynamic, or - the HD-UE is not provided ntn-RedcapPrioritizeUL-Dynamic and any symbol from the set of symbols is before after the last symbol of the PDCCH reception providing the first DCI format When a PDCCH reception by a HD-UE includes two PDCCH candidates from corresponding search space sets, as described in clause 10.1, the end of the PDCCH reception is the end of the PDCCH candidate that ends later. If a HD-UE is configured by higher layers to receive a PDCCH, or PDSCH, or CSI-RS, or DL PRS in a set of symbols, the HD-UE receives the PDCCH, or PDSCH, or CSI-RS, or DL PRS if the HD-UE does not detect a DCI format that indicates to the HD-UE to transmit a PUSCH, or PUCCH, or PRACH, or SRS in at least one symbol of the set of symbols; otherwise, the HD-UE does not receive the PDCCH, or PDSCH, or CSI-RS, or DL PRS in the set of symbols. If a HD-UE is configured by higher layers to transmit SRS, or PUCCH, or PUSCH in a set of symbols and the HD-UE detects a DCI format indicating to the HD-UE to receive CSI-RS or PDSCH in a subset of symbols from the set of symbols, then - the HD-UE does not expect to cancel the transmission of the PUCCH or PUSCH in the set of symbols if the first symbol in the set occurs within relative to a last symbol of a PDCCH reception where the HD-UE detects the DCI format; otherwise, the HD-UE cancels the PUCCH, or the PUSCH, or an actual repetition of the PUSCH [6, TS 38.214], determined from clauses 9 and 9.2.5 or clause 6.1 of [6, TS 38.214]. - the HD-UE does not expect to cancel the transmission of SRS in symbols from the subset of symbols that occur within relative to a last symbol of a PDCCH reception where the HD-UE detects the DCI format. The HD-UE cancels the SRS transmission in remaining symbols from the subset of symbols. is the PUSCH preparation time for HD-UE processing capability 1 [6, TS 38.214] assuming and corresponds to the smallest SCS configuration between the SCS configuration of the PDCCH carrying the DCI format and the SCS configuration of the SRS, PUCCH, PUSCH. A HD-UE operating on a non-NTN serving cell, or a HD-UE that operates on an NTN serving cell and does not indicate , does not expect to receive both dedicated higher layer parameters configuring transmission in a set of symbols and dedicated higher layer parameters configuring reception in the set of symbols. The HD-UE does not expect to receive both a Type-0/0A/0B/1/2-PDCCH CSS set configuration for PDCCH reception in a set of symbols and dedicated higher layer parameters configuring transmission in the set of symbols, except a Type-2-PDCCH CSS set configuration for PDCCH reception in a set of symbols and dedicated higher layer parameters configuring configured-grant based PUSCH transmission as described in clause 19.1 in the set of symbols for which case the HD-UE follows the procedure as in clause 5.1B.2.6 of [10, TS 38.133]. The HD-UE expects to be configured with a Type-2-PDCCH CSS set configuration for PDCCH reception such that there is at least one paging occasion that does not overlap with configured-grant based PUSCH transmission as described in clause 19.1 per SI modification period. A HD-UE that operates on an NTN serving cell in the RRC_CONNECTED state, indicates , would receive a PDCCH or would receive a PDSCH or CSI-RS or PRS based on a configuration by higher layers in a set of symbols, and would transmit a PUSCH, PUCCH, or SRS based on a configuration by higher layers that overlap with any symbol from the set of symbols, determines - to either receive the PDCCH or transmit the PUSCH/PUCCH/SRS based on the HD-UE implementation, if the PDCCH reception is according to a Type0/0A/1/2-PDCCH CSS set - to receive the PDCCH, if the PDCCH reception is not according to a Type0/0A/1/2-PDCCH CSS set, or the PDSCH, or the CSI-RS, or the PRS if the HD-UE is not provided ntn-RedcapPrioritizeUL-Semistatic - to transmit the PUSCH, the PUCCH, or the SRS, if the PDCCH reception is not according to a Type0/0A/1/2-PDCCH CSS set, and the HD-UE is provided ntn-RedcapPrioritizeUL-Semistatic A HD-UE that operates on an NTN serving cell in the RRC_INACTIVE state, would receive a PDCCH in a set of symbols and would transmit a PUSCH or SRS that overlap with any symbol from the set of symbols, determines to either receive the PDCCH or transmit the PUSCH or SRS based on the HD-UE implementation. < Unchanged text omitted > | 17.2 Half-Duplex UE in paired spectrum A half-duplex UE (HD-UE) in paired spectrum is not capable of simultaneous transmissions and receptions on a serving cell with paired spectrum. This clause is applicable for communication of a HD-UE on a serving cell with paired spectrum. Procedures for a HD-UE are same as described for a UE in all other clauses of this document unless stated otherwise. A HD-UE that operates on a non-NTN serving cell, or a HD-UE that operates on an NTN serving cell and does not indicate , does not expect to detect a DCI format scheduling a reception in a set of symbols and detect a DCI format scheduling a transmission in any symbol from the set of symbols. A HD-UE that operates on an NTN serving cell in the RRC_CONNECTED state, indicates , is scheduled to receive a PDSCH or CSI-RS in a set of symbols based on an indication by a first DCI format, and is scheduled to transmit a PUSCH, PUCCH, or PRACH that overlap with any symbol from the set of symbols based on an indication by a second DCI format, determines - to either receive the PDSCH or the CSI-RS or transmit the PRACH based on the HD-UE implementation; - to either receive the PDSCH or transmit the PUSCH or PUCCH based on the HD-UE implementation, if the first DCI format is provided by a PDCCH the HD-UE received according to a Type0/0A/1/2-PDCCH CSS set; - to receive the PDSCH or the CSI-RS if the first DCI format is not provided by a PDCCH the HD-UE received according to a Type0/0A/1/2-PDCCH CSS set, and the HD-UE is not provided ntn-RedcapPrioritizeUL-Dynamic, and the transmission of the PUCCH or the PUSCH would not start before after the last symbol of the PDCCH reception providing the first DCI format; - to transmit the PUSCH or PUCCH, if the first DCI format is not provided by a PDCCH the HD-UE received according to a Type0/0A/1/2-PDCCH CSS set, and - the HD-UE is provided ntn-RedcapPrioritizeUL-Dynamic, or - the HD-UE is not provided ntn-RedcapPrioritizeUL-Dynamic and the transmission of the PUCCH or the PUSCH would start before after the last symbol of the PDCCH reception providing the first DCI format. A HD-UE that operates on an NTN serving cell in the RRC_CONNECTED state, indicates , is scheduled to receive a PDSCH or CSI-RS based on an indication by a first DCI format, and is scheduled to transmit an SRS based on an indication by a second DCI format and the transmission of the SRS in a set of symbols overlaps with the PDSCH reception or CSI-RS reception, determines - to either receive the PDSCH or transmit the SRS based on the HD-UE implementation, if the first DCI format is provided by a PDCCH the HD-UE received according to a Type0/0A/1/2-PDCCH CSS set; - to receive the PDSCH or the CSI-RS if the first DCI format is not provided by a PDCCH the HD-UE received according to a Type0/0A/1/2-PDCCH CSS set, and the HD-UE is not provided ntn-RedcapPrioritizeUL-Dynamic, and the first symbol from the set of symbols is not before after the last symbol of the PDCCH reception providing the first DCI format; - to transmit the SRS if the first DCI format is not provided by a PDCCH the HD-UE received according to a Type0/0A/1/2-PDCCH CSS set, and - the HD-UE is provided ntn-RedcapPrioritizeUL-Dynamic, or - the HD-UE is not provided ntn-RedcapPrioritizeUL-Dynamic and any symbol from the set of symbols is before after the last symbol of the PDCCH reception providing the first DCI format When a PDCCH reception by a HD-UE includes two PDCCH candidates from corresponding search space sets, as described in clause 10.1, the end of the PDCCH reception is the end of the PDCCH candidate that ends later. If a HD-UE is configured by higher layers to receive a PDCCH, or PDSCH, or CSI-RS, or DL PRS in a set of symbols, the HD-UE receives the PDCCH, or PDSCH, or CSI-RS, or DL PRS if the HD-UE does not detect a DCI format that indicates to the HD-UE to transmit a PUSCH, or PUCCH, or PRACH, or SRS in at least one symbol of the set of symbols; otherwise, the HD-UE does not receive the PDCCH, or PDSCH, or CSI-RS, or DL PRS in the set of symbols. If a HD-UE is configured by higher layers to transmit SRS, or PUCCH, or PUSCH in a set of symbols and the HD-UE detects a DCI format indicating to the HD-UE to receive CSI-RS or PDSCH in a subset of symbols from the set of symbols, then - the HD-UE does not expect to cancel the transmission of the PUCCH or PUSCH in the set of symbols if the first symbol in the set occurs within relative to a last symbol of a PDCCH reception where the HD-UE detects the DCI format; otherwise, the HD-UE cancels the PUCCH, or the PUSCH, or an actual repetition of the PUSCH [6, TS 38.214], determined from clauses 9 and 9.2.5 or clause 6.1 of [6, TS 38.214]. - the HD-UE does not expect to cancel the transmission of SRS in symbols from the subset of symbols that occur within relative to a last symbol of a PDCCH reception where the HD-UE detects the DCI format. The HD-UE cancels the SRS transmission in remaining symbols from the subset of symbols. is the PUSCH preparation time for HD-UE processing capability 1 [6, TS 38.214] assuming and corresponds to the smallest SCS configuration between the SCS configuration of the PDCCH carrying the DCI format and the SCS configuration of the SRS, PUCCH, PUSCH. A HD-UE operating on a non-NTN serving cell, or a HD-UE that operates on an NTN serving cell and does not indicate , does not expect to receive both dedicated higher layer parameters configuring transmission in a set of symbols and dedicated higher layer parameters configuring reception in the set of symbols. The HD-UE does not expect to receive both a Type-0/0A/0B/1/2-PDCCH CSS set configuration for PDCCH reception in a set of symbols and dedicated higher layer parameters configuring transmission in the set of symbols, except a Type-2-PDCCH CSS set configuration for PDCCH reception in a set of symbols and dedicated higher layer parameters configuring configured-grant based PUSCH transmission as described in clause 19.1 in the set of symbols for which case the HD-UE follows the procedure as in clause 5.1B.2.6 of [10, TS 38.133]. The HD-UE expects to be configured with a Type-2-PDCCH CSS set configuration for PDCCH reception such that there is at least one paging occasion that does not overlap with configured-grant based PUSCH transmission as described in clause 19.1 per SI modification period. A HD-UE that operates on an NTN serving cell in the RRC_CONNECTED state, indicates , would receive a PDCCH or would receive a PDSCH or CSI-RS or PRS based on a configuration by higher layers in a set of symbols, and would transmit a PUSCH, PUCCH, or SRS based on a configuration by higher layers that overlap with any symbol from the set of symbols, determines - to either receive the PDCCH or transmit the PUSCH/PUCCH/SRS based on the HD-UE implementation, if the PDCCH reception is according to a Type0/0A/1/2-PDCCH CSS set - to receive the PDCCH, if the PDCCH reception is not according to a Type0/0A/1/2-PDCCH CSS set, or the PDSCH, or the CSI-RS, or the PRS if the HD-UE is not provided ntn-RedcapPrioritizeUL-Semistatic - to transmit the PUSCH, the PUCCH, or the SRS, if the PDCCH reception is not according to a Type0/0A/1/2-PDCCH CSS set, and the HD-UE is provided ntn-RedcapPrioritizeUL-Semistatic A HD-UE that operates on an NTN serving cell in the RRC_INACTIVE state, would receive a PDCCH in a set of symbols and would transmit a PUSCH or SRS that overlap with any symbol from the set of symbols, determines to either receive the PDCCH or transmit the PUSCH or SRS based on the HD-UE implementation. < Unchanged text omitted > |

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx)

**Agreement** · `8.8` Maintenance on others · `RAN1#124:8.8:003` · 후보 · 관련 주제: Beam management, CSI 보고/codebook, CSI-RS

> Adopt the following TP to TS38.214 Section 5.2.1.5.2
> | Reason for change The application timeline of activation/deactivation of SP CSI-RS/CSI-IM resources based on the newly specified MAC CE for LTM, SP CSI-RS/CSI-IM Resource Set Activation/Deactivation for Candidate Cell MAC CE, is missing from TS 38.214. Summary of change References to section 6.1.3.12a of TS 38.214 in clause 5.2.1.5.2 of TS 38.214 have been added. Also, a typo was corrected from the timeline description related to the activation command (“selection” is changed to “activation”). Consequences if not approved Ambiguity for the application timeline of activation/deactivation of SP CSI-RS/CSI-IM resources based on the newly specified MAC CE for LTM, SP CSI-RS/CSI-IM Resource Set Activation/Deactivation for Candidate Cell MAC CE. 5.2.1.5.2 Semi-persistent CSI/Semi-persistent CSI-RS <omitted Text> For a UE configured with CSI resource setting(s) where the higher layer parameter resourceType set to 'semiPersistent'. - when a UE receives an activation command, as described in clause 6.1.3.12 or 6.1.3.12a of [10, TS 38.321], for CSI-RS resource set(s) for channel measurement, CSI-IM/NZP CSI-RS resource set(s) for interference measurement and CLI-RSSI/SRS-RSRP for cross-link interference measurement associated with configured CSI resource setting(s), and when the UE would transmit a PUCCH with HARQ-ACK information in slot n corresponding to the PDSCH carrying the selection activation command, the corresponding actions in [10, TS 38.321] and the UE assumptions (including QCL assumptions provided by a list of reference to TCI-State's, one per activated resource) on CSI-RS/CSI-IM/CLI-RSSI/SRS-RSRP transmission corresponding to the configured CSI-RS/CSI-IM/CLI-RSSI/SRS-RSRP resource configuration(s) shall be applied starting from the first slot that is after slot where  is the SCS configuration for the PUCCH and is the subcarrier spacing configuration for with a value of 0 for frequency range 1 and for FR2-NTN, and is provided by K-Mac or if K-Mac is not provided. If a TCI-State referred to in the list is configured with a reference to an RS configured with qcl-Type set to 'typeD', that RS can be an SS/PBCH block, periodic or semi-persistent CSI-RS located in same or different CC/DL BWP. If the UE is configured with CLI-RSSI-MeasurementResourceSet or SRS-RSRP-MesaurementResourceSet without TCI-State configuration and unifiedTCI-StateType is not configured, the UE shall assume that the activated CLI-RSSI or SRS-RSRP measurement resources are QCL 'typeD' to one of the latest received PDSCH and the latest monitored CORESET. If the UE is configured with CLI-RSSI-MeasurementResourceSet or SRS-RSRP-MesaurementResourceSet without TCI-State configuration and unifiedTCI-StateType is configured, the UE shall assume that the activated CLI-RSSI or SRS-RSRP measurement resources are QCL 'typeD' according to the indicated DL only/joint TCI state. - when a UE receives a deactivation command, as described in clause 6.1.3.12 or 6.1.3.12a of [10, TS 38.321], for activated CSI-RS/CSI-IM/CLI-RSSI/SRS-RSRP resource set(s) associated with configured CSI resource setting(s), and when the UE would transmit a PUCCH with HARQ-ACK information in slot n corresponding to the PDSCH carrying the deactivation command, the corresponding actions in [10, TS 38.321] and UE assumption on cessation of CSI-RS/CSI-IM/CLI-RSSI/SRS-RSRP transmission corresponding to the deactivated CSI-RS/CSI-IM/CLI-RSSI/SRS-RSRP resource set(s) shall apply starting from the first slot that is after slot where  is the SCS configuration for the PUCCH and is the subcarrier spacing configuration for with a value of 0 for frequency range 1 and for FR2-NTN, and is provided by K-Mac or if K-Mac is not provided. <omitted Text> |
> Final CR is endorsed in R1-2601631

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601559](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601559.zip) · `[124-R19-others]`

**Agreement** · `8.8` Maintenance on others · `RAN1#124:8.8:006` · 후보 · 관련 주제: Beam management, CSI-RS

> Adopt the following TP to TS38.214 Section 5.1.5
> ---
> Reason for change
> In the current specification, QCL assumption for reception or transmission of DL or UL channels/signals has not been defined yet after RACH-based or RACH-less CLTM is triggered and before an indicated TCI state is applied for the serving cell.
> Summary of change
> Clarify UE behavior on how to determine QCL assumption for reception or transmission of DL or UL channels/signals after RACH-based or RACH-less CLTM is performed, especially for the following cases:
> - Case-1: After a UE receives an initial higher layer configuration of dl-OrJointTCI-StateList where more than one TCI-State can be used as an indicated TCI state and before application of an indicated TCI state from the configured TCI states.
> - Case-2: After a UE receives an initial higher layer configuration of dl-OrJointTCI-StateList where more than one TCI-State can be used as an indicated TCI state or an initial higher layer configuration of ul-TCI-StateList where more than one TCI-UL-State can be used as an indicated TCI state and before application of an indicated TCI state from the configured TCI states.
> - Case-3: If tci-PresentInDCI is set to 'enabled' or tci-PresentDCI-1-2 is configured for the CORESET scheduling the PDSCH, and the time offset between the reception of the DL DCI and the corresponding PDSCH is equal to or greater than timeDurationForQCL if applicable, after a UE receives an initial higher layer configuration of TCI states and before reception of the activation command.
> Consequences if not approved
> It is unclear for UE how to determined QCL assumption for reception or transmission of DL or UL channels/signals after RACH-based or RACH-less CLTM is triggered and before an indicated TCI state is applied for the serving cell.
> | 5.1.5 Antenna ports quasi co-location *** Unchanged parts are omitted *** After a UE receives an initial higher layer configuration of dl-OrJointTCI-StateList where more than one TCI-State can be used as an indicated TCI state and before application of an indicated TCI state from the configured TCI states: - The UE assumes that DM-RS of PDSCH and DM-RS of PDCCH that are not received during the RACH procedure, and the CSI-RS applying the indicated TCI state are quasi co-located with the reference signal(s) in the CandidateTCI-State indicated in the LTM Cell Switch Command MAC CE [10, 38.321] if applicable - he UE assumes that DM-RS of PDSCH and DM-RS of PDCCH and the CSI-RS applying the indicated TCI state are quasi co-located with the SS/PBCH block the UE identified during the initial access procedure |
> | After a UE receives an initial higher layer configuration of dl-OrJointTCI-StateList where more than one TCI-State can be used as an indicated TCI state or an initial higher layer configuration of ul-TCI-StateList where more than one TCI-UL-State can be used as an indicated TCI state and before application of an indicated TCI state from the configured TCI states: - The UE determines the UL TX spatial filter, if applicable, for dynamic-grant based PUSCH that is not transmitted during the RACH procedure and configured-grant based PUSCH and PUCCH that are not transmitted during the RACH procedure, and for SRS applying the indicated TCI state, from the CandidateTCI-State or CandidateTCI-UL-State indicated in the LTM Cell Switch Command MAC CE [10, 38.321] if applicable - he UE assumes that the UL TX spatial filter, if applicable, for dynamic-grant and configured-grant based PUSCH and PUCCH, and for SRS applying the indicated TCI state, is the same as that for a PUSCH transmission scheduled by a RAR UL grant or a MsgA PUSCH transmission during the initial access procedure *** Unchanged parts are omitted *** When the UE would transmit a PUCCH with HARQ-ACK information in slot n corresponding to the PDSCH carrying the activation command, the indicated mapping between TCI states and codepoints of the DCI field 'Transmission Configuration Indication' should be applied starting from the first slot that is after slot where m is the SCS configuration for the PUCCH and is the subcarrier spacing configuration for with a value of 0 for frequency range 1 and for FR2-NTN, and is provided by K-Mac or if K-Mac is not provided. If tci-PresentInDCI is set to 'enabled' or tci-PresentDCI-1-2 is configured for the CORESET scheduling the PDSCH, and the time offset between the reception of the DL DCI and the corresponding PDSCH is equal to or greater than timeDurationForQCL if applicable, after a UE receives an initial higher layer configuration of TCI states and before reception of the activation command, - the UE assumes that DM-RS of ports of PDSCH of a serving cell are quasi co-located with the reference signal(s) in the CandidateTCI-State indicated in the LTM Cell Switch Command MAC CE [10, 38.321], except during RACH procedure for RACH-based LTM, if applicable - the UE may assume that the DM-RS ports of PDSCH of a serving cell are quasi co-located with the SS/PBCH block determined in the initial access procedure with respect to qcl-Type set to 'typeA', and when applicable, also with respect to qcl-Type set to 'typeD'. *** Unchanged parts are omitted *** |
> Final CR is endorsed in R1-2601633

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601559](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601559.zip) · `[124-R19-others]`

**Agreement** · `9.3.2.3` Other procedures · `RAN1#124:9.3.2.3:010` · 후보

> On the measurement aspects (e.g., metric) for A-IoT device localization, capture the following observations in TR 38.769.
> ---
> Regarding the D2R RSRP-like measurement for A-IoT device localization, following observations were provided during the study.
> - [FUTUREWEI] Use NR measurements (SL PRS-RSRP and UL-SRS-RSRP) as a reference. For D2R RSRP-like measurement, the reader can use the D2R preamble for the reference signal and measure the power between the end of R2D transmission and start of the D2R transmission to estimate the noise and interference. To estimate proximity, a reader can also consider the effects of propagation delay based on when the D2R transmission is received.
> - [Huawei] D2R RSRP-like measurement is defined as the time domain linear average over the power contributions (in [W]) of preamble and midamble signals within the signal transmission bandwidth during the D2R transmission.
> - [Ericsson] D2R-amble-RSRP is defined as the linear average over the power contributions (in [W]) of chips that carry the D2R preamble over PDRCH. A secondary measurement can be defined as the linear averaging over the power contributions of chips that carry D2R preamble and D2R midambles over PDRCH.
> - [CATT] The definition of RSRP-like and AOA measurement quantity can refer to TR 38.215(NR; Physical layer measurements).
> - [Xiaomi] The RSRP-like definition in A-IoT is the linear average of the received power in occupied chips and over the frequency resources that carry the measured signal. For example, if D2R is applied with OOK modulation, referring to the definition of LP-RSRP where measured signal is also an OOK waveform, RSRP-like definition in A-IoT is the linear average of the received power in OOK ON chips over the frequency resources that carry the measured signal.
> - [Qualcomm] At reader side, how to measure the RSRP may be up to reader implementation. However, it may require the averaging of the D2R measurements based on D2R signals/channels with sufficient time duration and stable transmit power from device side.
> - [NEC] D2R RSRP based measurement and positioning is feasible. R20 AIoT should support D2R RSRP based measurement.
> ---

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2600550](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2600550.zip)

**Agreement** · `10.4` Energy efficiency · `RAN1#124:10.4:016` · 후보

> Adopt the following UL scaling for 6GR UE power consumption model:
> |  | Scaling | Comment |
> | Short PUCCH | Short PUCCH power = 0.3 x uplink power (Assume short PUCCH of 1-symbol) | Applicable for FR1 (including around 7GHz) and FR2 (including 24.25 GHz – 52.6 GHz). |
> | SRS | SRS power = 0.3 x uplink power (Assume SRS of 1-symbol) | Applicable for FR1 (including around 7GHz) and FR2 (including 24.25 GHz – 52.6 GHz). |
> - FFS: Scaling for different symbol numbers

남은 FFS 1건

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · `[124-R20-6GR-Energy efficiency]`

### RAN1#123 — 13건

**Agreement** · `7` Pre-Rel-19 NR Maintenance · `RAN1#123:7:002` · 후보 · 관련 주제: CSI 보고/codebook

> The draft CR in R1-2508507 for TS38.214, Rel-18 is endorsed with the following changed highlighted in cyan.
> The final CRs for TS38.214 for Rel-18 and Rel-19 (mirror) in R1-2509563 and R1-2509564, respectively, are endorsed.
> ================================================
> 6.2.3.1 	UE PT-RS transmission procedure when transform precoding is not enabled
> <Unchanged parts are omitted>
> The maximum number of configured PT-RS ports is given by the higher layer parameter maxNrofPorts in PTRS-UplinkConfig. The UE is not expected to be configured with a larger number of UL PT-RS ports than it has reported need for.
> If a UE has reported the capability of supporting full-coherent UL transmission with 2 or 4 antenna ports or the capability of codebook1-8TxPUSCH-r18 with 8 antenna ports, the UE shall expect maxNrofPorts in PTRS-UplinkConfig to be configured as one if UL PT-RS is configured. If a UE has reported the capability of supporting full-coherent UL transmission and when the higher layer parameter multipanelSchemeSDM is configured, subject to UE capability, the UE can be configured with maxNrofPorts-SDM in PTRS-UplinkConfig set to n2, where at most one PT-RS port is associated with each SRS resource set with higher layer parameter usage set to 'codebook'/'nonCodebook'.
> For codebook or non-codebook based UL transmission, the association between UL PT-RS port(s) and DM-RS port(s) is signalled by PTRS-DMRS association field(s) in DCI format 0_1, 0_2 and 0_3. For a PUSCH corresponding to a configured grant Type 1 transmission, the UE may assume the association between UL PT-RS port(s) and DM-RS port(s) defined by value 0 in Table 7.3.1.1.2-25, or value "00" in Table 7.3.1.1.1.2-26 or value "00" in Table 7.3.1.1.1.2-25a described in Clause 7.3.1 of [5, TS 38.212].
> <Unchanged parts are omitted>
> ================================================

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509537](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509537.zip)

**Agreement** · `8.3` Maintenance on Evolution of NR duplex operation: Sub-band full duplex (SBFD) · `RAN1#123:8.3:007` · 후보 · 관련 주제: CSI 보고/codebook

> Adopt the following TP to section 5.2.2.6, TS 38.214
> | 5.2.2.6 SRS-RSRP measurement resource <Unchanged parts omitted> |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · `[123-R19-SBFD]`

**Agreement** · `8.3` Maintenance on Evolution of NR duplex operation: Sub-band full duplex (SBFD) · `RAN1#123:8.3:010` · 후보

> Adopt the following TP in principle to Clause 7, TS 38.213.
> | 7 Uplink Power control ---------------------------Other parts are omitted ------------------------------- A PUSCH/PUCCH/SRS/PRACH transmission occasion is defined by a slot index within a frame with system frame number , a first symbol within the slot, and a number of consecutive symbols . For a PUSCH transmission with repetition Type B, a PUSCH transmission occasion is an actual repetition if p0AlphaSetforPUSCH-SBFD is provided or a nominal repetition otherwise [6, TS 38.214]. ---------------------------Other parts are omitted ------------------------------- |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · `[123-R19-SBFD]`

**Agreement** · `8.3` Maintenance on Evolution of NR duplex operation: Sub-band full duplex (SBFD) · `RAN1#123:8.3:013` · 후보

> Measurement resource for method#1 (L1-CLI-RSSI measurement in DL subband) and method#2 (L1-SRS-RSRP measurement in UL subband) cannot be configured in the same OFDM symbol for SBFD-aware UEs.

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · `[123-R19-SBFD]`

**Agreement** · `8.8` Maintenance on others · `RAN1#123:8.8:001` · 후보

> Adopt the following TP to TS38.213 Clause 24 for alignment.
> | <Unchanged parts are omitted> 24 Downlink carrier aggregation via switching A UE that can switch operation between a PCell, that includes a DL carrier and a paired UL carrier, and an SCell, that includes a DL carrier without a paired UL carrier, can be provided by LBCA-SwitchingPattern switchingPattern-r19 a bitmap of slots indicating a switching pattern between the PCell and the SCell when the SCell is activated. The switching pattern repeats continuously. The UE can either transmit/receive on the PCell in a slot or receive on the SCell in the slot. A bit value of ‘0’ for a first slot in the bitmap indicates that the UE can transmit/receive on the PCell in the first slot, and a bit value of ‘1’ for a second slot in the bitmap indicates that the UE can receive on the SCell in the second slot. The first slot of the bitmap is same as the first slot of a system frame with SFN 0 on the PCell. The SCS for all configured DL BWPs or UL BWPs on both the PCell and the SCell is 15 kHz and the periodicity of the switching pattern is 40 slots. When the UE is provided LBCA-SwitchingPattern LowBandCA-Switching-r19, the UE is provided - a first duration, by LBCA-SwitchingGap-Duration-PCelltoSCell gapDurationPCelltoSCell-r19, ending at the end of the last slot from a number of consecutive slots with bit value ‘0’, for the UE to switch operation from the PCell to the SCell over the first duration, and - a second duration, by LBCA-SwitchingGap-SCelltoPCell gapDurationSCelltoPCell-r19, ending at the end of the last slot from a number of consecutive slots with bit value ‘1’, for the UE to switch operation from the SCell to the PCell over the second duration The UE does not transmit a PUSCH, or PUCCH, or SRS, or PRACH configured by higher layers in a set of symbols when the set of symbols includes at least one symbol that is in the first duration or is in a slot with bit value ‘1’, assuming . <Unchanged parts are omitted> |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509088](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509088.zip)

**Agreement** · `8.8` Maintenance on others · `RAN1#123:8.8:002` · 후보 · 관련 주제: CSI-RS

> For Rel-19 low NR band carrier aggregation via switching, the collision handling for higher-layer configured transmission and reception is per repetition.
> - Adopt the following TP to TS38.213 Clause 24
> ---
> Reason for change: When the UE is provided LBCA-SwitchingPattern, it is not clear that collision handling for higher-layer configured transmission and reception is per repetition (slot) or per channel(all slots), if overlapping with at least one unavailable symbol of a slot based on the switching pattern.
> Summary of change: The collision handling for higher-layer configured transmission and reception is per repetition if overlapping with at least one unavailable symbol based on the switching pattern.
> Consequences if not approved: For low NR band carrier aggregation via switching, it is not clear the collision handling for higher-layer configured transmission and reception is per repetition or per channel.
> | 24 Downlink carrier aggregation via switching <Unchanged parts are omitted> When the UE is provided LBCA-SwitchingPattern, the UE is provided - a first duration, by LBCA-SwitchingGap-Duration-PCelltoSCell, ending at the end of the last slot from a number of consecutive slots with bit value ‘0’, for the UE to switch operation from the PCell to the SCell over the first duration, and - a second duration, by LBCA-SwitchingGap-SCelltoPCell, ending at the end of the last slot from a number of consecutive slots with bit value ‘1’, for the UE to switch operation from the SCell to the PCell over the second duration The UE does not transmit a PUSCH, or PUCCH, or SRS, or PRACH configured by higher layers in a set of symbols of a slot when the set of symbols of the slot includes at least one symbol that is in the first duration or is in a slot with bit value ‘1’, assuming . The UE does not receive a SS/PBCH block, PDSCH, or PDCCH, or CSI-RS, or PRS configured by higher layers in a set of symbols of a slot on the PCell when the set of symbols of the slot includes at least one symbol that is in the first duration or is in a slot with bit value ‘1’. The UE does not receive a SS/PBCH block, PDSCH, or PDCCH, or CSI-RS, or PRS configured by higher layers in a set of symbols of a slot on the SCell when the set of symbols of the slot includes at least one symbol that is in the second duration or is in a slot with bit value ‘0’. <Unchanged parts are omitted> |
> ---

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509088](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509088.zip)

**Agreement** · `8.8` Maintenance on others · `RAN1#123:8.8:005` · 후보 · 관련 주제: Beam management

> Endorse the following TP to TS38.213 Section 7
> | Reason for change: The current specification does not define how uplink power control parameters are derived when the UE selects a candidate TCI state for C-LTM. Summary of change: Update TS 38.213 to clarify that uplink power control shall use the pathloss RS, p0, and α associated with the candidate TCI state indicated by MAC CE or selected by the UE for C-LTM. Consequences if not approved: UEs may apply inconsistent uplink power control after C-LTM, causing misaligned pathloss estimation and degraded mobility performance. |
> | ==================================unchanged omitted=================================== 7 Uplink Power control Uplink power control determines a power for PUSCH, PUCCH, SRS, and PRACH transmissions. A UE does not expect to simultaneously maintain more than four pathloss estimates per serving cell for all PUSCH/PUCCH/SRS transmissions as described in clauses 7.1.1, 7.2.1, and 7.3.1, except for SRS transmissions configured by SRS-PosResourceSet as described in clause 7.3.1. If the UE is provided a number of RS resources for pathloss estimation for PUSCH/PUCCH/SRS transmissions that is larger than 4, the UE maintains for pathloss estimation RS resources corresponding to RS resource indexes as described in clauses 7.1.1, 7.2.1, and 7.3.1. If an RS resource updated by MAC CE, as described in clauses 7.1.1, 7.2.1 and 7.3.1, is one from the RS resources the UE maintains for pathloss estimation for PUSCH/PUCCH/SRS transmissions, the UE applies the pathloss estimation based on the RS resources starting from the first slot that is after slot where is the slot where the UE would transmit a PUCCH or PUSCH with HARQ-ACK information for the PDSCH providing the MAC CE, is the SCS configuration for the PUCCH or PUSCH, respectively, that is determined in the slot when the MAC CE command is applied and is a number of slots for SCS configuration provided by kmac or if kmac is not provided. A PUSCH/PUCCH/SRS/PRACH transmission occasion is defined by a slot index within a frame with system frame number , a first symbol within the slot, and a number of consecutive symbols . For a PUSCH transmission with repetition Type B, a PUSCH transmission occasion is a nominal repetition [6, TS 38.214]. In the remaining of this clause, if a UE is provided TCI-State in dl-OrJointTCI-StateList or TCI-UL-State or CandidateTCI-State or CandidateTCI-UL-State indicated in the LTM Cell Switch Command MAC CE, and for each indicated one or two TCI-State or TCI-UL-State or CandidateTCI-State or CandidateTCI-UL-State of a PUSCH, PUCCH, or SRS transmission occasion as described in [6, TS 38.214] - in clauses 7.1.1, 7.2.1, and 7.3.1, the RS index for obtaining the downlink pathloss estimate for PUSCH, PUCCH, and SRS transmission is provided by pathlossReferenceRS-Id-r17 associated with or included in the indicated TCI-State or TCI-UL-State except for SRS transmission that is not provided followUnifiedTCI-StateSRS, or by pathlossReferenceRS-Id included in CandidateTCI-State or CandidateTCI-UL-State indicated in the LTM Cell Switch Command MAC CE - in clause 7.1.1, if p0AlphaSetforPUSCH is provided, or if p0AlphaSetforPUSCH-SBFD is provided and for a PUSCH transmission in SBFD symbols as described in clause 11.1, the values of , , and the PUSCH power control adjustment state are provided by p0AlphaSetforPUSCH or by p0AlphaSetforPUSCH-SBFD, respectively, associated with the indicated TCI-State or TCI-UL-State, or by p0AlphaSetforPUSCH associated with the CandidateTCI-State or CandidateTCI-UL-State indicated in the LTM Cell Switch Command MAC CE - in clause 7.2.1, if p0AlphaSetforPUCCH is provided, or if p0AlphaSetforPUCCH-SBFD is provided and for a PUCCH transmission in SBFD symbols, the values of and the PUCCH power control adjustment state are provided by p0AlphaSetforPUCCH or by p0AlphaSetforPUCCH-SBFD, respectively, associated with the indicated TCI-State or TCI-UL-State, or by p0AlphaSetforPUCCH associated with the CandidateTCI-State or CandidateTCI-UL-State indicated in the LTM Cell Switch Command MAC CE - in clause 7.3.1, if p0AlphaSetforSRS is provided, - if followUnifiedTCI-StateSRS is provided for a SRS resource set, the values of , , and SRS power control adjustment state are provided by p0AlphaSetforSRS or, if p0AlphaSetforSRS-SBFD is provided and for an SRS transmission in SBFD symbols, by p0AlphaSetforSRS-SBFD, associated with the indicated TCI-State or TCI-UL-State, or by p0AlphaSetforSRS associated with the CandidateTCI-State or CandidateTCI-UL-State indicated in the LTM Cell Switch Command MAC CE - else, if followUnifiedTCI-StateSRS is not provided for a SRS resource set and for a SRS resource from the SRS resource set, the values of , , and SRS power control adjustment state are provided by p0AlphaSetforSRS or, if p0AlphaSetforSRS-SBFD is provided and for an SRS transmission in SBFD symbols, by p0AlphaSetforSRS-SBFD, associated with TCI-State or TCI-UL-State of an SRS resource with lowest SRS-ResourceId in the SRS resource set, a RS index for obtaining a pathloss estimate for the SRS transmission is provided by pathlossReferenceRS-Id-r17 associated with or included in the TCI-State or TCI-UL-State of an SRS resource with lowest SRS-ResourceId in the SRS resource set, and a value of a , when TCI-State or a TCI-UL-State includes pl-Offset, is provided by pl-Offset associated with TCI-State or TCI-UL-State of an SRS resource with lowest SRS-ResourceId in the SRS resource set is the sum of the component and a component p0 provided by SRS-ResourceSet corresponding to the SRS resource set. ==================================unchanged omitted=================================== 7.1.1 UE behaviour ==================================unchanged omitted=================================== - For a PUSCH (re)transmission configured by ConfiguredGrantConfig, , is provided by p0-NominalWithoutGrant, or if p0-NominalWithoutGrant is not provided. ==================================unchanged omitted=================================== - else, is provided by p0 obtained from p0-PUSCH-Alpha in ConfiguredGrantConfig that provides an index P0-PUSCH-AlphaSetId to a set of P0-PUSCH-AlphaSet, or by sdt-P0-PUSCH for a PUSCH (re)transmission as described in clause 19.1, or by rrc-P0-PUSCH for a PUSCH (re)transmission as described in clause 22.1, or by p0 of p0AlphaSetforPUSCH associated with the CandidateTCI-State or CandidateTCI-UL-State indicated in the LTM Cell Switch Command MAC CE for a configured grant Type-1 PUSCH (re)transmission as described in clause [21.1], for active UL BWP of carrier of serving cell ==================================unchanged omitted=================================== - For ==================================unchanged omitted=================================== - else is provided by alpha obtained from p0-PUSCH-Alpha in ConfiguredGrantConfig providing an index P0-PUSCH-AlphaSetId to a set of P0-PUSCH-AlphaSet, or by sdt-Alpha for a PUSCH (re)transmission as described in clause 19.1, or by rrc-Alpha for a PUSCH (re)transmission as described in clause 22.1, or by alpha of p0AlphaSetforPUSCH associated with the CandidateTCI-State or CandidateTCI-UL-State indicated in the LTM Cell Switch Command MAC CE for a configured grant Type-1 PUSCH (re)transmission as described in clause [21.1], for active UL BWP of carrier of serving cell ==================================unchanged omitted=================================== |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509086](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509086.zip)

**Agreement** · `8.8` Maintenance on others · `RAN1#123:8.8:010` · 후보 · 관련 주제: CSI 보고/codebook, CSI-RS

> Endorse the following TP to TS38.214 Section 5.2.2.5.1
> | 5.2.2.5.1 UE assumptions for CQI/PMI/RI calculation < Unchanged parts are omitted > - f a UE is configured with codebookType set to 'typeI-SinglePanel-r19' and with the higher layer parameter typeI-softScalingRank1-2-r19, for , and , if supported by UE capability, the UE can assume that the PDSCH signal for each layer mapped to a vector of group would have the same ratio of EPRE to CSI-RS EPRE for all CSI-RS resources, equal to times the powerControlOffset (in linear scale) of the respective CSI-RS resource, where and are described in Clause 5.2.2.2.1a; otherwise, the UE can assume that the PDSCH signals for layers would have the same ratio of EPRE to CSI-RS EPRE for all CSI-RS resources, equal to the powerControlOffset of the respective CSI-RS resource. - a UE configured with 48, 64 and 128 antenna ports, obtained by aggregating CSI-RS resources for channel measurement, and codebookType set to 'typeI-MultiPanel-r19', for CQI calculation, the UE should assume that PDSCH signals on antenna ports in the set , for layers, would result in signals equivalent to corresponding symbols transmitted on antenna ports of each of the CSI-RS resources, as given by where is the precoding matrix corresponding to the procedure described in Clause 5.2.2.2.2a. A UE can assume that the PDSCH signals for layers would have the same ratio of EPRE to CSI-RS EPRE for all CSI-RS resources , equal to the powerControlOffset of the respective CSI-RS resource. - a UE configured with one or more SRS resource sets with higher layer parameter usage set to 'antennaSwitching', with a total of or 8 ports across the resources intended for xT6R or xT8R, respectively, if the higher layer parameter reportQuantity in CSI-ReportConfig for which the CQI is reported is set to 'cri-RI-CQI' and the UE is configured with the higher layer parameter SRSPortGrouping-r19, the UE can assume that SRS port group 0 corresponds to codeword 0 and comprises the even ports, and that SRS port group 1 corresponds to codeword 1 and comprises the odd ports out of the total ports. The SRS ports are indexed in an ascending order according to SRS resource ID and port number within each SRS resource, for one SRS resource set, or according to SRS resource set ID, SRS resource ID in a set and port number within each SRS resource, for multiple aperiodic SRS resource sets. - that contains a list of sub-configurations provided by csi-ReportSubConfigToAddModList, - If a sub-configuration indicates a CSI-RS antenna port subset using the higher layer bitmap parameter portSubsetIndicator or portSubsetIndicator-r19, as described in clause 5.2.1.4.2, for CQI calculation, antenna ports corresponding to all bits with value of 1 in portSubsetIndicator are mapped to consecutive antenna ports starting at CSI-RS antenna port 3000 in increasing order of the bit position in portSubsetIndicator. The UE should assume that PDSCH signals on antenna ports in the set [1000,…, 1000+ν-1] for ν layers would result in signals equivalent to corresponding symbols transmitted on antenna ports [3000, …, 3000+P-1] T, as given by where P corresponds to the number of bits with value 1 in the bitmap portSubsetIndicator and T , and are as previously described in this Clause, and the corresponding PDSCH EPRE to CSI-RS EPRE is as previously defined in this Clause if the sub-configuration does not indicate a power offset powerOffset. - If a sub-configuration indicates a list of NZP CSI-RS resources, provided by nzp-CSI-RS-ResourceList and does not indicate a power offset powerOffset, for CQI calculation for the sub-configuration the UE follows the procedure previously described in this Clause. - If a sub-configuration indicates a power offset powerOffset, for CQI calculation, the UE shall assume the corresponding PDSCH signals transmitted on the antenna ports of a CSI-RS resource would have a ratio of EPRE to CSI-RS EPRE equal to the difference between powerControlOffset of the CSI-RS resource, given in Clause 5.2.2.3.1, and powerOffset, where the difference is expected to take one of the values that can be configured for powerControlOffset of the CSI-RS resource, given in Clause 5.2.2.3.1, and is also expected to take a value that is no larger than the value of powerControlOffset. < Unchanged parts are omitted > |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509087](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509087.zip)

**Agreement** · `9.2` UE features Batch B · `RAN1#123:9.2:005` · 후보 · 관련 주제: Beam management, CSI 보고/codebook, CSI-RS

> For active resource counting for L1 CLI-RSSI measurement across two DL subbands, add the following note for FG 60-1:
> - Note for component 11: If the UE reporting component 11 as “with factor-of-two relaxation for active CSI-RS resource and port counting” also reports FG 60-8 in the same band, factor-of-two relaxation for active CSI-RS resource and port counting also applies to L1 CLI-RSSI measurement resource counting
> - resource and port counting also applies to L1 CLI-RSSI measurement resource counting
> | 60-1 | Basic feature for SBFD-aware UE TX/RX/measurement behaviour and procedures | 1. Support of cell-common configuration of time and frequency location of SBFD subbands 2. Support of UL transmission in one UL subband and DL reception in one/two DL subband in SBFD symbols 3. Support of link direction determination based on configured/scheduled transmissions/receptions and collision handling 4. Support of UL transmissions or DL receptions across SBFD symbols and non-SBFD symbols in different slots, where the transmissions or receptions are restricted to SBFD symbols or non-SBFD symbols (Configuration 1) 5. Support of separate CSI reports for SBFD and non-SBFD symbols 6. Support of separate PUCCH frequency resource configuration in SBFD symbols and non-SBFD symbols 7. Support of separate UL power control parameters based on unified TCI framework in SBFD symbols and non-SBFD symbols 8. Support of separate PUSCH frequency hopping offset in SBFD symbols and non-SBFD symbols 9. Support of separate SRS resource set configuration in SBFD symbols and non-SBFD symbols 10. Number of partial PRGs supported 11. Supported CSI timeline, active CSI-RS ports counting and active CSI-RS resource counting for a single CSI-RS resource across two DL subbands 12. Maximum of one DL-UL switching point per SBFD slot for actual DL/UL transmission(s) 13. Determination of TBS of PDSCH/PUSCH in SBFD symbols |  | YES | n/a | Basic feature for SBFD-aware UE TX/RX/ measurement behaviour and procedures is not supported | Per band | TDD only | n/a | n/a | Component 7 applies only to UEs supporting FG 23-1-1h Note: Component 9 is only applicable for SRS resource sets with usage codebook, nonCodebook and beamManagement Component 10 candidate values: {2, 4} Component 11 candidate values: {“with factor-of-two relaxation”, “with factor-of-two relaxation for active CSI-RS resource and port counting”, “no relaxation”} Note for component 11: If the UE reporting component 11 as “with factor-of-two relaxation for active CSI-RS resource and port counting” also reports FG 60-8 in the same band, factor-of-two relaxation for active CSI-RS resource and port counting also applies to L1 CLI-RSSI measurement resource counting | Optional with capability signalling |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx)

**Agreement** · `9.2` UE features Batch B · `RAN1#123:9.2:006` · 후보 · 관련 주제: CSI 보고/codebook

> Add the following new components in FG 60-9:
> - Maximum number of configured L1 SRS-RSRP measurement resources (sum of aperiodic/semi-persistent/periodic) per CC
>   - Candidate values: All integers from 1 to 16
> - Maximum number of simultaneous L1 SRS-RSRP measurement resources (sum of aperiodic/semi-persistent/periodic) per CC
>   - Candidate values: All integers from 1 to 16
> - Maximum number of aperiodic CSI report setting per BWP for L1-SRS-RSRP report
>   - Candidate values: {1, 2, 3, 4}
> - Maximum number of SRS-RSRP measurement resources across all CCs within a slot
>   - Candidate values: {1, 2, 4, 8}
> - Maximum number of aperiodic SRS-RSRP measurement resources across all CCs
>   - Candidate values: {1, 2, 3, 4}
> NR_LPWUS
> Conclusion 2.6-2-2
> There is no consensus to adopt the following in Rel-19
> - For FG 62-2/2a, add a new component “Nominal MO duration = actual LP-WUS duration”
> - Define new FG for supporting nominal MO duration > actual LP-WUS duration for LP-WUS operation in CONNECTED mode
> NR_MC_enh2

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx)

**Agreement** · `9.2` UE features Batch B · `RAN1#123:9.2:009` · 후보

> Introduce the following FG 66-6a/6b/6c/6d:
> | 66-6a | Nominal RBG size of Configuration 3 for FDRA type 0 for DCI format 1_3 with different SCS and/or different carrier type | 1) Support of nominal RBG size of Configuration 3 for FDRA type 0 for DCI format 1_3 | 66-1 | Yes |  |  | Per UE | No | No | No |  | Optional with capability signaling |
> | 66-6b | Nominal RBG size of Configuration 3 for FDRA type 0 for DCI format 0_3 with different SCS and/or different carrier type | 1) Support of nominal RBG size of Configuration 3 for FDRA type 0 for DCI format 0_3 | 66-2 | Yes |  |  | Per UE | No | No | No |  | Optional with capability signaling |
> | 66-6c | Configurable Type-1A fields for DCI format 0_3/1_3 with different SCS and/or different carrier type | 1) Support Type-1A for ‘Antenna port(s)’ field for DCI format 1_3 2) Support Type-1A for ‘Antenna port(s)’, ‘Precoding information and number of layers’ and ‘SRS resource indicator’ fields for DCI format 0_3 | At least one of {66-1, 66-2} | Yes |  |  | Per UE | No | No | No |  | Optional with capability signaling |
> | 66-6d | FDRA Type 1 granularity of 2, 4, 8, or 16 consecutive RBs based RIV for DCI format 1_3/0_3 with different SCS and/or different carrier type | 1) Support of FDRA Type 1 granularity of 2, 4, 8, or 16 consecutive RBs based RIV for DCI format 0_3 2) Support of FDRA Type 1 granularity of 2, 4, 8, or 16 consecutive RBs based RIV for DCI format 1_3 | At least one of {66-1, 66-2} | Yes |  |  | Per UE | No | No | No |  | Optional with capability signaling |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx)

**Agreement** · `11.3.1` Waveform · `RAN1#123:11.3.1:007` · 후보 · 관련 주제: CSI 보고/codebook

> - Performance benefit to be evaluated using both link level and system level simulation.
> - FFS: metrics
> - Link level configuration for multi-layer UL waveforms study.
> | Parameters | Values |
> | Carrier frequency​​ | 4 GHz |
> | Subcarrier spacing​​ | 30 kHz​​ |
> | UE antenna ports | 2, 4 |
> | BS antenna ports | 64, port reduction is not precluded |
> | FDRA | 4, 8, 16, 32, 64​​ |
> | Waveform​​s | CP-OFDM DFT-s-OFDM​​ |
> | MCS/modulation​​ | NR UL MCS table with 256 QAM |
> | Number of layers​ | 2 layers​​, 4 layers |
> | Channel model​​ | CDL-A30​​, TDL-C300, CDL-C300, |
> | UE speed​​ | 3km/h​​, 30 km/h |
> | Channel est.​​ | Practical​ |
> | SRS periodicity | To be reported by the company |
> | Receiver | LMMSE |
> | HARQ retransmission​ | Disabled |
> | DMRS configuration | Configuration type 1 2 DMRS symbols per slot |
> | Number of PUSCH data | 12 symbols |
> | Waveform and MIMO configuration | 5G codebook, to be reported by the company |
> | BLER target | 10% |
> | Frequency hopping | Disabled |
> | Power class and power mode | Option 1: PC2, total power limited to 26 dBm. MaxRank 2: Each PA is limited to 23 dBm MaxRank 4: Each PA is limited to 20 dBm Option2: PC3, total power limited to 23 dBm. MaxRank 2: Each PA is limited to 20 dBm MaxRank 4: Each PA is limited to 17 dBm |

남은 FFS 1건

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · `[123-R20-6GR-Waveform]`

**Agreement** · `11.3.1` Waveform · `RAN1#123:11.3.1:008` · 후보

> Table: System level configuration for multi-layer UL CP-OFDM/DFT-s-OFDM study:
> | Parameters | Values |
> | System configuration | UMa, 21 cells, 10, 30 or 50 UEs/cell Detailed parameters not listed in this table according to UMa as defined in AI 11.2 |
> | Traffic model | FTP model 3, 0.5 Mbyte packet sizes Network load up to companies to report Full buffer (optional, for calibration) |
> | Carrier frequency | 4 GHz |
> | Channel bandwidth/Subcarrier spacing | At least 100 MHz, 30KHz |
> | Frame structure | TDD (DDDSU), S-slot D:G:U as 10:2:2 |
> | UE antenna ports | Same as link level |
> | BS antenna ports | Outdoor Combination 2 for UMa as agreed in 11.2 |
> | UE antenna model | The UE handheld model as agreed in AI 11.2, companies to report the used model. |
> | ISD | 500 m |
> | Maximum Number of layers (maxRank) per UE | Adaptive rank, maxRank 2 or 4 SU-MIMO |
> | Receiver | Same as link level, port reduction mapping to be reported |
> | Waveform and MIMO configuration | Same as link level |
> | Power class and power mode | Same as link level |
> | UL Maximum power | MPR based Pcmax according to modulation/FDRA/waveform/coherency/etc. Option 1: 38.101-1 section 6.2D definition Option 2: Based on a realistic PA model |
> | UL Power Control Settings | P0 and Alpha to be reported by the company |
> | SRS periodicity | To be reported by the company |
> Table: Link level multi-user evaluation assumption for UL low-PAPR proposals
> | Parameters | Values |
> | User # | 2 users |
> | RB allocation | X RBs per UE, with Y RB overlap. I.e. 2X-Y RBs as the total occupied BW |
> | Per user configuration | As in the single user sim assumptions agreed earlier. |
> | Multi-user overlap RBs | Reported by companies |
> | Baseline scheme | No spectrum extension/truncation. (2X-Y)/2 RB as the occupied BW for each simulated UE. |
> | Per UE MCS | Chosen to align with the spectral efficiency |
> | Receiver type | The receiver type/algorithm to be reported by the proponent |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · `[123-R20-6GR-Waveform]`

### RAN1#122bis — 11건

**Agreement** · `8.3` Maintenance on Evolution of NR duplex operation: Sub-band full duplex (SBFD) · `RAN1#122bis:8.3:014` · 후보 · 관련 주제: Beam management, CSI 보고/codebook, CSI-RS

> Adopt the following TP in principle to section 5.2.1.5.1 and 5.2.1.5.1a, TS 38.214
> | 5.2.1.5.1 Aperiodic CSI Reporting/Aperiodic CSI-RS when the triggering PDCCH and the CSI-RS have the same numerology <Unchanged parts omitted> - [If the scheduling offset between the last symbol of the PDCCH carrying the triggering DCI and the first symbol of the aperiodic CLI measurement resources in a CLI-RSSI-MeasurementResourceSet or in a SRS-RSRP-MeasurementResourceSet is equal to or greater than the UE reported threshold beamSwitchTiming when the reported value is one of the values of {14,28,48} and enableBeamSwitchTiming is not provided, or is equal to or greater than 48 when the UE provides beamSwitchTiming-r16 and enableBeamSwitchTiming is provided, and] - if the UE is configured with a list of TCI states in CSI-AssociatedReportConfigInfo and it is configured with unifiedTCI-StateType, the UE is expected to apply the QCL assumptions indicated by qcl-Info for the aperiodic CLI measurement resources in the CSI triggering state indicated by the CSI trigger field in DCI. - if the UE is not configured with a list of TCI states in CSI-AssociatedReportConfigInfo and if the UE is configured with unifiedTCI-StateType, the UE is expected to apply the indicated DL TCI state or joint TCI state. - if the UE is not configured with a list of TCI states in CSI-AssociatedReportConfigInfo and if the UE is not configured with unifiedTCI-StateType, the UE is expected to assume that the aperiodic CLI measurement resources are the QCL ‘typeD’ to one of the latest received PDSCH and the latest monitored CORESET. <Unchanged parts omitted> 5.2.1.5.1a Aperiodic CSI Reporting/Aperiodic CSI-RS when the triggering PDCCH and the CSI-RS have different numerologies <Unchanged parts omitted> [- If the scheduling offset between the last symbol of the PDCCH carrying the triggering DCI and the first symbol of the aperiodic CLI measurement resources in a CLI-RSSI-MeasurementResourceSet or in a SRS-RSRPMeasurementResourceSet is equal to or greater than beamSwitchTiming + d in CLI measurement resource symbols, when the reported value is one of the values of {14,28,48} and enableBeamSwitchTiming is not provided, or is equal to or greater than 48+ in CLI measurement resource symbols when the UE provides beamSwitchTiming-r16 and enableBeamSwitchTiming is provided, where if the µPDCCH < µCLI, the beam switching timing delay d is defined in Table 5.2.1.5.1a-1, else d is zero, and] - if the UE is configured with a list of TCI states in CSI-AssociatedReportConfigInfo and it is configured with unifiedTCI-StateType, the UE is expected to apply the QCL typeD assumptions indicated by qcl-Info for the aperiodic CLI measurement resources in the CSI triggering state indicated by the CSI trigger field in DCI. - if the UE is not configured with a list of TCI states in CSI-AssociatedReportConfigInfo and if the UE is configured with unifiedTCI-StateType, the UE is expected to apply the DL TCI state or joint TCI state as indicated by unifiedTCI-StateType. - if the UE is not configured with a list of TCI states in CSI-AssociatedReportConfigInfo, and if the UE is not configured with unifiedTCI-StateType, the UE is expected to assume that the aperiodic CLI measurement resources are the QCL ‘typeD’ to one of the latest received PDSCH and the latest monitored CORESET. |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · `[122bis-R19-SBFD]`

**Agreement** · `8.3` Maintenance on Evolution of NR duplex operation: Sub-band full duplex (SBFD) · `RAN1#122bis:8.3:016` · 후보 · 관련 주제: CSI 보고/codebook

> Adopt the following TP in principle to section 5.2.2.6, TS 38.214
> | 5.2.1.4.1 Resource Setting configuration <Unchanged parts omitted> For a semi-persistent or periodic L1-SRS-RSRP or L1-CLI-RSSI measurement resources if a UE is configured with SBFD symbols and a CSI-ReportConfig with the higher layer parameter symbolType, the UE only considers the measurement resources within either SBFD symbol(s) or non-SBFD symbol(s) as indicated by symbolType for the measurement and reporting. If a UE is not configured with SBFD symbols, the higher layer parameter symbolType is not applicable and the UE considers the measurement resources provided in CSI-ResourceConfig indicated by CSI-ReportConfig. |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · `[122bis-R19-SBFD]`

**Agreement** · `8.3` Maintenance on Evolution of NR duplex operation: Sub-band full duplex (SBFD) · `RAN1#122bis:8.3:018` · 후보 · 관련 주제: Beam management, CSI 보고/codebook, CSI-RS

> Adopt the following TP in principle to section 5.2.1.5.1a, 5.2.2.5 and 5.2.2.6, TS 38.214.
> | 5.2.1.5.1a Aperiodic CSI Reporting/Aperiodic CSI-RS when the triggering PDCCH and the CSI-RS have different numerologies <Unchanged parts omitted> [- If the scheduling offset between the last symbol of the PDCCH carrying the triggering DCI and the first symbol of the aperiodic CLI measurement resources in a CLI-RSSI-MeasurementResourceSet or in a SRS-RSRPMeasurementResourceSet is equal to or greater than beamSwitchTiming + d in CLI measurement resource symbols, when the reported value is one of the values of {14,28,48} and enableBeamSwitchTiming is not provided, or is equal to or greater than 48+ in CLI measurement resource symbols when the UE provides beamSwitchTiming-r16 and enableBeamSwitchTiming is provided, where if the µPDCCH < µCLI, the beam switching timing delay d is defined in Table 5.2.1.5.1a-1, else d is zero, and] - if the UE is configured with a list of TCI states in CSI-AssociatedReportConfigInfo and it is configured with unifiedTCI-StateType, the UE is expected to apply the QCL typeD assumptions indicated by qcl-Info for the aperiodic CLI measurement resources in the CSI triggering state indicated by the CSI trigger field in DCI. - if the UE is not configured with a list of TCI states in CSI-AssociatedReportConfigInfo and if the UE is configured with unifiedTCI-StateType, the UE is expected to apply the DL TCI state or joint TCI state as indicated by unifiedTCI-StateType apply the indicated DL TCI state or joint TCI state. - if the UE is not configured with a list of TCI states in CSI-AssociatedReportConfigInfo, and if the UE is not configured with unifiedTCI-StateType, the UE is expected to assume that the aperiodic CLI measurement resources are the QCL ‘typeD’ to one of the latest received PDSCH and the latest monitored CORESET. <Unchanged parts omitted> 5.2.2.5 SRS-RSRP measurement resource <Unchanged parts omitted> For all K periodic SRS-RSRP resources within an SRS-RSRP resource set: - If qcl-InfoPeriodicSRS-RSRP-MeasurementResource is configured, the UE shall also be configured with unifiedTCI-StateType and shall assume the configured TCI state indicated by qcl-InfoPeriodicSRS-RSRP-MeasurementResource. - If qcl-InfoPeriodicSRS-RSRP-MeasurementResource is not configured and unifiedTCI-StateType is not configured, the UE shall perform the SRS-RSRP measurement assuming that the resources are QCL ‘typeD’ to one of the latest received PDSCH and the latest monitored CORESET. - If qcl-InfoPeriodicSRS-RSRP-MeasurementResource is not configured and unifiedTCI-StateType is configured, the UE shall perform the SRS-RSRP measurement assuming the DL TCI state or joint TCI state as indicated by unifiedTCI-StateType the indicated DL TCI state or joint TCI state. <Unchanged parts omitted> 5.2.2.6 CLI-RSSI measurement resource <Unchanged parts omitted> A UE expects all K periodic CLI-RSSI resources within a CLI-RSSI resource set to be configured or not with qcl-InfoPeriodicCLI-RSSI-MeasurementResource. If qcl-InfoPeriodicCLI-RSSI-MeasurementResource is configured, the UE shall also be configured with unifiedTCI-StateType and shall assume the configured TCI state indicated by qcl-InfoPeriodicCLI-RSSI-MeasurementResource. If qcl-InfoPeriodicCLI-RSSI-MeasurementResource is not configured and unifiedTCI-StateType is not configured, the UE shall perform the CLI-RSSI measurement assuming that the resources are QCL ‘typeD’ to one of the latest received PDSCH and the latest monitored CORESET. If qcl-InfoPeriodicCLI-RSSI-MeasurementResource is not configured and unifiedTCI-StateType is configured, the UE shall perform the CLI-RSSI measurement assuming the DL TCI state or joint TCI state as indicated by unifiedTCI-StateType the indicated DL TCI state or joint TCI state. |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · `[122bis-R19-SBFD]`

**Agreement** · `8.8` Maintenance on others · `RAN1#122bis:8.8:010` · 후보 · 관련 주제: CSI 보고/codebook, CSI-RS

> - Draft LS R1-2507925 is endorsed in principle.
> - Adopt the following TP for TS38.214 Section 5.2.4a and TS 38.212, section 6.3.1.2.1
> - Note: No dedicated issue to support early CSI acquisition for L3 handover to be discussed in RAN1 before RAN#111.
> | 1. Overall Description RAN1 thanks RAN2 for the LS R1-2506717 (R2-2506504) on early CSI acquisition for L3 handover. From RAN1 perspective, there is no problem to support early CSI acquisition for L3 by re-using the early CSI acquisition framework for LTM. On the configuration of channel measurement and interference measurement resources in RAN2 RRC CR (R2-2506450), RAN1 suggest to directly use NZP CSI RS resource set and CSI-IM resource set and suggest the following changes on EarlyCSI-Acquisition-r19. EarlyCSI-Acquisition-r19 ::= SEQUENCE { early-NZP-CSI-RS-Resource-r19 NZP-CSI-RS-ResourceId, early-CSI-IM-Resource-r19 CSI-IM-ResourceId OPTIONAL, -- Need R reportQuantity-r19 ENUMERATED {cri-RI-PMI-CQI, spare}, cqi-Table-r19 ENUMERATED {table1, table2, table3, table4-r17}, codebookConfig-EarlyCSI-r19 CodeBookConfig-EarlyCSI-r19 } 2. Actions To RAN2 ACTION: RAN1 respectfully asks RAN2 to take the above information into account. |
> | 5.2.4a CSI Reporting for LTM A UE configured with LTM-Config can be provided configurations for CSI acquisition, by up to one Reporting Setting, ltm-CSI-ReportConfig, for a candidate cell. Each Reporting Setting ltm-CSI-ReportConfig is associated with either one or two Resource Settings When one Resource Setting (given by higher layer parameter ltm-ResourcesForChannelMeasurement) is configured, it provides a list of NZP CSI-RS resources for both channel and interference measurements. The UE is not expected to be configured with more than 128 NZP CSI-RS ports in the CSI-RS resource set contained within the Resource Setting. When two Resource Settings are configured, the first Resource Setting (given by higher layer parameter ltm-ResourcesForChannelMeasurement) provides a list of NZP CSI-RS resources for channel measurement, and the second Resource Setting (given by higher layer parameter ltm-ResourceForInterferenceMeasurements), provides a list of [CSI-IM resources] for interference measurement. The UE is not expected to be configured with more than 128 NZP CSI-RS ports in the CSI-RS resource set contained within the Resource Setting. The Resource Setting given by higher layer parameter ltm-ResourcesForChannelMeasurement, LTM-CSI-ResourceConfig, contains configuration of a ltm-NZP-CSI-RS-ResourceSet which comprises of a list of Z ≥ 1 NZP CSI-RS resource indices (given by ltm-CSI-RS-ResourceList) and a list of Z LTM-CandidateIds (given by ltm-CandidateIdList) referring to candidate cells associated with the NZP CSI-RS resource indices. For CSI acquisition associated with a Reporting Setting, ltm-CSI-ReportConfig, the UE is expected to measure the NZP-CSI-RS resources in ltm-CSI-RS-ResourceList associated with the LTM-CandidateId that is equal to the LTM-CandidateId of the LTM-Candidate under which the Reporting Setting is configured. The UE shall expect the following configuration provided by ltm-CSI-ReportConfig: - For the frequency granularity of the CSI report, the CQI format indicator is Wideband CQI. - For the frequency granularity of the CSI report, the PMI format indicator is Wideband PMI. - The codebook type is typeI-SinglePanel. - The reportQuantity is set to ‘cri-RI-PMI-CQI’. After a UE receives an LTM Cell Switch Command MAC CE [10, TS 38.321] providing a candidate cell (given by Target Configuration ID field), and a ltm-CSI-ReportConfig is configured for the candidate cell, the UE can measure corresponding NZP CSI-RS resources and CSI-IM resources if configured, and shall transmit a CSI report to the candidate cell. For RACH-less LTM cell switch [23, TS 38.300], the UE shall transmit the CSI report to the candidate cell using the first PUSCH corresponding to a dynamic grant or a configured grant [6, TS 38.213]. For RACH-based LTM cell switch using a contention-free random access procedure [23, TS 38.300], the UE shall transmit the CSI report to the candidate cell using the PUSCH scheduled by the RAR UL grant or MsgA PUSCH. For RACH-based LTM cell switch using a contention-based random access procedure [23, TS 38.300], the UE shall transmit the CSI report to the candidate cell using the first PUSCH corresponding to a dynamic grant or a configured grant after the HARQ-ACK transmission corresponding to Msg4 or MsgB. If a valid CSI is not available, the UE shall transmit a CSI report which contains a CQI corresponding to the lowest CQI index. Depending on the UE capability, the UE may measure NZP CSI-RS resources and CSI-IM resources if configured corresponding to a ltm-CSI-ReportConfig before receiving the LTM Cell Switch Command MAC CE [10, TS 38.321]. |
> | 6.3.2.1.2 CSI If cqi-BitsPerSubband is configured, this Clause 6.3.2.1.2 applies by taking Subband CQI as Subband differential CQI and replacing the corresponding number of bits 2 by 4. <Unchanged part omitted> The mapping order of CSI fields of one report for CSI reporting for L1/L2-triggered mobility as defined in Clause 5.2.4a of [6, TS 38.214] is provided in Table 6.3.1.1.2-7 by taking only Tables 6.3.1.1.2-1/3 for the determination of the bitwidth of a CSI field. The mapping order of CSI fields of one report for CRI/RSRP or SSBRI/RSRP or CRI/RSRP/CapabilityIndex or SSBRI/RSRP/CapabilityIndex reporting is provided in Table 6.3.1.1.2-8. The mapping order of CSI fields of one report for inter-cell SSBRI/RSRP reporting is provided in Table 6.3.1.1.2-8. The mapping order of CSI fields of one report for CRI/SINR or SSBRI/SINR or CRI/SINR/CapabilityIndex or SSBRI/SINR/CapabilityIndex reporting is provided in Table 6.3.1.1.2-8A. The mapping order of CSI fields of one report for group-based CRI/RSRP or SSBRI/RSRP reporting is provided in Table 6.3.1.1.2-8B. The mapping order of CSI fields of one report for SSBRI/RSRP or CRI/RSRP reporting for L1/L2-triggered mobility is provided in Table 6.3.1.1.2-8C. The mapping order of CSI fields of one report for MRI/CLI-RSSI is provided in Table 6.3.1.1.2-8D. The mapping order of CSI fields of one report for predicted CRI/RSRP or predicted SSBRI/RSRP reporting is provided in Table 6.3.1.1.2-8E. The mapping order of CSI fields of one report for time instance indicator/predicted CRI/predicted RSRP or time instance indicator/predicted SSBRI/predicted RSRP reporting is provided in Table 6.3.1.1.2-8F. The mapping order of CSI fields of one report for CRI/RSRP or SSBRI/RSRP if nrofReportedRS is configured is provided in Table 6.3.1.1.2-8G. The mapping order of CSI fields of one report for RS-PAI is provided in Table 6.3.1.1.2-8H. The procedure in clause 6.3.2 described for CSI part 1 is also applicable for one report for CRI/RSRP, SSBRI/RSRP, predicted CRI/RSRP, predicted SSBRI/RSRP, time instance indicator/predicted CRI/predicted RSRP, time instance indicator/predicted SSBRI/predicted RSRP, RS-PAI, CRI/SINR, SSBRI/SINR, MRI/SRS-RSRP, MRI/CLI-RSSI reporting, CSI reporting for L1/L2-triggered mobility, TDCP reporting, delay offset reporting, frequency offset reporting, both delay offset and frequency offset reporting, and phase offset reporting. <Unchanged part omitted> |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508156](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508156.zip)

**Conclusion** · `8.8` Maintenance on others · `RAN1#122bis:8.8:015` · 후보

> For Rel-19 low NR band carrier aggregation via switching, in RAN1, there is no consensus to support UE processing timeline relaxation for the following scenarios
> - a PDCCH reception schedules a PUSCH transmission
> - a PDCCH reception indicates SRS transmission
> - a RAR schedules a PUSCH transmission
> - a PUCCH transmission with HARQ-ACK for a PDSCH or PDCCH reception

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2507657](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2507657.zip)

**Agreement** · `9.3` UE features for evolution of NR duplex operation: SBFD · `RAN1#122bis:9.3:005` · 후보

> Update FG 60-9 as follows:
> - Remove “FFS: whether each of components within brackets is separate FG or require reporting”
> - Define no prerequisite FG
> - Revise consequence such as “[Aperiodic] L1 SRS-RSRP measurement and aperiodic reporting is not supported”
> - Add “[Candidate values for component 2 are {4, 8, 16, 32}]” in Note column
> - Remove “FFS: other potential component/FG”
> | 60-9 | L1 SRS-RSRP measurement and aperiodic reporting | 1. Aperiodic L1 SRS-RSRP reporting on PUSCH, and periodic and aperiodic SRS-RSRP measurement resource 2. Maximum number of L1 SRS-RSRP measurement resources across all CCs FFS: whether each of components within brackets is separate FG or require reporting FFS: other potential component/FG | FFS | YES | n/a | [Aperiodic] L1 SRS-RSRP measurement and aperiodic reporting is not supported | Per band | TDD only | n/a | n/a | Candidate values for component 2 are {4, 8, 16, 32} | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2507966](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2507966.zip)

**Agreement** · `9.11` UE features for MCE for NR Phase 3 · `RAN1#122bis:9.11:010` · 후보 · 관련 주제: Beam management, CSI 보고/codebook, CSI-RS

> Ask RAN2 to feedback if it is possible to update prerequisite FG(s) for Rel-18 RAN1 FG 49-4a/4b/4c/4d/5a/5b/6/7/8/9/10/12/12a/13/14 in Rel-19 as follows (red fonts):
> | Index | Feature group | Components | Prerequisite feature groups |
> | 49-4a | Nominal RBG size of Configuration 3 for FDRA type 0 for DCI format 1_3 | 1) Support of nominal RBG size of Configuration 3 for FDRA type 0 for DCI format 1_3 | At least one of {49-1, 49-1b, 66-1} |
> | 49-4b | Nominal RBG size of Configuration 3 for FDRA type 0 for DCI format 0_3 | 1) Support of nominal RBG size of Configuration 3 for FDRA type 0 for DCI format 0_3 | At least one of {49-2, 49-2b, 66-2} |
> | 49-4c | Configurable Type-1A fields for DCI format 0_3/1_3 | 1) Support Type-1A for ‘Antenna port(s)’ field for DCI format 1_3 2) Support Type-1A for ‘Antenna port(s)’, ‘Precoding information and number of layers’ and ‘SRS resource indicator’ fields for DCI format 0_3 | At least one of {49-1, 49-1b, 49-2, 49-2b, 66-1, 66-2} |
> | 49-4d | FDRA Type 1 granularity of 2, 4, 8, or 16 consecutive RBs based RIV for DCI format 1_3/0_3 | 1) Support of FDRA Type 1 granularity of 2, 4, 8, or 16 consecutive RBs based RIV for DCI format 0_3 2) Support of FDRA Type 1 granularity of 2, 4, 8, or 16 consecutive RBs based RIV for DCI format 1_3 | At least one of {49-1, 49-1b, 49-2, 49-2b, 66-1, 66-2} |
> | 49-5a | Trigger Type 3 HARQ CB based feedback using DCI format 1_3 | 1. Support feedback of type 3 HARQ-ACK codebook, triggered by a DCI 1_3 scheduling at least a PDSCH 2. Support feedback of type 3 HARQ-ACK codebook, triggered by a DCI 1_3 without scheduling a PDSCH using a reserved FDRA value | At least one of {49-1, 49-1b, 66-1} |
> | 49-5b | Trigger enhanced Type 3 HARQ CB based feedback using DCI format 1_3 | 1. Support feedback of enhanced type 3 HARQ-ACK codebook, triggered by a DCI 1_3 2. Support configuration of up to 8 enhanced type 3 HARQ-ACK codebooks. 3. Support feedback of a dynamically selected enhanced type 3 HARQ-ACK codebook based on triggering information in DCI 1_3 4. Support transmission of enhanced type 3 HARQ-ACK codebook using the first or second PUCCH configuration based on PHY priority indication in the triggering DCI (for a UE supporting two HARQ-ACK codebooks / PUCCH config in 49-6) 5. Supported maximum number of actual PUCCH transmissions for type 3 or enhanced type 3 HARQ-ACK codebook feedback within a slot | At least one of {49-1, 49-1b, 66-1} |
> | 49-6 | Two HARQ-ACK codebooks with up to one sub-slot based HARQ-ACK codebook simultaneously constructed for supporting HARQ-ACK codebooks with different priorities by DCI format 1_3 | 1. Supports two HARQ-ACK codebooks with different priorities to be simultaneously constructed with the restriction up to one sub-slot based HARQ-ACK codebook. 2. Supports separate PUCCH configuration for different HARQ-ACK codebooks. 3. Supports 2-level priority of HARQ-ACK for dynamically scheduled PDSCH and SPS PDSCH. 4. Supports a DCI format 1_3 scheduling PDSCH with different HARQ-ACK priorities when only DCI format 0_3/1_3 is configured per BWP. 5. Supports separate configuration of parameters PDSCH-HARQ-ACK-Codebook, UCI-OnPUSCH and 'codeBlockGroupTransmission" for different HARQ-ACK codebooks. 6. Supported maximum number of actual PUCCH transmissions for HARQ-ACK within a slot Candidate values for the component 6 of this FG is: For NCP, {4, 5, 6, 7} for 2-symbol*7 sub-slot configuration; For ECP, the candidate value is {4,5,6} for 2-symbol*6 sub-slot configuration 7. Support intra-UE multiplexing/prioritization of UL overlapping channels/signals with two priority levels for HARQ-ACK | At least one of {49-1, 49-1b, 66-1} |
> | 49-7 | UL intra-UE multiplexing/prioritization of overlapping channel/signals with two priority levels in physical layer for DCI format 1_3/0_3 | Support intra-UE multiplexing/prioritization of overlapping PUCCH/PUCCH and PUCCH/PUSCH with two priority levels in physical layer (PHY) for DCI format 1_3/0_3 1) Configuration of PHY priority level for CG PUSCH and SR, and dynamic indication of priority level for dynamic PUSCH with a single DCI format 0_3 2) Multiplexing/prioritization between UL channels/signals with the same PHY priority level 3) Prioritization between UL channels/signals with different PHY priority levels 4) Additional number of symbols (d1) needed beyond the PUSCH preparation time for cancelling a low priority UL transmission. 5) Additional number of symbols (d2) of the preparation time needed for the high priority UL transmission that cancels a low priority UL transmission | At least one of {49-1, 49-1b, 49-2, 49-2b, 66-1, 66-2} |
> | 49-8 | Triggered HARQ-ACK codebook re-transmission for DCI format 1_3 | 1. Support HARQ-ACK re-transmission from an earlier PUCCH slot based on the triggering information in DCI format 1_3 2. Support the related PHY priority handling in terms of HARQ-ACK codebook selection and the applicable PUCCH configuration (for a UE supporting two HARQ-ACK codebooks / PUCCH config in 49-6) 3. Supported minimum value M for the HARQ re-tx offset 4. Supported maximum value N for the HARQ re-tx offset | at least one of {49-1, 49-1b, 66-1} |
> | 49-9 | SCell dormancy indication within active time in DCI format 0_3/1_3 | Support for SCell dormancy indication sent within the active time on PCell with DCI format 0_3/1_3 | 6-5, at least one of {49-1, 49-1b, 49-2,49-2b, 66-1, 66-2} |
> | 49-10 | Dynamic indication of applicable minimum scheduling restriction by DCI format 0_3/1_3 | 1) Dynamic indication of applicable minimum scheduling restriction by DCI format 0_3 and 1_3 2) minimumSchedulingOffset K0 configuration for PDSCH and aperiodic CSI-RS triggering offset 3) minimumSchedulingOffset K2 configuration for PUSCH 4) Support of extended value range for aperiodic CSI-RS triggering offset | At least one of {49-1, 49-1b, 49-2,49-2b, 66-1, 66-2} |
> | 49-12 | Unified TCI with joint DL/UL TCI update by DCI format 1_3 for intra-cell and inter-cell beam management with more than one MAC-CE activated joint TCI state per CC | 1: TCI state indication for update and activation MAC-CE+DCI-based TCI state indication (use of DCI formats 1_3 with DL assignment for at least one serving cell in a scheduledCellListDCI-1-3 to provide indicated unified TCI state(s) for the CC(s) in the scheduledCellListDCI-1-3) 2: The minimum beam application time in Y symbols per SCS 3: The maximum number of MAC-CE activated joint TCI states per CC in a band | 23-1-1, At least one of {49-1, 49-1b, 66-1} |
> | 49-12a | Unified TCI with separate DL/UL TCI update by DCI format 1_3 for intra-cell beam management with more than one MAC-CE activated separate TCI state per CC | TCI state indication for update and activation MAC-CE+DCI-based TCI state indication (use of DCI formats 1_3 with DL assignment for at least one serving cell in a scheduledCellListDCI-1-3 to provide indicated unified TCI state(s) for the CC(s) in the scheduledCellListDCI-1-3) 2. The minimum beam application time in Y symbols per SCS 3. The maximum number of MAC-CE activated DL TCI states per CC in a band 4. The maximum number of MAC-CE activated UL TCI states per CC in a band | 23-10-1, At least one of {49-1, 49-1b, 66-1} |
> | 49-13 | Default QCL assumption for multi-cell scheduling by DCI format 1_3 | Indicates whether the UE can be configured with enabledDefaultBeamFormultiCellScheduling for default QCL assumption for multi-cell scheduling by DCI format 1_3 for same/different numerologies Candidate values are {different only, both} When "both" is reported, the UE supports this feature for same SCS and for different SCS combination(s) (low-to-high, high-to-low or both) reported for 49-1b | At least one of {49-1, 49-1b, 66-1} |
> | 49-14 | Support of BWP switch indication by DCI format 0_3/1_3 | Support of BWP switch indication by DCI format 0_3/1_3 | At least one of {49-1, 49-1b, 49-2, 49-2b, 66-1, 66-2} for the BC At least one of {6-2, 6-3, 6-4} for at least one band of the BC |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2507976](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2507976.zip)

**Conclusion** · `9.11` UE features for MCE for NR Phase 3 · `RAN1#122bis:9.11:011` · 후보

> Update a component in FG 66-2 “Support Type-2 for ‘Antenna port(s)’ field” as follows:
> “Support Type-2 for ‘Antenna port(s)’, ‘Precoding information and number of layers’ and ‘SRS resource indicator’ fields”

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2507976](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2507976.zip)

**Agreement** · `9.14` Others · `RAN1#122bis:9.14:002` · 후보

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 67. TEI19 [Simul_SRSCS] | 67-4 | Support of simultaneous SRS carrier switching [Simul_SRSCS] | 1.- Support simultaneous SRS carrier switches. Two SRS carrier switches are considered to be simultaneous if the SRS transmission (including RF retuning time) in both CCs overlap in time | 2-56 | Yes | N/A | Simultaneous SRS CS across multiple CC is not supported | Per band pair per band combination | N/A | N/A | N/A | For each target band, the UE can indicate with which other target bands in the band combination can SRS carrier switching be simultaneously triggered | Optional with capability signaling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508085](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508085.zip)

**Agreement** · `9.14` Others · `RAN1#122bis:9.14:003` · 후보

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 67. TEI19 [Pos_SRSHop] | 67-2b | UL Time Window and transmission of SRS for positioning with Tx Frequency hopping within the window for non-RedCap UEs [Pos_SRSHop] | Support of UL Time Window and transmission of SRS for positioning with Tx Frequency hopping within the window | 67-2 | No Yes | N.A. | UE does not support the UL time window for SRS for positioning with Tx frequency hopping | Per band | N.A. | N.A. | N.A. |  | Optional with capability signaling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508085](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508085.zip)

**Agreement** · `11.4.2` Modulation, joint channel coding and modulation · `RAN1#122bis:11.4.2:003` · 후보 · 관련 주제: Beam management, CSI 보고/codebook

> For link level simulation for modulation evaluation, companies are encouraged to evaluate with the following assumptions and should report the exact scheme evaluated.
> - channel configuration, including Channel profiles,Tx/RX antenna settings
> - For MIMO scenario: SU-MIMO or MU-MIMO, follow agenda item 11.2 for MIMO when available.
> - Precoder assumption
>   - Close loop MIMO (reciprocal beamforming (e.g., SVD, SLR/RZF, etc.), codebook based)
>     - Realistic CSI/SRS/AP-SRS periodicity and delay, and SRS chanEst assumptions,
>     - or genie beamforming
>   - Open loop MIMO
> - Receiver assumption (for MIMO): LMMSE (baseline) for UL, rML or LMMSE for DL
> - LLR demapper: Max-log (baseline) or Log-MAP
> - Channel estimation: Realistic (baseline) or ideal
> - Other assumptions: Channel coding NR-LDPC (baseline), PxSCH bandwidth, SCS, FD interleaver used or not, 5GNR BICM interleaver usage
> - Note: For MIMO, SIMO, MISO and SISO are included when possible

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · `[122-R20-6GR-Modulation, joint channel coding and modulation]`

### RAN1#122 — 9건

**Agreement** · `8.1.2` Specification support for positioning accuracy enhancement · `RAN1#122:8.1.2:005` · 후보

> Include the IE for Rel-19 enhanced measurement (i.e., UL SRS-TDCT, UL SRS-TDCP in 38.215) in higher layer parameter list to RAN3.
> |  | Sub-feature group | RAN3 Parent IE | Parameter name in the spec | New or existing? | Description | Value range | Per (UE, cell, TRP, …) |
> | Rel-19 enhanced measurement | NG-RAN node assisted positioning Case 3b | FFS for RAN3 | FFS for RAN3 | New | Rel-19 enhanced channel measurement, which can be either (a) or (b): (a) UL SRS-TDCT; (b) paired UL SRS-TDCT and UL SRS-TDCP. |  | Per UE |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506437](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506437.zip)

**Agreement** · `8.3.1` SBFD TX/RX/measurement procedures · `RAN1#122:8.3.1:005` · 후보 · 관련 주제: CSI 보고/codebook

> Adopt the following TP in principle to Section 11.1,TS 38.214.
> | 11.1 Slot configuration <omitted text> When the UE is provided sbfd-Configuration2-Transmission, the UE can, - transmit a first PUCCH or PUSCH or a first repetition of a PUCCH or PUSCH, or receive a first PDSCH or a first repetition of a PDSCH, in non-SBFD symbols, and - transmit a second PUCCH or PUSCH or a second repetition of the PUCCH or PUSCH, or receive a second PDSCH or a second repetition of the PDSCH, in SBFD symbols When the UE is provided sbfd-Configuration2-Reception, the UE can, - receive a first PDSCH or a first repetition of a PDSCH in non-SBFD symbols, and - receive a second PDSCH or a second repetition of the PDSCH in SBFD symbols When a UE is not provided sbfd-Configuration2-Transmission, - for a PUCCH or PUSCH transmission with repetitions, or for a PDSCH reception with repetitions, if the first repetition is either in SBFD symbols or in non-SBFD symbols, the remaining repetitions are also either in SBFD symbols or in non-SBFD symbols, respectively - for a Type 2 CG PUSCH transmission, or for a PUSCH transmission with SP-CSI reports, or for a SPS PDSCH reception, if the first transmission or reception after a latest activation is either in SBFD symbols or in non-SBFD symbols, the remaining transmissions or receptions associated with the latest activation are also either in SBFD symbols or in non-SBFD symbols, respectively - for a Type 1 CG PUSCH, or for a PUCCH transmission with SP-CSI reports, or for a PUCCH with SR, [LRR, UEIRI], or P-CSI, or SRS, all respective transmissions are either only in SBFD symbols or only in non-SBFD symbols as indicated by the respective configurations [12, TS 38.331] When a UE is not provided sbfd-Configuration2-Reception, - for a PDSCH reception with repetitions, if the first repetition is either in SBFD symbols or in non-SBFD symbols, the remaining repetitions are also either in SBFD symbols or in non-SBFD symbols, respectively - for a SPS PDSCH reception, if the first reception after a latest activation is either in SBFD symbols or in non-SBFD symbols, the remaining receptions associated with the latest activation are also either in SBFD symbols or in non-SBFD symbols, respectively <omitted text> |
> Note:
> The following misalignments on RRC parameters are identified. It is up to editors to align the RRC parameters.
> | Applicable RAN1 spec | Text in TS 38.21x | Text in TS 38.331 |
> | TS 38.213, 38.214 | sbfd-Configuration2-Transmission | sbfd-Config2-Transmission |
> | TS 38.214 | sbfd-Configuration2-Reception | sbfd-Config2-Reception |
> | TS 38.213 | SBFD-StartingSymbolInd | SBFD-StartingSymbolIndex |
> | TS 38.213 | ulSubbandlocationAndBandwidth | ul-subbandlocationAndBandwidth |
> | TS 38.213 | firstdlSubbandlocationAndBandwidth | firstDL-subbandlocationAndBandwidth |
> | TS 38.213 | seconddlSubbandlocationAndBandwidth | secondDL-subbandlocationAndBandwidth |
> | TS 38.214 | sbfd-Configuration2-PUSCH-RBOffset | sbfd-Config2-PUSCH-RB-Offset |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip)

**Agreement** · `8.3.3` CLI handling · `RAN1#122:8.3.3:002` · 후보 · 관련 주제: CSI 보고/codebook, CSI-RS

> Adopt the following text proposal to section 5.2.1.4.1, TS38.214 in principle.
> | 5.2.1.4.1 Resource Setting configuration *** Unchanged parts are omitted *** For a CSI report associated with semi-persistent or periodic CSI-RS, [or with semi-persistent or periodic SRS-RSRP measurement resources, or with semi-persistent or periodic CLI-RSSI measurement resource, and] if a UE is configured with SBFD symbols and a CSI-ReportConfig with the higher layer parameter symbolType, the UE only considers the CSI-RS occasions within either SBFD symbol(s) or non-SBFD symbol(s) as indicated by symbolType for the CSI derivation for the CSI report. The symbolType configured in CSI-ReportConfig applies to NZP-CSI-RS resources that are associated with the CSI report and configured for both channel measurement and interference measurement. For a semi-persistent or periodic L1-SRS-RSRP or L1-CLI-RSSI measurement resources if a UE is configured with SBFD symbols and a CSI-ReportConfig with the higher layer parameter symbolType, the UE only considers the measurement resources within either SBFD symbol(s) or non-SBFD symbol(s) as indicated by symbolType for the measurement and reporting. If a UE is not configured with SBFD symbols, the higher layer parameter symbolType is not applicable and the UE considers the measurement resources provided in CSI-ResourceConfig indicated by CSI-ReportConfig. |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip)

**Agreement** · `8.3.3` CLI handling · `RAN1#122:8.3.3:003` · 후보 · 관련 주제: Beam management, CSI 보고/codebook, CSI-RS

> Adopt the following text proposal to section 5.2.1.5.2, TS38.214 in principle.
> | 5.2.1.5.2 Semi-persistent CSI/Semi-persistent CSI-RS <-------------------------------- unchanged text omitted -------------------------------> For a UE configured with CSI resource setting(s) where the higher layer parameter resourceType set to 'semiPersistent'. - when a UE receives an activation command, as described in clause 6.1.3.12 of [10, TS 38.321], for CSI-RS resource set(s) for channel measurement, and CSI-IM/NZP CSI-RS resource set(s) for interference measurement and CLI-RSSI/SRS-RSRP for cross-link interference measurement associated with configured CSI resource setting(s), and when the UE would transmit a PUCCH with HARQ-ACK information in slot n corresponding to the PDSCH carrying the selection command, the corresponding actions in [10, TS 38.321] and the UE assumptions (including QCL assumptions provided by a list of reference to TCI-State's, one per activated resource) on CSI-RS/CSI-IM/CLI-RSSI/SRS-RSRP transmission corresponding to the configured CSI-RS/CSI-IM/CLI-RSSI/SRS-RSRP resource configuration(s) shall be applied starting from the first slot that is after slot where m is the SCS configuration for the PUCCH and is the subcarrier spacing configuration for with a value of 0 for frequency range 1 and for FR2-NTN, and is provided by K-Mac or if K-Mac is not provided. If a TCI-State referred to in the list is configured with a reference to an RS configured with qcl-Type set to 'typeD', that RS can be an SS/PBCH block, periodic or semi-persistent CSI-RS located in same or different CC/DL BWP. If the UE is configured with CLI-RSSI-MeasurementResourceSet or SRS-RSRP-MesaurementResourceSet without TCI-State configuration and unifiedTCI-StateType is not configured, the UE shall assume that the activated CLI-RSSI or SRS-RSRP measurement resources are QCL 'typeD' to one of the latest received PDSCH and the latest monitored CORESET. If the UE is configured with CLI-RSSI-MeasurementResourceSet or SRS-RSRP-MesaurementResourceSet without TCI-State configuration and unifiedTCI-StateType is configured, the UE shall assume that the activated CLI-RSSI or SRS-RSRP measurement resources are QCL 'typeD' according to the indicated DL only/joint TCI state. - when a UE receives a deactivation command, as described in clause 6.1.3.12 of [10, TS 38.321], for activated CSI-RS/CSI-IM/CLI-RSSI/SRS-RSRP resource set(s) associated with configured CSI resource setting(s), and when the UE would transmit a PUCCH with HARQ-ACK information in slot n corresponding to the PDSCH carrying the deactivation command, the corresponding actions in [10, TS 38.321] and UE assumption on cessation of CSI-RS/CSI-IM/CLI-RSSI/SRS-RSRP transmission corresponding to the deactivated CSI-RS/CSI-IM/CLI-RSSI/SRS-RSRP resource set(s) shall apply starting from the first slot that is after slot where m is the SCS configuration for the PUCCH and is the subcarrier spacing configuration for with a value of 0 for frequency range 1 and for FR2-NTN, and is provided by K-Mac or if K-Mac is not provided. |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip)

**Agreement** · `8.3.3` CLI handling · `RAN1#122:8.3.3:004` · 후보 · 관련 주제: Beam management, CSI 보고/codebook, CSI-RS

> Adopt the following TP in principle to section 5.2.1.4.1, TS38.214.
> | 5.2.1.4.1 Resource Setting configuration <Unchanged part omitted> For semi-persistent or periodic CSI, each CSI-ReportConfig is linked to periodic or semi-persistent Resource Setting(s): - When one Resource Setting (given by higher layer parameter resourcesForChannelMeasurement) is configured, the Resource Setting is for channel measurement for L1-RSRP, for channel and interference measurement for L1-SINR, or for cross-link interference measurement for L1-SRS-RSRP or for cross-link interference measurement for L1-CLI-RSSI computation. - When two Resource Settings are configured, - if the reportQuantity-r19 is set to 'p-cri-r19', 'p-cri-RSRP-r19', 'p-ssb-index-r19', or 'p-ssb-index-RSRP-r19', the first one Resource Setting (given by higher layer parameter resourcesForChannelMeasurement) is for channel measurement and the second one (given by higher layer parameter resourcesForSetA-r19) is for predicted RS quantities reporting. - otherwise, the first Resource Setting (given by higher layer parameter resourcesForChannelMeasurement) is for channel measurement and the second Resource Setting (given by higher layer parameter csi-IM-ResourcesForInterference) is used for interference measurement performed on CSI-IM. For L1-SINR computation, the second Resource Setting (given by higher layer parameter csi-IM-ResourcesForInterference or higher layer parameter nzp-CSI-RS-ResourceForInterference) is used for interference measurement performed on CSI-IM or on NZP CSI-RS. For periodic L1-CLI-RSSI, each CSI-ReportConfig is linked to periodic Resource Setting for cross-link interference measurement for L1-CLI-RSSI computation. <Unchanged part omitted> |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip)

**Agreement** · `8.3.3` CLI handling · `RAN1#122:8.3.3:005` · 후보 · 관련 주제: Beam management, CSI 보고/codebook, CSI-RS

> Adopt the following TP in principle to section 5.4, TS38.214.
> | 5.4 UE CSI computation time <Unchanged part omitted> Z, Z' and µ are defined as: and , where M is the number of updated CSI report(s) according to Clause 5.2.1.6, corresponds to the m-th updated CSI report and is defined as - of the table 5.4-1 if max{ µPDCCH, µCSI-RS, µUL} ≤ 3 and if the CSI is triggered without a PUSCH with either transport block or HARQ-ACK or both when L = 0 CPUs are occupied (according to Clause 5.2.1.6) and the CSI to be transmitted is a single CSI and corresponds to wideband frequency-granularity where the CSI corresponds to at most 4 CSI-RS ports in a single resource without CRI report and where CodebookType is set to 'typeI-SinglePanel' or where reportQuantity is set to 'cri-RI-CQI', or - of the table 5.4-2 if the CSI to be transmitted corresponds to wideband frequency-granularity where the CSI corresponds to at most 4 CSI-RS ports in a single resource without CRI report and where CodebookType is set to 'typeI-SinglePanel' or where reportQuantity is set to 'cri-RI-CQI', or - of the table 5.4-2 if the CSI to be transmitted corresponds to wideband frequency-granularity where the reportQuantity is set to 'ssb-Index-SINR', 'cri-SINR', 'ssb-Index-SINR- Index ', or 'cri-SINR- Index ', or - of the table 5.4-2 if reportQuantity is set to 'cri-RSRP', 'ssb-Index-RSRP', 'cri-RSRP- Index', 'L1-SRS-RSRP', 'L1-CLI-RSSI' or 'ssb-Index-RSRP- Index ', is according to UE reported capability beamReportTiming and KBl is according to UE reported capability beamSwitchTiming as defined in [13, TS 38.306], or if the CSI report is configured with ltm-CSI-ReportConfig for L1-RSRP measurement, or <Unchanged part omitted> |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip)

**Agreement** · `8.3.3` CLI handling · `RAN1#122:8.3.3:006` · 후보 · 관련 주제: CSI 보고/codebook

> Adopt the following TP to section 3.3 and 5.2.1.4, TS38.214 for alignment.
> | 3.3 Abbreviations For the purposes of the present document, the abbreviations given in TR 21.905 [1] and the following apply. An abbreviation defined in the present document takes precedence over the definition of the same abbreviation, if any, in TR 21.905 [1]. <omitted text> SBFD Sub-bBand non-overlapping fFull dDuplex <omitted text> 5.2.1.4 Reporting configurations <omitted text> A CSI Reporting Setting is said to have a wideband frequency-granularity if <omitted text> - reportQuantity is set to 'cli-SRS-RSRP', or - reportQuantity is set tois set to or 'cli-RSSI' otherwise, the CSI Reporting Setting is said to have a subband frequency-granularity. |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip)

**Agreement** · `8.11.2` Support of RedCap and eRedCap UEs with NR NTN operating in FR1-NTN bands · `RAN1#122:8.11.2:002` · 후보 · 관련 주제: CSI-RS

> The TP below for timeline clarification of case 4 is endorsed for TS38.213
> | Reason for change: The timeline condition for HD-UE on NTN is not correctly captured in current specifications. Summary of change: define the timeline conditions for cancelling PUCCH, PUSCH or SRS for Redcap UE on NTN. Consequences if not approved: unclear UE behaviour 17.2 Half-Duplex UE in paired spectrum <Unchanged parts omitted> A HD-UE that operates on a non-NTN serving cell, or a HD-UE that operates on an NTN serving cell and does not indicate CollisionHandlingOfHDFDDOperation, does not expect to detect a DCI format scheduling a reception in a set of symbols and detect a DCI format scheduling a transmission in any symbol from the set of symbols. A HD-UE that operates on an NTN serving cell in the RRC_CONNECTED state, indicates CollisionHandlingOfHDFDDOperation, is scheduled to receive a PDSCH or CSI-RS in a set of symbols based on an indication by a first DCI format, and is scheduled to transmit a PUSCH, PUCCH, SRS, or PRACH that overlap with any symbol from the set of symbols based on an indication by a second DCI format, determines - to either receive the PDSCH or the CSI-RS or transmit the PRACH based on the HD-UE implementation; - to either receive the PDSCH or transmit the PUSCH, or PUCCH, or SRS based on the HD-UE implementation, if the first DCI format is provided by a PDCCH the HD-UE received according to a Type0/0A/1/2-PDCCH CSS set; - to receive the PDSCH or the CSI-RS if the first DCI format is not provided by a PDCCH the HD-UE received according to a search space set other than a Type0/0A/1/2-PDCCH CSS set, and the HD-UE is not provided ntnRedCapCollisionCase4UlPriority, and the transmission of the PUCCH or the PUSCH would not start before after the last symbol of the PDCCH reception providing the first DCI format timeline conditions for cancellation of the UL transmission as defined in clause 17.2 are satisfied; - to transmit the PUSCH, or PUCCH, or SRS, if the first DCI format is not provided by a PDCCH the HD-UE received according to a Type0/0A/1/2-PDCCH CSS set, and - the HD-UE is provided ntnRedCapCollisionCase4UlPriority, or - the HD-UE is not provided ntnRedCapCollisionCase4UlPriority and the transmission of the PUCCH or the PUSCH would start before after the last symbol of the PDCCH reception providing the first DCI format timeline conditions for cancellation of the UL transmission as defined in clause 17.2 are not satisfied. A HD-UE that operates on an NTN serving cell in the RRC_CONNECTED state, indicates CollisionHandlingOfHDFDDOperation, is scheduled to receive a PDSCH or CSI-RS based on an indication by a first DCI format, and is scheduled to transmit an SRS based on an indication by a second DCI format and the transmission of the SRS in a set of symbols overlaps with the PDSCH reception or CSI-RS reception, determines - to either receive the PDSCH or transmit the SRS based on the HD-UE implementation, if the first DCI format is provided by a PDCCH the HD-UE received according to a Type0/0A/1/2-PDCCH CSS set; - to receive the PDSCH or the CSI-RS if the first DCI format is not provided by a PDCCH the HD-UE received according to a Type0/0A/1/2-PDCCH CSS set, and the HD-UE is not provided ntnRedCapCollisionCase4UlPriority, and the first symbol from the set of symbols is not before after the last symbol of the PDCCH reception providing the first DCI format; - to transmit the SRS if the first DCI format is not provided by a PDCCH the HD-UE received according to a Type0/0A/1/2-PDCCH CSS set, and - the HD-UE is provided ntnRedCapCollisionCase4UlPriority, or - the HD-UE is not provided ntnRedCapCollisionCase4UlPriority and any symbol from the set of symbols is before after the last symbol of the PDCCH reception providing the first DCI format <Unchanged parts omitted> |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506527](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506527.zip)

**Agreement** · `8.14` Maintenance on R19 TEI · `RAN1#122:8.14:004` · 후보

> Send LS to RAN3 and cc RAN2 taking the following as Overall description,
> RAN1 thanks RAN3 for the question.
> RAN1 has discussed this matter and agreed that no additional LMF requirements are to be provided to the gNB in requesting the UL SRS configuration with or without SRS frequency hopping for the non-RedCap UEs.
> as well as taking the following as Action
> RAN1 respectfully requests RAN3 to take above feedback into consideration.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506610](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506610.zip) · `[121-R19-TEI]`
