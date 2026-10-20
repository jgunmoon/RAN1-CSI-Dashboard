# CSI 보고/codebook — RAN1 CSI 결정

> 원본 DB 마지막 업데이트 **2026-10-19 20:12 KST** · [요약으로 돌아가기](../README.md)

주된 주제가 CSI 보고/codebook인 확정 128건 (Agreement 117 · WA 1 · Conclusion 10), 후보 104건. 결정 본문은 Chair notes 원문 그대로입니다(요약 없음). 최신 회의부터 보여줍니다.
주된 주제가 다른 결정 중 이 주제가 관련 주제로 붙은 것은 맨 아래 '관련 결정'에 모았습니다.

## RAN1#126bis — 16건

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#126bis:9.2:004` · 🆕 신규 · 관련 주제: CSI-RS

> On MAC-CE triggering indication for early CSI/CSI-RS based on a SCell activation command, study the following alternatives and down-select one in RAN1#127:
> - Alt-1: Indicating a CSI report configuration for each SCell activated by the SCell activation command MAC-CE.
>   - FFS: The CSI reporting configuration for a SCell is configured in the SCell itself or the serving cell which sends the SCell activation command MAC-CE
> - Alt-2: Indicating a single CSI trigger state in the SCell activation command MAC-CE.
>   - Note: CSI trigger state(s) and CSI reporting configuration(s) is configured in the serving cell which sends the SCell activation command MAC-CE.
>   - Note: UE determines the serving cell(s) which the associated CSI-RS is triggered for, via carrier configured in the CSI report configuration(s), where the CSI report configuration(s) is determined according to the CSI trigger state indicated in the MAC-CE
>   - FFS: Whether/How to restrict CSI reporting is triggered only for the SCell(s) activated by the SCell activation command MAC-CE
> - Alt-3: Indicating a new CSI trigger state for each SCell activated by the SCell activation command MAC-CE.
>   - The new CSI trigger state(s) for each SCell activated by the SCell activation command MAC-CE is configured in the SCell itself
>   - Note: It is not legacy CSI trigger state.

남은 FFS 2건

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · [R1-2607054](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2607054.zip) · `[126bis-R20-MIMO]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126bis:10.5.3.1:001` · 🆕 신규

> For the 6GR CJT report to facilitate CJT deployment,
> - Study whether/how to support reporting CJTC delay offset report and codebook-based CSI (with NTRP>1) assuming TRP/panel-specific SD basis selection and TRP/panel-common FD basis selection (if applicable), including:
>   - Linkage between separate xTRP delay offset report and codebook-based CSI report, whether jointly or separately triggered
>     - The two reports can be reported in a same reporting occasion or two different reporting occasions
>   - NW indication of delay offset that UE assumes in codebook-based CSI calculation
>   - Delay offset is reported together with codebook-based CSI report in one report, whether
>     - as a part of codebook-based CSI report, e.g., analogous to Rel-18 CJT CSI Mode-1, or
>       - FFS: precoder frequency granularity due to the delay offset
>     - not as a part of codebook-based CSI report (in one report, e.g., ri-pmi-cqi-Dd)

남은 FFS 1건

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126bis:10.5.3.1:002` · 🆕 신규

> For the study of the 6GR codebook design for CSI report, regarding the SD basis selection for the high-resolution scheme, regarding candidate L values
> - For Option 2, L>=1 Layer-specific/layer-group-specific SD basis selection, consider at least L= {1, 2} for evaluation
>   - Further down-selection on the candidate L values is possible
> - For Option 3, L>1 Layer-common SD basis selection, consider at least L= {2, 4, 6} for evaluation
>   - Further down-selection on the candidate L values is possible
> Note:
> - For DFT basis, L represents the number of DFT basis analogous to legacy Type-II
> - For non-DFT basis generated from combinations of DFT basis, L represents the number of combined non-DFT basis, and each non-DFT basis is constructed from a combination of L1 DFT basis. Companies report the number of L1.
> - For port-selection basis, L represents the number of port-selection basis analogous to legacy Type-II Port Selection
> Note: the above doesn’t mean Option 1 is down-selected.

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126bis:10.5.3.1:005` · 🆕 신규 · 관련 주제: CSI-RS

> For 6GR CSI-RS, to study the threshold X on whether M1 is larger than 1, and the detailed (M1, M2) values, the following aspects need to be considered
> - Channel coherent time or coherent bandwidth
> - UE buffering size
> - CSI-RS sharing use case 1 from either NW or UE point of view
> - Multiplexing with other DL channels/signals
> - UE CSI processing complexity
> - Frame structure

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126bis:10.5.3.1:006` · 🆕 신규 · 관련 주제: CSI-RS

> For 6GR CSI-RS study, the following template is adopted to collect evaluation results for CSI-RS pattern design
> | Parameters | Parameters | Company A |
> | Simulation assumptions | Carrier frequency |  |
> | Simulation assumptions | Numerology |  |
> | Simulation assumptions | Traffic model |  |
> | Simulation assumptions | RB allocation for PDSCH |  |
> | Simulation assumptions | Channel BW |  |
> | Simulation assumptions | Channel model |  |
> | Simulation assumptions | Delay spread |  |
> | Simulation assumptions | UE speed |  |
> | Simulation assumptions | BS antenna configuration |  |
> | Simulation assumptions | UE antenna configuration |  |
> | Simulation assumptions | MIMO Tx scheme, including MU or SU MIMO |  |
> | Simulation assumptions | PRG |  |
> | Simulation assumptions | Link adaptation |  |
> | Simulation assumptions | MCS |  |
> | Simulation assumptions | Channel estimation |  |
> | Simulation assumptions | CSI codebook type, and further details |  |
> | Simulation assumptions | CSI subband size |  |
> | Simulation assumptions | CSI periodicity and delay |  |
> | CSI-RS parameters | CSI-RS periodicity |  |
> | CSI-RS parameters | CSI-RS power boost |  |
> | CSI-RS parameters | Precoding CSI-RS specific parameters, e.g., precoder of CSI-RS, QCL assumption |  |
> | CSI-RS parameters | CSI-RS sharing use case (use case 1, 2 or others) |  |
> | CSI-RS parameters | Parameters for CSI-RS sharing use case (e.g., For case 1: Level 1, 2-1, or 2-2, port sampling method, etc For case 2: Alt 1 or 2, etc) |  |
> | CSI-RS parameters | CDM size and CDM type |  |
> | CSI-RS parameters | (M1, M2, Y) |  |
> | CSI-RS parameters | CSI-RS RE allocation option (Option 1-1 or Option 1-2) |  |
> | CSI-RS parameters | CDM mapping order (Option 2-1 or Option 2-2) |  |
> | CSI-RS parameters | Port mapping description |  |
> | CSI-RS parameters | Detailed CSI-RS RE locations (Starting RE index for each CDM group within each RB set) |  |
> | Performance | KPI (BLER, TPUT/SE, UPT) |  |
> | Performance | Observation |  |

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126bis:10.5.3.1:007` · 🆕 신규 · 관련 주제: CSI-RS

> For 6G CSI-RS sequence design, the following template is adopted to collect evaluation results
> | Parameters | Parameters | Company A |
> | Simulation assumptions | Carrier frequency |  |
> | Simulation assumptions | Numerology |  |
> | Simulation assumptions | Traffic model |  |
> | Simulation assumptions | RB allocation for PDSCH |  |
> | Simulation assumptions | Channel BW |  |
> | Simulation assumptions | Channel model |  |
> | Simulation assumptions | Delay spread |  |
> | Simulation assumptions | UE speed |  |
> | Simulation assumptions | BS antenna configuration |  |
> | Simulation assumptions | UE antenna configuration |  |
> | Simulation assumptions | SNR range |  |
> | Simulation assumptions | SIR range |  |
> | Simulation assumptions | MIMO Tx scheme, including MU or SU MIMO |  |
> | Simulation assumptions | PRG |  |
> | Simulation assumptions | Link adaptation |  |
> | Simulation assumptions | MCS |  |
> | Simulation assumptions | Channel estimation (including WB or SB channel estimation) |  |
> | Simulation assumptions | CSI codebook type, and further details |  |
> | Simulation assumptions | CSI subband size |  |
> | Simulation assumptions | CSI periodicity and delay |  |
> | CSI-RS parameters | CSI-RS periodicity |  |
> | CSI-RS parameters | CSI-RS power boost |  |
> | CSI-RS parameters | Precoding CSI-RS specific parameters, e.g., precoder of CSI-RS, QCL assumption |  |
> | CSI-RS parameters | CDM size and CDM type |  |
> | CSI-RS parameters | (M1, M2, Y) |  |
> | CSI-RS parameters | Detailed CSI-RS RE locations (Starting RE index for each CDM group within each RB set) |  |
> | CSI-RS parameters | Port mapping description |  |
> | CSI-RS parameters | PAPR option (Option 1-5), and further details (if needed) |  |
> | CSI-RS parameters | Inter-cell option, and further details (if needed) |  |
> | PAPR | PAPR observation |  |
> | Performance | KPI (AC, XC, BLER, TPUT/SE, UPT) |  |
> | Performance | Performance observation |  |

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126bis:10.5.3.1:008` · 🆕 신규 · 관련 주제: CSI-RS

> On the pattern for CSI-IM in 6G, both pattern 0 (2x2 resource grid) and pattern 1 (4x1 resource grid) defined in 5G NR are considered as baseline.
> - FFS in frequency domain, whether CSI-IM needs to appear in all the RBs associated with the CSI report
> - FFS in time domain, whether CSI-IM needs to appear in one or more slots when M1>1 for the associated CSI-RS

남은 FFS 2건

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126bis:10.5.3.1:010` · 🆕 신규 · 관련 주제: CSI-RS

> - For 6G CSI-RS study, assuming different cells use different scrambling IDs for sequence initialization, identify the cases where inter-cell interference issue caused by NR CSI-RS sequence mapping impacts PMI calculation considering the following
> - In the case of wideband channel estimation or subband channel estimation
> - The SIR level that impacts PMI calculation
> - In the identified cases (if any), study the following options to address the potential inter-cell interference issue caused by NR CSI-RS sequence mapping
> - Inter-cell Option 1: Sequence randomization in time domain
> - Inter-cell Option 2 (same as PAPR Option 2): Map the PN sequence to the global subcarrier indices in the whole bandwidth sequentially
> - Inter-cell Option 3 (same as PAPR Option 3): Multiply the PN sequence with an additional CDM group-specific scrambling sequence
> - Inter-cell Option 4 (same as PAPR Option 4): Multiply the PN sequence with an additional port-specific scrambling sequence
> - Inter-cell Option 5: CDM group-specific sequence initialization
> - Inter-cell Option 6: Port-specific sequence initialization
> - Inter-cell Option 7: OCC-specific scrambling
> - Inter-cell Option 8: OCC-specific sequence initialization
> - Note: combination of the above options can be considered

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126bis:10.5.3.1:011` · 🆕 신규 · 관련 주제: CSI-RS

> For the evaluation of configurable/downloadable codebook/basis, at least the following can be considered:
> - Number of bases indicated/configured
>   - For the number of SD bases for evaluation,
>     - For UE-specific SD bases and/or FD bases (if appliable) for evaluation considering:
>       - {2, 4, 6, 8, 16} for SD bases
>       - Ceil(y*N3), where y = {1/8, 1/4} for FD bases
>     - For cell-specific SD bases and/or FD bases (if appliable) for evaluation considering:
>       - Ceil(x*N1N2), where x = {1/8, 1/4, 1/2, 1, 4, 16} for SD bases
>       - Ceil(z*N3), where z = {1/4, 1/2, 1} for FD bases
>     - Note the joint SD-FD bases is discussed separately
>   - For the update periodicity of the bases:
>     - For UE-specific SD bases and/or FD bases (if appliable) for evaluation considering:
>       - 40ms, 100ms, 200ms, 400ms, 800ms
>     - For cell-specific SD bases and/or FD bases (if appliable), assuming no update on basis during the simulation time
>     - Note the joint SD-FD bases is discussed separately
>   - Note: other values can be reported by companies.
>   - Companies report the orthogonality assumption of the downloadable basis
>   - The definitions of N1, N2, and N3 are analogous to 5G NR
>   - For PMI reporting, UE can further select the bases for CSI report
> - Types of basis for option 2A
>   - Option-1: Only SD base;
>     - Note: the FD bases are determined by UE based on a set of DFT bases (if applicable)
>   - Option-2: Both SD and FD bases
>   - Note: UE can further select the basis for CSI report
> - Format and representation/quantization of basis for evaluation
>   - Option-1: a subset of DFT bases
>   - Option-2: the combination of multiple DFT bases
>   - Option-3: the combination of multiple port selection bases
> - Companies report the UE buffer of the codebook/basis
> - Note: both non-precoded CSI-RS and precoded CSI-RS can be considered

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126bis:10.5.3.1:012` · 🆕 신규

> For the evaluation of explicit CSI feedback, the compression method, at least considering the following:
> - Option 1: the same structure of high-resolution with the following on top of the codebook design for implicit CSI,
>   - Study the following as the form of explicit CSI for compression:
>     - Opt-1a: Per-Rx spatial-frequency Nt-by-Nf channel matrix
>     - Opt-1b: both the diagonal and off-diagonal elements of the channel covariance matrix H’H, where H is Nr-by-Nt channel matrix
>     - Opt-1c: The eigenvector(s) of the channel covariance matrix H’H, or right singular vector(s) of H, where H is Nr-by-Nt channel matrix
>       - Note: additional eigen/singular value(s) are to be reported
>     - Opt-1d: The eigenvector(s) of the channel covariance matrix H’H, and the eigenvector(s) of the channel covariance matrix HH’, where H is Nr-by-Nt channel matrix
>       - Note: additional information to represent the phase(s) corresponding to pair(s) of Tx-Rx eigenvectors and the corresponding eigen values are to be reported
>   - Additional component for reporting channel power(s), if needed.
>     - Companies report the definition on channel power(s), e.g., per-rx channel power or channel power of whole matrix
>   - SD basis selection:
>     - Option-a: orthogonal basis selection
>     - Option-b: non-orthogonal basis selection
>     - For Opt-1a, study Rx-common/Rx-specific basis selection
>   - Wf-structure:
>     - For Opt-1a, study Rx-common/Rx-specific basis selection
>   - Companies report whether compression over Rx ports is assumed or not in the simulation.
> - Option 2: AI-based CSI compression for the channel matrix H or H’H.
> - Option 3: QR decomposition with givens rotation of the channel matrix H or H’H
> - Option 4: Based on DFT basis and corresponding projection powers for H’H
> - Companies report the basis assumption, e.g., fixed basis or downloadable basis, when applicable
> - Companies report the frequency granularity unit (finer than wideband)

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126bis:10.5.3.1:014` · 🆕 신규

> For the evaluation on UE-initiated or event-triggered CSI reporting, the quantity for event definition
> - For CQI based event definition (under the condition of unchanged PMI/RI assumption),
>   - companies report CQI calculation assumption (WB or SB CQI), the assumed codebook, and corresponding reference RS, event definition (e.g., variation of the most recently computed quantity compared to the most recently reported/calculated one above a threshold), and event-triggered CSI report quantities.
> - For RI based event definition
>   - companies report details, e.g., event definition (e.g., variation of the most recently computed quantity compared to the most recently reported/calculated one above a threshold), and event-triggered CSI report quantities.
> - For other quantities-based event definition, e.g., PMI, SINR, channel property information, companies report corresponding details
> - Companies report the event-check periodicity and the overhead assumed for the event indication and the assumption on the reporting mechanism and latency for the event-triggered CSI reporting.
> For the evaluation on event-triggered CSI reporting configuration selection/adaptation by the UE, e.g., based on channel property information, companies report corresponding details.

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of DL based CSI acquisition]`

**Conclusion** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126bis:10.5.3.1:019` · 🆕 신규

> For study on PAPR reduction for JSCM-based CSI compression, deprioritize Option 0 without any subsequent nonlinear operation for PAPR reduction.
> - Note: Option 0 with subsequent nonlinear operation for PAPR reduction may be similar as Option 2 depending on the design of the nonlinear operation

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126bis:10.5.3.1:020` · 🆕 신규

> For the study on necessity and benefit of reliability verification for JSCM-based CSI compression, study on at least the following:
> - The purpose for reliability verification: it can be used by the NW to determinate whether to use the reconstructed CSI based on per JCSM-based CSI report
>   - FFS the applicability to NW side performance monitoring/for LCM/error cause detection, and relationship with reliability verification (if appliable)
> - The potential solutions, at least considering
>   - Opt 1: with additional redundancy
>     - Opt 1A: bit-level redundancy generated from the target CSI, e.g., perceptual Hashing, codebook-based, CRC-based
>       - Whether the bit-level redundancy to be transmitted using conventional channel coding/modulation
>     - Opt 1B: symbol-level redundancy generated directly (without considering bit level quantization) from the target CSI or compressed CSI output
>     - Opt 1C: bit-level redundancy generated based on compressed CSI output symbols
>       - Whether the bit-level redundancy to be transmitted using conventional channel coding/modulation
>     - Opt 1D: symbol-level redundancy based on pre-known/configured signals inserted as the target input for compression, e.g., reference CSI
>     - Opt 1E: a metric reported by UE, e.g., SGCS, generated based on target CSI and pre-known/configured reference CSI
>       - Whether the metric to be transmitted using conventional channel coding/modulation
>   - Opt 2: without additional redundancy (NW implementation-based)
>     - Option 2A: based on the estimated UL SINR,
>     - Option 2B: based on the comparison of the received (post-equalization) JSCM symbols () and the recompressed symbols (, where A is the projection matrix) from the reconstructed CSI ()
>   - Other options or combinations of the above options are not precluded
> - The impact on UPT (and SGCS intermediate) performance due to overhead (if any) of introducing reliability verification
> - To evaluate the performance benefit(necessity) of above,
>   - Study the scenarios where reliability verification has potential benefit
>   - companies report the performance benefit, e.g., SGCS, link-level throughput
>   - companies report along with the reliability verification, how NW determinate the precoder (e.g., fall back to previous report, NW side model selection),
>   - companies report the details on how to identify the reliability issue.

남은 FFS 1건

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126bis:10.5.3.1:022` · 🆕 신규

> For the study of CSI reporting and AI-based CSI compression, adopt the templates in the following documents for collecting companies’ results.
> - 10.5.3.1 Simulation results for CSI report.xlsx in R1-2608772
> - 10.5.3.1 Simulation results for AI-based CSI report.xlsx in R1-2608772
> Note: additional separate templates can be added.

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.3` Other aspects · `RAN1#126bis:10.5.3.3:005` · 🆕 신규

> Study and evaluate the following assistance information for sub use case 1A
> - Channel covariance matrix/spectrum
>   - The form agreed in AI10.5.3.1 can be used for reporting
> - Precoding matrix index reporting, e.g., via NR R16 eType II codebook
> - Explicit channel information

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Other Aspects related to CSI]`

**Agreement** · `10.5.3.3` Other aspects · `RAN1#126bis:10.5.3.3:010` · 🆕 신규

> For the study of other aspects related to CSI, adopt the templates in the following documents for collecting companies’ results.
> - Simulation results for joint DL and UL CSI acquisition_template_v1.xlsx in R1-2607650
> - Simulation results for RS for finer time and frequency tracking_template_v1.xlsx in R1-2607650

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Other Aspects related to CSI]`

## RAN1#126 — 12건

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#126:9.2:001` · 관련 주제: CSI-RS

> In SIBx configuration for early aperiodic CSI reporting and associated CSI-RS, when UE transition from IDLE/INACTIVE to CONNECTED mode:
> - Only one CSI-RS resource set is provided in a CSI resource configuration for channel measurement; and
> - Only one CSI-IM resource set is provided in a CSI resource configuration for CSI-IM based interference measurement

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606464](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606464.zip) · `[126-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#126:9.2:005`

> For aperiodic CSI reporting triggered based on a SCell activation command, on how to determine the serving cell where the PUSCH for the aperiodic CSI reporting is transmitted in, support Alt-1, i.e., PUSCH must be scheduled for transmission in the serving cell from which the SCell activation command is received.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606465](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606465.zip) · `[126-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#126:9.2:010` · 관련 주제: CSI-RS

> For aperiodic CSI reporting associated with aperiodic CSI-RS triggered by MAC-CE in MSG4 when UE transition from IDLE/INACTIVE to CONNECTED mode, support the followings to define the corresponding timeline for UE CSI computation:
> - The duration between the starting symbol and the first symbol of PUSCH carrying the aperiodic CSI report should satisfy the legacy CSI computation  delay requirement.
>   - The starting symbol is the first symbol of the first slot that is 3ms after UE transmits HARQ-ACK for the MSG4 PDSCH carrying the MAC-CE.
> - The duration between the last symbol among the associated CSI-RS resource(s) for channel and associated CSI-IM resource for interference measurement and the first symbol of PUSCH carrying the aperiodic CSI report should satisfy the legacy CSI computation  delay requirement.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606466](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606466.zip) · `[126-R20-MIMO]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126:10.5.3.1:001`

> For the 6GR codebook design for CSI report, study a W1W2 only structure for the low-resolution scheme with the following considerations at least for RI=1-4:
> - W1-structure
>   - SD basis
>     - NR oversampled 2D-DFT basis is a baseline
>       - FFS on other basis, e.g., basis constructed from combined 2D DFT beams
>       - FFS on alphabet set for combination coefficients for the basis constructed from combined 2D DFT beams
>   - SD basis selection
>     - eType-I Scheme-B like unrestricted orthogonal DFT beam selection in 2D direction is a baseline
>       - FFS on orthogonal basis selection in at least 1D direction, or non-orthogonal basis selection
>     - Layer-specific/layer-group-specific SD basis selection
>       - FFS on basis-to-layer (layer-group) mapping, e.g., ordering or no ordering
>       - FFS on the maximum number of SD basis vector selection
> - W2-structure
>   - Layer-specific/layer-group-specific inter-polarization co-phase selection
>     - FFS: inter-polarization amplitude
>   - Alphabet set for inter-polarization co-phase: BPSK, QPSK
>     - FFS: details for each rank
>     - FFS: for WB, whether to consider or not 8-PSK in addition to BPSK and QPSK
> - FFS on RI>4
> - Strive for having a unified codebook scheme for all supported ranks by 6G
> - FFS: details on whether/how to accommodate passive array with smaller number of ports
> - Note: UE implementation complexity is to be considered in the design of SD-basis and co-phasing selection, including the number of candidate combinations and the associated search complexity.
> - Note: CBSR discussion will be discussed separately
> - Note: For discussion of low resolution scheme, eType-1 Scheme-A and eType-II with L=1 are precluded

남은 FFS 10건

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of DL based CSI acquisition]`

**Conclusion** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126:10.5.3.1:002`

> For the 6GR codebook design for CSI report, for discussion purposes, based on the previous agreements, the following separate category is used:
> - Category for resolution: low- and high-resolution, comprising at least the following criteria:
>   - Target scenario (e.g., SU-MIMO, MU-MIMO)
>   - Feedback overhead
>   - UE complexity in CSI calculation

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126:10.5.3.1:004` · 관련 주제: CSI-RS

> For CSI-RS for CSI acquisition in 6GR, design on CSI-RS and CSI assumes the maximum number of CSI-RS ports is 256.
> - Final decision on the maximum number of CSI-RS ports (128, 256 or 512) is to be made in RAN1#127

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126:10.5.3.1:012`

> For the evaluation on downloadable/configurable codebook/basis for CSI report, the following is considered additionally on top of the agreement in RAN 1 #125:
> - Type-I-like scheme:
>   - Option-1A:
>     - , where  is a 2N1N2-dimensional precoding vector for layer , and  is the number of layers
>     - is determined by UE from a downloadable/configurable codebook, and company reports the size of the downloadable/configurable codebook
>   - Option-1B:,
>     - ,  is a N1N2-dimension SD basis for layer
>     - (wideband) is determined by UE from a downloadable/configurable SD basis set, and company reports the size of the downloadable/configurable SD basis set
>     - W2 is either SB or WB
> - Type-II-like scheme:
>   - Option-2A: ,
>     - (wideband) is determined by UE from a downloadable/configurable SD basis set for layer , and/or  is determined by UE from a downloadable/configurable FD basis set, and L is the number of selected SD basis
>     - Note: if FD basis set is not based on downloadable/configurable FD basis set, DFT FD basis set is assumed in the simulation.
>   - Option-2B: ,
>     - (wideband) is determined by UE from a downloadable/configurable SD-FD basis pair set for layer l, and L is the number of selected SD/FD basis vector pairs
> - Companies report the basis/precoding vector quantization assumption, if applicable
> - Companies report how the NW determines downloadable/configurable basis/codebook
> - Companies report the orthogonality of the downloadable/configurable basis/ precoding vector and the assumption for basis/ precoding vector selection (whether the selection is layer-common or layer-specific)
> - Strive to have common codebook structure with fixed codebook, if applicable
> - Companies are encouraged to compare with fixed codebook as well as AI-based CSI compression

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126:10.5.3.1:013`

> For the 6GR codebook design for CSI report, study a W1W2Wf structure as a starting point for the high-resolution scheme with the following considerations for RI=1-4:
> - W1-structure
>   - SD basis
>     - NR oversampled 2D-DFT basis is a baseline
>       - FFS on other basis
>       - FFS on alphabet set for combination coefficients for the basis constructed from combined 2D DFT beams
>   - SD basis selection
>     - Down-select from the following options:
>       - Opt1. L=1 only, Layer-specific/group-specific SD basis selection
>       - Opt2. L≥1 Layer-specific/group-specific SD basis selection
>       - Opt3. L>1 Layer-common SD basis selection
>     - eType-II orthogonal DFT beam selection in 2D direction is a baseline
>       - FFS orthogonal basis selection in at least 1D direction
>       - FFS non-orthogonal L basis selection, e.g., basis vector- specific (q1, q2) selection
>       - FFS orthogonal L basis selection, non-orthogonal basis selection across different layers, e.g., orthogonal DFT beam selection in 2D direction for each layer with layer-specific (q1, q2) selection
>       - FFS whether/how to further optimize SD basis selection, e.g., using layer-common in combination with layer-specific/layer group-specific
> - FFS whether to consider RI>4
> - Wf-structure
>   - eType-II layer-specific FD basis selection as a baseline
>     - FFS on whether/how to further optimize FD compression, e.g., delay-domain pre-alignment per-basis prior to FD compression
> - W2-structure
>   - Linear combining (LC) coefficient scheme (ref/diff amps, phase, SCI) analogous to Rel-16 NR eType-II as a starting point
>     - FFS: details on alphabet sets on LC coefficients
>   - Whether to support bitmap for indicating the location of NZCs as well as a parameter for the maximum number of NZCs
> - FFS parameter combination (PC) design
> - Note: UE implementation complexity is to be considered in the design of SD-basis selection, including the additional complexity of inter-layer interference mitigation for layer-specific schemes.

남은 FFS 10건

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126:10.5.3.1:015`

> For evaluation on CPI reporting in SD/FD/TD, study the following options of form of CPI:
> - Option 1: Channel covariance matrix/spectrum, e.g., ,  in form of basis matrix and associated coefficients and/or power, wherein  is in port/frequency domain
>   - FFS: Whether orthogonal or non-orthogonal bases are used for compression
>   - FFS: Whether off-diagonal coefficients in additional to diagonal coefficients of full or subset of
>   - FFS: Whether CPI in SD/FD/TD domains are reported separately or jointly
> - Option 2: Channel covariance matrix in form of quantization of decomposed channel covariance matrices, e.g., EVD, QR
> - Option 3: Normalized correlation
>   - FFS: whether CPIs in different domains are reported separately or jointly
> - Option 4: Channel matrix (utilizing the explicit CSI report)
> - Option 5: Explicit system parameter, e.g., codebook parameter, RS parameter.
> Companies to provide details of applicable use cases for the above options.
> Companies report calculation assumption of the channel covariance matrix/spectrum, e.g., average over time domain, average over frequency domain, average over spatial domain.
> Note: Strive for common report quantities for use cases for a certain domain, if applicable.

남은 FFS 4건

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126:10.5.3.1:019` · 관련 주제: CSI-RS

> For evaluation on precoded CSI-RS without considering CSI-RS overhead reduction:
> - Assume cell-specific wideband precoded CSI-RS, e.g., the number of precoded CSI-RS ports is same as the number of TXRUs at aNB
> - Company reports the precoder of CSI-RS, and information/how to determinate the precoder.
> - The following CSI feedback scheme can be considered for the evaluation:
> - Option 1: Type I-like (W1W2) and/or eType II-like (W1W2Wf) CSI reporting with port-selection (PS) basis
> - Option 2: Type I-like (W1W2) and/or eType II-like (W1W2Wf) CSI reporting with NR DFT basis with reconstruction information
> - Option 3: Type I-like (W1W2) and/or eType II-like(W1W2Wf) CSI reporting with NR DFT basis (CSI-RS port precoder is transparent to UE)
> - Company report how NW utilized the reported CSI for PDSCH precoder determination.
> - FFS on other basis, e.g., the basis constructed from combined 2D DFT beams/ port-selection (PS) basis
> - Benchmark:
>   - Type I and eType II codebook with non-precoded CSI-RS
> Companies report the QCL related assumptions
> Note: Precoded CSI-RS with less density in spatial domain is to be discussed separately.
> Note: downloadable basis/precoder (e.g. FD basis/precoder associated with each precoded CSI-RS port) can be considered additionally with precoded CSI-RS and the assumption/consideration for downloadable basis is taken into account
> Note: the PAPR issue of precoded CSI-RS is to be studied.

남은 FFS 1건

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126:10.5.3.1:021` · 관련 주제: CSI-RS

> For the evaluation on PDSCH DMRS-based CSI for PDSCH link adaptation, the following is consideration:
> - For channel measurement, the DMRS port(s) associated with data is considered as the baseline
>   - FFS on whether to consider DMRS port(s) allocated with PDSCH but not associated with the data
> - For interference measurement (when needed), company to report how to acquire interference information.
> - Company to report the UE assumptions for DMRS-based CSI calculation.
> - Email discussion for the templates and collect results for the use cases, e.g., fixed codebook, AI-CSI, CPI, downloadable/configurable codebook/basis, DMRS-based CSI, precoded CSI-RS.

남은 FFS 1건

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.3` Other aspects · `RAN1#126:10.5.3.3:003`

> For the evaluation of joint DL/UL based CSI acquisition, additionally consider the following KPIs
> - UPT
> - Intermediate KPI (e.g., SGCS, NMSE)
> - RS overhead
> - Feedback overhead
> - Computation complexity and model complexity, if any
> - Storage complexity, if any

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Other Aspects related to CSI]`

## RAN1#125 — 11건

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#125:9.2:005` · 관련 주제: CSI-RS

> For aperiodic CSI-RS associated with aperiodic CSI reporting triggered by MAC-CE in MSG4, support Option-2, i.e.,
> - If the aperiodic CSI-RS is triggered along with an aperiodic TRS by the same MAC-CE in MSG4 and the aperiodic TRS is transmitted before the aperiodic CSI-RS , the CSI-RS is QCLed Type-A with the triggered aperiodic TRS; otherwise, the CSI-RS is QCLed Type-C with the SSB the UE identified during the random access procedure when UE transition from IDLE/INACTIVE to CONNECTED mode.
> Note: Whether to have time gap requirement between aperiodic CSI-RS and aperiodic TRS is separately discussed

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2603722](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2603722.zip) · `[125-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#125:9.2:008` · 관련 주제: CSI-RS

> For MSG4-triggered aperiodic TRS when UE transition from IDLE/INACTIVE to CONNECTED mode, the MAC-CE in MSG4 can indicate triggering of one or two TRS burst(s).
> - In SIBx, only one CSI resource set for tracking is provided in the CSI resource configuration for aperiodic TRS
> - FFS: Whether the gap between two TRS bursts is configured in SIBx or indicated in MAC-CE

남은 FFS 1건

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2605114](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2605114.zip) · `[125-R20-MIMO]`

**Conclusion** · `9.2` NR MIMO Phase 6 · `RAN1#125:9.2:010` · 관련 주제: CSI-RS

> For CSI-RS frequency-domain densities ρ = 1/3 and 1/6, there is no RAN1 consensus to support the following new CSI subband sizes for different BWP sizes.
> | Bandwidth part size (PRBs) | CSI subband size (PRBs) |
> | 24-72 | 12 |
> | 73-144 | 6 |
> | 145-275 | 30 |

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2605114](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2605114.zip) · `[125-R20-MIMO]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#125:10.5.3.1:004`

> Support at least codebook based implicit CSI feedback in 6GR.
> Study whether/how to support explicit CSI feedback, including at least the following aspects:
> - Reporting quantities/format, including compression/quantization methods
>   - e.g., full channel matrix, channel covariance matrix, eigenvector(s) with eigenvalue(s)
> - Companies to provide reporting overhead, instance assumption for channel covariance matrix, performance and complexity analysis, and assumption for link adaptation and other reference signal (if applicable)
> - Note: both sTRP and mTRP can be considered
> - Note: Both AI and non-AI based solution for CSI feedback can be considered.
> - Note: The related testability issue is up to RAN 4.
> - Note: LS to RAN 4 is to be considered for RAN 4 testability issues, when mature.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#125:10.5.3.1:006` · 관련 주제: CSI-RS

> For the 6GR codebook design for CSI report, the following is considered:
> - NR fixed DFT basis is used as a baseline for evaluation for W1 and Wf  at least for non-precoded CSI-RS
>   - For cell-specific precoded CSI-RS, port-selection basis and/or NR DFT basis can be used as a baseline for evaluation
>   - FFS on other basis, e.g., for near field, basis combined from DFT beams/port selection, and non-orthogonal DFT basis
> - Low- resolution scheme:
>   - Max RI=8 as a baseline for evaluation
>   - Candidate structures include Type-I Scheme-A like (W1 W2), Type-I Scheme-B like (W1 W2), eType-II like L=1 (W1 W2 Wf) structures
>     - For eType-II like L=1, layer-specific/layer-group-specific SD basis selection
>     - Other candidate schemes are not precluded
>   - FFS: details on whether/how to accommodate passive array with smaller number of ports
> - High- resolution scheme:
>   - Max RI=4 as a baseline for evaluation
>   - eType-II L>1 (W1 W2 Wf) structure as a baseline for evaluation (including implicit and explicit feedback)
>   - Note: Whether/how to use this for explicit channel feedback is not precluded.
> - For both low- and high-res, CJT codebook with NTRP>1 TRPs/panels
>   - TRP/panel specific SD basis selection, TRP/panel common FD basis selection (if applicable) as a baseline for evaluation
>   - Study whether/how to support dynamic TRP/panel selection mechanism
>   - Company reports the multi-TRP/panel assumption, e.g., co-located, non-co-located
>   - Note: The term “TRP” and “panel” are used for discussion purposes
> Note: Additional details are still to be studied, including enhancements for UPT-overhead trade-off and UE complexity

남은 FFS 2건

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#125:10.5.3.1:014`

> For 6GR CSI container design, CSI report in L1 is supported with
> - separate CSI measurement/computation triggering/configuration and CSI reporting triggering/configuration
> - minimizing collision handling cases and simplification on the collision handling rules between more than 1 UL channels where at least 1 of the UL channels carrying CSI reports,
>   - E.g., No collision handling rules between multiple carriers, if applicable
>   - Designs are to be discussed and decided in 10.5.4.4
> - streamlined CSI timeline including timeline relaxation

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#125:10.5.3.1:015` · 관련 주제: CSI-RS

> For CJT calibration report,
> - Study the following three types of reporting quantities:
> - Inter-TRP (xTRP) delay offset, analogous to Rel-19 cjtc-Dd
> - Inter-TRP (xTRP) frequency offset, analogous to Rel-19 cjtc-F
> - Inter-TRP (xTRP) DL/UL phase offset, analogous to Rel-19 cjtc-P
> - Note: Additional details are still to be studied, including dynamic range and resolution, and their additional use cases (if any)
> - Stand-alone reporting as a baseline for evaluation
> - Study whether/how to support reporting CJTC delay offset report and codebook-based CSI (with NTRP>1)
> - Note: when CSI-RS and DMRS have different delay pre-compensation assumption, the potential impact on DMRS based channel estimation can be discussed in 10.5.2.2

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#125:10.5.3.1:017`

> For SLS/LLS evaluation for JSCM-based CSI compression,
> - For both JSCM and SSCCM, the following Tx/Rx chain is considered.
> Companies report the assumption and/or abstraction for each block.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#125:10.5.3.1:018` · 관련 주제: CSI-RS

> For SLS evaluation for JSCM-based CSI compression,
> - Considering the following options of the SSCCM below could be used for the SLS evaluation as a starting point:
>   - Option 1: variable RE overhead {Throughput vs CSI feedback overhead (# of REs)}
>     - Step 1: for SSCCM, fixed payload determination (per PC or per payload)
>       - Different parameter combination or payload is simulated.
>     - Step 2: CSI feedback overhead (# of REs) is averaged of scheduled UEs in SLS, and the UL resource of each UE is determined based on the UL SINR considering link adaption
>     - Step 3(if applicable): check whether UL transmission is successfully decoded or not
>       - Based on the PHY abstraction (flip coin) according to UL SINR for each UE
>         - Y: Calculate UPT based on the current CSI
>         - N: Calculate UPT based on the historical CSI
>     - Step 4: gNB uses the received CSI feedback for DL transmission for UPT calculation across UEs.
>   - Option 2: Fixed CSI feedback overhead (#RE) with per UE level PC/payload selection for SSCCM and per scheduling UE level uplink link adaptation for SSCCM
>     - Step 1: Fixed CSI feedback overhead (# of REs) is used across all UEs.
>       - Payload determination (parameter combination/payload) for each UE
>         - Companies report how to determine the parameter commination/payload
>       - for each UE, the payload size can be selected according to UL SINR
>         - Companies report how to generate UL SINR, e.g., based on geometry only, or based on geometry and fast fading.
>         - Companies report the target BLER and UL SINR definition (e.g., port domain or UL SINR after Rx combination)
>     - Step 2 (if applicable): check whether UL transmission is successfully decoded or not
>       - Based on the PHY abstraction (flip coin) according to UL SINR for each UE
>         - Y: Calculate UPT based on the current CSI and update the historical CSI
>         - N: Calculate UPT based on the historical CSI
>   - Option 3: variable RE overhead with per scheduled UE level PC/payload selection and per scheduling UE level uplink link adaptation for SSCCM
>     - Step 1:
>       - Payload determination (parameter combination/payload) and link adaptation to determine the variable RE for each UE
>         - Companies report how to determine the parameter combination/payload and link adaption
>     - Step 2 (if applicable): check whether UL transmission is successfully decoded or not
>       - Based on the PHY abstraction (flip coin) according to UL SINR for each UE
>         - Y: Calculate UPT based on the current CSI and update the historical CSI
>         - N: Calculate UPT based on the historical CSI
>         - Note: Error free can be reported.
>     - Step 3: gNB uses the received CSI feedback for DL transmission for UPT calculation across UEs
>   - Other refinement to the above options are not precluded.
>   - Other options can be reported.
> - SSCCM baseline assumption for SLS is up to companies’ report
> - For JSCM, CSI feedback overhead is selected for each scheduled UEs in SLS.
>   - Companies report how to select the CSI overhead for each UE for other method.
> - Companies report how to generate UL SINR, e.g., based on geometry only, or based on geometry and fast fading.
>   - Companies report the uplink channel estimation error assumption.
> - Companies report the target BLER (e.g., error free, or 1% or 10%) and UL SINR definition (e.g., port domain or UL SINR after Rx combination) for SSCCM in Step 2.
> - Fixed max Tx power for uplink, companies report MPR assumption in the simulation. Companies report the UL power control assumption, e.g., P0 and alpha values.
>   - PRB is used as power control adjustment granularity
> - Companies report constellation assumption and corresponding PAPR (considering potential multiplexing with other UCI/UL-SCH).
> - 1Tx or multiple Tx can be considered for UL. If more than 1 Tx is assumed, companies report the UL Tx/precoder assumptions.
> - Companies report the PHY abstraction for uplink based on polar coding, if applicable.
> - Companies report the handling of scalability of number of REs for JSCM-based CSI compression, if applicable, and whether to adopt UCI only on PUSCH or UCI with UL-SCH for benchmark and JSCM-based compression.
> - Companies report the assumptions of JSCM, e.g., the projection-matrix-based compression (compress target CSI by multiplying with a projection matrix at UE) or encoder-based (e.g., transformer-based)
> - Companies report the assumption on obtaining projection matrix/encoder for JSCM-based CSI compression
> - Companies report the assumption on DL CSI-RS channel estimation error:
>   - Error modelling in TR36.897 Table A.1-2 as a baseline if channel estimation error is modelled.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.3` Other aspects · `RAN1#125:10.5.3.3:004`

> Study and evaluate the following assistance information for joint DL/UL based CSI acquisition use case 2
> - SINR
> - Non-PMI CSI feedback, e.g., CRI-RI-CQI
> - RSRP + interference-plus-noise
> - Note: The information can be wideband or subband, if applicable
> - Note: How to calculate, use and report the information shall be reported by companies.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Other Aspects related to CSI]`

**Agreement** · `10.5.3.3` Other aspects · `RAN1#125:10.5.3.3:005`

> Study and evaluate the following assistance information for joint DL/UL based CSI acquisition use case 1
> - Channel covariance matrix related information
>   - E.g., spatial/beam, frequency, or joint spatial frequency domain channel covariance matrix
> - Multipath components (MPC) related information
>   - E.g., Power Angular Spectrum (PAS), Power Delay Profile (PDP), Doppler shift/spread, Power Delay Angular and Doppler profile
> - Channel matrix related information
>   - E.g., Precoding matrix, channel eigenvector and eigenvalue, explicit channel matrix, etc.
>   - Full or partial channel matrix related information may be used
> - Received power difference between UE Rx ports
> - L1-RSRPs with finer granularity in frequency (e.g., subband level) and/or spatial (e.g., Rx ports group)
> Note 1: When the information is needed, how to report the information will be discussed in 10.5.3.1.
> Note 2: How to calculate, use and report the information shall be reported by companies.
> Note 3: The feasibility to obtain and report the information should be considered.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Other Aspects related to CSI]`

## RAN1#124bis — 14건

**Agreement** · `8.2` Maintenance on NR MIMO Phase 5 · `RAN1#124bis:8.2:001`

> The following TP for Clause  6.3.2.1.2 is endorsed for Alignment CR for 38.212.
> - Reason for change: In TS 38.212, “CapabilityIndex” appears in the title of Table 6.3.2.1.2-14. However, CapabilityIndex is not present in the table itself, nor is it one of the parameters that should be included in the CSI report for UE-initiated CSI reporting.
> - Summary of change: Remove “CapabilityIndex” from the title of Table 6.3.2.1.2-14 in TS 38.212.
> - Consequences if not approved: This would lead to inconsistency and ambiguity.
> | 6.3.2.1.2 CSI <Unchanged parts are omitted> Table 6.3.2.1.2-14: CRI, SSBRI, RSRP, CapabilityIndex, CSI report configuration indicator and Condition met indicator |

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2603249](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603249.zip) · `[124-R19b-MIMO]`

**Agreement** · `8.2` Maintenance on NR MIMO Phase 5 · `RAN1#124bis:8.2:003`

> The following TP for Rel-19 TS38.213, Clause 7.2.1, is endorsed as Alignment CR.
> - Reason for change: In the current specification, UEIRI is considered as a new type of SR for multiplexing rules of UEIRI. However, that is not described for PUCCH power control part.
> - Summary of change: Update TS 38.213 to count UEIRI bit as toward to  for PUCCH power control.
> - Consequences if not approved: UE behavior regarding PUCCH power control when UEIRI is transmitted becomes ambiguous.
> | ===========================unchanged omitted============================== 7.2.1 UE behaviour If a UE transmits a PUCCH on active UL BWP of carrier in the primary cell using PUCCH power control adjustment state with index ===========================unchanged omitted============================== - For a PUCCH transmission using PUCCH format 2 or PUCCH format 3 or PUCCH format 4 and for a number of UCI bits smaller than or equal to 11, , where - - is a number of HARQ-ACK information bits that the UE determines as described in clause 9.1.2.1 or 16.5.1.1 for Type-1 HARQ-ACK codebook and as described in clause 9.1.3.1 or 9.1.3.3 or 16.5.2.1 for Type-2 HARQ-ACK codebook, or as described in clause 9.1.5 for HARQ-ACK codebook retransmission, or as described in clause 9.2.5.4 for deferring HARQ-ACK for SPS PDSCH. is the same as as described in clause 9.1.4 for Type-3 HARQ-ACK codebook. If the UE is not provided any of pdsch-HARQ-ACK-Codebook, pdsch-HARQ-ACK-Codebook-r16, or pdsch-HARQ-ACK-OneShotFeedback, if the UE includes a HARQ-ACK information bit in the PUCCH transmission; otherwise, - is a number of SR/UEIRI information bits that the UE determines as described in clause 9.2.5.1 - is a number of CSI information bits that the UE determines as described in clause 9.2.5.2 - is a number of resource elements determined as , where is a number of subcarriers per resource block excluding subcarriers used for DM-RS transmission, and is a number of symbols excluding symbols used for DM-RS transmission, as defined in clause 9.2.5.2, for PUCCH transmission occasion on active UL BWP of carrier of primary cell - For a PUCCH transmission using PUCCH format 2 or PUCCH format 3 or PUCCH format 4 and for a number of UCI bits larger than 11, , where - - - is a number of HARQ-ACK information bits that the UE determines as described in clause 9.1.2.1 or 16.5.1.1 for Type-1 HARQ-ACK codebook and as described in clause 9.1.3.1 or 9.1.3.3 or 16.5.2.1 for Type-2 HARQ-ACK codebook, or as described in clause 9.1.4 for Type-3 HARQ-ACK codebook, or as described in clause 9.1.5 for HARQ-ACK codebook retransmission, or as described in clause 9.2.5.4 for deferring HARQ-ACK for SPS PDSCH. If the UE is not provided any of pdsch-HARQ-ACK-Codebook, pdsch-HARQ-ACK-Codebook-r16, or pdsch-HARQ-ACK-OneShotFeedback, if the UE includes a HARQ-ACK information bit in the PUCCH transmission; otherwise, - is a number of SR/UEIRI information bits that the UE determines as described in clause 9.2.5.1 - is a number of CSI information bits that the UE determines as described in clause 9.2.5.2 - is a number of CRC bits that the UE determines as described in clause 9.2 - is a number of resource elements that the UE determines as , where is a number of subcarriers per resource block excluding subcarriers used for DM-RS transmission, and is a number of symbols excluding symbols used for DM-RS transmission, as defined in clause 9.2.5.2, for PUCCH transmission occasion on active UL BWP of carrier of primary cell . ===========================unchanged omitted============================== |

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2603250](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603250.zip) · `[124-R19b-MIMO]`

**Agreement** · `8.2` Maintenance on NR MIMO Phase 5 · `RAN1#124bis:8.2:006` · 관련 주제: CSI-RS

> The following TP for TS38.212 , Clause 6.3.2.1.2 is endorsed.
> The corresponding final CR for Rel-19 TS38.212 in R1-2603414 is endorsed.
> | Impacted spec(s): |
> | Reason for change: Per 38.214, for RRC connected mode, a UE is configured with NZP-CSI-RS-ResourceSet with higher layer parameter set to trs-Info for tracking, and not TRS resource set which is the TRS configured for IDLE/INACTIVE with trs-ResourceSetConfig/TRS-ResourceSet-r18. |
> | Summary of the change: Replace “Reference TRS Resource Set index” with “Index of reference CSI-RS set for tracking” For other instances of “TRS resource set”, rename it to “CSI-RS resource set for tracking” |
> | Consequences if not approved: Inconsistent referencing and ambiguous UE behavior on which resource set index to include in the CSI report for CJT delay and frequency offsets. |
> | 6.3.2.1.2 CSI -------------------------------------------Unchanged parts are omitted------------------------------------------ Table 6.3.2.1.2-3E: Mapping order of CSI fields of one CSI report for reportQuantity=cjtc-Dd Table 6.3.2.1.2-3F: Mapping order of CSI fields of one CSI report for reportQuantity=cjtc-F Table 6.3.2.1.2-3G: Mapping order of CSI fields of one CSI report for reportQuantity=cjtc-Dd-F -------------------------------------------Unchanged parts are omitted------------------------------------------ Table 6.3.2.1.2-11: Reference TRS resource set index of reference CSI-RS resource set for tracking, delay offset and inside/outside indicator for reportQuantity=cjtc-Dd -------------------------------------------Unchanged parts are omitted------------------------------------------ Table 6.3.2.1.2-12: Reference TRS resource set index of reference CSI-RS resource set for tracking, and frequency offset for reportQuantity=cjtc-F |

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2602154](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2602154.zip) · `[124-R19b-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#124bis:9.2:003` · 관련 주제: CSI-RS

> For aperiodic CSI-RS associated with aperiodic CSI reporting triggered by MAC-CE in MSG4, down select one from the following options in RAN1#125:
> - Option-1: The triggered aperiodic CSI-RS is QCLed Type-C with the SSB the UE identified during the random access procedure when UE transition from IDLE/INACTIVE to CONNECTED mode
> - Option-2: If the aperiodic CSI-RS is triggered along with an aperiodic TRS by the same MAC-CE in MSG4 and the aperiodic TRS is transmitted before the aperiodic CSI-RS , the CSI-RS is QCLed Type-A with the triggered aperiodic TRS; otherwise, the CSI-RS is QCLed Type-C with the SSB the UE identified during the random access procedure when UE transition from IDLE/INACTIVE to CONNECTED mode.
>     - FFS whether/how there is impact on the time gap requirements between the triggered AP-TRS and AP-CSI-RS.
> FFS: Whether to consider QCL Type-D when applicable

남은 FFS 2건

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2602826](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2602826.zip) · `[124b-R20-MIMO]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#124bis:10.5.3.1:001`

> For 6GR codebook design for CSI report, study considering the following to ensure better performance than 5G
>   - SU-MIMO and MU-MIMO
>   - Single TRP and multi-TRP including CJT
>   - Other use scenarios, at least including High Doppler / High Speed Train (HST), Near-Field Propagation, spatial non-stationary (SNS)
> Note: Companies to provide complexity analysis

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#124bis:10.5.3.1:002`

> Starting from NR L1-based CSI reporting design, study whether/how the following aspects to be addressed in 6GR CSI reporting design taking into account of the comparison, at least including:
> - B1. Scheduling constraint relaxation
> - B2. Streamlined multiplexing complexity/collision handling rules, if applicable
> - B3. Streamlined CSI timeline including timeline relaxation
> - B4. Handling of varying CSI payload size
> For comparison on CSI report in L1 and L2, considering at least the following aspects taking into account of B1~B4:
> - A1. Efficiency /overhead
> - A2. Latency
> - A3. Reliability
> - A4. Implementation processing complexity at UE considering cross layer complexity (if any)
> - A5. Implementation processing complexity at NW considering cross layer complexity (if any)
> - A6. Congestion
> - A7. Min/Max CSI payload

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#124bis:10.5.3.1:004` · 관련 주제: CSI-RS

> For CSI-RS for CSI acquisition in 6GR, study the maximum number of ports considering the following alternatives
>   - Alt 1: The maximum number of CSI-RS ports is 128
>   - Alt 2: The maximum number of CSI-RS ports is 256
>   - Alt 3: The maximum number of CSI-RS ports is 512
>   - The study includes evaluation of the performance and CSI-RS overhead
>     - Note: relevant complexity can also be considered
>   - FFS whether all the NR port numbers are supported

남은 FFS 1건

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#124bis:10.5.3.1:005` · 관련 주제: CSI-RS

> 6GR supports NZP CSI-RS as the channel measurement RS for DL based CSI acquisition
> - FFS other reference signals, e.g., DMRS
> - FFS Aspects related with non-precoded CSI-RS or precoded CSI-RS

남은 FFS 2건

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#124bis:10.5.3.1:006` · 관련 주제: CSI-RS

> Consider CSI-IM as the baseline for interference measurement resource for DL CSI acquisition in 6GR
> - FFS other RS types, e.g., NZP CSI-RS, DMRS, etc

남은 FFS 1건

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#124bis:10.5.3.1:007` · 관련 주제: CSI-RS

> On time-domain type of 6G CSI-RS for downlink based CSI acquisition, at least support periodic and aperiodic CSI-RS, and further study
> - Whether semi-persistent CSI-RS is additionally supported
> - Whether new time-domain behavior is beneficial

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#124bis:10.5.3.1:011` · 관련 주제: CSI-RS

> For 6GR CSI-RS for DL based CSI acquisition, study CSI-RS RE sharing considering the following use cases.
> - Use case 1: Sharing a common set or subset of REs among CSI-RS with different number of ports
> - Use case 2: Sharing a common set or subset of REs among CSI-RS with different frequency densities
> - Use case 3: Sharing a common set or subset of REs among CSI-RS with different periodicities/time domain types
> - Use case 4: Sharing a common set or subset of REs among 5G CSI-RS and 6G CSI-RS
> - Note: the combination of the above use cases can be considered.
> - Note: the above use cases are design principles at this stage. Whether there is specification impact subjects to further discussion.
> - Note: the scenarios for sharing of CSI-RS may need to consider CSI-RS channel estimation performance at cell-edge, precoded/non-precoded CSI-RS, AI/non-AI, NES enabled/disabled, UEs with different measurement capabilities, single-TRP/Panel or multi-TRP/Panel etc

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#124bis:10.5.3.1:014`

> For the codebook design, study at least the following codebook structures
> - For low-resolution/ high-resolution CSI, considering ,  for evaluation
> - Note: Other codebook structure and enhancements of NR codebook structure(s), or other codebook are not precluded
> - Note: NR codebooks are used as benchmark for performance and complexity assessment
> For evaluation on codebook design, companies report
> - the max rank assumption, and whether a single codebook structure across all ranks for low-/high-resolution CSI, if appliable
> - the assumption of SD/FD basis selection, if appliable
> - the codebook parameter assumptions
> - basis format assumption
> - assumption of target CSI and corresponding codebook structure, e.g., implicit/explicit CSI
> - complexity analysis

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#124bis:10.5.3.1:015`

> For the evaluation of scalability/generalization for AI-based CSI compression, the evaluation methodology in NR (as in TR 38.843) can be considered as the starting point. The set of configurations are considered focusing on one or more of the following aspects at a starting point:
> - Various DL channels for compression, for example, deployment scenarios (e.g., UMa, UMi, InH), outdoor/indoor UE distributions (e.g., 10:0, 8:2, 5:5, 2:8, 0:10), antenna virtualization (TxRU mapping)
> - Various uplink channel/interference for uplink transmission (e.g., AWGN, CDL, TDL, Uma channel, different uplink SNR range, different UL noise/interference patterns)
> - Various UL resource size, e.g., #of REs for CSI feedback
> - Various NW (Rx chain, channel estimation, equalization) and UE (Tx chain, and RF impairments) implementations
> - Various number of Tx/Rx ports/layers, if applicable
> - Various number of subbands
> - Companies report the training and testing assumptions

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#124bis:10.5.3.1:017`

> Study on whether/how to support CSI report for CJT calibration.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of DL based CSI acquisition]`

## RAN1#124 — 9건

**Agreement** · `8.2` Maintenance on NR MIMO Phase 5 · `RAN1#124:8.2:005`

> Adopt the following changes in Section 9.2.5 in TS38.213:
> The corresponding CR for Rel-19 and TS38.214 in R1-2601679 is endorsed.
> | Impacted spec(s): TS38.213 |
> | Reason for change: The agreement reached in RAN1#119 has not been incorporated into the current 213 (V19.1.0). This modification is necessary because the Rel-19 Type-I SP codebook exhibits significant overhead variation across different measured ranks. Specifically, RANK 7/8 yields the maximum overhead for Scheme-A, whereas RANK 4 for Scheme-B. However, according to the current spec, UE shall determine PUCCH resources under the assumption of feedback rank 1 for each CSI report. This approach is based on observations that the Rel-15 Type-I codebook maintains consistent overhead across ranks. Persisting with rank 1 assumption for Rel-19 Type-I codebook CSI reports will inevitably increase the frequency of UCI dropping incidents. |
> | Summary of the change: Change the rank assumption for determination of the PUCCH resource or the number of PRBs or number of part 2 CSI reports. |
> | Consequences if not approved: Unnecessary UCI dropping will occur for Rel-19 Type-I codebook. |
> | =====================Start of Text Proposal to TS38.213================== 9.2.5 UE procedure for reporting multiple UCI types If a UE would multiplex CSI reports that include Part 2 CSI reports in a PUCCH resource, the UE determines the PUCCH resource and a number of PRBs for the PUCCH resource or a number of Part 2 CSI reports assuming that each of the CSI reports and, if any, each CSI sub-report included in a CSI report, indicates rank 1, or rank combination of {1, 1} if applicable. If csi-ReportMode of CSI reports is set to 'Mode2', the UE determines the PUCCH resource and a number of PRBs for the PUCCH resource or a number of Part 2 CSI reports assuming that each CRI in the CSI report is associated with a resource pair. If the UE is provided CSI-ReportConfig that includes valueOfM, the UE determines a PUCCH resource and a number of PRBs for the PUCCH resource, or a number of Part 2 CSI reports, assuming that each CSI sub-report corresponding to each of M CRIs indicates rank 1. If the UE is provided CSI-ReportConfig that includes a codebookType set to 'typeI-SinglePanel-r19', the UE determines a PUCCH resource and a number of PRBs for the PUCCH resource, or a number of Part 2 CSI reports, assuming that the CSI report, or, if applicable, each CSI sub-report of the CSI report indicates rank 8 if codebookMode set to 'modeA' and typeI-SinglePanelRI-Restriction for the CSI report includes an allowed RI of rank 5, 6, 7 or 8, indicates rank 4 if codebookMode set to 'modeB', and indicates rank 1 otherwise. <Unchanged parts are omitted> =====================End of Text Proposal to TS 38.213================== |

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601519](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601519.zip) · `[124-R19-MIMO]`

**Agreement** · `8.2` Maintenance on NR MIMO Phase 5 · `RAN1#124:8.2:006`

> Adopt the following changes in Section 5.2.2.2.5a in TS38.214:
> The corresponding CR for Rel-19 and TS38.214 in R1-2601680 is endorsed.
> | Impacted spec(s): TS38.214 |
> | Reason for change: The proposed TP below was already endorsed verbatim in RAN1#122bis but was not captured in the latest version of TS38.214. Agreement (RAN1#122bis) The TP2.A for TS38.214 in R1-2507269 is endorsed. |
> | Summary of the change: Added the missing oversampling parameters |
> | Consequences if not approved: Endorsed TP in RAN1#122bis is not captured in TS38.214 – procedural error |
> | 5.2.2.2.5a Refined eType II Codebook < Unchanged parts omitted > The bitmap parameter typeII-CBSR-r19 forms the bit sequence , where is the LSB and is the MSB and the number of bits is given by , where the values are configured by the higher layer parameters valueOfX1-typeII-CBSR-r19 and valueOfX2-typeII-CBSR-r19, respectively. The supported combinations of for a given combination of are given in Table 5.2.2.2.5a-1. A bit value of zero for bit indicates that PMI reporting is not allowed to correspond to any precoder associated with vector group , , , given by < Unchanged parts omitted > |

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601519](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601519.zip) · `[124-R19-MIMO]`

**Agreement** · `9.2.2` Enhancing DL CSI acquisition · `RAN1#124:9.2.2:003`

> For aperiodic CSI reporting for a SCell(s), triggered based on a legacy SCell activation command activating the SCell(s), the SCell activation command indicates a UL grant for a PUSCH to carry the aperiodic CSI report(s) for the CSI report configuration(s) triggered for the SCell(s)
> - Strive to reuse legacy UL grant design in RAR
> - The aperiodic CSI report(s) is reported in the same PUSCH.
> - FFS: The serving cell where the PUSCH is scheduled in

남은 FFS 1건

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2600647](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2600647.zip)

**Agreement** · `9.2.2` Enhancing DL CSI acquisition · `RAN1#124:9.2.2:007` · 관련 주제: CSI-RS

> For CSI-RS frequency-domain densities ρ = 1/3 and 1/6, support new CSI subband sizes as follows:
> | Bandwidth part size (PRBs) | CSI subband size (PRBs) |
> | 24-72 | 6 (FFS: 12) |
> | 73-144 | 12 (FFS: 6) |
> | 145-275 | 24 (FFS: 30) |
> Note: Legacy PRG sizes are reused without enhancement.

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2600648](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2600648.zip)

**Conclusion** · `9.2.2` Enhancing DL CSI acquisition · `RAN1#124:9.2.2:008` · 관련 주제: CSI-RS

> No enhancement to the following legacy specification restriction on frequency density of CSI-RS port in a CSI subband for the frequency-domain densities ρ = 1/3 and 1/6, i.e., the following from Clause 5.2.1.4 in TS 38.214 shall be applied:
> - A UE is not expected to be configured with csi-ReportingBand which contains a subband where a CSI-RS resource linked to the CSI Report setting has the frequency density of each CSI-RS port per PRB in the subband less than the configured density of the CSI-RS resource.

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2600648](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2600648.zip)

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#124:10.5.3.1:001` · 관련 주제: CSI-RS

> Adopt the following table as the basic assumption of SLS for evaluation of DL-based CSI acquisition.
> Table General Assumption
> | Parameters | Proposals |
> | #1 Carrier frequency | Around 700MHz (FDD) Around 2 GHz (FDD) Around 4 GHz (TDD) Around 7 GHz (TDD) Other carrier frequency is not precluded |
> | #2 Simulation bandwidth | 20MHz 100MHz (not applicable for 700MHz) Other BW is not precluded System/channel bandwidth assumption is reported by companies. |
> | #3 Number of subbands and subbands size | Number of SBs 1 for WB 13 SB for 20MHz TBD SB for 100MHz Subband size: 4 or 8 PRBs for 20MHz TBD PRBs for 100MHz Note: Temporary, before subband size for 6GR is decided Other number can be reported. |
> | #4 Scenario | Note: Reuse SLS assumption for PDSCH |
> | #5 UE number/cell | 10, 30 for FTP3 Other numbers is not precluded. |
> | #6 Layout/deployment | 1-ring (7*3), 2-ring (19*3) Other layout/deployment are not precluded. |
> | #7 Channel model | Rel-19 TR 38.901 Note: spatial consistency could be considered, if applicable |
> | #8 Numerology | OFDM, 15 kHz for FDD, 30 kHz for TDD |
> | #9 Transmit power (per 20MHz) | Dense urban: 44dBm Urban macro: 46dBm Suburban Marco:49dBm Other values can be reported by companies. Note: For evaluation purpose, BS Tx power scales up with bandwidth proportionally under the limitation of the maximum BS Tx power is 56dBm for outdoor and 33dBmfor indoor for the above carrier frequencies. |
> | #10 BS antenna configuration | Reuse the assumption under AI 10.5.2.2 when applicable, otherwise refer to AI 10.1 |
> | #11 UE power class | 23dBm, 26dBm[,29dBm] |
> | #12 UE antenna configuration | Details follow corresponding agreements in Agenda 10.1 |
> | #13 UE Receiver | MMSE-IRC (baseline) R-ML (Reported by companies) |
> | #14 Traffic model | FTP Model 1/3 (0.5 Mbyte packet sizes) Low RU about 30% Medium RU about 50% High RU about 70% Other model is not precluded. |
> | #15 Scheduling | PF |
> | #16 Inter-cell interference model | Explicitly and realistically modelled |
> | #17 Channel estimation assumption | Realistic as the baseline Companies to report the detailed CSI-RS channel estimation |
> | #18 CSI feedback | CSI periodicity: 10ms, 20ms Scheduling delay: Minimum [4ms] from CSI measurement to CSI application Companies to report if other assumptions are used |
> | #19 MIMO scheme | SU-MIMO MU-MIMO with rank adaptation NR CW-to-layer mapping is used and other mapping is not precluded. |
> | #20 Feedback assumption | Companies report UCI reception assumption. FFS: how to modeling |
> | #21 Evaluation Metric | Throughput and CSI feedback overhead as baseline metrics, the CSI feedback overhead is the actual feedback overhead statistics per system level evaluation Other KPI is not precluded. |
> | #22 Baseline for performance evaluation | Rel-19 Type I Scheme A/B Rel-19 eType II Codebook Ideal SVD for calibration [NR AI-CSI compression, when applicable] |
> | #23 Phase errors for radios with uncalibrated antennas (for 4 TXRUs) | Wideband phase error between Tx antenna port 0 and Tx antenna port () can be modeled: Independent random phase offset uniformly distributed between 0 and 2π between any two Tx antenna ports. |
> | #24 Calibration error modeling for other antennas | FFS |
> - Note: EVM assumption for HST scenarios will be treated separately

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · `[124-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#124:10.5.3.1:005`

> For the study on AI-based CSI compression, the following is considered:
> - KPI: SGCS (Intermediate), PAPR (when applicable), throughput vs CSI feedback overhead, DL throughput/BLER vs SNR
>   - CSI feedback overhead: the number of UL resource elements
>     - Companies to report values
>   - Note: the overhead of DMRS (if applicable) is reported by company
> - Model/computation complexity at UE side (when applicable): FLOPs/M
> - Model/computation complexity at NW side: FLOPs/M
> - Model size: Number of parameters/M
> - Overhead of downloadable basis/codebook/matrix for compression (when applicable): size of parameters (Mbytes) and updated frequency
> - Overhead/complexity/impact of inter-vendor collaboration (when applicable)
> - Benchmark:
>   - Rel-20 NR SSCC approach with 2-sided model (companies report the inter-vender collaboration assumption) and/or NR eType II feedback and/or NR Type I feedback
>   - Link adaptation is considered
> - Evaluation assumptions follow general EVM.
>   - For uplink transmission (e.g., UL channel model, UL SNR range, UL channel estimation, UL noise + interference estimation) are reported by companies
>   - Companies to report the considered non-ideal factors, if assumed, e.g., Tx PA nonlinearity & RF impairment, UL/DL channel estimation errors, uplink interference pattern
>   - Companies to report the bitwidth/shape of the modulation constellation
> - Note: the above assumptions can also apply for non-AI schemes, i.e., without training/inference/data collection/projection, when applicable.
> - Note: RAN4 related impacts, e.g., EVM, ACLR, SEM, are to be considered

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · `[124-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.3` Other aspects · `RAN1#124:10.5.3.3:002`

> For joint DL and UL based DL CSI acquisition, reuse the evaluation methodology for LLS and SLS agreed in DL CSI / UL CSI agendas.
> - Note: Specific necessary aspects on joint operation will be discussed.

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · `[124-R20-6GR-Other Aspects related to CSI]`

**Agreement** · `10.5.3.3` Other aspects · `RAN1#124:10.5.3.3:003`

> Study joint DL and UL based CSI acquisition in TDD system.

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · `[124-R20-6GR-Other Aspects related to CSI]`

## RAN1#123 — 8건

**Agreement** · `8.2` Maintenance on NR MIMO Phase 5 · `RAN1#123:8.2:004`

> Adopt the following changes in Clause 6 of TS38.214:
> For  the remaining of this clause, unless otherwise stated, reference to PUSCH with aperiodic CSI reports includes a PUSCH with UE initiated report when reportTransmissionMode is configured as ‘ModeA’ in the CSI report configuration (as defined in Section 5.2.1.5.4.1).
> - Reason for change:  From the excerpt from 38.214, there is no description on how the UE would transmit the CSI report associated with event driven reporting, regarding mode-B. The understanding in RAN1 is that the same procedure as for aperiodic CSI reports would be used.
> - Summary of change: The UE behavior of UEI CSI reporting when reportTransmissionMode is configured as ‘ModeA’ in the CSI report configuration is to reuse that for PUSCH with aperiodic CSI reports, unless otherwise stated.
> - Consequences if not approved: UE initiated CSI report procedure when reportTransmissionMode is configured as ‘ModeA’ in the CSI report configuration is unclear.

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2508529](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2508529.zip) · `[123-R19-MIMO]`

**Conclusion** · `8.2` Maintenance on NR MIMO Phase 5 · `RAN1#123:8.2:011`

> The UE capability mixCodeBookSpatialAdaptation from Rel-18 NES is not supported with Rel-19 Type-I codebook.

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2508775](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2508775.zip) · `[123-R19-MIMO]`

**Agreement** · `8.2` Maintenance on NR MIMO Phase 5 · `RAN1#123:8.2:012`

> - The following TP for TS38.215 is endorsed.
> | Spec | TS38.215 |
> | Reason for change | is specified in 38.214 (section 5.2.1.4.10), however it is not clear what is the reference frequency in relation to ppm. If not clarified, absolute frequency offset values may be unaligned, which may lead to performance loss. Since ‘Coherent joint transmission calibration frequency offset’ is specified in 38.215, it should be clarified that the reference frequency in relation to ppm is the frequency of Point A in 38.215 |
> | Summary of change | A description is added to define the reference frequency in relation to ppm as the frequency of Point A. |
> | Consequences if not approved | If not clarified, absolute frequency offset values may be unaligned, which can lead to performance loss. |
> | 5.1.51 Coherent joint transmission calibration frequency offset | 5.1.51 Coherent joint transmission calibration frequency offset |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2508775](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2508775.zip) · `[123-R19-MIMO]`

**Agreement** · `10.2.2` Enhancing DL CSI acquisition · `RAN1#123:10.2.2:004` · 관련 주제: CSI-RS

> For early triggering of aperiodic TRS when UE transition from IDLE/INACTIVE to CONNECTED mode, support Option-1, i.e.,
> - In Step-1, SIBx provides one CSI resource configuration for aperiodic TRS
>   - FFS: Whether to support more than one TRS resource sets provided in one CSI resource configuration (e.g., TRS resource sets can be provided with different triggering offsets, numbers of TRS bursts and/or gap between TRS bursts, etc)
> - In Step-2, UE reports through MSG3 whether the CSI resource configuration for aperiodic TRS provided in SIBx is supported.
>   - FFS: Whether/How UE additionally reports via MSG3 the number of TRS bursts that the UE needs

남은 FFS 2건

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2508520](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2508520.zip)

**Agreement** · `10.2.2` Enhancing DL CSI acquisition · `RAN1#123:10.2.2:006` · 관련 주제: CSI-RS

> On PUSCH allocation for MSG4-triggered aperiodic CSI reporting associated with aperiodic CSI-RS for CSI, when UE transition from IDLE/INACTIVE to CONNECTED mode, support Alt-1 from Agreement in RAN1#122bis, i.e., the PUSCH is scheduled by MAC CE in MSG4 along with the aperiodic CSI report triggering.
> - Strive to reuse legacy UL grant design in RAR
> - FFS: Whether/How to handle the re-transmission of MSG4 PDSCH with the aperiodic CSI report triggering
> - FFS: Whether HARQ-ACK for PDSCH Msg4 is transmitted or not.

남은 FFS 2건

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2508520](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2508520.zip)

**Conclusion** · `10.2.2` Enhancing DL CSI acquisition · `RAN1#123:10.2.2:007` · 관련 주제: CSI-RS

> No enhancement to the following legacy specification restriction on frequency density of CSI-RS port in a CSI subband for the frequency-domain densities ρ = 1/4 and 1/8, i.e., the following from Clause 5.2.1.4 in TS 38.214 shall be applied:
> - A UE is not expected to be configured with csi-ReportingBand which contains a subband where a CSI-RS resource linked to the CSI Report setting has the frequency density of each CSI-RS port per PRB in the subband less than the configured density of the CSI-RS resource.
> FFS: Whether to apply the legacy specification restriction to the frequency-domain densities ρ = 1/3 and 1/6

남은 FFS 1건

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2508520](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2508520.zip)

**Agreement** · `10.2.2` Enhancing DL CSI acquisition · `RAN1#123:10.2.2:008` · 관련 주제: CSI-RS

> Support frequency-domain density ρ = 1/8 for K NZP CSI-RS resources in the same CSI-RS resource set for 48/64/128 CSI-RS ports aggregation with the following configurations, for wideband CSI reporting based on Rel-19 Type-1 codebooks:
> - K=4 16-port NZP CSI-RS resources in a resource set aggregating 64 CSI-RS ports
> - K=4 32-port NZP CSI-RS resources in a resource set aggregating 128 CSI-RS ports

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2508520](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2508520.zip)

**WA** · `10.2.2` Enhancing DL CSI acquisition · `RAN1#123:10.2.2:009` · 관련 주제: CSI-RS

>   - K=2 24-port NZP CSI-RS resources in a resource set aggregating 48 CSI-RS ports
> - FFS: For subband CSI reporting and Type-2 codebook
> Support of frequency-domain density ρ = 1/8 is a separate UE capability.
> Note: Different frequency-domain densities configured to the K NZP CSI-RS resources in the same CSI-RS resource set for 48/64/128 CSI-RS ports aggregation are not precluded

남은 FFS 1건

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2508520](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2508520.zip)

## RAN1#122bis — 33건

**Agreement** · `8.2` Maintenance on NR MIMO Phase 5 · `RAN1#122bis:8.2:011`

> The TP1.B for TS38.214 in R1-2507269 is endorsed. Note that the Clause number for this TP is Clause 5.2.2.5 and not 5.2.1.4.1.

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2507269](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2507269.zip) · `[122bis-R19-MIMO]`

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122bis:9.2:001` · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-1 | Enhanced Type-I SP codebook for 64 ports – Scheme-A | 1. Support of enhanced Type-I SP codebook for Scheme-A with 64 Tx ports by aggregating multiple NZP CSI-RS resources within one slot 2. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 3. Supported maximum rank 4. Max # of CSI-RS resource in a resource set 5. Supported processing capability 6. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 2-35 | yes | n/a | Enhanced Type-I SP codebook is not supported for 64 ports – Scheme-A, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 2 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Component 3 candidate value {4, 5, 6, 7, 8} Component 4 candidate value {2,4} Component 5 candidate value {Capability 1, Capability 2} Component 6 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Note: For component of processing capability Capability 1: Reuse legacy Z/Z’ values OCPU = ceil(P/32) Capability 2: Scale the legacy timeline Z/Z’ by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = 1 | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508081](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508081.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122bis:9.2:002` · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as show
> | 59. NR_MIMO_Ph5 | 59-2-1-1a | Enhanced Type-I SP codebook for 48 ports – Scheme-A | 1. Support of enhanced Type-I SP codebook for Scheme-A with 48 Tx ports by aggregating multiple NZP CSI-RS resources within one slot 2. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 3. Supported maximum rank 4. Max # of CSI-RS resource in a resource set 5. Supported processing capability 6. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 59-2-1-1 | yes | n/a | Enhanced Type-I SP codebook is not supported for Scheme-A for 48 Tx ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 2 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Component 3 candidate value {4, 5, 6, 7, 8} Component 4 candidate value {1:82,3} Component 5 candidate value {Capability 1, Capability 2} Component 6 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Note: For component of processing capability Capability 1: Reuse legacy Z/Z’ values OCPU = ceil(P/32) Capability 2: Scale the legacy timeline Z/Z’ by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = 1 | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508081](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508081.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122bis:9.2:003` · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-1b | Enhanced Type-I SP codebook for 128 ports – Scheme-A | 1. Support of enhanced Type-I SP codebook for Scheme-A with 128 Tx ports by aggregating multiple NZP CSI-RS resources within one slot 2. A list of supported combinations, each combination is Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 3. Supported maximum rank 4. Support 4 CSI-RS resources in a resource set 5. Supported processing capability 6. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 59-2-1-1 | yes | n/a | Enhanced Type-I SP codebook is not supported for Scheme-A for 128 Tx ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 2 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Component 3 candidate value {4, 5, 6, 7, 8} Component 5 candidate value {Capability 1, Capability 2} Component 6 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Note: For component of processing capability Capability 1: Reuse legacy Z/Z’ values OCPU = ceil(P/32) Capability 2: Scale the legacy timeline Z/Z’ by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = 1 | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508081](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508081.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122bis:9.2:004` · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-1c | Enhanced Type-I SP codebook for 64 ports – Scheme-B | 1. Support of enhanced Type-I SP codebook for Scheme-B with 64 Tx ports by aggregating multiple NZP CSI-RS resources within one slot 2. A list of supported combinations, each combination is Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 3. Supported maximum rank 4. Max # of CSI-RS resource in a resource set 5. Supported processing capability 6. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 2-35 | yes | n/a | Enhanced Type-I SP codebook is not supported for Scheme-B for 64 Tx ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 2 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Component 3 candidate value {4, 5, 6, 7, 8} Component 4 candidate value {2,4} Component 5 candidate value {Capability 1, Capability 2} Component 6 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Note: For component of processing capability Capability 1: Reuse legacy Z/Z’ values OCPU = ceil(P/32) Capability 2: Scale the legacy timeline Z/Z’ by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = 1 | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508081](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508081.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122bis:9.2:005` · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-1d | Enhanced Type-I SP codebook for 48 ports – Scheme-B | 1. Support of enhanced Type-I SP codebook for Scheme-B with 48 Tx ports by aggregating multiple NZP CSI-RS resources within one slot 2. A list of supported combinations, each combination is Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 3. Supported maximum rank 4. Max # of CSI-RS resource in a resource set 5. Supported processing capability 6. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 59-2-1-1c | yes | n/a | Enhanced Type-I SP codebook is not supported for Scheme-B for 48 Tx ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 2 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Component 3 candidate value {4, 5, 6, 7, 8} Component 4 candidate value {2,3} Component 5 candidate value {Capability 1, Capability 2} Component 6 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Note: For component of processing capability Capability 1: Reuse legacy Z/Z’ values OCPU = ceil(P/32) Capability 2: Scale the legacy timeline Z/Z’ by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = 1 | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508081](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508081.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122bis:9.2:006` · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-1e | Enhanced Type-I SP codebook for 128 ports – Scheme-B | 1. Support of enhanced Type-I SP codebook for Scheme-B with 128 Tx ports by aggregating multiple NZP CSI-RS resources within one slot 2. A list of supported combinations, each combination is Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 3. Supported maximum rank 4. Support 4 CSI-RS resources in a resource set 5. Supported processing capability 6. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 59-2-1-1c | yes | n/a | Enhanced Type-I SP codebook is not supported for Scheme-B for 128 Tx ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 2 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Component 3 candidate value {4, 5, 6, 7, 8} Component 5 candidate value {Capability 1, Capability 2} Component 6 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Note: For component of processing capability Capability 1: Reuse legacy Z/Z’ values OCPU = ceil(P/32) Capability 2: Scale the legacy timeline Z/Z’ by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = 1 | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508081](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508081.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122bis:9.2:007` · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-2 | Enhanced Type-I MP codebook for 64 ports | 1. Support of enhanced Type-I MP codebook for 64 ports within 1 slot 2. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 3. Supported maximum number of panels 4. Max # of CSI-RS resource in a resource set 5. Supported processing capability 6. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 2-35 | yes | n/a | Enhanced Type-I MP codebook is not supported for 64 ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 2 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Component 3 candidate value {2, 4} Component 4 candidate value {2,4} Component 5 candidate value {Capability 1, Capability 2} Component 6 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Note: For component of processing capability Capability 1: Reuse legacy Z/Z’ values OCPU = ceil(P/32) Capability 2: Scale the legacy timeline Z/Z’ by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = 1 | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508081](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508081.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122bis:9.2:008` · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-2a | Enhanced Type-I MP codebook for 48 ports | 1. Support of enhanced Type-I MP codebook for 48 ports within 1 slot 2. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 3. Supported maximum number of panels 4. Max # of CSI-RS resource in a resource set 5. Supported processing capability 6. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 59-2-1-2 | yes | n/a | Enhanced Type-I MP codebook is not supported for 48 ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 2 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Component 3 candidate value {2, 4} Component 4 candidate value {2,3} Component 5 candidate value {Capability 1, Capability 2} Component 6 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Note: For component of processing capability Capability 1: Reuse legacy Z/Z’ values OCPU = ceil(P/32) Capability 2: Scale the legacy timeline Z/Z’ by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = 1 | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508081](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508081.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122bis:9.2:009` · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-2b | Enhanced Type-I MP codebook for 128 ports | 1. Support of enhanced Type-I MP codebook for 128 ports within 1 slot 2. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 3. Supported maximum number of panels 4. Support 4 CSI-RS resources in a resource set 5. Supported processing capability 6. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 59-2-1-2 | yes | n/a | Enhanced Type-I MP codebook is not supported for 128 ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 2 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Component 3 candidate value {2, 4} Component 5 candidate value {Capability 1, Capability 2} Component 6 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Note: For component of processing capability Capability 1: Reuse legacy Z/Z’ values OCPU = ceil(P/32) Capability 2: Scale the legacy timeline Z/Z’ by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU =1 | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508081](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508081.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122bis:9.2:010` · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-3 | Extended Rel-16 eType-II codebook for 64 Tx ports | 1. Support of extended Rel-16 eType-II codebook for 64 Tx ports by aggregating multiple NZP CSI-RS resources within 1 slot 2. Support of parameter combination 1-6 3. Support of rank 1-2 4. Support R=1 5. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously with R=1 6. supported processing capability 7. Max # of CSI-RS resource in a resource set 8. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 16-3a | yes | n/a | Extended Rel-16 eType-II codebook is not supported for 64 Tx ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 5 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Component 6 candidate value {Capability 1, Capability 2} Component 7 candidate value {2,4} Component 8 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Note: For component of processing capability Capability 1: Reuse legacy Z/Z’ values OCPU = ceil(P/32) Capability 2: Scale the legacy timeline Z/Z’ by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = 1 | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508081](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508081.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122bis:9.2:011` · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-3a | Extended Rel-16 eType-II codebook for 48 Tx ports | 1. Support of extended Rel-16 eType-II codebook for 48 Tx ports by aggregating multiple NZP CSI-RS resources within 1 slot 2. Support of parameter combination 1-6 3. Support of rank 1-2 4. Support R=1 5. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously with R=1 6. supported processing capability 7. Max # of CSI-RS resource in a resource set 8. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 59-2-1-3 | yes | n/a | Extended Rel-16 eType-II codebook is not supported for 48 Tx ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 5 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Component 6 candidate value {Capability 1, Capability 2} Component 7 candidate value {2,3} Component 8 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Note: For component of processing capability Capability 1: Reuse legacy Z/Z’ values OCPU = ceil(P/32) Capability 2: Scale the legacy timeline Z/Z’ by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = 1 | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508081](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508081.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122bis:9.2:012` · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-3b | Extended Rel-16 eType-II codebook for 128 Tx ports | 1. Support of extended Rel-16 eType-II codebook for 128 Tx ports by aggregating multiple NZP CSI-RS resources within 1 slot 2. Support of parameter combination 1-6 3. Support of rank 1-2 4. Support R=1 5. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously with R=1 6. supported processing capability 7. Support 4 CSI-RS resources in a resource set 8. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 59-2-1-3 | yes | n/a | Extended Rel-16 eType-II codebook is not supported for 128 Tx ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 5 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Component 6 candidate value {Capability 1, Capability 2} Component 8 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Note: For component of processing capability Capability 1: Reuse legacy Z/Z’ values OCPU = ceil(P/32) Capability 2: Scale the legacy timeline Z/Z’ by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = 1 | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508081](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508081.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122bis:9.2:013`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-3-1 | PMI sub-bands with R=2 for extended Rel-16 eType-II codebook for up to 128 ports | 1. Support of PMI sub-bands with R=2 for extended Rel-16 eType-II codebook for up to 128 ports 2. A list of supported combinations, each combination is {Max # of Tx ports in a report, Max # of sets of aggregated resources, and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously with R=2 | 59-2-1-3 | Yes | n/a | PMI sub-bands with R=2 for extended Rel-16 eType-II codebook for up to 128 ports is not supported | Per band and Per BC | n/a | n/a | n/a | Component 2 candidate values a. {48, 64, 128} b. {1, …, 64, 128, 256} c. {64, …, 256, 512, 768, 1024} | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508081](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508081.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122bis:9.2:014`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-3-3 | Rank 3,4 for extended Rel-16 eType-II codebook for up to 128 ports | 1. Support of Rank 3,4 for extended Rel-16 eType-II codebook for up to 128 ports 4. Support R=1 5. A list of supported combinations, each combination is {Max # of Tx ports in a report, Max # of sets of aggregated resources, and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously with R=1 | 59-2-1-3 | Yes | n/a | Rank 3,4 for extended Rel-16 eType-II codebook for up to 128 ports is not supported | Per band and Per BC | n/a | n/a | n/a | Component 5 candidate values a. {48, 64, 128} b. {1, 2, …, 64} c. {64, …, 256, 512, 768, 1024} | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508081](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508081.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122bis:9.2:015` · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-4 | Extended Rel-17 FeType-II codebook with 64 Tx ports | 1. Support of extended Rel-17 FeType-II codebook for 64 Tx ports by aggregating multiple NZP CSI-RS resources within 1 slot 2. Support of parameter combinations with M=1 3. Support of rank 1-2 4. Support R=1 5. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously with M=1 and R=1 6. Supported processing capability 7. Max # of CSI-RS resource in a resource set 8. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 23-9-1 | yes | n/a | Extended Rel-17 FeType-II codebook is not supported with 64 Tx ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 5 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Component 6 candidate value {Capability 1, Capability 2} Component 7 candidate value {2,4} Component 8 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Note: For component of processing capability Capability 1: Reuse legacy Z/Z’ values OCPU = ceil(P/32) Capability 2: Scale the legacy timeline Z/Z’ by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = 1 | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508081](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508081.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122bis:9.2:016` · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-4a | Extended Rel-17 FeType-II codebook with 48 Tx ports | 1. Support of extended Rel-17 FeType-II codebook for 48 Tx ports by aggregating multiple NZP CSI-RS resources within 1 slot 2. Support of parameter combinations with M=1 3. Support of rank 1-2 4. Support R=1 5. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously with M=1 and R=1 6. Supported processing capability 7. Max # of CSI-RS resource in a resource set 8. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 59-2-1-4 | yes | n/a | Extended Rel-17 FeType-II codebook is not supported with 48 Tx ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 5 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Component 6 candidate value {Capability 1, Capability 2} Component 7 candidate value {2,3} Component 8 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Note: For component of processing capability Capability 1: Reuse legacy Z/Z’ values OCPU = ceil(P/32) Capability 2: Scale the legacy timeline Z/Z’ by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = 1 | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508081](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508081.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122bis:9.2:017` · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-5 | Extended Rel-18 eType-II Doppler codebook for 64 Tx ports | 1. Support of extended Rel-18 Type-II Doppler codebook for 64 Tx ports by aggregating multiple NZP CSI-RS resource groups within 1 slot 2. Support X=1 CQI based on the first/earliest slot of the CSI reporting window and the first/earliest predicted PMI (TDCQI=’1-1’) 3. Support PMI subband R=1 4. Support parameter combinations with L=2,4 5. Support rank = 1,2 6. Support 64 ports 7. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 8. Supported processing capability 9. Value of Y for CPU occupation when P/SP-CSI-RS is configured for CMR 10. Value of Y for CPU occupation when A-CSI-RS is configured for CMR 11. Support for the size of DD-basis, N4=1 12. Scaling factor for active resource counting Kp 13. Max # of CSI-RS resource in a resource group for aperiodic CSI-RS resource set or in a resource set for periodic CSI-RS resource set 14. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 40-3-2-1 | yes | n/a | Extended Rel-18 Type-II Doppler codebook is not supported for 64 Tx ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 7 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Component 8 candidate value {Capability 1, Capability 2} Component 9 candidate values: {1, 2, 3} Component 10 candidate values: {1, 2, 3} Component 12 candidate values: {1, 2, 4} Component 13 candidate value {2,4} Component 14 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Note: For component of processing capability Capability 1: Legacy timeline OCPU = YxN4xceil(P/32) ), when P/SP-CSI-RS is configured for CMR OCPU = Yx KDOPPxceil(P/32)), when A-CSI-RS is configured for CMR Capability 2: Scale the legacy timeline by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = YxN4, when P/SP-CSI-RS is configured for CMR OCPU = Yx KDOPP, when A-CSI-RS is configured for CMR Note: maximum OCPU is 8 Note: KDOPP is the number of CSI-RS resource groups configured for channel measurement, and each CSI-RS resource groups contain K CSI-RS resources for aggregating up to 128 ports | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508081](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508081.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122bis:9.2:018` · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-5a | Extended Rel-18 eType-II Doppler codebook for 48 Tx ports | 1. Support of extended Rel-18 Type-II Doppler codebook for 48 Tx ports by aggregating multiple NZP CSI-RS resource groups within 1 slot 2. Support X=1 CQI based on the first/earliest slot of the CSI reporting window and the first/earliest predicted PMI (TDCQI=’1-1’) 3. Support PMI subband R=1 4. Support parameter combinations with L=2,4 5. Support rank = 1,2 6. Support 64 ports 7. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 8. Supported processing capability 9. Value of Y for CPU occupation when P/SP-CSI-RS is configured for CMR 10. Value of Y for CPU occupation when A-CSI-RS is configured for CMR 11. Support for the size of DD-basis, N4=1 12. Scaling factor for active resource counting Kp 13. Max # of CSI-RS resource in a resource group for aperiodic CSI-RS resource set or in a resource set for periodic CSI-RS resource set 14. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 59-2-1-5 | yes | n/a | Extended Rel-18 Type-II Doppler codebook is not supported for 48 Tx ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 7 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Component 8 candidate value {Capability 1, Capability 2} Component 9 candidate values: {1, 2, 3} Component 10 candidate values: {1, 2, 3} Component 12 candidate values: {1, 2, 4} Component 13 candidate value {2,3} Component 14 candidate values a. {1, …, 64} b. {64, …, 256, 512, 768, 1024} Note: For component of processing capability Capability 1: Legacy timeline OCPU = Y x N4 x ceil(P/32) ), when P/SP-CSI-RS is configured for CMR OCPU = Y x KDOPP x ceil(P/32)), when A-CSI-RS is configured for CMR Capability 2: Scale the legacy timeline by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = Y x N4, when P/SP-CSI-RS is configured for CMR OCPU = Y x KDOPP, when A-CSI-RS is configured for CMR Note: maximum OCPU is 8 Note: KDOPP is the number of CSI-RS resource groups configured for channel measurement, and each CSI-RS resource groups contain K CSI-RS resources for aggregating up to 128 ports | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508081](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508081.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122bis:9.2:019` · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-5b | Extended Rel-18 eType-II Doppler codebook for 128 Tx ports | 1. Support of extended Rel-18 Type-II Doppler codebook for 128 Tx ports by aggregating multiple NZP CSI-RS resource groups within 1 slot 2. Support X=1 CQI based on the first/earliest slot of the CSI reporting window and the first/earliest predicted PMI (TDCQI=’1-1’) 3. Support of PMI subband R=1 for extended Rel-18 eType II Doppler codebook 4. Support parameter combinations with L=2,4 5. Support for rank = 1,2 6. Support 64 ports 7. A list of supported combinations, each combination is { Max # of Tx ports in one resource, Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 8. Supported processing capability 9. Value of Y for CPU occupation (OCPU = Y.N4), when P/SP-CSI-RS is configured for CMR 10. Value of Y for CPU occupation (OCPU = Y. KDOPP), when A-CSI-RS is configured for CMR 11. Support for the size of DD-basis, N4=1 12. Scaling factor for active resource counting Kp 13. Support 4 CSI-RS resources in a resource group for aperiodic CSI-RS resource set or in a resource set for periodic CSI-RS resource set 14. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 59-2-1-5 | yes | n/a | Extended Rel-18 Type-II Doppler codebook is not supported for 128 Tx ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 7 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Component 8 candidate value {Capability 1, Capability 2} Component 9 candidate values: {1, 2, 3} Component 10 candidate values: {1, 2, 3} Component 12 candidate values: {1, 2, 4} Component 14 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Note: For component of processing capability Capability 1: Legacy timeline OCPU = Y x N4 x ceil(P/32) ), when P/SP-CSI-RS is configured for CMR OCPU = Y x KDOPP x ceil(P/32)), when A-CSI-RS is configured for CMR Capability 2: Scale the legacy timeline by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = Y x N4, when P/SP-CSI-RS is configured for CMR OCPU = Y x KDOPP, when A-CSI-RS is configured for CMR Note: maximum OCPU is 8 Note: KDOPP is the number of CSI-RS resource groups configured for channel measurement, and each CSI-RS resource groups contain K CSI-RS resources for aggregating up to 128 ports | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508081](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508081.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122bis:9.2:020`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-2-1 | Hybrid BF (CRI-based) with Rel-15 Type-I SP codebook | 1. The maximal supported number of CRI report M 2. A list of supported combinations, each combination is {Max # of Tx ports in one resource, Max # of resources and total # of Tx ports} across all CCs simultaneously. 3. The maximum value of KS | 2-36 | yes | n/a | Hybrid BF (CRI-based) with Rel-15 Type-I SP codebook is not supported | Per band and per BC | n/a | n/a | n/a | Component 1 candidate values: {1,2,3,4} Component 2 candidate values: a. {2,4,8,12,16, 24, 32} b. {1,2,3,4 … 256} c. {64, …, 256, 512, 768, 1024} Component 3 candidate values: {2,3,4,5,6,7,8} | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508081](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508081.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122bis:9.2:021`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-2-2 | Hybrid BF (CRI-based) with Rel-16 eType-II codebook | 1. The maximal supported number of CRI report M 2. A list of supported combinations, each combination is {Max # of Tx ports in one resource, Max # of resources and total # of Tx ports} across all CCs simultaneously. 3. The maximum value of KS | 16-3a | yes | n/a | Hybrid BF (CRI-based) with Rel-16 eType-II codebook is not supported | Per band and per BC | n/a | n/a | n/a | Component 1 candidate values: {1,2} Component 2 candidate values: a. {2,4,8,12,16, 24, 32} b. {1,2,3,4 … 256} c. {64, …, 256, 512, 768, 1024} Component 3 candidate values: {2,3,4,5,6,7,8} | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508081](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508081.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122bis:9.2:023`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-4b | M=2 and R=1 for extended Rel-17 FeType-II PS (port selection) codebook for up to 64 ports | 1. Support M=2 and R=1 for extended Rel-17 FeType-II PS (port selection) codebook for up to 64 ports 2. Support of parameter combinations with M=2 3. A list of supported combinations, each combination is {Max # of Tx ports in a report, Max # of sets of aggregated resources, and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously with M=2 and R=1 | 59-2-1-4 | Yes | n/a | M=2 and R=1 for extended Rel-17 FeType-II PS (port selection) codebook for up to 64 ports is not supported | Per band and Per BC | n/a | n/a | n/a | Component 3 candidate values a. {48, 64} b. {1, 2, …, 64, 128, 256} c. {64, …, 256, 512, 768, 1024} | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508081](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508081.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122bis:9.2:024`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-4c | M=2 and R=2 for extended Rel-17 FeType-II PS (port selection) codebook for up to 64 ports | 1. Support M=2 and R=2 for extended Rel-17 FeType-II PS (port selection) codebook for up to 64ports 2. A list of supported combinations, each combination is {Max # of Tx ports in a report, Max # of sets of aggregated resources, and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously with M=2 and R=2 | 59-2-1-4 | Yes | n/a | M=2 and R=2 for extended Rel-17 FeType-II PS (port selection) codebook for up to 64 ports is not supported | Per band and Per BC | n/a | n/a | n/a | Component 2 candidate values a. {48, 64} b. {1, 2, …, 64, 128, 256} c. {64, …, 256, 512, 768, 1024} | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508081](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508081.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122bis:9.2:025` · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-5c | N4>1 for extended Rel-18 Type-II Doppler codebook for up to 128 ports | 1. Support for the size of DD-basis, N4>1 2. A list of supported combinations, each combination is {Max N4, Max # of Tx ports in a report, Max # of sets of aggregated resources or groups of aggregated resource, and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 3. A list of supported combinations, each combination is {Max N4, Max # of Tx ports in a report, Max # of sets of aggregated resources or groups of aggregated resource, and total # of Tx ports} for one CSI report setting 4. Value of d=m for the DD unit size when A-CSI-RS is configured for CMR | 59-2-1-5 | Yes | n/a | N4>1 for extended Rel-18 Type-II Doppler codebook for up to 128 ports is not supported | Per band and Per BC | n/a | n/a | n/a | Component 2 candidate values a. {1,2,4,8} b. {48, 64,128} c. {1, 2,3,4 … 64, 128, 256} d. {64, …, 256, 512, 768, 1024} Component 3 Candidate values a. {1,2,4,8} b. {48, 64,128} c. {4,8,12} d. {64, …, 256} | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508081](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508081.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122bis:9.2:026`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-5f | PMI subband R=2 for extended Rel-18 Type-II Doppler codebook for up to 128 ports | 1. Support PMI subband R=2 for Rel-18 Type-II Doppler codebook enhancement for up to 128 ports 2. A list of supported combinations, each combination is {Max N4, Max # of Tx ports in a report, Max # of sets of aggregated resources or groups of aggregated resource, and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously with R=2 | 59-2-1-5 | Yes | n/a | PMI subband R=2 for extended Rel-18 Type-II Doppler codebook for up to 128 ports is not supported | Per band and Per BC | n/a | n/a | n/a | Component 2 candidate values a. {1,2,4,8} b. {48, 64,128} c. {1, 2,3,4 … 64, 128, 256} d. {64, …, 256, 512, 768, 1024} | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508081](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508081.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122bis:9.2:027` · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-9 | NES SD Type1 for Rel-19 Type-I single-panel codebook | 1. Support NES SD Type1 for Rel-19 Type-I single-panel codebook 2. Supported NES SD Type1 timeline from two timeline capabilities, for Rel-19 Type-I single-panel codebook 3 Supported number of ports for CSI report subconfig | 59-2-1-1, 1a, 1b, 1c, 1d, or 1e and 42-1,1a, 1b or 1c | Yes | n/a | NES SD Type1 for Rel-19 Type-I single-panel codebook is not supported | [Per-band and per-BC] | n/a | n/a | n/a | Component 2 candidate values: Capability 1: Reuse legacy Z/Z’ values (i.e., Z2 and Z’2) Capability 2 timeline: Scale the legacy timeline Z/Z’ (i.e., Z2 and Z’2) by where M is the number of sub-configurations that refer to the any of the K aggregated CSI-RS resources Component 3 candidate values: One or more values from {2, 4, 8, 12, 16, 24, 32, 48, 64, 128} | Optional with capability signaling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508081](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508081.zip)

**Agreement** · `10.2.2` Enhancing DL CSI acquisition · `RAN1#122bis:10.2.2:002` · 관련 주제: CSI-RS

> For early triggering of CSI/CSI-RS when SCell transition from a dormant BWP to a non-dormant BWP, support aperiodic CSI reporting for the non-dormant BWP, triggered via a DCI indicating switching out of SCell dormancy.
> - The aperiodic CSI reporting is associated with aperiodic CSI-RS for CSI on the non-dormant BWP
> - Legacy DCI format(s) for switching out of SCell dormancy is reused without introducing new DCI field or resizing the existing DCI field
> - FFS: Which DCI format(s) from DCI format 0_1/0_3/1_1/1_3/2_6 is supported
> - FFS: Triggering mechanism(s)
> - FFS: Timeline of the aperiodic CSI reporting and corresponding aperiodic CSI-RS for CSI (requirement is up to RAN4)

남은 FFS 3건

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2506838](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2506838.zip)

**Agreement** · `10.2.2` Enhancing DL CSI acquisition · `RAN1#122bis:10.2.2:003`

> For UE transition from IDLE/INACTIVE to CONNECTED mode, support the followings for aperiodic CSI reporting triggered by MSG4:
> - For PMI-based reporting, support the report quantity ‘CRI-RI-PMI-CQI’
>   - FFS: ‘CRI-RI-LI-PMI-CQI’
> - For PMI-free reporting, support the report quantity ‘CRI-RI-CQI’

남은 FFS 1건

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2506838](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2506838.zip)

**Agreement** · `10.2.2` Enhancing DL CSI acquisition · `RAN1#122bis:10.2.2:006`

> For SCell transition from deactivation to activation, support the followings for aperiodic CSI reporting triggered based on legacy SCell activation command:
> - For PMI-based reporting, support the report quantity ‘CRI-RI-PMI-CQI’
>   - FFS: ‘CRI-RI-LI-PMI-CQI’
> - For PMI-free reporting, support the report quantity ‘CRI-RI-CQI’

남은 FFS 1건

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2506839](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2506839.zip)

**Agreement** · `10.2.2` Enhancing DL CSI acquisition · `RAN1#122bis:10.2.2:007`

> For SCell transition from dormant-BWP to non-dormant BWP, support the followings for aperiodic CSI reporting triggered via a DCI indicating switching out of SCell dormancy:
> - For PMI-based reporting, support the report quantity ‘CRI-RI-PMI-CQI’
>   - FFS: ‘CRI-RI-LI-PMI-CQI’
> - For PMI-free reporting, support the report quantity ‘CRI-RI-CQI’

남은 FFS 1건

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2506839](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2506839.zip)

**Agreement** · `10.2.2` Enhancing DL CSI acquisition · `RAN1#122bis:10.2.2:010` · 관련 주제: CSI-RS

> For early triggering of aperiodic CSI reporting and the associated CSI-RS for CSI when UE transition from IDLE/INACTIVE to CONNECTED mode, support Option-2 as follows:
> - In Step-1, SIBx provides one or multiple CSI report configurations based on one or multiple UE capability assumptions
>   - Each CSI reporting configuration is associated with a CSI resource configuration for channel measurement.
>     - The CSI-RS resource set(s) in the CSI resource configuration for channel measurement is provided with a same number of CSI-RS ports
>   - Each CSI reporting configuration is associated with a CSI resource configuration for CSI-IM based interference measurement.
>   - FFS: Support of NZP CSI-RS based interference measurement
>   - FFS: Information to be provided in a CSI report/resource configuration
> - In Step-2, UE reports through MSG3 which/whether the CSI report configuration(s) provided in SIBx is/are supported.
>   - FFS: How to report which/whether the CSI report configuration(s) provided in SIBx is/are supported.

남은 FFS 3건

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2506840](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2506840.zip)

**Agreement** · `10.2.2` Enhancing DL CSI acquisition · `RAN1#122bis:10.2.2:011` · 관련 주제: CSI-RS

> On PUSCH allocation for MSG4-triggered aperiodic CSI reporting associated with aperiodic CSI-RS for CSI, when UE transition from IDLE/INACTIVE to CONNECTED mode, down select one from the following alternatives to determine PUSCH for carrying the aperiodic CSI report by RAN1#123:
> - Alt-1: The PUSCH is scheduled by MAC CE in MSG4 along with the aperiodic CSI report triggering.
> - Alt-2: The PUSCH is scheduled by a legacy DCI after MSG4
> - Alt-3: The PUSCH is configured by SIBx providing resource/reporting configuration for early triggering of aperiodic CSI reporting.
> Note: The timeline of PUSCH for aperiodic CSI reporting is separately discussed.

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508115](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508115.zip)

## RAN1#122 — 25건

**Agreement** · `8.2.1` Enhancements for UE-initiated/event-driven beam management · `RAN1#122:8.2.1:003`

> Adopt the following changes in Clause 5.2.5 in TS38.214.
> - Reason for change: Reusing the intra-UE multiplexing/prioritization rules of PUSCH with SP-CSI for PUSCH for UEI-BR for Mode B was agreed. However, it is not captured in the current specification on the priority rules of CSI reports.
> - Summary of change: In TS38.214 section 5.2.5, clarify the intra-UE multiplexing/prioritization rules of PUSCH with SP-CSI for PUSCH is reused for UEI-BR for Mode B.
> - Consequences if not approved: UE behavior is not clear when PUSCH carrying UEI-BR for Mode B overlaps with other PUSCHs.
> | 5.2.5 Priority rules for CSI reports <Unchanged parts are omitted> If a UE would transmit a first PUSCH that includes semi-persistent CSI reports or UE initiated CSI report for mode B and a second PUSCH that includes an UL-SCH on the same carrier, and the first PUSCH transmission would overlap in time with the second PUSCH transmission, the UE does not transmit the first PUSCH and transmits the second PUSCH. The UE expects that the first and second PUSCH transmissions satisfy the above timing conditions for PUSCH transmissions that overlap in time when at least one of the first or second PUSCH transmissions is in response to a DCI format detection by the UE. |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506253](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506253.zip)

**Agreement** · `8.2.2` CSI enhancements · `RAN1#122:8.2.2:002`

> For the Rel-19 Type-I SP and Type-II codebook refinement, refine the following agreement in RAN1#121 as follows:

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2505535](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2505535.zip)

**Agreement** · `8.2.2` CSI enhancements · `RAN1#122:8.2.2:003` · 관련 주제: CSI-RS

> For the Rel-19 Type-I SP and Type-II codebook refinement for P=48, 64, and 128 CSI-RS ports with K>1 aggregated NZP aperiodic CSI-RS resources for CMR, to implement the previous agreements on the mapping from CSI-RS resource index/port index per resource and port index to CSI/PMI calculation
> - In TS38.211, extend the enumeration of antenna port p=3000+p’ with p’=0 …P–1
> - In TS38.214, remove the term ‘port index for CSI/PMI calculation’
> Consequently, based on the endorsed version of TS38.214 V19.0.0, the current description for aperiodic CSI-RS resources should also be applied to periodic and semi-persistent CSI-RS resources.
> TPs in Section 3.1 and 3.2 of R1-2505335 for TS 38.214 are endorsed.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2505535](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2505535.zip)

**Conclusion** · `8.2.2` CSI enhancements · `RAN1#122:8.2.2:004` · 관련 주제: CSI-RS

> For the Rel-19 Type-I SP codebook refinement for 48, 64, and 128 CSI-RS ports, joint configuration of the Rel-18 SD NES Type-I, the Rel-19 Type-I SP codebook, and the Rel-19 soft scaling for the Rel-19 Type-I SP codebook is not supported.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506513](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506513.zip)

**Conclusion** · `8.2.2` CSI enhancements · `RAN1#122:8.2.2:005` · 관련 주제: CSI-RS

> For Rel-19 Type-II codebook refinement for 48, 64, and 128 CSI-RS ports based on the Rel-18 Type-II Doppler codebook, following the legacy (Rel-18) principle, a UE shall assume that CSI-RS ports mapped to the same port index  across the K aperiodic CSI-RS resources, , as described in Clause 7.4.1.5.3 of [4, TS 38.211], share the same antenna port.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506513](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506513.zip)

**Conclusion** · `8.2.2` CSI enhancements · `RAN1#122:8.2.2:006` · 관련 주제: CSI-RS

> For the Rel-19 Type-II codebook refinement for 48, 64, and 128 CSI-RS ports, on CBSR, the -bit group-based bitmap is identical for all the  groups

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506513](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506513.zip)

**Conclusion** · `8.2.2` CSI enhancements · `RAN1#122:8.2.2:007` · 관련 주제: CSI-RS

> For the Rel-19 CRI-based CSI refinement for up to 128 CSI-RS ports, when one NZP CSI-RS resource for interference measurement is configured, it is associated with all the KS NZP CSI-RS resources for channel measurement

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506513](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506513.zip)

**Agreement** · `8.2.3` Support for 3-antenna-port codebook-based transmissions · `RAN1#122:8.2.3:005`

> Adopt the following TP for TS 38.214 section 6.2.3.1.
> Reason for change: Correct the PTRS-DMRS association as DCI format 0_3 is not supported for a 3TX UE
> Summary of change: Include a new text without referencing PUSCH port 1003 that is not supported.
> Consequence if not changed: Incomplete/incorrect specification of PTRS-DMRS association.
> | 6.2.3.1 UE PT-RS transmission procedure when transform precoding is not enabled --------------------------------------Unchanged parts are omitted-------------------------------------- For partial-coherent and non-coherent codebook-based UL transmission with 2 or 4 antenna ports, or non-coherent codebook-based UL Transmission with 3 antenna ports, or when the higher layer parameter CodebookTypeUL is set to ‘codebook2’, ‘codebook3’, or ‘codebook4’ with 8 antenna ports, the actual number of UL PT-RS port(s) is determined based on TPMI(s) and/or number of layers which are indicated by 'Precoding information and number of layers' field(s) in DCI format 0_1, 0_2 or 0_3 or configured by higher layer parameter precodingAndNumberOfLayers: if the UE is configured with the higher layer parameter maxNrofPorts in PTRS-UplinkConfig set to 'n2', the actual UL PT-RS port(s) and the associated transmission layer(s) are derived from indicated TPMI(s) as: for PUSCH transmission with 2, 3 or 4 ports, PUSCH antenna port 1000 and 1002 in indicated TPMI(s) share PT-RS port 0, and PUSCH antenna port 1001 and 1003 in indicated TPMI(s) share PT-RS port 1. UL PT-RS port 0 is associated with the UL layer 'x' of layers which are transmitted with PUSCH antenna port 1000 and PUSCH antenna port 1002 in indicated TPMI(s), and UL PT-RS port 1 is associated with the UL layer 'y' of layers which are transmitted with PUSCH antenna port 1001 and PUSCH antenna port 1003 in indicated TPMI(s), where 'x' and/or 'y' are given by DCI parameter 'PTRS-DMRS association' as shown in DCI format 0_1, 0_2 0_3 described in Clause 7.3.1 of [5, TS 38.212]. --------------------------------------Unchanged parts are omitted-------------------------------------- |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506516](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506516.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:001`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-3-1 | PMI sub-bands with R=2 for extended Rel-16 eType-II codebook for up to 128 ports | 1. Support of PMI sub-bands with R=2 for extended Rel-16 eType-II codebook for up to 128 ports 2. A list of supported combinations, each combination is {Max # of Tx ports in a report, Max # of sets of aggregated resources, and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously with R=2 | 59-2-1-3 | Yes | n/a | PMI sub-bands with R=2 for extended Rel-16 eType-II codebook for up to 128 ports is not supported | Per band and Per BC | n/a | n/a | n/a | Component 2 candidate values a. {48, 64, 128} b. {1, …, 64} c. {64, …, 256, 512, 768, 1024} | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:002`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-3-3 | Rank 3,4 for extended Rel-16 eType-II codebook for up to 128 ports | 1. Support of Rank 3,4 for extended Rel-16 eType-II codebook for up to 128 ports 4. Support R=1 5. A list of supported combinations, each combination is {Max # of Tx ports in a report, Max # of sets of aggregated resources, and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously with R=1 | one or more of {59-2-1-3, 59-2-1-3a, 59-2-1-3b} | Yes | n/a | Rank 3,4 for extended Rel-16 eType-II codebook for up to 128 ports is not supported | Per band and Per BC | n/a | n/a | n/a | Component 5 candidate values a. {48, 64, 128} b. {1, 2, …, 64} c. {64, …, 256, 1024} | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:003`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-5f | PMI subband R=2 for extended Rel-18 Type-II Doppler codebook for up to 128 ports | 1. Support PMI subband R=2 for Rel-18 Type-II Doppler codebook enhancement for up to 128 ports 2. A list of supported combinations, each combination is {Max N4, Max # of Tx ports in a report, Max # of sets of aggregated resources or groups of aggregated resource, and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously with R=2 | 59-2-1-5 | Yes | n/a | PMI subband R=2 for extended Rel-18 Type-II Doppler codebook for up to 128 ports is not supported | Per band and Per BC | n/a | n/a | n/a | Component 2 candidate values a.{1,2,4,8} ab {48, 64,128} bc. {2,3,4 … 64} cd. {64, …, 256, 1024} | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:004` · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-5l | Processing timeline for CSI reference slot for extended Rel-18 Type-II Doppler codebook for up to 128 ports | 1. Aperiodic CSI report timing relaxation, w, extended Rel-18 Type-II Doppler codebook for up to 128 ports 2. Aperiodic CSI report timing relaxation, type, for extended Rel-18 Type-II Doppler codebook for up to 128 ports | 59-2-1-5 | Yes | n/a |  | Per band and Per BC | n/a | n/a | n/a | Component 1 candidate values: UE reports candidate value, w, independently for each SCS in unit of symbols: {14*(KP–1)*d, 14*KP*d} Note: Kp is according to Component 12 of FG 59-2-1-5 Note: d=4 (minimum periodicity of periodic CSI-RS) Component 2 candidate values: {CAP1, CAP2} For N4 = 1 1) For AP CSI-RS: (Z,Z’) = (Z2 + 14*( KDOPP –1)*m, Z'2) 2) For P/SP CSI-RS: (Z,Z’) = (Z2 + w, Z'2) For N4 > 1 and CAP1 in component 2 1) For AP CSI-RS: (Z,Z’) = (Z2 + 14*( KDOPP –1)*m, Z'2) 2) For P/SP CSI-RS: (Z,Z’) = (Z2 + w, Z'2) For N4 > 1 and CAP2 in component 2 1) For AP CSI-RS: (Z,Z’) = (Z2 + 14*( KDOPP –1)*m + Z'2, 2Z'2) 2) For P/SP CSI-RS: (Z,Z’) = (Z2 + w + Z'2, 2Z'2) Z2/Z'2 are defined in Table 5.4-2 in TS38.214 KDOPP is the number of CSI-RS resource groups configured for channel measurement, and each CSI-RS resource groups contain K CSI-RS resources for aggregating up to 128 ports M = {1,2}, is the offset between two adjacent AP CSI-RS resource groups for the CMR in slots This FG is not applicable to FR 2-2 | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:007` · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-1 | Enhanced Type-I SP codebook for 64 ports – Scheme-A | 1. Support of enhanced Type-I SP codebook for Scheme-A with 64 Tx ports by aggregating multiple NZP CSI-RS resources within one slot 2. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 3. Supported maximum rank 4. Max # of CSI-RS resource in a resource set 5. Supported processing capability 6. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 2-35 | yes | n/a | Enhanced Type-I SP codebook is not supported for 64 ports – Scheme-A, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 2 candidate values a. {1, …, 64} b. {64, …, 256, 1024} Component 3 candidate value {4, 5, 6, 7, 8} Component 4 candidate value {1:8}{2,4} Component 5 candidate value {Capability 1, Capability 2} Component 6 candidate values a. {1, …, 64} b. {64, …, 256, 1024} Note: For component of processing capability Capability 1: Reuse legacy Z/Z’ values OCPU = ceil(P/32) Capability 2: Scale the legacy timeline Z/Z’ by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = 1 ceil(P/32) | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-1-1a | Enhanced Type-I SP codebook for 48 ports – Scheme-A | 1. Support of enhanced Type-I SP codebook for Scheme-A with 48 Tx ports by aggregating multiple NZP CSI-RS resources within one slot 2. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 3. Supported maximum rank 4. Max # of CSI-RS resource in a resource set 5. Supported processing capability 6. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 59-2-1-1 | yes | n/a | Enhanced Type-I SP codebook is not supported for Scheme-A for 48 Tx ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 2 candidate values a. {1, …, 64} b. {64, …, 256, 1024} Component 3 candidate value {4, 5, 6, 7, 8} Component 4 candidate value {1:8}{2,3} Component 5 candidate value {Capability 1, Capability 2} Component 6 candidate values a. {1, …, 64} b. {64, …, 256, 1024} Note: For component of processing capability Capability 1: Reuse legacy Z/Z’ values OCPU = ceil(P/32) Capability 2: Scale the legacy timeline Z/Z’ by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = 1 ceil(P/32) | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-1-1b | Enhanced Type-I SP codebook for 128 ports – Scheme-A | 1. Support of enhanced Type-I SP codebook for Scheme-A with 128 Tx ports by aggregating multiple NZP CSI-RS resources within one slot 2. A list of supported combinations, each combination is Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 3. Supported maximum rank 4. Max # of CSI-RS resource in a resource set Support 4 CSI-RS resources in a resource set 5. Supported processing capability 6. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 59-2-1-1 | yes | n/a | Enhanced Type-I SP codebook is not supported for Scheme-A for 128 Tx ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 2 candidate values a. {1, …, 64} b. {64, …, 2561024} Component 3 candidate value {4, 5, 6, 7, 8} Component 4 candidate value {1:8} Component 5 candidate value {Capability 1, Capability 2} Component 6 candidate values a. {1, …, 64} b. {64, …, 256, 1024} Note: For component of processing capability Capability 1: Reuse legacy Z/Z’ values OCPU = ceil(P/32) Capability 2: Scale the legacy timeline Z/Z’ by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = 1 ceil(P/32) | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-1-1c | Enhanced Type-I SP codebook for 64 ports – Scheme-B | 1. Support of enhanced Type-I SP codebook for Scheme-B with 64 Tx ports by aggregating multiple NZP CSI-RS resources within one slot 2. A list of supported combinations, each combination is Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 3. Supported maximum rank 4. Max # of CSI-RS resource in a resource set 5. Supported processing capability 6. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 2-35 | yes | n/a | Enhanced Type-I SP codebook is not supported for Scheme-B for 64 Tx ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 2 candidate values a. {1, …, 64} b. {64, …, 256,1024} Component 3 candidate value {4, 5, 6, 7, 8} Component 4 candidate value {1:82,4} Component 5 candidate value {Capability 1, Capability 2} Component 6 candidate values a. {1, …, 64} b. {64, …, 256, 1024} Note: For component of processing capability Capability 1: Reuse legacy Z/Z’ values OCPU = ceil(P/32) Capability 2: Scale the legacy timeline Z/Z’ by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = 1 ceil(P/32) | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-1-1d | Enhanced Type-I SP codebook for 48 ports – Scheme-B | 1. Support of enhanced Type-I SP codebook for Scheme-B with 48 Tx ports by aggregating multiple NZP CSI-RS resources within one slot 2. A list of supported combinations, each combination is Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 3. Supported maximum rank 4. Max # of CSI-RS resource in a resource set 5. Supported processing capability 6. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 59-2-1-1c | yes | n/a | Enhanced Type-I SP codebook is not supported for Scheme-B for 48 Tx ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 2 candidate values a. {1, …, 64} b. {64, …, 256,1024} Component 3 candidate value {4, 5, 6, 7, 8} Component 4 candidate value {1:82,3} Component 5 candidate value {Capability 1, Capability 2} Component 6 candidate values a. {1, …, 64} b. {64, …, 256, 1024} Note: For component of processing capability Capability 1: Reuse legacy Z/Z’ values OCPU = ceil(P/32) Capability 2: Scale the legacy timeline Z/Z’ by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = 1 ceil(P/32) | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-1-1e | Enhanced Type-I SP codebook for 128 ports – Scheme-bB | 1. Support of enhanced Type-I SP codebook for Scheme-B with 128 Tx ports by aggregating multiple NZP CSI-RS resources within one slot 2. A list of supported combinations, each combination is Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 3. Supported maximum rank 4. Max # of CSI-RS resource in a resource set Support 4 CSI-RS resources in a resource set 5. Supported processing capability 6. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 59-2-1-1c | yes | n/a | Enhanced Type-I SP codebook is not supported for Scheme-B for 128 Tx ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 2 candidate values a. {1, …, 64} b. {64, …, 2561024} Component 3 candidate value {4, 5, 6, 7, 8} Component 4 candidate value {1:8} Component 5 candidate value {Capability 1, Capability 2} Component 6 candidate values a. {1, …, 64} b. {64, …, 256, 1024} Note: For component of processing capability Capability 1: Reuse legacy Z/Z’ values OCPU = ceil(P/32) Capability 2: Scale the legacy timeline Z/Z’ by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = 1 ceil(P/32) | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-1-2 | Enhanced Type-I MP codebook for 64 ports | 1. Support of enhanced Type-I MP codebook for 64 ports within 1 slot 2. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 3. Supported maximum number of panels 4. Max # of CSI-RS resource in a resource set 5. Supported processing capability 6. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 2-35 | yes | n/a | Enhanced Type-I MP codebook is not supported for 64 ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 2 candidate values a. {1, …, 64} b. {64, …, 256,1024} Component 3 candidate value {2, 4} Component 4 candidate value {1:82,4} Component 5 candidate value {Capability 1, Capability 2} Component 6 candidate values a. {1, …, 64} b. {64, …, 256, 1024} Note: For component of processing capability Capability 1: Reuse legacy Z/Z’ values OCPU = ceil(P/32) Capability 2: Scale the legacy timeline Z/Z’ by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = 1 ceil(P/32) | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-1-2a | Enhanced Type-I MP codebook for 48 ports | 1. Support of enhanced Type-I MP codebook for 48 ports within 1 slot 2. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 3. Supported maximum number of panels 4. Max # of CSI-RS resource in a resource set 5. Supported processing capability 6. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 59-2-1-2 | yes | n/a | Enhanced Type-I MP codebook is not supported for 48 ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 2 candidate values a. {1, …, 64} b. {64, …, 256,1024} Component 3 candidate value {2, 4} Component 4 candidate value {1:82,3} Component 5 candidate value {Capability 1, Capability 2} Component 6 candidate values a. {1, …, 64} b. {64, …, 256, 1024} Note: For component of processing capability Capability 1: Reuse legacy Z/Z’ values OCPU = ceil(P/32) Capability 2: Scale the legacy timeline Z/Z’ by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = 1 ceil(P/32) | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-1-2b | Enhanced Type-I MP codebook for 128 ports | 1. Support of enhanced Type-I MP codebook for 128 ports within 1 slot 2. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 3. Supported maximum number of panels 4. Max # of CSI-RS resource in a resource set Support 4 CSI-RS resources in a resource set 5. Supported processing capability 6. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 59-2-1-2 | yes | n/a | Enhanced Type-I MP codebook is not supported for 128 ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 2 candidate values a. {1, …, 64} b. {64, …, 2561024} Component 3 candidate value {2, 4} Component 4 candidate value {1:8} Component 5 candidate value {Capability 1, Capability 2} Component 6 candidate values a. {1, …, 64} b. {64, …, 256, 1024} Note: For component of processing capability Capability 1: Reuse legacy Z/Z’ values OCPU = ceil(P/32) Capability 2: Scale the legacy timeline Z/Z’ by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = 1 ceil(P/32) | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-1-3 | Extended Rel-16 eType-II codebook for 64 Tx ports | 1. Support of extended Rel-16 eType-II codebook for 64 Tx ports by aggregating multiple NZP CSI-RS resources within 1 slot 2. Support of parameter combination 1-6 3. Support of rank 1-2 4. Support R=1 5. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously with R=1 6. supported processing capability 7. Max # of CSI-RS resource in a resource set 8. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 16-3a | yes | n/a | Extended Rel-16 eType-II codebook is not supported for 64 Tx ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 5 candidate values a. {1, …, 64, 256} b. {64, …, 256, 1024} Component 6 candidate value {Capability 1, Capability 2} Component 7 candidate value {2,4} Component 8 candidate values a. {1, …, 64} b. {64, …, 256, 1024} Note: For component of processing capability Capability 1: Reuse legacy Z/Z’ values OCPU = ceil(P/32) Capability 2: Scale the legacy timeline Z/Z’ by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = 1 ceil(P/32) | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-1-3a | Extended Rel-16 eType-II codebook for 48 Tx ports | 1. Support of extended Rel-16 eType-II codebook for 48 Tx ports by aggregating multiple NZP CSI-RS resources within 1 slot 2. Support of parameter combination 1-6 3. Support of rank 1-2 4. Support R=1 5. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously with R=1 6. supported processing capability 7. Max # of CSI-RS resource in a resource set 8. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 59-2-1-3 | yes | n/a | Extended Rel-16 eType-II codebook is not supported for 48 Tx ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 5 candidate values a. {1, …, 64, 256} b. {64, …, 256, 1024} Component 6 candidate value {Capability 1, Capability 2} Component 7 candidate value {2,3} Component 8 candidate values a. {1, …, 64} b. {64, …, 256, 1024} Note: For component of processing capability Capability 1: Reuse legacy Z/Z’ values OCPU = ceil(P/32) Capability 2: Scale the legacy timeline Z/Z’ by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = 1 ceil(P/32) | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-1-3b | Extended Rel-16 eType-II codebook for 128 Tx ports | 1. Support of extended Rel-16 eType-II codebook for 128 Tx ports by aggregating multiple NZP CSI-RS resources within 1 slot 2. Support of parameter combination 1-6 3. Support of rank 1-2 4. Support R=1 5. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously with R=1 6. supported processing capability 7. Support 4 CSI-RS resources in a resource set 8. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 59-2-1-3 | yes | n/a | Extended Rel-16 eType-II codebook is not supported for 128 Tx ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 5 candidate values a. {1, …, 64, 256} b. {64, …, 256, 1024} Component 6 candidate value {Capability 1, Capability 2} Component 8 candidate values a. {1, …, 64} b. {64, …, 256, 1024} Note: For component of processing capability Capability 1: Reuse legacy Z/Z’ values OCPU = ceil(P/32) Capability 2: Scale the legacy timeline Z/Z’ by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = 1 ceil(P/32) | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-1-4 | Extended Rel-17 FeType-II codebook with 64 Tx ports | 1. Support of extended Rel-17 FeType-II codebook for 64 Tx ports by aggregating multiple NZP CSI-RS resources within 1 slot 2. Support of parameter combinations with M=1 3. Support of rank 1-2 4. Support R=1 5. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously with M=1 and R=1 6. Supported processing capability 7. Max # of CSI-RS resource in a resource set 8. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 23-9-1 | yes | n/a | Extended Rel-17 FeType-II codebook is not supported with 64 Tx ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 5 candidate values a. {1, …, 64} b. {64, …, 256,1024} Component 6 candidate value {Capability 1, Capability 2} Component 7 candidate value {2,4} Component 6 candidate values a. {1, …, 64} b. {64, …, 256, 1024} Component 8 candidate values a. {1, …, 64} b. {64, …, 256, 1024} Note: For component of processing capability Capability 1: Reuse legacy Z/Z’ values OCPU = ceil(P/32) Capability 2: Scale the legacy timeline Z/Z’ by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = 1 ceil(P/32) | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-1-4a | Extended Rel-17 FeType-II codebook with 48 Tx ports | 1. Support of extended Rel-17 FeType-II codebook for 48 Tx ports by aggregating multiple NZP CSI-RS resources within 1 slot 2. Support of parameter combinations with M=1 3. Support of rank 1-2 4. Support R=1 5. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously with M=1 and R=1 6. Supported processing capability 7. Max # of CSI-RS resource in a resource set 8. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 59-2-1-4 | yes | n/a | Extended Rel-17 FeType-II codebook is not supported with 48 Tx ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 5 candidate values a. {1, …, 64} b. {64, …, 256} Component 6 candidate value {Capability 1, Capability 2} Component 7 candidate value {2,3} Component 8 candidate values a. {1, …, 64} b. {64, …, 256, 1024} Note: For component of processing capability Capability 1: Reuse legacy Z/Z’ values OCPU = ceil(P/32) Capability 2: Scale the legacy timeline Z/Z’ by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = 1 ceil(P/32) | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-1-5 | Extended Rel-18 eType-II Doppler codebook for 64 Tx ports | 1. Support of extended Rel-18 Type-II Doppler codebook for 64 Tx ports by aggregating multiple NZP CSI-RS resource groups within 1 slot 2. Support X=1 CQI based on the first/earliest slot of the CSI reporting window and the first/earliest predicted PMI (TDCQI=’1-1’) 3. Support PMI subband R=1 4. Support parameter combinations with L=2,4 5. Support rank = 1,2 6. Support 64 ports 7. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 8. Supported processing capability 9. Value of Y for CPU occupation when P/SP-CSI-RS is configured for CMR 10. Value of Y for CPU occupation when A-CSI-RS is configured for CMR 11. Support for the size of DD-basis, N4=1 12. Scaling factor for active resource counting Kp 13. Max # of CSI-RS resource in a resource group for aperiodic CSI-RS resource set or in a resource set for periodic CSI-RS resource set 14. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 40-3-2-1 | yes | n/a | Extended Rel-18 Type-II Doppler codebook is not supported for 64 Tx ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 7 candidate values a. {1, …, 64} b. {64, …, 256} Component 8 candidate value {Capability 1, Capability 2} Component 9 candidate values: {1, 2, 3} Component 10 candidate values: {1, 2, 3} Component 12 candidate values: {1, 2, 4} Component 13 candidate value {2,4} Component 14 candidate values a. {1, …, 64} b. {64, …, 256, 1024} Note: For component of processing capability Capability 1: Legacy timeline OCPU = YxN4xceil(P/32) ), when P/SP-CSI-RS is configured for CMR OCPU = Yx KDOPPxceil(P/32)), when A-CSI-RS is configured for CMR Capability 2: Scale the legacy timeline by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = YxN4, when P/SP-CSI-RS is configured for CMR OCPU = Yx KDOPP, when A-CSI-RS is configured for CMR Note: maximum OCPU is 8 Note: KDOPP is the number of CSI-RS resource groups configured for channel measurement, and each CSI-RS resource groups contain K CSI-RS resources for aggregating up to 128 ports | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-1-5a | Extended Rel-18 eType-II Doppler codebook for 48 Tx ports | 1. Support of extended Rel-18 Type-II Doppler codebook for 48 Tx ports by aggregating multiple NZP CSI-RS resource groups within 1 slot 2. Support X=1 CQI based on the first/earliest slot of the CSI reporting window and the first/earliest predicted PMI (TDCQI=’1-1’) 3. Support PMI subband R=1 4. Support parameter combinations with L=2,4 5. Support rank = 1,2 6. Support 64 ports 7. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 8. Supported processing capability 9. Value of Y for CPU occupation when P/SP-CSI-RS is configured for CMR 10. Value of Y for CPU occupation when A-CSI-RS is configured for CMR 11. Support for the size of DD-basis, N4=1 12. Scaling factor for active resource counting Kp 13. Max # of CSI-RS resource in a resource group for aperiodic CSI-RS resource set or in a resource set for periodic CSI-RS resource set 14. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 59-2-1-5 | yes | n/a | Extended Rel-18 Type-II Doppler codebook is not supported for 48 Tx ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 7 candidate values a. {1, …, 64} b. {64, …, 256} Component 8 candidate value {Capability 1, Capability 2} Component 9 candidate values: {1, 2, 3} Component 10 candidate values: {1, 2, 3} Component 12 candidate values: {1, 2, 4} Component 13 candidate value {2,3} Component 14 candidate values a. {1, …, 64} b. {64, …, 256, 1024} Note: For component of processing capability Capability 1: Legacy timeline OCPU = Y x N4 x ceil(P/32) ), when P/SP-CSI-RS is configured for CMR OCPU = Y x KDOPP x ceil(P/32)), when A-CSI-RS is configured for CMR Capability 2: Scale the legacy timeline by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = Y x N4, when P/SP-CSI-RS is configured for CMR OCPU = Y x KDOPP, when A-CSI-RS is configured for CMR Note: maximum OCPU is 8 Note: KDOPP is the number of CSI-RS resource groups configured for channel measurement, and each CSI-RS resource groups contain K CSI-RS resources for aggregating up to 128 ports | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-1-5b | Extended Rel-18 eType-II Doppler codebook for 128 Tx ports | 1. Support of extended Rel-18 Type-II Doppler codebook for 128 Tx ports by aggregating multiple NZP CSI-RS resource groups within 1 slot 2. Support X=1 CQI based on the first/earliest slot of the CSI reporting window and the first/earliest predicted PMI (TDCQI=’1-1’) 3. Support of PMI subband R=1 for extended Rel-18 eType II Doppler codebook 4. Support parameter combinations with L=2,4 5. Support for rank = 1,2 6. Support 64 ports 7. A list of supported combinations, each combination is { Max # of Tx ports in one resource, Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 8. Supported processing capability 9. Value of Y for CPU occupation (OCPU = Y.N4), when P/SP-CSI-RS is configured for CMR 10. Value of Y for CPU occupation (OCPU = Y. KDOPP), when A-CSI-RS is configured for CMR 11. Support for the size of DD-basis, N4=1 12. Scaling factor for active resource counting Kp 13. Support 4 CSI-RS resources in a resource group for aperiodic CSI-RS resource set or in a resource set for periodic CSI-RS resource set 14. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 59-2-1-5 | yes | n/a | Extended Rel-18 Type-II Doppler codebook is not supported for 128 Tx ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 7 candidate values a. {1, …, 64} b. {64, …, 256, 1024} Component 8 candidate value {Capability 1, Capability 2} Component 9 candidate values: {1, 2, 3} Component 10 candidate values: {1, 2, 3} Component 12 candidate values: {1, 2, 4} Component 14 candidate values a. {1, …, 64} b. {64, …, 256, 1024} Note: For component of processing capability Capability 1: Legacy timeline OCPU = Y x N4 x ceil(P/32) ), when P/SP-CSI-RS is configured for CMR OCPU = Y x KDOPP x ceil(P/32)), when A-CSI-RS is configured for CMR Capability 2: Scale the legacy timeline by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = Y x N4, when P/SP-CSI-RS is configured for CMR OCPU = Y x KDOPP, when A-CSI-RS is configured for CMR Note: maximum OCPU is 8 Note: KDOPP is the number of CSI-RS resource groups configured for channel measurement, and each CSI-RS resource groups contain K CSI-RS resources for aggregating up to 128 ports | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:008`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-2-1 | Hybrid BF (CRI-based) with Rel-15 Type-I SP codebook | 1. The maximal supported number of CRI report M 2. A list of supported combinations, each combination is {Max # of Tx ports in one resource, Max # of resources and total # of Tx ports} across all CCs simultaneously. 3. The maximum value of KS | FFS 2-36 | yes | n/a | Hybrid BF (CRI-based) with Rel-15 Type-I SP codebook is not supported | Per band and per BC | n/a | n/a | n/a | Component 1 candidate values: {1,2,3,4} Component 2 candidate values: a. {2,4,8,12,16, 24, 32} b. {1,2,3,4 … 256} c. {64, …, 256, 1024} Component 3 candidate values: {2,3,4,5,6,7,8} | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:009`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-2-2 | Hybrid BF (CRI-based) with Rel-16 eType-II codebook | 1. The maximal supported number of CRI report M 2. A list of supported combinations, each combination is {Max # of Tx ports in one resource, Max # of resources and total # of Tx ports} across all CCs simultaneously. 3. The maximum value of KS | FFS 16-3a | yes | n/a | Hybrid BF (CRI-based) with Rel-16 eType-II codebook is not supported | Per band and per BC | n/a | n/a | n/a | Component 1 candidate values: {1,2} Component 2 candidate values: a. {2,4,8,12,16, 24, 32} b. {1,2,3,4 … 256} c. {64, …, 256, 1024} Component 3 candidate values: {2,3,4,5,6,7,8} | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:014` · 관련 주제: CSI-RS

> Introduce the following Rel. 19 UE FGs (yellow highlighting, if any, shows text that’s not yet agreed)
> | 59. NR_MIMO_Ph5 | 59-2-3-1a | CJTC Dd report processing | 1. Maximum number of configured TRS resource sets for delay offset report 2. Maximum number of configured TRS resource sets for delay offset report across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC 3. Maximum number of simultaneously active CSI-RS resources for delay offset report per CC 4. Maximum number of simultaneously active CSI-RS resources for delay offset report across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC 5. Value of X for CPU occupation (OCPU=XNTRP) | 59-2-3-1 | yes | n/a |  | Per band and Per BC | n/a | n/a | n/a | Component 1 candidate values: {2, 4, 6, 8, 10, 12} Component 2 candidate values: {2, 4, 6, 8, 12, … 64} Component 3 candidate values: {2, 4, 6, 8, 12, 16, 20, 24, 28, 32} Component 4 candidate values: {2, 4, 6, 8, 12, 16, 20, 24, 28, 32, …, 64} Component 5 candidate values: {1, 2} | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-3-2a | CJTC FO report processing | 1. Maximum number of configured TRS resource sets for frequency offset report 2. Maximum number of configured TRS resource sets for frequency offset report across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC 3. Maximum number of simultaneously active CSI-RS resources for frequency offset report per CC 4. Maximum number of simultaneously active CSI-RS resources for frequency offset report across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC 5. Value of X for CPU occupation (OCPU=XNTRP) | 59-2-3-2 | yes | n/a | CJTC FO report is not supported | Per band and Per BC | n/a | n/a | n/a | Component 1 candidate values: {2, 4, 6, 8, 10, 12} Component 2 candidate values: {2, 4, 6, 8, 12, … 64} Component 3 candidate values: {2, 4, 6, 8, 12, 16, 20, 24, 28, 32} Component 4 candidate values: {2, 4, 6, 8, 12, 16, 20, 24, 28, 32, …, 64} Component 5 candidate values: {1, 2} |  |
> | 59. NR_MIMO_Ph5 | 59-2-3-3a | CJTC wideband PO report processing | 1. Maximum number of configured CSI-RS resources for phase offset report 2. Maximum number of configured CSI-RS resources for phase offset report across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC 3. Maximum number of simultaneously active CSI-RS resources for phase offset report per CC 4. Maximum number of simultaneously active CSI-RS resources for phase offset report across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC 5. Value of X for CPU occupation (OCPU=XNTRP) | 59-2-3-3 | yes | n/a | CJTC PO report is not supported | Per band and Per BC | n/a | n/a | n/a | Component 1 candidate values: {2, 4, 6, 8, 10, 12} Component 2 candidate values: {2, 4, 6, 8, 12, … 64} Component 3 candidate values: {2, 4, 6, 8, 12, 16, 20, 24, 28, 32} Component 4 candidate values: {2, 4, 6, 8, 12, 16, 20, 24, 28, 32, …, 64} Component 5 candidate values: {1, 2} | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-3-5a | CJTC Dd+FO report processing | 1. Maximum number of configured TRS resource sets for joint delay and frequency offset report 2. Maximum number of configured TRS resource sets for joint delay and frequency offset report across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC 4. Maximum number of simultaneously active CSI-RS resources for joint delay and frequency offset report per CC 4. Maximum number of simultaneously active CSI-RS resources for joint delay and frequency offset report across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC 5. Value of X for CPU occupation (OCPU=2XNTRP) | 59-2-3-5 | yes | n/a | CJTC Dd+FO report is not supported | Per band and Per BC | n/a | n/a | n/a | Component 1 candidate values: {2, 4, 6, 8, 10, 12} Component 2 candidate values: {2, 4, 6, 8, 12, … 64} Component 3 candidate values: {2, 4, 6, 8, 12, 16, 20, 24, 28, 32} Component 4 candidate values: {2, 4, 6, 8, 12, 16, 20, 24, 28, 32, …, 64} Component 5 candidate values: {1, 2} | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:016` · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-6 | CSI-RS resource time domain restriction for extended Type-I and Type II codebook enhancement for up to 128 ports | Support of the K CSI-RS resources configured within two slots for Type-I and Type II codebook enhancement for up to 128 ports | FFS One or more of {59-2-1-1,1c, 2, 3, 4, 5} | yes | n/a | 2-slot resource aggregation is not supported | Per band and per BC | n/a | n/a | n/a |  | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:017`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-7 | Group-specific 3-bit scaling factors for up to 128 ports | Support of group-specific 3-bit scaling factors | FFS One or more of {59-2-1-1, 59-2-1-1c} | yes | n/a | Group-specific 3-bit scaling factors is not supported | Per band and per BC | n/a | n/a | n/a | Candidate values: {’rank-1’, ‘rank-1 and rank-2’} Note: 3-bit scaling applies only to the Type-I SP codebook | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:019`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-2-3a | Configuration of MR always-reported resources with Rel-15 Type-I SP codebook | Support MR={1,2} for hybrid BF (CRI-based) with Rel-15 Type-I SP codebook | FFS 59-2-2-1 | yes | n/a | Configuration of MR always-reported resources is not supported, i.e. MR=0 with Rel-15 Type-I SP codebook | Per band and per BC | n/a | n/a | n/a |  | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:020`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-2-3b | Configuration of MR always-reported resources with Rel-16 eType-II codebook with R=1 | Support MR={1} for hybrid BF (CRI-based) with Rel-16 eType-II codebook with R=1 | FFS 59-2-2-2 | Yes | n/a | Configuration of MR always-reported resources is not supported, i.e. MR=0 with Rel-16 eType-II codebook with R=1 | Per band and per BC | n/a | n/a | n/a |  | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:024`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-3-7 | Linkage of CJTC Dd and Rel-18 eType-II CJT with joint triggering | 1. Support of joint triggering for linked CJTC Delay offset reporting and Rel-18 eType-II CJT CSI | FFS 59-2-3-1 and 40-3-1-1 | yes | n/a | Linkage of CJTC Dd and Rel-18 eType-II CJT with joint triggering is not supported | Per band and Per BC | n/a | n/a | n/a |  | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:025`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-3-7a | Linkage of CJTC Dd and Rel-18 eType-II CJT with separate triggering | Support separate triggering for linked CJTC Delay offset reporting and Rel-18 eType-II CJT CSI | FFS 59-2-3-1 and 40-3-1-1 | yes | n/a | Separate triggering for linked CJTC Delay offset reporting and Rel-18 eType-II CJT CSI is not supported | Per band and Per BC | n/a | n/a | n/a |  | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:026`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-3-8 | Separate triggering with configuration of 1-bit indicator per CSI trigger state | Support of 1 bit indicate per trigger state for separate triggering of linked DO reporting and Type II CJT reporting | FFS 59-2-3-7a | yes | n/a | Separate triggering with configuration of 1-bit indicator per CSI trigger state is not supported | Per band and Per BC | n/a | n/a | n/a |  | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `10.2.2` Enhancing DL CSI acquisition · `RAN1#122:10.2.2:002` · 관련 주제: CSI-RS

> For UE transition from IDLE/INACTIVE to CONNECTED mode, support aperiodic CSI reporting  triggered via MSG4 of 4-Step RACH based on the followings:
> - The aperiodic CSI reporting is transmitted on PUSCH.
> - Support at least aperiodic CSI-RS for CSI associated with the aperiodic CSI reporting
> - Support PMI-based reporting with wideband PMI based on Rel-15 Type-I SP codebook and wideband CQI
>   - FFS: Which report quantity(s) can be configured
> - Support PMI-free reporting with wideband CQI
>   - FFS: Which report quantity can be configured

남은 FFS 2건

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506539](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506539.zip)

**Agreement** · `10.2.2` Enhancing DL CSI acquisition · `RAN1#122:10.2.2:007` · 관련 주제: CSI-RS

> For early triggering of CSI/CSI-RS when SCell transition from deactivation to activation, support aperiodic CSI reporting for a SCell triggered based on legacy SCell activation command activating the SCell.
> - The aperiodic CSI reporting is assosicated with at least aperiodic CSI-RS for CSI on the SCell
> - FFS: Timeline of the aperiodic CSI reporting and corresponding aperiodic CSI-RS for CSI (requirement is up to RAN4)
> - FFS: How to trigger the aperiodic CSI reporting and corresponding aperiodic CSI-RS for CSI based on legacy SCell activation command?
> - FFS: Whether/what new information is provided in SCell activation command?

남은 FFS 3건

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506583](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506583.zip)

---

## 관련 결정 201건 (주된 주제는 다른 주제)

원문에 CSI 보고/codebook 관련 표현이 있지만 주된 주제가 다른 확정 결정입니다. 전문은 각 주된 주제 리포트에 있습니다.

| 회의 | 구분 | 주된 주제 | Agenda | 원문 첫 줄 | 출처 |
|---|---|---|---|---|---|
| RAN1#126bis | Agreement | [Beam management](beam.md) | 10.5.3.3 Other aspects | Further study and evaluate the following assistant information for use case 2 | [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Other Aspects related to CSI]` |
| RAN1#126bis | Agreement | [SRS](srs.md) | 10.5.3.2 Aspects of uplink-based CSI acquisition | For the study of AI based receiver for SRS overhead reduction, the following template is used as a starting p… | [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of UL based CSI acquisition]` |
| RAN1#126bis | Agreement | [SRS](srs.md) | 10.5.3.2 Aspects of uplink-based CSI acquisition | Study at least the following aspects of TD-OCC: | [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of UL based CSI acquisition]` |
| RAN1#126bis | Agreement | [SRS](srs.md) | 10.5.3.1 Aspects of downlink-based CSI acquisition | For the study/evaluation of early CSI triggering/reporting, the following is considered: | [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of DL based CSI acquisition]` |
| RAN1#126bis | Agreement | [AI/ML CSI](aiml.md) | 10.5.3.1 Aspects of downlink-based CSI acquisition | For the study of time-domain CSI prediction at UE side in 6GR, among UE-side prediction schemes, consider N4=… | [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of DL based CSI acquisition]` |
| RAN1#126bis | Conclusion | [SRS](srs.md) | 9.2 NR MIMO Phase 6 | There is no consensus to support Rel-20 early CSI/SRS/CSI-RS for the case that BWP switching is configured in… | [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · [R1-2607055](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2607055.zip) · `[126bis-R20-MIMO]` |
| RAN1#126bis | Agreement | [SRS](srs.md) | 9.2 NR MIMO Phase 6 | MSG4-triggered CSI/TRS/SRS must be in the initial BWP. | [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · [R1-2607055](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2607055.zip) · `[126bis-R20-MIMO]` |
| RAN1#126bis | Agreement | [SRS](srs.md) | 9.2 NR MIMO Phase 6 | To determine the transmission/reception slot of the DL/UL signalling triggered/scheduled via the DCI indicati… | [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · [R1-2607055](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2607055.zip) · `[126bis-R20-MIMO]` |
| RAN1#126bis | Agreement | [SRS](srs.md) | 9.2 NR MIMO Phase 6 | For early aperiodic SRS/CSI/CSI-RS triggered via SCell activation command or DCI indicating switching out of … | [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · [R1-2607054](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2607054.zip) · `[126bis-R20-MIMO]` |
| RAN1#126bis | Agreement | [SRS](srs.md) | 9.2 NR MIMO Phase 6 | Support a per-cell new RRC parameter to disable/enable Rel-20 early SRS triggering for a SCell switching out … | [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · [R1-2607052](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2607052.zip) · `[126bis-R20-MIMO]` |
| RAN1#126bis | Agreement | [SRS](srs.md) | 9.2 NR MIMO Phase 6 | The first slot as the reference slot in the following agreement is determined based on the numerology of the … | [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · [R1-2607052](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2607052.zip) · `[126bis-R20-MIMO]` |
| RAN1#126bis | Conclusion | [AI/ML CSI](aiml.md) | 9.1.2 Inter-vendor training collaboration for two-sided AI/ML models | For Option 4-1 under Direction A in AI/ML based CSI compression, there is no consensus to support additional … | [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) |
| RAN1#126bis | Agreement | [AI/ML CSI](aiml.md) | 9.1.1 CSI spatial/frequency compression without temporal aspects (“Case 0”) | For CSI feedback via two-sided model, for inference only, support CSI processing timeline {Z+t’, Z’+t’} where… | [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · [R1-2608403](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2608403.zip) |
| RAN1#126bis | Agreement | [AI/ML CSI](aiml.md) | 9.1.1 CSI spatial/frequency compression without temporal aspects (“Case 0”) | For CSI feedback via two-sided model, for inference only, reuse the legacy R19 APU and CPU framework consider… | [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · [R1-2608403](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2608403.zip) |
| RAN1#126bis | Agreement | [AI/ML CSI](aiml.md) | 9.1.1 CSI spatial/frequency compression without temporal aspects (“Case 0”) | Support following configuration for NW data collection | [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) |
| RAN1#126bis | Conclusion | [AI/ML CSI](aiml.md) | 9.1.1 CSI spatial/frequency compression without temporal aspects (“Case 0”) | For CSI feedback via two-sided model, there is no consensus on the need for RAN1 specification impact of CQI. | [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) |
| RAN1#126 | Agreement | [SRS](srs.md) | 10.5.3.3 Other aspects | On top of agreement in RAN1#125, further study and evaluate the following sub use cases for joint DL/UL CSI a… | [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Other Aspects related to CSI]` |
| RAN1#126 | Agreement | [SRS](srs.md) | 10.5.3.3 Other aspects | For the evaluation of joint DL/UL based CSI acquisition, at least take the following baseline for use case 2 | [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Other Aspects related to CSI]` |
| RAN1#126 | Agreement | [SRS](srs.md) | 10.5.3.3 Other aspects | Use the following template to collect the simulation results for use case 2: | [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Other Aspects related to CSI]` |
| RAN1#126 | Agreement | [SRS](srs.md) | 10.5.3.3 Other aspects | Use the following template to collect the simulation results for use case 1: | [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Other Aspects related to CSI]` |
| RAN1#126 | Agreement | [SRS](srs.md) | 10.5.3.3 Other aspects | For the evaluation of joint DL/UL based CSI acquisition, at least take the following baseline for use case 1 | [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Other Aspects related to CSI]` |
| RAN1#126 | Agreement | [SRS](srs.md) | 10.5.3.2 Aspects of uplink-based CSI acquisition | Study at least the following aspects of precoded SRS | [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of UL based CSI acquisition]` |
| RAN1#126 | Agreement | [Beam management](beam.md) | 10.5.3.1 Aspects of downlink-based CSI acquisition | For the evaluation on the benefit of early CSI triggering/reporting, considering the following aspects: | [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of DL based CSI acquisition]` |
| RAN1#126 | Agreement | [Beam management](beam.md) | 10.5.3.1 Aspects of downlink-based CSI acquisition | For the study of explicit CSI feedback, the evaluation considers the following aspects: | [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of DL based CSI acquisition]` |
| RAN1#126 | Agreement | [SRS](srs.md) | 10.5.3.1 Aspects of downlink-based CSI acquisition | For the evaluation of stand-alone reporting for CJT calibration report, consider the following aspects: | [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of DL based CSI acquisition]` |
| RAN1#126 | Agreement | [AI/ML CSI](aiml.md) | 10.5.3.1 Aspects of downlink-based CSI acquisition | For the study of non-AI/AI based CSI prediction in frequency/spatial/time domain at UE or NW side, adopt the … | [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of DL based CSI acquisition]` |
| RAN1#126 | Agreement | [SRS](srs.md) | 10.5.3.1 Aspects of downlink-based CSI acquisition | For 6GR codebook design for CSI report, study whether/how to address near-field (NF) propagation as follows: | [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of DL based CSI acquisition]` |
| RAN1#126 | Agreement | [SRS](srs.md) | 9.2 NR MIMO Phase 6 | On how to indicate the slot offset of MSG4-scheduled PUSCH for aperiodic CSI reporting when UE transition fro… | [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606467](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606467.zip) · `[126-R20-MIMO]` |
| RAN1#126 | Agreement | [SRS](srs.md) | 9.2 NR MIMO Phase 6 | RAN1 conclude that how UE report through MSG3 which/whether the configuration(s), provided in SIB, for early … | [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606466](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606466.zip) · `[126-R20-MIMO]` |
| RAN1#126 | Agreement | [SRS](srs.md) | 9.2 NR MIMO Phase 6 | RAN1 conclude that which SIB is used to carry the resource/reporting configuration(s) for early SRS-AS/CSI/CS… | [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606466](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606466.zip) · `[126-R20-MIMO]` |
| RAN1#126 | Agreement | [SRS](srs.md) | 9.2 NR MIMO Phase 6 | On MAC-CE triggering indication in MSG4 for early SRS/CSI/CSI-RS when UE transition from IDLE/INACTIVE to CON… | [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606464](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606464.zip) · `[126-R20-MIMO]` |
| RAN1#126 | Agreement | [AI/ML CSI](aiml.md) | 9.1.2 Inter-vendor training collaboration for two-sided AI/ML models | For Direction A, Option 3a-1, combination(s) of the configuration parameters to which the exchanged model par… | [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606012](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606012.zip) |
| RAN1#126 | Agreement | [AI/ML CSI](aiml.md) | 9.1.2 Inter-vendor training collaboration for two-sided AI/ML models | For Option 4-1 under Direction A in AI/ML based CSI compression, for the format of the NMSE and SGCS performa… | [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606012](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606012.zip) |
| RAN1#126 | Agreement | [AI/ML CSI](aiml.md) | 9.1.2 Inter-vendor training collaboration for two-sided AI/ML models | For Option 4-1, for a CSI feedback set associated with the -th Target CSI set andthe m-th payload size config… | [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606012](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606012.zip) |
| RAN1#126 | Agreement | [AI/ML CSI](aiml.md) | 9.1.2 Inter-vendor training collaboration for two-sided AI/ML models | For the association between Target CSI and CSI feedback in Option 4-1, support CSI feedback rank as part of e… | [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606012](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606012.zip) |
| RAN1#126 | Agreement | [AI/ML CSI](aiml.md) | 9.1.1 CSI spatial/frequency compression without temporal aspects (“Case 0”) | Support following configuration for inference configuration | [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606362](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606362.zip) |
| RAN1#126 | Agreement | [AI/ML CSI](aiml.md) | 9.1.1 CSI spatial/frequency compression without temporal aspects (“Case 0”) | The following text for Draft LS in R1-2606881 is endorsed. | [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606362](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606362.zip) |
| RAN1#126 | Agreement | [AI/ML CSI](aiml.md) | 9.1.1 CSI spatial/frequency compression without temporal aspects (“Case 0”) | Support L1 signaling for performance monitoring, down-selection from the following alternatives: | [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606361](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606361.zip) |
| RAN1#126 | Agreement | [AI/ML CSI](aiml.md) | 9.1.1 CSI spatial/frequency compression without temporal aspects (“Case 0”) | Send LS to RAN2 to study, and if deemed feasible, specify L3 signaling for performance monitoring, including … | [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606361](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606361.zip) |
| RAN1#125 | Agreement | [SRS](srs.md) | 10.5.3.2 Aspects of uplink-based CSI acquisition | For UL-based CSI in 6GR, study carrier switching and consider at least the following aspects | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of UL based CSI acquisition]` |
| RAN1#125 | Agreement | [SRS](srs.md) | 10.5.3.2 Aspects of uplink-based CSI acquisition | Study at least the following aspects of SRS antenna switching for DL CSI acquisition | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of UL based CSI acquisition]` |
| RAN1#125 | Agreement | [SRS](srs.md) | 10.5.3.2 Aspects of uplink-based CSI acquisition | For the evaluation of scalability/generalization of AI/ML-based UL-based CSI acquisition, the evaluation meth… | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of UL based CSI acquisition]` |
| RAN1#125 | Agreement | [SRS](srs.md) | 10.5.3.2 Aspects of uplink-based CSI acquisition | For the evaluation of AI/ML-based UL-based CSI acquisition, | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of UL based CSI acquisition]` |
| RAN1#125 | Agreement | [SRS](srs.md) | 10.5.3.2 Aspects of uplink-based CSI acquisition | Study the following cases for AI/ML UL-based CSI, and strive to support the unified SRS patterns/designs/fram… | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of UL based CSI acquisition]` |
| RAN1#125 | Agreement | [AI/ML CSI](aiml.md) | 10.5.3.1 Aspects of downlink-based CSI acquisition | For the study on channel property information (CPI), the evaluation at least considering the following: | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of DL based CSI acquisition]` |
| RAN1#125 | Agreement | [AI/ML CSI](aiml.md) | 10.5.3.1 Aspects of downlink-based CSI acquisition | For the study of non-AI/AI based CSI prediction in time domain at UE side, consider the following aspects | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of DL based CSI acquisition]` |
| RAN1#125 | Agreement | [AI/ML CSI](aiml.md) | 10.5.3.1 Aspects of downlink-based CSI acquisition | For the study of non-AI/AI based CSI prediction in frequency/spatial domain at NW side, consider the followin… | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of DL based CSI acquisition]` |
| RAN1#125 | Agreement | [Beam management](beam.md) | 10.5.3.1 Aspects of downlink-based CSI acquisition | At least support NW triggered and/or configured CSI reporting. | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of DL based CSI acquisition]` |
| RAN1#125 | Agreement | [SRS](srs.md) | 10.5.3.1 Aspects of downlink-based CSI acquisition | For study of DMRS-based CSI, considering at least the following aspects: | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of DL based CSI acquisition]` |
| RAN1#125 | Agreement | [SRS](srs.md) | 10.5.3.1 Aspects of downlink-based CSI acquisition | For the study on configurable/downloadable codebook/basis/bases, consider at least the following: | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of DL based CSI acquisition]` |
| RAN1#125 | Agreement | [AI/ML CSI](aiml.md) | 10.5.3.1 Aspects of downlink-based CSI acquisition | For the study of non-AI/AI based CSI prediction in frequency/spatial domain at UE side, consider the followin… | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of DL based CSI acquisition]` |
| RAN1#125 | Agreement | [Beam management](beam.md) | 10.5.2.4 Beam management for downlink and uplink | Support the following table as the assumption of LLS for evaluation of 6GR beam management | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Beam management]` |
| RAN1#125 | Agreement | [Beam management](beam.md) | 10.5.2.4 Beam management for downlink and uplink | Support the following table as the assumption of SLS for evaluation of 6GR beam management | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Beam management]` |
| RAN1#125 | Agreement | [Beam management](beam.md) | 10.5.2.4 Beam management for downlink and uplink | Regarding the scenario of high-speed train, support the following revision in red on the agreement for SLS ev… | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Beam management]` |
| RAN1#125 | Agreement | [SRS](srs.md) | 9.2 NR MIMO Phase 6 | For a MSG4-triggered UL signal (i.e., aperiodic SRS-AS and PUSCH for aperiodic CSI reporting) when UE transit… | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2603720](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2603720.zip) · `[125-R20-MIMO]` |
| RAN1#125 | Agreement | [SRS](srs.md) | 9.2 NR MIMO Phase 6 | When UE transition from IDLE/INACTIVE to CONNECTED mode, the pathloss RS for the MSG4-triggered UL signal (i.… | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2603720](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2603720.zip) · `[125-R20-MIMO]` |
| RAN1#125 | Agreement | [SRS](srs.md) | 9.2 NR MIMO Phase 6 | For early aperiodic SRS-AS/CSI-RS/CSI triggering when UE transition from IDLE/INACTIVE to CONNECTED mode, in … | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2603720](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2603720.zip) · `[125-R20-MIMO]` |
| RAN1#125 | Agreement | [AI/ML CSI](aiml.md) | 9.1.2 Inter-vendor training collaboration for two-sided AI/ML models | For Option 4-1, for a CSI feedback set associated with the -th Target CSI set andthe m-th payload size config… | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2603839](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2603839.zip) |
| RAN1#125 | Agreement | [AI/ML CSI](aiml.md) | 9.1.2 Inter-vendor training collaboration for two-sided AI/ML models | For Option 4-1 under Direction A in AI/ML based CSI compression, when the target CSI is precoding matrix with… | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2603839](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2603839.zip) |
| RAN1#125 | Agreement | [AI/ML CSI](aiml.md) | 9.1.2 Inter-vendor training collaboration for two-sided AI/ML models | For Option 4-1 under Direction A in AI/ML based CSI compression, for CSI feedback type and format, supports: | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2603839](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2603839.zip) |
| RAN1#125 | Agreement | [AI/ML CSI](aiml.md) | 9.1.1 CSI spatial/frequency compression without temporal aspects (“Case 0”) | Support following configuration for candidate UE data collection | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2604679](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2604679.zip) |
| RAN1#125 | Agreement | [AI/ML CSI](aiml.md) | 9.1.1 CSI spatial/frequency compression without temporal aspects (“Case 0”) | In NW data collection, UE reports target CSI according to the configured rank by the NW. | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2604678](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2604678.zip) |
| RAN1#125 | Agreement | [AI/ML CSI](aiml.md) | 9.1.1 CSI spatial/frequency compression without temporal aspects (“Case 0”) | Decide the necessity of target CSI restriction in RAN1 #126 considering the following cases: | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2604677](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2604677.zip) |
| RAN1#125 | Agreement | [AI/ML CSI](aiml.md) | 9.1.1 CSI spatial/frequency compression without temporal aspects (“Case 0”) | For quantization of target CSI for NW side data collection, support amplitude and phase quantization with 3-b… | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2604677](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2604677.zip) |
| RAN1#124bis | Agreement | [SRS](srs.md) | 10.5.3.3 Other aspects | For the purpose of performance evaluation of joint DL/UL based CSI acquisition, study whether and how to mode… | [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Other Aspects related to CSI]` |
| RAN1#124bis | Agreement | [SRS](srs.md) | 10.5.3.3 Other aspects | For the purpose of performance evaluation of joint DL/UL based CSI acquisition, consider the following antenn… | [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Other Aspects related to CSI]` |
| RAN1#124bis | Agreement | [SRS](srs.md) | 10.5.3.3 Other aspects | For the purpose of performance evaluation of joint DL/UL based CSI acquisition, consider the following SRS er… | [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Other Aspects related to CSI]` |
| RAN1#124bis | Agreement | [SRS](srs.md) | 10.5.3.3 Other aspects | At least study the following use case for joint DL/UL CSI acquisition | [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Other Aspects related to CSI]` |
| RAN1#124bis | Agreement | [SRS](srs.md) | 10.5.3.2 Aspects of uplink-based CSI acquisition | For UL-based CSI acquisition, study at least the following aspects of precoded SRS transmission. | [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of UL based CSI acquisition]` |
| RAN1#124bis | Agreement | [SRS](srs.md) | 10.5.3.2 Aspects of uplink-based CSI acquisition | For UL-based CSI acquisition, study at least the following mechanisms of SRS interference mitigation | [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of UL based CSI acquisition]` |
| RAN1#124bis | Agreement | [SRS](srs.md) | 10.5.3.2 Aspects of uplink-based CSI acquisition | For UL-based CSI acquisition, study the following aspects of SRS repetition | [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of UL based CSI acquisition]` |
| RAN1#124bis | Agreement | [AI/ML CSI](aiml.md) | 10.5.3.1 Aspects of downlink-based CSI acquisition | For the study on channel property information (CPI), at least the following is considered. | [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of DL based CSI acquisition]` |
| RAN1#124bis | Agreement | [AI/ML CSI](aiml.md) | 10.5.3.1 Aspects of downlink-based CSI acquisition | For AI based CSI prediction, evaluate generalization/scalability performances of prediction models at least a… | [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of DL based CSI acquisition]` |
| RAN1#124bis | Agreement | [AI/ML CSI](aiml.md) | 10.5.3.1 Aspects of downlink-based CSI acquisition | For the study on JSCM-based CSI compression, at least considering the following aspects on top of previous ag… | [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of DL based CSI acquisition]` |
| RAN1#124bis | Agreement | [AI/ML CSI](aiml.md) | 10.5.3.1 Aspects of downlink-based CSI acquisition | For the study of non-AI/AI based time domain CSI prediction at UE or NW side, consider | [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of DL based CSI acquisition]` |
| RAN1#124bis | Agreement | [AI/ML CSI](aiml.md) | 10.5.3.1 Aspects of downlink-based CSI acquisition | For spatial domain CSI prediction, Baseline #2 is Linear interpolation, where the channel of an unmeasured po… | [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of DL based CSI acquisition]` |
| RAN1#124bis | Agreement | [Beam management](beam.md) | 10.5.2.4 Beam management for downlink and uplink | Support the following table as the basic assumption of LLS for evaluation of 6GR beam management: | [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Beam management]` |
| RAN1#124bis | Agreement | [Beam management](beam.md) | 10.5.2.4 Beam management for downlink and uplink | Support the following table as the assumption of SLS for evaluation of 6GR beam management: | [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Beam management]` |
| RAN1#124bis | Conclusion | [SRS](srs.md) | 9.2 NR MIMO Phase 6 | For early aperiodic SRS/CSI/CSI-RS when UE transition from IDLE/INACTIVE to CONNECTED mode: | [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2602826](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2602826.zip) · `[124b-R20-MIMO]` |
| RAN1#124bis | Agreement | [SRS](srs.md) | 9.2 NR MIMO Phase 6 | For early aperiodic SRS/CSI/CSI-RS when UE transition from IDLE/INACTIVE to CONNECTED mode, support the follo… | [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2602826](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2602826.zip) · `[124b-R20-MIMO]` |
| RAN1#124bis | Agreement | [AI/ML CSI](aiml.md) | 9.1.2 Inter-vendor training collaboration for two-sided AI/ML models | For Option 4-1 under Direction A in AI/ML based CSI compression, | [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2602692](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2602692.zip) |
| RAN1#124bis | Agreement | [AI/ML CSI](aiml.md) | 9.1.2 Inter-vendor training collaboration for two-sided AI/ML models | For Option 4-1 under Direction A in AI/ML based CSI compression, the performance targets are exchanged per la… | [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) |
| RAN1#124bis | Agreement | [AI/ML CSI](aiml.md) | 9.1.2 Inter-vendor training collaboration for two-sided AI/ML models | For Option 4-1 under Direction A in AI/ML based CSI compression, when the target CSI is precoding matrix with… | [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) |
| RAN1#124bis | Agreement | [AI/ML CSI](aiml.md) | 9.1.1 CSI spatial/frequency compression without temporal aspects (“Case 0”) | For performance monitoring: | [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) |
| RAN1#124bis | Agreement | [AI/ML CSI](aiml.md) | 9.1.1 CSI spatial/frequency compression without temporal aspects (“Case 0”) | For NW side data collection, support target CSI quantization | [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) |
| RAN1#124bis | Agreement | [AI/ML CSI](aiml.md) | 9.1.1 CSI spatial/frequency compression without temporal aspects (“Case 0”) | Support two-part UCI for CSI feedback via two-sided model, where | [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) |
| RAN1#124bis | Agreement | [AI/ML CSI](aiml.md) | 9.1.1 CSI spatial/frequency compression without temporal aspects (“Case 0”) | For the standardized SQ codebook when NW does not exchange a codebook, support [1/8, 3/8, 5/8, 7/8] for Q=2 a… | [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) |
| RAN1#124bis | Agreement | [SRS](srs.md) | 8.2 Maintenance on NR MIMO Phase 5 | Send LS to RAN2 to update description of parameter “fourPortSRS-3Tx” in TS 38.331, including, | [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2603256](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603256.zip) · `[124-R19b-MIMO]` |
| RAN1#124bis | Agreement | [SRS](srs.md) | 8.2 Maintenance on NR MIMO Phase 5 | Adopt the following correction in section 6.4.1.4.3 of TS 38.211. | [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2603256](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603256.zip) · `[124-R19b-MIMO]` |
| RAN1#124bis | Agreement | [Beam management](beam.md) | 8.2 Maintenance on NR MIMO Phase 5 | The following TP for Clause 5.2.1.5.4.1 in Rel-19 TS38.214 is endorsed. | [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2603250](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603250.zip) · `[124-R19b-MIMO]` |
| RAN1#124bis | Agreement | [SRS](srs.md) | 8.2 Maintenance on NR MIMO Phase 5 | The following changes in Section 7.5 in TS38.213 are endorsed. | [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2603249](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603249.zip) · `[124-R19b-MIMO]` |
| RAN1#124 | Agreement | [SRS](srs.md) | 10.5.3.2 Aspects of uplink-based CSI acquisition | For LLS for UL-based UL CSI acquisition, reuse the LLS assumption for uplink transmission schemes under AI 10… | [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · `[124-R20-6GR-Aspects of UL based CSI acquisition]` |
| RAN1#124 | Agreement | [SRS](srs.md) | 10.5.3.2 Aspects of uplink-based CSI acquisition | Adopt the assumptions in the following table as the basic assumption of LLS for evaluation of UL-based DL CSI… | [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · `[124-R20-6GR-Aspects of UL based CSI acquisition]` |
| RAN1#124 | Agreement | [SRS](srs.md) | 10.5.3.2 Aspects of uplink-based CSI acquisition | Adopt the assumptions in the following table as the basic assumption of SLS for evaluation of UL-based CSI ac… | [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · `[124-R20-6GR-Aspects of UL based CSI acquisition]` |
| RAN1#124 | Agreement | [SRS](srs.md) | 10.5.3.2 Aspects of uplink-based CSI acquisition | For UL-based CSI acquisition, study at least the following SRS usages: | [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · `[124-R20-6GR-Aspects of UL based CSI acquisition]` |
| RAN1#124 | Agreement | [SRS](srs.md) | 10.5.3.2 Aspects of uplink-based CSI acquisition | Study at least the following aspects of SRS for uplink and downlink CSI acquisition: | [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · `[124-R20-6GR-Aspects of UL based CSI acquisition]` |
| RAN1#124 | Agreement | [AI/ML CSI](aiml.md) | 10.5.3.1 Aspects of downlink-based CSI acquisition | To evaluate the performance of non-AI/AI based CSI prediction at UE side or NW side, consider | [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · `[124-R20-6GR-Aspects of DL based CSI acquisition]` |
| RAN1#124 | Agreement | [AI/ML CSI](aiml.md) | 10.5.3.1 Aspects of downlink-based CSI acquisition | Adopt the following table as the assumptions for LLS for DL based CSI acquisition. | [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · `[124-R20-6GR-Aspects of DL based CSI acquisition]` |
| RAN1#124 | Agreement | [Beam management](beam.md) | 10.5.2.4 Beam management for downlink and uplink | Regarding system-level evaluation of 6GR beam management, in RAN1#124b, , to use the following template as st… | [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · `[124-R20-6GR-Beam management]` |
| RAN1#124 | Agreement | [Beam management](beam.md) | 10.5.2.4 Beam management for downlink and uplink | Study of UE-initiated/event-driven beam management (UEIBM) mechanisms for 6GR, covering at least the followin… | [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · `[124-R20-6GR-Beam management]` |
| RAN1#124 | Agreement | [SRS](srs.md) | 9.2.2 Enhancing DL CSI acquisition | On triggering mechanism for early SRS/CSI-RS/CSI, via a DCI indicating switching out of dormancy for an SCell… | [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2600649](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2600649.zip) |
| RAN1#124 | Agreement | [SRS](srs.md) | 9.2.2 Enhancing DL CSI acquisition | For SCell transition from deactivation to activation, at least support triggering early aperiodic SRS and/or … | [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2600648](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2600648.zip) |
| RAN1#124 | Agreement | [SRS](srs.md) | 9.2.2 Enhancing DL CSI acquisition | To determine the transmission/reception slot of a MSG4-triggered DL/UL signalling (i.e., aperiodic SRS-AS, ap… | [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2600647](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2600647.zip) |
| RAN1#124 | Agreement | [SRS](srs.md) | 9.2.2 Enhancing DL CSI acquisition | To determine the transmission/reception slot of the DL/UL signalling triggered/scheduled based on a legacy SC… | [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2600647](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2600647.zip) |
| RAN1#124 | Agreement | [SRS](srs.md) | 9.2.2 Enhancing DL CSI acquisition | Support a MAC-CE in MSG4 PDSCH for triggering aperiodic SRS-AS/CSI-RS indicates at least | [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2600647](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2600647.zip) |
| RAN1#124 | Agreement | [AI/ML CSI](aiml.md) | 9.1.2 Inter-vendor training collaboration for two-sided AI/ML models | The draft LS R1-2601717 is endorsed with the following changes and re-arrangement of the paragraph before the… | [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601152](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601152.zip) |
| RAN1#124 | Agreement | [AI/ML CSI](aiml.md) | 9.1.2 Inter-vendor training collaboration for two-sided AI/ML models | For Option 4-1 under Direction A in AI/ML based CSI compression, for target CSI format, adopt scalar quantiza… | [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601150](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601150.zip) |
| RAN1#124 | Conclusion | [AI/ML CSI](aiml.md) | 9.1.1 CSI spatial/frequency compression without temporal aspects (“Case 0”) | Configuration of pairing ID in the CSI report for inference is sufficient to distinguish the CSI feedback wit… | [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601254](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601254.zip) |
| RAN1#124 | Conclusion | [AI/ML CSI](aiml.md) | 9.1.1 CSI spatial/frequency compression without temporal aspects (“Case 0”) | There is no consensus on determining the actual payload size of the inference report based on UE indications … | [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601254](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601254.zip) |
| RAN1#124 | Agreement | [AI/ML CSI](aiml.md) | 9.1.1 CSI spatial/frequency compression without temporal aspects (“Case 0”) | For the evaluation of the target CSI format options for NW side data collection, consider following quantizat… | [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601254](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601254.zip) |
| RAN1#124 | Agreement | [AI/ML CSI](aiml.md) | 9.1.1 CSI spatial/frequency compression without temporal aspects (“Case 0”) | Support layer-based UCI mapping and omission. | [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601253](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601253.zip) |
| RAN1#124 | Agreement | [AI/ML CSI](aiml.md) | 9.1.1 CSI spatial/frequency compression without temporal aspects (“Case 0”) | Down-select up to two options from the following options for target CSI format for NW side data collection at… | [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601253](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601253.zip) |
| RAN1#124 | Agreement | [Beam management](beam.md) | 8.2 Maintenance on NR MIMO Phase 5 | Adopt the following changes in Section 5.2.1.4.1 in TS38.214: | [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601519](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601519.zip) · `[124-R19-MIMO]` |
| RAN1#124 | Agreement | [Beam management](beam.md) | 8.2 Maintenance on NR MIMO Phase 5 | Adopt the following changes in Sections 9 and 9.3 in TS 38.213. | [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601519](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601519.zip) · `[124-R19-MIMO]` |
| RAN1#124 | Agreement | [Beam management](beam.md) | 8.2 Maintenance on NR MIMO Phase 5 | Send a reply to the RAN4 LS R4-2511656 clarifying that, for a UE configured with a UEIBM CSI report configura… | [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601518](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601518.zip) · `[124-R19-MIMO]` |
| RAN1#124 | Agreement | [Beam management](beam.md) | 8.2 Maintenance on NR MIMO Phase 5 | Adopt the following changes in Section 5.2.1.4.3 in TS38.214: | [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601518](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601518.zip) · `[124-R19-MIMO]` |
| RAN1#123 | Agreement | [SRS](srs.md) | 10.2.2 Enhancing DL CSI acquisition | On triggering mechanism for early aperiodic SRS-AS transmission on a SCell and early aperiodic CSI reporting … | [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2508520](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2508520.zip) |
| RAN1#123 | Conclusion | [SRS](srs.md) | 10.2.2 Enhancing DL CSI acquisition | For SCell transition from deactivation to activation, there is no RAN1 consensus to support the following cas… | [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2508520](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2508520.zip) |
| RAN1#123 | Conclusion | [SRS](srs.md) | 10.2.2 Enhancing DL CSI acquisition | For UE transition from IDLE/INACTIVE to CONNECTED mode, there is no RAN1 consensus to support the following c… | [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2508520](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2508520.zip) |
| RAN1#123 | Agreement | [AI/ML CSI](aiml.md) | 10.1.2 Inter-vendor training collaboration for two-sided AI/ML models | For Option 4-1 under Direction A in AI/ML based CSI compression: | [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509097](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509097.zip) |
| RAN1#123 | Agreement | [AI/ML CSI](aiml.md) | 10.1.2 Inter-vendor training collaboration for two-sided AI/ML models | When the target CSI is precoding matrix with port-subband domain representation, for the association between … | [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509097](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509097.zip) |
| RAN1#123 | Agreement | [AI/ML CSI](aiml.md) | 10.1.1.2 Other aspects | Support providing Pairing ID(s) in CSI-ReportConfig for UE side data collection | [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509507](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509507.zip) |
| RAN1#123 | Agreement | [AI/ML CSI](aiml.md) | 10.1.1.2 Other aspects | For Option 1 (scalar quantization) of NW side data collection with higher layer reporting, down select betwee… | [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509507](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509507.zip) |
| RAN1#123 | Agreement | [AI/ML CSI](aiml.md) | 10.1.1.2 Other aspects | For NW side data collection with higher layer reporting, regarding Target CSI quantization, Option 1 (Scalar … | [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509507](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509507.zip) |
| RAN1#123 | Agreement | [AI/ML CSI](aiml.md) | 10.1.1.1 Inference related aspects | If target CSI type is pre-coder matrix, at least for SQ, for the PC with rank-1 payload of 384 bits, select o… | [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509215](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509215.zip) |
| RAN1#123 | Agreement | [AI/ML CSI](aiml.md) | 10.1.1.1 Inference related aspects | If target CSI type is pre-coder matrix, at least for SQ, for the PC with rank-1 payload of 64 bits, select on… | [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509215](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509215.zip) |
| RAN1#123 | Agreement | [AI/ML CSI](aiml.md) | 10.1.1.1 Inference related aspects | If target CSI type is pre-coder matrix, at least for SQ, for the PC with rank-1 payload of 256 bits, support … | [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509215](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509215.zip) |
| RAN1#123 | Agreement | [AI/ML CSI](aiml.md) | 10.1.1.1 Inference related aspects | If target CSI type is pre-coder matrix, at least for SQ, for the PC with rank-1 payload of 128 bits, support … | [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509215](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509215.zip) |
| RAN1#123 | Agreement | [AI/ML CSI](aiml.md) | 10.1.1.1 Inference related aspects | If target CSI type is pre-coder matrix, at least support per-layer payload parameter pairs {32, 2}, {64, 2}, … | [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509215](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509215.zip) |
| RAN1#123 | Agreement | [AI/ML CSI](aiml.md) | 10.1.1.1 Inference related aspects | Support NW side optionally exchanges codebook to the UE side. | [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509215](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509215.zip) |
| RAN1#123 | Agreement | [Beam management](beam.md) | 8.2 Maintenance on NR MIMO Phase 5 | Adopt the following changes in Clause 5.2.1.5.4 in TS38.214. | [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2508529](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2508529.zip) · `[123-R19-MIMO]` |
| RAN1#123 | Agreement | [Beam management](beam.md) | 8.2 Maintenance on NR MIMO Phase 5 | Regarding triggering event determination, besides for Candidate#2, at least Candidate #1, and Candidate#7 is … | [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2508529](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2508529.zip) · `[123-R19-MIMO]` |
| RAN1#122bis | Agreement | [SRS](srs.md) | 10.2.2 Enhancing DL CSI acquisition | On triggering mechanism for early aperiodic SRS-AS transmission on a SCell and early aperiodic CSI reporting … | [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508115](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508115.zip) |
| RAN1#122bis | Agreement | [SRS](srs.md) | 10.2.2 Enhancing DL CSI acquisition | For early triggering of SRS-AS when UE transition from IDLE/INACTIVE to CONNECTED mode, support Option-2 as f… | [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2506839](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2506839.zip) |
| RAN1#122bis | Agreement | [SRS](srs.md) | 10.2.2 Enhancing DL CSI acquisition | For early aperiodic SRS-AS/CSI-RS/CSI triggering (i.e., early triggering of aperiodic SRS-AS transmission, ap… | [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2506839](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2506839.zip) |
| RAN1#122bis | Agreement | [SRS](srs.md) | 10.2.2 Enhancing DL CSI acquisition | For UE transition from IDLE/INACTIVE to CONNECTED mode, using MAC-CE in the PDSCH for MSG4 to trigger early a… | [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2506839](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2506839.zip) |
| RAN1#122bis | Agreement | [SRS](srs.md) | 10.2.1 Improvement of SRS capacity and coverage | - Support cross-slot SRS for all SRS resource types, i.e., for periodic, semi-persistent, and aperiodic SRS. | [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508045](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508045.zip) |
| RAN1#122bis | Agreement | [SRS](srs.md) | 10.2.1 Improvement of SRS capacity and coverage | - For intra-repetition hopping for SRS repetition symbols within each SRS frequency, support periodic, semi-p… | [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508045](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508045.zip) |
| RAN1#122bis | Agreement | [AI/ML CSI](aiml.md) | 10.1.2 Inter-vendor training collaboration for two-sided AI/ML models | For Option 4-1 under Direction A in AI/ML based CSI compression, for the association between target CSI and C… | [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2507668](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2507668.zip) |
| RAN1#122bis | Agreement | [AI/ML CSI](aiml.md) | 10.1.2 Inter-vendor training collaboration for two-sided AI/ML models | - For Option 4-1 under Direction A in AI/ML based CSI compression, both average SGCS and average NMSE as perf… | [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2507666](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2507666.zip) |
| RAN1#122bis | Conclusion | [AI/ML CSI](aiml.md) | 10.1.2 Inter-vendor training collaboration for two-sided AI/ML models | For Option 4-1 under Direction A in AI/ML based CSI compression, there is no consensus to further study the n… | [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2507666](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2507666.zip) |
| RAN1#122bis | Agreement | [AI/ML CSI](aiml.md) | 10.1.1.2 Other aspects | For CPU counting of UE side data collection, | [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508031](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508031.zip) |
| RAN1#122bis | Agreement | [AI/ML CSI](aiml.md) | 10.1.1.2 Other aspects | For the study of NW side data collection with higher layer reporting, following evaluation assumptions are co… | [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508030](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508030.zip) |
| RAN1#122bis | Agreement | [AI/ML CSI](aiml.md) | 10.1.1.2 Other aspects | For NW side data collection with higher layer reporting, regarding Option 4 (eType II like codebook with new … | [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508030](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508030.zip) |
| RAN1#122bis | Agreement | [AI/ML CSI](aiml.md) | 10.1.1.2 Other aspects | For NW side data collection with higher layer reporting, for further study of Option 1 (scalar quantization),… | [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508028](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508028.zip) |
| RAN1#122bis | Agreement | [AI/ML CSI](aiml.md) | 10.1.1.1 Inference related aspects | For CSI feedback via two-sided AIML models, reuse legacy CSI reporting framework | [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508023](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508023.zip) |
| RAN1#122bis | Agreement | [AI/ML CSI](aiml.md) | 10.1.1.1 Inference related aspects | When the Target CSI is precoder matrix, in order to down-select to N per-layer payload parameter combinations… | [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508022](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508022.zip) |
| RAN1#122bis | Agreement | [AI/ML CSI](aiml.md) | 10.1.1.1 Inference related aspects | For determining the payload parameters combinations  or   across all layers and ranks, consider following gen… | [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508021](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508021.zip) |
| RAN1#122bis | Agreement | [AI/ML CSI](aiml.md) | 10.1.1.1 Inference related aspects | Support precoding matrix with port-subband domain representation as target CSI type. | [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508021](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508021.zip) |
| RAN1#122bis | Agreement | [SRS](srs.md) | 9.2 UE features for NR MIMO Phase 5 | Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as… | [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508081](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508081.zip) |
| RAN1#122bis | Agreement | [SRS](srs.md) | 8.2 Maintenance on NR MIMO Phase 5 | Adopt the following corrections for TS 38.211, TS 38.213 and TS 38.214. | [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2506791](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2506791.zip) · `[122bis-R19-MIMO]` |
| RAN1#122bis | Agreement | [Beam management](beam.md) | 8.2 Maintenance on NR MIMO Phase 5 | Adopt the following changes in TS38.213 Section 9: | [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508094](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508094.zip) · `[122bis-R19-MIMO]` |
| RAN1#122bis | Agreement | [Beam management](beam.md) | 8.2 Maintenance on NR MIMO Phase 5 | Adopt the following changes in Clause 5.2.1.5.4.1 in TS38.214. | [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508094](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508094.zip) · `[122bis-R19-MIMO]` |
| RAN1#122 | Agreement | [SRS](srs.md) | 10.2.2 Enhancing DL CSI acquisition | For early triggering of SRS-AS/CSI-RS/CSI when UE transition from IDLE to CONNECTED mode, study the following… | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506583](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506583.zip) |
| RAN1#122 | Agreement | [SRS](srs.md) | 10.2.2 Enhancing DL CSI acquisition | For a UE transition from IDLE to CONNECTED mode, support the following procedure at least for early aperiodic… | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506539](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506539.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 10.1.2 Inter-vendor training collaboration for two-sided AI/ML models | For Option 4-1 under Direction A in AI/ML based CSI compression,  if the quantization codebook for CSI feedba… | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506470](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506470.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 10.1.2 Inter-vendor training collaboration for two-sided AI/ML models | For Option 4-1 under Direction A in AI/ML based CSI compression, support exchange of single pairing ID along … | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506470](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506470.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 10.1.2 Inter-vendor training collaboration for two-sided AI/ML models | For Option 4-1 under Direction A in AI/ML based CSI compression, for CSI feedback type and format, down selec… | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506470](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506470.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 10.1.2 Inter-vendor training collaboration for two-sided AI/ML models | For Option 4-1 under Direction A in AI/ML based CSI compression, consider  the following methods for performa… | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506468](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506468.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 10.1.2 Inter-vendor training collaboration for two-sided AI/ML models | For Option 4-1 under Direction A in AI/ML based CSI compression, support at least target CSI and CSI feedback… | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506468](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506468.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 10.1.1 CSI spatial/frequency compression without temporal aspects (“Case 0”) | For NW side data collection, study the solution for quantizing Target CSI, from the aspects of overhead, quan… | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506485](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506485.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 10.1.1 CSI spatial/frequency compression without temporal aspects (“Case 0”) | To enable UE side data collection, CSI-ReportConfig can be used for configuring the resources for data collec… | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506482](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506482.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 10.1.1 CSI spatial/frequency compression without temporal aspects (“Case 0”) | For NW side data collection of CSI compression, discuss the content and format of the collected data by assum… | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506482](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506482.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 10.1.1 CSI spatial/frequency compression without temporal aspects (“Case 0”) | For model pairing procedure for inference, consider the applicability report procedure of Rel-19 AI/ML beam m… | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506482](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506482.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 10.1.1 CSI spatial/frequency compression without temporal aspects (“Case 0”) | For quantization codebook used for quantizing the feedback, | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506498](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506498.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 10.1.1 CSI spatial/frequency compression without temporal aspects (“Case 0”) | For CSI feedback via two-sided model, support at least precoding matrix as target CSI type. | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506496](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506496.zip) |
| RAN1#122 | Agreement | [SRS](srs.md) | 9.2 UE features for NR MIMO Phase 5 | Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as… | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip) |
| RAN1#122 | Agreement | [SRS](srs.md) | 9.2 UE features for NR MIMO Phase 5 | Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as… | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip) |
| RAN1#122 | Agreement | [SRS](srs.md) | 9.2 UE features for NR MIMO Phase 5 | Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as… | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip) |
| RAN1#122 | Agreement | [SRS](srs.md) | 9.2 UE features for NR MIMO Phase 5 | Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as… | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip) |
| RAN1#122 | Agreement | [SRS](srs.md) | 9.2 UE features for NR MIMO Phase 5 | Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as… | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip) |
| RAN1#122 | Agreement | [SRS](srs.md) | 9.2 UE features for NR MIMO Phase 5 | Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as… | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip) |
| RAN1#122 | Agreement | [SRS](srs.md) | 8.2.3 Support for 3-antenna-port codebook-based transmissions | Adopt the following TP for TS 38.214 section 6.2.1.2. | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2505237](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2505237.zip) |
| RAN1#122 | Agreement | [SRS](srs.md) | 8.2.2 CSI enhancements | Adopt the following changes to TS38.214 V19.0.0 Clause 6.2.1.3 on priority rules for UE sounding procedure as… | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2505535](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2505535.zip) |
| RAN1#122 | Agreement | [Beam management](beam.md) | 8.2.1 Enhancements for UE-initiated/event-driven beam management | On beam report transmission procedure for UE-initiated/event-driven beam reporting, occupation time of occupi… | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506255](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506255.zip) |
| RAN1#122 | Agreement | [Beam management](beam.md) | 8.2.1 Enhancements for UE-initiated/event-driven beam management | Adopt the following changes in TS38.214 Section 5.2.1.5.4.1: | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506253](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506253.zip) |
| RAN1#122 | Agreement | [Beam management](beam.md) | 8.2.1 Enhancements for UE-initiated/event-driven beam management | Adopt the following changes in Section 5.4 in TS 38.214. | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506253](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506253.zip) |
| RAN1#122 | Agreement | [Beam management](beam.md) | 8.2.1 Enhancements for UE-initiated/event-driven beam management | Adopt the following changes in TS38.214 Section 5.2.1.5.4.1d: | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506253](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506253.zip) |
| RAN1#122 | Agreement | [SRS](srs.md) | 8.2.1 Enhancements for UE-initiated/event-driven beam management | Adopt the following changes in TS38.213 Section 7.5: | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506253](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506253.zip) |
| RAN1#122 | Agreement | [Beam management](beam.md) | 8.2.1 Enhancements for UE-initiated/event-driven beam management | Adopt the following changes in TS38.213 Section 9.2.5.1: | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506253](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506253.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 8.1.3 Specification support for CSI prediction | For CSI prediction using UE-side model, for UE assisted performance monitoring, | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506572](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506572.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 8.1.3 Specification support for CSI prediction | For CSI-PAI report, support | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506502](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506502.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 8.1.3 Specification support for CSI prediction | For PMI assumption on SGCS calculation of  and  ,support Rel-16 eType II CSI. | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506502](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506502.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 8.1.3 Specification support for CSI prediction | For CSI-PAI report, when the UE is configured with two linked CSI report configurations, adopt UCI padding to… | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506501](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506501.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 8.1.3 Specification support for CSI prediction | The following TP2.6-1 and TP2.6-2 are endorsed as editorial corrections for TS 38.214 for Clauses 5.2.1.4.6 a… | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506501](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506501.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 8.1.3 Specification support for CSI prediction | For CSI prediction, for monitoring report, SP CSI report is only supported on PUSCH. | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506501](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506501.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 8.1.3 Specification support for CSI prediction | For CSI-PAI report, UE is expected to be configured with the same subband configuration with that of inferenc… | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506501](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506501.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 8.1.3 Specification support for CSI prediction | Adopt following TPs for TS38.214 Section 5.2.1.4.6. | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506501](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506501.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 8.1.3 Specification support for CSI prediction | Adopt following TPs for TS38.214 Section 5.2.1.4.6. | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506501](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506501.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 8.1.1 Specification support for beam management | Support the configuration of following parameters in a CSI-ReportConfig with the higher layer parameter repor… | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506453](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506453.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 8.1.1 Specification support for beam management | Adopt the following TP in section 5.2.1.6, TS 38.214. | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506453](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506453.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 8.1.1 Specification support for beam management | Adopt the following TP for TS 38.214 Clause 5.2.2.5. | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506453](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506453.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 8.1.1 Specification support for beam management | Adopt the following TP for TS 38.214 Clause 5.2.2.5. | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506453](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506453.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 8.1.1 Specification support for beam management | For AP CSI report for inference, regarding the associated ID for aperiodic CSI resource setting with multiple… | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506452](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506452.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 8.1.1 Specification support for beam management | Support the following on the reporting condition of CSI reporting for monitoring | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506452](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506452.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 8.1.1 Specification support for beam management | Support the following on the reporting condition of CSI reporting for inference | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506452](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506452.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 8.1.1 Specification support for beam management | For one CSI resource setting for Set A for CSI report for inference for UE-side model | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506452](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506452.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 8.1.1 Specification support for beam management | Adopt the following TP for Clause 6.3.1.1.2 in TS 38.212. | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506451](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506451.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 8.1.1 Specification support for beam management | Adopt the following TP in section 5.2.1.6, TS 38.214. | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506451](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506451.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 8.1.1 Specification support for beam management | Adopt the following TP for CSI reporting for monitoring. | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506451](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506451.zip) |
| RAN1#122 | Agreement | [AI/ML CSI](aiml.md) | 8.1.1 Specification support for beam management | Adopt the following TP for the clarification of ranking information. | [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506451](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506451.zip) |

---

## 후보 104건 (키워드 일치 · 확인 필요)

포함 Agenda 밖에서 키워드로 잡힌 결정입니다. CSI 범위가 아닐 수 있습니다.

### RAN1#126bis — 8건

**Agreement** · `8.1` Maintenance on AI/ML for NR Air interface, NR MIMO Phase 5,  NES and NTN for NR and IoT · `RAN1#126bis:8.1:004` · 후보 · 🆕 신규

> The draft CR in R1-2607797 for Rel-19 TS38.214, Clause 5.2.2.5 is endorsed.
> The corresponding final CR for Rel-19 TS38.214, Clause 5.2.2.5 in R1-2608711 is endorsed.

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R19-AI 8.1]`

**Agreement** · `8.1` Maintenance on AI/ML for NR Air interface, NR MIMO Phase 5,  NES and NTN for NR and IoT · `RAN1#126bis:8.1:009` · 후보 · 🆕 신규

> Proposal 1 in Section 4 of R1-2608695 for Rel-19, TS38.214, Clause 5.2.5 is endorsed.
> The corresponding final CR for Rel-19, TS38.214 in R1-2608703 is endorsed.

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R19-AI 8.1]`

**Agreement** · `8.2` Maintenance on others · `RAN1#126bis:8.2:005` · 후보 · 🆕 신규 · 관련 주제: CSI-RS

> Adopt the following TP for TS38.214 in principle
> | Reason for change: nCSI_ref is determined based on the number of CSI-RS/SSB resources. For L1-CLI-RSSI report, the CLI is measured based on the CLI-RSSI resource rather than CSI-RS/SSB resources. The existing rule for nCSI_ref determination is not applicable for L1 CLI-RSSI report. Summary of change: Clarify nCSI_ref for L1-CLI-RSSI report as follows: If a single CLI-RSSI measurement resource is configured for interference measurement, nCSI_ref is the smallest value greater than or equal to , such that it corresponds to a valid downlink slot. If multiple CLI-RSSI measurement resources are configured for interference measurement, nCSI_ref is the smallest value greater than or equal to , such that it corresponds to a valid downlink slot. Consequences if not approved: UE behavior for nCSI_ref determination of LI-CLI-RSSI report is unclear. |
> | 5.2.2.5 CSI reference resource definition The CSI reference resource for a serving cell is defined as follows: - In the frequency domain, the CSI reference resource is defined by the group of downlink physical resource blocks corresponding to the band to which the derived CSI relates. - In the time domain, the CSI reference resource for a CSI reporting in uplink slot n', or a CSI reporting in an OCC group starting in uplink slot n' if OCC is enabled, is defined by a single downlink slot , where is a parameter configured by higher layer as specified in clause 4.2 of [6, TS 38.213], and where is the subcarrier spacing configuration for with a value of 0 for frequency range 1 and for FR2-NTN, - where and and are the subcarrier spacing configurations for DL and UL, respectively, and and are determined by higher-layer configured ca-SlotOffset for the cells transmitting the uplink and downlink, as defined in clause 4.5 of [4, TS 38.211] - where for periodic and semi-persistent CSI reporting or for periodic CLI RSSI reporting - if a single CSI-RS/SSB resource is configured for channel measurement or if a single CLI-RSSI measurement resource is configured for interference measurement, nCSI_ref is the smallest value greater than or equal to , such that it corresponds to a valid downlink slot, or - if multiple CSI-RS/SSB resources are configured for channel measurement or if multiple CLI-RSSI measurement resources are configured for interference measurement, nCSI_ref is the smallest value greater than or equal to , such that it corresponds to a valid downlink slot. If a CSI-ReportConfig is configured with the higher layer parameter codebookType set to 'typeI-SinglePanel-r19', with total number of CSI-RS ports , for capability 2, as reported by UE capability indication, nCSI_ref is the smallest value greater than or equal to , such that it corresponds to a valid downlink slot. |
> Final CR in R1-2608747 is agreed.

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · [R1-2608698](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2608698.zip) · `[126bis-R19-AI 8.2]`

**Agreement** · `8.2` Maintenance on others · `RAN1#126bis:8.2:010` · 후보 · 🆕 신규 · 관련 주제: CSI-RS

> Adopt the following TP to TS38.214 Section 5.2.4a in principle
> | Reason for change: | Clause 5.2.4a specifies early CSI acquisition for both LTM and L3 handover. In the first paragraph, "candidate cell" is used for LTM and "target cell" is used for handover. However, in the remaining part of the clause, the CSI-IM association, the number of NZP-CSI-RS resources for channel measurement, and the PUSCH used for the CSI report are described only for a candidate cell, although the same procedures apply to the target cell for handover. |
> |  |  |
> | Summary of change: | In clause 5.2.4a, "or the target cell" is added where only "candidate cell" is used, so that the early CSI reporting procedure applies to both LTM and handover. |
> |  |  |
> | Consequences if not approved: | The early CSI reporting procedure for handover is not fully specified in clause 5.2.4a, since the CSI-IM association and the PUSCH for the CSI report are described only for a candidate cell. This may lead to ambiguous or incorrect implementation of early CSI reporting for handover. |
> | ==============First change============== 5.2.4a CSI Reporting for LTM and handover A UE configured with LTM-Config can be provided configurations for CSI acquisition, by up to one Reporting Setting, ltm-CSI-ReportConfig, for a candidate cell. A UE can be provided configuration for CSI acquisition, by one Reporting Setting, earlyCSI-Acquisition in ReconfigurationWithSync, for a target cell. Each Reporting Setting ltm-CSI-ReportConfig or earlyCSI-Acquisition is associated with either one or two Resource Settings - When one Resource Setting (given by higher layer parameter ltm-ResourcesForChannelMeasurement or early-NZP-CSI-RS-ResourceSet) is configured, it provides a list of NZP CSI-RS resources for both channel and interference measurements. The UE is not expected to be configured with more than 128 NZP CSI-RS ports in the CSI-RS resource set contained within the Resource Setting. - When two Resource Settings are configured, the first Resource Setting (given by higher layer parameter ltm-ResourcesForChannelMeasurement or early-NZP-CSI-RS-ResourceSet) provides a list of NZP CSI-RS resources for channel measurement, and the second Resource Setting (given by higher layer parameter ltm-ResourceForInterferenceMeasurements or early-CSI-IM-ResourceSet), provides a list of CSI-IM resources for interference measurement. The UE is not expected to be configured with more than 128 NZP CSI-RS ports in the CSI-RS resource set contained within the Resource Setting. The Resource Setting given by higher layer parameter ltm-ResourcesForChannelMeasurement, LTM-CSI-ResourceConfig, contains configuration of a LTM-NZP-CSI-RS-ResourceSet which comprises of a list of Z ≥ 1 NZP CSI-RS resource indices (given by ltm-CSI-RS-ResourceList) and a list of Z LTM-CandidateIds (given by ltm-CandidateIdList) referring to candidate cells associated with the NZP CSI-RS resource indices. For CSI acquisition associated with a Reporting Setting, ltm-CSI-ReportConfig, the UE is expected to measure the NZP-CSI-RS resources in ltm-CSI-RS-ResourceList associated with the LTM-CandidateId that is equal to the LTM-CandidateId of the LTM-Candidate under which the Reporting Setting is configured. If interference measurement is performed on CSI-IM, each NZP-CSI-RS resource the UE is expected to measure for channel measurement for a candidate cell is resource-wise associated with a CSI-IM resource for the same candidate cell by the ordering of the NZP-CSI-RS resources and CSI-IM resources in the corresponding resource sets. The number of NZP-CSI-RS resources the UE is expected to measure for channel measurement for a candidate cell equals to the number of CSI-IM resources for interference measurement. The UE shall expect the following configuration provided by ltm-CSI-ReportConfig or earlyCSI-Acquisition: - For the frequency granularity of the CSI report, the CQI format indicator is Wideband CQI. - For the frequency granularity of the CSI report, the PMI format indicator is Wideband PMI. - The codebook type is typeI-SinglePanel. - The reportQuantity is set to ‘cri-RI-PMI-CQI’. After a UE receives an LTM Cell Switch Command MAC CE [10, TS 38.321] providing a candidate cell (given by Target Configuration ID field), and a ltm-CSI-ReportConfig is configured for the candidate cell, the UE can measure corresponding NZP CSI-RS resources and CSI-IM resources if configured/activated, and shall transmit a CSI report to the candidate cell. After a UE receives a ReconfigurationWithSync configured with earlyCSI-Acquisition, the UE can measure corresponding NZP CSI-RS resources and CSI-IM resources if configured/activated, and shall transmit a CSI report to the target cell. For RACH-less LTM cell switch or RACH-less handover [23, TS 38.300], the UE shall transmit the CSI report to the candidate cell using the first PUSCH corresponding to a dynamic grant or a configured grant [6, TS 38.213]. For RACH-based LTM cell switch or RACH-based handover using a contention-free random access procedure [23, TS 38.300], the UE shall transmit the CSI report to the candidate cell using the PUSCH scheduled by the RAR UL grant or MsgA PUSCH. For RACH-based LTM cell switch or RACH-based handover using a contention-based random access procedure [23, TS 38.300], the UE shall transmit the CSI report to the candidate cell using the first PUSCH corresponding to a dynamic grant or a configured grant after the HARQ-ACK transmission having ACK value corresponding to PDSCH scheduled by a PDCCH transmission addressed to the C-RNTI that is received in response to MSG A, or the first PUSCH scheduled by a PDCCH transmission addressed to the C-RNTI, received in response to Msg3 or MsgA. For the PUSCH determined for CSI reporting, when the UE applies PUSCH repetition Type A or Type B, the CSI report is transmitted only on the first repetition for PUSCH repetition Type A, or on the first actual repetition for PUSCH repetition Type B. If a valid CSI is not available, the UE shall transmit a CSI report which contains a CQI corresponding to the lowest CQI index. Depending on the UE capability, the UE may measure NZP CSI-RS resources and CSI-IM resources if configured/activated corresponding to a ltm-CSI-ReportConfig before receiving the LTM Cell Switch Command MAC CE [10, TS 38.321]. ==============End of change============== |
> Final CR in R1-2608766 is agreed.

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · [R1-2608653](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2608653.zip) · `[126bis-R19-AI 8.2]`

**Agreement** · `8.2` Maintenance on others · `RAN1#126bis:8.2:011` · 후보 · 🆕 신규 · 관련 주제: CSI-RS

> Adopt the following TP to TS38.214 Section 5.2.1.4.2 in principle
> | Reason for change: | SSBRI and CRI (the highlighted part below) are used in event triggered L1 measurement report (TS 38.321 clause 5.35.1, 5.35.4, 6.1.3.84), which is associated with LTM-CSI-ReportConfig with ltm-ReportConfigType set to ‘eventTriggered’ and with reportquantity set to ssb-index-RSRP or cri-RSRP (the highlighted part below). However SSBRI and CRI (with definition highlighted below) are not defined when ltm-ReportConfigType is set to ‘eventTriggered’ (the highlighted condition below), as from RAN1 TS 38.214 clause 5.2.1.4.2: A CR to TS 38.321 was submitted to RAN2-135 meeting, it was discussed in RAN2, and the conclusion is ‘Noted. Interesting company can submit RAN1 correction’. |
> |  |  |
> | Summary of change: | Add definition of SSBRI and CRI for the case that ltm-ReportConfigType set to ‘eventTriggered’. |
> |  |  |
> | Consequences if not approved: | It remains unclear which index of SSB / CSI-RS is referred by SSBRI / CRI. |
> | ==============First change============== 5.2.1.4.2 Report quantity configurations <Unchanged part omitted> If a UE is configured with a ltm-CSI-ReportConfig with ltm-ReportConfigType which is set to ‘periodic’ or ‘semiPersistentOnPUCCH’ or ‘semiPersistentOnPUSCH’ or ‘aperiodic’, - if the UE is configured with spCellInclusion with reportQuantity set to 'ssb-Index-RSRP', the UE shall report in a single reporting instance nrOfReportedRS-PerCell different SSBRI for the current SpCell and each of the nrOfReportedCells -1 candidate cells. Otherwise, the UE shall report in a single reporting instance nrOfReportedRS-PerCell different SSBRI for each of the nrOfReportedCells candidate cells, - where SSBRI k (k ≥ 0) corresponds to the configured (k+1)-th entry of the associated ltm-SSB-ResourceList in the corresponding ltm-SSB-ResourceSet, - if spCellInclusion is configured, SSB resources in ltm-SSB-ResourceList associated with the current SpCell are the entries where PCI (given by ltm-CandidatePCI) and frequency information (given by ssb-Frequency) of the candidate cell associated with the LTM-CandidateId (given by the corresponding entry in ltm-CandidateIdList) is equal to the PCI and center frequency of cell-defining SSB of the current SpCell. - if the UE is configured with spCellInclusion with reportQuantity set to 'cri-RSRP’, the UE shall report in a single reporting instance nrOfReportedRS-PerCell different CRI for the current SpCell and each of the nrOfReportedCells -1 candidate cells. Otherwise, the UE shall report in a single reporting instance nrOfReportedRS-PerCell different CRI for each of the nrOfReportedCells candidate cells, - where CRI k (k ≥ 0) corresponds to the configured (k+1)-th entry of the associated ltm-CSI-RS-ResourceList in the corresponding LTM-NZP-CSI-RS-ResourceSet, - if spCellInclusion is configured, NZP-CSI-RS resources in ltm-CSI-RS-ResourceList associated with the current SpCell are the entries where PCI (given by ltm-CandidatePCI) and frequency information (given by ssb-Frequency for the SSBs QCLed with NZP-CSI-RSs) of the candidate cell associated with the LTM-CandidateId (given by the corresponding entry in ltm-CandidateIdList)) is equal to the PCI and center frequency of cell-defining SSB of the current SpCell. If the UE is configured with a CSI-ReportConfig that contains a list of sub-configurations provided by csi-ReportSubConfigToAddModList, the UE can only be configured with NZP CSI-RS for interference measurement if each sub-configuration is configured with powerOffset and not configured with portSubsetIndicator. ==============End of change============== |
> Final CR in R1-2608767 is agreed.
> XR Phase 3

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · [R1-2608653](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2608653.zip) · `[126bis-R19-AI 8.2]`

**Agreement** · `10.3.2` Modulation · `RAN1#126bis:10.3.2:002` · 후보 · 🆕 신규

> For performance study to allow a single spectrum efficiency point (subject to quantization error) to be supported by multiple  pairs, both fixed SE simulations and simulations with link adaptation are needed.
> - The performance study is to identify if the preferred  pair changes with respect to channel profile, rank, spatial-layer imbalance, receiver type, Doppler, EVM, UL power back-off, and LDPC code
>   - FFS: Other factors that may affect the preferred  pair choice
> - For channels to be evaluated
>   - The set of fading channels include: CDL-A 100ns, CDL-B 30ns, CDL-C 300ns, CDL-D 30ns
>     - Other fading channel can be included in the set, per company report
>   - The set of MIMO schemes include: SIMO 1x4 (UL), MIMO 4x4 (DL), MIMO 2x4 (UL), MIMO32x4 (DL), MIMO2x32 (UL)
>     - Other MIMO schemes can be included in the set, per company report
> - Precoder assumption: Closed loop precoder. Open loop precoder for high Doppler channels (at least 200Hz).
> - CW to layer mapping: NR CW to layer mapping as baseline.
>   - Other CW to layer mapping can be reported
> - LDPC: NR BG1/BG2 as baseline
>   - BG3 results can be reported.
> - For UL, both DFTs and CP-OFDM waveform can be evaluated
>   - Other waveform can be reported
> - For fixed SE simulations
>   - The SE points of current NR are used as starting point of the evaluation. For each SE point, can evaluate MCS with one step higher modulation order (if applicable) and MCS with one step lower modulation order (if applicable), with coding rate adjusted to maintain the SE to be the same (subject to quantization error).
>   - If more than one step higher/lower modulation order evaluated, please add more columns to the table
> - For link level simulation with link adaptation (prioritize fading channel) for a set of fading channels and MIMO schemes:
>   - Performance report in the form of SNR and the corresponding achieved spectrum efficiency with and without a single spectrum efficiency point to be supported by multiple  pairs
>   - Report the MCS table used with one single spectrum efficiency point supported by multiple  pairs
>   - Report the SNR for rank switching points with rank adaptation
>   - Report the supporting CQI design and/or mechanism for gNB to select between different MCS entries corresponding to the same SE point.
> - When reporting results, please also provide
>   - If applicable, EVM, power back-off assumption for each modulation order or each MCS
>   - Receiver used (MMSE or rML(DL))
>   - Demapping/decoding complexity difference with respect to NR MCS for fixed SE evaluations

남은 FFS 1건

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · [R1-2608656](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2608656.zip) · `[126bis-R20-6GR-Modulation, joint channel coding and modulation]`

**Agreement** · `10.5.2.3` Uplink transmission scheme(s) for uplink channels · `RAN1#126bis:10.5.2.3:012` · 후보 · 🆕 신규

> For the study on downloadable UL codebook for codebook based PUSCH transmission for 6GR, the following is considered for evaluation:
> - Each precoder matrix , where  is a P-dimensional precoding vector for layer , and  is the number of layers, where P is the number of UE antenna ports.
>   - (wideband, FFS: subband) is indicated by NW, e.g., via DCI field, from a set of precoder(s) of the downloadable codebook configured to the UE.
> - Company reports the number of precoders per rank of the downloadable codebook
> - Companies report how to satisfy UE power constraints (e.g., Using  where its elements are constant modulus)
> - Companies report which/how coherent types of UL precoder are supported
> - Companies report the element/vector/matrix quantization assumption, if applicable (e.g., per element phase/amplitude (if any) scalar quantization
> - Companies report how the NW determines downloadable UL codebook and its correspondent computational complexity when NW determines
>   - Encourage companies to report the detail procedure of determination of downloadable codebook, and which information is used for determination (if applicable) as much as possible
> - Companies report signalling overhead, representing format of downloadable codebook, updated frequency of the downloadable codebook, how to determinate when to update

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · [R1-2607567](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2607567.zip) · `[126bis-R20-6GR-Transmission scheme for UL channels]`

**Agreement** · `10.5.2.3` Uplink transmission scheme(s) for uplink channels · `RAN1#126bis:10.5.2.3:014` · 후보 · 🆕 신규

> For the study of DL/UL reciprocity based PUSCH transmission for 6GR, companies to report the following
> - Sensitivity of performance to DL/UL reciprocity calibration error comparing the case of zero reciprocity calibration error
> - Performance comparison between NR codebook based PUSCH and DL/UL reciprocity based PUSCH transmission with DL/UL reciprocity calibration error value(s)

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · [R1-2607568](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2607568.zip) · `[126bis-R20-6GR-Transmission scheme for UL channels]`

### RAN1#126 — 15건

**Agreement** · `7` Pre-Rel-19 NR Maintenance · `RAN1#126:7:006` · 후보

> The draft CR for TS38.214 in R1-2605800 is endorsed in principle with removing “'codebook'/” from the revision.
> Final CRs in R1-2606917 for Rel-18 and in R1-2606918 for Rel-19 are endorsed.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2605800](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2605800.zip)

**Agreement** · `8.1` Maintenance on AI/ML for NR Air interface, NR MIMO Phase 5,  NES and NTN for NR and IoT · `RAN1#126:8.1:001` · 후보 · 관련 주제: CSI-RS

> The following TP for TS 38.214 Clause 5.2.1.6 is endorsed.
> The corresponding CR for Rel-19, TS 38.214 in R1-2606870 is endorsed.
> | Reason for change | Incorrectly capture of previous agreement. |
> | Summary of change | To align with the agreement made in RAN1#122, remove “consecutive” from CPU occupancy duration for SP CSI-PAI report. |
> | Consequences if not approved | The current specification would contain an inaccurate description of CPU occupancy duration for SP CSI-PAI report. |
> | 5.2.1.6 CSI processing criteria ============================= unchanged parts are omitted ============================ For a CSI report with CSI-ReportConfig with higher layer parameter reportQuantity not set to 'none', or a CSI report with LTM-CSI-ReportConfig, or reportQuantity not set to 'none-bm-r19' or 'none-csi-r19', the CPU(s) (including and/or , for CSI reports with reportQuantity set to 'p-cri-r19', 'p-cri-RSRP-r19', 'p-ssb-index-r19', or 'p-ssb-index-RSRP-r19', and CSI reports configured with the higher layer parameter csi-InferencePrediction-r19, and for CSI report with reportQuantity set to 'rs-pai-r19' or 'csi-pai-r19') are occupied for a number of OFDM symbols as follows: - A periodic or semi-persistent CSI report (excluding an initial semi-persistent CSI report on PUSCH after the PDCCH triggering the report, a semi-persistent CSI report on PUSCH configured with reportQuantity set to 'csi-pai-r19', and a semi-persistent CSI report on PUSCH configured with the higher layer parameter codebookType set to 'typeII-Doppler-r18' or 'typeII-Doppler-PortSelection-r18') occupies CPU(s) from the first symbol of the earliest one of each CSI-RS/CSI-IM/SSB resource, or each CSI-RS/CSI-IM resource associated with all configured sub-configurations for periodic CSI report corresponding to a CSI-ReportConfig that contains a list of sub-configurations provided by csi-ReportSubConfigToAddModList, or each CSI-RS/CSI-IM resource associated with all activated/triggered sub-configurations for semi-persistent CSI report corresponding to a CSI-ReportConfig that contains a list of sub-configurations provided by csi-ReportSubConfigToAddModList, for channel or interference measurement, respective latest CSI-RS/CSI-IM/SSB occasion no later than the corresponding CSI reference resource, until the last symbol of the configured PUSCH/PUCCH carrying the report. - An aperiodic CSI report occupies CPU(s) from the first symbol after the PDCCH triggering the CSI report until the last symbol of the scheduled PUSCH carrying the report. When the PDCCH reception includes two PDCCH candidates from two respective search space sets, as described in clause 10.1 of [6, TS 38.213], for the purpose of determining the CPU occupation duration, the PDCCH candidate that ends later in time is used. - An initial semi-persistent CSI report on PUSCH after the PDCCH trigger occupies CPU(s) from the first symbol after the PDCCH until the last symbol of the scheduled PUSCH carrying the report. When the PDCCH reception includes two PDCCH candidates from two respective search space sets, as described in clause 10.1 of [6, TS 38.213], for the purpose of determining the CPU occupation duration, the PDCCH candidate that ends later in time is used. - A semi-persistent CSI report on PUSCH configured with the higher layer parameter codebookType set to 'typeII-Doppler-r18' or 'typeII-Doppler-PortSelection-r18' occupies CPU(s) from the first symbol of KP-th latest consecutive periodic/semi-persistent CSI-RS occasions no later than CSI reference resource, until the last symbol of the PUSCH carrying the report, where the value of is indicated by UE capability. - A semi-persistent CSI report on PUSCH configured with reportQuantity set to 'csi-pai-r19' occupies CPU(s) from the first symbol of the latest consecutive periodic/semi-persistent CSI-RS occasion of a corresponding linked CSI report (linked by inferenceReportConfigId-r19) no later than CSI reference resource of the linked CSI report, until the last symbol of the PUSCH carrying the CSI-PAI report. ============================= unchanged parts are omitted ============================ |

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606794](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606794.zip) · `[126-R19-AI 8.1]`

**Agreement** · `8.1` Maintenance on AI/ML for NR Air interface, NR MIMO Phase 5,  NES and NTN for NR and IoT · `RAN1#126:8.1:006` · 후보

> The following changes for Clause 9 in TS 38.213 is endorsed.
> The corresponding CR for Rel-19, TS 38.213 in R1-2606869 is endorsed.
> - Reason for change:  UE behaviour is unclear for overlapping PUCCH with UEIRI and other channels/signals.
> - Summary of change: Reuse the same behaviour as SR for overlapping PUCCH with UEIRI and other channels/signals.
> - Consequences if not approved: Unclear UE behaviour.
> | 9 UE procedure for reporting control information <Unchanged parts are omitted> If a UE is configured for NR-DC operation, the UE does not expect to be configured with a PUCCH-SCell. For the remaining of this clause, unless stated otherwise, any reference to SR is applicable for LRR and/or for UEIRI. A PUSCH or a PUCCH transmission other than PUCCH transmissions with SL HARQ-ACK reports, including repetitions if any, can be of priority index 0 or of priority index 1. For a configured grant PUSCH transmission, a UE determines a priority index from phy-PriorityIndex, if provided. For a PUCCH transmission with HARQ-ACK information corresponding to a SPS PDSCH reception or a SPS PDSCH release, a UE determines a priority index from harq-CodebookID, if provided. For a PUCCH transmission with SR, a UE determines the corresponding priority as described in clause 9.2.4. For a PUSCH transmission with semi-persistent CSI report, a UE determines a priority index from a priority indicator field, if provided, in a DCI format that activates the semi-persistent CSI report. If a priority index is not provided to a UE for a PUSCH or a PUCCH transmission other than PUCCH transmissions with SL HARQ-ACK reports, the priority index is 0. <Unchanged parts are omitted> |

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606809](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606809.zip) · `[126-R19-AI 8.1]`

**Conclusion** · `8.1` Maintenance on AI/ML for NR Air interface, NR MIMO Phase 5,  NES and NTN for NR and IoT · `RAN1#126:8.1:010` · 후보

> There is no consensus in RAN1 to support the TP from R1-2605669 of Clause 6.3.2.1.2 in TS 38.212 and Clause 5.2.1.5.4.1 in TS 38.214.
> NES

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606867](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606867.zip) · `[126-R19-AI 8.1]`

**Agreement** · `8.2` Maintenance on others · `RAN1#126:8.2:005` · 후보 · 관련 주제: CSI-RS

> Adopt the following TP to TS38.214 Section 5.2.1.4 in principle.
> | ---- Reason for change: The agreement achieved during RAN1#117 meeting for CSI reporting subband with SBFD operation is missing. It should be captured in TS 38.214 that if a configured CSI subband overlaps with at least one PRB outside DL usable PRBs, the CSI reporting subband includes PRB(s) within DL usable PRBs only, on top of the TP agreed in RAN1#122 meeting. ----------------------------------------------------------Start of TP#1-------------------------------------------------------------- 5.2.1.4 Reporting configurations … The reportFreqConfiguration contained in a CSI-ReportConfig indicates the frequency granularity of the CSI Report. A CSI Reporting Setting configuration defines a CSI reporting band as a subset of subbands of the bandwidth part, where the reportFreqConfiguration indicates: - the csi-ReportingBand as a contiguous or non-contiguous subset of subbands in the bandwidth part for which CSI shall be reported. - A UE is not expected to be configured with csi-ReportingBand which contains a subband where a CSI-RS resource linked to the CSI Report setting has the frequency density of each CSI-RS port per PRB in the subband less than the configured density of the CSI-RS resource. - If a CSI-IM resource is linked to the CSI Report Setting, a UE is not expected to be configured with csi-ReportingBand which contains a subband where not all PRBs in the subband have the CSI-IM REs present. - For a CSI-ReportConfig with the higher layer parameter symbolType set to ‘sbfd’, a UE can be configured with a CSI subband if at least one PRB in the CSI subband is within PRBs that are both in the active DL BWP and in the DL sub-band(s). The CSI subband for CSI derivation only includes PRB(s) that are both in the active DL BWP and in the DL sub-band(s). - wideband CQI or subband CQI reporting, as configured by the higher layer parameter cqi-FormatIndicator. When wideband CQI reporting is configured, a wideband CQI is reported for each codeword for the entire CSI reporting band. When subband CQI reporting is configured, one CQI for each codeword is reported for each subband in the CSI reporting band. … ----------------------------------------------------------End of TP#1--------------------------------------------------------------- |
> Final CR in R1-2605543 is endorsed.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2605539](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2605539.zip) · `[126-R19-AI 8.2]`

**Agreement** · `8.2` Maintenance on others · `RAN1#126:8.2:007` · 후보

> Adopt the following TP to section 8 and 11, TS 38.213 as alignment CR
> | 8 Random access procedure *** Unchanged parts are omitted *** For unpaired spectrum - if a UE is not provided tdd-UL-DL-ConfigurationCommon or sib1-tdd-UL-DL-ConfigurationCommon, all PRACH occasions are first PRACH occasions - otherwise, a PRACH occasion is - a first PRACH occasion, when it includes only symbols that are indicated as uplink or flexible by tdd-UL-DL-ConfigurationCommon or sib1-tdd-UL-DL-ConfigurationCommon and the UE is not provided by sbfd-RACH-DualConfig, and, or - a second PRACH occasion, when the UE is provided by sbfd-RACHDualConfigsbfd-RACH-DualConfig, or when it is only within SBFD symbols and includes at least one SBFD symbol indicated as downlink by tdd-UL-DL-ConfigurationCommon and the UE is provided sbfd-RACHSingleConfigsbfd-RACH-SingleConfig The procedures in clause 8.1 apply separately for the first PRACH occasions and the second PRACH occasions. Only a Type-1 random access procedure is applicable for the second PRACH occasions. *** Unchanged parts are omitted *** If a random access procedure is initiated by a PDCCH order and the UE is provided either sbfd-RACHSingleConfigsbfd-RACH-SingleConfig or sbfd-RACHDualConfigsbfd-RACH-DualConfig, the PDCCH order indicates [5, TS 38.212] whether the UE uses a PRACH occasion associated with either the first PRACH occasions or the second PRACH occasions, for the PRACH transmission that is initiated by the PDCCH order. 8.1 Random access preamble *** Unchanged parts are omitted *** - for a second PRACH occasion - it is in RBs that are both in the active UL BWP and in the UL sub-band, and - it starts at least symbols after a last non-SBFD downlink symbol and at least symbols after a last SS/PBCH block symbol, where is provided in Table 8.1-2, and does not overlap with a SS/PBCH block symbol, and - it is only within SBFD symbols, includes at least one SBFD symbol indicated as downlink by tdd-UL-DL-ConfigurationCommon, if the UE is provided sbfd-RACHSingleConfigsbfd-RACH-SingleConfig, or - it is only within SBFD symbols, if the UE is provided sbfd-RACHDualConfigsbfd-RACH-DualConfig, or - it starts from an SBFD symbol and ends in a non-SBFD symbols, if the UE is provided sbfd-RACHDualConfigsbfd-RACH-DualConfig and sbfd-RACHDualConfig-ValidROAcrossSymbolTypessbfd-RACH-DualConfig-ValidRO-AcrossSymbolTypes - for each of the candidate cells configured by LTM-config, if a UE is provided ltm-tdd-UL-DL-ConfigurationCommon, a PRACH occasion in a PRACH slot for a candidate cell is valid if *** Unchanged parts are omitted *** 11.1 Slot configuration *** Unchanged parts are omitted *** Except for a PRACH transmission in a PRACH occasion determined based on a second RACH configuration provided by sbfd-RACHDualConfigsbfd-RACH-DualConfig as described in clause 8, the UE transmits or receives a physical channel or signal either only in SBFD symbols or only in non-SBFD symbols. For a PUCCH transmission with SP-CSI reports, or for a PUCCH with SR, LRR, UEIRI, UE doesn’t transmit the PUCCH transmission occasion that is mapped to SBFD symbols and non-SBFD symbols. *** Unchanged parts are omitted *** |

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606864](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606864.zip) · `[126-R19-AI 8.2]`

**Agreement** · `8.2` Maintenance on others · `RAN1#126:8.2:014` · 후보 · 관련 주제: CSI-RS

> Adopt the following TP to TS38.214 Section 5.2.1.2 and 5.2.1.4.2 as alignment CR
> | Reason for change: | The higher layer parameter carrying the list of SS/PBCH block indices in an LTM CSI resource setting was renamed by RAN2 in Rel-19. In TS 38.331 Rel-19 the parameter is ltm-SSB-ResourceList-r18 within LTM-SSB-ResourceSet-r18, whereas TS 38.214 still refers to it as ltm-CSI-SSB-ResourceList. The corresponding resource set parameter was already aligned in TS 38.214 v19.4.0, but the resource list parameter was not, so a misalignment between the RAN1 and RAN2 specifications remains. The Rel-18 versions of TS 38.214 and TS 38.331 are mutually consistent and are not affected. | The higher layer parameter carrying the list of SS/PBCH block indices in an LTM CSI resource setting was renamed by RAN2 in Rel-19. In TS 38.331 Rel-19 the parameter is ltm-SSB-ResourceList-r18 within LTM-SSB-ResourceSet-r18, whereas TS 38.214 still refers to it as ltm-CSI-SSB-ResourceList. The corresponding resource set parameter was already aligned in TS 38.214 v19.4.0, but the resource list parameter was not, so a misalignment between the RAN1 and RAN2 specifications remains. The Rel-18 versions of TS 38.214 and TS 38.331 are mutually consistent and are not affected. | The higher layer parameter carrying the list of SS/PBCH block indices in an LTM CSI resource setting was renamed by RAN2 in Rel-19. In TS 38.331 Rel-19 the parameter is ltm-SSB-ResourceList-r18 within LTM-SSB-ResourceSet-r18, whereas TS 38.214 still refers to it as ltm-CSI-SSB-ResourceList. The corresponding resource set parameter was already aligned in TS 38.214 v19.4.0, but the resource list parameter was not, so a misalignment between the RAN1 and RAN2 specifications remains. The Rel-18 versions of TS 38.214 and TS 38.331 are mutually consistent and are not affected. | The higher layer parameter carrying the list of SS/PBCH block indices in an LTM CSI resource setting was renamed by RAN2 in Rel-19. In TS 38.331 Rel-19 the parameter is ltm-SSB-ResourceList-r18 within LTM-SSB-ResourceSet-r18, whereas TS 38.214 still refers to it as ltm-CSI-SSB-ResourceList. The corresponding resource set parameter was already aligned in TS 38.214 v19.4.0, but the resource list parameter was not, so a misalignment between the RAN1 and RAN2 specifications remains. The Rel-18 versions of TS 38.214 and TS 38.331 are mutually consistent and are not affected. |
> |  |  |  |  |  |
> | Summary of change: | In clauses 5.2.1.2 and 5.2.1.4.2, the higher layer parameter name ltm-CSI-SSB-ResourceList is changed to ltm-SSB-ResourceList, aligning TS 38.214 with the parameter name defined in TS 38.331. | In clauses 5.2.1.2 and 5.2.1.4.2, the higher layer parameter name ltm-CSI-SSB-ResourceList is changed to ltm-SSB-ResourceList, aligning TS 38.214 with the parameter name defined in TS 38.331. | In clauses 5.2.1.2 and 5.2.1.4.2, the higher layer parameter name ltm-CSI-SSB-ResourceList is changed to ltm-SSB-ResourceList, aligning TS 38.214 with the parameter name defined in TS 38.331. | In clauses 5.2.1.2 and 5.2.1.4.2, the higher layer parameter name ltm-CSI-SSB-ResourceList is changed to ltm-SSB-ResourceList, aligning TS 38.214 with the parameter name defined in TS 38.331. |
> |  |  |  |  |  |
> | Consequences if not approved: | A misalignment remains between TS 38.214 and TS 38.331, since TS 38.214 refers to a higher layer parameter name that does not exist in the Rel-19 version of TS 38.331. This may lead to ambiguous or incorrect implementation of LTM L1 measurement and reporting. | A misalignment remains between TS 38.214 and TS 38.331, since TS 38.214 refers to a higher layer parameter name that does not exist in the Rel-19 version of TS 38.331. This may lead to ambiguous or incorrect implementation of LTM L1 measurement and reporting. | A misalignment remains between TS 38.214 and TS 38.331, since TS 38.214 refers to a higher layer parameter name that does not exist in the Rel-19 version of TS 38.331. This may lead to ambiguous or incorrect implementation of LTM L1 measurement and reporting. | A misalignment remains between TS 38.214 and TS 38.331, since TS 38.214 refers to a higher layer parameter name that does not exist in the Rel-19 version of TS 38.331. This may lead to ambiguous or incorrect implementation of LTM L1 measurement and reporting. |
> |  |  |  |  |  |
> | Clauses affected: | 5.2.1.2, 5.2.1.4.2 | 5.2.1.2, 5.2.1.4.2 | 5.2.1.2, 5.2.1.4.2 | 5.2.1.2, 5.2.1.4.2 |
> |  |  |  |  |  |
> |  | Y | N |  |  |
> | Other specs |  | x | Other core specifications | TS/TR ... CR ... |
> | affected: |  | x | Test specifications | TS/TR ... CR ... |
> | (show related CRs) |  | x | O&M Specifications | TS/TR ... CR ... |
> |  |  |  |  |  |
> | Other comments: |  |  |  |  |
> |  |  |  |  |  |
> | Forge related attachments: |  |  |  |  |
> |  |  |  |  |  |
> | This CR's revision history: |  |  |  |  |
> | **unchanged omitted** 5.2.1.2 Resource settings **unchanged omitted** Each LTM CSI Resource Setting LTM-CSI-ResourceConfig contains either configuration of a ltm-SSB-ResourceSet or a LTM-NZP-CSI-RS-ResourceSet. - A ltm-SSB-ResourceSet comprises of a list of Z ≥ 1 SS/PBCH blocks indices (given by ltm-SSB-ResourceList) and a list of Z LTM-CandidateIds (given by ltm-CandidateIdList) referring to candidate cells associated with the SS/PBCH block indices. For each candidate cell, the UE determines the time domain behavior of a SS/PBCH block from ssb-Periodicity and ssb-PositionsInBurst and the frequency domain behavior of a SS/PBCH block is determined by the higher layer parameters subcarrierSpacing, ssb-Frequency. - A LTM-NZP-CSI-RS-ResourceSet comprises of a list of Z ≥ 1 NZP CSI-RS resource indices (given by ltm-CSI-RS-ResourceList) and a list of Z LTM-CandidateIds (given by ltm-CandidateIdList) referring to candidate cells associated with the NZP CSI-RS resource indices. The UE shall expect that LTM-NZP-CSI-RS-ResourceSet are configured with the higher layer parameter repetition set to ‘off’ when LTM-ReportContent configured within the LTM-CSI-ReportConfig associated with the LTM CSI Resource Setting is set to ‘cri-RSRP’. **unchanged omitted** 5.2.1.4.2 Report quantity configurations **unchanged omitted** If a UE is configured with a ltm-CSI-ReportConfig with ltm-ReportConfigType which is set to ‘periodic’ or ‘semiPersistentOnPUCCH’ or ‘semiPersistentOnPUSCH’ or ‘aperiodic’, - if the UE is configured with spCellInclusion with reportQuantity set to 'ssb-Index-RSRP', the UE shall report in a single reporting instance nrOfReportedRS-PerCell different SSBRI for the current SpCell and each of the nrOfReportedCells -1 candidate cells. Otherwise, the UE shall report in a single reporting instance nrOfReportedRS-PerCell different SSBRI for each of the nrOfReportedCells candidate cells, - where SSBRI k (k ≥ 0) corresponds to the configured (k+1)-th entry of the associated ltm-SSB-ResourceList in the corresponding ltm-SSB-ResourceSet, - if spCellInclusion is configured, SSB resources in ltm-SSB-ResourceList associated with the current SpCell are the entries where PCI (given by ltm-CandidatePCI) and frequency information (given by ssb-Frequency) of the candidate cell associated with the LTM-CandidateId (given by the corresponding entry in ltm-CandidateIdList) is equal to the PCI and center frequency of cell-defining SSB of the current SpCell. **unchanged omitted** |

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606748](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606748.zip) · `[126-R19-AI 8.2]`

**Agreement** · `10.5.2.1` Downlink transmission scheme(s) for downlink control channels · `RAN1#126:10.5.2.1:007` · 후보

> Study the need, feasibility including at least UE complexity and benefits of CSI acquisition for PDCCH.
> Note: Solutions, if found to be feasible and needed, shall be coordinated with the other AIs.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606614](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606614.zip) · `[126-R20-6GR-Transmission scheme for DL control channel]`

**Agreement** · `10.5.2.3` Uplink transmission scheme(s) for uplink channels · `RAN1#126:10.5.2.3:001` · 후보

> For codebook based PUSCH transmission for 6GR, study the following coherency types of UL precoder
> - Non-coherent type
> - Partial-coherent type
> - Full-coherent type
> - Full-power transmission precoder is separately discussed.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2605829](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2605829.zip) · `[126-R20-6GR-Transmission scheme for UL channels]`

**Agreement** · `10.5.2.3` Uplink transmission scheme(s) for uplink channels · `RAN1#126:10.5.2.3:002` · 후보

> For codebook based PUSCH transmission for 6GR, study fixed codebook for full-coherent precoder type considering the following options and aspects:
> - Option 1. Reuse NR UL codebook
> - Option 2. Grassmannian codebook
> - Option 3. Per-element phase/amplitude quantization targeting SVD precoder approximation
> - Option 4. DFT based precoder
> - Other option(s) are not precluded.
> - Consider different antenna architectures and different waveforms
> - Whether/how to separately or commonly design 2TX/3TX/4TX/8TX codebook
> - Whether to keep constant modulus property
> - Whether/how to consider UE PA (power amplifier) constraint
> - Whether/how to define single-layer precoder only, and indicating a combination of precoder(s)
> - Consider different codebook size and precoder indication overhead
> - Whether/how to separately or commonly design codebook for CP-OFDM and DFT-S-OFDM.
> - Note: Partial/non-coherent precoder type are separately discussed.
> - Note: Per-layer power control is separately discussed.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2605829](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2605829.zip) · `[126-R20-6GR-Transmission scheme for UL channels]`

**Agreement** · `10.5.2.3` Uplink transmission scheme(s) for uplink channels · `RAN1#126:10.5.2.3:012` · 후보

> The following is endorsed  as Draft an LS to RAN4 regarding the 6GR the RF coherence requirements.
> 1 Overall description:
> RAN1 are studying UL MIMO codebooks for 6G and have reached the following agreements:
> | Agreement: For codebook based PUSCH transmission for 6GR, study fixed codebook for full-coherent precoder type considering the following options and aspects: Option 1. Reuse NR UL codebook Option 2. Grassmannian codebook Option 3. Per-element phase/amplitude quantization targeting SVD precoder approximation Option 4. DFT based precoder Other option(s) are not precluded. Consider different antenna architectures and different waveforms Whether/how to separately or commonly design 2TX/3TX/4TX/8TX codebook Whether to keep constant modulus property Whether/how to consider UE PA (power amplifier) constraint Whether/how to define single-layer precoder only, and indicating a combination of precoder(s) Consider different codebook size and precoder indication overhead Whether/how to separately or commonly design codebook for CP-OFDM and DFT-S-OFDM. Note: Partial/non-coherent precoder type are separately discussed. Note: Per-layer power control is separately discussed. Agreement: For evaluation on coherent UL MIMO based PUSCH transmission for 6GR, at least the RF coherence requirements for coherent UL MIMO defined in TS38.101-1/2 are used as baseline Companies to report Other additional RF coherence requirements can be reported by companies (optional) TX coherency error model |
> RAN1 are currently using the coherent UL MIMO requirements in TS38.101-1/2 as baselines for evaluations including coherence imperfections. RAN1 would like to know if the /phase errors in these requirements  for 6G, especially for devices that support more than two port UL MIMO transmission.
> RAN1 have not so far agreed to models of coherence imperfections for codebook evaluations, and so such models are determined by each company. Therefore, while RAN1 can continue investigations, RAN1 would welcome suggestions on /phase error modeling for 6G UEs so that these may be used to refine RAN1’s evaluations.
> 2	Actions
> To RAN4
> ACTION: 	RAN1 respectfully asks RAN4 if the /phase errors in current coherent UL MIMO requirements in TS38.101-1/2  for 6G, especially for devices that support more than two port UL MIMO transmission. While RAN1 can continue investigations, RAN1 would also welcome suggestions on /phase error modeling for UL MIMO.
> The corresponding final LS in R1-2606899 is endorsed.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2605832](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2605832.zip) · `[126-R20-6GR-Transmission scheme for UL channels]`

**Agreement** · `10.5.2.3` Uplink transmission scheme(s) for uplink channels · `RAN1#126:10.5.2.3:013` · 후보

> For codebook based PUSCH transmission for 6GR, a fixed codebook is further clarified as follow:
> - For a given precoder indication size, a set of precoder(s) in fixed codebook is pre-defined/specified in the specification
> - Note: All 5G NR DL/UL codebooks are fixed codebook.
> - Note: Per agreement in RAN1#124bis, a fixed codebook is a codebook which is pre-defined in specification.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2605832](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2605832.zip) · `[126-R20-6GR-Transmission scheme for UL channels]`

**Agreement** · `10.5.2.3` Uplink transmission scheme(s) for uplink channels · `RAN1#126:10.5.2.3:014` · 후보

> For codebook based PUSCH transmission for 6GR, study configurable codebook considering the following options and aspects:
> - Option 1. Downloadable codebook
>   - NW determines a set of precoder(s)/matrices.
>   - From NW, UE is configured with a set of precoder(s)/matrices.
>   - After NW acquires UL CSI, an UL precoder within the set of precoder(s) is indicated by NW to UE.
> - Option 2. Uploadable codebook
>   - UE determines a set of precoder(s) and reports to NW.
>   - From NW, UE is configured with a set of precoder(s).
>   - After NW acquires UL CSI, an UL precoder within the set of precoder(s) is indicated by NW to UE.
> - Whether to consider constant modulus property
> - Whether/how to indicate/obtain UE’s relevant information
> - How to construct hybrid approach between fixed codebook and configurable codebook
> - Memory burden / implementation complexity for UE/NW side
> - Applicable scenario/use case (e.g., applicable number of antenna ports)
> - How to consider PAPR increase and UE power constraint

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2605832](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2605832.zip) · `[126-R20-6GR-Transmission scheme for UL channels]`

**Agreement** · `10.5.4.3` HARQ related Aspects · `RAN1#126:10.5.4.3:001` · 후보

> - For the study of downlink HARQ-ACK feedback granularity smaller than TB-level and the corresponding mechanism, candidate options in RAN1#125 are categorized as follow.
> - Category A (HARQ-ACK schemes):
>   - NR CBG HARQ-ACK feedback as comparison baseline
>   - XOR-based retransmission feedback
>   - CB/CBG-level HARQ-ACK feedback of high-probability error patterns / codebook-based compressed feedback
>   - 2D lattice-based CBs feedback
> - Category B (feedback mechanisms/procedures may be applicable on top of a Category A scheme):
>   - Non-uniform CB-to-CBG mapping feedback
>   - Two-stage feedback
>   - Mixture of TB-level and CBG-level feedback
>   - Per-PDSCH on-demand request of CBG-level feedback
>   - Enabling/disabling of CBG-level HARQ-ACK feedback
>   - HARQ-ACK feedback enabling/disabling for some of CBGs
> - At least a common set of evaluation assumptions are to be determined in this meeting for Category A.
> - FFS same/additional evaluation assumptions are to be applied for Category B.

남은 FFS 1건

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606797](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606797.zip) · `[126-R20-6GR-HARQ related]`

**Agreement** · `10.5.4.3` HARQ related Aspects · `RAN1#126:10.5.4.3:003` · 후보

> - For study of 6G HARQ-ACK codebook based on NR Type-1 codebook as starting point, consider at least the following
>   - Whether / how to reduce the codebook payload size
>   - Whether / how to reduce codebook construction complexity
> - For study of 6G HARQ-ACK codebook based on NR Type-2 codebook as starting point, consider at least the following
>   - Whether/how to achieve additional robustness against the DCI(s) missing including last DCI(s) missing
>   - Whether the counting / accumulating indication is confined within a cell or a set of cells
> - For study of 6G HARQ-ACK codebook based on NR (e)Type 3 codebook as starting point, consider at least the following
>   - Whether/how to achieve additional robustness against missing the DCI triggering the feedback
>   - Whether / how to reduce codebook payload size
> - FFS for each codebook type:
>   - HARQ-ACK bit ordering
>   - Determination of HARQ-ACK codebook payload size
>   - For relaxing the need for tight coordination between schedulers, determine which codebook type(s) should be considered
>   - Scheduling complexity
>   - How to carry HARQ-ACK bits for a DCI that does not schedule a PDSCH, for at least (e)type 3 codebook
>   - Whether/how to support standalone operation
> - FFS: other approaches

남은 FFS 2건

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606799](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606799.zip) · `[126-R20-6GR-HARQ related]`

### RAN1#125 — 7건

**Agreement** · `8.1` Maintenance on AI/ML for NR Air interface, NR MIMO Phase 5,  NES and NTN for NR and IoT · `RAN1#125:8.1:001` · 후보

> The following TP is endorsed as Alignment CR for TS.38.212 and Clause 6.3.2.1.2.
> Reason for change: The current specification incorrectly states the SGCS fields of the CSI report for CSI-PAI are included in CSI part 1.
> Summary of change: Remove “CSI part 1” to clarify that the SGCS fields of the CSI report for CSI-PAI are in a single CSI report.
> Consequences if not approved: The specification would contain an inaccurate description of the CSI fields for CSI-PAI reporting.
> | 6.3.2.1.2 CSI <unchanged parts are omitted> Table 6.3.2.1.2-3K: Mapping order of CSI fields of one CSI report for CSI-PAI <unchanged parts are omitted> |

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2605022](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2605022.zip)

**Agreement** · `8.1` Maintenance on AI/ML for NR Air interface, NR MIMO Phase 5,  NES and NTN for NR and IoT · `RAN1#125:8.1:002` · 후보

> The following TP is endorsed as Alignment CR for TS.38.214 for Clause 5.2.1.4.6.
> Reason for change: Incorrect capture of previous agreement.
> Summary of change: Change the brackets to align with the agreement made in RAN1#122.
> Consequence if not approved: UE does not know which code point to report when a calculated SGCS falls at the endpoint of intervals.
> | TS38.214 5.2.1.4.6 CSI-PAI reporting << Unchanged parts are omitted >> Table 5.2.1.4.6-1: SGCS Quantization Mapping << Unchanged parts are omitted >> |

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2605022](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2605022.zip)

**Agreement** · `8.1` Maintenance on AI/ML for NR Air interface, NR MIMO Phase 5,  NES and NTN for NR and IoT · `RAN1#125:8.1:008` · 후보

> The following TP for Clause 9 of TS 38.213 is endorsed.
> The corresponding final CR for TS38.213 in R1-2605107 is endorsed.
> |  |
> | Reason for change: For a UE enabled with inter-slot OCC operation, UE behaviour is not clear in case where a UE may determine to do multiplexing UCI in the PUSCH in a first slot and determine to drop the PUSCH in the second slot of a same OCC group. Summary of change: UE drops all the PUSCH repetitions in an OCC group before multiplexing UCI in the PUSCH when enabled with inter-slot OCC. Consequences if not approved: Unclear UE behaviour |
> | 9 UE procedure for reporting control information *** Unchanged parts are omitted *** For the remaining of this clause, for a UE operating on an NTN serving cell, the timeline conditions for resolving time overlapping between a PUSCH transmission with repetitions in an OCC group [6, TS 38.214] and PUCCH transmissions are applicable with respect to the first repetition of the PUSCH transmission in the OCC group - if the UE would multiplex UCI from the PUCCH transmissions in the PUSCH, and for the case where the PUSCH would not be dropped as described in the remaining of this clause or in clause 6.1.2.1 [6, TS 38.214], the UE multiplexes the UCI in all repetitions of the PUSCH transmission in the OCC group - if the UE would not transmit a repetition of the PUSCH transmission, the UE does not transmit all repetitions of the PUSCH transmission in the OCC group - the UE does not expect to transmit in different slots more than one PUCCHs that provide HARQ-ACK information or CSI reports and would overlap with the PUSCH transmission in the OCC group *** Unchanged parts are omitted *** |

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2604991](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2604991.zip)

**Agreement** · `8.2` Maintenance on others · `RAN1#125:8.2:006` · 후보

> Adopt the following TP to TS38.214 Section 5.2.4a
> | Reason for change | For LTM, ‘ltm-CandidateConfig’ includes an RRCReconfiguration message that is used to provide an LTM candidate configuration, where the RRCReconfiguration message includes a ‘CellGroupConfig’ containing a ‘ReconfigurationWithSync’ that carries a ‘newUE-Identity’ to indicate a RNTI value for UE applied in target cell. For L3 handover, such ‘newUE-Identity’ is also provided for UE through handover command ‘ReconfigurationWithSync’. Thus, for 2-step CBRA based LTM or handover, UE always carries the C-RNTI in MSG A. Based on the above considerations and the CR (R1-2603427) already agreed in RAN1#124bis meeting, the wording “MSG B or” in clause 5.2.4a of TS 38.214-j30 should be removed. The reason is that for the determination of first PUSCH for early CSI report in 2-step CBRA based LTM or handover, the UE shall transmit the CSI report to the candidate cell using the first PUSCH corresponding to a dynamic grant or a configured grant after the HARQ-ACK transmission corresponding to “PDSCH scheduled by a PDCCH transmission addressed to the C-RNTI that is received in response to MSG A”, rather than referencing “MSG B”. |
> | Summary of change | Remove “MSG B or” from the following paragraph in clause 5.2.4a of TS 38.214-j30 with updates based on the endorsed CR (R1-2603427). |
> | Consequences if not approved | The UE behavior on determining UL resource of early CSI report when C-RNTI has been included in MSG A for CBRA based LTM or handover scenario is incorrect. |
> | Clauses affected | 5.2.4a |
> | 5.2.4a CSI Reporting for LTM and handover *** Unchanged parts are omitted *** For RACH-less LTM cell switch or RACH-less handover [23, TS 38.300], the UE shall transmit the CSI report to the candidate cell using the first PUSCH corresponding to a dynamic grant or a configured grant [6, TS 38.213]. For RACH-based LTM cell switch or RACH-based handover using a contention-free random access procedure [23, TS 38.300], the UE shall transmit the CSI report to the candidate cell using the PUSCH scheduled by the RAR UL grant or MsgA PUSCH. For RACH-based LTM cell switch or RACH-based handover using a contention-based random access procedure [23, TS 38.300], the UE shall transmit the CSI report to the candidate cell using the first PUSCH corresponding to a dynamic grant or a configured grant after the HARQ-ACK transmission corresponding to , or the first PUSCH scheduled by a PDCCH transmission addressed to the C-RNTI, received in response to Msg3. *** Unchanged parts are omitted *** | 5.2.4a CSI Reporting for LTM and handover *** Unchanged parts are omitted *** For RACH-less LTM cell switch or RACH-less handover [23, TS 38.300], the UE shall transmit the CSI report to the candidate cell using the first PUSCH corresponding to a dynamic grant or a configured grant [6, TS 38.213]. For RACH-based LTM cell switch or RACH-based handover using a contention-free random access procedure [23, TS 38.300], the UE shall transmit the CSI report to the candidate cell using the PUSCH scheduled by the RAR UL grant or MsgA PUSCH. For RACH-based LTM cell switch or RACH-based handover using a contention-based random access procedure [23, TS 38.300], the UE shall transmit the CSI report to the candidate cell using the first PUSCH corresponding to a dynamic grant or a configured grant after the HARQ-ACK transmission corresponding to , or the first PUSCH scheduled by a PDCCH transmission addressed to the C-RNTI, received in response to Msg3. *** Unchanged parts are omitted *** |
> Final CR in R1-2605090 is endorsed.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2605008](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2605008.zip)

**Agreement** · `10.2.1` Waveform · `RAN1#125:10.2.1:003` · 후보

> - Max rank for multi-layer UL DFT-s-OFDM:
>   - Max rank = 2
> - Codebook for two-layer UL DFT-s-OFDM:
>   - For each precoder, each Tx port transmits at most one layer
>   - Final decision is to be done in UL transmission agenda
> - Relation of UE’s support of MaxRank for DFT-s-OFDM and CP-OFDM in the uplink:
>   - An UE supporting MaxRank = X (X=1 or 2) with DFT-s-OFDM supports at least the same MaxRank with CP-OFDM
> - Waveform Switching
>   - Support semi-static (RRC configured) PUSCH waveform determination for all RRC states operation
>     - FFS: details
>   - Support Dynamic PUSCH waveform determination for RRC connected mode operation
>     - FFS: details
> - Note: UE capability for above features can be discussed later once 6G UE capability framework is decided

남은 FFS 2건

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2603725](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2603725.zip)

**Agreement** · `10.5.2.3` Uplink transmission scheme(s) for uplink channels · `RAN1#125:10.5.2.3:008` · 후보

> For 6GR PUSCH transmission
> - Study codeword-to-layer mapping scheme at least considering the followings:
>   - The number of codewords for each rank
>   - The number of layer(s) per codeword for each rank
>   - The maximum number of codewords
>   - Mapping of same or different modulation order for a number of layer(s) of a codeword
>   - Performance comparison with system aspects (e.g., DL control signaling overhead, HARQ complexity, different precoding schemes, impact on BS receiver implementation, performance with link adaptation and scheduling, small packet transmission with higher ranks, performance with directional antennas and/or impairments, MPR, antenna imbalance, UE complexity, processing delay, UL CSI acquisition, etc. Other aspects are not precluded)
> - Study whether/how to map one or more transport block(s) to time/frequency resources and its impact on codeword-to-layer mapping
> - Study same or different power allocation across-layers and its impact on codeword-to-layer mapping
> - Study aspects related to modulation order and code rate and its impact on codeword-to-layer mapping

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Transmission scheme for UL channels]`

**Agreement** · `10.5.4.3` HARQ related Aspects · `RAN1#125:10.5.4.3:004` · 후보

> In 6GR, for the study of downlink HARQ-ACK feedback granularity smaller than TB-level and corresponding mechanism, consider at least the following:
> - XOR-based retransmission feedback
> - CB/CBG-level HARQ-ACK feedback of high-probability error patterns
> - NR CBG HARQ-ACK feedback
> - Codebook-based feedback
> - Two-stage feedback
> - 2D lattice-based CBs feedback
> - Per-PDSCH on demand request of CBG-level feedback
> - Mixture of TB-level and CBG-level feedback
> - Non-uniform CB-to-CBG mapping feedback
> - HARQ-ACK feedback enabling/disabling for some of CBGs
> - enabling/disabling of CBG-level HARQ-ACK feedback
> - Separate HARQ-ACK for CBs that carry MAC CEs or similar important data
> Note: in the above applicable options, CB-level and CBG-level can be both considered.
> Note: For the evaluation of above options, consider at least (average) feedback overhead per TB, ratio between size of retransmitted CB(s)/CBG(s) and size of original TB, and impact on DL control overhead, considering practical setup (e.g., fading channel, correlation across CBs, link adaptation, etc.)
> Note: Companies are encouraged to check FL summary and contributions

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2604827](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2604827.zip) · `[125-R20-6GR-HARQ related]`

### RAN1#124bis — 6건

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#124bis:8.1:001` · 후보

> The following TP for TS 38.212 Clause 6.3.1.1.2 is endorsed.
> The corresponding final CR for Rel-19 TS 38.212 in R1-2603378 is endorsed
> Reason for change: For P/SP CSI reporting on PUCCH for performance monitoring, it is possible that the number of information bits of RS-PAI becomes less than 3 bits. However, NR specifications do not support PUCCH carrying 1 or 2 information bits other than HARQ-ACK/SR.
> Summary of change: For P/SP CSI reporting on PUCCH for performance monitoring, the number of information bits of related CSI is zero padded to 3 bits.
> Consequences if not approved: For P/SP CSI reporting on PUCCH for performance monitoring, 1-bit or 2-bit payload size of RS-PAI is not supported.
> | 6.3.1.1.2 CSI only <omitted texts> If none of the CSI reports for transmission on a PUCCH is of two parts, the CSI fields of all CSI reports, in the order from upper part to lower part in Table 6.3.1.1.2-12, are mapped to the UCI bit sequence starting with . The most significant bit of each field is mapped to the lowest order information bit for that field, e.g. the most significant bit of the first field is mapped to. If the length of UCI bit sequence is less than 3 bits, zeros shall be appended to the UCI bit sequence until its length equals 3. Table 6.3.1.1.2-12: Mapping order of CSI reports to UCI bit sequence , without two-part CSI report(s) <omitted texts> |

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2603260](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603260.zip) · `[124b-R19-AI/ML]`

**Conclusion** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#124bis:8.1:003` · 후보 · 관련 주제: CSI-RS

> There is no RAN1 consensus on the following:
> - For virtual resource blocks mapping of PDSCH in TS38.211, rate matching of the resource elements in the corresponding physical resource blocks are not performed around the NZP CSI-RS only configured in Set A for CSI report for inference.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2603260](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603260.zip) · `[124b-R19-AI/ML]`

**Agreement** · `8.3` Maintenance on Evolution of NR duplex operation: Sub-band full duplex (SBFD) · `RAN1#124bis:8.3:005` · 후보

> Adopt the following TPs for TS38.214.
> | 5.2.2.5 CSI reference resource definition *** Unchanged parts are omitted *** If configured to report CQI index, in the CSI reference resource, the UE shall assume the following for the purpose of deriving the CQI index, and if also configured, for deriving PMI and RI: The first 2 OFDM symbols are occupied by control signaling. The number of PDSCH and DM-RS symbols is equal to 12. The same bandwidth part subcarrier spacing configured as for the PDSCH reception The bandwidth as configured for the corresponding CQI report If a UE is configured with SBFD symbols and a CSI-ReportConfig with the higher layer parameter symbolType indicating SBFD symbols, CQI is generated based on the PRBs in the configured CSI report bandwidth that are both in the active DL BWP and in the DL sub-band(s). The IAB-MT shall only assume the frequency resources as indicated by the DL TX power adjustment MAC CE, if indicated for the slot of the CSI reference resource by DL Tx Power Adjustment MAC CE as described in [10, TS 38.321]. *** Unchanged parts are omitted *** |
> | Reason for change In the definition of the hypothetical PDSCH used in calculating the CQI report, the frequency resources are determined by the configured bandwidth for CQI reporting. In SBFD slots, the definition of the frequency resources needs to be clarified to correspond to only usable DL PRBs within the configured reporting bandwidth. Summary of change When UE is configured with CSI report indicating symbolType as SBFD, the CQI is calculated based on the valid DL PRBs in the reporting bandwidth. |
> Final CR in R1-2603434 is endorsed.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2603361](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603361.zip) · `[124b-R19-SBFD]`

**Agreement** · `8.7` Maintenance on others · `RAN1#124bis:8.7:001` · 후보 · 관련 주제: CSI-RS

> - Adopt the following TP to TS38.214 Section 5.2.4a
> | Reason for change: periodic CSI-RS/CSI-IM configuration for early CSI acquisition for a candidate cell is captured in the TS 38.214, while the semi-persistent CSI-RS/CSI-IM support is missing. Summary of change: Clarify that the CSI-RS/CSI-IM for CSI acquisition on a candidate cell can be semi-persistently activated. Consequences if not approved: UE’s behaviors of CSI acquisition for a candidate cell become incomplete. |
> | 5.2.4a CSI Reporting for LTM and handover <Unchanged parts are omitted> After a UE receives an LTM Cell Switch Command MAC CE [10, TS 38.321] providing a candidate cell (given by Target Configuration ID field), and a ltm-CSI-ReportConfig is configured for the candidate cell, the UE can measure corresponding NZP CSI-RS resources and CSI-IM resources if configured, and shall transmit a CSI report to the candidate cell. After a UE receives a ReconfigurationWithSync configured with earlyCSI-Acquisition, the UE can measure corresponding NZP CSI-RS resources and CSI-IM resources if configured, and shall transmit a CSI report to the target cell. <Unchanged parts are omitted> If a valid CSI is not available, the UE shall transmit a CSI report which contains a CQI corresponding to the lowest CQI index. Depending on the UE capability, the UE may measure NZP CSI-RS resources and CSI-IM resources if configured corresponding to a ltm-CSI-ReportConfig before receiving the LTM Cell Switch Command MAC CE [10, TS 38.321]. |
> The final CR in R1-2603406 is endorsed.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2603335](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603335.zip) · `[124b-R19-others]`

**Agreement** · `8.7` Maintenance on others · `RAN1#124bis:8.7:006` · 후보

> - Adopt the following TP to TS38.214 Section 5.2.4a
> | Reason for change: In existing specification, for early CSI acquisition during RACH-based HO with CBRA, the current 2-step RA relies on “after MsgB HARQ-ACK”, which does not cover the MsgA success path via C-RNTI addressed PDCCH UL grant, and it also does not exclude the NACK case. Summary of change: Update TS 38.214 to clarify that ACK value is required for the MsgB HARQ-ACK and allow the first PUSCH to be the one scheduled by a C-RNTI addressed PDCCH received in response to MsgA. Consequences if not approved: Early CSI acquisition for 2-step RA HO may be missing in the MsgA UL-grant success path and may be triggered after a NACK, leading to inconsistent UE behavior and potential performance/interoperability issues. |
> | 5.2.4a CSI Reporting for LTM and handover ==================================unchanged omitted======================= For RACH-less LTM cell switch or RACH-less handover [23, TS 38.300], the UE shall transmit the CSI report to the candidate cell using the first PUSCH corresponding to a dynamic grant or a configured grant [6, TS 38.213]. For RACH-based LTM cell switch or RACH-based handover using a contention-free random access procedure [23, TS 38.300], the UE shall transmit the CSI report to the candidate cell using the PUSCH scheduled by the RAR UL grant or MsgA PUSCH. For RACH-based LTM cell switch or RACH-based handover using a contention-based random access procedure [23, TS 38.300], the UE shall transmit the CSI report to the candidate cell using the first PUSCH corresponding to a dynamic grant or a configured grant after the HARQ-ACK transmission corresponding to MsgB, or the first PUSCH scheduled by a PDCCH transmission addressed to the C-RNTI, received in response to Msg3. ==================================unchanged omitted==================== |
> The final CR in R1-2603426 is endorsed.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2603381](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603381.zip) · `[124b-R19-others]`

**Agreement** · `8.7` Maintenance on others · `RAN1#124bis:8.7:007` · 후보

> - Adopt the following TP to TS38.214 Section 5.2.4a
> | Reason for change: | For CBRA based LTM or handover scenario, UE shall transmit CSI report to the candidate cell using the first PUSCH corresponding to a dynamic grant or a configured grant after the HARQ-ACK transmission corresponding to PDSCH scheduled by a PDCCH transmission addressed to the C-RNTI that is received in response to MSG A. However, the above method for determining UL resource of early CSI report is missing in the RAN1 spec, i.e., TS 38.214 clause 5.2.4a. |
> |  |  |
> | Summary of change: | For CBRA based LTM or handover case, add a rule to determine UL resource of early CSI report if C-RNTI MAC CE is included in MSG A, i.e., For RACH-based LTM cell switch or RACH handover using a contention-based random access procedure [23, TS 38.300], the UE shall transmit the CSI report to the candidate cell using the first PUSCH corresponding to a dynamic grant or a configured grant after the HARQ-ACK transmission corresponding to PDSCH scheduled by a PDCCH transmission addressed to the C-RNTI that is received in response to MSG A. |
> |  |  |
> | Consequences if not approved: | The UE behavior on determining UL resource of early CSI report when C-RNTI has been included in MSG A for CBRA based LTM or handover scenario is unclear. |
> | 5.2.4a CSI Reporting for LTM and handover *** Unchanged parts are omitted *** For RACH-less LTM cell switch or RACH-less handover [23, TS 38.300], the UE shall transmit the CSI report to the candidate cell using the first PUSCH corresponding to a dynamic grant or a configured grant [6, TS 38.213]. For RACH-based LTM cell switch or RACH-based handover using a contention-free random access procedure [23, TS 38.300], the UE shall transmit the CSI report to the candidate cell using the PUSCH scheduled by the RAR UL grant or MsgA PUSCH. For RACH-based LTM cell switch or RACH-based handover using a contention-based random access procedure [23, TS 38.300], the UE shall transmit the CSI report to the candidate cell using the first PUSCH corresponding to a dynamic grant or a configured grant after the HARQ-ACK transmission corresponding to MsgB, or the first PUSCH scheduled by a PDCCH transmission addressed to the C-RNTI, received in response to Msg3. *** Unchanged parts are omitted *** |
> The final CR in R1-2603427 is endorsed.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2603381](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603381.zip) · `[124b-R19-others]`

### RAN1#124 — 4건

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#124:8.1:002` · 후보 · 관련 주제: CSI-RS

> Adopt the following TP for TS 38.214 Clause 5.2.1.6.
> The corresponding final CR for Rel-19, TS 38.214 in R1-2601645 is endorsed.
> Reason for change: The notation of “and/or ” is mistakenly used to describe occupied CPU for CPU occupation time for CSI report for monitoring.
> Summary of change: Adding correct notation of occupied CPU for CPU occupation time for CSI report for monitoring.
> Consequences if not approved: The notation of occupied CPU for CPU occupation time for CSI report for monitoring is incorrect.
> | 5.2.1.6 CSI processing criteria <omitted texts> For a CSI report with CSI-ReportConfig with higher layer parameter reportQuantity not set to 'none', or a CSI report with LTM-CSI-ReportConfig, or reportQuantity not set to 'none-bm-r19' or 'none-csi-r19', the CPU(s) (including and/or , for CSI reports with reportQuantity set to 'p-cri-r19', 'p-cri-RSRP-r19', 'p-ssb-index-r19', or 'p-ssb-index-RSRP-r19', or ‘csi-pai-r19’, or ‘rs-pai-r19’, and CSI reports configured with the higher layer parameter csi-InferencePrediction-r19, and for CSI report with reportQuantity set to ‘rs-pai-r19’ or ‘csi-pai-r19’) are occupied for a number of OFDM symbols as follows: - A periodic or semi-persistent CSI report (excluding an initial semi-persistent CSI report on PUSCH after the PDCCH triggering the report, a semi-persistent CSI report on PUSCH configured with reportQuantity set to 'csi-pai-r19', and a semi-persistent CSI report on PUSCH configured with the higher layer parameter codebookType set to 'typeII-Doppler-r18' or 'typeII-Doppler-PortSelection-r18') occupies CPU(s) from the first symbol of the earliest one of each CSI-RS/CSI-IM/SSB resource, or each CSI-RS/CSI-IM resource associated with all configured sub-configurations for periodic CSI report corresponding to a CSI-ReportConfig that contains a list of sub-configurations provided by csi-ReportSubConfigToAddModList, or each CSI-RS/CSI-IM resource associated with all activated/triggered sub-configurations for semi-persistent CSI report corresponding to a CSI-ReportConfig that contains a list of sub-configurations provided by csi-ReportSubConfigToAddModList, for channel or interference measurement, respective latest CSI-RS/CSI-IM/SSB occasion no later than the corresponding CSI reference resource, until the last symbol of the configured PUSCH/PUCCH carrying the report. <omitted texts> |

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2600736](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2600736.zip) · `[124-R19-AI/ML]`

**Agreement** · `8.7.2` Maintenance for Rel-19 IoT NTN · `RAN1#124:8.7.2:004` · 후보

> The draft LS in R1-2601608 is endorsed with applying the following change.
> - The CQI should can be measured on the narrowband on which MPDCCH of CB-Msg4 is monitored.
> The final LS in R1-2601612 is endorsed.

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx)

**Agreement** · `8.8` Maintenance on others · `RAN1#124:8.8:007` · 후보 · 관련 주제: CSI-RS

> Adopt the following TP to TS38.214 Section 5.2.4a
> ---
> Reason for change
> For CSI acquisition for LTM candidate cells, the association between NZP-CSI-RSs for channel measurements and CSI-IM resources for interference measurement is missing.
> Summary of change
> This is clarified that, each NZP-CSI-RS resource the UE is expected to measure for channel measurement for a candidate cell is resource-wise associated with a CSI-IM resource based on the ordering of the NZP-CSI-RS resources and CSI-IM resources in the corresponding resource sets, and the number of NZP-CSI-RS resources the UE is expected to measure for channel measurement for a candidate cell equals the number of CSI-IM resources for interference measurement.
> Consequences if not approved
> The procedure to acquire CSI for a candidate cell, including the association between channel and interference measurements based on NZP-CSI-RS and CSI-IM resources, respectively, is not fully specified.
> 5.2.4a	CSI Reporting for LTM
> <omitted Text>
> A UE configured with LTM-Config can be provided configurations for CSI acquisition, by up to one Reporting Setting, ltm-CSI-ReportConfig, for a candidate cell. A UE can be provided configuration for CSI acquisition, by one Reporting Setting, earlyCSI-Acquisition in ReconfigurationWithSync, for a target cell. Each Reporting Setting ltm-CSI-ReportConfig or earlyCSI-Acquisition is associated with either one or two Resource Settings
> - When one Resource Setting (given by higher layer parameter ltm-ResourcesForChannelMeasurement or early-NZP-CSI-RS-ResourceSet) is configured, it provides a list of NZP CSI-RS resources for both channel and interference measurements. The UE is not expected to be configured with more than 128 NZP CSI-RS ports in the CSI-RS resource set contained within the Resource Setting.
> - When two Resource Settings are configured, the first Resource Setting (given by higher layer parameter ltm-ResourcesForChannelMeasurement or early-NZP-CSI-RS-ResourceSet) provides a list of NZP CSI-RS resources for channel measurement, and the second Resource Setting (given by higher layer parameter ltm-ResourceForInterferenceMeasurements or early-CSI-IM-ResourceSet), provides a list of CSI-IM resources for interference measurement. The UE is not expected to be configured with more than 128 NZP CSI-RS ports in the CSI-RS resource set contained within the Resource Setting.
> The Resource Setting given by higher layer parameter ltm-ResourcesForChannelMeasurement, LTM-CSI-ResourceConfig, contains configuration of a ltm-NZP-CSI-RS-ResourceSet which comprises of a list of Z ≥ 1 NZP CSI-RS resource indices (given by ltm-CSI-RS-ResourceList) and a list of Z LTM-CandidateIds (given by ltm-CandidateIdList) referring to candidate cells associated with the NZP CSI-RS resource indices. For CSI acquisition associated with a Reporting Setting, ltm-CSI-ReportConfig, the UE is expected to measure the NZP-CSI-RS resources in ltm-CSI-RS-ResourceList associated with the LTM-CandidateId that is equal to the LTM-CandidateId of the LTM-Candidate under which the Reporting Setting is configured. If interference measurement is performed on CSI-IM, each NZP-CSI-RS resource the UE is expected to measure for channel measurement for a candidate cell is resource-wise associated with a CSI-IM resource for the same candidate cell by the ordering of the NZP-CSI-RS resources and CSI-IM resources in the corresponding resource sets. The number of NZP-CSI-RS resources the UE is expected to measure for channel measurement for a candidate cell equals to the number of CSI-IM resources for interference measurement.
> <omitted Text>
> ---
> Final CR is endorsed in R1-2601698.

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601559](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601559.zip) · `[124-R19-others]`

**Agreement** · `8.9` Maintenance on UE features · `RAN1#124:8.9:005` · 후보 · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-5l | Processing timeline for CSI reference slot for extended Rel-18 Type-II Doppler codebook for up to 128 ports | 1. Aperiodic CSI report timing relaxation, w, extended Rel-18 Type-II Doppler codebook for up to 128 ports 2. Aperiodic CSI report timing relaxation, type, for extended Rel-18 Type-II Doppler codebook for up to 128 ports | 59-2-1-5 | Yes | n/a |  | Per band and Per BC | n/a | n/a | n/a | Component 1 candidate values: UE reports candidate value, w, independently for each SCS in unit of symbols: {14*(KP–1)*d, 14*KP*d} Note: Kp is according to Component 12 of FG59-2-1-5 Note: d=4 (minimum periodicity of periodic CSI-RS) Component 2 candidate values: {CAP1, CAP2} Note: For Component 2 ‘CAP2’ is the lower capability For N4 = 1 1) For AP CSI-RS: (Z,Z’) = (Z2 + 14*( KDOPP –1)*m, Z'2) 2) For P/SP CSI-RS: (Z,Z’) = (Z2 + w, Z'2) For N4 > 1 and CAP1 in component 2 1) For AP CSI-RS: (Z,Z’) = (Z2 + 14*( KDOPP –1)*m, Z'2) 2) For P/SP CSI-RS: (Z,Z’) = (Z2 + w, Z'2) For N4 > 1 and CAP2 in component 2 1) For AP CSI-RS: (Z,Z’) = (Z2 + 14*( KDOPP –1)*m + Z'2, 2Z'2) 2) For P/SP CSI-RS: (Z,Z’) = (Z2 + w + Z'2, 2Z'2) Z2/Z'2 are defined in Table 5.4-2 in TS38.214 KDOPP is the number of CSI-RS resource groups configured for channel measurement, and each CSI-RS resource groups contain K CSI-RS resources for aggregating up to 128 ports M = {1,2}, is the offset between two adjacent AP CSI-RS resource groups for the CMR in slots This FG is not applicable to FR 2-2 | Optional with capability signalling |

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601216](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601216.zip) · `[124-R19-UE features]`

### RAN1#123 — 15건

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#123:8.1:001` · 후보

> Adopt the following TPs for TS 38.214 Clause 5.2.1.6.
> Reason for change: The release of CPU1 and CPUx for a CSI report not considered within any of  and  is unclear.
> Summary of change: Clarify that the CPU1 and CPUx for a CSI report not considered within any of  and  are not occupied.
> Consequences if not approved: gNB and UE may have different understanding on the release of CPU1 and CPUx for a CSI report not considered within any of  and .
> | TP for TS 38.214 Clause 5.2.1.6 CSI processing criteria <omitted texts> For CSI reports with reportQuantity set to 'p-cri-r19', 'p-cri-RSRP-r19', 'p-ssb-index-r19', or 'p-ssb-index-RSRP-r19', and CSI reports configured with the higher layer parameter csi-InferencePrediction-r19, the UE may indicate a second value for the number of supported simultaneous CSI calculations with parameter SecondValuesSimultaneousCSI-ReportsPerCC in a component carrier, and SecondValuesSimultaneousCSI-ReportsAllCC across all component carriers, and if applicable, a third value for the number of supported simultaneous CSI calculations with parameter ThirdValuesSimultaneousCSI-ReportsPerCC in a component carrier, and ThirdValuesSimultaneousCSI-ReportsAllCC across all component carriers, in addition to . If a UE supports simultaneous CSI calculations it is said to have CSI processing units for processing CSI reports. If CPUs are occupied for calculation of CSI reports in a given OFDM symbol, the UE has unoccupied CPUs. If CSI reports start occupying their respective CPUs on the same OFDM symbol on which CPUs are unoccupied, where each CSI report corresponds to , the UE is not required to update the requested CSI reports with lowest priority (according to Clause 5.2.5), where is the largest value such that holds. If only the second value is indicated, x = 2. If both of the second value and the third value are indicated, x = 2, 3 where the CSI reports with reportQuantity set to 'p-cri-r19', 'p-cri-RSRP-r19', 'p-ssb-index-r19', or 'p-ssb-index-RSRP-r19' corresponds to either x = 2 or x = 3 subject to UE capability and the CSI reports configured with the higher layer parameter the higher layer parameter csi-InferencePrediction-r19 corresponds to either x = 2 or x = 3 subject to UE capability. For CSI reports with reportQuantity set to 'p-cri-r19', 'p-cri-RSRP-r19', 'p-ssb-index-r19', or 'p-ssb-index-RSRP-r19', and CSI reports configured with the higher layer parameter csi-InferencePrediction-r19, and are considered for determining and , and if a CSI report is not considered within any of and , the values for the CPUs corresponding to and of the CSI report are not occupied considered to be 0, for the procedure previously described in this clause, and the UE is not required to update the CSI report. <omitted texts> |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2508772](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2508772.zip) · `[123-R19-AI/ML]`

**Agreement** · `8.3` Maintenance on Evolution of NR duplex operation: Sub-band full duplex (SBFD) · `RAN1#123:8.3:004` · 후보

> Adopt the following TP in principle to Clause 9.2.6, TS 38.213.
> | 9.2.6 PUCCH repetition procedure For unpaired spectrum, the UE determines the slots for a PUCCH transmission starting from a slot indicated to the UE as described in clause 9.2.3 for HARQ-ACK reporting, or a slot determined as described in clause 9.2.4 for SR reporting or in clause 5.2.1.4 of [6, TS 38.214] for CSI reporting and having - an UL symbol, as described in clause 11.1, or flexible symbol, or an SBFD symbol as described in clause 11.1, that is not SS/PBCH block symbol provided by startingSymbolIndex as a first symbol, and - consecutive UL symbols, as described in clause 11.1, or flexible symbols, or consecutive SBFD symbols as described in clause 11.1, respectively, that are not SS/PBCH block symbols, starting from the first symbol, equal to or larger than a number of symbols provided by nrofsymbols, and - if the UE is not provided sbfd-Config2-Transmission, and if the valid symbol type for the PUCCH transmission is determined as SBFD symbol, the UE shall only consider slots containing consecutive SBFD symbols, that are not SS/PBCH block symbols, starting from the first symbol provided by startingSymbolIndex, with a length equal to or larger than the number of symbols provided by nrofsymbols. if the valid symbol type for the PUCCH transmission is determined as non-SBFD symbol, the UE shall only consider slots containing consecutive non-SBFD symbols, that are not DL symbols indicated by tdd-UL-DL-ConfigurationCommon or tdd-UL-DL-ConfigurationDedicated if provided or SS/PBCH block symbols, starting from the first symbol provided by startingSymbolIndex, with a length equal to or larger than the number of symbols provided by nrofsymbols. |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · `[123-R19-SBFD]`

**Agreement** · `8.5` Maintenance on Enhancements of network energy savings for NR · `RAN1#123:8.5:005` · 후보

> The following is background information:
> | For a cell supporting on-demand SSB SCell operation, PUSCH available slot counting (as described in Clause 6.1.2.1 of TS 38.214) PUSCH transmissions, e.g., repetition types A and B, TBoMS, CG-PUSCH (as described in Clause 6.1.2.3 of TS 38.214) Multi-PUSCH scheduling by a single DCI (as described in Clauses 6.1 and 6.1.2.1 of TS 38.214) PUCCH repetition (as described in Clause 9.2.6 of TS 38.213) PUCCH deferral (as described in Clause 9.2.5.4 of TS 38.213) UTO-UCI (as described in Clause 9.3.1 of TS 38.213) CPU occupancy (as described in Clause 5.2.1.6 of TS 38.214) the SS/PBCH blocks at least for the above Clauses can be replaced by Union of all configured OD-SSB configuration(s) in RRC for Case #1, and Union of AO-SSB and all configured OD-SSB configuration(s) in RRC for Case #2. |
> The following is an endorsed TP to be captured in TS 38.213 and TS 38.214.
> It is up to the editors in which clause(s) to capture the following endorsed TP. It is preferred to minimize the affected number of clause(s), e.g. one clause.
> | In the following, if a UE is not provided SS/PBCH block indexes by ssb-PositionsInBurst in ServingCellConfigCommon and is provided od-ssb-Config, reference to SS/PBCH blocks is for the union of SS/PBCH blocks provided by each combination of od-ssb-SFN-Offset, od-ssb-halfFrameIndex, od-ssb-PositionsInBurst and od-ssb-Periodicity in od-ssb-Config. If the UE is provided SS/PBCH block indexes by ssb-PositionsInBurst in ServingCellConfigCommon and is provided od-ssb-Config, reference to SS/PBCH blocks is for the union of SS/PBCH blocks provided by ssb-Periodicity and ssb-PositionsInBurst in ServingCellConfigCommon and by each combination of od-ssb-SFN-Offset, od-ssb-halfFrameIndex, od-ssb-PositionsInBurst and od-ssb-Periodicity in od-ssb-Config. |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2508896](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2508896.zip) · `[123-R19-NES]`

**Agreement** · `8.7.1` Maintenance for Rel-19 NR NTN · `RAN1#123:8.7.1:004` · 후보

> The following TP is endorsed in Pricipal for TS 38.214 Clause 5.2.2.5
> | Reason for change: | When a CSI report is transmitted in an OCC group, the CSI reference resource should be defined relative to the first slot in the OCC group. |
> | Summary of change: | The CSI reference resource is defined relative to the first slot in the OCC group. |
> | Consequences if not approved: | The UE may not be able to fulfill the timeline requirements for generating a CSI report. |
> | 5.2.2.5 CSI reference resource definition <unchanged text omitted> The CSI reference resource for a serving cell is defined as follows: - In the frequency domain, the CSI reference resource is defined by the group of downlink physical resource blocks corresponding to the band to which the derived CSI relates. In the time domain, the CSI reference resource for a CSI reporting in uplink slot n', or a CSI reporting in an OCC group starting in uplink slot n' if OCC is enabled, is defined by a single downlink slot , where is a parameter configured by higher layer as specified in clause 4.2 of [6, TS 38.213], and where is the subcarrier spacing configuration for with a value of 0 for frequency range 1 and for FR2-NTN, < unchanged text omitted > | 5.2.2.5 CSI reference resource definition <unchanged text omitted> The CSI reference resource for a serving cell is defined as follows: - In the frequency domain, the CSI reference resource is defined by the group of downlink physical resource blocks corresponding to the band to which the derived CSI relates. In the time domain, the CSI reference resource for a CSI reporting in uplink slot n', or a CSI reporting in an OCC group starting in uplink slot n' if OCC is enabled, is defined by a single downlink slot , where is a parameter configured by higher layer as specified in clause 4.2 of [6, TS 38.213], and where is the subcarrier spacing configuration for with a value of 0 for frequency range 1 and for FR2-NTN, < unchanged text omitted > |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509589](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509589.zip)

**Agreement** · `8.8` Maintenance on others · `RAN1#123:8.8:007` · 후보 · 관련 주제: CSI-RS

> Endorse the following TP to TS38.214 Section 5.2.1.6
> | 5.2.1.6 CSI processing criteria <Unchanged parts are omitted> For a report setting ltm-CSI-ReportConfig configured with reportQuantity is set to 'cri-RI-PMI-CQI': - If the UE is capable of performing CSI measurement for CSI acquisition for candidate cell(s) before receiving the LTM Cell Switch Command MAC CE [10, TS 38.321]: - For a periodic CSI-RS, the CSI-RS resource and CSI-RS ports within the CSI-RS resource are counted as active in a duration of time starting when the periodic CSI-RS resource is configured by higher layer signaling until, and ending at the end of when the reception of the LTM cell switch command MAC CE is applied or a RRC reconfiguration message when the periodic CSI-RS configuration is released, whichever occurs first. - For a semi-persistent CSI-RS, the CSI-RS resource and CSI-RS ports within the CSI-RS resource are counted as active in a duration of time starting from the end of when the activation command MAC CE is applied until, and ending at the end of when the reception of the LTM cell switch command MAC CE or a deactivation command MAC CE is applied, whichever occurs first. - If the UE is only capable of performing CSI measurement for CSI acquisition for a candidate cell (given by Target Configuration ID field in the LTM Cell Switch Command MAC CE) after receiving the LTM Cell Switch Command MAC CE [10, TS 38.321], no CSI-RS resource and CSI-RS ports are counted as active before the reception of the LTM Cell Switch Command MAC CE [10, TS 38.321]. <Unchanged parts are omitted> |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509087](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509087.zip)

**Agreement** · `9.2` UE features Batch B · `RAN1#123:9.2:004` · 후보

> Support the following new components in FG 60-8
> - Maximum number of aperiodic CSI report setting per BWP for L1-CLI-RSSI report
>   - Candidate values: {1, 2, 3, 4}
> - Maximum number of configured L1 CLI-RSSI measurement resources (sum of aperiodic/semi-persistent/periodic) per CC
>   - Candidate values: All integers from 1 to 32
> - Maximum number of simultaneous L1 CLI-RSSI measurement resources with resource type #1/#2 (sum of aperiodic/semi-persistent/periodic) per CC
>   - Candidate values: All integers from 1 to 32

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx)

**Agreement** · `9.2` UE features Batch B · `RAN1#123:9.2:011` · 후보

> Introduce the following FG 66-8/8a/8b:
> | 66-8 | Two HARQ-ACK codebooks with up to one sub-slot based HARQ-ACK codebook simultaneously constructed for supporting HARQ-ACK codebooks with different priorities by DCI format 1_3 with different SCS and/or different carrier type | 1. Supports two HARQ-ACK codebooks with different priorities to be simultaneously constructed with the restriction up to one sub-slot based HARQ-ACK codebook. 2. Supports separate PUCCH configuration for different HARQ-ACK codebooks. 3. Supports 2-level priority of HARQ-ACK for dynamically scheduled PDSCH and SPS PDSCH. 4. Supports a DCI format 1_3 scheduling PDSCH with different HARQ-ACK priorities when only DCI format 0_3/1_3 is configured per BWP. 5. Supports separate configuration of parameters PDSCH-HARQ-ACK-Codebook, UCI-OnPUSCH and 'codeBlockGroupTransmission" for different HARQ-ACK codebooks. 6. Supported maximum number of actual PUCCH transmissions for HARQ-ACK within a slot Candidate values for the component 6 of this FG is: For NCP, {4, 5, 6, 7} for 2-symbol*7 sub-slot configuration; For ECP, the candidate value is {4,5,6} for 2-symbol*6 sub-slot configuration 7. Support intra-UE multiplexing/prioritization of UL overlapping channels/signals with two priority levels for HARQ-ACK | 66-1 | Yes |  |  | Per FS | N/A | N/A | N/A | If a UE reports both 11-3 and this FG, it can support two slot-based HARQ-ACK codebooks, and one slot-based and one-sub-slot-based HARQ-ACK codebooks. If a UE reports this FG but not 11-3, it can only support two slot-based HARQ-ACK codebooks. The number of PUCCHs for CSI reporting per slot is not impacted compared with Rel-15 by introducing the new HARQ-ACK CBs Component 6 is applied to the sub-slot HARQ-ACK codebook. It is assumed that only 1 actual PUCCH transmission for HARQ-ACK within a slot for slot-based HARQ-ACK codebook. Component 6 is reported for 2-symbol*7 sub-slot configuration. For 7-symbol*2 sub-slot configuration, the value of component 6 is {2} for both NCP and ECP cases. For component 6, maximum of 1 actual PUCCH transmission for HARQ-ACK within a slot for slot-based HARQ-ACK codebook. Thus value reported for component 6 has no meaning for "slot-based + slot based". For component 6, same values as for FG11-4 are reported (if the UE also report FG11-4) | Optional with capability signaling |
> | 66-8a | Two HARQ-ACK codebooks with two sub-slot based HARQ-ACK codebook simultaneously constructed for supporting HARQ-ACK codebooks with different priorities by DCI format 1_3 with different SCS and/or different carrier type | 1. Supports two subslot based HARQ-ACK codebooks with different priorities to be simultaneously constructed. 2. Supports separate PUCCH configuration for different HARQ-ACK codebooks. 3. Supports 2-level priority of HARQ-ACK for dynamically scheduled PDSCH and SPS PDSCH. 4. Supports a DCI format 1_3 scheduling PDSCH with different HARQ-ACK priorities when only DCI format 0_3/1_3 is configured in USS per BWP. 5. Supports separate configuration of parameters PDSCH-HARQ-ACK-Codebook, UCI-OnPUSCH and "codeBlockGroupTransmission" for different HARQ-ACK codebooks. 6. Supported maximum number of actual PUCCH transmissions for HARQ-ACK within a slot. Candidate values for the component 6 of this FG is: For NCP, {4, 5, 6, 7} for 2-symbol*7 sub-slot configuration; For ECP, the candidate value is {4,5,6} for 2-symbol*6 sub-slot configuration. | 11-3, 66-8 | Yes |  |  | Per FS | N/A | N/A | N/A | The number of PUCCHs for CSI reporting per slot is not impacted compared with Rel-15 by introducing the new HARQ-ACK CBs Component 6 is applied to the two sub-slot HARQ-ACK codebooks, respectively. Component 6 is reported for 2-symbol*7 sub-slot configuration. For 7-symbol*2 sub-slot configuration, the value of component 6 is {2} for both NCP and ECP cases. For component 6, same values as for FG11-4a are reported (if the UE also report FG11-4a) | Optional with capability signaling |
> | 66-8b | DL priority indication in DCI with mixed DCI formats including DCI format 1_3 with different SCS and/or different carrier type | Support of priority indicator field configured in DCI formats 1_3 and (1_1 or 1_2) in a BWP when configured to monitor both DCI formats 1_3 and (1_1 or 1_2) in the BWP | 66-8 |  |  |  | Per UE | No | No | N/A |  | Optional with capability signaling |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx)

**Agreement** · `9.3` UE features Batch C · `RAN1#123:9.3:001` · 후보 · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-2 | UE-side beam prediction for BM Case1 for inference | 1. Support of beam prediction with reporting of predicted beam index for BM-Case1 for inference with UE-side model 3. Maximum number of inference report(s) configured for BM-Case1 per BWP 3a. Maximum number of inference report(s) configured for BM-Case1 across all CCs 6. Support of SSB as RS type for Set B 6a. Support of CSI-RS as RS type for Set B 6b. Support of SSB as RS type for Set A 6c. Support of CSI-RS as RS type for Set A 7a: Supported maximum number of resources for Set B 7b: Supported maximum number of resources for Set A 8. Supported CSI-RS resource types for Set B 9. Supported inference report types 11. Supported BM-Case 1 sub-usecase(s) 12. Supported maximum number of predicted beams in each reporting instance 13. Supported number of occupied CPU 14. Supported number of occupied CPU,2/CPU,3 15. Supported value of di for the relaxation of Z3 timeline, where i is the index of SCS, i=1,2,3,4,5,6 corresponding to 15,30,60,120,480,960 kHz SCS 16. Supported value of d’i for the relaxation of Z’3 timeline, where i is the index of SCS, i=1,2,3,4,5,6 corresponding to 15,30,60,120,480,960 kHz SCS 17. Occupied resource pool between CPU,2 and CPU,3 | 2-35 | yes | n/a | UE-sided beam prediction for BM Case 1 for inference is not supported | Per band | n/a | n/a | n/a | Component 3 candidate values: - Periodic reporting: {1, 2, 3, 4} - Aperiodic reporting: {1, 2, 3, 4} - Semi-persistent reporting: {1, 2, 3, 4} Component 3a candidate values: {1, 2, 3, 4, 8, 10, 12, 16} Component 7a candidate values: {4, 8, 16} Component 7b candidate values: {8, 16, 32, 64} Component 8 candidate values: {Periodic CSI-RS, Semi-persistent CSI-RS, Aperiodic CSI-RS} Component 9 candidate values: {Periodic CSI report, Aperiodic CSI report, semi-persistent CSI report} Component 11 candidate values: {setB-subset-of-setA, setB-different-from-setA, both} Component 12 candidate values: {1, 2, 3, 4} Component 13 candidate values: {0, 1, 2, …, 8} Component 14 candidate values: {0, 1, 2, …, 8} Note: The values of component 13 and 14 are not allowed to be 0 simultaneously Component 15 candidate values: d1 is FFS {7,14, 21, 28, 35, 42, 56} d2 is FFS {14, 28, 42, 56, 70, 84, 112} d3 is FFS {28, 56, 84,112, 140, 168, 224} d4 is FFS {56, 112, 168, 224, 280, 336, 448} d5 is FFS {224, 448, 672, 896, 1120, 1344, 1792} d6 is FFS {448, 896, 1344, 1792} Component 16 candidate values: d1 is FFS {7,14, 21, 28, 35, 42, 56} d2 is FFS {14, 28, 42, 56, 70, 84, 112} d3 is FFS {28, 56, 84,112, 140, 168, 224} d4 is FFS {56, 112, 168, 224, 280, 336, 448} d5 is FFS {224, 448, 672, 896, 1120, 1344, 1792} d6 is FFS {448, 896, 1344, 1792} Component 17 candidate values: {1, 2} representing the first CPU pool (i.e., CPU,2) and the second CPU pool (i.e., CPU,3), respectively | Optional with capability signalling |
> | 58. NR_AIML_air | 58-1-4 | UE-side beam prediction for BM Case2 for inference | 1. Support of beam prediction with reporting of predicted beam index for BM-Case2 for inference with UE-side model 3. Maximum number of inference report(s) configured for BM-Case2 per BWP 3a. Maximum number of inference report(s) configured for BM-Case2 across all CCs 6. Support of SSB as RS type for Set B 6a. Support of CSI-RS as RS type for Set B 6b. Support of SSB as RS type for Set A 6c. Support of CSI-RS as RS type for Set A 7a: Supported maximum number of resources for Set B 7b: Supported maximum number of resources for Set A 8. Supported CSI-RS resource types for Set B 9. Supported inference report types 11. Supported maximum number of predicted beams in each predicted time instance 12. Supported maximum number of predicted time instances 13. Supported maximum total number of reported predicted beams for predicted time instances in one report 15. Supported value(s) of time gap between predicted time instances and between reference time to the first future time instance 21. supported number of occupied CPU 22. supported number of occupied CPU,2/CPU,3 23. supported value of di for the relaxation of Z3 timeline, where i is the index of SCS, i=1,2,3,4,5,6 corresponding to 15,30,60,120,480,960 kHz SCS 24. supported value of d’i for the relaxation of Z’3 timeline, where i is the index of SCS, i=1,2,3,4,5,6 corresponding to 15,30,60,120,480,960 kHz SCS 25. Occupied resource pool between CPU,2 and CPU,3 | 2-35 | yes | n/a | UE-side beam prediction for BM-Case2 for inference is not supported | Per band | n/a | n/a | n/a | Component 3 candidate values: - Periodic reporting: {1, 2, 3, 4} - Aperiodic reporting: {1, 2, 3, 4} - Semi-persistent reporting: {1, 2, 3, 4} Component 3a candidate values: {1, 2, 3, 4, 8, 10, 12, 16} Component 7a candidate values: {4, 8, 16, 32, 64} Component 7b candidate values: {4, 8, 16, 32, 64} Component 8 candidate values: {Periodic CSI-RS, Semi-persistent CSI-RS} Component 9 candidate values: {Periodic CSI report, Aperiodic CSI report, semi-persistent CSI report} Component 11 candidate values: {1, 2, 3, 4} Component 12 candidate values: {1, 2, 4, 8} Component 13 candidate values: {1, 2, 4, 6, 8, 12, 16, 32} Component 15 candidate values: {10ms, 20ms, 40ms, 80ms, 160ms} Component 21 candidate values: {0, 1, 2, … 8} Component 22 candidate values: {0, 1, 2, … 8} Note: The values of component 21 and 22 are not allowed to be 0 simultaneously. Component 23 candidate values: d1 is FFS {14, 28, 42, 56, 70, 84, 98} d2 is FFS {28, 56, 84, 112, 140, 168, 196} d3 is FFS {56, 112, 168, 224, 280, 336, 392} d4 is FFS {112, 224, 336, 448} d5 is FFS {448, 896, 1344, 1792} d6 is FFS { 896, 1792} Component 24 candidate values: d1 is FFS {14, 28, 42, 56, 70, 84, 98} d2 is FFS {28, 56, 84, 112, 140, 168, 196} d3 is FFS {56, 112, 168, 224, 280, 336, 392} d4 is FFS {112, 224, 336, 448} d5 is FFS {448, 896, 1344, 1792} d6 is FFS { 896, 1792} Component 25 candidate values: {1, 2} representing the first CPU pool (i.e., CPU,2) and the second CPU pool (i.e., CPU,3), respectively Note: UE should not report non-zero value for Component 22 if FG 58-0-1 is not signalled | Optional with capability signalling |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx)

**Agreement** · `9.3` UE features Batch C · `RAN1#123:9.3:005` · 후보

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-0-1 | CSI report framework for UE-side inference | 1. Number of CPU,x pools N 2. Maximum number of CPU,x in each CPU,x pool of UE-sided inference for CSI report(s) simultaneously in a CC 3. Maximum number of CPU,x in each CPU,x pool of UE-sided inference for CSI report(s) simultaneously across all CCs | 2-35 | yes | n/a | Maximum number of CPU(s),x per each CPU pool and CPU pool(s) for UE-sided inference is unknown to the network | Per band and per BC | n/a | n/a | n/a | Component 1 candidate values: {1,2} Component 2candidate values: {1…8} Component 3 candidate values: {1…32} Note: Component 2 and 3 candidate values are signalled separately for each pool A UE that does not support this FG should not report non-zero occupied CPU,2 or CPU,3 values in any dependency FG | Optional with capability signalling |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx)

**Agreement** · `9.3` UE features Batch C · `RAN1#123:9.3:007` · 후보 · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 63. NR_Mob_Ph4 | 63-8 | Inclusion of current SpCell in the L1 measurement report based on CSI-RS (s) | 1. Support of always including the current SpCell in the L1 measurement report based on CSI-RS (s) | 63-1, or 63-2, 63-1a, or 63-2a | Yes | No | UE does not always include measurement report for SpCell in the L1 measurement report based on CSI-RS (s) | Per BC | n/a | n/a | n/a |  | Optional with capability signalling |
> | 63. NR_Mob_Ph4 | 63-10 | CSI-RS measurement and CSI reporting without CSI-IM reception | 1. Support of CSI-RS measurement and CSI reporting for candidate cells without CSI-IM resource configuration | 63-6 or 63-6a or 63-7 or 63-7a or 63-7c or 63-7d | Yes | No | CSI -RS measurement and CSI reporting without CSI-IM reception is not supported | Per band | n/a | n/a | n/a |  | Optional with capability signaling |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx)

**Agreement** · `9.3` UE features Batch C · `RAN1#123:9.3:009` · 후보 · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-5b | Extended Rel-18 eType-II Doppler codebook for 128 Tx ports | 1. Support of extended Rel-18 Type-II Doppler codebook for 128 Tx ports by aggregating multiple NZP CSI-RS resource groups within 1 slot 2. Support X=1 CQI based on the first/earliest slot of the CSI reporting window and the first/earliest predicted PMI (TDCQI=’1-1’) 3. Support of PMI subband R=1 for extended Rel-18 eType II Doppler codebook 4. Support parameter combinations with L=2,4 5. Support for rank = 1,2 6. Support 64 ports 7. A list of supported combinations, each combination is { Max # of Tx ports in one resource, Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 8. Supported processing capability 9. Value of Y for CPU occupation (OCPU = Y.N4), when P/SP-CSI-RS is configured for CMR 10. Value of Y for CPU occupation (OCPU = Y. KDOPP), when A-CSI-RS is configured for CMR 11. Support for the size of DD-basis, N4=1 12. Scaling factor for active resource counting Kp 13. Support 4 CSI-RS resources in a resource group for aperiodic CSI-RS resource set or in a resource set for periodic CSI-RS resource set 14. A list of supported combinations, each combination is {Max # of resources and total # of Tx ports} per CC simultaneously | 59-2-1-5 | yes | n/a | Extended Rel-18 Type-II Doppler codebook is not supported for 128 Tx ports, aggregated CSI-RS resources within one slot | Per band and per BC | n/a | n/a | n/a | Component 7 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Component 8 candidate value {Capability 1, Capability 2} Component 9 candidate values: {1, 2, 3} Component 10 candidate values: {1, 2, 3} Component 12 candidate values: {1, 2, 4} Component 14 candidate values a. {1, …, 64, 128, 256} b. {64, …, 256, 512, 768, 1024} Note: For component of processing capability Capability 1: Legacy timeline OCPU = Y x N4 x ceil(P/32) ), when P/SP-CSI-RS is configured for CMR OCPU = Y x KDOPP x ceil(P/32)), when A-CSI-RS is configured for CMR Capability 2: Scale the legacy timeline by ceil(P/32) where P is the total number of ports across all the K aggregated CSI-RS resources OCPU = Y x N4, when P/SP-CSI-RS is configured for CMR OCPU = Y x KDOPP, when A-CSI-RS is configured for CMR Note: maximum OCPU is 8 Note: KDOPP is the number of CSI-RS resource groups configured for channel measurement, and each CSI-RS resource groups contain K CSI-RS resources for aggregating up to 128 ports | Optional with capability signalling |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx)

**Agreement** · `9.3` UE features Batch C · `RAN1#123:9.3:011` · 후보

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-7 | Group-specific 3-bit scaling factors for up to 128 ports | Support of group-specific 3-bit scaling factors | One or more of {59-2-1-1, 59-2-1-1c} | yes | n/a | Group-specific 3-bit scaling factors is not supported | Per band and per BC | n/a | n/a | n/a | Candidate values: {’rank-1’, ‘rank-1 and rank-2’} Note: ‘rank-1’is the lower capability Note: 3-bit scaling applies only to the Type-I SP codebook | Optional with capability signalling |
> .

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx)

**Agreement** · `9.3` UE features Batch C · `RAN1#123:9.3:013` · 후보 · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-1-5l | Processing timeline for CSI reference slot for extended Rel-18 Type-II Doppler codebook for up to 128 ports | 1. Aperiodic CSI report timing relaxation, w, extended Rel-18 Type-II Doppler codebook for up to 128 ports 2. Aperiodic CSI report timing relaxation, type, for extended Rel-18 Type-II Doppler codebook for up to 128 ports | 59-2-1-5 | Yes | n/a |  | Per band and Per BC | n/a | n/a | n/a | Component 1 candidate values: UE reports candidate value, w, independently for each SCS in unit of symbols: {14*(KP–1)*d, 14*KP*d} Note: Kp is according to Component 12 of FG59-2-5 Note: d=4 (minimum periodicity of periodic CSI-RS) Component 2 candidate values: {CAP1, CAP2} Note: For Component 2 ‘CAP2’ is the lower capability For N4 = 1 1) For AP CSI-RS: (Z,Z’) = (Z2 + 14*( KDOPP –1)*m, Z'2) 2) For P/SP CSI-RS: (Z,Z’) = (Z2 + w, Z'2) For N4 > 1 and CAP1 in component 2 1) For AP CSI-RS: (Z,Z’) = (Z2 + 14*( KDOPP –1)*m, Z'2) 2) For P/SP CSI-RS: (Z,Z’) = (Z2 + w, Z'2) For N4 > 1 and CAP2 in component 2 1) For AP CSI-RS: (Z,Z’) = (Z2 + 14*( KDOPP –1)*m + Z'2, 2Z'2) 2) For P/SP CSI-RS: (Z,Z’) = (Z2 + w + Z'2, 2Z'2) Z2/Z'2 are defined in Table 5.4-2 in TS38.214 KDOPP is the number of CSI-RS resource groups configured for channel measurement, and each CSI-RS resource groups contain K CSI-RS resources for aggregating up to 128 ports M = {1,2}, is the offset between two adjacent AP CSI-RS resource groups for the CMR in slots This FG is not applicable to FR 2-2 | Optional with capability signalling |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx)

**Agreement** · `9.3` UE features Batch C · `RAN1#123:9.3:016` · 후보 · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-4 | UE-side beam prediction for BM Case2 for inference | 1. Support of beam prediction with reporting of predicted beam index for BM-Case2 for inference with UE-side model 3. Maximum number of inference report(s) configured for BM-Case2 per BWP 3a. Maximum number of inference report(s) configured for BM-Case2 across all CCs 6. Support of SSB as RS type for Set B 6a. Support of CSI-RS as RS type for Set B 6b. Support of SSB as RS type for Set A 6c. Support of CSI-RS as RS type for Set A 7a: Supported maximum number of resources for Set B 7b: Supported maximum number of resources for Set A 7c: Supported minimum number of received transmission occasions KBM for Set B 8. Supported CSI-RS resource types for Set B 9. Supported inference report types 11. Supported maximum number of predicted beams in each predicted time instance 12. Supported maximum number of predicted time instances 13. Supported maximum total number of reported predicted beams for predicted time instances in one report 15. Supported value(s) of time gap between predicted time instances and between reference time to the first future time instance 21. supported number of occupied CPU 22. supported number of occupied CPU,2/CPU,3 23. supported value of di for the relaxation of Z3 timeline, where i is the index of SCS, i=1,2,3,4,5,6 corresponding to 15,30,60,120,480,960 kHz SCS 24. supported value of d’i for the relaxation of Z’3 timeline, where i is the index of SCS, i=1,2,3,4,5,6 corresponding to 15,30,60,120,480,960 kHz SCS 25. Occupied resource pool between CPU,2 and CPU,3 | 2-35 | yes | n/a | UE-side beam prediction for BM-Case2 for inference is not supported | Per band | n/a | n/a | n/a | Component 3 candidate values: - Periodic reporting: {1, 2, 3, 4} - Aperiodic reporting: {1, 2, 3, 4} - Semi-persistent reporting: {1, 2, 3, 4} Component 3a candidate values: {1, 2, 3, 4, 8, 10, 12, 16} Component 7a candidate values: {4, 8, 16, 32, 64} Component 7b candidate values: {4, 8, 16, 32, 64} Component 7c candidate values: {2, 4, 8} Component 8 candidate values: {Periodic CSI-RS, Semi-persistent CSI-RS} Component 9 candidate values: {Periodic CSI report, Aperiodic CSI report, semi-persistent CSI report} Component 11 candidate values: {1, 2, 3, 4} Component 12 candidate values: {1, 2, 4, 8} Component 13 candidate values: {1, 2, 4, 6, 8, 12, 16, 32} Component 15 candidate values: {10ms, 20ms, 40ms, 80ms, 160ms} Component 21 candidate values: {0, 1, 2, … 8} Component 22 candidate values: {0, 1, 2, … 8} Note: The values of component 21 and 22 are not allowed to be 0 simultaneously. Component 23 candidate values: d1 is {14, 28, 42, 56, 70, 84, 98} d2 is {28, 56, 84, 112, 140, 168, 196} d3 is {56, 112, 168, 224, 280, 336, 392} d4 is {112, 224, 336, 448} d5 is {448, 896, 1344, 1792} d6 is {896, 1792} Component 24 candidate values: d'1 is {14, 28, 42, 56, 70, 84, 98} d’2 is {28, 56, 84, 112, 140, 168, 196} d’3 is {56, 112, 168, 224, 280, 336, 392} d’4 is {112, 224, 336, 448} d’5 is {448, 896, 1344, 1792} d’6 is {896, 1792} Component 25 candidate values: {1, 2} representing the first CPU pool (i.e., CPU,2) and the second CPU pool (i.e., CPU,3), respectively Note: UE should not report non-zero value for Component 22 if FG 58-0-1 is not signalled | Optional with capability signalling |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx)

**Agreement** · `11.2` Evaluation assumptions for 6GR air interface · `RAN1#123:11.2:007` · 후보

> For 6GR evaluation, the following are assumed for system-level simulation:
> | Parameters | Indoor Hotspot | Dense Urban | Rural | Urban Macro | Suburban Macro |
> | ISD | 20m, equivalent to 12TRxPs per 120m x 50m | Macro layer: 200m | ISD 1: 1732m ISD 2: 5000m | Macro: 500m | ISD 1: 1299m ISD 2: 1732m |
> | BS antenna height | 3m | 25m for macro cells and 10m for micro cells | 35 m | 25m for macro cells and 10m for micro cells | Alt 1: 35m(baseline) Alt 2: 25m(optional) |
> | BS noise figure | Around 7GHz and below: 5dB Around 15GHz and above: 7dB | Around 7GHz and below: 5dB Around 15GHz and above: 7dB | Around 7GHz and below: 5dB Around 15GHz and above: 7dB | Around 7GHz and below: 5dB Around 15GHz and above: 7dB | Around 7GHz and below: 5dB Around 15GHz and above: 7dB |
> | UE antenna height | TR38.901 Indoor-Office Table 7.2-2 | TR38.901 UMi/UMa Table 7.2-1 | TR38.901 RMa Table 7.2-3 | TR38.901 UMa Table 7.2-1 | TR38.901 SMa Table 7.2-5 |
> | UE noise figure | Around 7GHz and below: [7, 9]dB Around 15GHz and above: 13dB, 10dB | Around 7GHz and below: [7, 9]dB Around 15GHz and above: 13dB, 10dB | Around 7GHz and below: [7, 9]dB Around 15GHz and above: 13dB, 10dB | Around 7GHz and below: [7, 9]dB Around 15GHz and above: 13dB, 10dB | Around 7GHz and below: [7, 9]dB Around 15GHz and above: 13dB, 10dB |
> | UE Receiver | MMSE-IRC as the baseline R-ML Receiver as optional (FFS modelling) | MMSE-IRC as the baseline R-ML Receiver as optional (FFS modelling) | MMSE-IRC as the baseline R-ML Receiver as optional (FFS modelling) | MMSE-IRC as the baseline R-ML Receiver as optional (FFS modelling) | MMSE-IRC as the baseline R-ML Receiver as optional (FFS modelling) |
> | UE Power control parameter for UL | Company report | Company report | Company report | Company report | Company report |
> | Channel model | TR 38.901 v19.1.0 Indoor-Office | TR 38.901 v19.1.0 UMa/UMi | TR 38.901 v19.1.0 RMa | TR 38.901 v19.1.0 UMa | TR 38.901 v19.1.0 SMa, 0% vegetation. |
> | Numerology | In line with AI 11.3 | In line with AI 11.3 | In line with AI 11.3 | In line with AI 11.3 | In line with AI 11.3 |
> | Scheduling | Proportional fairness (PF) | Proportional fairness (PF) | Proportional fairness (PF) | Proportional fairness (PF) | Proportional fairness (PF) |
> | Inter-cell interference model | Explicitly and realistically modelled | Explicitly and realistically modelled | Explicitly and realistically modelled | Explicitly and realistically modelled | Explicitly and realistically modelled |
> | Inter-cell interference estimation model | Alt 1: Ideal, calculated by ground truth channel matrix Alt 2: Realistic model, Company report, e.g., Wishart distribution-based model; retain only diagonal elements of interference Cov. Matrix. | Alt 1: Ideal, calculated by ground truth channel matrix Alt 2: Realistic model, Company report, e.g., Wishart distribution-based model; retain only diagonal elements of interference Cov. Matrix. | Alt 1: Ideal, calculated by ground truth channel matrix Alt 2: Realistic model, Company report, e.g., Wishart distribution-based model; retain only diagonal elements of interference Cov. Matrix. | Alt 1: Ideal, calculated by ground truth channel matrix Alt 2: Realistic model, Company report, e.g., Wishart distribution-based model; retain only diagonal elements of interference Cov. Matrix. | Alt 1: Ideal, calculated by ground truth channel matrix Alt 2: Realistic model, Company report, e.g., Wishart distribution-based model; retain only diagonal elements of interference Cov. Matrix. |
> | Channel estimation assumption | Alt 1: Ideal for benchmark Alt 2: Realistic, company report, e.g., direct/explicit RS estimation, apply gauss noise to real channel matrix, or random | Alt 1: Ideal for benchmark Alt 2: Realistic, company report, e.g., direct/explicit RS estimation, apply gauss noise to real channel matrix, or random | Alt 1: Ideal for benchmark Alt 2: Realistic, company report, e.g., direct/explicit RS estimation, apply gauss noise to real channel matrix, or random | Alt 1: Ideal for benchmark Alt 2: Realistic, company report, e.g., direct/explicit RS estimation, apply gauss noise to real channel matrix, or random | Alt 1: Ideal for benchmark Alt 2: Realistic, company report, e.g., direct/explicit RS estimation, apply gauss noise to real channel matrix, or random |
> | Feedback assumption | Alt 1: Ideal Alt 2: Realistic, company report, e.g., consider feedback delay and overhead; codebook; | Alt 1: Ideal Alt 2: Realistic, company report, e.g., consider feedback delay and overhead; codebook; | Alt 1: Ideal Alt 2: Realistic, company report, e.g., consider feedback delay and overhead; codebook; | Alt 1: Ideal Alt 2: Realistic, company report, e.g., consider feedback delay and overhead; codebook; | Alt 1: Ideal Alt 2: Realistic, company report, e.g., consider feedback delay and overhead; codebook; |
> | O2I penetration loss (X% high loss, Y% low loss) | NA | Two options are supported: Option 1: 80% low loss, 20% high loss; Option 2: 50% low loss, 50% high loss | 100% low loss | Two options are supported: Option 1: 80% low loss, 20% high loss; Option 2: 50% low loss, 50% high loss | Option 1: 100% Low-loss A Model as TR38.901. Option 2: 50% Low-loss A 50% Low-loss Model as TR38.901. |
> | Mechanic tilt | 180° in GCS (pointing to the ground) as baseline | 90° in GCS (pointing to horizontal direction) as baseline. Company can report if not follow the baseline. | 90° in GCS (pointing to horizontal direction) as baseline. Company can report if not follow the baseline. | 90° in GCS (pointing to horizontal direction) as baseline. Company can report if not follow the baseline. | Baseline: 95° in GCS (pointing to horizontal direction) for ISD = 1299m; 92° in GCS (pointing to horizontal direction) for ISD = 1732m; Company can report if not follow the baseline. |
> | Electrical tilt | Company can report other values for evaluations. | Company can report other values for evaluations. | Company can report other values for evaluations. | Company can report other values for evaluations. | Company can report other values for evaluations. |
> | Handover margin (dB) | 1dB as baseline. 0dB and 3dB as optional configuration. | 1dB as baseline. 0dB and 3dB as optional configuration. | 1dB as baseline. 0dB and 3dB as optional configuration. | 1dB as baseline. 0dB and 3dB as optional configuration. | 1dB as baseline. 0dB and 3dB as optional configuration. |
> | UE attachment | Based on RSRP from BS | Based on RSRP from BS | Based on RSRP from BS | Based on RSRP from BS | Based on RSRP from BS |
> | Wrapping around method | No wrapping around | Geographical distance-based wrapping | Geographical distance-based wrapping | Geographical distance-based wrapping | Geographical distance-based wrapping |
> | Multi-TRP operation, e.g., ideal or non-ideal backhaul/sync | Backhaul: ideal or non-ideal; sync: ideal or non-ideal; Company reports the assumptions of the non-ideal backhaul/non-ideal sync. | Backhaul: ideal or non-ideal; sync: ideal or non-ideal; Company reports the assumptions of the non-ideal backhaul/non-ideal sync. | Backhaul: ideal or non-ideal; sync: ideal or non-ideal; Company reports the assumptions of the non-ideal backhaul/non-ideal sync. | Backhaul: ideal or non-ideal; sync: ideal or non-ideal; Company reports the assumptions of the non-ideal backhaul/non-ideal sync. | Backhaul: ideal or non-ideal; sync: ideal or non-ideal; Company reports the assumptions of the non-ideal backhaul/non-ideal sync. |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · `[123-R20-6GR-Evaluation]`

### RAN1#122bis — 24건

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#122bis:8.1:001` · 후보

> The following TP for TS 38.214 Clause 5.2.1.4.3b is endorsed.
> Reason for change: The slot of transmission occasion for monitoring is unclear for the linkage of the corresponding CSI report for inference.
> Summary of change: Clarify the first slot of transmission occasion for monitoring is used for the linkage.
> Consequences if not approved: gNB and UE may have different understanding on the linkage.
> | TS 38.214 Clause 5.2.1.4.3b RS-PAI Reporting <omitted texts> - check a condition : - for the transmission occasion of the second CSI Reporting Setting, there is a linked report of the first CSI Reporting Setting. When nroftimeinstance-r19 is not configured in the first Reporting Setting, the linking is determined if CSI reference resource of a report of the first CSI Reporting Setting has a minimal slot offset, no larger than 64 slots, from the first slot of the transmission occasion of the corresponding Resource Set for channel measurement of the second CSI Reporting Setting. When nroftimeinstance-r19 is configured in the first Reporting Setting, timeinstanceformonitoring-r19 configured in the second CSI Reporting Setting indicates the timeinstanceformonitoring-r19-th time instance among nroftimeinstance-r19 time instance(s), and the linking is determined if the slot corresponding to the time instance indicated by timeinstanceformonitoring-r19 of a report of the first CSI Reporting Setting has a minimal slot offset, no larger than 64 slots, from the first slot of the transmission occasion of the corresponding Resource Set for channel measurement of the second CSI Reporting Setting; <omitted texts> |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2507998](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2507998.zip) · `[122bis-R19-AI/ML]`

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#122bis:8.1:006` · 후보 · 관련 주제: CSI-RS

> The following TP for TS 38.214 Clause 5.2.1.4.2 is endorsed.
> Reason for change: The configuration restriction of AP RS resource set with no more than 16 resources is too restrictive for Set A for inference.
> Summary of change: For Set A for inference, relax the configuration restriction of AP RS resource set with no more than 16 resources.
> Consequences if not approved: The configuration of more than 16 resource within Set A for inference is not possible.
> | TS 38.214 Clause 5.2.1.4.2 Report quantity configurations <omitted texts> If the UE is configured with a CSI-ReportConfig with the higher layer parameter reportQuantity set to 'cri-RI-LI-PMI-CQI', UE does not expect the CSI-ReportConfig to be configured with higher layer parameter codebookType set to 'typeII-r16' or 'typeII-PortSelection-r16', 'typeII-PortSelection-r17', 'typeII-CJT-r18', 'typeII-CJT-PortSelection-r18', 'typeII-Doppler-r18', 'typeII-Doppler-PortSelection-r18', 'eTypeII-r19', 'TypeII-FePortSelection-r19' or 'typeII-Doppler-r19'. If the UE is configured with a CSI-ReportConfig with higher layer parameter reportQuantity set to 'cri-RSRP', 'cri-SINR', 'none', 'cri-RSRP- Index', 'cri-SINR- Index, 'p-cri-r19', 'p-cri-RSRP-r19', 'p-ssb-index-r19', 'p-ssb-index-RSRP-r19', or ‘rs-pai-r19', and the CSI-ReportConfig is linked to a resource setting not configured by resourcesForSetA-r19 and configured with the higher layer parameter resourceType set to 'aperiodic', then the UE is not expected to be configured with more than 16 CSI-RS resources in a CSI-RS resource set contained within the resource setting. <omitted texts> |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2507999](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2507999.zip) · `[122bis-R19-AI/ML]`

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#122bis:8.1:010` · 후보 · 관련 주제: CSI-RS

> The following TP for TS 38.214 is endorsed.
> | Reason for change | During non-active periods of cell DTX, UE is not expected to receive P/SP CSI-RS for CSI report associated with report quantity comprising at least RI which means this can be applied to SP inference report. However, whether it is applied for monitoring report is not clear. |
> | Summary of change | Report quantity ‘csi-pai-r19’ is added. |
> | Consequences if not approved | Inconsistent UE behaviour during non-active periods of cell DTX. |
> | TS38.214 5.1.6.1 CSI-RS reception procedure << Unchanged parts are omitted >> During non-active periods of cell DTX if cell DTX is activated for a serving cell, the UE is not expected to receive the periodic CSI-RS and semi-persistent CSI-RS on the serving cell configured in CSI report configuration in CSI-ReportConfig associated with the higher layer parameter reportQuantity comprising at least 'RI' or 'cjtc-P' or ‘csi-pai-r19’. If the cell DTX is activated for a serving cell [10, TS 38.321], the most recent CSI measurement occasion of semi-persistent CSI-RS resource or periodic CSI-RS resource on the serving cell occurs in active periods of cell DTX for CSI report configured by CSI-ReportConfig associated with the higher layer parameter reportQuantity comprising at least 'RI' or 'cjtc-P' or ‘csi-pai-r19’. << Unchanged parts are omitted >> | TS38.214 5.1.6.1 CSI-RS reception procedure << Unchanged parts are omitted >> During non-active periods of cell DTX if cell DTX is activated for a serving cell, the UE is not expected to receive the periodic CSI-RS and semi-persistent CSI-RS on the serving cell configured in CSI report configuration in CSI-ReportConfig associated with the higher layer parameter reportQuantity comprising at least 'RI' or 'cjtc-P' or ‘csi-pai-r19’. If the cell DTX is activated for a serving cell [10, TS 38.321], the most recent CSI measurement occasion of semi-persistent CSI-RS resource or periodic CSI-RS resource on the serving cell occurs in active periods of cell DTX for CSI report configured by CSI-ReportConfig associated with the higher layer parameter reportQuantity comprising at least 'RI' or 'cjtc-P' or ‘csi-pai-r19’. << Unchanged parts are omitted >> |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508061](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508061.zip) · `[122bis-R19-AI/ML]`

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#122bis:8.1:012` · 후보 · 관련 주제: CSI-RS

> Adopt the following TP for TS 38.214.
> | Reason for change | According to the agreement, Rel-16 eType II codebook is used for calculating both the precoder represented by PMI based on the channel measurement corresponding to the monitoring report and the precoder represented by PMI based on the latest CSI-RS resource transmission occasion, no later than CSI reference resource, corresponding to the inference report. However, the codebook for calculating was not clearly captured by the specification. |
> | Summary of change | Add the corresponding description of the codebook for calculating in TS 38.214. |
> | Consequences if not approved | How to select the codebook for calculating is not clearly defined in TS 38.214, which is not aligned with the agreement. |
> | TS38.214 5.2.1.4.6 CSI-PAI reporting << Unchanged parts are omitted >> - to report CSI-PAI for the second Reporting Setting, the UE is expected to be configured in the second Report Setting with codebookType set to ‘etypeII-r16’ and it shall: <Unrelated part omitted> for , is the RI reported for the CSI report corresponding to the first Reporting Setting, calculate SGCS value(s) as, , , where is the predicted precoder represented by predicted PMI for -th layer, n-th subband and for -th time instance corresponding to the report of the first Reporting Setting, is the precoder represented by non-predicted PMI for -th layer, n-th subband based on the channel measurement corresponding to the second Reporting Setting, and is the precoder represented by PMI for -th layer and n-th subband, , corresponds to the subbands configured by csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband, based on the latest CSI-RS resource transmission occasion, no later than CSI reference resource, corresponding to the report of the first Reporting Setting. Both and are calculated based on the codebookConfig within the second Reporting Setting. The UE is expected to be configured with same csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband configurations for the first CSI Reporting Setting and the second CSI Reporting Setting. << Unchanged parts are omitted >> | TS38.214 5.2.1.4.6 CSI-PAI reporting << Unchanged parts are omitted >> - to report CSI-PAI for the second Reporting Setting, the UE is expected to be configured in the second Report Setting with codebookType set to ‘etypeII-r16’ and it shall: <Unrelated part omitted> for , is the RI reported for the CSI report corresponding to the first Reporting Setting, calculate SGCS value(s) as, , , where is the predicted precoder represented by predicted PMI for -th layer, n-th subband and for -th time instance corresponding to the report of the first Reporting Setting, is the precoder represented by non-predicted PMI for -th layer, n-th subband based on the channel measurement corresponding to the second Reporting Setting, and is the precoder represented by PMI for -th layer and n-th subband, , corresponds to the subbands configured by csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband, based on the latest CSI-RS resource transmission occasion, no later than CSI reference resource, corresponding to the report of the first Reporting Setting. Both and are calculated based on the codebookConfig within the second Reporting Setting. The UE is expected to be configured with same csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband configurations for the first CSI Reporting Setting and the second CSI Reporting Setting. << Unchanged parts are omitted >> |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508062](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508062.zip) · `[122bis-R19-AI/ML]`

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#122bis:8.1:015` · 후보

> Support the configuration of following parameter in a CSI-ReportConfig with the higher layer parameter reportQuantity set to 'none-CSI-r19'
> - CodebookConfig-r18 set to ‘typeII-Doppler-r18’

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508142](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508142.zip) · `[122bis-R19-AI/ML]`

**Agreement** · `8.3` Maintenance on Evolution of NR duplex operation: Sub-band full duplex (SBFD) · `RAN1#122bis:8.3:015` · 후보

> Adopt the following TP in principle to section 5.2.1.4.8, TS 38.214
> | 5.2.1.4.8 L1-CLI-RSSI Reporting <Unchanged part omitted> If the higher layer parameter timeRestrictionForChannelMeasurements in CSI-ReportConfig is set to ‘Configured’, the UE shall derive the channel measurements for computing L1-CLI-RSSI reported in uplink, SBFD or [flexible] slot n based on only the most recent, no later than the CSI reference resource, occasion of CLI-RSSI resources (defined in [4, TS 38.211]) associated with the CSI resource setting. A UE configured with SBFD symbols and with a CLI-RSSI measurement resource in SBFD symbols and across two DL subbands shall derive the frequency resources for L1-CLI-RSSI measurement by excluding the frequency resources outside the RBs that are both in the active DL BWP and in the DL sub-bands and shall report a single wideband L1-CLI-RSSI measurement. A UE configured with SBFD symbols does not expect to be configured with a CSI-ReportConfig associated with CLI-RSSI measurement resources configured within an UL subband and with CLI-RSSI measurement resources configured within one DL subband or across two DL subbands. A UE configured with SBFD symbols does not expect to be configured with CLI-RSSI measurement resources within an UL subband and CLI-RSSI measurement resources within one DL subband or across two DL subbands in a same symbol. |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · `[122bis-R19-SBFD]`

**Agreement** · `8.3` Maintenance on Evolution of NR duplex operation: Sub-band full duplex (SBFD) · `RAN1#122bis:8.3:017` · 후보

> Adopt the following TP in principle to section 5.2.2.7, TS 38.214
> | 5.2.2.7 CLI-RSSI measurement resource <Unchanged parts omitted> [The bandwidth and initial common resource block (CRB) index of a CLI-RSSI resource within a BWP, as defined in Clause 7.4.1.5 of [4, TS 38.211], are determined based on the higher layer parameters nrofRBs and startingRB, respectively. Both nrofRBs and startingRB are is configured as integer multiples of [4] RBs, and the reference point for startingRB is CRB 0 on the common resource block grid. If the UE shall assume that the initial CRB index of the CLI-RSSI resource is , otherwise . If , the UE shall assume that the bandwidth of the CLI-RSSI resource is , otherwise .] |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · `[122bis-R19-SBFD]`

**Conclusion** · `8.5` Maintenance on Enhancements of network energy savings for NR · `RAN1#122bis:8.5:002` · 후보

> - For a cell supporting on-demand SSB SCell operation and for Case #2 (i.e., Always-on SSB is periodically transmitted on the cell),
>   - If a CSI report configuration is associated with both of AO-SSB and OD-SSB,
>     - if the higher layer timeRestrictionForChannelMeasurements in CSI-ReportConfig is set to “Configured”,
>       - Which SSB to measure between the most recent AO-SSB no later than the CSI reference resource and the most recent OD-SSB no later than the CSI reference resource is up to UE implementation as long as RAN4 requirements are met.
>   - No spec change is expected

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508034](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508034.zip) · `[122bis-R19-NES]`

**Agreement** · `8.8` Maintenance on others · `RAN1#122bis:8.8:001` · 후보 · 관련 주제: CSI-RS

> Adopt the following TP to TS38.214 Section 5.2.1.2 in principle.
> | 5.2.1.2 Resource settings <unchanged parts are omitted> Each LTM CSI Resource Setting LTM-CSI-ResourceConfig contains either configuration of a ltm-CSI-SSB-ResourceSet or a ltm-NZP-CSI-RS-ResourceSet. - A ltm-CSI-SSB-ResourceSet comprises of a list of Z ≥ 1 SS/PBCH blocks indices (given by ltm-CSI-SSB-ResourceList) and a list of Z LTM-CandidateIds (given by ltm-CandidateIdList) referring to candidate cells associated with the SS/PBCH block indices. For each candidate cell, the UE determines the time domain behavior of a SS/PBCH block from ssb-Periodicity and ssb-PositionsInBurst and the frequency domain behavior of a SS/PBCH block is determined by the higher layer parameters subcarrierSpacing, ssb-Frequency. - A ltm-NZP-CSI-RS-ResourceSet comprises of a list of Z ≥ 1 NZP CSI-RS resource indices (given by ltm- CSI-RS-ResourceList) and a list of Z LTM-CandidateIds (given by ltm-CandidateIdList) referring to candidate cells associated with the NZP CSI-RS resource indices. The UE shall expect that the NZP CSI-RS resources in ltm-NZP-CSI-RS-ResourceSet are configured with the higher layer parameter repetition set to ‘off’ when LTM-ReportContent configured within the LTM-CSI-ReportConfig associated with the LTM CSI Resource Setting is set to ‘cri-RSRP’. For a report setting ltm-CSI-ReportConfig configured with ltm-ReportConfigType set to ‘periodic’ or ‘semiPersistentOnPUCCH’ or ‘semiPersistentOnPUSCH’ or ‘aperiodic’, the time domain behavior of the NZP CSI-RS resources within a ltm-NZP-CSI-RS-ResourceSet are indicated by the higher layer parameter resourceType. <unchanged parts are omitted> |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508156](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508156.zip)

**Agreement** · `8.8` Maintenance on others · `RAN1#122bis:8.8:002` · 후보 · 관련 주제: CSI-RS

> Adopt the following TP to TS38.214 Section 5.2.1.5.2 in principle
> <omitted text>
> 5.2.1.5.2	Semi-persistent CSI/Semi-persistent CSI-RS
> …
> For semi-persistent reporting on PUCCH, the PUCCH resource used for transmitting the CSI report are configured by reportConfigType or ltm-ReportConfigType. Semi-persistent reporting on PUCCH is activated by an activation command as described in clause 6.1.3.16 of [10, TS 38.321], which selects one of the semi-persistent reporting settings for use by the UE on the PUCCH. For a selected reporting setting for which the CSI-ReportConfig contains a list of sub-configurations provided by the higher layer parameter csi-ReportSubConfigToAddModList, the activation command can also select one or more sub-configurations to use by the UE as described in clause 6.1.3.X of [10, TS 38.321]. When the UE would transmit a PUCCH with HARQ-ACK information in slot n corresponding to the PDSCH carrying the activation command, the indicated semi-persistent Reporting Setting should be applied starting from the first slot that is after slot  where  is the SCS configuration for the PUCCH.
> …
> <omitted text>

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508156](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508156.zip)

**Agreement** · `8.8` Maintenance on others · `RAN1#122bis:8.8:004` · 후보

> - For the purpose of deriving the CQI for target candidate cell, the UE shall assume the following:
>   - The parameters are derived from the initial BWP configuration of the target cell.

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508156](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508156.zip)

**Agreement** · `8.8` Maintenance on others · `RAN1#122bis:8.8:007` · 후보

> Adopt the following TP#7-1 to TS38.214 Section 5.2.4a.
> | 5.2.4a CSI Reporting for LTM <omitted Text> For RACH-less LTM cell switch [23, TS 38.300], the UE shall transmit the CSI report to the candidate cell using the first PUSCH corresponding to a dynamic grant or a configured grant [6, TS 38.213]. For RACH-based LTM cell switch using a contention-free random access procedure [23, TS 38.300], the UE shall transmit the CSI report to the candidate cell using the PUSCH scheduled by the RAR UL grant or MsgA PUSCH. For RACH-based LTM cell switch using a contention-based random access procedure [23, TS 38.300], the UE shall transmit the CSI report to the candidate cell using the first PUSCH corresponding to a dynamic grant or a configured grant after the HARQ-ACK transmission corresponding to Msg4 or MsgB, or the first PUSCH scheduled by a PDCCH transmission addressed to the C-RNTI, received in response to Msg3. <omitted Text> |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508156](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508156.zip)

**Agreement** · `8.8` Maintenance on others · `RAN1#122bis:8.8:013` · 후보

> - Following TP to Section 9.1.3.1, TS38.213 is endorsed in principle.
> | 9.1.3.1 Type-2 HARQ-ACK codebook in physical uplink control channel <Unchanged parts are omitted> If a UE is provided pdsch-TimeDomainAllocationListForMultiPDSCH-DCI-1-3 for a serving cell in a set of serving cells provided by MC-DCI-SetofCells in a PUCCH group, the UE determines the according to the previous pseudo-codes with the following modifications - the first HARQ-ACK sub-codebook is associated with - unicast SPS PDSCH receptions - any unicast DCI format scheduling a single PDSCH reception on a serving cell - any unicast DCI format having associated HARQ-ACK information without scheduling a PDSCH reception - any DCI format 1_3 scheduling more than one PDSCH receptions on a serving cell for which the UE is provided nrofHARQ-BundlingGroups with value - the second HARQ-ACK sub-codebook is associated with DCI format 1_3 that - schedules PDSCH receptions on more than one serving cells from the set of serving cells, or - schedules more than one PDSCH receptions on a serving cell , from the set of serving cells, for which the UE is not provided nrofHARQ-BundlingGroups or is provided nrofHARQ-BundlingGroups with value , or - does not include a SCell dormancy indication field or the SCell dormancy indication field is reserved, indicates SCell dormancy, and schedules PDSCH receptions on one or more serving cells from the set of serving cells - in the above, and for the purpose of providing HARQ-ACK information corresponding to SCell dormancy indication by the DCI format 1_3 - the UE assumes that the UE receives one PDSCH, with first SLIV in the row of pdsch-TimeDomainAllocationListForMultiPDSCH-DCI-1-3 for DCI format 1_3, on the serving cell associated with fields in DCI format 1_3 for SCell dormancy indication, as described in Clause 10.3, and that the PDSCH provides one transport block that the UE correctly decodes, if the UE is not provided nrofHARQ-BundlingGroups for the serving cell - the UE assumes that the UE receives one or more PDSCHs associated with a TBG with smallest index, or a PDSCH reception group with smallest index, among one or more PDSCH receptions scheduled by the DCI format 1_3, on the serving cell associated with fields in DCI format 1_3 for SCell dormancy indication, as described in Clause 10.3, and that each of the one or more PDSCHs provides one transport block that the UE correctly decodes if the UE is provided nrofHARQ-BundlingGroups for the serving cell - the UE assumes incorrect decoding for transport blocks in each of the remaining PDSCH receptions scheduled by the DCI format 1_3 on the serving cell associated with fields in DCI format 1_3 for SCell dormancy indication - instead of generating HARQ-ACK information bits when harq-ACK-SpatialBundlingPUCCH is not provided, or generating HARQ-ACK information bits when harq-ACK-SpatialBundlingPUCCH is provided, for the PDSCH receptions scheduled by a DCI format 1_3, the UE generates - HARQ-ACK information bits for the PDSCH receptions scheduled by the DCI format 1_3, where is the maximum number, over the number sets of serving cells provided by MC-DCI-SetofCells in the PUCCH group, of the sum of - if nrofHARQ-BundlingGroups is not provided for a serving cell , or - if nrofHARQ-BundlingGroups is provided for the serving cell , across serving cells of a respective set of serving cells MC-DCI-SetofCells that can be scheduled PDSCH reception by a DCI format 1_3, where - is the value of maxNrofCodeWordsScheduledByDCI for serving cell if harq-ACK-SpatialBundlingPUCCH is not provided; else, ; - is the maximum number of SLIVs over all rows of the TDRA table provided by pdsch-TimeDomainAllocationListForMultiPDSCH-DCI-1-3 for serving cell ; and - is provided by nrofHARQ-BundlingGroups for serving cell - If the UE is provided with pdsch-TimeDomainAllocationListForMultiPDSCH-DCI-1-3 for the serving cell in the set s, by applying the above procedure, the UE generates - HARQ-ACK information bits if nrofHARQ-BundlingGroups is not provided for a serving cell - HARQ-ACK information bits if nrofHARQ-BundlingGroups is provided for the serving cell - where the UE assumes incorrect decoding for transport blocks in each of the PDSCH receptions scheduled by the DCI format 1_3 on the serving cell , if PDCCH monitoring occasion is before an active DL BWP change on serving cell , and the active DL BWP change is not triggered in PDCCH monitoring occasion , and the PUCCH with the HARQ-ACK information starts at or after a slot for the active DL BWP change. - If for a set of serving cells provided by MC-DCI-SetofCells, is equal to the sum of - if nrofHARQ-BundlingGroups is not provided for a serving cell , or - if nrofHARQ-BundlingGroups is provided for the serving cell , across the serving cells of the set that are scheduled PDSCH receptions by a DCI format 1_3, and , the UE generates NACK values for the last HARQ-ACK information bits corresponding to the DCI format 1_3 - The counter DAI value and the total DAI value apply separately for each HARQ-ACK sub-codebook. - The UE generates the HARQ-ACK codebook by appending the second HARQ-ACK sub-codebook to the first HARQ-ACK sub-codebook. <Unchanged parts are omitted> |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2507657](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2507657.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122bis:9.1:006` · 후보

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-0-1 | CSI report framework for UE-side inference | 1. Number of APU CPU,x pools N 2. Maximum number of APU CPU,x in each APU CPU,x pool of UE-sided inference for CSI report(s) for simultaneously in a CC 3. Maximum number of APU CPU,x in each APU CPU,x pool of UE-sided inference for CSI report(s) simultaneously across all CCs | FFS 2-35 | yes | n/a | Maximum number of APUs for UE-sided inference is unknown to the network | Per UE Per band and per BC | No n/a | No n/a | No n/a | Component 1 candidate values: {1,2} Component 2candidate values: {1…8} Component 3 candidate values: {1…32} Note: Component 2 and 3 candidate values are signalled separately for each pool [A UE that does not support this FG should not report non-zero occupied CPU,2 or CPU,3 values in any dependency FG reuses the CPU] | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508080](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508080.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122bis:9.1:008` · 후보 · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-2 | UE-side beam prediction for BM Case1 for inference | 1. Support of beam prediction with reporting of predicted beam index for BM-Case1 for inference with UE-side model 3. Maximum number of inference report(s) configured for BM-Case1 per BWP 3a. Maximum number of inference report(s) configured for BM-Case1 across all CCs 6. Support of SSB as RS type for Set B 6a. Support of CSI-RS as RS type for Set B 6b. Support of SSB as RS type for Set A 6c. Support of CSI-RS as RS type for Set A 7a: Supported maximum number of resources for Set B 7b: Supported maximum number of resources for Set A 8. Supported CSI-RS resource types for Set B 9. Supported inference report types 11. Supported BM-Case 1 sub-usecase(s): {setB-subset-of-setA, setB-different-from-setA, both}] 12. Supported maximum number of predicted beams in each reporting instance FFS: whether/how to merge this FG with other FG(s) for performance monitoring and/or data collection 13. Supported number of occupied CPU 14. Supported number of occupied APU CPU,2/CPU,3 15. Supported value of d for the relaxation of Z3 timeline 16. Supported value of d’ for the relaxation of Z’3 timeline 17. Index of the Occupied APU resource pool between CPU,2 and CPU,3 | FFS 2-35 | yes | n/a | UE-sided beam prediction for BM Case 1 for inference is not supported | Per UE Per band | No n/a | No n/a | No n/a | Component 3 candidate values: Periodic reporting: {1, 2, 3, 4} Aperiodic reporting: {1, 2, 3, 4} Semi-persistent reporting: {1, 2, 3, 4} Component 3a candidate values: {1, 2, 3, 4, 8, 10, 12, 16} Component 7a candidate values: {4, 8, 16} Component 7b candidate values: {8, 16, 32, 64} Component 8 candidate values: {Periodic CSI-RS, Semi-persistent CSI-RS, Aperiodic CSI-RS} Component 9 candidate values: {Periodic CSI report, Aperiodic CSI report, semi-persistent CSI report} Component 11 candidate values: {setB-subset-of-setA, setB-different-from-setA, both} Component 12 candidate values: {1, 2, 3, 4} Component 13 candidate values: {0, 1, 2, …, 8} Component 14 candidate values: {0, 1, 2, …, 8} Note: The values of component 13 and 14 are not allowed to be 0 simultaneously Component 15 candidate values: FFS Component 16 candidate values: FFS Component 17 candidate values: {1, 2} representing the first APU pool (i.e., CPU,2) and the second APU pool (i.e., CPU,3), respectively Note: “CPU” corresponds to “CPU,1” in TS 38.214, and “APU” corresponds to “CPU,x” in TS 38.214, x = 2, 3 FFS: candidate values for components | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508080](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508080.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122bis:9.1:010` · 후보 · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-4 | UE-side beam prediction for BM Case2 for inference | 1. Support of beam prediction with reporting of predicted beam index for BM-Case2 for inference with UE-side model 3. Maximum number of inference report(s) configured for BM-Case2 per BWP 3a. Maximum number of inference report(s) configured for BM-Case2 across all CCs 6. Support of SSB as RS type for Set B 6a. Support of CSI-RS as RS type for Set B 6b. Support of SSB as RS type for Set A 6c. Support of CSI-RS as RS type for Set A 7a: Supported maximum number of resources for Set B 7b: Supported maximum number of resources for Set A 8. Supported CSI-RS resource types for Set B 9. Supported inference report types 11. Supported maximum number of predicted beams in each predicted time instance 12. Supported maximum number of predicted time instances 13. Supported maximum total number of reported predicted beams for predicted time instances in one report 14. Supported combinations of supported value(s) of valid time duration for each predicted time instance and number of predicted beams for each value of valid time duration 15. Supported value(s) of time gap between predicted time instances and between reference time to the first future time instance 21. supported number of occupied CPU 22. supported number of occupied APU CPU,2/CPU,3 23. supported value of d for the relaxation of Z3 timeline 24. supported value of d’ for the relaxation of Z’3 timeline 25. Index of the Occupied APU resource pool between CPU,2 and CPU,3 | FFS 2-35 | yes | n/a | UE-side beam prediction for BM-Case2 for inference is not supported | Per UE Per band | No n/a | No n/a | No n/a | Component 3 candidate values: Periodic reporting: {1, 2, 3, 4} Aperiodic reporting: {1, 2, 3, 4} Semi-persistent reporting: {1, 2, 3, 4} Component 3a candidate values: {1, 2, 3, 4, 8, 10, 12, 16} Component 7a candidate values: {4, 8, 16, 32, 64} Component 7b candidate values: {4, 8, 16, 32, 64} Component 8 candidate values: {Periodic CSI-RS, Semi-persistent CSI-RS} Component 9 candidate values: {Periodic CSI report, Aperiodic CSI report, semi-persistent CSI report}FFS: candidate values for components Component 11 candidate values: {1, 2, 3, 4} Component 12 candidate values: {1, 2, 4, 8} Component 13 candidate values: {1, 2, 4, 6, 8, 12, 16, 32} Component 15 candidate values: {10ms, 20ms, 40ms, 80ms, 160ms} Component 21 candidate values: {0, 1, 2, … 8} Component 22 candidate values: {0, 1, 2, … 8} Note: The values of component 21 and 22 are not allowed to be 0 simultaneously. Component 23 candidate values: FFS Component 24 candidate values: FFS Component 25 candidate values: {1, 2} representing the first APU pool (i.e., CPU,2) and the second APU pool (i.e., CPU,3), respectively Note: “CPU” corresponds to “CPU,1” in TS 38.214, and “APU” corresponds to “CPU,x” in TS 38.214, x = 2, 3 Note: UE should not report non-zero value for Component 22 if FG 58-0-1 is not signalled | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508080](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508080.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122bis:9.1:018` · 후보

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-0-1 | CSI report framework for UE-side inference | 1. Number of CPU,x pools N 2. Maximum number of CPU,x in each CPU,x pool of UE-sided inference for CSI report(s) for simultaneously in a CC 3. Maximum number of CPU,x in each CPU,x pool of UE-sided inference for CSI report(s) simultaneously across all CCs | 2-35 | yes | n/a | Maximum number of APU CPU,x for UE-sided inference is unknown to the network | Per band and per BC | n/a | n/a | n/a | Component 1 candidate values: {1,2} Component 2candidate values: {1…8} Component 3 candidate values: {1…32} Note: Component 2 and 3 candidate values are signalled separately for each pool A UE that does not support this FG should not report non-zero occupied CPU,2 or CPU,3 values in any dependency FG | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508080](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508080.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122bis:9.1:022` · 후보 · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-2 | UE-side beam prediction for BM Case1 for inference | 1. Support of beam prediction with reporting of predicted beam index for BM-Case1 for inference with UE-side model 3. Maximum number of inference report(s) configured for BM-Case1 per BWP 3a. Maximum number of inference report(s) configured for BM-Case1 across all CCs 6. Support of SSB as RS type for Set B 6a. Support of CSI-RS as RS type for Set B 6b. Support of SSB as RS type for Set A 6c. Support of CSI-RS as RS type for Set A 7a: Supported maximum number of resources for Set B 7b: Supported maximum number of resources for Set A 8. Supported CSI-RS resource types for Set B 9. Supported inference report types 11. Supported BM-Case 1 sub-usecase(s) 12. Supported maximum number of predicted beams in each reporting instance 13. Supported number of occupied CPU 14. Supported number of occupied CPU,2/CPU,3 15. Supported value of d for the relaxation of Z3 timeline, where i is the index of SCS, i=1,2,3,4,5,6 corresponding to 15,30,60,120,480,960 kHz SCS 16. Supported value of d’ for the relaxation of Z’3 timeline, where i is the index of SCS, i=1,2,3,4,5,6 corresponding to 15,30,60,120,480,960 kHz SCS 17. Occupied resource pool between CPU,2 and CPU,3 | 2-35 | yes | n/a | UE-sided beam prediction for BM Case 1 for inference is not supported | Per band | n/a | n/a | n/a | Component 3 candidate values: Periodic reporting: {1, 2, 3, 4} Aperiodic reporting: {1, 2, 3, 4} Semi-persistent reporting: {1, 2, 3, 4} Component 3a candidate values: {1, 2, 3, 4, 8, 10, 12, 16} Component 7a candidate values: {4, 8, 16} Component 7b candidate values: {8, 16, 32, 64} Component 8 candidate values: {Periodic CSI-RS, Semi-persistent CSI-RS, Aperiodic CSI-RS} Component 9 candidate values: {Periodic CSI report, Aperiodic CSI report, semi-persistent CSI report} Component 11 candidate values: {setB-subset-of-setA, setB-different-from-setA, both} Component 12 candidate values: {1, 2, 3, 4} Component 13 candidate values: {0, 1, 2, …, 8} Component 14 candidate values: {0, 1, 2, …, 8} Note: The values of component 13 and 14 are not allowed to be 0 simultaneously Component 15 candidate values: d1 is FFS d2 is FFS d3 is FFS d4 is FFS d5 is FFS d6 is FFS Component 16 candidate values: d'1 is FFS d’2 is FFS d’3 is FFS d’4 is FFS d’5 is FFS d’6 is FFS Component 17 candidate values: {1, 2} representing the first APU pool (i.e., CPU,2) and the second APU pool (i.e., CPU,3), respectively Note: “CPU” corresponds to “CPU,1” in TS 38.214, and “APU” corresponds to “CPU,x” in TS 38.214, x = 2, 3 | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508080](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508080.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122bis:9.1:023` · 후보 · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-4 | UE-side beam prediction for BM Case2 for inference | 1. Support of beam prediction with reporting of predicted beam index for BM-Case2 for inference with UE-side model 3. Maximum number of inference report(s) configured for BM-Case2 per BWP 3a. Maximum number of inference report(s) configured for BM-Case2 across all CCs 6. Support of SSB as RS type for Set B 6a. Support of CSI-RS as RS type for Set B 6b. Support of SSB as RS type for Set A 6c. Support of CSI-RS as RS type for Set A 7a: Supported maximum number of resources for Set B 7b: Supported maximum number of resources for Set A 8. Supported CSI-RS resource types for Set B 9. Supported inference report types 11. Supported maximum number of predicted beams in each predicted time instance 12. Supported maximum number of predicted time instances 13. Supported maximum total number of reported predicted beams for predicted time instances in one report 15. Supported value(s) of time gap between predicted time instances and between reference time to the first future time instance 21. supported number of occupied CPU 22. supported number of occupied CPU,2/CPU,3 23. supported value of d for the relaxation of Z3 timeline, where i is the index of SCS, i=1,2,3,4,5,6 corresponding to 15,30,60,120,480,960 kHz SCS 24. supported value of d’ for the relaxation of Z’3 timeline, where i is the index of SCS, i=1,2,3,4,5,6 corresponding to 15,30,60,120,480,960 kHz SCS 25. Occupied resource pool between CPU,2 and CPU,3 | 2-35 | yes | n/a | UE-side beam prediction for BM-Case2 for inference is not supported | Per band | n/a | n/a | n/a | Component 3 candidate values: Periodic reporting: {1, 2, 3, 4} Aperiodic reporting: {1, 2, 3, 4} Semi-persistent reporting: {1, 2, 3, 4} Component 3a candidate values: {1, 2, 3, 4, 8, 10, 12, 16} Component 7a candidate values: {4, 8, 16, 32, 64} Component 7b candidate values: {4, 8, 16, 32, 64} Component 8 candidate values: {Periodic CSI-RS, Semi-persistent CSI-RS} Component 9 candidate values: {Periodic CSI report, Aperiodic CSI report, semi-persistent CSI report} Component 11 candidate values: {1, 2, 3, 4} Component 12 candidate values: {1, 2, 4, 8} Component 13 candidate values: {1, 2, 4, 6, 8, 12, 16, 32} Component 15 candidate values: {10ms, 20ms, 40ms, 80ms, 160ms} Component 21 candidate values: {0, 1, 2, … 8} Component 22 candidate values: {0, 1, 2, … 8} Note: The values of component 21 and 22 are not allowed to be 0 simultaneously. Component 23 candidate values: d1 is FFS d2 is FFS d3 is FFS d4 is FFS d5 is FFS d6 is FFS Component 24 candidate values: d'1 is FFS d’2 is FFS d’3 is FFS d’4 is FFS d’5 is FFS d’6 is FFS Component 25 candidate values: {1, 2} representing the first APU pool (i.e., CPU,2) and the second APU pool (i.e., CPU,3), respectively Note: “CPU” corresponds to “CPU,1” in TS 38.214, and “APU” corresponds to “CPU,x” in TS 38.214, x = 2, 3 Note: UE should not report non-zero value for Component 22 if FG 58-0-1 is not signalled | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508080](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508080.zip)

**Agreement** · `9.3` UE features for evolution of NR duplex operation: SBFD · `RAN1#122bis:9.3:008` · 후보 · 관련 주제: CSI-RS

> Regarding “FFS: details of counting” in FG 60-1, adopt Alt1.1
> - Alt-1: Update candidate values for Component 11
>   - Alt-1.1: Component 11 candidate values: {“with factor-of-two relaxation for CSI timeline”, “with factor-of-two relaxation for active CSI-RS resource and port counting”, “no relaxation”}

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2507966](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2507966.zip)

**Agreement** · `9.6` UE features for NR mobility enhancements Phase 4 · `RAN1#122bis:9.6:002` · 후보 · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 63. NR_Mob_Ph4 | 63-6 | Intra-frequency CSI-RS and CSI-IM measurement and CSI reporting for cell indicated in CSC MAC CE after reception of LTM CSC MAC CE based on periodic CSI-RS and CSI-IM resource | 1. Support of CSI-RS and CSI-IM measurement and CSI reporting after reception of LTM CSC MAC CE based on periodic CSI-RS(s) and CSI-IM resources of cell indicated in CSC MAC CE 3. Maximum number of CSI-RS resources for CMR associated with CSI report configuration for a candidate cell 4. Max number of ports of CSI-RS resource(s) associated with a CSI report configuration for CSI reporting for a candidate cell 5. Maximum number of ports in one NZP CSI-RS resource 6. Max rank for CSI reporting for a candidate cell 7. Maximum number of CSI-IM resources for interference measurement associated with CSI report configuration for a candidate cell | FFS RAN2 FG for LTM in Rel-18 | Yes | No | Intra-frequency Periodic CSI-RS and CSI-IM measurement and CSI reporting for cell indicated in CSC MAC CE after reception of LTM CSC MAC CE is not supported | Per band | n/a | n/a | n/a | Component 3 candidate values: {1,2,3,4,5,6,7,8} Component 4 candidate values: {1,2,4,8,12,16,24,32,48,64,128} Component 5 candidate values: {1, 2, 4, 8, 12, 16, 24, 32} Component 6 candidate values: {1,2,3,4,5,6,7,8} Component 7 candidate values: {1,2,3,4,5,6,7,8} | Optional with capability signaling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508083](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508083.zip)

**Agreement** · `9.6` UE features for NR mobility enhancements Phase 4 · `RAN1#122bis:9.6:003` · 후보 · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 63. NR_Mob_Ph4 | 63-6a | Intra-frequency CSI-RS and CSI-IM measurement and CSI reporting for cell indicated in CSC MAC CE after reception of LTM CSC MAC CE based on semi-persistent CSI-RS and CSI-IM resource | 1. Support of CSI-RS and CSI-IM measurement and CSI reporting after reception of LTM CSC MAC CE based on periodic semi-persistent CSI-RS(s) and CSI-IM resources of cell indicated in CSC MAC CE 3. Maximum number of CSI-RS resources for CMR associated with CSI report configuration for a candidate cell 4. Max number of ports of CSI-RS resource(s) associated with a CSI report configuration for CSI reporting for a candidate cell 5. Maximum number of ports in one NZP CSI-RS resource 6. Max rank for CSI reporting for a candidate cell 7. Maximum number of CSI-IM resources for interference measurement associated with CSI report configuration for a candidate cell | FFS 63-6 | Yes | No | Intra-frequency Semi-persistent CSI-RS and CSI-IM measurement and CSI reporting for cell indicated in CSC MAC CE after reception of LTM CSC MAC CE is not supported | Per band | n/a | n/a | n/a | Component 3 candidate values: {1,2,3,4,5,6,7,8} Component 4 candidate values: {1,2,4,8,12,16,24,32,48,64,128} Component 5 candidate values: {1, 2, 4, 8, 12, 16, 24, 32} Component 6 candidate values: {1,2,3,4,5,6,7,8} Component 7 candidate values: {1,2,3,4,5,6,7,8} | Optional with capability signaling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508083](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508083.zip)

**Agreement** · `9.6` UE features for NR mobility enhancements Phase 4 · `RAN1#122bis:9.6:004` · 후보 · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 63. NR_Mob_Ph4 | 63-7 | Intra-frequency CSI-RS and CSI-IM measurement for candidate cell before reception of LTM CSC MAC CE based on periodic CSI-RS(s) and CSI-IM resources of candidate cells | 1. Support of intra-frequency CSI-RS and CSI-IM measurement before reception of CSC MAC CE based on periodic CSI-RS(s) and CSI-IM resources of candidate cells 2. Maximum number of RRC configured candidate cells for CSI measurement before LTM CSC MAC CE 3. Maximum number of RRC configured CSI-RS resources across candidate cells RRC configured for CSI measurement before LTM CSC MAC CE 4. Max number of ports of CSI-RS resource(s) associated with a CSI report configuration for CSI reporting for a candidate cell 5. Maximum number of ports in one NZP CSI-RS resource associated with a CSI report configuration for CSI reporting for a candidate cell 6. Maximum number of RRC configured CSI-IM resources across candidate cells RRC configured for CSI measurement before LTM CSC MAC CE | 63-6 | Yes | No | Intra-frequency periodic CSI-RS and CSI-IM measurement for candidate cell before reception of LTM CSC MAC CE is not supported | Per BC | n/a | n/a | n/a | Component 2 candidate values: {1,2,3,4,5,6,7,8} Component 3 candidate values: {1,2,...64} Component 4 candidate values: {1,2,4,8,12,16,24,32,48,64,128} Component 5 candidate values: {1,2,4,8,12,16,24,32} Component 6 candidate values: {1,2,…64} | Optional with capability signaling |
> | 63. NR_Mob_Ph4 | 63-7c | Inter-frequency CSI-RS and CSI-IM measurement for candidate cell before reception of LTM CSC MAC CE based on periodic CSI-RS(s) and CSI-IM resources of candidate cells | 1. Support of inter-frequency CSI-RS and CSI-IM measurement before reception of CSC MAC CE based on periodic CSI-RS(s) and CSI-IM resources of candidate cells 2. Maximum number of RRC configured candidate cells for CSI measurement before LTM CSC MAC CE 3. Maximum number of RRC configured CSI-RS resources across candidate cells RRC configured for CSI measurement before LTM CSC MAC CE 4. Max number of ports of CSI-RS resource(s) associated with a CSI report configuration for CSI reporting for a candidate cell 5. Maximum number of ports in one NZP CSI-RS resource associated with a CSI report configuration for CSI reporting for a candidate cell 6. Maximum number of RRC configured CSI-IM resources across candidate cells RRC configured for CSI measurement before LTM CSC MAC CE | 63-6 | Yes | No | Inter-frequency periodic CSI-RS and CSI-IM measurement for candidate cell before reception of LTM CSC MAC CE is not supported | Per BC | n/a | n/a | n/a | Component 2 candidate values: {1,2,3,4,5,6,7,8} Component 3 candidate values: {1,2,...64} Component 4 candidate values: {1,2,4,8,12,16,24,32,48,64,128} Component 5 candidate values: {1,2,4,8,12,16,24,32} Component 6 candidate values: {1,2,…64} | Optional with capability signaling |
> | 63. NR_Mob_Ph4 | 63-7a | Intra-frequency CSI-RS and CSI-IM measurement for candidate cell before reception of LTM CSC MAC CE based on semi-persistent CSI-RS(s) and CSI-IM resources of candidate cells | 1. Support of intra-frequency CSI-RS and CSI-IM measurement before reception of CSC MAC CE based on semi-persistent CSI-RS(s) and CSI-IM resources of candidate cells 2. Maximum number of RRC configured candidate cells for CSI measurement before LTM CSC MAC CE 3. Maximum number of RRC configured CSI-RS resources across candidate cells RRC configured for CSI measurement before LTM CSC MAC CE 4. Max number of ports of CSI-RS resource(s) associated with a CSI report configuration for CSI reporting for a candidate cell 5. Maximum number of ports in one NZP CSI-RS resource associated with a CSI report configuration for CSI reporting for a candidate cell 6. Maximum number of RRC configured CSI-IM resources across candidate cells RRC configured for CSI measurement before LTM CSC MAC CE | 63-6a | Yes | No | Intra-frequency semi-persistent CSI-RS and CSI-IM measurement for candidate cell before reception of LTM CSC MAC CE is not supported | Per BC | n/a | n/a | n/a | Component 2 candidate values: {1,2,3,4,5,6,7,8} Component 3 candidate values: {1,2,...64} Component 4 candidate values: {1,2,4,8,12,16,24,32,48,64,128} Component 5 candidate values: {1,2,4,8,12,16,24,32} Component 6 candidate values: {1,2,...64} | Optional with capability signaling |
> | 63. NR_Mob_Ph4 | 63-7d | Inter-frequency CSI-RS and CSI-IM measurement for candidate cell before reception of LTM CSC MAC CE based on semi-persistent CSI-RS(s) and CSI-IM resources of candidate cells | 1.. Support of inter-frequency CSI-RS and CSI-IM measurement before reception of CSC MAC CE based on semi-persistent CSI-RS(s) and CSI-IM resources of candidate cells 2. Maximum number of RRC configured candidate cells for CSI measurement before LTM CSC MAC CE 3. Maximum number of RRC configured CSI-RS resources across candidate cells RRC configured for CSI measurement before LTM CSC MAC CE 4. Max number of ports of CSI-RS resource(s) associated with a CSI report configuration for CSI reporting for a candidate cell 5. Maximum number of ports in one NZP CSI-RS resource associated with a CSI report configuration for CSI reporting for a candidate cell 6. Maximum number of RRC configured CSI-IM resources across candidate cells RRC configured for CSI measurement before LTM CSC MAC CE | 63-6a | Yes | No | Inter-frequency semi-persistent CSI-RS and CSI-IM measurement for candidate cell before reception of LTM CSC MAC CE is not supported | Per BC | n/a | n/a | n/a | Component 2 candidate values: {1,2,3,4,5,6,7,8} Component 3 candidate values: {1,2,...64} Component 4 candidate values: {1,2,4,8,12,16,24,32,48,64,128} Component 5 candidate values: {1,2,4,8,12,16,24,32} Component 6 candidate values: {1,2,...64} | Optional with capability signaling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508083](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508083.zip)

**Agreement** · `9.6` UE features for NR mobility enhancements Phase 4 · `RAN1#122bis:9.6:005` · 후보 · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 63. NR_Mob_Ph4 | 63-10 | Intra-frequency CSI-RS-RS measurement and CSI reporting without CSI-IM reception | 1. Support of CSI-RS measurement and CSI reporting for candidate cells without CSI-IM resource configuration | 63-6 or 63-6a or 63-7 or 63-7a or 63-11 | Yes | No | Intra-frequency CSI-RS-RS measurement and CSI reporting without CSI-IM reception is not supported | Per band | n/a | n/a | n/a |  | Optional with capability signaling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508083](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508083.zip)

### RAN1#122 — 25건

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#122:8.1:002` · 후보

> Adopt the following TP in section 5.2.1.6, TS 38.214.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506557](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506557.zip) · `[122-R19-AI/ML]`

**Agreement** · `8.3.1` SBFD TX/RX/measurement procedures · `RAN1#122:8.3.1:003` · 후보 · 관련 주제: CSI-RS

> Adopt the following TP in principle to Section 5.2.1.4, TS 38.214.
> | 5.2.1.4 Reporting configurations *** Unchanged parts are omitted *** The reportFreqConfiguration contained in a CSI-ReportConfig indicates the frequency granularity of the CSI Report. A CSI Reporting Setting configuration defines a CSI reporting band as a subset of subbands of the bandwidth part, where the reportFreqConfiguration indicates: - the csi-ReportingBand as a contiguous or non-contiguous subset of subbands in the bandwidth part for which CSI shall be reported. - A UE is not expected to be configured with csi-ReportingBand which contains a subband where a CSI-RS resource linked to the CSI Report setting has the frequency density of each CSI-RS port per PRB in the subband less than the configured density of the CSI-RS resource. - If a CSI-IM resource is linked to the CSI Report Setting, a UE is not expected to be configured with csi-ReportingBand which contains a subband where not all PRBs in the subband have the CSI-IM REs present. - For a CSI-ReportConfig with the higher layer parameter symbolType set to ‘sbfd’, UE can be configured with a CSI subband if at least one PRB in the CSI subband is within PRBs that are both in the active DL BWP and in the DL sub-band(s). *** Unchanged parts are omitted *** |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip)

**Agreement** · `8.5.1` On-demand SSB SCell operation · `RAN1#122:8.5.1:002` · 후보

> Adopt the following TP for TS 38.214 Clause 5.2.1.4
> Reason for change: To clarify that CSI report for an SCell configured with od-ssb-config cannot be configured with eventType
> Summary of change: Add description that CSI report for an SCell configured with od-ssb-config cannot be configured with eventType
> Consequence if not approved: Whether or not CSI report for an SCell configured with od-ssb-config can be configured with eventType is unclear
> | 5.2.1.4 Reporting configurations <omitted text> For a UE configured with od-ssb-config on a SCell and for CSI report with CSI-ReportConfig with higher layer parameter reportQuantity set to 'ssb-Index-RSRP', 'ssb-Index-SINR', 'ssb-Index-RSRP- Index', or 'ssb-Index-SINR- Index ' - if the UE is not provided absoluteFrequencySSB for the SCell, the CSI report configuration is associated with the SS/PBCH block configured by od-ssb-config and the UE reports SSBRI based on SSB-index corresponding to the currently transmitted SS/PBCH block. - if the UE is provided absoluteFrequencySSB for the SCell, the CSI report configuration is associated with both the SS/PBCH block configured by od-ssb-config and the SS/PBCH block provided by absoluteFrequencySSB and the UE reports SSBRI based on SSB-index corresponding to the currently transmitted SS/PBCH block(s) that may be the one configured by od-ssb-config and/or provided by absoluteFrequencySSB based on measurement requirements defined in [11, TS 38.133]. - The UE reports SSBRI based on SSB-index corresponding to the currently transmitted SS/PBCH block, where the SSBRI k (k ≥ 0) corresponds to the configured (k+1)-th entry of the associated csi-SSB-ResourceList in the corresponding CSI-SSB-ResourceSet. The reportConfigType of CSI reporting configuration based on SS/PBCH block configured with od-ssb-config may be aperiodic or semi-persistent. |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506493](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506493.zip)

**Agreement** · `8.5.1` On-demand SSB SCell operation · `RAN1#122:8.5.1:005` · 후보 · 관련 주제: CSI-RS

> Adopt the following TP for TS 38.214 Clause 4.1
> Reason for change
> - The SSS EPRE for OD-SSB in Case #1 is undefined
> - The CSI-RS EPRE for CSI-RS that is QCLed to the OD-SSB in Case #1 is undefined
> Summary of change
> - The downlink SS/PBCH SSS EPRE can be derived from the SS/PBCH downlink transmit power given by the parameter od-ss-PBCH-BlockPower provided in od-ssb-config for SS/PBCH block transmitted according to Clause 4.4 of [6, TS 38.213].
> - The downlink CSI-RS EPRE can be derived from the SS/PBCH block downlink transmit power given by the parameter od-ss-PBCH-BlockPower provided in od-ssb-config for SS/PBCH block transmitted according to Clause 4.4 of [6, TS 38.213]
> Consequence if not approved:
> - Undefined EPRE of SSS and CSI-RS for OD-SSB in Case #1
> | 4.1 Power allocation for downlink The gNB determines the downlink transmit EPRE. For the purpose of SS-RSRP, SS-RSRQ and SS-SINR measurements, the UE may assume downlink EPRE is constant across the bandwidth. For the purpose of SS-RSRP, SS-RSRQ and SS-SINR measurements, the UE may assume downlink EPRE is constant over SSS carried in different SS/PBCH blocks. For the purpose of SS-RSRP, SS-RSRQ and SS-SINR measurements, the UE may assume that the ratio of SSS EPRE to PBCH DM-RS EPRE is 0 dB. For the purpose of CSI-RSRP, CSI-RSRQ and CSI-SINR measurements, the UE may assume downlink EPRE of a port of CSI-RS resource configuration is constant across the configured downlink bandwidth and constant across all configured OFDM symbols. The downlink SS/PBCH SSS EPRE can be derived from the SS/PBCH downlink transmit power given by the parameter ss-PBCH-BlockPower provided by higher layers or od-ss-PBCH-BlockPower provided in od-ssb-config for SS/PBCH block transmitted according to Clause 4.4 of [6, TS 38.213]. The downlink SSS transmit power is defined as the linear average over the power contributions (in [W]) of all resource elements that carry the SSS within the operating system bandwidth. The downlink CSI-RS EPRE can be derived from the SS/PBCH block downlink transmit power given by the parameter ss-PBCH-BlockPower or od-ss-PBCH-BlockPower provided in od-ssb-config for SS/PBCH block transmitted according to Clause 4.4 of [6, TS 38.213] and CSI-RS power offset given by the parameter powerControlOffsetSS provided by higher layers if the SS/PBCH block is associated with serving cell PCI, or derived from ss-PBCH-BlockPower-r17 in SSB-MTC-AdditionalPCI-r17 and powerControlOffsetSS provided by higher layers if the SS/PBCH block is associated with additional PCI different from serving cell PCI, where the CSI-RS is QCLed with the SS/PBCH block. The downlink reference-signal transmit power is defined as the linear average over the power contributions (in [W]) of the resource elements that carry the configured CSI-RS within the operating system bandwidth. |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506493](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506493.zip)

**Agreement** · `8.9.1` Measurements related enhancements for LTM · `RAN1#122:8.9.1:001` · 후보 · 관련 주제: CSI-RS

> Following TP to TS38.214 Section 5.2.4a is endorsed in principle.
> - Reason for change: Current texts in the referred paragraph in TS 38.214 create some ambiguity. First, “corresponding NZP CSI-RS resources” is unclear. It presents unclear meaning of what the NZP CSI-RS resources are corresponding to. In our views, we should instead describe that NZP CSI-RS resources are corresponding to a [ltm-eCSI-ReportConfig]. Second, “start” is redundant here and never exists in the agreement.
> - Summary of change: Describe UE measures NZP CSI-RS resources corresponding to a [ltm-eCSI-ReportConfig] before receiving LTM CSC MAC CE. Remove the redundant “start” wording.
> - Consequences if not approved: Unclear UE behavior on LTM RS measurement before receiving LTM CSC MAC CE.
> | Text Proposal 1 for TS 38.214 Clause 5.2.4a < Unchanged parts are omitted > If a valid CSI is not available, the UE shall transmit a CSI report which contains a CQI corresponding to the lowest CQI index. [Depending on the UE capability] the UE may start measureing corresponding NZP CSI-RS resources corresponding to a [ltm-eCSI-ReportConfig] before receiving the LTM Cell Switch Command MAC CE [10, TS 38.321]. |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip)

**Agreement** · `8.9.1` Measurements related enhancements for LTM · `RAN1#122:8.9.1:003` · 후보 · 관련 주제: CSI-RS

> Following TP to TS38.214 Section 5.2.4a is endorsed in principle.
> | Reason for change: | For LTM CSI reporting, both channel measurements and interference measurements would be done by UE. For interference measurement, UE could either measure NZP CSI-RS or CSI-IM depending on the configuration. In TS 38.214, the measurement on CSI-IM resources is missing. |
> |  |  |
> | Summary of change: | For LTM CSI reporting, UE should measure CSI-IM resources if configured. |
> |  |  |
> | Consequences if not approved: | UE would not measure CSI-IM resources for interference measurement. |
> -------------------- Start of text proposal to TS 38.214 v19.0.0 ---------------------------------------
> 5.2.4a CSI Reporting for LTM
> <<< UNCHANGED PART OMITTED >>>
> After a UE receives an LTM Cell Switch Command MAC CE [10, TS 38.321] providing a candidate cell (given by Target Configuration ID field), and a [ltm-eCSI-ReportConfig] is configured for the candidate cell, the UE can measure corresponding NZP CSI-RS resources and CSI-IM resources if configured, and shall transmit a CSI report to the candidate cell.
> <<< UNCHANGED PART OMITTED >>>
> ---------------------- End of text proposal to TS 38.214 v19.0.0 ---------------------------------------

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip)

**Agreement** · `8.9.1` Measurements related enhancements for LTM · `RAN1#122:8.9.1:004` · 후보 · 관련 주제: CSI-RS

> Following TP to TS38.214 Section 5.2.4a is endorsed in principle.
> | 5.2.4a CSI Reporting for LTM <omitted text> A UE configured with LTM-Config can be provided configurations for CSI acquisition, by up to one Reporting Setting, [ltm-eCSI-ReportConfig], for a candidate cell. Each Reporting Setting [ltm-eCSI-ReportConfig] is associated with either one or two Resource Settings - When one Resource Setting (given by higher layer parameter ltm-ResourcesForChannelMeasurement) is configured, it provides a list of NZP CSI-RS resources for both channel and interference measurements. The UE is not expected to be configured with more than 128 NZP CSI-RS ports in the CSI-RS resource set contained within the Resource Setting. - When two Resource Settings are configured, the first Resource Setting (given by higher layer parameter ltm-ResourcesForChannelMeasurement) provides a list of NZP CSI-RS resources for channel measurement, and the second Resource Setting (given by higher layer parameter [ltm-ResourceForInterferenceMeasurements]), provides a list of [CSI-IM resources] for interference measurement. The UE shall expect the following configuration provided [ltm-eCSI-ReportConfig]: - For the frequency granularity of the CSI report, the CQI format indicator is Wideband CQI. - For the frequency granularity of the CSI report, the PMI format indicator is Wideband PMI. - The codebook type is typeI-SinglePanel. - The reportQuantity is set to ‘cri-RI-PMI-CQI’. <omitted text> |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip)

**Agreement** · `8.9.1` Measurements related enhancements for LTM · `RAN1#122:8.9.1:005` · 후보

> - Introduce a new RRC IE for LTM codebook configuration
> CodebookConfig-LTM-r19 ::=         CHOICE {
> twoToThirtyTwoPorts                 CodebookConfig,
> moreThanThirtyTwoPorts           CodebookConfig-r19
> ...
> }
> - Add note in RRC parameter list to inform RAN2 to add ‘typeI and single panel’ restriciton.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip)

**Agreement** · `8.9.1` Measurements related enhancements for LTM · `RAN1#122:8.9.1:006` · 후보 · 관련 주제: CSI-RS

> - Add the optional field ‘repetition’ to LTM-NZP-CSI-RS-ResourceSet
>   - When LTM-NZP-CSI-RS-ResourceSet is used for beam-management, ‘repetition’ should be set to ‘off’ and when it is used for early CSI acquisition, the field should be absent.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip)

**Agreement** · `8.9.1` Measurements related enhancements for LTM · `RAN1#122:8.9.1:007` · 후보 · 관련 주제: CSI-RS

> - Adapt LTM-CSI-ReportConfig to include cqi-Table for CQI reporting
> - Clarify in RAN1 specification that the LTM-CandidateId-r18 in ltm-CandidateIdList-r19 of LTM-NZP-CSI-RS-ResourceSet-r19 should be same as that of LTM-Candidate-r18 under which CSI report configuration for CSI acquisition is configured.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip)

**Agreement** · `8.9.1` Measurements related enhancements for LTM · `RAN1#122:8.9.1:008` · 후보 · 관련 주제: CSI-RS

> Semi-persistent CSI-IM measurement resource is supported for the CSI acquisition for candidate cells.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip)

**Agreement** · `8.9.1` Measurements related enhancements for LTM · `RAN1#122:8.9.1:009` · 후보 · 관련 주제: CSI-RS

> For a UE capable of CSI acquisition of performing early CSI measurement operations before and after LTM Cell Switch Command MAC CE:
> - For candidate cell(s), a periodic CSI-RS resource and port are counted as ‘active’ in a duration starting when the periodic CSI-RS resource is configured by higher layer signaling until the reception of the LTM cell switch command MAC CE or a RRC reconfiguration message, which comes first.
> - For candidate cell(s), a SP CSI-RS resource and port are counted as ‘active’ in a duration starting from the end of when the activation command is applied until the reception of the LTM cell switch command MAC CE or a deactivation command MAC CE, which comes first.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip)

**Agreement** · `8.9.1` Measurements related enhancements for LTM · `RAN1#122:8.9.1:010` · 후보 · 관련 주제: CSI-RS

> For a UE capable of CSI acquisition of performing early CSI measurement operations only after LTM Cell Switch Command MAC CE:
> - For candidate cell(s), periodic and SP-CSI-RS resources and ports configured for early CSI acquisition in an LTM Candidate cell are not counted as active before reception of LTM Cell Switch Command MAC CE.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122:9.1:001` · 후보

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-0-1 | CSI report framework for UE-side inference | 1. Number of APU pools N 12. Maximum number of APUs in each APU pool for all types of UE-sided inference for CSI report(s) for simultaneously in a CC 23. Maximum number of APUs in each APU pool for all types of UE-sided inference for CSI report(s) simultaneously across all CCs | FFS | yes | n/a | Maximum number of APUs for UE-sided inference is unknown to the network | FFS Per UE | FFS N/A | FFS N/A | FFS N/A | Component 1 candidate values: {1,2} Component 12 candidate values: FFS{1…8} Component 23 candidate values: FFS{1…32} Note: Component 2 and 3 candidate values are signalled separately for each pool [A UE that does not support this FG reuses the CPU] | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506605](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506605.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122:9.1:003` · 후보 · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-2 | UE-side beam prediction for BM Case1 [for inference] | 1. Support of beam prediction with reporting of predicted beam index for BM-Case1 [for inference] with UE-side model 3. Maximum number of inference report(s) configured for BM-Case1 per BWP 3a. Maximum number of inference report(s) configured for BM-Case1 across all CCs [4. Maximum number of inference report(s) activated for BM-Case1 per BWP] [4a. Maximum number of inference report(s) activated for BM-Case1 across all CCs] [5. Maximum number of inference report(s) triggered for BM-Case1 per BWP] [5a. Maximum number of inference report(s) triggered for BM-Case1 across all CCs] 6. Support of SSB as RS type for Set B 6a. Support of CSI-RS as RS type for Set B 6b. Support of SSB as RS type for Set A 6c. Support of CSI-RS as RS type for Set A [7. Supported combinations of the number of resources for Set B and the number of resources for Set A] [7a: Supported maximum number of resources for Set B] [7b: Supported maximum number of resources for Set A] [8. Supported CSI-RS resource types: Periodic CSI-RS, Semi-persistent CSI-RS, Aperiodic CSI-RS] [9. Supported inference report types: Periodic CSI report, Aperiodic CSI report, semi-persistent CSI report] [10. Supported options for performance monitoring for beam case 1 with UE side model] [11. Supported BM-Case 1 sub-usecase(s): {setB-subset-of-setA, setB-different-from-setA, both} 12. Supported maximum number of predicted beams in each reporting instanceFFS: whether/how to merge this FG with other FG(s) for performance monitoring and/or data collection 13. Supported number of occupied CPU 14. Supported number of occupied APU 15. Supported value of d for the relaxation of Z3 timeline 16. Supported value of d’ for the relaxation of Z’3 timeline 17. Index of the occupied APU pool | FFS | yes | n/a | UE-sided beam prediction for BM Case 1 [for inference] is not supported | FFS | FFS | FFS | FFS | FFS: CPU/AIMLPU related information | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506605](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506605.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122:9.1:005` · 후보 · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-4 | UE-side beam prediction for BM Case2 [for inference] | 1. Support of beam prediction with reporting of predicted beam index for BM-Case2 [for inference] with UE-side model 3. Maximum number of inference report(s) configured for BM-Case2 per BWP 3a. Maximum number of inference report(s) configured for BM-Case2 across all CCs [4. Maximum number of inference report(s) activated for BM-Case2 per BWP] [4a. Maximum number of inference report(s) activated for BM-Case2 across all CCs] [5. Maximum number of inference report(s) triggered for BM-Case2 per BWP] [5a. Maximum number of inference report(s) triggered for BM-Case2 across all CCs] 6. Support of SSB as RS type for Set B 6a. Support of CSI-RS as RS type for Set B 6b. Support of SSB as RS type for Set A 6c. Support of CSI-RS as RS type for Set A [7. Supported combinations of the number of resources for Set B and the number of resources for Set A] [7a: Supported maximum number of resources for Set B] [7b: Supported maximum number of resources for Set A] [8. Supported CSI-RS resource types: Periodic CSI-RS, Semi-persistent CSI-RS] [9. Supported inference report types: Periodic CSI report, Aperiodic CSI report, semi-persistent CSI report] [10. Supported options for performance monitoring for beam case 2 with UE side model] 11. Supported maximum number of predicted beams in each predicted time instance 12. Supported maximum number of predicted time instances [13. Supported maximum total number of reported predicted beams for predicted time instances in one report] 14. Supported combinations of supported value(s) of valid time duration for each predicted time instance and number of predicted beams for each value of valid time duration [20. Supported BM-Case 2 sub usecase(s): e.g., setB-equals-to-setA, setB-subset-of-setA, setB-different-from-setA, or merged version(s)] 21. supported number of occupied CPU 22. supported number of occupied APU 23. supported value of d for the relaxation of Z3 timeline 24. supported value of d’ for the relaxation of Z’3 timeline 17. Index of the occupied APU pool | FFS | yes | n/a | UE-side beam prediction for BM-Case2 [for inference] is not supported | FFS | FFS | FFS | FFS | FFS: CPU/AIMLPU related information FFS: candidate values for components | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506605](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506605.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122:9.1:024` · 후보 · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-2 | UE-side beam prediction for BM Case1 [for inference] | 1. Support of beam prediction with reporting of predicted beam index for BM-Case1 [for inference] with UE-side model 3. Maximum number of inference report(s) configured for BM-Case1 per BWP 3a. Maximum number of inference report(s) configured for BM-Case1 across all CCs [4. Maximum number of inference report(s) activated for BM-Case1 per BWP] [4a. Maximum number of inference report(s) activated for BM-Case1 across all CCs] [5. Maximum number of inference report(s) triggered for BM-Case1 per BWP] [5a. Maximum number of inference report(s) triggered for BM-Case1 across all CCs] 6. Support of SSB as RS type for Set B 6a. Support of CSI-RS as RS type for Set B 6b. Support of SSB as RS type for Set A 6c. Support of CSI-RS as RS type for Set A [7. Supported combinations of the number of resources for Set B and the number of resources for Set A] [7a: Supported maximum number of resources for Set B] [7b: Supported maximum number of resources for Set A] 8. Supported CSI-RS resource types: Periodic CSI-RS, Semi-persistent CSI-RS, Aperiodic CSI-RS 9. Supported inference report types: Periodic CSI report, Aperiodic CSI report, semi-persistent CSI report 11. Supported BM-Case 1 sub-usecase(s): {setB-subset-of-setA, setB-different-from-setA, both} 12. Supported maximum number of predicted beams in each reporting instanceFFS: whether/how to merge this FG with other FG(s) for performance monitoring and/or data collection 13. Supported number of occupied CPU 14. Supported number of occupied APU 15. Supported value of d for the relaxation of Z3 timeline 16. Supported value of d’ for the relaxation of Z’3 timeline 17. Index of the occupied APU pool | FFS | yes | n/a | UE-sided beam prediction for BM Case 1 [for inference] is not supported | FFS Per UE | FFS No | FFS No | FFS No | Component 8 candidate values: {Periodic CSI-RS, Semi-persistent CSI-RS, Aperiodic CSI-RS} Component 9 candidate values: {Periodic CSI report, Aperiodic CSI report, semi-persistent CSI report} FFS: candidate values for components | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506605](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506605.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122:9.1:025` · 후보 · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-4 | UE-side beam prediction for BM Case2 [for inference] | 1. Support of beam prediction with reporting of predicted beam index for BM-Case2 [for inference] with UE-side model 3. Maximum number of inference report(s) configured for BM-Case2 per BWP 3a. Maximum number of inference report(s) configured for BM-Case2 across all CCs [4. Maximum number of inference report(s) activated for BM-Case2 per BWP] [4a. Maximum number of inference report(s) activated for BM-Case2 across all CCs] [5. Maximum number of inference report(s) triggered for BM-Case2 per BWP] [5a. Maximum number of inference report(s) triggered for BM-Case2 across all CCs] 6. Support of SSB as RS type for Set B 6a. Support of CSI-RS as RS type for Set B 6b. Support of SSB as RS type for Set A 6c. Support of CSI-RS as RS type for Set A [7. Supported combinations of the number of resources for Set B and the number of resources for Set A] [7a: Supported maximum number of resources for Set B] [7b: Supported maximum number of resources for Set A] 8. Supported CSI-RS resource types: Periodic CSI-RS, Semi-persistent CSI-RS 9. Supported inference report types: Periodic CSI report, Aperiodic CSI report, semi-persistent CSI report 11. Supported maximum number of predicted beams in each predicted time instance 12. Supported maximum number of predicted time instances 13. Supported maximum total number of reported predicted beams for predicted time instances in one report 14. Supported combinations of supported value(s) of valid time duration for each predicted time instance and number of predicted beams for each value of valid time duration 21. supported number of occupied CPU 22. supported number of occupied APU 23. supported value of d for the relaxation of Z3 timeline 24. supported value of d’ for the relaxation of Z’3 timeline 2517. Index of the occupied APU pool | FFS | yes | n/a | UE-side beam prediction for BM-Case2 [for inference] is not supported | FFS Per UE | FFS No | FFS No | FFS No | Component 8 candidate values: {Periodic CSI-RS, Semi-persistent CSI-RS} Component 9 candidate values: {Periodic CSI report, Aperiodic CSI report, semi-persistent CSI report} FFS: candidate values for components | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506605](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506605.zip)

**Agreement** · `9.3` UE features for evolution of NR duplex operation: SBFD · `RAN1#122:9.3:002` · 후보 · 관련 주제: CSI-RS

> - FG 60-1 to include support of PDSCH/CSI-RS reception in two DL subbands
> Ø   Add a new component to report the number of partial PRGs supported
> Candidate values: {2, 4}
> Ø   Add a new component to report CSI timeline, active CSI-RS ports counting and active CSI-RS resource counting for a single CSI-RS resource across two DL subbands
> ²  Candidate values: {“with factor-of-two relaxation”, “without factor-of-two relaxation”}
> ²  Add a note: “FFS: details of counting”
> Ø   Add a new component of “maximum of one DL-UL switching point per SBFD slot for actual DL/UL transmission(s)”
> Ø   Add a new component of “Determination of TBS of PDSCH/PUSCH in SBFD symbols”
> - For FG 60-2, define another FG for Transmission across SBFD symbols and non-SBFD symbols in different slots (Configuration 2)
> - For FG 60-7 and 7a, confirm only one common pattern between DG/Type 2 CG PUSCH and Type 1 CG PUSCH
> - Introduce two FGs “separate UL resource muting for Type-1 CG PUSCH for CP-OFDM waveform” and “separate UL resource muting for Type-1 CG PUSCH for DFT-s-OFDM waveform”.
>   - FFS: Whether/how to capture maximum number of UL muting symbols per slot

남은 FFS 1건

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506409](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506409.zip)

**Agreement** · `9.6` UE features for NR mobility enhancements Phase 4 · `RAN1#122:9.6:001` · 후보 · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 63. NR_Mob_Ph4 | 63-6 | Intra-frequency CSI-RS and CSI-IM measurement and CSI reporting for cell indicated in CSC MAC CE after reception of LTM CSC MAC CE based on periodic CSI-RS resource | 1. Support of CSI-RS and CSI-IM measurement and CSI reporting after reception of LTM CSC MAC CE based on periodic CSI-RS(s) of cell indicated in CSC MAC CE [2. Maximum number of the RRC configured candidate cells] 3. Maximum number of CSI-RS resources for CMR associated with CSI report configuration for a candidate cell 4. Max number of CSI-RS ports of CSI-RS resource(s) associated with a CSI report configuration for CSI reporting for a candidate cell 5. Maximum number of Tx ports in one NZP CSI-RS resource 6. Max rank for CSI reporting for a candidate cell 7. Maximum number of CSI-IM resources for interference measurement associated with CSI report configuration for a candidate cell | FFS | Yes | No | Intra-frequency periodic CSI-RS and CSI-IM measurement and CSI reporting for cell indicated in CSC MAC CE after reception of LTM CSC MAC CE is not supported | FFS Per Band | n/a | n/a | n/a | Component 2 candidate values: {1,2,3,4,5,6,7,8} Component 3 candidate values: {1,2,3,4,5,6,7,8} Component 4 candidate values: {1,2,4,8,12,16,24,32,48,64,128} Component 5 candidate values: {1, 2, 4, 8, 12, 16, 24, 32} Component 6 candidate values: FFS {1,2,3,4,5,6,7,8} Component 7 candidate values: {1,2,3,4,5,6,7,8} | Optional with capability signaling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506608](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506608.zip)

**Agreement** · `9.6` UE features for NR mobility enhancements Phase 4 · `RAN1#122:9.6:002` · 후보 · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 63. NR_Mob_Ph4 | 63-6a | Intra-frequency CSI-RS and CSI-IM measurement and CSI reporting for cell indicated in CSC MAC CE after reception of LTM CSC MAC CE based on semi-persistent CSI-RS resource | 1. Support of CSI-RS and CSI-IM measurement and CSI reporting after reception of LTM CSC MAC CE based on periodic CSI-RS(s) of cell indicated in CSC MAC CE [2. Maximum number of the RRC configured candidate cells] 3. Maximum number of CSI-RS resources for CMR associated with CSI report configuration for a candidate cell 4. Max number of CSI-RS ports of CSI-RS resource(s) associated with a CSI report configuration for CSI reporting for a candidate cell 5. Maximum number of Tx ports in one NZP CSI-RS resource 6. Max rank for CSI reporting for a candidate cell 7. Maximum number of CSI-IM resources for interference measurement associated with CSI report configuration for a candidate cell | FFS | Yes | No | Intra-frequency semi-persistent CSI-RS and CSI-IM measurement and CSI reporting for cell indicated in CSC MAC CE after reception of LTM CSC MAC CE is not supported | FFS Per Band | n/a | n/a | n/a | Component 2 candidate values: {1,2,3,4,5,6,7,8} Component 3 candidate values: {1,2,3,4,5,6,7,8} Component 4 candidate values: {1,2,4,8,12,16,24,32,48,64,128} Component 5 candidate values: {1, 2, 4, 8, 12, 16, 24, 32} Component 6 candidate values: FFS {1,2,3,4,5,6,7,8} Component 7 candidate values: {1,2,3,4,5,6,7,8} | Optional with capability signaling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506608](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506608.zip)

**Agreement** · `9.6` UE features for NR mobility enhancements Phase 4 · `RAN1#122:9.6:003` · 후보 · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 63. NR_Mob_Ph4 | 63-7 | Intra-frequency CSI-RS and CSI-IM measurement for candidate cell before reception of LTM CSC MAC CE based on periodic CSI-RS(s) of candidate cells | 1. Support of CSI-RS and CSI-IM measurement before reception of CSC MAC CE based on periodic CSI-RS(s) of candidate cells 2. Maximum number of RRC configured candidate cells for CSI measurement before LTM CSC MAC CE 3. Maximum number of RRC configured CSI-RS resources across candidate cells for CSI measurement before LTM CSC MAC CE 4. Max number of CSI-RS ports of CSI-RS resource(s) associated with a CSI report configuration for CSI reporting for a candidate cell 5. Maximum number of Tx ports in one NZP CSI-RS resource associated with a CSI report configuration for CSI reporting for a candidate cell [6. Max rank for CSI reporting for a candidate cell] 6. Maximum number of RRC configured CSI-IM resources across candidate cells for CSI measurement before LTM CSC MAC CE | 63-6 | Yes | No | Intra-frequency periodic CSI-RS and CSI-IM measurement for candidate cell before reception of LTM CSC MAC CE is not supported | Per BC | n/a | n/a | n/a | Component 2 candidate values: {1,2,3,4,5,6,7,8} Component 3 candidate values: {1,2,...64} Component 4 candidate values: FFS {1,2,4,8,12,16,24,32,48,64,128} Component 5 candidate values: FFS {1,2,4,8,12,16,24,32} Component 6 candidate values: {1,2,…64} | Optional with capability signaling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506608](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506608.zip)

**Agreement** · `9.6` UE features for NR mobility enhancements Phase 4 · `RAN1#122:9.6:004` · 후보 · 관련 주제: CSI-RS

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 63. NR_Mob_Ph4 | 63-7a | Intra-frequency CSI-RS and CSI-IM measurement for candidate cell before reception of LTM CSC MAC CE based on semi-persistent CSI-RS(s) of candidate cells | 1. Support of CSI-RS and CSI-IM measurement before reception of CSC MAC CE based on semi-persistent CSI-RS(s) of candidate cells 2. Maximum number of RRC configured candidate cells for CSI measurement before LTM CSC MAC CE 3. Maximum number of RRC configured CSI-RS resources across candidate cells for CSI measurement before LTM CSC MAC CE 4. Max number of CSI-RS ports of CSI-RS resource(s) associated with a CSI report configuration for CSI reporting for a candidate cell 5. Maximum number of Tx ports in one NZP CSI-RS resource associated with a CSI report configuration for CSI reporting for a candidate cell [6. Max rank for CSI reporting for a candidate cell] 6. Maximum number of RRC configured CSI-IM resources across candidate cells for CSI measurement before LTM CSC MAC CE | 63-6a | Yes | No | Intra-frequency semi-persistent CSI-RS and CSI-IM measurement for candidate cell before reception of LTM CSC MAC CE is not supported | Per BC | n/a | n/a | n/a | Component 2 candidate values: {1,2,3,4,5,6,7,8} Component 3 candidate values: {1,2,...64} Component 4 candidate values: FFS {1,2,4,8,12,16,24,32,48,64,128} Component 5 candidate values: FFS {1,2,4,8,12,16,24,32} Component 6 candidate values: {1,2,...64} | Optional with capability signaling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506608](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506608.zip)

**Agreement** · `9.6` UE features for NR mobility enhancements Phase 4 · `RAN1#122:9.6:005` · 후보 · 관련 주제: CSI-RS

> Introduce the following Rel. 19 UE FGs (yellow highlighting, if any, shows text that’s not yet agreed)
> | 63. NR_Mob_Ph4 | 63-10 | Intra-frequency CSI-RS-RS measurement and CSI reporting without CSI-IM reception | 1. Support of CSI-RS measurement and CSI reporting for candidate cells without CSI-IM resource configuration | 63-6 or 63-6a or 63-7 or 63-7a | Yes | No | Intra-frequency CSI-RS-RS measurement and CSI reporting without CSI-IM reception is not supported | Per band | n/a | n/a | n/a |  | Optional with capability signaling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506608](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506608.zip)

**Agreement** · `9.14` Others · `RAN1#122:9.14:004` · 후보 · 관련 주제: CSI-RS

> Introduce the following Rel. 19 UE FGs (yellow highlighting, if any, shows text that’s not yet agreed)
> | 67. TEI19 [SimCSI_countNES] | 67-8 | Simultaneous NZP-CSI-RS resource counting NES | For simultaneous CSI-RS reception in Network Energy Saving UE features 42-1/1a/1b/1c, and 42-2/2a/2b/2c, for a periodic/semi-persistent CSI-RS resource referred N times by one or more CSI Reporting Settings with at least one CSI Reporting Setting configured with higher layer csi-ReportSubConfigToAddModList, the CSI-RS resource is counted one time by the UE and the CSI-RS ports within that CSI-RS resource, are counted as P, where P is the number of ports configured by nrofPorts. | 42-1/1a/1b/1c, or 42-2/2a/2b/2c | yes | n/a | gNB would not assume that UE supports this capability | Per BC | No | No | n/a |  | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506610](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506610.zip)
