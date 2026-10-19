# Beam management — RAN1 CSI 결정

> 원본 DB 마지막 업데이트 **2026-10-19 20:12 KST** · [요약으로 돌아가기](../README.md)

확정 118건 (Agreement 116 · WA 1 · Conclusion 1), 후보 64건. 결정 본문은 Chair notes 원문 그대로입니다(요약 없음). 최신 회의부터 보여줍니다.

## RAN1#126bis — 18건

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#126bis:10.5.1.1:001` · 🆕 신규

> The following templates are used to capture the coverage gap relative to the basic coverage of 143 dB MaxCL and extended coverage of 153 dB MaxCL for different signals and channels during initial access
> Note: The coverage gap is determined as the trimmed mean of all submitted samples, trimmed mean is calculated by discarding the single lowest and highest values.
> Note: the results for UE with 1Rx and 2Rx, 15kHz SCS and 30kHz SCS will be captured in separate Tables.
> Table X: Coverage gap relative to 143 dB MaxCL for different signals and channels during initial access [Template] based on R15 NR assumptions
> | Signals/channels | Number of Sample(s) | Coverage gap (trimmed mean) | Standard Deviation (w/o outlier) |
> | PSS/SSS |  |  |  |
> | PBCH |  |  |  |
> | SIB1 PDCCH |  |  |  |
> | SIB1 PDSCH |  |  |  |
> | Msg2 PDSCH |  |  |  |
> | Msg4 PDSCH |  |  |  |
> | PRACH format 0 |  |  |  |
> | PRACH format B4 |  |  |  |
> | PRACH format C2 |  |  |  |
> | Msg3 PUSCH |  |  |  |
> | Msg5 PUSCH |  |  |  |
> | PUCCH format 1 |  |  |  |
> Table X: Coverage gap relative to 153 dB MaxCL for different signals and channels during initial access [Template] based on R15 NR assumptions
> | Signals/channels | Number of Sample(s) | Coverage gap (trimmed mean) | Standard Deviation (w/o outlier) |
> | PSS/SSS |  |  |  |
> | PBCH |  |  |  |
> | SIB1 PDCCH |  |  |  |
> | SIB1 PDSCH |  |  |  |
> | Msg2 PDSCH |  |  |  |
> | Msg4 PDSCH |  |  |  |
> | PRACH format 0 |  |  |  |
> | PRACH format B4 |  |  |  |
> | PRACH format C2 |  |  |  |
> | Msg3 PUSCH |  |  |  |
> | Msg5 PUSCH |  |  |  |
> | PUCCH format 1 |  |  |  |
> Note: 2 more rows for PSS/SSS, PBCH with 4 times combination will be added additionally.

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Synchronization and Beam Measurement]`

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#126bis:10.5.1.1:002` · 🆕 신규

> 6GR supports configurable Timing Advance Offset
> - For TN,
>   - For FR1, Timing Advance Offset values include 0, 25600 Tc and 39936 Tc, where Tc is the time unit used in NR.

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Synchronization and Beam Measurement]`

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#126bis:10.5.1.1:003` · 🆕 신규

> - One 6GR SSB spans X OFDM symbols within a slot, where X is down-selected from {4, 5, 6}
>   - Alt 1: 1 symbol for PSS and 1 symbol for SSS for X = 4
>   - Alt 2: 2 symbols for PSS for X = 5, 6
> - Each slot including candidate SSBs consists of two candidate SSBs time locations

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Synchronization and Beam Measurement]`

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#126bis:10.5.1.1:004` · 🆕 신규

> For 6GR TN, the maximum number of candidate SSB beams within one 6GR SSB period L is
> - For < 3GHz: 4, 8
>   - FFS: detailed applicable bands
> - For sub 6GHz: 8
> - For around 7GHz: 16

남은 FFS 1건

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Synchronization and Beam Measurement]`

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#126bis:10.5.1.1:005` · 🆕 신규

> RAN1 to down-select from the following options
> - Option 1:
>   - SSB repetition within one default SSB periodicity: UE is assumed to support SSB combining across different SSB repetitions within one default SSB periodicity by the maximum number of repetitions M
>     - 160 ms default SSB periodicity for initial cell search
>     - Maximum number of repetitions: M = 4
>     - Fixed or adjustable number of repetitions
>       - Alt 1: Adjustable number of repetitions within one SSB period: {1, 2, 4} or {1, 4} or {2, 4}
>         - FFS: other restrictions
>       - Alt 2: Fixed number of repetitions within one SSB period: 4
> - Option 2a:
>   - SSB repetition within one default SSB periodicity: UE is assumed to support SSB combining across different SSB repetitions within one default SSB periodicity by the maximum number of repetitions M and across different default SSB periodicities by the number of N
>     - 80 ms default SSB periodicity for initial cell search
>     - Maximum number of repetitions and number of default SSB periodicities for UE to perform SSB combining: M = 2, N = 2
>     - Fixed or adjustable number of repetitions
>       - Alt 1: Adjustable number of repetitions within one SSB period: {1, 2}
>         - FFS: other restrictions
>       - Alt 2: Fixed number of repetitions within one SSB period: 2
> - Option 2b:
>   - SSB repetition within one default SSB periodicity: UE is assumed to support SSB combining across different SSB repetitions within one default SSB periodicity by the maximum number of repetitions M
>     - 80 ms default SSB periodicity for initial cell search
>     - Maximum number of repetition: M = 4
>     - Fixed or adjustable number of repetitions
>       - Alt 1: Adjustable number of repetitions within one SSB period: {1, 2, 4} or {1, 4} or {2, 4}
>         - FFS: other restrictions
>       - Alt 2: Fixed number of repetitions within one SSB period: 4
> - Option 3:
>   - No SSB repetition within one default SSB periodicity: UE is assumed to support SSB combining across different SSB default periodicities by the number of N
>     - 40 ms default SSB periodicity for initial cell search
>     - number of default SSB periodicities for UE to perform SSB combining: N = 4
> - Option 4:
>   - SSB repetition within one default SSB periodicity: UE is assumed to support SSB combining across different SSB repetitions within one default SSB periodicity by the maximum number of repetitions M and across different default SSB periodicities by the number of N
>     - 40 ms default SSB periodicity for initial cell search
>     - Maximum number of repetitions and number of default SSB periodicities for UE to perform SSB combining: (M = 2, N = 2)
>     - Fixed or adjustable number of repetitions
>       - Alt 1: Adjustable number of repetitions within one SSB period: {1, 2}
>         - FFS: other restrictions
>       - Alt 2: Fixed number of repetitions within one SSB period: 2 for M = 2
> - Option 5:
>   - No SSB repetition within one default SSB periodicity: UE is assumed to support SSB combining across different SSB default periodicities by the number of N
>     - 20 ms default SSB periodicity for initial cell search
>     - number of default SSB periodicities for UE to perform SSB combining: N = 4
> - Note: The performance requirement in the above options will be defined by RAN4 including the assumptions on UE combining behaviors
> - For Option 1/2/3/4, RAN1 will consider the following solutions to mitigate the UE impact
>   - Solutions to reduce cell search complexity and latency
>   - Additional synchronization/reference signal in addition to SSB transmissions in one default SSB periodicity at least for UEs in connected mode with configurable periodicity at least including 20 ms
> Note: The maximum number of SSB combining in the above options is discussed from targeting coverage point of view.
> Note: The detailed UE capability definition will be discussed separately.
> Note: The SSB combining assumptions does not preclude other UE implementations, provided that the performance requirements are met.

남은 FFS 4건

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Synchronization and Beam Measurement]`

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#126bis:10.5.1.1:006` · 🆕 신규

> Study Sub-case D in R1-2600986 with focusing on potential spec impact of AI/ML based spatial/temporal beam prediction during 6GR initial access.
> - Note: the benefits and the feasibility justification can refer to study outcome in TR 38.843.

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Synchronization and Beam Measurement]`

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#126bis:10.5.1.1:007` · 🆕 신규

> For the further study of PSS and SSS (including sequence type, sequence length and number of sequences, number of symbols for PSS and SSS), companies are encouraged to report PSS and PSS&SSS detection performance without combining across multiple SSB occasions considering the following performance metrics:
> - False alarm rate (FAR)
>   - Option 1: 1% for PSS
>   - Option 2: 1% for PSS&SSS
> - Miss detection rate (MDR) for PSS&SSS: 1%, 10%
>   - The detection is claimed to be successful only when both PSS and SSS are correctly detected and the detected timing is within half CP length compared to the strongest path of the channel.
>   - [False timing performance for 1% FAR]
>     - [Number of peaks exceeding the threshold]
>   - Residual timing error: RMSE or 95th percentile
>   - Residual frequency offset: RMSE or 95th percentile
>   - [PAPR]
> - Detection complexity
>   - PSS detection complexity: total # of real value multiplications for one detection attempt within one default SSB periodicity
>     - [Note: companies are encouraged to report the number of PSS peak positions in the evaluation, which are passed to SSS for further detection]
>   - SSS detection complexity: total # of real value multiplications for one detection attempt within one default SSB periodicity
>   - [Memory usage: the amount of memory for PSS and SSS detection]
> Note: companies are encouraged to report the PSS/SSS detection procedure, interference modeling, and algorithms for the above evaluation.

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Synchronization and Beam Measurement]`

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#126bis:10.5.1.1:008` · 🆕 신규

> For the further study of PSS and SSS (including sequence type, sequence length and number of sequences, number of symbols for PSS and SSS), companies are encouraged to report PSS and PSS&SSS detection performance with combining across M repetitions within N SSB periodicities considering the following performance metrics:
> - False alarm rate (FAR)
>   - Option 1: 1% for PSS
>   - Option 2: 1% for PSS&SSS
> - Miss detection rate (MDR) for PSS&SSS: 1%
>   - The detection is claimed to be successful only when both PSS and SSS are correctly detected and the detected timing is within half CP length compared to the strongest path of the channel.
>   - [False timing performance for 1% FAR]
>     - [Number of peaks exceeding the threshold]
>   - Residual timing error: RMSE or 95th percentile
>   - Residual frequency offset: RMSE or 95th percentile
> - Detection complexity
>   - PSS detection complexity: total # of real value multiplications for one detection attempt across M repetitions within N SSB periodicities
>     - [Note: companies are encouraged to report the number of PSS peak positions in the evaluation, which are passed to SSS for further detection]
>   - SSS detection complexity: total # of real value multiplications for one detection attempt for one detection attempt across M repetitions within N SSB periodicities
>   - [Memory usage: the amount of memory for PSS and SSS detection]
> Note: companies are encouraged to report the PSS/SSS detection procedure and algorithms, interference modeling for the above evaluation.
> Note: to evaluate PSS/SSS combining across multiple SSB occasions,
> - Option 1 and Option 3 are recommended (referring to the 6 SSB periodicity options) for the number of SSB repetitions and number of SSB periodicities for combining.
> - Companies are encouraged to model the sampling frequency offset (SFO).

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Synchronization and Beam Measurement]`

**Agreement** · `10.5.3.3` Other aspects · `RAN1#126bis:10.5.3.3:002` · 🆕 신규

> Further study and evaluate the following assistant information for use case 2
> - Wideband/Subband L1-RSRP + IPN
>   - L1-RSRP is measured based on NZP CSI-RS and IPN is measured based on a CSI-IM
> - Subband L1-SINR/RSRP
>   - L1-SINR is measured based on NZP CSI-RS as CMR and a CSI-IM as IMR, if any
>   - L1-RSRP is measured based on NZP CSI-RS as CMR
> - CQI/RI/PMI or CQI/RI
>   - CQI is derived from the NZP CSI-RS as CMR and a CSI-IM as IMR
>   - CQI is derived from PDSCH DMRS

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Other Aspects related to CSI]`

**Agreement** · `10.5.3.4` Beam management for downlink and uplink · `RAN1#126bis:10.5.3.4:001` · 🆕 신규

> Regarding UE initiated beam management, on event detection for triggering UL transmission,
> - For event evaluation metric on Event-2, at least L1-RSRP is supported
>   - FFS: Option-2b, L1-SINR

남은 FFS 1건

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Beam management]`

**Agreement** · `10.5.3.4` Beam management for downlink and uplink · `RAN1#126bis:10.5.3.4:002` · 🆕 신규

> For the study on beam measurement and report on the deployment scenarios of NW multi-TRP/multi-panel and/or single/multi-panel UE, the following can be studied on Case-2:
> - Regarding L1-RSRP calculation, NR L1-RSRP definition can be used as the starting point.
>   - FFS: Whether any other extension of L1-RSRP definition is needed
> - Regarding RS measurement requirements,
>   - Consider a functionality of enabling UE to differentiate DL RSs from different NW TRPs/panels within a cell or across cells for DL beam measurement and report.
> - Regarding report content/format, study the report content to support the UE to report DL RSs that can be received simultaneously
> - Note (Case-2): To identify/report the preferred M >1 DL beams of different NW TRPs/panels that can be received simultaneously to facilitate multi-TRP/panel joint transmission
> - Note: Above TRPs may belong to a same cell or different cells.
> - Note (for the study purpose): The above study at least considers the following transmission schemes: CJT, SFN and NCJT (if supported), using NW multi-TRP/multi-panel.

남은 FFS 1건

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Beam management]`

**Agreement** · `10.5.3.4` Beam management for downlink and uplink · `RAN1#126bis:10.5.3.4:003` · 🆕 신규

> For the study on spatial/temporal domain DL Tx beam prediction and management on multi-TRP/cell(intra/inter-cell), study both NW-side prediction and UE-side prediction.
> - Regarding NW-side prediction, study the report contents in one report instance.
>   - The number of measured beams across TRPs/cell(s) to be reported.
>   - The number of measured beams for one TRP/cell to be reported.
>   - FFS: Other report contents
> - Regarding UE-side prediction,
>   - Study the report contents in one report instance
>   - Study the training and inference consistency for UE-side model, e.g., extensions of association ID to support multi-TRP/cell (intra/inter-cell).
>   - FFS: information about the time instance corresponding the predicted beam(s), regarding temporal domain DL Tx beam prediction.
> - Note: Prediction can be performed based on AI/ML or non-AI/advanced schemes.

남은 FFS 2건

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Beam management]`

**Agreement** · `10.5.3.4` Beam management for downlink and uplink · `RAN1#126bis:10.5.3.4:004` · 🆕 신규

> For the study on frequency domain beam measurement/prediction (cross-frequency), study both NW-side prediction and UE-side prediction:
> - Regarding NW-side prediction, study the report contents in one report instance.
>   - Metrics of measured beams in a set-B for source frequency to be reported.
> - Regarding UE-side prediction, study the report contents in one report instance, training and inference consistency for UE-side model, e.g., extensions of the association ID to support cross-frequency.
> - Note: Prediction can be performed based on AI/ML or non-AI/advanced schemes.

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Beam management]`

**Agreement** · `10.5.3.4` Beam management for downlink and uplink · `RAN1#126bis:10.5.3.4:005` · 🆕 신규

> Regarding QCL framework, study whether and how to define QCL combination of one or more QCL properties (associated with a same source QCL-RS)

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Beam management]`

**Agreement** · `10.5.3.4` Beam management for downlink and uplink · `RAN1#126bis:10.5.3.4:006` · 🆕 신규

> Regarding QCL framework,
> - Support QCL relationship at least for spatial Rx parameters, where the source QCL-RS and target channel/RS is in a same CC.
> - Support intra-band cross-CC QCL relationship w.r.t. spatial Rx parameter, where the source QCL-RS can be located on a carrier different from the carrier of the target channel/RS.

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Beam management]`

**Agreement** · `10.5.3.4` Beam management for downlink and uplink · `RAN1#126bis:10.5.3.4:007` · 🆕 신규

> Regarding requirement/functionality of DL RS for beam measurement, for inter-symbol NW/UE-side beam sweeping, the following is considered:
> - No more than 2 ports for a DL RS resource for beam measurement is considered, and final decision on the number of ports for a DL RS resource is made in RAN1#127.
> - Note (for evaluation purpose): Companies are encouraged to report port virtualization for a cross-polarized array for 1-port or 2-port, and the criteria of beam selection.
> At least support the following time domain behavior of DL RS for beam measurement: aperiodic, and periodic
> - FFS: Whether/how to support semi-persistent DL RS for beam measurement
> - Note: Sync-signal design is not considered herein

남은 FFS 1건

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Beam management]`

**Agreement** · `10.5.3.4` Beam management for downlink and uplink · `RAN1#126bis:10.5.3.4:008` · 🆕 신규

> On NW-initiated beam management, regarding intra-symbol beam sweeping, for evaluation purpose, companies to report the details on DL-RS multiplexing for the followings:
> - Frequency-domain/FDMed for NW Tx beam sweeping.
> - Sequence-domain/CDMed for NW Tx beam sweeping.
> - Sub-symbol/TDMed for UE Rx beam sweeping.

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Beam management]`

**Agreement** · `10.5.3.4` Beam management for downlink and uplink · `RAN1#126bis:10.5.3.4:009` · 🆕 신규

> For the study on spatial/frequency domain beam prediction, for evaluation purpose, study the following aspects on matrix-based approach,
> - UE-side derivation approach of predicted results based on the combination coefficient(s), W, and measured results of Set-B,
>   - For example, Y = WX, where Y is predicted result(s) of Set-A, and X is measured L1-RSRPs of Set-B.
>   - Companies to clarify the reporting metric based on Y.
>   - Companies to report whether measured results of Set-B is quantized or not
> - Matrix size
> - Companies to report applicability of this approach, e.g., single/multi-TRP spatial domain, co-located frequency domain beam prediction (cross-frequency).

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Beam management]`

## RAN1#126 — 30건

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#126:10.5.1.1:001`

> For the link budget evaluations in around 7 GHz for coverage gap identification, the assumptions for the receiver noise figure are 9 dB and 5 dB for DL and UL respectively (agreed in RAN1#124)
> - Send an LS to RAN4 about the assumptions for information only.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Synchronization and Beam Measurement]`

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#126:10.5.1.1:002`

> For the link budget evaluations for the coverage gap identification, no update to the cell area reliability for initial-access related signals/channels, i.e., 95% for control channel, SSB and SIB1 and 90% for other channels that are capable of HARQ retransmissions but HARQ retransmissions are not assumed.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Synchronization and Beam Measurement]`

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#126:10.5.1.1:003`

> Support Resource block boundaries alignment between NR and 6GR on a MRSS carrier.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Synchronization and Beam Measurement]`

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#126:10.5.1.1:004`

> In 6GR, aNB-side semi-static SBFD is supported.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Synchronization and Beam Measurement]`

**WA** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#126:10.5.1.1:005`

> For 6GR, one SSB is defined by a single value of X
> - One 6GR SSB spans X (4<=X<=7) OFDM symbols within a slot

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Synchronization and Beam Measurement]`

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#126:10.5.1.1:006`

> - One 6GR SSB spans 20 RBs

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Synchronization and Beam Measurement]`

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#126:10.5.1.1:007`

> For one 6G SSB, the number of RBs for PSS is 12 RBs.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Synchronization and Beam Measurement]`

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#126:10.5.1.1:008`

> Study the following aspects for 6GR PSS
> - Sequence type
>   - Option 1: m-sequence
>   - Option 2: ZC-based sequence
>   - Option 3: Other sequence
> - Sequence length
>   - Option 1: 127
>   - Option 2: 127<L<=144
> - Number of sequences
> - Number of symbols for PSS

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Synchronization and Beam Measurement]`

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#126:10.5.1.1:009`

> Study the following aspect for 6GR SSS
> - Sequence type
>   - Gold sequence as a benchmark
>   - FFS: Other sequences
> - Sequence length
>   - Option 1: 127
>   - Option 2: > 127
> - Number of sequences
> - Number of symbols for SSS

남은 FFS 1건

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Synchronization and Beam Measurement]`

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#126:10.5.1.1:010`

> Final LS R1-2606913 with following contents is endorsed.
> 1. Overall Description:
> In the study of “Re-use of existing 5G mid-band (~3.5GHz) site grid for 6G deployments in at least around 7 GHz and targeting comparable coverage to 5G mid-band”, RAN1 made an agreement that for the link budget evaluations in around 7 GHz for coverage gap identification, the assumptions for the receiver noise figure are 9 dB and 5 dB for DL and UL respectively. There is no implication that RAN4 should use the same assumption.
> 2. Actions:
> To RAN4
> ACTION: RAN1 would like to respectfully inform RAN4 about the above receiver noise figure assumptions.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Synchronization and Beam Measurement]`

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#126:10.5.1.1:011`

> The coverage gap between ~7GHz and 5G mid-band for different signals and channels during initial access are identified in the following tables.
> Table X: Coverage gap between 7.0 GHz and 5G mid-band (3.5 GHz) for different signals and channels during initial access for UMa O2I
> | Signals/channels | Number of Sample(s) | Coverage gap (trimmed mean) | Standard Deviation (w/o outlier) |
> | PSS/SSS w/o combining | 11 | -7.24 | 1.63 |
> | PBCH w/o combining | 9 | -8.32 | 1.83 |
> | PSS/SSS w/ 4 combining | 8 | -4.08 | 1.30 |
> | PBCH w/ 4 combining | 14 | -3.09 | 1.62 |
> | SIB1 PDCCH | 17 | -5.56 | 1.63 |
> | SIB1 PDSCH | 16 | -6.91 | 1.68 |
> | Msg2 PDSCH | 11 | -3.96 | 2.61 |
> | Msg4 PDSCH | 13 | -4.11 | 1.77 |
> | PRACH format 0 | 14 | -2.73 | 1.43 |
> | PRACH format B4 | 14 | -4.80 | 2.19 |
> | PRACH format C2 | 11 | -8.37 | 1.21 |
> | Msg3 PUSCH | 20 | -8.68 | 1.67 |
> | Msg5 PUSCH | 11 | -13.00 | 2.98 |
> | PUCCH format 1 | 13 | -3.64 | 2.33 |
> Comparing the coverage between 3.5GHz and 2.6GHz in UMa O2I, there is 4.5 dB difference for Msg 3, which is assumed to be applicable for all signals/channels.
> Table X: Coverage gap between 7.0 GHz and 5G mid-band (3.5 GHz) for different signals and channels during initial access for UMa O2O
> | Signals/channels | Number of Sample(s) | Coverage gap (trimmed mean) | Standard Deviation (w/o outlier) |
> | PSS/SSS w/o combining | 5 | -2.81 | 0.33 |
> | PBCH w/o combining | 4 | -1.51 | 0.13 |
> | PSS/SSS w/ 4 combining | 6 | 1.13 | 2.15 |
> | PBCH w/ 4 combining | 9 | 1.69 | 1.52 |
> | SIB1 PDCCH | 8 | -1.28 | 0.65 |
> | SIB1 PDSCH | 9 | -2.92 | 1.33 |
> | Msg2 PDSCH | 6 | 0.21 | 2.61 |
> | Msg4 PDSCH | 7 | -1.06 | 1.64 |
> | PRACH format 0 | 8 | 2.54 | 0.57 |
> | PRACH format B4 | 7 | 0.22 | 1.68 |
> | PRACH format C2 | 7 | -4.09 | 1.47 |
> | Msg3 PUSCH | 11 | -3.75 | 1.11 |
> | Msg5 PUSCH | 6 | -10.19 | 3.01 |
> | PUCCH format 1 | 5 | -0.03 | 1.12 |
> Comparing the coverage between 3.5GHz and 2.6GHz in UMa O2O, there is 2.58 dB difference for Msg 3, which is assumed to be applicable for all signals/channels.
> Table X: Coverage gap between 7.0 GHz and 5G mid-band (3.5 GHz) for different signals and channels during initial access for SMa O2I
> | Signals/channels | Number of Sample(s) | Coverage gap (trimmed mean) | Standard Deviation (w/o outlier) |
> | PSS/SSS w/o combining | 5 | -3.64 | 0.44 |
> | PBCH w/o combining | 3 | -2.16 | N/A |
> | PSS/SSS w/ 4 combining | 4 | -1.27 | 1.47 |
> | PBCH w/ 4 combining | 7 | 1.11 | 0.99 |
> | SIB1 PDCCH | 7 | -1.80 | 0.60 |
> | SIB1 PDSCH | 7 | -3.35 | 1.21 |
> | Msg2 PDSCH | 5 | 0.68 | 2.01 |
> | Msg4 PDSCH | 5 | -1.91 | 1.35 |
> | PRACH format 0 | 7 | 1.88 | 0.59 |
> | PRACH format B4 | 5 | -1.40 | 1.54 |
> | PRACH format C2 | 6 | -5.23 | 1.09 |
> | Msg3 PUSCH | 7 | -4.01 | 0.41 |
> | Msg5 PUSCH | 5 | -11.76 | 2.88 |
> | PUCCH format 1 | 4 | -0.22 | 0.89 |
> Table X: Coverage gap between 7.0 GHz and 5G mid-band (3.5 GHz) for different signals and channels during initial access for SMa O2O
> | Signals/channels | Number of Sample(s) | Coverage gap (trimmed mean) | Standard Deviation (w/o outlier) |
> | PSS/SSS w/o combining | 5 | -2.81 | 0.33 |
> | PBCH w/o combining | 3 | -1.42 | N/A |
> | PSS/SSS w/ 4 combining | 4 | -0.50 | 1.25 |
> | PBCH w/ 4 combining | 7 | 1.92 | 1.03 |
> | SIB1 PDCCH | 7 | -1.18 | 0.67 |
> | SIB1 PDSCH | 7 | -2.67 | 1.21 |
> | Msg2 PDSCH | 5 | 1.07 | 2.40 |
> | Msg4 PDSCH | 5 | -0.85 | 1.24 |
> | PRACH format 0 | 7 | 2.60 | 0.61 |
> | PRACH format B4 | 5 | -0.82 | 1.17 |
> | PRACH format C2 | 6 | -4.60 | 1.05 |
> | Msg3 PUSCH | 7 | -3.21 | 0.49 |
> | Msg5 PUSCH | 5 | -11.13 | 2.88 |
> | PUCCH format 1 | 4 | 0.56 | 0.67 |

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Synchronization and Beam Measurement]`

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#126:10.5.1.1:012`

> For the MaxCL requirement in TR 38.914, companies are encouraged to provide MaxCL evaluations based on the following assumptions:
> - Assumptions used for maxCL calculations in TR38.914:
> - Table 5.1.20.1-2: MaxCL calculation assumptions
> | UE Tx power | 23dBm |
> | DL Tx power | 46dBm |
> | BS receiver noise figure | 5dB |
> | UE receiver noise figure | 9dB |
> | Interference margin | 0dB |
>   - Note: DL Tx power is 46dBm per 20 MHz and scales with wider bandwidth.
> - Carrier frequency, duplex and SCS
>   - FDD, carrier frequency: 0.7 GHz, 15kHz SCS
>   - TDD, carrier frequency: 2.6 GHz, 30kHz SCS
> - UE speed: 3kmh
> - Channel model
>   - TDL-C with 300ns delay spread
>     - DL: 2T2R and 2T1R
>     - UL: 1T2R
> - Signals/channels to be evaluated
>   - DL: NR PSS/SSS, PBCH, Common PDCCH, SIB1 PDSCH, Msg2/4 PDSCH
>   - UL: NR PRACH format C2/B4/0, MSG3 PUSCH, MSG5 PUSCH (companies to report assumption of the payload of actual transmission),  MSG4 PUCCH Format 1
> - The simulation assumptions in section A.1 in TR38.830 are used as a starting point.
>   - The payload for NR SIB1 PDSCH is 1200 bits.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Synchronization and Beam Measurement]`

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#126:10.5.1.1:013`

> Capture the evaluation results from companies on NES evaluations into the TR
> - Note: Evaluation results can be updated in the next meeting.
> | Company | BS Cat | Load (RU) | Configuration | 40 ms | 80 ms | 160 ms |
> | Mid-band (~2-4 GHz) — NES gains vs 20 ms baseline | Mid-band (~2-4 GHz) — NES gains vs 20 ms baseline | Mid-band (~2-4 GHz) — NES gains vs 20 ms baseline | Mid-band (~2-4 GHz) — NES gains vs 20 ms baseline | Mid-band (~2-4 GHz) — NES gains vs 20 ms baseline | Mid-band (~2-4 GHz) — NES gains vs 20 ms baseline | Mid-band (~2-4 GHz) — NES gains vs 20 ms baseline |
> | CEWiT [R1-2606646] | Cat 1 | 5% / 10% / 20% | SLS 21-cell, SIB1 retained at 20 ms | – | 23.4% / 19.3% / 16.4% | 24.9% / 20.8% / 17.5% |
> | CEWiT [R1-2606646] | Cat 1 | 5% / 10% / 20% | SLS 21-cell, SIB1 and common signals CLUSTERED | – | 51% / 47.8% / 45.4% | 56.3% / 52.7% / 49.5% |
> | OPPO [R1-2605917] | Cat 1 / Cat 2 / Cat 2.1 | 0% | — | 32% / 20% / 20% | 67% / 31% / 31% | 81% / 36% / 62% |
> | OPPO [R1-2605917] | Cat 1 / Cat 2 / Cat 2.1 | Low NA | — | 23% / 16% / 16% | 40% / 23% / 24% | 49% / 27% / 30% |
> | OPPO [R1-2605917] | Cat 1 / Cat 2 / Cat 2.1 | Light NA. | — | 15% / 11% / 11% | 24% / 16% / 16% | 28% / 19% / 19% |
> | OPPO [R1-2605917] | Cat 1 / Cat 2 / Cat 2.1 | Med NA | — | 9% / 7% / 7% | 14% / 11% / 11% | 17% / 12% / 13% |
> | Samsung [R1-2605823] | Cat 1 / Cat 2 | 0% | — | 36% / 26.2% | 72.3% / 39.3% | 85.6% / 45.8% |
> | Samsung [R1-2605823] | Cat 1 / Cat 2 | 14% | — | 19.5% / 5.2% | 29.5% / 13.6% | 34.7% / 14.6% |
> | Qualcomm [R1-2606375] | Cat 1 / Cat 2 | 0% | — | 18% / 3.7% | 57% / 5.5% | 78% / 6.5% |
> | Qualcomm [R1-2606375] | Cat 1 / Cat 2 | 5% | — | 11% / 3.1% | 18% / 4.5% | 19% / 5.5% |
> | Qualcomm [R1-2606375] | Cat 1 / Cat 2 | 15% | — | 5% / 2.1% | 8% / 3.7% | 9% / 4.2% |
> | Ericsson [R1-2605521] | Cat 1 | 0% / 4% | — | 13% / 12% | 62% / 38% | 80% / 62% |
> | Ofinno [R1-2605675] | Cat 1 / Cat 2 | 0% | Set 1 | 11% / 8% | 72% / 12% | 84% / 14% |
> | Ofinno [R1-2605675] | Cat 1 / Cat 2 | 0% | Set 2 | 21% / 11% | 59% / 16% | 78% / 19% |
> | Ofinno [R1-2605675] | Cat 1 / Cat 2 | 0% | Set 3 | 12% / 37% | 87% / 55% | 93% / 64% |
> | Spreadtrum [R1-2605254] | Cat 2.1 | 0% | — | 12.48% | 18.71% | – |
> | ZTE [R1-2605431] | Cat 1 | 0% | SSB + SIB1 + PRACH all at 160 ms | – | – | 53.5% |
> | ZTE [R1-2605431] | Cat 1 | Low n.s. | SSB + SIB1 + PRACH at 160 ms | – | – | 32.9% |
> | Lenovo [R1-2606336] | Cat 1 | 0% | Clustered SSB | – | 23.5% | 61% |
> | Lenovo [R1-2606336] | Cat 1 | 0% | Non-clustered SSB | 20.5% | 57% | 77.5% |
> | HONOR [R1-2606186] | Cat 1 | 0% | 20 → 160 ms | – | – | 80% |
> | InterDigital [R1-2605686] | Cat 1 / Cat 2 / Cat 2.1 | ~5% | Single beam | 49.4%/3.9%/3.9% | 53.1%/5.9%/43.1% | 54.9%/6.9%/45.1% |
> | InterDigital [R1-2605686] | Cat 1 / Cat 2 / Cat 2.1 | ~25% | Single beam | 15.4%/1.6%/1.6% | 17.3%/2.4%/15.4% | 18.2%/2.9%/17.9% |
> | InterDigital [R1-2605686] | Cat 1 / Cat 2 / Cat 2.1 | ~5% | 4 beams | 48.4%/13.5%/13.5% | 58.7%/20.3%/49.2% | 63.8%/23.8%/53.7% |
> | InterDigital [R1-2605686] | Cat 1 / Cat 2 / Cat 2.1 | ~25% | 4 beams | 19.1%/7.3%/6.3% | 24.1%/9.7%/21.3% | 26.8%/11.5%/25.1% |
> | Huawei [R1-2605291] | Cat 1 | 0% / 4% / 8% | 8 beams, no AD-SS | baseline | 19% / 18% / 17% | 31% / 30% / 28% |
> | Huawei [R1-2605291] | Cat 1 | 0% / 4% / 8% | 4 beams, no AD-SS | baseline | 30% / 22% / 20% | 44% / 37% / 33% |
> | Huawei [R1-2605291] | Cat 1 | 0% / 4% / 8% | 8 beams, WITH AD-SS | baseline | 12% / 12% / 11% | 21% / 20% / 19% |
> | Huawei [R1-2605291] | Cat 1 | 0% / 4% / 8% | 4 beams, WITH AD-SS | baseline | 22% / 15% / 13% | 31% / 25% / 23% |
> | Nokia (R1- 2601832 | Cat 2 | 0% | SSB and SIB1 same periodicity and in consegutive slots, 8 beams | 27% | 41% | 48% |
> | Nokia (R1- 2601832) | Cat 2.1 | 0% | SSB and SIB1 same periodicity and in consegutive slots, 8 beams | 27% | 41% | 66% |
> | Xiaomi [R1-2605563] | Cat 1/Cat 2 | 0% | SS#0 period of 20ms, PO period of 1.28s, RO period of 10ms | 39.3%/9.3% | 45% / 13.1% | 49% / 15.9 |
> | Mid-band (~2–4 GHz), reference configuration Set 1 (TDD, FR1), 8 beams / 64 ports — NES gains vs 20 ms baseline | Mid-band (~2–4 GHz), reference configuration Set 1 (TDD, FR1), 8 beams / 64 ports — NES gains vs 20 ms baseline | Mid-band (~2–4 GHz), reference configuration Set 1 (TDD, FR1), 8 beams / 64 ports — NES gains vs 20 ms baseline | Mid-band (~2–4 GHz), reference configuration Set 1 (TDD, FR1), 8 beams / 64 ports — NES gains vs 20 ms baseline | Mid-band (~2–4 GHz), reference configuration Set 1 (TDD, FR1), 8 beams / 64 ports — NES gains vs 20 ms baseline | Mid-band (~2–4 GHz), reference configuration Set 1 (TDD, FR1), 8 beams / 64 ports — NES gains vs 20 ms baseline | Mid-band (~2–4 GHz), reference configuration Set 1 (TDD, FR1), 8 beams / 64 ports — NES gains vs 20 ms baseline |
> | MediaTek [R1-2606847] | Cat 1 / Cat 2 | Low (0 < L ≤ 15%) | SSB + SIB1 + RO, un-clustered | 17.2% / 4.6% | 37.7% / 7.7% | 49.9% / 9.3% |
> | MediaTek [R1-2606847] | Cat 1 / Cat 2 | Low (0 < L ≤ 15%) | No SIB1 (SSB + RO only), un-clustered | 26.6% / 9.5% | 43.0% / 10.5% | 52.9% / 11.1% |
> | MediaTek [R1-2606847] | Cat 1 / Cat 2 | Low (0 < L ≤ 15%) | SSB + SIB1 + RO, clustered | 13.0% / 2.4% | 30.8% / 2.6% | 44.4% / 1.4% |
> | MediaTek [R1-2606847] | Cat 1 / Cat 2 | Low (0 < L ≤ 15%) | No SIB1 (SSB + RO only), clustered | 22.1% / 6.5% | 36.1% / 5.1% | 46.7% / 3.4% |
> | MediaTek [R1-2606847] | Cat 1 / Cat 2 | Light (15 < L ≤ 30%) | SSB + SIB1 + RO, un-clustered | 8.1% / 2.8% | 15.2% / 4.2% | 19.9% / 5.0% |
> | MediaTek [R1-2606847] | Cat 1 / Cat 2 | Light (15 < L ≤ 30%) | No SIB1 (SSB + RO only), un-clustered | 12.6% / 5.3% | 18.1% / 6.3% | 22.1% / 5.7% |
> | MediaTek [R1-2606847] | Cat 1 / Cat 2 | Light (15 < L ≤ 30%) | SSB + SIB1 + RO, clustered | 1.2% / −2.4% | 4.5% / −5.1% | 11.2% / −6.3% |
> | MediaTek [R1-2606847] | Cat 1 / Cat 2 | Light (15 < L ≤ 30%) | No SIB1 (SSB + RO only), clustered | 5.3% / 0.4% | 6.9% / −3.0% | 13.0% / −4.6% |
> | MediaTek [R1-2606847] | Cat 1 / Cat 2 | Medium (30 < L ≤ 50%) | SSB + SIB1 + RO, un-clustered | 4.5% / 2.0% | 7.7% / 2.6% | 9.7% / 3.0% |
> | MediaTek [R1-2606847] | Cat 1 / Cat 2 | Medium (30 < L ≤ 50%) | No SIB1 (SSB + RO only), un-clustered | 7.3% / 3.8% | 10.1% / 4.6% | 11.6% / 3.4% |
> | MediaTek [R1-2606847] | Cat 1 / Cat 2 | Medium (30 < L ≤ 50%) | SSB + SIB1 + RO, clustered | −0.8% / −2.4% | 1.2% / −3.6% | 4.7% / −4.8% |
> | MediaTek [R1-2606847] | Cat 1 / Cat 2 | Medium (30 < L ≤ 50%) | No SIB1 (SSB + RO only), clustered | 2.0% / −0.2% | 3.0% / −1.6% | 6.1% / −3.0% |
> | Around 7 GHz (Set 4) — NES gains vs 20 ms baseline | Around 7 GHz (Set 4) — NES gains vs 20 ms baseline | Around 7 GHz (Set 4) — NES gains vs 20 ms baseline | Around 7 GHz (Set 4) — NES gains vs 20 ms baseline | Around 7 GHz (Set 4) — NES gains vs 20 ms baseline | Around 7 GHz (Set 4) — NES gains vs 20 ms baseline | Around 7 GHz (Set 4) — NES gains vs 20 ms baseline |
> | vivo [R1-2605459] | Cat 1 / Cat 2 / Cat 2.1 | 0% | N=1 (no repetition) | 36% / 24% / 24% | 68% / 36% / 36% | 83% / 43% / 63% |
> | vivo [R1-2605459] | Cat 1 / Cat 2 / Cat 2.1 | 0% | N=2 | 2% / 0% / 0% | 48% / 24% / 24% | 72% / 36% / 55% |
> | vivo [R1-2605459] | Cat 1 / Cat 2 / Cat 2.1 | 0% | N=4 | – | 4% / 0% / 0% | 50% / 23% / 39% |
> | CMCC [R1-2605631] | Cat 1 / Cat 2.1 | 0% | 8 beams | 34.7% / 23.1% | 52.9% / 33.6% | 69.4% / 51% |
> | NTT DOCOMO [R1-2606501] | Cat 1 / Cat 2 | 10% | Clustered signal + clustered data occasions | 53% / 46% | 70% / 56% | 77% / 60% |
> | CATT [R1-2605717] | Cat 1 | 0% | L=4 beams | – | 76.6% | 87.1% |
> | CATT [R1-2605717] | Cat 1 | 0% | L=8 beams | – | 75.6% | 86.8% |
> | Huawei [R1-2605291] | Cat 1 | 0% / 4% / 8% | 8 beams, no AD-SS | baseline | 16% / 15% / 9% | 25% / 22% / 15% |
> | Huawei [R1-2605291] | Cat 1 | 0% / 4% / 8% | 16 beams, no AD-SS | baseline | 6% / 5% / 5% | 14% / 13% / 12% |
> | Huawei [R1-2605291] | Cat 1 | 0% / 4% / 8% | 8 beams, WITH AD-SS | baseline | 10% / 5% / 4% | 15% / 13% / 11% |
> | Huawei [R1-2605291] | Cat 1 | 0% / 4% / 8% | 8 beams, no AD-SS | baseline | 16% / 15% / 9% | 25% / 22% / 15% |
> | Band not stated — NES gains vs 20 ms baseline | Band not stated — NES gains vs 20 ms baseline | Band not stated — NES gains vs 20 ms baseline | Band not stated — NES gains vs 20 ms baseline | Band not stated — NES gains vs 20 ms baseline | Band not stated — NES gains vs 20 ms baseline | Band not stated — NES gains vs 20 ms baseline |
> | Apple [R1-2606022] | Cat 1 / Cat 2 / Cat 2.1 | 0% | — | 32.7% / 21.9% / 21.9% | 61.3% / 32.8% / 32.8% | 79.7% / 38.2% / 56.3% |
> | Apple [R1-2606022] | Cat 1 / Cat 2 / Cat 2.1 | 9.8% | — | 24.5% / 17.2% / 17.2% | 43.8% / 25.8% / 25.8% | 56.1% / 30% / 38.7% |
> | Apple [R1-2606022] | Cat 1 / Cat 2 / Cat 2.1 | 22% | — | 16.6% / 12.5% / 12.5% | 28.8% / 18.7% / 18.7% | 36.3% / 21.8% / 26.2% |

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Synchronization and Beam Measurement]`

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#126:10.5.1.1:014`

> For SSB transmission, study
> Option 1:
> For a given frequency band, a single set of values for {X, Y, M} is predefined in default 6GR SSB periodicity
> - Non-adjustable number of repetitions of transmitted SSBs
> Note: for discussion purpose,
> - X: the max number of candidate 6GR SSBs in a 6GR SSB burst
> - Y: the max number of candidate 6GR SSB burst(s) in a default 6GR SSB periodicity
> - M: the max number of candidate 6GR SSB repetitions within a default 6GR SSB periodicity
> Option 2:
> For a given frequency band, a single set of values for {X, Y, M} is predefined in default 6GR SSB periodicity and the actual number of repetitions of transmitted SSBs can be adjusted by the aNB
> - FFS: how to adjust the actual number of repetitions of transmitted SSBs including potential restrictions
> Note: for discussion purpose,
> - X: the max number of candidate 6GR SSBs in a 6GR SSB burst
> - Y: the max number of candidate 6GR SSB burst(s) in a default 6GR SSB periodicity
> - M: the max number of candidate 6GR SSB repetitions within a default 6GR SSB periodicity

남은 FFS 1건

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Synchronization and Beam Measurement]`

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#126:10.5.1.1:015`

> RAN1 to study and evaluate the following solutions
> - Option 1:
>   - SSB repetition within one SSB period and UE is assumed to at least support SSB combining within one SSB period
>   - 160 ms default SSB periodicity for initial cell search
> - Option 2:
>   - SSB repetition within one SSB period and UE is assumed to at least support SSB combining within one SSB period
>   - 80 ms default SSB periodicity for initial cell search
> - Option 3:
>   - UE is assumed to at least support SSB combining across different SSB periods
>   - 40 ms default SSB periodicity for initial cell search
> - Option 4:
>   - SSB repetition within one SSB period and UE is assumed to at least support SSB combining within one SSB period and support SSB combining across different SSB periods
>   - 40 ms default SSB periodicity for initial cell search
> - Option 5:
>   - UE is assumed to at least support SSB combining across different SSB periods
>   - 20 ms default SSB periodicity for initial cell search
> To mitigate the UE impact with longer SSB periodicity in Option 1/2/3/4, RAN1 to study the following solutions
> - Solutions to reduce cell search complexity and latency
> - Additional synchronization signals
> - Clustered allocations of SSB, SIB1 and paging
> - Other solutions are not precluded
> FFS: Additional configurable SSB periodicities

남은 FFS 1건

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Synchronization and Beam Measurement]`

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#126:10.5.1.1:016`

> Draft LS R1-2606890 is endorsed in principle.
> Final LS R1-2606891 is endorsed.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Synchronization and Beam Measurement]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126:10.5.3.1:017`

> For the study of explicit CSI feedback, the evaluation considers the following aspects:
> - Form of explicit CSI
>   - Opt-A: information facilitating NW reconstruction of the channel matrix H (e.g., NRX x NTX) per frequency granularity unit
>     - Note:  NRX does not necessarily mean the number of UE Rx physical antenna(s)
>   - Opt-B: information facilitating NW reconstruction of H’H per frequency granularity unit
>   - Companies to report compression/quantization scheme used for the evaluation
> - Handling of link adaptation via at least one of the following options
>   - Opt-1: CQI/RI information in another report (e.g., based on CSI-RS or DMRS)
>   - Opt-2: Assistance information (e.g., L1-SINR, L1-RSRP, Interference-plus-noise (IpN) information) in the same explicit CSI report or another report
>   - Opt-3: the explicit feedback considering pre-whitening channel or channel covariance
>   - Note: other options are not precluded.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126:10.5.3.1:020`

> For the evaluation on the benefit of early CSI triggering/reporting, considering the following aspects:
> - Potential scenarios/use cases:
>   - UE transition from IDLE/INACTIVE to CONNECTED mode,
>   - During activation of serving cells /carriers
>   - Mobility
>   - Note: Early beam report is to be discussed separately
>   - Other use cases are not precluded.
> - For each potential use case, studying details of
>   - Report quantities for each use case
>   - RS for measurement
>   - Benchmark
>   - KPI
> - Note: Strive to minimize Msg 1 impact.
> - Note: Both measured and predicted CSI can be considered, if appliable.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.4` Beam management for downlink and uplink · `RAN1#126:10.5.3.4:001`

> For the study on requirement/functionality of DL RS for beam measurement, for inter-symbol NW/UE-side beam sweeping, the following is considered:
> - Study the following time-domain behavior of DL RS for beam measurement: aperiodic, semi-persistent and periodic.
> - At least support the functionality for UE to assume whether DL RSs are transmitted with same DL Tx spatial filter(s) or not.
> - Note: Sync-signal design is not considered herein
> - At least following aspects to be considered for DL RS for beam measurement:
>   - UE complexity,
>   - Energy efficiency,
>   - RS overhead,
>   - Measurement performance, and corresponding coverage.
>   - Beam measurement/sweeping latency
>   - Multiplexing with other data and RS

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Beam management]`

**Agreement** · `10.5.3.4` Beam management for downlink and uplink · `RAN1#126:10.5.3.4:002`

> Regarding QCL framework,
> - At least support the following QCL properties for DL:
>   - Doppler shift, Doppler spread, average delay, delay spread, and spatial Rx parameter
>   - FFS: Whether/how to introduce average gain as a QCL property.
>   - FFS: Other QCL properties
> - FFS: Where/how/when to use above QCL properties.
> - FFS: Source QCL-RS

남은 FFS 4건

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Beam management]`

**Agreement** · `10.5.3.4` Beam management for downlink and uplink · `RAN1#126:10.5.3.4:003`

> Regarding UE initiated beam management, at least the following procedure can be considered
> - Event detection for triggering UL transmission
> - UL transmission procedure
> - NW response, if any, to UL transmission procedure
>   - UE behavior, if any, after receiving NW response.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Beam management]`

**Agreement** · `10.5.3.4` Beam management for downlink and uplink · `RAN1#126:10.5.3.4:004`

> Regarding UE initiated beam management, at least for a single-TRP operation, on event detection for triggering UL transmission, the following can be studied for Event-1 and Event-2.
> - Event evaluation metric/threshold,
> - Current/serving DL RS determination,
> - Candidate DL RS identification, if applicable.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Beam management]`

**Agreement** · `10.5.3.4` Beam management for downlink and uplink · `RAN1#126:10.5.3.4:005`

> For the study on beam measurement and report regarding DL beam measurement and report procedure on DL RS(s) for multi-TRP scenario(s), the following can be considered on Case-1:
> - Regarding L1-RSRP calculation, NR L1-RSRP definition can be used as the starting point.
>   - FFS: Whether any other extension of L1-RSRP definition is needed, e.g., TRP-specific or port-specific L1-RSRP.
> - Regarding RS measurement requirements,
>   - Study the need of a functionality of enabling UE to a) differentiate DL RSs from different TRPs within a cell, or b) differentiate DL RSs across cells for DL beam measurement and report.
> - Regarding report content/format,
>   - Information of identifying DL RS can be included in the report as a starting point, besides for L1-RSRP
>   - FFS: the following report content can be studied:
>     - N DL RSs per selected TRP or per measured TRP
>     - M DL RSs across different TRPs
>   - FFS: Whether/How to include the information of selected TRP in the report.
>   - FFS: other metrics, e.g., L1-SINR.
> - Note (Case-1): To identify/report the preferred N>1 DL beams per NW TRP/panel or across NW TRP(s)/panel(s) for supporting multi-TRP/panel transmission scheme(s).
> - Note: Above TRPs may belong to a same cell or different cells.
> - Note (for the study purpose): The above study at least considers the following transmission schemes: TDMed and DPS transmission scheme, if supported.

남은 FFS 4건

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Beam management]`

**Agreement** · `10.5.3.4` Beam management for downlink and uplink · `RAN1#126:10.5.3.4:006`

> For the study on spatial/temporal/frequency domain beam measurement/prediction (relevant to AI/ML or non-AI/advanced schemes), the following is considered:
> - Regarding spatial/temporal domain DL Tx beam prediction and management on multi-TRP/cell(intra/inter-cell), at least support the case that the cells/TRPs corresponding to the predicted beam(s) (Set-A) are within the set of cells/TRPs corresponding to the measured beam(s) (Set-B).
>   - FFS: Other cases that the case that at least one of the cells/TRPs corresponding to the predicted beam(s) (Set-A) are outside the set of cells/TRPs corresponding to the measured beam(s) (Set-B).
> - Regarding frequency domain beam measurement/prediction (cross-frequency), at least support the collocated scenarios of source and target frequencies (using same height of NW antenna(s)).
>   - FFS: Non-collocated scenarios of source and target frequencies.
> - FFS: How to ensure the training and inference consistency for UE-side model, e.g., association ID.
> - FFS: Whether/how to indicate the combination coefficient(s), W, between measured beams (set B) for computation of the target beams (set A), e.g., matrix-based approach (from NW to UE).
>   - Predicted results of Set-A is derived based on W and measured results of Set-B
> - FFS: Report content
>   - Whether/how to report confidence level associated with reported beam, e.g., inaccurate, invalid prediction

남은 FFS 5건

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Beam management]`

**Agreement** · `10.5.3.4` Beam management for downlink and uplink · `RAN1#126:10.5.3.4:007`

> - Study target usage/necessity and procedure of UE UL beam sweeping
> - From RAN1 perspective, as a baseline, Tx beam of UL channel/RS may be determined according to DL-RS.
>   - Note: UE beam correspondence is assumed RAN1
> - Send an LS to RAN4

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Beam management]`

**Agreement** · `10.5.3.4` Beam management for downlink and uplink · `RAN1#126:10.5.3.4:008`

> Draft LS R1-2606909 is endorsed in principle.
> Final LS R1-2606910 is endorsed.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Beam management]`

**Agreement** · `10.5.3.4` Beam management for downlink and uplink · `RAN1#126:10.5.3.4:009`

> Regarding UE initiated beam management, on a single-TRP operation, on UL transmission procedure, the following can be studied for Event-1 and Event-2.
> - Candidate-1a: First UL channel + Second UL channel
>   - First channel (e.g., PUCCH, PRACH) is to at least notify event occurrence;
>   - Second channel (e.g., PUSCH) is to carry a beam report
> - Candidate-1b: First UL channel + SRS
>   - First channel (e.g., PUCCH) is to at least notify event occurrence;
>   - SRS can be used for NW DL-Tx/UL-Rx beam determination.
> - Candidate-2a: First UL channel at least notifying event occurrence
>   - First UL channel can be PUCCH, PUSCH, or PRACH.
> - Candidate-2b: SRS used for NW DL-Tx/UL-Rx beam determination

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Beam management]`

**Agreement** · `10.5.3.4` Beam management for downlink and uplink · `RAN1#126:10.5.3.4:010`

> For network-initiated beam reporting in 6GR,
> - Study the following time-domain behavior of beam reporting: aperiodic, semi-persistent, periodic.
> - Support DL RS identifier as another report quantity in a beam report, when applicable.
>   - Note: DL RS may be measured or predicted by the UE.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Beam management]`

**Agreement** · `10.5.3.4` Beam management for downlink and uplink · `RAN1#126:10.5.3.4:011`

> Regarding DL beam measurement and report procedure, for the study on NW determination of refined analog beam(s), including the feasibility and necessity, the following is considered:
> - Potential use cases:
>   - To improve beam-forming gain/throughput via generating NW refined analog beam(s) based on UE report which may be different from measured beams
> - Studying the details of:
>   - Benchmark: Companies report the benchmark in evaluation.
>     - Benchmark #1 Beam selection from a set of measured beams
>     - Benchmark #2 Beam selection from a set of measured beams plus candidate analog beams (for subsequent transmission)
>   - RS measurement requirements
>   - Potential report content (based on the measured beams):
>   - Applicable frequency range
>   - Others are not precluded.
> - Note: NW implementation information is not disclosed.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Beam management]`

**Agreement** · `10.5.3.4` Beam management for downlink and uplink · `RAN1#126:10.5.3.4:012`

> Regarding NW initiated beam indication, study transmission configuration indicator (TCI) framework involving both joint and separate DL/UL TCI state(s) for both single-TRP/cell/carrier and multi-TRP/cell/carrier operations
> - Regarding joint-DL/UL TCI state(s), study joint-DL/UL TCI state(s) at least apply to PDSCH, and PUSCH;
>   - FFS: what other target channel(s)/RS(s) which shall/can follow the TCI state, including CSI-RS, SRS, PDCCH, PUCCH and PRACH
> - Regarding separate DL/UL TCI state, study the following
> - DL-TCI state(s) at least apply to PDSCH;
>   - FFS: The target channel(s)/RS(s) which shall/can follow the DL-TCI state, including CSI-RS, and/or PDCCH
> - UL-TCI state(s) at least apply to PUSCH;
>   - FFS: The target channel(s)/RS(s) which shall/can follow the UL-TCI state, including SRS, and PRACH, and/or PUCCH
> - FFS: At least for joint-DL/UL TCI state/DL-TCI state, one state comprises at least one source QCL-RS, and each source QCL-RS is associated with at least one QCL property.
>   - The joint-DL/UL TCI state can also used for determining UL TX beam
>   - FFS: Other transmission parameter(s) for DL and UL associated with the TCI state (e.g., power control parameters, TAG, etc), besides for QCL properties.
> - FFS: At least for UL-TCI state, one state comprises at least one reference signal, if applicable, for determining UL TX beam.
>   - FFS: Other transmission parameter(s) for UL associated with the TCI state (e.g., power control parameters, TAG, etc), besides for UL TX beam.
> Note: TCI state is for the purpose of discussion

남은 FFS 7건

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Beam management]`

## RAN1#125 — 22건

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#125:10.5.1.1:001`

> Design of the common signals/channels (at least for SSB) for initial access by assuming bandwidth larger than 3MHz with 15kHz SCS, which is applicable to any spectrum allocations with adjustment, if applicable
> Note: at least bandwidth of SSB larger than 5G NR should be well justified.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx)

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#125:10.5.1.1:002`

> For idle mode mobility,
> - At least 6GR SSS of 6GR SSB is supported as measurement resource.
>   - FFS other signal in addition (e.g. other types of 6GR sync signal or reference signal, DMRS of PBCH)
> - For measurement metric, at least RSRP is supported, FFS
>   - RSRQ and the default SS-RSRQ definition if supported,
>   - SINR,
> and select one of those two in addition to RSRP

남은 FFS 1건

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx)

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#125:10.5.1.1:003`

> Study the following options for 6GR SSB time-domain structure
> - Option 1: one 6GR SSB spans X (4<=X<=7) symbols within a slot
>   - Option 1-1:  one 6GR SSB spans 4 symbols within a slot
>   - Option 1-2:  one 6GR SSB spans X (4<X <=7) symbols within a slot
> - Option 2: one 6GR SSB spans Y (7<Y<=12) symbols within a slot

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx)

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#125:10.5.1.1:004`

> For the purpose of discussing 6GR SSB burst pattern and associated default SSB periodicity, study the following:
> - The max number of candidate 6GR SSBs in a 6GR SSB burst: X
> - The max number of candidate 6GR SSB burst(s) in a default 6GR SSB periodicity: Y
> - The max number of candidate 6GR SSB repetitions within a default 6GR SSB periodicity: M
> - Default SSB periodicity for initial cell selection: T
> - The max number of default 6GR SSB periodicities (similar as what is assumed for evaluation in 5G NR performance) for UE performing 6GR SSB combining: N
> - Note: As an example, for NR in 3.5 GHz, X = 8, Y = 1, M = 1, N = 4, T = 20ms.
> For the study on the values of X, Y, Nand M for a given default SSB periodicity T, at least SSB detection performance, UE complexity, UE measurement aspects should be considered.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx)

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#125:10.5.1.1:005`

> For the study of 6GR SSB performance, the following can be assumed
> - Alt.1: Combining is performed across all 6GR SSB repetitions within a 6GR SSB burst in case of intra-burst repetition within an SSB periodicity
> - Alt.2: Combining is performed across all 6GR SSB repetitions across 6GR SSB bursts in case of inter-burst repetition (Y>1) within a SSB periodicity
> - Alt.3: Combining is performed across all 6GR SSBs within a 6GR SSB burst
> - Alt.4: Combining is performed across different SSB periodicities
> - Alt.5: Combining is not performed across 6GR SSBs within a SSB periodicity when M = 1
> - Alt.6: Combination of above alternatives
> Note: To compare different 6GR SSB burst patterns, the same total number of SSBs (X*Y*N) within N*T are assumed.
> Note: The above assumptions are only for evaluation purpose and do not mandate UE implementations.
> Note: Companies to report which combining(s) is/are assumed in the study.
> Note: Companies to report the combining details and assumptions
> Note: Companies to report the burst pattern design details, e.g. the duration of the SSB burst, interval between different SSB burst.
> Note: SSB performance, UE complexity, UE measurement aspects should be considered.
> Note: Companies to report other related assumptions, e.g., whether power boosting is applied.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx)

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#125:10.5.1.1:006`

> As a baseline, the number of 6GR physical cell IDs is 1008
> - FFS: Motivation to extend or reduce the number of PCI

남은 FFS 1건

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx)

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#125:10.5.1.1:007`

> 6GR synchronization signals (PSS and SSS) in 6GR SSB carry full PCI information as baseline
> - FFS: Motivation to carry other information
> - FFS: Motivation to carry part of PCI information by other signals, e.g., PBCH DMRS, if 6GR synchronization signals carry part of PCI information

남은 FFS 2건

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx)

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#125:10.5.1.1:008`

> For initial access procedures starting from initial cell search and cell search of reselection till the completion of random access in multi-TRP based deployments, study the following options
> - Option 1: Multiple TRPs are transparent to the UE, and corresponding definition about what transparent Multiple TRPs mean
> - Option 2: Multiple TRPs are non-transparent to the UE, and corresponding definition about what non-transparent Multiple TRPs mean
> Note: Companies are encouraged to study the coverage performance, network energy saving, the associated signalling overhead, access latency, UE complexity, and compatibility with single-TRP deployments for both options.
> Note: RACH related procedure/behaviour will be discussed under AI 10.5.1.2

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx)

**Agreement** · `10.5.2.4` Beam management for downlink and uplink · `RAN1#125:10.5.2.4:001`

> Support the following table as the assumption of SLS for evaluation of 6GR beam management:
> | Parameter | Value |
> | #6 BS Antenna Configuration | Reuse the agreed configuration(s) from 6GR air interface evaluation assumptions For 30GHz, the following can be further considered: (M, N, P, Mg, Ng; Mp, Np) = (8, 16, 2, 1, 1; 1, 1), or (16, 32, 2, 1, 1; 1, 1)), (dH, dV) = (0.5, 0.5); |
> | #14 UE Antenna Configuration | 4GHz & 7GHz: Reuse the agreed configuration(s) from 6GR air interface evaluation assumptions; 30GHz: Reuse the agreed configuration(s) from 6GR air interface evaluation assumptions: For one-panel, (M, N, P, Mg, Ng; Mp, Np) = (4, 1, 2, 1, 1; 1, 1) is considered as a baseline For multi-panel, (M, N, P; Mp, Np) = (2, 2, 2; 1, 1) is considered as a baseline. |

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Beam management]`

**Agreement** · `10.5.2.4` Beam management for downlink and uplink · `RAN1#125:10.5.2.4:002`

> Regarding the scenario of high-speed train, support the following revision in red on the agreement for SLS evaluation assumption of 6GR beam management:
> | Parameter | Value |
> | #11 Multi-TRP operation | Reuse the assumptions for multi-TRP scenarios of DL-based CSI (A.I. 10.5.3.1) with the following interpretation except for high-speed train scenario: The maximum number of coordinated TRP(s) = {1, 2, 3, 4}, and other larger value(s) are not precluded Backhaul: ideal (baseline) or non-ideal; sync: ideal (baseline) or non-ideal; FFS: Other update for high-speed train Regarding high-speed train scenario, reuse the assumptions of downlink/uplink transmission schemes (10.5.2.2/3) Maximum number of coordinated TRPs is 2, 4, 8 or 16 Other number of coordinated TRPs are not precluded |
> | #33 CSI Feedback | CSI periodicity: 10ms, 20ms (baseline), 40ms, 80ms, 160ms FFS: Other update for high-speed train |
> | #37 Layout/deployment | Reuse the assumptions of uplink/downlink transmission schemes (10.5.2.2/3) 7 x 3, single layer, hex grid (baseline) 7 x 3 two layers, macro layer: hex grid; micro layer: locations of micro sites are reported by company (optional) 19 x 3, single layer, hex grid (optional) FFS: Other update for high-speed train Regarding high-speed train, reuse the assumptions of downlink/uplink transmission schemes (10.5.2.2/3) Regarding around 4 and 7 GHz, rural macro, 500 m or 1732 m ISD between RRH sites, two TRxPs per RRH site, one or more RRH sites connected to a BBU, with RRH site to railway track distance: 100 m Inter-track distance: 6 m Train length: 400 m Train width: 3.38 m Regarding around 30 GHz, rural macro, 500 m or 1732 m between BBU sites, one or more RRH sites connected to 1 BBU, one TRxP per RRH site, with RRH site to railway track distance: 5 m Inter-RRH site distance: [580 m, 580 m, 572 m] Inter-track distance: 6 m Train length: 400 m Train width: 3.38 m |

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Beam management]`

**Agreement** · `10.5.2.4` Beam management for downlink and uplink · `RAN1#125:10.5.2.4:003`

> Support the following table as the basic assumption of LLS for evaluation of 6GR beam management:
> | Parameter | Value |
> | #7 NW Antenna Config | Reuse the agreed configuration(s) from 6GR air interface evaluation assumptions For 30GHz, the following can be further considered: (M, N, P, Mg, Ng; Mp, Np) = (8, 16, 2, 1, 1; 1, 1), or (16, 32, 2, 1, 1; 1, 1)), (dH, dV) = (0.5, 0.5); |
> | #14 UE Antenna Configuration | 4GHz & 7GHz: Reuse the agreed configuration(s) from 6GR air interface evaluation assumptions; 30GHz: Reuse the agreed configuration(s) from 6GR air interface evaluation assumptions: For one-panel, (M, N, P, Mg, Ng; Mp, Np) = (4, 1, 2, 1, 1; 1, 1) is considered as a baseline For multi-panel, (M, N, P; Mp, Np) = (2, 2, 2; 1, 1) is considered as a baseline. |

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Beam management]`

**Agreement** · `10.5.2.4` Beam management for downlink and uplink · `RAN1#125:10.5.2.4:004`

> Study QCL framework, including QCL property, QCL relationship/chain between source QCL-RS(s) and target channel(s)/RS(s).
> - Study the following QCL properties at least for DL as a starting point:
>   - Doppler shift, Doppler spread, average delay, delay spread, average gain, spatial Rx parameter
>   - Note: The above does not necessarily mean that the above is a part of QCL properties by default.
> - Study source QCL-RS(s) w.r.t. QCL properties of each target channel/RS
>   - Each target channel/RS can be associated with at least one source QCL-RS as a baseline
>     - Study whether/how to introduce more than one source QCL-RS w.r.t. a same QCL property for a target channel/RS
>     - Study whether/how to introduce more than one source QCL-RS w.r.t different QCL properties for a target channel/RS
> - Study QCL relationship for multi-carrier/TRP/cell scenarios

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Beam management]`

**Agreement** · `10.5.2.4` Beam management for downlink and uplink · `RAN1#125:10.5.2.4:005`

> For UE-initiated beam management in 6GR, study the following as an event evaluation metric as starting point.
> -        measured or predicated L1-RSRP
> -        L1-SINR
> -        Hypothetical BLER.
> For UE-initiated beam management in 6GR, study the following as report metric for beam reporting if applicable as starting point.
> -        measured or predicated L1-RSRP
> -        L1-SINR

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Beam management]`

**Agreement** · `10.5.2.4` Beam management for downlink and uplink · `RAN1#125:10.5.2.4:006`

> On NW-initiated beam management, regarding DL beam measurement and report procedure on DL RS(s) for both single-TRP/cell/carrier and multi-TRP/cell/carrier scenario(s), the following aspects on DL beam measurement can be studied
> - Study the procedure of beam sweeping considering the following alternatives:
>   - At least support inter-symbol NW/UE-side beam sweeping including multiple DL RS(s) for DL Tx beam sweeping/repetition.
>   - Whether/how to support the following on intra-symbol beam sweeping
>     - Frequency-domain/FDMed at least for NW Tx beam sweeping: multiple DL RS(s) for beam measurement are multiplexed in/associated with different frequency resource(s)
>     - Sequence-domain/CDMed at least for NW Tx beam sweeping: multiple DL RS(s) for beam measurement are multiplexed with different sequence (e.g., sequence root, or CDMed);
>     - Sub-symbol/TDMed at least for UE Rx beam sweeping: each sub-symbol (e.g., time-domain multiplexing within a symbol) is measured by a respective Rx beam;
>       - Note: ‘Sub-symbol’ is just for discussion purpose, which does not imply whether to introduce any new terminologies.
>   - Note: UE-side beam sweeping is applied to the case of Rx multi-beam in FR2.
> - Note: Granularity of DL RS can be further discussed.
> - Study functionality requirement on DL RS measurement
>   - Per DL measurement or across DL measurement(s), the following can be considered:
>     - The maximum number of TRPs (within a cell or across cell)/cells/carriers
>     - The maximum number of DL Tx beams per TRP/cell/carrier
>     - The maximum number of DL Tx beams across measured TRPs/cells/carriers
> - At least following aspects to be considered for designing the procedure of beam sweeping/tracking:
>   - Increase of the number of coordinated TRPs/beams-per-TRP compared with 5G-NR
>   - Hybrid/analog beam-forming architecture in NW
>   - Latency/RS overhead for beam sweeping/tracking

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Beam management]`

**Agreement** · `10.5.2.4` Beam management for downlink and uplink · `RAN1#125:10.5.2.4:007`

> Support the following table as the assumption of SLS for evaluation of 6GR beam management
> - Revise the RAN1#124-bis agreement as follows:
> | Parameter | Value |
> | #1 Scenario (Carrier frequency) | Indoor hotspot, Urban macro, Dense urban (one-layer, and two-layer), High Speed Train, SMa, Urban grid, 4 GHz, TDD 7 GHz, TDD 30 GHz, TDD Other scenarios are not precluded (companies to report) |
> | #2 Mode | DL/UL SU-MIMO/MU-MIMO |
> | #3 System BW | 4GHz: 20MHz 7GHz: 100 MHz 30GHz: 100 MHz |
> | #4 Subcarrier spacing for data | 4GHz/7GHz: 30KHz; 30GHz: 120 KHz |
> | #5 Channel model | TR 38.901 with the following features, if needed: Spatial consistency, including Autocorrelation of shadow fading (Section 7.4.4 in TR 38.901) Correlation modeling for multi‑frequency simulations. Near-field characters Spatial non-stationarity |
> | #6 BS Antenna Configuration | Reuse the agreed configuration(s) from 6GR air interface evaluation assumptions For 30GHz, the following can be further considered: (M, N, P, Mg, Ng; Mp, Np) = (8, 16, 2, 1, 1; 1, 1), or (16, 32, 2, 1, 1; 1, 1)), (dH, dV) = (0.5, 0.5); |
> | #7 BS array orientation | Mechanical tilt: 180° in GCS for indoor hotspot; 90° in GCS for Urban Macro, Dense Urban and High Speed Train Electrical tilt: Company to report Other mechanical tilts are not precluded (companies to report) |
> | #8 TXRU mapping to antenna elements | A single TXRU is mapped per panel per subarray per polarization. Others are not precluded (companies to report). |
> | #9 Beam-forming scheme | Companies explain the details, e.g., DFT-based or Eigen-based |
> | #10 Procedure of beam sweeping | Companies explain the details |
> | #11 Multi-TRP operation | Reuse the assumptions for multi-TRP scenarios of DL-based CSI (A.I. 10.5.3.1) with the following interpretation except for high-speed train scenario: The maximum number of coordinated TRP(s) = {1, 2, 3, 4}, and other larger value(s) are not precluded Backhaul: ideal (baseline) or non-ideal; sync: ideal (baseline) or non-ideal; FFS: Other update for high-speed train Regarding high-speed train scenario, reuse the assumptions of downlink/uplink transmission schemes (10.5.2.2/3) Maximum number of coordinated TRPs is 2, 4, 8 or 16 Other number of coordinated TRPs are not precluded |
> | #12 Criteria for selection for serving TRP(s) | Serving TRP selection with objective of maximizing RSRP is considered as baseline, and other criteria is not precluded and up to companies to report. For TRP switching, it is up to companies to report the TRP selection margin, if any. |
> | #13 Criteria for beam selection for serving TRP(s) | Beam selection with objective of maximizing RSRP is considered as baseline, and other criteria is not precluded and up to companies to report. |
> | #14 UE Antenna Configuration | 4GHz & 7GHz: Reuse the agreed configuration(s) from 6GR air interface evaluation assumptions; 30GHz: Reuse the agreed configuration(s) from 6GR air interface evaluation assumptions: For one-panel, (M, N, P, Mg, Ng; Mp, Np) = (4, 1, 2, 1, 1; 1, 1) is considered as a baseline For multi-panel, (M, N, P; Mp, Np) = (2, 2, 2; 1, 1) is considered as a baseline. |
> | #15 UE array orientation | Ω‌UT,a uniformly distributed on [0, 360] deg, Ω‌UT,b = 0 deg, Ω‌UT,g = 0 deg is considered as a baseline. Others are not precluded (companies to report) |
> | #16 Beam correspondence | Ideal (baseline) or non-ideal. Others are not precluded. |
> | #17 Link adaptation | Based on CSI-RS (Adaptive Modulation and Coding, AMC) |
> | #18 UE receiver type | MMSE-IRC as baseline; other advanced receivers are not precluded |
> | #19 BS Tx Power | Reuse the configuration(s) from 6GR air interface evaluation assumptions |
> | #20 Maximum UE Tx Power | Reuse the configuration(s) from 6GR air interface evaluation assumptions |
> | #21 Inter site distance | Reuse the configuration(s) from 6GR air interface evaluation assumptions, besides for the following: High Speed Train: 1732 m ISD |
> | #22 UE antenna element radiation pattern | Reuse the configuration(s) from 6GR air interface evaluation assumptions |
> | #23 UE Speed and UE distribution | Reuse the configuration(s) from 6GR air interface evaluation assumptions, besides for the following: High Speed Train: 100% outdoor in train (up to 500km/h) |
> | #24 UE rotation | No UE rotation (baseline). UE rotation is not precluded and the corresponding rotation speed is up to companies to report. |
> | #25 BS Antenna height | Dense urban macro and Urban Macro: 25 m; Dense urban micro: 10 m; Indoor: 3m |
> | #26 UE Antenna height | Section 7.2 in TR 38.901. Others are not precluded (companies to report). |
> | #27 Car penetration Loss | TR 38.901, sec 7.4.3.2: μ = 9 dB, σp = 5 dB |
> | #28 Building penetration loss (O2I) | Table 7.4.3-2 in TR 38.901 |
> | #29 UE mobility feature (optional) | Baseline: Random direction straight-line trajectories (from 38.843, Option-3) - Initial UE location, moving direction and speed: UE is randomly dropped in a cell, and an initial moving direction is randomly selected, with a fixed speed. - The initial UE location should be randomly drop within the following blue area: where d1 is the minimum distance that UE should be away from the BS. Each sector is a cell and that the cell association is geometry based. Company to report whether inter-cell handover or switching is disabled during the simulation. Company to report whether the trajectory should be terminated (e.g., single-TRP) or be retained (e.g., multi-TRP), if the UE trajectory hits the site boundary (the hexagonal grid) Other UE mobility model(s), e.g., EVM for NR ICBM, linear trajectory model with random and smooth direction change (i.e., TR38.843, Option-2), are not precluded (companies to report). |
> | #30 Scheduling algorithm | PF scheduler |
> | #31 MCS | Use NR MCS |
> | #32 Traffic Model | FTP model 1/3 with packet size 0.5 Mbytes (other value is not precluded) Other traffic models are not precluded (companies to report). Full buffer (Optional) |
> | #33 CSI Feedback | CSI periodicity: 10ms, 20ms (baseline), 40ms, 80ms, 160ms FFS: Other update for high-speed train |
> | #34 Resource Utilization | 30%, 50%, 70% (optional) |
> | #35 Prediction parameter | Company can report assumption for set-A and set-B, prediction window and any extension for intra-/inter-cell/multi-TRP measurement Set A: M*N M: {8, 16, 32, 64, 256,1024}. N: {1, 2, 3, 4}. Ratio of the size of Set-B to Set-A: {1, 1/2, 1/4, 1/8, 1/16, 1/32} For multi-TRP, Set-A and Set-B can contain beams across TRP(s). Other values for M, N and ratio are not precluded. Set A/Set B combinations: Alt1: Set B is different from Set A Alt2: Set B is a subset of Set A Alt3: Set B is the same as Set A Regarding temporal domain prediction, the following can be considered: Time gap between neighboring predicted time instances: {20ms, 40ms, 80ms, 120ms, 160ms, 200ms}. Predicted time instances: {1, 2, 4, 8}. Measured time instances: companies to report. Other values for the above are not precluded Other prediction mechanism is not precluded and up to companies’ report. |
> | #36 UE number/cell | Reuse the configuration(s) from 6GR air interface evaluation assumptions |
> | #37 Layout/deployment | Reuse the assumptions of uplink/downlink transmission schemes (10.5.2.2/3) 7 x 3, single layer, hex grid (baseline) 7 x 3 two layers, macro layer: hex grid; micro layer: locations of micro sites are reported by company (optional) 19 x 3, single layer, hex grid (optional) FFS: Other update for high-speed train Regarding high-speed train, reuse the assumptions of downlink/uplink transmission schemes (10.5.2.2/3) Regarding around 4 and 7 GHz, rural macro, 500 m or 1732 m ISD between RRH sites, two TRxPs per RRH site, one or more RRH sites connected to a BBU, with RRH site to railway track distance: 100 m Inter-track distance: 6 m Train length: 400 m Train width: 3.38 m Regarding around 30 GHz, rural macro, 500 m or 1732 m between BBU sites, one or more RRH sites connected to 1 BBU, one TRxP per RRH site, with RRH site to railway track distance: 5 m Inter-RRH site distance: [580 m, 580 m, 572 m] Inter-track distance: 6 m Train length: 400 m Train width: 3.38 m |
> | #38 Inter-cell interference model | Reuse the assumptions of DL-based CSI (10.5.3.1) Explicitly and realistically modelled |
> | #39 Metric | Top-K/1 beam prediction accuracy (with or without L1-RSRP margin), average/5%-ile UPT/throughput, SINR/RSRP, L1-RSRP/SINR difference between Top-1 predicted beam and genie-aided beam, RS overhead reduction, beam management latency, and/or number of model-parameter(s)/model computational complexity. Companies can report other performance metrics Companies report the assumption of transmission scheme, if UPT/throughput is reported. |

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Beam management]`

**Agreement** · `10.5.2.4` Beam management for downlink and uplink · `RAN1#125:10.5.2.4:008`

> Support the following table as the assumption of LLS for evaluation of 6GR beam management
> - Revise the RAN1#124-bis agreement as follows:
> | Parameter | Value |
> | #1 Carrier Frequency | 4GHz, 7GHz, 30GHz |
> | #2 Duplex / Waveform | TDD/CP-OFDM |
> | #3 Subcarrier Spacing | For 4GHz/7GHz: 30KHz; For 30GHz:120KHz |
> | #4 Simulation Bandwidth | Reuse the assumptions of PDSCH EVM (10.5.2.2) 20 MHz, 100 MHz Other bandwidths are not precluded (companies to report) |
> | #5 Channel Model | Reuse the assumptions of PDSCH EVM/CSI-others (10.5.2.2/10.5.3.3) CDL-A/B/C/D model in TR 38.901 The CDL table is translated so that the strongest cluster’s AoD and AoA occur at a random angle for both the antenna panels of TRP and UE in the local coordinate. The value of the random angle is selected to be uniformly distributed from +30 to -30 degree. The random value is chosen independently for both AoD and AoA. |
> | #6 Delay Spread | Reuse the assumptions of PDSCH EVM (10.5.2.2) 30 ns, 100 ns, 300 ns, 1000 ns (optional) |
> | #7 NW Antenna Config | Reuse the agreed configuration(s) from 6GR air interface evaluation assumptions For 30GHz, the following can be further considered: (M, N, P, Mg, Ng; Mp, Np) = (8, 16, 2, 1, 1; 1, 1), or (16, 32, 2, 1, 1; 1, 1)), (dH, dV) = (0.5, 0.5); |
> | #8 Multi-TRP operation | The maximum number of coordinated TRP(s) = {1 (baseline), 2, 3, 4}, and other larger value(s) are not precluded CDL channel model is generated per TRP independently; Backhaul: ideal (baseline) or non-ideal; Sync: ideal (baseline) or non-ideal; Companies explain the details, if any. |
> | #9 TXRU mapping to antenna elements | A single TXRU is mapped per panel per subarray per polarization. Others are not precluded (companies to report). |
> | #10 Beam-forming scheme | Companies explain the details, e.g., DFT-based or Eigen-based |
> | #11 Procedure of beam sweeping | Companies explain the details |
> | #12 Criteria for beam selection | To maximize RSRP (with/without a margin (baseline for margin: 3dB, companies to report)) as a baseline. Other criteria is not precluded and up to companies to report. |
> | #13 UE Antenna Config | 4GHz & 7GHz: Reuse the agreed configuration(s) from 6GR air interface evaluation assumptions; 30GHz: Reuse the agreed configuration(s) from 6GR air interface evaluation assumptions: For one-panel, (M, N, P, Mg, Ng; Mp, Np) = (4, 1, 2, 1, 1; 1, 1) is considered as a baseline For multi-panel, (M, N, P; Mp, Np) = (2, 2, 2; 1, 1) is considered as a baseline. |
> | #14 BS array orientation | Azimuth 0°, mechanic downtilt: 90° in GCS. |
> | #15 UE array orientation | ΩUT,a uniformly distributed on [0, 360] degree, ΩUT,b = 0°, ΩUT,g = 0° |
> | #16 UE antenna element radiation pattern | For 4 GHz/7GHz: Option-1: Omni-directional with 0dBi gain; Option-2: According to Table 7.3-2 in TR 38.901 (radiation power pattern for handheld UT) For 30 GHz: See Table A.2.1-8 in TR 38.802 |
> | #17 UE Velocity | 3km/h, 30km/h, 120km/h (Optional), 350km/h(Optional), 500km/h (Optional) |
> | #18 MIMO Scheme | SU-MIMO/MU-MIMO |
> | #19 CW-to-layer mapping | Reuse the assumptions of CSI EVM (10.5.3.1) |
> | #20 Channel coding | LDPC for DL/UL data channel, Polar for CSI |
> | #21 SSB, CSI-RS configuration for BM | NR SSB, CSI-RS for BM as benchmark, and it is up to company to report other configuration, e.g., periodicity. |
> | #22 SRS configuration for BM | NR SRS with usage set to BM as baseline, and it is up to company to report other configuration, e.g., periodicity |
> | #23 Receiver Type | MMSE-IRC as baseline; R-ML (companies to report) |
> | #24 Channel Estimation | Ideal or realistic |
> | #25 MCS | NR MCS (fixed, or AMC) |
> | #26 Performance Metric(s) | BLER and Spectrum Efficiency (SE) Companies can report other performance metrics |

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Beam management]`

**Agreement** · `10.5.2.4` Beam management for downlink and uplink · `RAN1#125:10.5.2.4:009`

> Study the following uplink signal and channels transmission in response to a triggered Event-1:
> - PRACH
> - PUCCH
> - PUSCH
> - SRS

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Beam management]`

**Agreement** · `10.5.2.4` Beam management for downlink and uplink · `RAN1#125:10.5.2.4:010`

> For the study on DL beam measurement and report (AI/ML-based or non-AI/ML-based) on the deployment scenarios of NW multi-TRP/panel and/or UE single/multi-panel/irregular-handheld/CPE UE, the following can be considered:
> - Potential use cases (multi-TRP transmission scheme may use the following beam measurement and report procedure):
>   - Case-1: To identify/report the preferred N>1 DL beams per NW TRP/panel or across NW TRP(s)/panel(s) for supporting multi-TRP/panel transmission scheme(s).
>   - Case-2: To identify/report the preferred M >1 DL beams of different NW TRPs/panels that can be received simultaneously to facilitate multi-TRP/panel joint transmission.
>   - Other use cases are not precluded.
> - For each potential use case, studying details of:
>   - Benchmark:
>     - Beam measurement and report (non-group based L1-RSRP report) on single-TRP/single-panel-UE, multi-TRP/single-panel-UE, of 5G NR
>     - 5G NR L1-RSRP
>   - L1-RSRP calculation
>   - RS measurement requirements
>   - Report content/format
>   - Others are not precluded.
> - Note-1: Strive for unified beam measurement and report procedure for all NW single-/multi-TRP/panel and single-panel-/multi-panel/irregular-handheld-UE.
> - Note-2: Which multi-TRP transmission scheme to be supported will be discussed under other agenda.
> - Companies report the assumption of transmission scheme, if UPT/throughput is reported.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Beam management]`

**Agreement** · `10.5.2.4` Beam management for downlink and uplink · `RAN1#125:10.5.2.4:011`

> Regarding DL beam measurement and report procedure
> (at least for non-AI/ML-based), for the study on L1-SINR based DL beam measurement and report, the following is considered:
> - Studying details of
>   - Benchmark: L1-RSRP based DL beam measurement and report
>   - L1-SINR calculation
>   - Resource requirements for channel and interference measurement
>   - Report content
>   - Others are not precluded.
> - Potential design target/benefits/Use case(s):
>   - Case-1: To reduce intra-TRP/cell interference
>   - Case-2: To reduce cross-TRP/cell interference
>   - Other cases

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Beam management]`

**Agreement** · `10.5.2.4` Beam management for downlink and uplink · `RAN1#125:10.5.2.4:012`

> Support the following as clarification on urban grid as in the assumption of SLS for evaluation of 6GR beam management
> - Inter site distance: 500 m ISD, 250 m ISD
> - Layout/deployment:
>   - 5 x 3 single layer, hex grid (baseline)
>   - 18x 3 single layer, hex grid (baseline)

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Beam management]`

**Agreement** · `10.5.2.4` Beam management for downlink and uplink · `RAN1#125:10.5.2.4:013`

> For the study on spatial/temporal/frequency domain beam measurement/prediction (relevant to AI/ML or non-AI/advanced schemes), the following is considered:
> - Regarding frequency domain beam measurement/prediction (cross-frequency),
>   - The following pair of measured/predicted frequencies can be considered for further evaluation.
>     - Case-1:
>       - Measured frequency: [4 GHz]
>       - Predicted frequency: [7 GHz]
>     - Case-2:
>       - Measured frequency: [4 GHz]
>       - Predicted frequency: [30 GHz]
>     - Other cases are not precluded.
>   - For the study of cross-frequency DL Tx beam prediction for collocated source and target frequencies (using same placement of NW antenna(s) for source and target frequencies), the following procedure for channel model generation can be considered as a starting point:
>     - Step 1: To generate channel layout/properties for all TRPs (including both source and target) operating at the source frequency (e.g., 4GHz).
>     - Step 2: To extend channels of target-frequency TRPs to target frequency (e.g., 7GHz) based on correlation modeling for multi‑frequency simulations (in TR 38.901)
>     - Step 3: To remove the source-frequency (e.g., 4GHz) channels from these target prediction TRPs.
>   - Note: RAN1 identify the requirement of channel modelling for evaluating
>     - non-collocated source and target frequencies
>     - collocated source and target frequencies (using [same] different height of NW antenna(s) and/or different orientation)
> - Study AI/ML model generalization by evaluating inference performance of spatial/temporal/frequency domain beam measurement/prediction under different generalization cases.
>   - Note: Identified generalization cases in 38.843 can be considered as a starting point

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Beam management]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#125:10.5.3.1:005`

> At least support NW triggered and/or configured CSI reporting.
> Study whether/how to support UE-initiated or event-triggered CSI reporting, at least the following aspects:
> - Performance and complexity evaluation, including signalling overhead
>   - Taking NW triggered and/or configured CSI as benchmark
> - Reporting format/quantities
> - Event definition including use cases/scenarios and triggering and reporting mechanism
>   - e.g., CSI report/component is transmitted only if associated event has occurred, CSI reporting configuration selection/adaptation by the UE if associated event has occurred
> - Note: UE-initiated (event-triggered) reporting for beam management is to be discussed separately in the Beam Management agenda

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of DL based CSI acquisition]`

## RAN1#124bis — 12건

**Agreement** · `8.2` Maintenance on NR MIMO Phase 5 · `RAN1#124bis:8.2:005`

> The following TP for Clause 5.2.1.5.4.1 in Rel-19 TS38.214 is endorsed.
> The corresponding final CR for Rel-19 TS38.214 in R1-2603465 is endorsed.
> - Reason for change: Current specification for Mode B UE-initiated reporting defines the timing only with reference to the first transmitted PUCCH. When UEIRI is multiplexed on a PUSCH, the processing time may not be enough for the network for rescheduling the CG PUSCH resource.
> - Summary of change: Clarify that for the determination of type 1 CG-PUSCH, “PUCCH” is replaced with “PUSCH with UEIRI” if the UE would multiplex UEIRI in a PUSCH.
> - Consequences if not approved: If this ambiguity is not resolved, different implementations may interpret the reference point differently, leading to inconsistent UE behavior and potential interoperability issues in Mode B reporting.
> | 5.2.1.5.4.1 UE Initiated CSI reporting For a UE configured with a CSI-ReportConfig with eventType for periodic reference signals with the same periodicity configured by the newBeamResourceSet, without eventDetectionTimeWindowLength, and with dl-OrJointTCI-StateList, when an event instance is determined (as described in the following clauses), - for a reference signal configured by the newBeamResourceSet, if eventType is set to ‘event2’ or ‘event7’, or - for the reference signal in the indicated TCI state or the SS/PBCH block which is QCLed with the reference signal in the indicated TCI state, if eventType is set to ‘event1’, the UE transmits UEIRI on a PUCCH format 0 or format 1 in the PUCCH resource (in the CC provided by pucchCell, if configured, in the CSI-ReportConfig) configured by PUCCHResource in the CSI-ReportConfig. For a UE configured with a CSI-ReportConfig with eventType for periodic reference signals with the same periodicity configured by the newBeamResourceSet, with eventDetectionTimeWindowLength, and with dl-OrJointTCI-StateList, when an event instance is determined (as described in the following clauses), - for a reference signal configured by the newBeamResourceSet, if eventType is set to ‘event2’ or ‘event7’, or - for the reference signal in the indicated TCI state or the SS/PBCH block which is QCLed with the reference signal in the indicated TCI state, if eventType is set to ‘event1’, the UE - starts a timer for such reference signal from the initial value equal to the time window length provided by eventDetectionTimeWindowLength and sets the counter to 1, if the timer for such reference signal is not running; or - increments the counter for such reference signal by 1, if the timer for such reference signal is running. If the number of event instances determined by the counter for such reference signal is greater than or equal to eventInstanceCount, the UE transmits UEIRI on a PUCCH format 0 or format 1 in the PUCCH resource (in the CC provided by pucchCell, if configured, in the CSI-ReportConfig) configured by PUCCHResource in the CSI-ReportConfig. The counter of the event instances for such reference signal is reset: - if the reference signal in the indicated TCI state or the SS/PBCH block which is QCLed with the reference signal in the indicated TCI state is updated when the UE is configured with a CSI-ReportConfig with the higher layer parameter eventType set to ‘event2’ or ‘event1’, or - if the reference signal with the valueOfQ-th highest L1-RSRP out of the reference signals among the activated TCI states or the SS/PBCH block with the valueOfQ-th highest L1-RSRP out of the SS/PBCH blocks QCLed with the reference signals among the activated TCI states, which determines event instance(s), is updated when the UE is configured with a CSI-ReportConfig with the higher layer parameter eventType set to ‘event7’, or - if eventThreshold or valueOfQ or eventInstanceCount or eventDetectionTimeWindow in the CSI-ReportConfig are reconfigured. The UE does not expect that a CSI trigger state associated with CSI report configuration(s) configured with the higher layer parameter eventType is further associated with other CSI report configurations that are not configured with the higher layer parameter eventType. In the remaining of this clause, for the determination of type 1 CG-PUSCH configured by configuredPUSCHResourceOfModeB, “PUCCH” is replaced with “PUSCH with UEIRI” if the UE would multiplex UEIRI in a PUSCH [6, TS38.213]. |

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2603250](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603250.zip) · `[124-R19b-MIMO]`

**Conclusion** · `8.2` Maintenance on NR MIMO Phase 5 · `RAN1#124bis:8.2:009`

> If pathloss offset is configured in any TCI states, for the case of the UE is not configured with tci-SelectionPresentInDCI, the UE applying both indicated joint TCI states to the scheduled or activated PDSCH reception will operate in sDCI-based mTRP mode, the network ensures that both indicated joint TCI states are QCLed with the same RS.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2603037](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603037.zip) · `[124-R19b-MIMO]`

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#124bis:10.5.1.1:001`

> For discussion purpose, the following terminologies are defined
> - 6GR SSB burst: one 6GR SSB or multiple 6GR SSBs each with a different index compose a 6GR SSB burst
> - 6GR SSB burst set: one or multiple 6GR SSB burst(s) compose a 6GR SSB burst set
>   - Note: Whether and how to use the ’6GR SSB burst set’ is up to companies to report.
> - 6GR SSB periodicity: The time interval at which an SSB within a given SSB burst repeats in time
> Note: “index” is only for illustration purpose to identify a 6GR SSB within a 6GR SSB burst, whether and how to specify the terminologies will be further discussed.
> Note: all below examples are only used for improving understanding about above terminologies
> Example 1: 4 SSBs within a SSB burst (no repetition), 1 SSB burst within 1 SSB burst set
> Example 2: 4 SSBs within a SSB burst (4 consecutive repetitions), 1 SSB burst within 1 SSB burst set
> Example 3-1: 16 SSBs within a SSB burst (4 consecutive repetitions), 1 SSB burst within 1 SSB burst set
> Example 3-2: 16 SSBs within a SSB burst (4 consecutive repetitions), 4 SSB bursts within 1 SSB burst set
> Example 4-1: 16 SSBs within a SSB burst (4 interleaved repetitions), 1 SSB burst within 1 SSB burst set
> Example 4-2: 4 SSBs within a SSB burst (4 interleaved repetitions), 4 SSB bursts within 1 SSB burst set

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx)

**Agreement** · `10.5.2.4` Beam management for downlink and uplink · `RAN1#124bis:10.5.2.4:001`

> Support the following table as the assumption of SLS for evaluation of 6GR beam management:
> | Parameter | Value |
> | #1 Scenario (Carrier frequency) | Indoor hotspot, Urban macro, Dense urban (one-layer, and two-layer), High Speed Train, SMa, Urban grid, 4 GHz, TDD 7 GHz, TDD 30 GHz, TDD Other scenarios are not precluded (companies to report) |
> | #2 Mode | DL/UL SU-MIMO/MU-MIMO |
> | #3 System BW | 4GHz: 20MHz 7GHz: 100 MHz 30GHz: 100 MHz |
> | #4 Subcarrier spacing for data | 4GHz/7GHz: 30KHz; 30GHz: 120 KHz |
> | #5 Channel model | TR 38.901 with the following features, if needed: Spatial consistency, including Autocorrelation of shadow fading (Section 7.4.4 in TR 38.901) Correlation modeling for multi‑frequency simulations. Near-field characters Spatial non-stationarity |
> | #6 BS Antenna Configuration | Reuse the agreed configuration(s) from 6GR air interface evaluation assumptions For 7GHz, the following can be further considered: 128 TXRUs, 2048AEs, (M, N, P, Mg, Ng; Mp, Np) = (64, 16, 2, 1, 1, 8, 8), (dH, dV) = (0.5, 0.5); For 30GHz, the following can be further considered: (M, N, P, Mg, Ng; Mp, Np) = (8, 16, 2, 1, 1; 1, 1), or (16, 32, 2, 1, 1; 1, 1)), (dH, dV) = (0.5, 0.5); |
> | #7 BS array orientation | Mechanical tilt: 180° in GCS for indoor hotspot; 90° in GCS for Urban Macro, Dense Urban and High Speed Train Electrical tilt: Company to report Other mechanical tilts are not precluded (companies to report) |
> | #8 TXRU mapping to antenna elements | A single TXRU is mapped per panel per subarray per polarization. Others are not precluded (companies to report). |
> | #9 Beam-forming scheme | Companies explain the details, e.g., DFT-based or Eigen-based |
> | #10 Procedure of beam sweeping | Companies explain the details |
> | #11 Multi-TRP operation | Reuse the assumptions for multi-TRP scenarios of DL-based CSI (A.I. 10.5.3.1) with the following interpretation: The maximum number of coordinated TRP(s) = {1, 2, 3, 4}, and other larger value(s) are not precluded Backhaul: ideal (baseline) or non-ideal; sync: ideal (baseline) or non-ideal; FFS: Other update for high-speed train |
> | #12 Criteria for selection for serving TRP(s) | Serving TRP selection with objective of maximizing RSRP is considered as baseline, and other criteria is not precluded and up to companies to report. For TRP switching, it is up to companies to report the TRP selection margin, if any. |
> | #13 Criteria for beam selection for serving TRP(s) | Beam selection with objective of maximizing RSRP is considered as baseline, and other criteria is not precluded and up to companies to report. |
> | #14 UE Antenna Configuration | 4GHz & 7GHz: Reuse the agreed configuration(s) from 6GR air interface evaluation assumptions; 30GHz: Reuse the agreed configuration(s) from 6GR air interface evaluation assumptions: [Config 0 (one panel) or Config 1 (two panels)]: (M, N, P, Mg, Ng; Mp, Np) = (4, 1, 2, 1, 1; 1, 1) is considered as a baseline |
> | #15 UE array orientation | Ω‌UT,a uniformly distributed on [0, 360] deg, Ω‌UT,b = 0 deg, Ω‌UT,g = 0 deg is considered as a baseline. Others are not precluded (companies to report) |
> | #16 Beam correspondence | Ideal (baseline) or non-ideal. Others are not precluded. |
> | #17 Link adaptation | Based on CSI-RS (Adaptive Modulation and Coding, AMC) |
> | #18 UE receiver type | MMSE-IRC as baseline; other advanced receivers are not precluded |
> | #19 BS Tx Power | Reuse the configuration(s) from 6GR air interface evaluation assumptions |
> | #20 Maximum UE Tx Power | Reuse the configuration(s) from 6GR air interface evaluation assumptions |
> | #21 Inter site distance | Reuse the configuration(s) from 6GR air interface evaluation assumptions, besides for the following: High Speed Train: 1732 m ISD |
> | #22 UE antenna element radiation pattern | Reuse the configuration(s) from 6GR air interface evaluation assumptions |
> | #23 UE Speed and UE distribution | Reuse the configuration(s) from 6GR air interface evaluation assumptions, besides for the following: High Speed Train: 100% outdoor in train (up to 500km/h) |
> | #24 UE rotation | No UE rotation (baseline). UE rotation is not precluded and the corresponding rotation speed is up to companies to report. |
> | #25 BS Antenna height | Dense urban macro and Urban Macro: 25 m; Dense urban micro: 10 m; Indoor: 3m |
> | #26 UE Antenna height | Section 7.2 in TR 38.901. Others are not precluded (companies to report). |
> | #27 Car penetration Loss | TR 38.901, sec 7.4.3.2: μ = 9 dB, σp = 5 dB |
> | #28 Building penetration loss (O2I) | Table 7.4.3-2 in TR 38.901 |
> | #29 UE mobility feature (optional) | Baseline: Random direction straight-line trajectories (from 38.843, Option-3) - Initial UE location, moving direction and speed: UE is randomly dropped in a cell, and an initial moving direction is randomly selected, with a fixed speed. - The initial UE location should be randomly drop within the following blue area: where d1 is the minimum distance that UE should be away from the BS. Each sector is a cell and that the cell association is geometry based. Company to report whether inter-cell handover or switching is disabled during the simulation. Company to report whether the trajectory should be terminated (e.g., for co-located case) or be retained (e.g., non co-located case), if the UE trajectory hits the site boundary (the hexagonal grid) Other UE mobility model(s), e.g., EVM for NR ICBM, are not precluded (companies to report). |
> | #30 Scheduling algorithm | PF scheduler |
> | #31 MCS | Use NR MCS |
> | #32 Traffic Model | FTP model 1/3 with packet size 0.5 Mbytes (other value is not precluded) Other traffic models are not precluded (companies to report). Full buffer (Optional) |
> | #33 CSI Feedback | CSI periodicity: 10ms, 20ms (baseline), 40ms, 80ms, 160ms FFS: Other update for high-speed train |
> | #34 Resource Utilization | 30%, 50%, 70% (optional) |
> | #35 Prediction parameter | Company can report assumption for set-A and set-B, prediction/observation window and any extension for multi-TRP measurement Set A: {16, 32, 64, 128, 256, 512, 1024}. Other values are not precluded. Set B: {4, 8, 16, 32, 48, 64}. Other values are not precluded: Set A/Set B combinations: Alt1: Set B is different from Set A Alt2: Set B is a subset of Set A Alt3: Set B is the same as Set A Regarding temporal domain prediction, the following can be considered: Time gap between predicted time instances (including first future time instance): {40ms, 80ms, 120ms, 160ms, 200ms}. Other values not precluded Prediction/observation window: {1, 2, 4, 8} predicted/measured time instances. Other values not precluded. Note: Regarding cross-frequency prediction, as a baseline, NW antenna(s) for source and target frequencies reuse the same placement and orientation. Others are not precluded (companies to report). |
> | #36 UE number/cell | Reuse the configuration(s) from 6GR air interface evaluation assumptions |
> | #37 Layout/deployment | Reuse the assumptions of uplink/downlink transmission schemes (10.5.2.2/3) 7 x 3, single layer, hex grid (baseline) 7 x 3 two layers, macro layer: hex grid; micro layer: locations of micro sites are reported by company (optional) 19 x 3, single layer, hex grid (optional) FFS: Other update for high-speed train |
> | #38 Inter-cell interference model | Reuse the assumptions of DL-based CSI (10.5.3.1) Explicitly and realistically modelled |
> | #39 Metric | Top-K/1 beam prediction accuracy (with or without L1-RSRP margin), average UPT, and 5%-ile UPT Companies can report other performance metrics observations, e.g., SINR/RSRP prediction accuracy, RS overhead reduction, beam management latency, model and computational complexity, etc. Companies report the assumption of transmission scheme (e.g., Type-I/II PMI or SVD), if UPT is reported. |

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Beam management]`

**Agreement** · `10.5.2.4` Beam management for downlink and uplink · `RAN1#124bis:10.5.2.4:002`

> Support the following table as the basic assumption of LLS for evaluation of 6GR beam management:
> | Parameter | Value |
> | #1 Carrier Frequency | 4GHz, 7GHz, 30GHz |
> | #2 Duplex / Waveform | TDD/CP-OFDM |
> | #3 Subcarrier Spacing | For 4GHz/7GHz: 30KHz; For 30GHz:120KHz |
> | #4 Simulation Bandwidth | Reuse the assumptions of PDSCH EVM (10.5.2.2) 20 MHz, 100 MHz Other bandwidths are not precluded (companies to report) |
> | #5 Channel Model | Reuse the assumptions of PDSCH EVM/CSI-others (10.5.2.2/10.5.3.3) CDL-A/B/C/D model in TR 38.901 The CDL table is translated so that the strongest cluster’s AoD and AoA occur at a random angle for both the antenna panels of TRP and UE in the local coordinate. The value of the random angle is selected to be uniformly distributed from +30 to -30 degree. The random value is chosen independently for both AoD and AoA. |
> | #6 Delay Spread | Reuse the assumptions of PDSCH EVM (10.5.2.2) 30 ns, 100 ns, 300 ns, 1000 ns (optional) |
> | #7 NW Antenna Config | Reuse the agreed configuration(s) from 6GR air interface evaluation assumptions For 7GHz, the following can be further considered: 128 TXRUs, 2048AEs, (M, N, P, Mg, Ng; Mp, Np) = (64, 16, 2, 1, 1, 8, 8), (dH, dV) = (0.5, 0.5); For 30GHz, the following can be further considered: (M, N, P, Mg, Ng; Mp, Np) = (8, 16, 2, 1, 1; 1, 1), or (16, 32, 2, 1, 1; 1, 1)), (dH, dV) = (0.5, 0.5); |
> | #8 Multi-TRP operation | The maximum number of coordinated TRP(s) = {1 (baseline), 2, 3, 4}, and other larger value(s) are not precluded CDL channel model is generated per TRP independently; Backhaul: ideal (baseline) or non-ideal; Sync: ideal (baseline) or non-ideal; Companies explain the details, if any. |
> | #9 TXRU mapping to antenna elements | A single TXRU is mapped per panel per subarray per polarization. Others are not precluded (companies to report). |
> | #10 Beam-forming scheme | Companies explain the details, e.g., DFT-based or Eigen-based |
> | #11 Procedure of beam sweeping | Companies explain the details |
> | #12 Criteria for beam selection | To maximize RSRP (with/without a margin (baseline for margin: 3dB, companies to report)) as a baseline. Other criteria is not precluded and up to companies to report. |
> | #13 UE Antenna Config | 4GHz & 7GHz: Reuse the agreed configuration(s) from 6GR air interface evaluation assumptions; 30GHz: Reuse the agreed configuration(s) from 6GR air interface evaluation assumptions: [Config 0 (one panel) or Config 1 (two panels)]: (M, N, P, Mg, Ng; Mp, Np) = (4, 1, 2, 1, 1; 1, 1) is considered as a baseline |
> | #14 BS array orientation | Azimuth 0°, mechanic downtilt: 90° in GCS. |
> | #15 UE array orientation | ΩUT,a uniformly distributed on [0, 360] degree, ΩUT,b = 0°, ΩUT,g = 0° |
> | #16 UE antenna element radiation pattern | For 4 GHz/7GHz: Option-1: Omni-directional with 0dBi gain; Option-2: According to Table 7.3-2 in TR 38.901 (radiation power pattern for handheld UT) For 30 GHz: See Table A.2.1-8 in TR 38.802 |
> | #17 UE Velocity | 3km/h, 30km/h, 120km/h (Optional), 350km/h(Optional), 500km/h (Optional) |
> | #18 MIMO Scheme | SU-MIMO/MU-MIMO |
> | #19 CW-to-layer mapping | Reuse the assumptions of CSI EVM (10.5.3.1) |
> | #20 Channel coding | LDPC for DL/UL data channel, Polar for CSI |
> | #21 SSB, CSI-RS configuration for BM | NR SSB, CSI-RS for BM as benchmark, and it is up to company to report other configuration, e.g., periodicity. |
> | #22 SRS configuration for BM | NR SRS with usage set to BM as baseline, and it is up to company to report other configuration, e.g., periodicity |
> | #23 Receiver Type | MMSE-IRC as baseline; R-ML (companies to report) |
> | #24 Channel Estimation | Ideal or realistic |
> | #25 MCS | NR MCS (fixed, or AMC) |
> | #26 Performance Metric(s) | BLER and Spectrum Efficiency (SE) Companies can report other performance metrics. |

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Beam management]`

**Agreement** · `10.5.2.4` Beam management for downlink and uplink · `RAN1#124bis:10.5.2.4:003`

> Support the following table as the assumption of SLS for evaluation of 6GR beam management:
> | #29 UE mobility feature (optional) | Baseline: Random direction straight-line trajectories (from 38.843, Option-3) - Initial UE location, moving direction and speed: UE is randomly dropped in a cell, and an initial moving direction is randomly selected, with a fixed speed. - The initial UE location should be randomly drop within the following blue area: where d1 is the minimum distance that UE should be away from the BS. Each sector is a cell and that the cell association is geometry based. Company to report whether inter-cell handover or switching is disabled during the simulation. Company to report whether the trajectory should be terminated (e.g., single-TRP) or be retained (e.g., multi-TRP), if the UE trajectory hits the site boundary (the hexagonal grid) Other UE mobility model(s), e.g., EVM for NR ICBM, linear trajectory model with random and smooth direction change (i.e., TR38.843, Option-2), are not precluded (companies to report). |
> | #35 Prediction parameter | Company can report assumption for set-A and set-B, prediction window and any extension for intra-/inter-cell/multi-TRP measurement Set A: M*N M: {8, 16, 32, 64, 256,1024}. N: {1, 2, 3, 4}. Ratio of the size of Set-B to Set-A: {1, 1/2, 1/4, 1/8, 1/16, 1/32} For multi-TRP, Set-A and Set-B can contain beams across TRP(s). Other values for M, N and ratio are not precluded. Set A/Set B combinations: Alt1: Set B is different from Set A Alt2: Set B is a subset of Set A Alt3: Set B is the same as Set A Regarding temporal domain prediction, the following can be considered: Time gap between neighboring predicted time instances: {20ms, 40ms, 80ms, 120ms, 160ms, 200ms}. Predicted time instances: {1, 2, 4, 8}. Measured time instances: companies to report. Other values for the above are not precluded Other prediction mechanism is not precluded and up to companies’ report. |
> | #39 Metric | Top-K/1 beam prediction accuracy (with or without L1-RSRP margin), average/5%-ile UPT/throughput, SINR/RSRP, L1-RSRP/SINR difference between Top-1 predicted beam and genie-aided beam, RS overhead reduction, beam management latency, and/or number of model-parameter(s)/model computational complexity. Companies can report other performance metrics Companies report the assumption of transmission scheme, if UPT/throughput is reported. |

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Beam management]`

**Agreement** · `10.5.2.4` Beam management for downlink and uplink · `RAN1#124bis:10.5.2.4:004`

> Support the following table as the assumption of LLS for evaluation of 6GR beam management:
> | #26 Performance Metric(s) | BLER and Spectrum Efficiency (SE) Companies can report other performance metrics |

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Beam management]`

**Agreement** · `10.5.2.4` Beam management for downlink and uplink · `RAN1#124bis:10.5.2.4:005`

> For 6GR UE-initiated beam management (UEIBM), Study the following events for single-TRP as a starting point:
> - Event-1: The measured/predicted quality of the current/serving beam is worse than a threshold, including “beam failure”.
> - Event-2: The measured/predicted quality of at least one candidate beam becomes a threshold value better than the current/serving beam.
>   - The candidate beam is associated with a same (i.e., intra-cell) or a different physical cell ID (i.e., inter-cell case) as the current/serving beam.
> - How to extend to m-TRP use case, including the feasibility.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Beam management]`

**Agreement** · `10.5.2.4` Beam management for downlink and uplink · `RAN1#124bis:10.5.2.4:006`

> - Study requirement/functionality of DL RS for beam measurement, e.g., number of RS ports, time/frequency-domain RS pattern, time-domain behavior, etc.
>   - Note: Sync-signal design is not considered herein

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Beam management]`

**Agreement** · `10.5.2.4` Beam management for downlink and uplink · `RAN1#124bis:10.5.2.4:007`

> For the study on spatial/temporal/frequency domain beam measurement/prediction (relevant to AI/ML or non-AI/advanced schemes), the following is considered:
> - Implementation complexity/overhead:
>   - Model/computation complexity: FLOPs
>   - Model size, if AI/ML is involved: Number of parameters
>   - Note: The above complexity/overhead with the increase of TRP number should be clarified.
> - Benchmark:
>   - Benchmark-1: based on the measurement of Set-A;
>   - Benchmark-2: only based on the measurement of Set-B (non-prediction).
>   - Other benchmarks are not precluded and up to companies report
> - Evaluation assumptions with the following clarifications
>   - Spatial/Temporal domain DL Tx beam prediction and management, scenarios of both single-TRP and multi-TRP (intra/inter-cell) can be considered.
>     - For multi-TRP (intra/inter-cell), companies report whether the predicted beam(s) (Set-A) are from the same set of cells/TRPs corresponding to the measured beam(s) (Set-B) or not.
>     - Note (Sample and Hold): Regarding temporal domain prediction, reuse the result of the latest measurement.
>   - Regarding frequency domain beam measurement/prediction (cross-frequency), the scenario of co-located and non-colocated, intra-frequency-range (inter-/intra-band) and inter-frequency-range can be considered.
>     - Note: Regarding Cross frequency DL Tx beam prediction, Set-A includes beams in the predicted/target frequency, and Set-B is based on the measurement in the source frequency
>     - Further clarification/extension on channel modeling (e.g., inter-frequency-range, non-colocated) can be studied.
>     - Note: For colocated case, impact on performance using same/different placement and orientation on NW antenna(s) for source and target frequencies should be considered.
> - Note: the above assumptions can also apply for non-AI schemes, i.e., without training/inference/data collection, when applicable.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Beam management]`

**Agreement** · `10.5.2.4` Beam management for downlink and uplink · `RAN1#124bis:10.5.2.4:008`

> For network-initiated beam reporting in 6GR, support at least L1-RSRP as a measurement/report quantity for beam reporting, when applicable.
> - Note: L1-RSRP maybe measured or predicted by UE.
> - FFS: L1-SINR and others.

남은 FFS 1건

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Beam management]`

**Agreement** · `10.5.2.4` Beam management for downlink and uplink · `RAN1#124bis:10.5.2.4:009`

> Regarding NW-initiated beam management, study DL beam measurement and report procedure on DL RS(s) for both single-TRP/cell/carrier and multi-TRP/cell/carrier scenario(s).
> - At least the following aspects can be studied:
>   - Procedure of beam sweeping/tracking, e.g., intra-/inter-symbol, time-domain/frequency-domain sweeping
>   - Measurement/prediction metrics
>   - Time-domain behavior for report, e.g., aperiodic, semi-persistent, periodic
>   - Report content
>   - Note: Report container for study will be discussed under other agenda.
>   - Note: RAN1 strives to support a unified framework for beam measurement and reporting for MIMO and mobility.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Beam management]`

## RAN1#124 — 15건

**Agreement** · `8.2` Maintenance on NR MIMO Phase 5 · `RAN1#124:8.2:001`

> Adopt the following changes in [Sections 6.2.7 and 6.3.2.1.4 in TS 38.212.
> The corresponding final CR for Rel-19 TS 38.212 in R1-2601670 is endorsed.
> - Reason for change: On beam report transmission procedure for UE-initiated/event-driven beam reporting, regarding the multiplexing first PUCCH(s) with UEIRIs collided/overlapped with a PUSCH, the field of UEIRI is jointly encoded with HARQ-ACK by appending the UEIRI to the HARQ-ACK information bits.
> - Summary of change: Specify multiplexing of UEIRI into PUSCH by jointly encoding UEIRI bits and HARQ-ACK information bits, which including: 1) coded bits of UEIRI in TS38.212; 2) UEIRI bits mapped to UCI bit sequence in TS 38.212
> - Consequences if not approved: UE procedures of multiplexing UEIRI into a PUSCH in the specification are incomplete.
> |  |
> | 6.3.2.1.4 HARQ-ACK and CG-UCI/UTO-UCI/UEIRI If the higher layer parameter nrofBitsInUTO-UCI is configured, the procedure in this clause 6.3.2.1.4 applies by replacing CG-UCI with UTO-UCI in all the notations and texts, replacing "When higher layer parameter cg-UCI-Multiplexing is configured" with "When UTO-UCI and HARQ-ACK have the same priority index and are jointly encoded and transmitted on a PUSCH" and replacing "is given by Table 6.3.2.1.3-1 mapped in the order from upper part to lower part " with "is given by Clause 9.3.1 of [5, TS 38.213]". If a UE would multiplex UEIRI and HARQ-ACK in a PUSCH [5, TS 38.213], the procedure in this clause 6.3.2.1.4 applies by replacing CG-UCI with UEIRI in all the notations and texts assuming higher layer parameter cg-UCI-Multiplexing is configured and replacing "is given by Table 6.3.2.1.3-1 mapped in the order from upper part to lower part " with "is determined as described in clause 6.3.2.1.3B ". When higher layer parameter cg-UCI-Multiplexing is configured, the UCI bit sequence is determined as follows, where . - The CG-UCI bits are mapped to the UCI bit sequence, where for . The CG-UCI bit sequence is given by Table 6.3.2.1.3-1 mapped in the order from upper part to lower part, and is number of CG-UCI bits; - The HARQ-ACK bits are mapped to the UCI bit sequence , where for . The HARQ-ACK bit sequence is given by Clause 9.1 of [5, TS38.213], and is number of HARQ-ACK bits. |

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601518](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601518.zip) · `[124-R19-MIMO]`

**Agreement** · `8.2` Maintenance on NR MIMO Phase 5 · `RAN1#124:8.2:002`

> Adopt the following changes in Section 5.2.1.4.3 in TS38.214:
> The corresponding CR for Rel-19 and TS38.214 in R1-2601671 is endorsed.
> - Reason for change:  On channel measurement for UE-initiated/event-driven beam reporting, the RRC parameter of ‘timeRestrictionForChannelMeasurement’ specified for legacy beam reporting can be reused for UEI beam reporting by adopting the following operations.
>   - RRC parameter of timeRestrictionForChannelMeasurement can be applied to Event-2, Event-1 and Event-7.
>   - Besides for new beam RS(s), the value of M determined for measurement period of the new beam(s) by timeRestrictionForChannelMeasurements in the UEIBR CSI report configuration can also be used for the current beam RS measurement.
> - Summary of change:  Specify the rule of channel measurements for UE-initiated/event-driven beam reporting depending on RRC parameter of timeRestrictionForChannelMeasurement.
> - Consequences if not approved: UE procedures of deriving channel measurements for L1-RSRP based UEI beam reporting is unclear.
> | 5.2.1.4.3 L1-RSRP Reporting <Omitted> If the higher layer parameter timeRestrictionForChannelMeasurements in CSI-ReportConfig is set to "notConfigured", the UE shall derive the channel measurements for computing L1-RSRP value reported in uplink slot n based on only the SS/PBCH or NZP CSI-RS, no later than the CSI reference resource, (defined in [4, TS 38.211]) associated with the CSI resource setting. , which triggers UEIRI transmission If the higher layer parameter timeRestrictionForChannelMeasurements in CSI-ReportConfig is set to "Configured", the UE shall derive the channel measurements for computing L1-RSRP reported in uplink slot n based on only the most recent, no later than the CSI reference resource, occasion of SS/PBCH or NZP CSI-RS (defined in [4, TS 38.211]) associated with the CSI resource setting., which triggers UEIRI transmission |

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601518](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601518.zip) · `[124-R19-MIMO]`

**Agreement** · `8.2` Maintenance on NR MIMO Phase 5 · `RAN1#124:8.2:003`

> Send a reply to the RAN4 LS R4-2511656 clarifying that, for a UE configured with a UEIBM CSI report configuration, UEIBM measurement reporting delay requirements should consider that:
> - timeRestrictionForChannelMeasurements can be configured for any event type, i.e., Event-1, Event-2 and Event-7;
> - the value of M determined for the measurement period of the new beams by timeRestrictionForChannelMeasurements in the UEIBM CSI report configuration is also used for the current beam in the event determination/evaluation measurements.
> The Final LS in R1-2601672 is endorsed.

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601518](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601518.zip) · `[124-R19-MIMO]`

**Agreement** · `8.2` Maintenance on NR MIMO Phase 5 · `RAN1#124:8.2:004`

> Adopt the following changes in Sections 9 and 9.3 in TS 38.213.
> The corresponding CR for Rel-19 and TS38.213 in R1-2601722 is endorsed.
> - Reason for change: On beam report transmission procedure for UE-initiated/event-driven beam reporting, regarding the multiplexing first PUCCH(s) with UEIRIs collided/overlapped with a PUSCH, the field of UEIRI is jointly encoded with HARQ-ACK by appending the UEIRI to the HARQ-ACK information bits.
> - Summary of change: Specify multiplexing of UEIRI with/without HARQ-ACK  into PUSCH, which including: 1) UEIRI multiplexed into PUSCH in TS 38.213; 2) “Betaoffset” value applied for rate matching in case of UEIRI is multiplexed into PUSCH in  TS 38.213.
> - Consequences if not approved: UE procedures of multiplexing UEIRI into a PUSCH in the specification are incomplete.
> | 9 UE procedure for reporting control information <Irrelevant part is omitted> If a UE - would multiplex UCI in a PUCCH transmission that overlaps with a PUSCH transmission, and - the PUSCH and PUCCH transmissions fulfil the conditions in clause 9.2.5 for UCI multiplexing, the UE - multiplexes only HARQ-ACK information and/or UEIRI, if any, from the UCI in the PUSCH transmission and does not transmit the PUCCH if the UE multiplexes aperiodic or semi-persistent CSI reports in the PUSCH; - multiplexes only HARQ-ACK information, UEIRI and CSI reports, if any, from the UCI in the PUSCH transmission and does not transmit the PUCCH if the UE does not multiplex aperiodic or semi-persistent CSI reports in the PUSCH. <Irrelevant part is omitted> |
> | 9.3 UCI reporting in physical uplink shared channel <Irrelevant part is omitted> For a PUSCH transmission that is configured by a ConfiguredGrantConfig and includes CG-UCI, the UE multiplexes the CG-UCI in the PUSCH transmission using a value provided by betaOffsetCG-UCI with the mapping defined in Table 9.3-1. The CG-UCI has same priority value as the PUSCH. If the UE is provided cg-UCI-Multiplexing and multiplexes HARQ-ACK information of same priority value as the CG-UCI in the PUSCH transmission, as described in clauses 9 and 9.2.5, the UE jointly encodes the HARQ-ACK information and the CG-UCI [5, TS 38.212] and determines a number of resources for multiplexing the combined information in a PUSCH using which provides indexes and for the UE to use if the UE multiplexes up to 11, and more than 11 combined information bits, respectively. <Irrelevant part is omitted> When the UE would multiplex UEIRI, and HARQ-ACK information if any, in a PUSCH, the UE determines a number of resources for multiplexing the UEIRI bits and HARQ-ACK information, if any, in the PUSCH using which provides indexes and for the UE to use if the UE multiplexes up to 11, and more than 11 information bits, respectively, where if the PUSCH transmission includes HARQ-ACK information, the UE jointly encodes the HARQ-ACK information and the UEIRI [5, TS 38.212]. <Irrelevant part is omitted> |

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601519](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601519.zip) · `[124-R19-MIMO]`

**Agreement** · `8.2` Maintenance on NR MIMO Phase 5 · `RAN1#124:8.2:007`

> Adopt the following changes in Section 5.2.1.4.1 in TS38.214:
> The corresponding CR for Rel-19 and TS38.214 in R1-2601680 is endorsed.
> | Impacted spec(s): TS38.214 |
> | Reason for change: Two conflicting descriptions exist in the current version of the spec: 1) clause 5.2.1.4.1: “if interference measurement is performed on NZP CSI-RS, a UE does not expect to be configured with more than one NZP CSI-RS resource in the associated resource set within the resource setting for channel measurement” 2) clause 5.2.1.4.2: “Ks>1 CSI-RS resources are configured in the corresponding NZP-CSI-RS-ResourceSet for channel measurement” According to the second description, for M-CRI report, one NZP IMR can be configured and Ks>1 CSI-RS resources are configured in the corresponding NZP-CSI-RS-ResourceSet for channel measurement, which conflicts with the first description. |
> | Summary of the change: Also, except for a CSI-ReportConfig with higher layer parameter valueOfM and reportQuantity set to 'cri-RI-PMI-CQI' or 'cri-RI-LI-PMI-CQI' and codebookType set to 'typeI-SinglePanel', or a CSI-ReportConfig with higher layer parameter valueOfM and reportQuantity set to 'cri-RI-PMI-CQI' and codebookType set to 'typeII-r16', if interference measurement is performed on NZP CSI-RS, a UE does not expect to be configured with more than one NZP CSI-RS resource in the associated resource set within the resource setting for channel measurement. |
> | Consequences if not approved: If not clarified, the specification is inconsistent. |
> | 5.2.1.4.1 Resource Setting configuration < Unchanged parts are omitted > Except for L1-SINR, codebookType set to 'typeII-CJT-r18', 'typeII-CJT-PortSelection-r18', 'typeII-Doppler-r18', or 'typeII-Doppler-PortSelection-r18', 'typeI-SinglePanel-r19', 'typeI-MultiPanel-r19', 'eTypeII-r19', 'typeII-FePortSelection-r19', or 'typeII-Doppler-r19', a CSI-ReportConfig with higher layer parameter valueOfM and reportQuantity set to 'cri-RI-PMI-CQI' or 'cri-RI-LI-PMI-CQI' and codebookType set to 'typeI-SinglePanel', or a CSI-ReportConfig with higher layer parameter valueOfM and reportQuantity set to 'cri-RI-PMI-CQI' and codebookType set to 'typeII-r16', if interference measurement is performed on NZP CSI-RS, a UE does not expect to be configured with more than one NZP CSI-RS resource in the associated resource set within the resource setting for channel measurement. Except for L1-SINR, the UE configured with the higher layer parameter nzp-CSI-RS-ResourcesForInterference may expect no more than 18 NZP CSI-RS ports configured in a NZP CSI-RS resource set. < Unchanged parts are omitted > |

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601519](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601519.zip) · `[124-R19-MIMO]`

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#124:10.5.1.1:001`

> For initial access and mobility in 6GR, study the following deployment scenarios
> - Single beam and multi-beam based deployments
> - Single TRP and multi-TRP based deployments
> - Single carrier and multi-carrier deployments
> - Other deployment scenarios

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx)

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#124:10.5.1.1:002`

> For 6GR paging transmission/reception, study at least the following aspects:
> - Study paging transmission scheme(s) to facilitate network energy savings
> - Study paging scheme(s) to facilitate UE energy savings
> - Study necessity of paging capacity enhancement
> - Study necessity of paging coverage enhancement

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx)

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#124:10.5.1.1:003`

> Study 6GR signals, channels and procedures for initial access and idle mobility, considering at least
> - Cell/Initial Cell search and cell ID identification
> - Time/frequency synchronization/tracking
> - Beam measurement
> - System information acquisition
> - Whether TRP is transparent/non-transparent to UE during above procedures
> Study 6GR signals, channels and procedures for idle mobility, considering at least
> - Cell search and cell ID identification
> - Time/frequency synchronization/tracking
> - Beam measurement
> - System information acquisition
> - Whether TRP is transparent/non-transparent to UE during above procedures

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx)

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#124:10.5.1.1:004`

> For 6GR measurements in initial access and for mobility, study measurement resource, measurement quantity, measurement functionality and measurement procedure, at least including:
> - L1 measurements
> - Cell-level/[TRP-level] and beam-level measurement

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx)

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#124:10.5.1.1:005`

> Study beam operation during 6GR initial access, including:
> - Beam acquisition during initial access
> - Beam report/refinement during initial access
> - Feasibility and performance of spatial/temporal beam prediction during initial access

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx)

**Agreement** · `10.5.1.1` Synchronization acquisition and beam measurement · `RAN1#124:10.5.1.1:006`

> Basic 6GR sync signal structure is defined as 6GR SSB, which consists of primary synchronization signal(s), secondary synchronization signal(s) and physical broadcast channel(s)
> - FFS: Other types of 6GR sync signal/channel structure or reference signal and their structure

남은 FFS 1건

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx)

**Agreement** · `10.5.2.4` Beam management for downlink and uplink · `RAN1#124:10.5.2.4:001`

> Study TCI/QCL-related aspects, e.g., definition of QCL/TCI-state, QCL property/chain
> On beam management for DL and UL of 6GR, at least the following aspects should be studied:
> - Beam measurement(prediction)/report/indication within a same TRP, i.e., single-TRP, in a cell/carrier;
> - Beam measurement(prediction)/report/indication among different TRPs, i.e., multi-TRP, in a cell/carrier;
> - Beam measurement(prediction)/report/indication among different cells/carrier, i.e., inter-cell/carrier
> - Note: Both AI/ML and non-AI/ML related mechanism(s) for the above can be further studied.
> Note-1: Which multi-TRP transmission scheme for study will be discussed under other agenda.

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · `[124-R20-6GR-Beam management]`

**Agreement** · `10.5.2.4` Beam management for downlink and uplink · `RAN1#124:10.5.2.4:002`

> Study of UE-initiated/event-driven beam management (UEIBM) mechanisms for 6GR, covering at least the following aspects:
> - Event definition and the corresponding target use case.
> - UL transmission, UE’s behavior, and procedure for a triggered event, including the necessity and design of the associated network’s response.
> - Note 1: Both AI/ML and non-AI/ML related mechanism(s) for the above can be further studied.
> - Note 2: UE-initiated/event-driven CSI reporting is not discussed in this agenda.

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · `[124-R20-6GR-Beam management]`

**Agreement** · `10.5.2.4` Beam management for downlink and uplink · `RAN1#124:10.5.2.4:003`

> Regarding link-level evaluation of 6GR beam management, in RAN1#124b, to use the following template as starting point for collecting related parameters.
> | Parameter | Value |
> | Carrier Frequency |  |
> | Duplex / Waveform |  |
> | Subcarrier Spacing |  |
> | Simulation Bandwidth |  |
> | Channel Model |  |
> | Delay Spread |  |
> | NW Antenna Config |  |
> | Multi-TRP operation |  |
> | TXRU mapping to antenna elements |  |
> | Beam-forming scheme |  |
> | Procedure of beam sweeping |  |
> | Criteria for beam selection |  |
> | UE Antenna Config |  |
> | BS array orientation |  |
> | UE array orientation |  |
> | UE antenna element radiation pattern |  |
> | UE Velocity |  |
> | MIMO Scheme |  |
> | CW-to-layer mapping |  |
> | Channel coding |  |
> | SSB, CSI-RS configuration for BM |  |
> | SRS configuration for BM |  |
> | Receiver Type |  |
> | Channel Estimation |  |
> | MCS |  |
> | Performance Metric(s) |  |

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · `[124-R20-6GR-Beam management]`

**Agreement** · `10.5.2.4` Beam management for downlink and uplink · `RAN1#124:10.5.2.4:004`

> Regarding system-level evaluation of 6GR beam management, in RAN1#124b, , to use the following template as starting point for collecting related parameters.
> | Parameter | Value |
> | Scenario (Carrier frequency) |  |
> | Mode |  |
> | System BW |  |
> | Subcarrier spacing for data |  |
> | Channel model |  |
> | BS Antenna Configuration |  |
> | BS array orientation |  |
> | TXRU mapping to antenna elements |  |
> | Beam-forming scheme |  |
> | Procedure of beam sweeping |  |
> | Multi-TRP operation |  |
> | Criteria for selection for serving TRP(s) |  |
> | Criteria for beam selection for serving TRP(s) |  |
> | UE Antenna Configuration |  |
> | UE array orientation |  |
> | Beam correspondence |  |
> | Link adaptation |  |
> | UE receiver type |  |
> | BS Tx Power |  |
> | Maximum UE Tx Power |  |
> | Inter site distance |  |
> | UE antenna element radiation pattern |  |
> | UE Speed and UE distribution |  |
> | UE rotation |  |
> | BS Antenna height |  |
> | UE Antenna height |  |
> | Car penetration Loss |  |
> | Building penetration loss (O2I) |  |
> | UE mobility feature (optional) |  |
> | Scheduling algorithm |  |
> | MCS |  |
> | Traffic Model |  |
> | CSI Feedback |  |
> | Resource Utilization |  |
> | Prediction parameter |  |
> | UE number/cell |  |
> | Layout/deployment |  |
> | Inter-cell interference model |  |
> | Metric |  |

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · `[124-R20-6GR-Beam management]`

## RAN1#123 — 3건

**Agreement** · `8.2` Maintenance on NR MIMO Phase 5 · `RAN1#123:8.2:005`

> Regarding triggering event determination, besides for Candidate#2, at least Candidate #1, and Candidate#7 is additionally supported for resetting the counting.
> - Candidate#1: Regarding Event-2 and 7, RS reconfiguration for new beam is received;
>   - In such case, the UE only needs to reset the counting of the removed new beams by RS reconfiguration, and stops the timers for those new beams.
>     - FFS: Whether/how to have any spec impact on the resetting the counting of the removed new beams by RS reconfiguration and stopping the timers for those new beams.
> - Candidate#7: The RRC parameter(s) of the threshold for event evaluation in Event-1/2/7, the value of Q in Event-7, eventInstanceCount and/or eventDetectionTimeWindowLength are reconfigured for the CSI report configuration for UEI beam report.
>   - In such case, the UE needs to reset the counting and stop the timers for all new beams.
> When Candidate#2 is satisfied, the timers for all new beams should be stopped, besides for resetting counting.
> Note: Candidate#2: The measured current beam RS is updated based on indicated TCI state

남은 FFS 1건

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2508529](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2508529.zip) · `[123-R19-MIMO]`

**Agreement** · `8.2` Maintenance on NR MIMO Phase 5 · `RAN1#123:8.2:006`

> Adopt the following changes in Clause 5.2.1.5.4 in TS38.214.
> - Reason for change: The agreed corresponding reference of differential value are not specified.
> - Summary of change: Clarify the reference of deriving the differential RSRP in a report instance.
> - Consequences if not approved: The report format and corresponding definition of corresponding differential L1-RSRP field is incomplete, regarding event-1/2/7.
> | 5.2.1.5.4.1a UE Initiated CSI reporting for event 2 <Unchanged parts are omitted> After transmitting UEIRI, the UE reports, as defined in Clause 6.3.2.1.2 of [5, TS 38.212], in a single reporting instance nrofReportedRS-UEIBR CRIs or SSBRIs corresponding to reference signals provided by the newBeamResourceSet that comprise at least one reference signal that triggers the UEIRI transmission. For each or SSBRI, the CSI report includes the absolute L1-RSRP or differential L1-RSRP and, when PresenceOfConditionMetIndicator is configured, condition met indicator indicating whether the reference signal indicated by reported CRI or SSBRI triggers the UEIRI transmission, and, when enabledCurrentBeamReport is configured, the differential L1-RSRP corresponding to the reference signal in the indicated TCI state, or to the SS/PBCH block which is QCLed with the reference signal in the indicated TCI state. The differential L1-RSRP values are with a reference to the largest measured L1-RSRP value of the reported nrofReportedRS-UEIBR reference signals. The UE sends the CSI report <Unchanged parts are omitted> 5.2.1.5.4.1b UE Initiated CSI reporting for event 1 <Unchanged parts are omitted> After transmitting UEIRI, the UE reports, as defined in Clause 6.3.2.1.2 of [5, TS 38.212], in a single reporting instance nrofReportedRS-UEIBR CRIs or SSBRIs corresponding to reference signals provided by the newBeamResourceSet. For each CRI or SSBRI, the CSI report includes the absolute L1-RSRP or differential L1-RSRP and, when enabledCurrentBeamReport is configured, the absolute L1-RSRPs, corresponding to the reference signal in the indicated TCI state, or to the SS/PBCH block which is QCLed with the reference signal in the indicated TCI state. The differential L1-RSRP values are with a reference to the largest measured L1-RSRP value of the reported nrofReportedRS-UEIBR reference signals. The UE sends the CSI report <Unchanged parts are omitted> 5.2.1.5.4.1c UE Initiated CSI reporting for event 7 <Unchanged parts are omitted> After transmitting UEIRI, the UE reports, as defined in Clause 6.3.2.1.2 of [5, TS 38.212] in a single reporting instance nrofReportedRS-UEIBR CRIs or SSBRIs corresponding to reference signals provided by the newBeamResourceSet that comprise at least one reference signal that triggers the UEIRI transmission. For each CRI or SSBRI, the CSI report includes the absolute L1-RSRP or differential L1-RSRP and, when PresenceOfConditionMetIndicator is configured a condition met indicator indicating whether the reference signal indicated by reported CRI or SSBRI triggers the UEIRI transmission and, when enabledCurrentBeamReport is configured, the differential L1-RSRP corresponding to the reference signal with the valueOfQ highest L1-RSRP out of the activated TCI state reference signals, or to the SS/PBCH block which is QCLed with the reference signal with the valueOfQ highest L1-RSRP out of the activated TCI state reference signals. The differential L1-RSRP values are with a reference to the largest measured L1-RSRP value of the reported nrofReportedRS-UEIBR reference signals. The UE sends the CSI report <Unchanged parts are omitted> |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2508529](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2508529.zip) · `[123-R19-MIMO]`

**Agreement** · `8.2` Maintenance on NR MIMO Phase 5 · `RAN1#123:8.2:007`

> On beam report transmission procedure for UE-initiated/event-driven beam reporting, regarding the multiplexing a number of L (L>=1) first PUCCH(s) with UEIRIs collided/overlapped with a PUSCH:
> - A field of bit sequence with a length of L bit is piggyback into the PUSCH.
>   - Each of bits in the bit sequence corresponds to respective first PUCCH(s) by an ascending order of the values of PUCCH resource ID associated with the first PUCCHs.
>   - The value of 1 indicates positive UEIRI.
>   - The value of 0 indicates negative UEIRI.

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2508529](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2508529.zip) · `[123-R19-MIMO]`

## RAN1#122bis — 3건

**Agreement** · `8.2` Maintenance on NR MIMO Phase 5 · `RAN1#122bis:8.2:003`

> On beam report transmission procedure for UE-initiated/event-driven beam reporting, regarding mode-A, introduce RRC configuration parameter of reportSlotOffsetList in the configuration of the report transmission mode.

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508014](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508014.zip) · `[122bis-R19-MIMO]`

**Agreement** · `8.2` Maintenance on NR MIMO Phase 5 · `RAN1#122bis:8.2:006`

> Adopt the following changes in Clause 5.2.1.5.4.1 in TS38.214.
> - Reason for change: Regarding the condition of resetting the counter of event instances, the following candidate#2 was agreed to be applied for Event-2, Event-1 and Event-7, i.e., the measured current beam RS is updated based on indicated TCI state. However, it is intuitive that current beam RS of Event-7 is just related to the activated TCI states, rather than the indicated TCI state. Consequently, the condition of resetting the counter for Event-7 has not yet been captured in the current specifications, i.e., the measured current beam RS is updated based on activated TCI states.
> - Summary of change: Clarifying the condition of resetting the counter for Event-7, i.e., the measured current beam RS is updated based on activated TCI states.
> - Consequences if not approved: It is unclear how to reset the counter for Event-7.
> | 5.2.1.5.4 UE Initiated reporting 5.2.1.5.4.1 UE Initiated CSI reporting <Irrelevant part is omitted> If the number of event instances determined by the counter for such reference signal is greater than or equal to eventInstanceCount, the UE transmits UEIRI on a PUCCH format 0 or format 1 in the PUCCH resource (in the CC provided by pucchCell, if configured, in the CSI-ReportConfig) configured by PUCCHResource in the CSI-ReportConfig. The counter of the event instances for such reference signal is reset: - if the reference signal in the indicated TCI state or the SS/PBCH block which is QCLed with the reference signal in the indicated TCI state is updated when the UE is configured with a CSI-ReportConfig with the higher layer parameter eventType set to ‘event2’ or ‘event1’, or - if the reference signal with the valueOfQ highest L1-RSRP out of the reference signals among the activated TCI states or the SS/PBCH block with the valueOfQ highest L1-RSRP out of the SS/PBCH blocks QCLed with the reference signals among the activated TCI states, which determines event instance(s), is updated when the UE is configured with a CSI-ReportConfig with the higher layer parameter eventType set to ‘event7’. The UE does not expect that a CSI trigger state associated with CSI report configuration(s) configured with the higher layer parameter eventType is further associated with other CSI report configurations that are not configured with the higher layer parameter eventType. <Irrelevant part is omitted> |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508094](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508094.zip) · `[122bis-R19-MIMO]`

**Agreement** · `8.2` Maintenance on NR MIMO Phase 5 · `RAN1#122bis:8.2:007`

> Adopt the following changes in TS38.213 Section 9:
> - Reason for change: Reusing the intra-UE multiplexing/prioritization rules of PUSCH with A-CSI for PUSCH for UEI-BR for Mode A was agreed. However, it is not captured in the current specification.
> - Summary of change: In TS38.213 section 9, clarify the intra-UE multiplexing/prioritization rules of PUSCH with A-CSI for PUSCH is reused for UEI-BR for Mode A.
> - Consequences if not approved: UE behavior is not clear when PUSCH carrying UEI-BR for Mode A overlaps with other uplink channels/RSs.
> | 9 UE procedure for reporting control information < Unchanged parts are omitted > For the remaining of this clause, when a UE - is not provided coresetPoolIndex or is provided coresetPoolIndex with a value of 0 for first CORESETs, and is provided coresetPoolIndex with a value of 1 for second CORESETs, on active DL BWPs of serving cells, and - is provided sTx-2Panel the UE separately determines and resolves time overlapping among first PUSCH transmissions that use respective first spatial domain filters corresponding to first TCI-State or TCI-UL-State associated with the first CORESETs, and among second PUSCH transmissions that use respective second spatial domain filters corresponding to second TCI-State or TCI-UL-State associated with the second CORESETs. For the remaining of this clause, reference to PUSCH with semi-persistent CSI reports includes a PUSCH with UE initiated reports when reportTransmissionMode is configured as ‘ModeB’ in the CSI report configuration [6, TS 38.214]. For the remaining of this clause, unless otherwise stated, reference to PUSCH with aperiodic CSI reports includes a PUSCH with UE initiated report when reportTransmissionMode is configured as ‘ModeA’ in the CSI report configuration [6, TS 38.214]. For the remaining of this clause, for a UE operating on an NTN serving cell, the timeline conditions for resolving time overlapping between a PUSCH transmission with repetitions in an OCC group [6, TS 38.214] and PUCCH transmissions are applicable with respect to the first repetition of the PUSCH transmission in the OCC group - if the UE would multiplex UCI from the PUCCH transmissions in the PUSCH, the UE multiplexes the UCI in all repetitions of the PUSCH transmission in the OCC group - if the UE would not transmit a repetition of the PUSCH transmission, the UE does not transmit all repetitions of the PUSCH transmission in the OCC group - the UE does not expect to transmit in different slots more than one PUCCHs that provide HARQ-ACK information or CSI reports and would overlap with the PUSCH transmission in the OCC group When a UE determines overlapping for PUCCH transmissions with SL HARQ-ACK reports and PUCCH of larger and/or smaller priority index, the UE resolves the overlapping for PUCCH transmissions with SL HARQ-ACK reports and PUCCH of each priority index as described in clause 9.2.5 and 9.2.6 before resolving the overlapping for PUCCH transmissions without SL HARQ-ACK or the overlapping for PUCCH transmissions and PUSCH transmissions. < Unchanged parts are omitted > |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508094](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508094.zip) · `[122bis-R19-MIMO]`

## RAN1#122 — 15건

**Agreement** · `8.2.1` Enhancements for UE-initiated/event-driven beam management · `RAN1#122:8.2.1:001`

> Adopt the following changes in TS38.213 Section 9.2.5.1:
> - Reason for change: In the last meeting, when the PUCCH resource for UE-initiated/event-driven beam reporting is collided/overlapped with a PUCCH format 2/3/4 carrying CSI/SR, the multiplexing rule that was agreed in RAN1#121.  However, in the current specification, only the priority rule of LRR, UEIRI and normal SR is captured when the PUCCH resource for UE-initiated/event-driven beam reporting is collided/overlapped with a PUCCH format 2/3/4 carrying CSI/SR.
> - Summary of change: In TS38.213 section 9.2.5.1, add the case of no positive LRR and at least one positive UEIBRs to the multiplexing rule of PUCCH with UEIBR.
> - Consequences if not approved: UE behavior is unclear for the case of no positive LRR and at least one positive UEIBRs, when the PUCCH resource for UE-initiated/event-driven beam reporting is collided/overlapped with a PUCCH format 2/3/4 carrying CSI/SR.
> | 9.2.5.1 UE procedure for multiplexing HARQ-ACK or CSI and SR in a PUCCH < Unchanged parts are omitted > If a UE would transmit a PUCCH with HARQ-ACK information bits in a resource using PUCCH format 2 or PUCCH format 3 or PUCCH format 4 in a slot, as described in clauses 9.2.1 and 9.2.3, bits representing a negative or positive SR/UEIRI, in ascending order of the values of schedulingRequestResourceId, a schedulingRequestResourceId associated with schedulingRequestID-BFR-SCell, a schedulingRequestResourceId associated with schedulingRequestID-BFR, a schedulingRequestResourceId associated with schedulingRequestID-BFR2 if the UE provides twoLRRcapability, and a schedulingRequestResourceId associated with schedulingRequestID-LBT-SCell for SR, and then in ascending order of the values of pucch-ResourceId for UEIRI, are appended to the HARQ-ACK information bits and the UE transmits the combined UCI bits in a PUCCH using a resource with PUCCH format 2 or PUCCH format 3 or PUCCH format 4 that the UE determines as described in clauses 9.2.1 and 9.2.3. If one of the SRs is a positive LRR, the value of the bits indicates the positive LRR; else, if one of the UEIRIs is a positive UEIRI, the value of the bits indicates the positive UEIRI. An all-zero value for the bits represents a negative SR/UEIRI value across all SRs and UEIRIs. If a UE would transmit a PUCCH with CSI report bits in a resource using PUCCH format 2 or PUCCH format 3 or PUCCH format 4 in a slot, bits representing corresponding negative or positive SR/UEIRI, in ascending order of the values of schedulingRequestResourceId, a schedulingRequestResourceId associated with schedulingRequestID-BFR-SCell, a schedulingRequestResourceId associated with schedulingRequestID-BFR, a schedulingRequestResourceId associated with schedulingRequestID-BFR2 if the UE provides twoLRRcapability, and a schedulingRequestResourceId associated with schedulingRequestID-LBT-SCell for SR, and then in ascending order of the values of pucch-ResourceId for UEIRI, are prepended to the CSI information bits as described in clause 9.2.5.2 and the UE transmits a PUCCH with the combined UCI bits in a resource using the PUCCH format 2 or PUCCH format 3 or PUCCH format 4 for CSI reporting. If one of the SRs is a positive LRR, the value of the bits indicates the positive LRR; else, if one of the UEIRIs is a positive UEIRI, the value of the bits indicates the positive UEIRI. An all-zero value for the bits represents a negative SR/UEIRI value across all SRs and UEIRIs. |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506253](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506253.zip)

**Agreement** · `8.2.1` Enhancements for UE-initiated/event-driven beam management · `RAN1#122:8.2.1:004`

> Adopt the following changes in TS38.214 Section 5.2.1.5.4.1d:
> - Reason for change: In TS38.214 [3], the CSI report identifier in the beam report format is captured as CSI-ReportConfigID. However, according to the related agreement, the CSI report identifier is determined based on the order of the triggered CSI report in the CSI report configurations associated with the same PUCCH resource. Thus, the specification description is aligned with the agreement only when all CSI report configurations in a CC are associated with the same PUCCH resource.
> - Summary of change: In TS38.214 section 5.2.1.5.4.1d, clarify the determination of a CSI report identifier in the report format when multiple CSI report configurations are associated with one PUCCH resource.
> - Consequences if not approved: The spec is not aligned with the agreement.
> | 5.2.1.5.4.1d UE Initiated CSI reporting for multiple CSI configurations For a UE configured with multiple CSI-ReportConfig with same higher layer parameters eventType and PUCCHResource, the UE expects - the multiple CSI-ReportConfig to be configured in the same CC, - the multiple CSI-ReportConfig to be associated with a same CSI trigger state if reportTransmissionMode is configured as ‘ModeA’, else - the same configuredPUSCHResourceOfModeB if reportTransmissionMode is configured as ‘ModeB’. The UE reports in a single reporting instance nrofReportedRS-UEIBR CRIs or SSBRIs corresponding to reference signals provided by the newBeamResourceSet in a CSI-ReportConfig that satisfies the event. The CSI report includes the corresponding CSI-ReportConfigId CSI report configuration indicator as defined in Table 6.3.2.1.2-3I in [5, TS38.212] corresponding to the CSI-ReportConfig the and is zero padded to a fixed payload size (when needed), with the fixed payload size given by the maximum payload size among all the multiple CSI-ReportConfig. |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506253](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506253.zip)

**Agreement** · `8.2.1` Enhancements for UE-initiated/event-driven beam management · `RAN1#122:8.2.1:005`

> Adopt the following changes in Section 5.4 in TS 38.214.
> - Reason for change: Legacy CSI reference definition of aperiodic CSI reporting is reused for mode-A and definition of Z' for mode-B follows the legacy definition, hence we should capture the agreement by declaring that  and  defined for legacy beam report are used for UEI-CSI report as well.
> - Summary of change: Clarifying that  and  defined for legacy beam report are used for UEI-CSI report as well.
> - Consequences if not approved: Z/Z' definition for UEI-CSI report is unclear.
> | 5.4 UE CSI computation time <Irrelevant part is omitted> - of the table 5.4-2 if reportQuantity is set to 'cri-RSRP', 'ssb-Index-RSRP', 'cri-RSRP- Index' or 'ssb-Index-RSRP- Index ', is according to UE reported capability beamReportTiming and KBl is according to UE reported capability beamSwitchTiming as defined in [13, TS 38.306], or if the CSI report is configured with ltm-CSI-ReportConfig for L1-RSRP measurement, or if the CSI report is configured with eventType, or |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506253](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506253.zip)

**Agreement** · `8.2.1` Enhancements for UE-initiated/event-driven beam management · `RAN1#122:8.2.1:006`

> Adopt the following changes in TS38.214 Section 5.2.1.5.4.1:
> - Reason for change: Besides for correcting typos, when “current” beam RS for event evaluation is SSB QCLed with RS in an activated TCI state, the SSB having the Q-th best quality among all SSBs QCLed with the RSs in all the activated TCI states should be clarified:
> - Summary of change:
>   - In TS38.214 section 5.2.1.5.4.1, add “state” after “indicated TCI”.
>   - In TS38.214 section 5.2.1.5.4.1c, clarify the current beam RS determination when enabledCurrentBeamReport is configured for event-7.
> - Consequences if not approved: It can cause inconsistency in the specification description.
> | 5.2.1.5.4.1 UE Initiated CSI reporting For a UE configured with a CSI-ReportConfig with eventType for periodic reference signals with the same periodicity configured by the newBeamResourceSet, without eventDetectionTimeWindowLength, and with dl-OrJointTCI-StateList, when an event instance is determined (as described in the following clauses), - for a reference signal configured by the newBeamResourceSet, if eventType is set to ‘event2’ or ‘event7’, or - for the reference signal in the indicated TCI state or the SS/PBCH block which is QCLed with the reference signal in the indicated TCI state, if eventType is set to ‘event1’, the UE transmits UEIRI on a PUCCH format 0 or format 1 in the PUCCH resource (in the CC provided by pucchCell, if configured, in the CSI-ReportConfig) configured by PUCCHResource in the CSI-ReportConfig. For a UE configured with a CSI-ReportConfig with eventType for periodic reference signals with the same periodicity configured by the newBeamResourceSet, with eventDetectionTimeWindowLength, and with dl-OrJointTCI-StateList, when an event instance is determined (as described in the following clauses), - for a reference signal configured by the newBeamResourceSet, if eventType is set to ‘event2’ or ‘event7’, or - for the reference signal in the indicated TCI state or the SS/PBCH block which is QCLed with the reference signal in the indicated TCI state, if eventType is set to ‘event1’, the UE - starts a timer for such reference signal from the initial value equal to the time window length provided by eventDetectionTimeWindowLength and sets the counter to 1, if the timer for such reference signal is not running; or - increments the counter for such reference signal by 1, if the timer for such reference signal is running. < Unchanged parts are omitted > 5.2.1.5.4.1c UE Initiated CSI reporting for event 7 < Unchanged parts are omitted > After transmitting UEIRI, the UE reports, as defined in Clause 6.3.2.1.2 of [5, TS 38.212] in a single reporting instance nrofReportedRS-UEIBR CRIs or SSBRIs corresponding to reference signals provided by the newBeamResourceSet that comprise at least one reference signal that triggers the UEIRI transmission. For each CRI or SSBRI, the CSI report includes the absolute L1-RSRP or differential L1-RSRP and, when PresenceOfConditionMetIndicator is configured a condition met indicator indicating whether the reference signal indicated by reported CRI or SSBRI triggers the UEIRI transmission and, when enabledCurrentBeamReport is configured, the differential L1-RSRP corresponding to the reference signal with the valueOfQ-th highest L1-RSRP out of the activated TCI state reference signals, or to the SS/PBCH block with the valueOfQ-th highest L1-RSRP out of the SS/PBCH blocks QCLed with the activated TCI state reference signals which is QCLed with the reference signal with the valueOfQ highest L1-RSRP out of the activated TCI state reference signals. The UE sends the CSI report - on a PUSCH indicated by the DCI format 0_1/0_2 in a PDCCH reception if reportTransmissionMode is configured as ‘ModeA’ and the CSI trigger state associated with the CSI-ReportConfig is indicated in the CSI request field in the DCI format 0_1/0_2, or - on a type 1 CG-PUSCH configured by configuredPUSCHResourceOfModeB in the same CC as the corresponding CSI-ReportConfig, on the first available transmission occasion numOfSymbols-ModeB symbols after the end of the transmitted PUCCH if reportTransmissionMode is configured as ‘ModeB’, where the periodicity of the PUCCH resource and type 1 CG-PUSCH resource is the same, numOfSymbols-ModeB is based on the numerology of the PUCCH resource with UEIRI transmitted, and the CG-PUSCH does not carry UL-SCH. < Unchanged parts are omitted > |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506253](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506253.zip)

**Agreement** · `8.2.1` Enhancements for UE-initiated/event-driven beam management · `RAN1#122:8.2.1:008`

> On beam report transmission procedure for UE-initiated/event-driven beam reporting, occupation time of occupied CPU(s) starts when CSI report configuration for the UEI beam report is configured, and ends when it is released.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506255](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506255.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:005`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-1-2 | UE-initiated/event-driven beam management Mode B | 1. Support of Mode B UE-initiated/event-driven beam report 32. Supported minimum value of X symbols between the last symbol of sending first PUCCH and the first available symbol of transmission occasion of second PUSCH | 59-1-1 FFS for other potential FG(s) | yes | n/a | UEI/ED beam report Mode-B is not supported | Per band | n/a | n/a | n/a | Component 32 candidate values: [{0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512}] 15kHz SCS: {0,1,2,4,8,16} 30kHz SCS: {0,2,4,8,16,32} 60kHz SCS: {0,4,8,32,64} 120kHz SCS: {0,8,16,32,64,128} 480kHz SCS: {0,32,64,128,256,512} 960kHz SCS: {0,64,128,256,512} | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:006`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-1-3 | Triggering event determination via detecting ≥ M event instances for at least one new beam within a time window. | Triggering 1. Support of UEI/ED UE initiated/event driven beam report procedure via detecting ≥ M event instance(s) for at least one new beam within a time window, where M>1 2. Maximum number of timers | 59-1-1 FFS for other potential FG(s) | yes | n/a | Triggering event determination via detecting ≥ M event instances within a time window is not supported | Per band | n/a | n/a | n/a | Component 2 candidate values: {1, 2, …, 64} | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:012`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-1-1 | UE-initiated/event-driven beam management for Event-2 based measurement and report for Mode A | 1. Support of UE-initiated/event-driven beam report based on one event instance 2. Support of Event-2 based measurement and report 3. Support of Mode A UE-initiated/event-driven beam report 4. Maximum number of the configured RS(s) for new beam in the RS resource set 5. Support of current beam measurement by using QCL RS in the indicated TCI state and the corresponding QCL SSB for Scheme-1 and Scheme-2, respectively 6. Support the first PUCCH and second PUSCH from the same PUCCH group | FFS | yes | n/a | UEI/ED beam report is not supported for Event-2 and Mode A | Per band | n/a | n/a | n/a | Component 4 candidate values: {1, 2, …, 64} Note For Component 4 and Component 5, an SSB can be associated with the serving cell PCI or a PCI other than the serving cell PCI | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:013`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-1-5 | UE-initiated/event-driven beam management for Event-7 based measurement and report for Mode A | 1. Support of Event-7 based measurement and report for Mode A that L1-RSRP of at least one new beam becomes a threshold value better than the RS derived from the activated TCI state with the Q-th best quality based on one event instance 23. Support of the RS derived from the activated TCI state with the Q-th best quality measurement by using QCL RS in the activated TCI state with the Q-th best quality and the corresponding QCL SSB for the activated TCI state with the Q-th best quality for Scheme-1 and Scheme-2, respectively | 59-1-1 | yes | n/a | UE-initiated/event-driven beam management for Event-7 based measurement is not supported for Mode A | Per Band | n/a | n/a | n/a | Component 1 candidate values for Q: bitmap of size 8, the n-th bit signals support for Q=n, n = 1,2,…,8, zero means no support, 1 means support Note: The UE does not expect that the configured Q is greater than the number of the activated DL/joint TCI state(s) Note: For Component 2, an SSB can be associated with the serving cell PCI or a PCI other than the serving cell PCI | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:021`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-3-6a | New CJT QCL assumptions for PDSCH pre-compensation for Scheme-C | The PDSCH DMRS port(s) are QCLed with the DL-RS associated with the first TCI state with respect to QCL-TypeA and QCLed with the DL-RS in the second TCI state with respect to QCL-TypeA except for {Doppler shift} | FFS 40-1-1 | yes | n/a | New QCL assumptions for PDSCH pre-compensation is not supported for Scheme-C | Per band | n/a | n/a | n/a |  | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:022`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-3-6b | New CJT QCL assumptions for PDSCH pre-compensation for Scheme-D | 1. The PDSCH DMRS port(s) are QCLed with the DL-RS associated with the first TCI state with respect to QCL-TypeA and QCLed with the DL-RS in the second TCI state with respect to QCL-TypeA except for {average delay} | FFS 40-1-1 | yes | n/a | New QCL assumptions for PDSCH pre-compensation is not supported for Scheme-D | Per band | n/a | n/a | n/a |  | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:023`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-3-6c | New CJT QCL assumptions for PDSCH pre-compensation for Scheme-E | 1.The PDSCH DMRS port(s) are QCLed with the DL-RS associated with the first TCI state with respect to QCL-TypeA and QCLed with the DL-RS in the second TCI state with respect to QCL-TypeA except for {Doppler shift, average delay} | FFS 40-1-1 | yes | n/a | New QCL assumptions for PDSCH pre-compensation is not supported for Scheme-E | Per band | n/a | n/a | n/a |  | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:046`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-1-1 | UE-initiated/event-driven beam management for Event-2 based measurement and report for Mode A | 1. Support of UE-initiated/event-driven beam report based on one event instance 2. Support of Event-2 based measurement and report 3. Support of Mode A UE-initiated/event-driven beam report 4. Maximum number of the configured RS(s) for new beam in the RS resource set 5. Support of current beam measurement by using QCL RS in the indicated TCI state and the corresponding QCL SSB for Scheme-1 and Scheme-2, respectively 6. Support the first PUCCH and second PUSCH from the same PUCCH group |  | yes | n/a | UEI/ED beam report is not supported for Event-2 and Mode A | Per band | n/a | n/a | n/a | Component 4 candidate values: {1, 2, …, 64} Note For Component 4 and Component 5, an SSB can be associated with the serving cell PCI or a PCI other than the serving cell PCI Note: Regarding Event-2, QCL RS(s) in indicated TCI state(s) and resources configured for component 4 are also counted in FG 16-1g, and 16-1g-1 | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:047`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-1-4 | UE-initiated/event-driven beam management for Event-1 based measurement and report for Mode A | 1. Support of Event-1 based measurement and report for Mode A that L1-RSRP of the current beam becomes worse than a configured threshold based on one event instance | 59-1-1 | yes | n/a | UE-initiated/event-driven beam management for Event-1 based measurement is not supported for Mode A | Per Band | n/a | n/a | n/a | Note: the event definition Event 1: Quality of the current beam is worse than a certain threshold Note: Regarding Event-1, QCL RS(s) in indicated TCI state(s) and resources configured for component 4 of FG 59-1-1 are also counted in FG 16-1g, and 16-1g-1 | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:048`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-1-5 | UE-initiated/event-driven beam management for Event-7 based measurement and report for Mode A | 1. Support of Event-7 based measurement and report for Mode A that L1-RSRP of at least one new beam becomes a threshold value better than the RS derived from the activated TCI state with the Q-th best quality based on one event instance 2. Support of the RS derived from the activated TCI state with the Q-th best quality measurement by using QCL RS in the activated TCI state with the Q-th best quality and the corresponding QCL SSB for the activated TCI state with the Q-th best quality for Scheme-1 and Scheme-2, respectively | 59-1-1 | yes | n/a | UE-initiated/event-driven beam management for Event-7 based measurement is not supported for Mode A | Per Band | n/a | n/a | n/a | Component 1 candidate values for Q: bitmap of size 8, the n-th bit signals support for Q=n, n = 1,2,…,8, zero means no support, 1 means support Note: The UE does not expect that the configured Q is greater than the number of the activated DL/joint TCI state(s) Note: Regarding Event-7, the number of QCL RS(s) in activated TCI state(s) and resources configured for component 4 of FG 59-1-1 are also counted in FG 16-1g, and 16-1g-1 Note: For Component 2, an SSB can be associated with the serving cell PCI or a PCI other than the serving cell PCI | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

---

## 후보 64건 (키워드 일치 · 확인 필요)

포함 Agenda 밖에서 키워드로 잡힌 결정입니다. CSI 범위가 아닐 수 있습니다.

### RAN1#126bis — 5건

**Agreement** · `10.5.2.2` Downlink transmission scheme(s) for downlink shared channels · `RAN1#126bis:10.5.2.2:009` · 후보 · 🆕 신규

> - Support the Gold sequence for DMRS sequence generation to be a length-31 Gold sequence
> - Support different DMRS sequences for DMRS ports in different CDM groups
> - Study at least the following options for the DMRS scrambling ID indication
>   - Option 1: The scrambling ID is indicated by DCI based on N scrambling IDs configured by the aNB
>     - FFS: The value of N
>   - Option 2: The scrambling ID is associated with the TCI state applied for the PDSCH

남은 FFS 1건

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · [R1-2607734](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2607734.zip) · `[126bis-R20-6GR-Transmission scheme for DL shared channel]`

**Agreement** · `10.5.5` Other physical layer signals, channels and procedure · `RAN1#126bis:10.5.5:004` · 후보 · 🆕 신규

> For UE-initiated UE-to-UE CLI (UEI CLI) reporting, at least the following aspects are to be studied:
> - The configuration of UE-to-UE CLI measurement resources/occasions for CLI event detection.
> - The measurement metric used for CLI event detection: non-filtered L1-RSRP/L1-RSSI or filtered L1-RSRP/L1-RSSI.
>   - Note: Both filtered and non-filter L1-RSRP/L1-RSSI can be applied to all the following candidates/options.
> - For the CLI reporting triggering procedure, at least considering the following candidates:
>   - Candidate 1: one or more CLI measurement resources/ occasions have RSRP/RSSI measurement > configured threshold for consecutive N >=1 times.
>   - Candidate 2: one or more CLI measurement resources/occasions have RSRP/RSSI measurement > configured threshold for at least N times within a given time duration length.
> - Consider the following options for UE-initiated CLI reporting mechanisms:
>   - Option 1: MAC CE based CLI reporting.
>   - Option 2: RRC-based reporting.
>   - Option 3: L1 CLI reporting:
>     - Option 3-1: The UE is configured with a PUCCH resource for sending a notification of occurrence of CLI event to BS and the BS can then schedule a PUSCH resource for the UE to send CLI reporting.
>     - Option 3-2: The UE is configured with a first PUCCH resource and a second PUSCH/PUCCH resource. When CLI event is detected, the UE sends notification of occurrence of CLI event in the first PUCCH resource and sends CLI reporting in the associated second PUSCH/PUCCH resource.
>     - Option 3-3: The UE is provided with a preconfigured PUSCH/PUCCH for UE to report CLI reporting.
>     - Other option is not precluded.
> - Note: the reporting overhead, latency reporting reliability and specification complexity of UEI CLI reporting (with pre-configured (if any) or with requested reporting resources)) is to be compared with network-controlled CLI reporting.

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Other signals, channels, and procedures]`

**Agreement** · `10.6.3` WUS operation with other functionalities · `RAN1#126bis:10.6.3:001` · 후보 · 🆕 신규

> - For UEs in RRC_CONNECTED state, RAN1 to study at least the following candidate additional functions for DL-WUS,
>   - Candidate-1: Interaction between DL-WUS and Cell DTX or Cell DRX,
>   - Candidate-2: DL-WUS interacts with ‘Cell/Carrier Dormancy/(De)activation’ Operation
>   - Candidate-3: Use DL-WUS as a trigger or indication for on-demand and/or additional RS and/or common signals/channels and/or CSI report, if supported.
>   - Candidate-4: Study DL-WUS to indicate throughput reduction for subsequent active time
>   - Candidate-5: DL WUS carries acknowledgement information (ACK/NACK) in response to a UE request for UL data transmission
>   - Candidate-6: DL WUS indicating beam parameter/TCI update
>   - Candidate 7: DL-WUS triggers DL-SPS PDSCH reception.
>   - Candidate 8: DL-WUS activates/de-activates CG-PUSCH transmission.
>   - Note: 5G NR design is assumed as starting point and further RAN1 and RAN2 progress on relevant features are considered, if applicable.
> Note: Interaction between DL-WUS and PDCCH monitoring adaption (at least including ‘SSSG switching’ / monitoring-config selection, PDCCH skipping, ‘PDCCH BD reduction’) are to be handled under AI 10.6.1.2.

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-WUS operation with other functionalities]`

**Agreement** · `10.8.2` Aspects of integration with communication · `RAN1#126bis:10.8.2:002` · 후보 · 🆕 신규

> - Study at least the following beam related aspects for Rel-20 ISAC taking communication beam management as starting point, to identify whether sensing specific enhancement on beam related aspects for sensing is necessary or not
>   - Measurement/report/information to determine best Tx-Rx beam pair(s) for sensing
>   - QCL/TCI state or spatial-relation assumptions of sensing RS

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-ISAC-Integration]`

**Agreement** · `10.8.2` Aspects of integration with communication · `RAN1#126bis:10.8.2:008` · 후보 · 🆕 신규

> Study at least the following aspects for a sensing RS resource consisting of one or multiple component RS
> - The multiple component RS have the same [QCL, Tx beamforming, spatial transmit filter, spatial transmit reference, antenna port(s)] and can be assumed to be transmitted coherently

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · [R1-2607233](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2607233.zip) · `[126bis-R20-6GR-ISAC-Integration]`

### RAN1#126 — 9건

**Agreement** · `8.1` Maintenance on AI/ML for NR Air interface, NR MIMO Phase 5,  NES and NTN for NR and IoT · `RAN1#126:8.1:004` · 후보

> The following TP for TS 38.214 Clause 5.1.6.1.2.
> The corresponding CR for Rel-19, TS 38.214 Clause 5.1.6.1.2 in R1-2606879 is endorsed.
> Reason for change: A new RRC IE CSI-LoggedMeasurementConfig is defined in 38.331 for network-side data collection, which is used to configure UE to perform the logging of measurements on CSI-RS resources. For CSI-RS measurement configured by the IE CSI-ReportConfig for L1 CSI report, there are some descriptions and constraints in spec 38.214, which are also needed for CSI-RS measurement configured by the IE CSI-LoggedMeasurementConfig for L3 CSI report.
> Summary of change: Add descriptions and constraints for CSI-RS measurement configured by the IE CSI-LoggedMeasurementConfig (L3 CSI report) in 38.214.
> Consequences if not approved: The descriptions and constraints for CSI-RS measurement configured by the IE CSI-LoggedMeasurementConfig (L3 CSI report) are missing in 38.214.
> | 5.1.6.1.2 CSI-RS for L1-RSRP and L1-SINR computation If a UE is configured with a NZP-CSI-RS-ResourceSet configured with the higher layer parameter repetition set to 'on', the UE may assume that the CSI-RS resources, described in Clause 5.2.2.3.1, within the NZP-CSI-RS-ResourceSet are transmitted with the same downlink spatial domain transmission filter, where the CSI-RS resources in the NZP-CSI-RS-ResourceSet are transmitted in different OFDM symbols. If repetition is set to 'off', the UE shall not assume that the CSI-RS resources within the NZP-CSI-RS-ResourceSet are transmitted with the same downlink spatial domain transmission filter. If the UE is configured with a CSI-ReportConfig with reportQuantity set to 'cri-RSRP', 'cri-SINR', 'cri-RSRP-Index', 'cri-SINR-Index', 'none', 'p-cri-r19', 'p-cri-RSRP-r19', 'p-ssb-index-r19', 'p-ssb-index-RSRP-r19', 'none-bm-r19', or 'rs-pai-r19', and if the CSI-ResourceConfig for channel measurement (higher layer parameters resourcesForChannelMeasurement and resourcesForSetA-r19 when reportQuantity set to 'none-bm-r19') contains a NZP-CSI-RS-ResourceSet that is configured with the higher layer parameter repetition and without the higher layer parameter trs-Info, the UE can only be configured with the same number (1 or 2) of ports with the higher layer parameter nrofPorts for all CSI-RS resources within the set. If the UE is configured with the CSI-RS resource in the same OFDM symbol(s) as an SS/PBCH block, the UE may assume that the CSI-RS and the SS/PBCH block are quasi co-located with 'typeD' if 'typeD' is applicable. Furthermore, the UE shall not expect to be configured with the CSI-RS in PRBs that overlap with those of the SS/PBCH block, and the UE shall expect that the same subcarrier spacing is used for both the CSI-RS and the SS/PBCH block. If the UE is configured with a CSI-LoggedMeasurementConfig, and if the CSI-ResourceConfig for channel measurement (higher layer parameters csi-LoggedResourceConfig) contains a NZP-CSI-RS-ResourceSet that is configured with the higher layer parameter repetition and without the higher layer parameter trs-Info, the UE can only be configured with the same number (1 or 2) of ports with the higher layer parameter nrofPorts for all CSI-RS resources within the set. Each Reporting Setting CSI-LoggedMeasurementConfig is associated with a single downlink BWP (indicated by higher layer parameter BWP-Id) given in the associated CSI-ResourceConfig for channel measurement. <omitted texts> |
> MIMO

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606835](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606835.zip) · `[126-R19-AI 8.1]`

**Agreement** · `8.1` Maintenance on AI/ML for NR Air interface, NR MIMO Phase 5,  NES and NTN for NR and IoT · `RAN1#126:8.1:005` · 후보

> The following changes for Clause 9.2 in TS 38.213 is endorsed.
> The corresponding CR for Rel-19, TS 38.213 in R1-2606868 is endorsed.
> - Reason for change: In Rel-19, UEIRI is introduced as a new type of UCI for notifying (ModeA) or requesting a PUSCH resource (ModeB) for UE-initiated/event-driven beam reporting. Whether UE transmits UEIRI on a PUCCH format 0 or format 1 in the PUCCH resource depends on whether the triggering condition of the event(s) for UE-initiated/event-driven beam reporting is met or not. In this case, the information bit of UEIRI is not always included in the PUCCH resource. However, in the current spec, UEIRI is described as a compulsory UCI in the PUCCH resource, which is not correct.
> - Summary of change: Add the condition “if any” to the information bit for UEIRI where the contents of UCI bit(s) are described in the first paragraph of Section 9.2, TS38.213.
> - Consequences if not approved: The availability of information bit for UEIRI in PUCCH is not correctly stated.
> | 9.2 UCI reporting in physical uplink control channel UCI types reported in a PUCCH include HARQ-ACK information, SR, LRR, UEIRI, and CSI. UCI bits include HARQ-ACK information bits, if any, SR information bits, if any, LRR information bit, if any, UEIRI information bit, if any, and CSI bits, if any. The HARQ-ACK information bits correspond to a HARQ-ACK codebook as described in clause 9.1. For the remaining of this clause, unless stated otherwise in clauses 9.2.4A and 9.2.5.1, any reference to SR is applicable for SR and/or for LRR and/or for UEIRI. <Unchanged parts are omitted> |

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606809](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606809.zip) · `[126-R19-AI 8.1]`

**Conclusion** · `8.1` Maintenance on AI/ML for NR Air interface, NR MIMO Phase 5,  NES and NTN for NR and IoT · `RAN1#126:8.1:009` · 후보

> There is no consensus in RAN1 to support the following change from R1-2605805 of Clause 5.2.1.5.4.1 in TS 38.214:
> | 5.2.1.5.4.1 UE Initiated CSI reporting <Unchanged parts are omitted> The counter of the event instances for such reference signal is reset: - if the reference signal in the indicated TCI state is updated and newBeamResourceSet is a NZP-CSI-RS-ResourceSet configured with repetition, or the SS/PBCH block which is QCLed with the reference signal in the indicated TCI state is updated and newBeamResourceSet is a CSI-SSB-ResourceSet when the UE is configured with a CSI-ReportConfig with the higher layer parameter eventType set to ‘event2’ or ‘event1’, or - if the reference signal with the valueOfQ-th highest L1-RSRP out of the reference signals among the activated TCI states is updated and newBeamResourceSet is a NZP-CSI-RS-ResourceSet configured with repetition, or the SS/PBCH block with the valueOfQ-th highest L1-RSRP out of the SS/PBCH blocks QCLed with the reference signals among the activated TCI states, which determines event instance(s), is updated and newBeamResourceSet is a CSI-SSB-ResourceSet when the UE is configured with a CSI-ReportConfig with the higher layer parameter eventType set to ‘event7’, or - if eventThreshold or valueOfQ or eventInstanceCount or eventDetectionTimeWindow in the CSI-ReportConfig are reconfigured. <Unchanged parts are omitted> |

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606867](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606867.zip) · `[126-R19-AI 8.1]`

**Agreement** · `8.1` Maintenance on AI/ML for NR Air interface, NR MIMO Phase 5,  NES and NTN for NR and IoT · `RAN1#126:8.1:012` · 후보

> The following TP for TS 38.211 Clause 6.3.3.1 is endorsed.
> The corresponding CR for Rel-19, TS 38.211 in R1-2606849 is endorsed.
> | Reason for change: The parameter sib1-RestrictedSetConfig of UL-WUS configuration for SIB1 request in TS 38.331 is not captured in TS 38.211. Summary of change: Add description for parameter sib1-RestrictedSetConfig of TS 38.211 according to the IE sib1-RestrictedSetConfig defined in the TS 38.331. Consequence if not approved: Ambiguity occurs for the sib1-RestrictedSetConfig for on demand SIB1. 6.3.3 Physical random-access channel 6.3.3.1 Sequence generation The set of random-access preambles shall be generated according to from which the frequency-domain representation shall be generated according to where , , , or depending on the PRACH preamble format as given by Tables 6.3.3.1-1 and 6.3.3.1-2. There are 64 preambles defined in each time-frequency PRACH occasion, enumerated in increasing order of first increasing cyclic shift of a logical root sequence, and then in increasing order of the logical root sequence index, starting with the index obtained from the higher-layer parameter - prach-RootSequenceIndex or rootSequenceIndex-BFR or by msgA-PRACH-RootSequenceIndex if configured and a type-2 random-access procedure is initiated as described in clause 8.1 of [5, TS 38.213], or by - prach-RootSequenceIndex in EarlyUL-SyncConfig if the PRACH transmission is for a candidate cell, or by - prach-RootSequenceIndex in RACH-ConfigTwoTA if the PRACH transmission is associated with an additional PCI different from serving cell PCI, or by - prach-RootSequenceIndex in SIB1-RequestConfig if the PRACH transmission is for SIB1 request. Additional preamble sequences, in case 64 preambles cannot be generated from a single root Zadoff-Chu sequence, are obtained from the root sequences with the consecutive logical indexes until all the 64 sequences are found. The logical root sequence order is cyclic; the logical index 0 is consecutive to . The sequence number is obtained from the logical root sequence index according to Tables 6.3.3.1-3 to 6.3.3.1-4B. The cyclic shift is given by where is given by Tables 6.3.3.1-5 to 6.3.3.1-7. The type of restricted sets (unrestricted, restricted type A, restricted type B) is given by - the higher-layer parameter msgA-RestrictedSetConfig, if provided; - or the higher-layer parameter ltm-restrictedSetConfig associated with a candidate cell indicated in Cell indicator field of a PDCCH order, if provided; - or the higher-layer parameter twoTA-restrictedSetConfig associated with an additional PCI indicated in PRACH association indicator field of a PDCCH order, if provided; - otherwise, the higher-layer parameter restrictedSetConfig. < Unchanged Text Omitted > |

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606825](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606825.zip) · `[126-R19-AI 8.1]`

**Agreement** · `8.2` Maintenance on others · `RAN1#126:8.2:011` · 후보

> Adopt the following TP to TS 38.214 clause 5.2.2.5 as alignment CR.
> | ============================ TP for TS 38.214 =============================== Reason for change: The RRC parameter configured to report periodic CSI when LP-WUS is configured is not aligned with the exact one in TS38.331. Summary of changes: “lpwus-TransmitOtherPeriodicL1-RSRP” is corrected to “lpwus-TransmitPeriodicL1-RSRP”. Consequence if not approved: UE behavior to report periodic CSI when LP-WUS is configured is unclear. ===========================Start of TP ================================== 5.2.2.5 CSI reference resource definition =========================== Unchanged Text Omitted ========================= - if the UE configured by higher layer parameter ps-TransmitPeriodicL1-RSRP or lpwus-TransmitPeriodicL1-RSRP to report L1-RSRP with the higher layer parameter reportConfigType set to 'periodic' and reportQuantity set to 'cri-RSRP', 'ssb-Index-RSRP', 'cri-RSRP- Index', or 'ssb-Index-RSRP- Index' when drx-onDurationTimer is not started, the UE shall report L1-RSRP during the time duration indicated by drx-onDurationTimer in DRX-Config also outside active time according to the procedure described in clause 5.2.1.4 and when reportQuantity set to 'cri-RSRP' or 'cri-RSRP- Index' if receiving at least one CSI-RS transmission occasion for channel measurement during the time duration indicated by drx-onDurationTimer in DRX-Config outside DRX active time or in DRX Active Time no later than CSI reference resource and drops the report otherwise. ========================== Unchanged Text Omitted ========================== ============================ End of TP =================================== |

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606855](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606855.zip) · `[126-R19-AI 8.2]`

**Agreement** · `10.5.2.2` Downlink transmission scheme(s) for downlink shared channels · `RAN1#126:10.5.2.2:010` · 후보

> - Consider the following for the co-schedule UE information indication/assumption for a target UE
>   - Study at least the following options for the DMRS ports for the co-scheduled UEs
>     - Option 0: The aNB indicates the CDM group(s) without data
>     - Option 1: The aNB indicates the CDM group(s) for the co-scheduled UEs
>     - Option 2: The aNB indicates the DMRS ports for the co-scheduled UEs within the same CDM group as the target UE
>     - Option 3: The aNB indicates the FD-OCC despreading length
>     - Option 4: The aNB indicates the DMRS port(s) for the co-scheduled UEs
>   - Study at least the following options for modulation order and/or coding scheme for the co-scheduled UEs
>     - Option 1: The aNB indicates modulation order for co-scheduled UE(s)
>     - Option 2: The aNB indicates modulation order and coding scheme for co-scheduled UE(s)
>     - Option 3: The target UE may assume modulation order and/or coding scheme for co-scheduled UE(s)
>   - Study at least the following options on the frequency domain DMRS density for the co-scheduled UE(s)
>     - Option 1: The target UE can assume the frequency domain DMRS density for the co-scheduled UE(s) is the same as the target UE
>     - Option 2: The aNB indicates the frequency domain DMRS density for the co-scheduled UE(s)
>   - Study at least the following options for the QCL/TCI for co-scheduled UE(s)
>     - Option 1: The target UE can assume the QCL/TCI for the co-scheduled UE(s) is the same as the target UE
>     - Option 2: The aNB indicates the QCL/TCI for the co-scheduled UE(s)
>     - Option 3: The target UE may determine any QCL/TCI information for co-scheduled UE(s).
>   - Support that a target UE can assume the time-domain location for the co-scheduled UE’s DMRS should be the same as the target UE’s DMRS
>   - FFS: The target UE can assume the PRG allocation for the co-scheduled UE(s) is the same as the target UE
>   - FFS: The target UE can assume the DMRS sequence for the co-scheduled UE(s) is the same or different as the target UE
>   - FFS: Whether the information above can be optional or not with regard to different types of UE receivers
>   - FFS: When the target UE can assume there is no co-scheduled UEs
>   - FFS: For each item above, the DCI bit count per co-scheduled UE and its scaling with the number of co-scheduled UEs

남은 FFS 5건

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606678](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606678.zip) · `[126-R20-6GR-Transmission scheme for DL shared channel]`

**Agreement** · `10.5.5` Other physical layer signals, channels and procedure · `RAN1#126:10.5.5:006` · 후보

> Study UE-initiated UE-to-UE CLI (UEI CLI) reporting with considering the following details:
> - The definition of CLI event is: when at least one RSRP/RSSI measurement larger than a configured threshold for a given time length, the CLI event is triggered.
>   - FFS: other CLI-related event(s).
> - Study and determine the measurement metric for CLI event detection:
>   - Option 1: non-filtered L1-RSRP/L1-RSSI
>   - Option 2: filtered L1-RSRP/L1-RSSI.
> - Study the CLI event detection procedure, report procedure and report contents.

남은 FFS 1건

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Other signals, channels, and procedures]`

**Agreement** · `10.6.2` Uplink WUS and operation · `RAN1#126:10.6.2:002` · 후보

> - For study of necessity for UL WUS, at least followings are considered as candidates of use cases.
>   - For UEs in idle mode,
>     - UE-initiated on-demand or adaptation procedures for one or multiple of the following signals/channels:
>       - 6GR SS/PBCH
>       - 6GR SIB1
>       - 6GR PRACH
>       - 6GR DL Reference Signal
>   - For UEs in connected mode,
>     - UE-initiated on-demand or adaptation procedures for one or multiple of the following signals/channels:
>       - 6GR SS/PBCH
>       - 6GR SIB1
>       - 6GR PRACH
>       - 6GR DL Reference Signal
>     - UL data indication (including ‘no UL data’ indication)
>     - Selection of PUSCH resource and/or PUSCH transmission parameter
>     - UL WUS based measurement
>     - Indication of new beam for BFR (if supported for 6GR)
> - With consideration of at least the following aspects:
>   - 6GR SSB/SIB1 periodicity/repetition
>   - Coverage
>   - UL WUS detection performance
>   - NW and UE energy/power consumption
>   - Latency
>   - NW and UE complexity
>   - Resource overhead
>   - Necessity of UE-triggered operation compared to NW-triggered mechanisms
>   - Which DS(s) are applicable to the above use cases
>   - Interference aspects
>   - Inter-node coordination
>   - Overlapping with existing or other 6GR mechanisms that could play the same functionalities

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Uplink WUS]`

**WA** · `10.8.2` Aspects of integration with communication · `RAN1#126:10.8.2:001` · 후보

> - The following representative use cases for sensing assisted communication is/are selected for study in Rel-20 ISAC
>   - Sensing assisted beam management
>   - [Sensing assisted CSI acquisition and reporting]
>   - Note: companies can also study other use cases for sensing assisted communication
> - Note: In AI10.8, physical layer design discussions are limited to sensing related aspects

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2605585](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2605585.zip) · `[126-R20-6GR-ISAC-Integration]`

### RAN1#125 — 3건

**Agreement** · `8.2` Maintenance on others · `RAN1#125:8.2:001` · 후보

> Adopt the following TP to TS38.213 Section 11.1 in principle.
> | Title Draft CR on avoiding ambiguity for UE transmission in SBFD flexible symbols Reason for change There is an ambiguity between the UE and the gNB regarding PUCCH or PUSCH transmission in flexible symbols indicated as SBFD by tdd-UL-DL-ConfigurationCommon and associated with PRACH transmission in first PRACH occasions. In this case, the UE may assume the flexible symbols as SBFD symbols, whereas the gNB may schedule the PUCCH or PUSCH transmission assuming the flexible symbols as non-SBFD symbols. Such ambiguity leads to UE/gNB misalignment in the following transmission behaviours: Selection of p0AlphaSetforPUSCH or p0AlphaSetforPUSCH-SBFD in Clause 7 of TS38.213 Selection of p0AlphaSetforPUCCH or p0AlphaSetforPUCCH-SBFD in Clause 7 of TS38.213 Selection of msgA-Alpha or msgA-Alpha-sbfd in Clause 7.1.1 of TS38.213 Selection of p0-nominal or p0-nominal-sbfd in Clause 7.2.1 of TS38.213 Time domain resource allocation according to Clause 6.1.2.1 and 6.1.2.1a of TS38.214 Frequency hopping according to Clauses 6.3.1 and 6.3.3 of TS38.214 Summary of change For a PUCCH or a PUSCH transmission in flexible symbols indicated as SBFD by tdd-UL-DL-ConfigurationCommon and associated with PRACH transmission in first PRACH occasions, the UE assumes the flexible symbols as non-SBFD symbols. Consequences if not approved UE/gNB ambiguity for PUCCH or PUSCH transmission in SBFD flexible symbols associated with PRACH transmission in first PRACH occasions remains unresolved, leading to inconsistent transmission behaviour. |
> | *** Unchanged parts are omitted *** 11.1 Slot configuration *** Unchanged parts are omitted *** A downlink or flexible symbol provided by tdd-UL-DL-ConfigurationCommon can include an UL sub-band provided by ul-SubbandlocationAndBandwidth, a first DL sub-band provided by firstDL-SubbandlocationAndBandwidth and may additionally include a second DL sub-band provided by secondDL-SubbandlocationAndBandwidth, for a SCS configuration of any configured UL BWP or DL BWP, respectively, as provided by scs-SpecificCarrierList [4, TS 38.211]. The downlink or flexible symbol is then referred to as an SBFD symbol; otherwise, it is referred to as a non-SBFD symbol. Unless otherwise stated, the UE considers symbols in a slot indicated as downlink and as SBFD by tdd-UL-DL-ConfigurationCommon to be available for transmissions. Uplink symbols by tdd-UL-DL-ConfigurationCommon are non-SBFD symbols. An SBFD symbol or a non-SBFD symbol provided by tdd-UL-DL-ConfigurationCommon cannot change to a non-SBFD symbol or to an SBFD symbol, respectively, by other information. The UE is not provided coresetPoolIndex and is not configured to receive PDSCH according to more than one TCI states mapped to one TCI codepoint [6, TS 38.214] for a serving cell where the UE is provided SBFD symbols. For a PUCCH or a PUSCH transmission in flexible symbols indicated as SBFD by tdd-UL-DL-ConfigurationCommon and associated with PRACH transmission in first PRACH occasions, the UE assumes the flexible symbols as non-SBFD symbols in this RACH attempt. *** Unchanged parts are omitted *** |
> Final CR in R1-2605127 is endorsed.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2605085](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2605085.zip)

**Agreement** · `8.2` Maintenance on others · `RAN1#125:8.2:007` · 후보

> Adopt the following TP to TS38.215 Section 5.1.1
> | Reason for change: | CSI-RS-based intra-frequency L1-RSRP measurement and inter-frequency L1-RSRP measurement for neighbor cell have been supported for LTM, but only CSI-RS-based intra-frequency L1-RSRP measurement is captured in TS38.215. Besides, in the last meeting, CR on adding the inter-frequency scenario to applicable scenarios of SS-RSRP for R18 LTM was agreed. But the corresponding description in the R19 specification has not been revised. |
> | Summary of change | Capture CSI-RS-based and SSB-based inter-frequency L1-RSRP measurement for neighbor cell in Rel-19 LTM. |
> | Consequences if not approved | CSI-RS-based inter-frequency L1-RSRP measurement and SSB-based inter-frequency L1-RSRP measurement for neighbor cell in Rel-19 LTM are not supported for Rel-19 LTM. |
> | Clauses affected | 5.1.1 |
> ---------------------------------------------Start of TP#3-2-------------------------------------------------------------
> 5.1.1	SS reference signal received power (SS-RSRP)
> | Definition | SS reference signal received power (SS-RSRP) is defined as the linear average over the power contributions (in [W]) of the resource elements that carry secondary synchronization signals. The measurement time resource(s) for SS-RSRP are confined within SS/PBCH Block Measurement Time Configuration (SMTC) window duration, except when measurement is being performed by wake-up receiver (WUR). If SS-RSRP is used for L1-RSRP as configured by reporting configurations as defined in TS 38.214 [6], the measurement time resources(s) restriction by SMTC window duration is not applicable. For SS-RSRP determination demodulation reference signals for physical broadcast channel (PBCH) and, if indicated by higher layers, CSI reference signals in addition to secondary synchronization signals may be used. SS-RSRP using demodulation reference signal for PBCH or CSI reference signal shall be measured by linear averaging over the power contributions of the resource elements that carry corresponding reference signals taking into account power scaling for the reference signals as defined in TS 38.213 [5]. If SS-RSRP is not used for L1-RSRP, the additional use of CSI reference signals for SS-RSRP determination is not applicable. SS-RSRP shall be measured only among the reference signals corresponding to SS/PBCH blocks with the same SS/PBCH block index and the same physical-layer cell identity. If SS-RSRP is not used for L1-RSRP and higher-layers indicate certain SS/PBCH blocks for performing SS-RSRP measurements, then SS-RSRP is measured only from the indicated set of SS/PBCH block(s). For frequency range 1, the reference point for the SS-RSRP shall be the antenna connector of the UE. For frequency range 2, SS-RSRP shall be measured based on the combined signal from antenna elements corresponding to a given receiver branch. For frequency range 1 and 2, if receiver diversity is in use by the UE, the reported SS-RSRP value shall not be lower than the corresponding SS-RSRP of any of the individual receiver branches. |
> | Applicable for | If SS-RSRP is used for L1-RSRP, RRC_CONNECTED intra-frequency, If SS-RSRP is being performed by wake-up receiver (WUR), RRC_IDLE for serving cell, RRC_INACTIVE for serving cell. Otherwise, RRC_IDLE intra-frequency, RRC_IDLE inter-frequency, RRC_INACTIVE intra-frequency, RRC_INACTIVE inter-frequency, RRC_CONNECTED intra-frequency, RRC_CONNECTED inter-frequency |
> 5.1.2	CSI reference signal received power (CSI-RSRP)
> | Definition | CSI reference signal received power (CSI-RSRP), is defined as the linear average over the power contributions (in [W]) of the resource elements of the antenna port(s) that carry CSI reference signals configured for RSRP measurements within the considered measurement frequency bandwidth in the configured CSI-RS occasions. For CSI-RSRP determination CSI reference signals transmitted on antenna port 3000 according to TS 38.211 [3] shall be used. If CSI-RSRP is used for L1-RSRP, CSI reference signals transmitted on antenna ports 3000, 3001 can be used for CSI-RSRP determination. For intra-frequency CSI-RSRP measurements, if the measurement gap is not configured, UE is not expected to measure the CSI-RS resource(s) outside of the active downlink bandwidth part. For frequency range 1, the reference point for the CSI-RSRP shall be the antenna connector of the UE. For frequency range 2, CSI-RSRP shall be measured based on the combined signal from antenna elements corresponding to a given receiver branch. For frequency range 1 and 2, if receiver diversity is in use by the UE, the reported CSI-RSRP value shall not be lower than the corresponding CSI-RSRP of any of the individual receiver branches. |
> | Applicable for | If CSI-RSRP is used for L1-RSRP, RRC_CONNECTED intra-frequency, Otherwise, RRC_CONNECTED intra-frequency, RRC_CONNECTED inter-frequency |
> Final CR in R1-2605091 is endorsed.
> 7-24 GHz

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2605008](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2605008.zip)

**Agreement** · `10.8.2` Aspects of integration with communication · `RAN1#125:10.8.2:005` · 후보

> - Study the necessity, scenario and related physical layer specification impacts of beam related aspects for RS used for sensing, taking communication beam management as starting point.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2603996](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2603996.zip) · `[125-R20-6GR-ISAC-Integration]`

### RAN1#124bis — 8건

**Conclusion** · `7` Pre-Rel-19 NR Maintenance · `RAN1#124bis:7:004` · 후보

> If unified TCI is configured, PUSCH can be scheduled with DCI format 0_0.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2603383](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603383.zip)

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#124bis:8.1:002` · 후보

> The following TP for TS 38.214 Clause 5.2.1.6 is endorsed.
> The corresponding final CR for Rel-19 TS 38.214 in R1-2603379 is endorsed
> Reason for change: CPU duration for beam management related UE-side data collection is not captured correctly. In current specification, periodic CSI report for UE-side data collection for beam management is not supported.
> | Agreement For UE-sided model, regarding the resource type for data collection purpose, only always-on SSB and P/SP CSI-RS are supported. Agreement For UE-sided model, regarding a CSI-ReportConfig for data collection, Reuse the existing CPU occupation time for a CSI report with CSI-ReportConfig with reportQuantity set to 'none' and TRS-info not configured |
> Summary of change: Reflect the RAN1 agreements accurately in Section 5.2.1.6 of TS 38.214. Include periodic CSI report for UE-side data collection for beam management.
> Consequence if not approved: Incorrect UE behaviour for CPU duration for UE-side data collection for training.
> | 5.2.1.6 CSI processing criteria < Unchanged parts are omitted > For a CSI report with CSI-ReportConfig with higher layer parameter reportQuantity set to 'none' and CSI-RS-ResourceSet with higher layer parameter trs-Info not configured, or reportQuantity set to 'none-bm-r19', the CPU(s) are occupied for a number of OFDM symbols as follows: - A semi-persistent CSI report (excluding an initial semi-persistent CSI report on PUSCH after the PDCCH triggering the report) occupies CPU(s) from the first symbol of the earliest one of each transmission occasion of periodic or semi-persistent CSI-RS/SSB resource for channel measurement for L1-RSRP computation, until symbols after the last symbol of the latest one of the CSI-RS/SSB resource for channel measurement for L1-RSRP computation in each transmission occasion. - An aperiodic CSI report occupies CPU(s) from the first symbol after the PDCCH triggering the CSI report until the last symbol between symbols after the first symbol after the PDCCH triggering the CSI report and symbols after the last symbol of the latest one of each CSI-RS/SSB resource for channel measurement for L1-RSRP computation. For a CSI report with CSI-ReportConfig with higher layer parameter reportQuantity set to 'none-csi-r19', the CPU(s) are occupied for a number of OFDM symbols as follows: - CSI report occupies CPU(s) from the first symbol of each transmission occasion of periodic or semi-persistent CSI-RS resource for channel measurement, until symbols after the transmission occasion of periodic or semi-persistent CSI-RS resource for channel measurement. where are defined in the table 5.4-2. For a CSI report with CSI-ReportConfig with higher layer parameter reportQuantity set to 'none-bm-r19', the CPU(s) are occupied for a number of OFDM symbols as follows: - CSI report occupies CPU(s) from the first symbol of the earliest one of each transmission occasion of periodic or semi-persistent CSI-RS/SSB resource for channel measurement for L1-RSRP computation, until symbols after the last symbol of the latest one of the CSI-RS/SSB resource for channel measurement for L1-RSRP computation in each transmission occasion. where are defined in the table 5.4-2. < Unchanged parts are omitted > |

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2603260](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603260.zip) · `[124b-R19-AI/ML]`

**Agreement** · `8.5` Maintenance on Low-power wake-up signal and receiver for NR (LP-WUS/WUR) · `RAN1#124bis:8.5:004` · 후보

> Adopt the following TP to section 10.4D, TS 38.213 as alignment CR:
> | ======================== Start of TP======================================= 10.4D PDCCH monitoring activation by WUS in RRC_CONNECTED A UE configured with DRX mode operation and operating in the RRC_CONNECTED state can be provided for WUS reception on the primary cell of a cell group - a number of OOK symbols per OFDM symbol, a first RB by lpwus-StartRB, and overlaid OFDM sequences per OOK symbol for WUS reception [4, TS 38.211], and - a number of codepoints provided for the UE by the WUS [6, TS 38.212], by lpwus-CodepointWUS-codepointCONNECTED A UE assumes that a WUS is quasi co-located with an SS/PBCH block or a CSI-RS with respect to quasi co-location ‘typeC’ or ‘typeD’ properties, when applicable. If a UE is provided dl-OrJointTCI-StateList, the UE receives WUS based on the quasi co-location information of the TCI states provided by dl-OrJointTCI-StateList, indicated by a most recent DCI format or MAC CE, after a respective application time in clause 5.1.5 [6, TS 38.214]; otherwise, the UE receives WUS based on the quasi co-location information of the TCI states for a CORESET with controlResourceSetId value that is same as the one indicated by lpwus-TCI-StatesWUS_TCI_states_CONNECTED. A UE assumes that an SCS configuration for WUS receptions is same as an SCS configuration for the active DL BWP. A UE does not monitor a WUS during Active Time [11, TS 38.321]. A UE does not monitor WUS during DTX inactive period for the primary cell. When lpwus-PDCCH-MonitoringTimer is not provided, A a UE can be provided by lpwus-MO-1-1WUS-MOCONNECTED-Option1-1 a periodicity, by periodicityMO-Option 1-1, and a time offset, by offsetMO-Option 1-1, relative to the start of a system frame with SFN 0, for the UE to determine WUS monitoring occasions. The UE starts to monitor WUS in a first WUS monitoring occasion that is not earlier than a first slot that is prior to a second slot where the drx-onDurationTimer would start by a time provided by lpwus-TimeOffset1-1timeOffsetCONNECTEDOption1-1, and monitors WUS for a number of monitoring occasions provided by lpwus-NumOfMO-1-1numMO-Option 1-1. The UE reports a number of milliseconds [18, TS 38.306] where the UE is not required to monitor WUS prior to the slot where the drx-onDurationTimer would start. The UE is not required to monitor WUS within the reported number of slots prior to the slot where the drx-onDurationTimer would start. If the UE determines to monitor PDCCH based on a detected WUS, the UE starts the drx-onDurationTimer [11, TS 38.321]. When lpwus-PDCCH-MonitoringTimer is provided, aA UE can be provided by lpwus-MO-1-2WUS-MOCONNECTED-Option1-2 a periodicity, by periodicityMO-Option 1-2, and a time offset, by offsetMO-Option 1-2, relative to the start of a system frame with SFN 0, for the UE to determine first WUS monitoring occasions from a number of WUS monitoring occasions per periodicity, provided by lpwus-NumOfMO-1-2numMO-perPeriodicity-Option 1-2. The UE assumes WUS monitoring occasions per periodicity are consecutive in time. The UE reports a number of milliseconds [18, TS 38.306] and expects that a time gap, from a last WUS monitoring occasion from the number of WUS monitoring occasions per periodicity to the slot where the lpwus-PDCCH-MonitoringTimer would start, is no smaller than the reported number of milliseconds If the UE determines to monitor PDCCH based on a detected WUS, the UE starts lpwus-PDCCH-MonitoringTimer [11, TS 38.321] after a time, provided by lpwus-TimeOffset1-2timeOffsetCONNECTEDOption1-2, with respect to the start of the first WUS monitoring occasion from the number of WUS monitoring occasions per periodicity. A UE can be provided, by lpwus-AvailableSlot in LPWUS-ConfigWUS_available_slot_CONNECTED, a bitmap that corresponds to a set of time units that repeats continuously and indicates a subset of time units from the set of time units that is available for the UE to monitor WUS [12, TS 38.331]. A time unit includes one slot or two slots. A set of time units includes a total of either 10, or 20, or 40 time units. A duration , in msec, of the set of time units has maximum value of 40 msec. The first symbol of the set of time units every 40 msec/ periods is a first symbol in frame mod 4 = 0. The UE can be additionally provided, by lpwus-AvailableSymbol in LPWUS-ConfigWUS_available_symbol_CONNECTED, an indication of symbols in each time unit from the subset of time units that is available for the UE to monitor WUS. If the UE is not provided lpwus-AvailableSlotWUS_available_slot_CONNECTED, the UE assumes that all time units are available for the UE to monitor WUS. If the UE is not provided lpwus-AvailableSymbolWUS_available_symbol_CONNECTED, the UE assumes a time unit of one slot and, for a time unit that is available for the UE to monitor WUS, all symbols in the time unit are available for the UE to monitor WUS. The UE assumes that a symbol is not available to monitor WUS when - the symbol is indicated as uplink, by tdd-UL-DL-configurationCommon or tdd-UL-DL-ConfigurationDedicated - the symbol is indicated for transmission of SS/PBCH blocks, by ssb-PositionsInBurst in SIB1 or in ServingCellConfigCommon A WUS monitoring occasion is over a first number of symbols, provided by lpwus-NominalMoDuration in LPWUS-ConfigWUS_NominalMO_duration_CONNECTED. If a number of available symbols for the UE to monitor WUS in a WUS monitoring occasion is smaller than a second number of symbols, provided by lpwus-ActualDuration in LPWUS-ConfigWUS_ActualMO_duration_CONNECTED, the UE does not monitor WUS in the WUS monitoring occasion. The UE monitors WUS in a WUS monitoring occasion over the earliest available lpwus-ActualDurationWUS_ActualMO_duration_CONNECTED symbols in the WUS monitoring occasion. If a UE detects a codepoint in a WUS reception, from the number of codepoints, on the primary cell of the cell group, the UE starts monitoring PDCCH on all applicable serving cells of the cell group, and the UE does not need to monitor WUS before lpwus-PDCCH-MonitoringTimer starts, if lpwus-PDCCH-MonitoringTimer is provided. ========================= End of TP======================================= |
> R1-263402	Summary #2 of maintenance on Low-power wake-up signal and receiver for NR (LP-WUS/WUR)			Moderator (vivo)

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2602036](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2602036.zip) · `[124b-R19-LP-WUS]`

**Agreement** · `8.7` Maintenance on others · `RAN1#124bis:8.7:002` · 후보

> - Adopt the following TP to TS38.214 Section 5.2.1.5.4.2
> | Reason for change: determination of serving cell RS for event triggered LTM is not accurately described in the TS 38.214. Summary of change: Clarify the condition of a UE to determine the reference signal in the indicated TCI state as the serving cell RS. Consequences if not approved: UE’s behaviors of serving cell RS determination for event triggered LTM is unclear. |
> The final CR in R1-2603407 is endorsed.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2603335](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603335.zip) · `[124b-R19-others]`

**Agreement** · `8.7` Maintenance on others · `RAN1#124bis:8.7:003` · 후보

> - Adopt the following TP to TS38.213 Section 21.1
> | Reason for change: | In RACH-less conditional LTM, CG-PUSCH will be used for UE to transmit first UL to target cell. However, in clause 21.1 of TS38.213, the procedure of CG-PUSCH for LTM does not consider the RACH-less conditional LTM case, where there is no LTM cell switch MAC CE indicate LTM TCI state to be used in the target cell. |
> |  |  |
> | Summary of change: | To determine the CG-PUSCH occasion, the RS resource selected in RACH-less conditional LTM defined in TS38.321 should be used. To acquire the power control parameters for CG-PUSCH, the LTM TCI state determined RACH less conditional LTM as defined in clause 21 should be used. |
> |  |  |
> | Consequences if not approved: | How to select the PUSCH occasion and power control parameter for CG-PUSCH transmission in RACH-less conditional LTM is not specified. |
> | 21.1 Configured-grant PUSCH transmission in RACH-less LTM cell switch ==================================unchanged omitted======================= If the UE is provided cg-LTM-Configuration, the UE performs configured grant Type 1 PUSCH transmission on the valid PUSCH occasions associated with the SS/PBCH block indexes same as the SS/PBCH block indexes provided by or associated with QCL RS of the CandidateTCI-State or CandidateTCI-UL-State indicated by the LTM Cell Switch Command MAC CE. A UE determines a power of a PUSCH transmission as described in clause 7.1.1, where the UE obtains using a RS resource from pathlossReferenceRS-Id included in the CandidateTCI-State or CandidateTCI-UL-State indicated by the LTM Cell Switch Command MAC CE . |
> The final CR in R1-2603408 is endorsed.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2603335](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603335.zip) · `[124b-R19-others]`

**Agreement** · `8.7` Maintenance on others · `RAN1#124bis:8.7:004` · 후보

> - Adopt the following TP to TS38.213 Section 21 in principle
> | 21 L1/L2-triggered mobility procedures <Unchanged parts are omitted> After RACH-based conditional LTM cell switch is triggered, all activated TCI states are deactivated. For RACH-less conditional LTM cell switch, the UE determines a TCI state in CandidateTCI-State or CandidateTCI-UL-State to apply for receptions or transmissions on the candidate cell before a new TCI state is applied for the candidate cell, where the QCL RS of the TCI state is same as the RS resource selected in the RACH-less conditional LTM cell switch or is QCLed with the SS/PBCH block selected in the RACH-less conditional LTM cell switch as described in clause 5.36.3 [11, TS 38.321]. If there are two RS indexes in the TCI state, the QCL RS with RS index configured with qcl-Type set to 'typeD' is used for determination. After RACH-less conditional LTM cell switch is triggered, all activated TCI states, other than the TCI state, are deactivated. |

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2603335](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603335.zip) · `[124b-R19-others]`

**Agreement** · `10.5.0` General aspects and frameworks · `RAN1#124bis:10.5.0:002` · 후보

> RAN1 to discuss beamforming gain for DL broadcast channel and UL channel and to align the interpretation of the following parameters in link budget template candidate 1
> - (4b) Antenna gain correction factor at antenna gain component 3 & antenna gain component 4 of transmitter (dB)
> - (5b) Antenna gain correction factor at antenna gain component 2 of transmitter (dB)
> - (11b) Antenna gain correction factor at antenna gain component 3 & antenna gain component 4 of receiver (dB)
> - (11bis-b) Antenna gain correction factor at antenna gain component 2 of receiver (dB)
> - (15) Receiver interference density
> - (27) Penetration margin (dB): Whether account for the indoor distance in the pathloss calculation in O2I scenarios
> - (25) Shadow fading margin (function of the cell area reliability and lognormal shadow fading std deviation) (dB): Function definition and whether handoff gain is accounted

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-General, Synchronization and Beam Measurement]`

**Agreement** · `10.5.2.2` Downlink transmission scheme(s) for downlink shared channels · `RAN1#124bis:10.5.2.2:004` · 후보

> - Study the DMRS assumption for MU-MIMO considering at least the following aspects
>   - Network indication or UE assumption of DMRS CDM group/ports/density/pattern/symbol(s) for co-scheduled UE(s)
>   - Network indication of number of CDM groups without data as in NR
>   - Network indication to assist the UE’s OCC despreading
>   - Network indication or UE assumption of the DMRS sequence for the co-scheduled UE(s)
>   - Network indication or UE assumption of the modulation order(s) for the co-scheduled UE(s)
>   - Network indication or UE assumption of the QCL/TCI information for the co-scheduled UE(s)
>   - Network indication or UE assumption of PRG allocation for the co-scheduled UE(s)

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Transmission scheme for DL shared channel]`

### RAN1#124 — 5건

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#124:8.1:001` · 후보

> The following TP for TS 38.214 Clause 5.2.1.4.2 for Rel-19 is endorsed.
> The corresponding final CR for Rel-19, TS 38.214 in R1-2601645 is endorsed.
> Reason for change: There is a bracket related to Set A description. Report quantity name and RRC parameters name are not aligned with the latest TS38.331.
> Summary of change: Remove the bracket related to Set A description and align the report quantity name and RRC parameters name.
> Consequences if not approved: The description related to Set A is unclear.
> | 5.2.1.4.2 Report quantity configurations <omitted texts> If the UE is configured with a CSI-ReportConfig with reportQuantity-r19 set to 'p-cri-r19p-CRI-r19', 'p-cri-RSRP-r19p-CRI-RSRP-r19', 'p-ssb-index-r19p-SSB-Index-r19' or 'p-ssb-index-RSRP-r19p-SSB-Index-RSRP-r19', and with nrofreportedpredictedrs-r19nrofReportedPredictedRS-r19 and/or nroftimeinstance-r19nrofTimeInstance-r19, the following applies: the UE is not required to update measurements for more than 64 CSI-RS or SSB resources given by resourcesForChannelMeasurement,[ and is not expected to predict for more than 64 CSI-RS or SSB resources given by resourcesForSetA-r19]resourcesForChannelPrediction-r19, the UE shall report one of the following in a single report: - nrofreportedpredictedrs-r19nrofReportedPredictedRS-r19 different P-CRIs or P-SSBRIs of the second Resource Setting, if nroftimeinstance-r19nrofTimeInstance-r19 is not configured and reportQuantity-r19 is set to ' p-cri-r19p-CRI-r19' or ' p-ssb-index-r19p-SSB-Index-r19', - nrofreportedpredictedrs-r19nrofReportedPredictedRS-r19 different P-CRIs or P-SSBRIs of the second Resource Setting, with corresponding predicted L1-RSRP(s), if nroftimeinstance-r19nrofTimeInstance-r19 is not configured and reportQuantity-r19 set to ' p-cri-RSRP-r19p-CRI-RSRP-r19' or ' p-ssb-index-RSRP-r19p-SSB-Index-RSRP-r19', - nrofreportedpredictedrs-r19nrofReportedPredictedRS-r19 different P-CRIs or P-SSBRIs of the second Resource Setting for each of nroftimeinstance-r19nrofTimeInstance-r19 time instance(s), if nroftimeinstance-r19nrofTimeInstance-r19 is configured and reportQuantity-r19 set to 'p-cri-r19' or ' p-ssb-index-RSRP-r19p-SSB-Index-RSRP-r19', - nrofreportedpredictedrs-r19nrofReportedPredictedRS-r19 different P-CRIs or P-SSBRIs of the second Resource Setting for each of nroftimeinstance-r19nrofTimeInstance-r19 time instance(s), with corresponding predicted L1-RSRP(s), if nroftimeinstance-r19nrofTimeInstance-r19 is configured and reportQuantity-r19 set to ' p-cri-RSRP-r19p-CRI-RSRP-r19' or ' p-ssb-index-RSRP-r19p-SSB-Index-RSRP-r19'. <omitted texts> |

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2600736](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2600736.zip) · `[124-R19-AI/ML]`

**Agreement** · `8.6` Maintenance on Low-power wake-up signal and receiver for NR (LP-WUS/WUR) · `RAN1#124:8.6:006` · 후보

> Adopt the following TP to Clause 5.1.5, TS 38.214.
> | Reason for change: The UE assumption on QCL information before applying an indicated TCI state is not yet described in specification. Summary of Change: Clarify the assumption for QCL information during WUS monitoring before applying the indicated TCI state by updating the existing clause 5.1.5 to add WUS in addition to CSI-RS and DMRS of PDSCH/PDCCH. Consequences if not approved: Unclear UE behaviour for WUS monitoring prior to applying an indicated TCI state. |
> | ---------------------------------Start of Text Proposal on 3GPP TS 38.214 V19.2.0----------------------- <Unchanged part is omitted> After a UE receives an initial higher layer configuration of dl-OrJointTCI-StateList where more than one TCI-State can be used as an indicated TCI state and before application of an indicated TCI state from the configured TCI states: - The UE assumes that DM-RS of PDSCH and DM-RS of PDCCH that are not received during the RACH procedure, WUS, and the CSI-RS applying the indicated TCI state are quasi co-located with the reference signal(s) in the CandidateTCI-State indicated in the LTM Cell Switch Command MAC CE [10, 38.321] if applicable, otherwise. - The UE assumes that DM-RS of PDSCH and DM-RS of PDCCH, WUS, and the CSI-RS applying the indicated TCI state are quasi co-located with the SS/PBCH block the UE identified during the initial access procedure <Unchanged part is omitted> After a UE receives a higher layer configuration of dl-OrJointTCI-StateList where more than one TCI-State can be used as an indicated TCI state as part of a Reconfiguration with sync procedure as described in [12, TS 38.331] and before applying an indicated TCI state from the configured TCI states: - The UE assumes that DM-RS of PDSCH and DM-RS of PDCCH, WUS, and the CSI-RS applying the indicated TCI state are quasi co-located with the SS/PBCH block or the CSI-RS resource the UE identified during the random access procedure initiated by the Reconfiguration with sync procedure as described in [12, TS 38.331]. <Unchanged part is omitted> ---------------------------------End of Text Proposal on 3GPP TS 38.214 V19.2.0----------------------- |
> Final CR is endorsed in R1-2601591

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601581](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601581.zip) · `[124-R19-LP-WUS]`

**Agreement** · `8.8` Maintenance on others · `RAN1#124:8.8:004` · 후보

> Adopt the following TP to TS38.213 Section 21
> | Reason for change: | For RACH-less CLTM, UE determines a TCI state for communication in target cell, based on QCL RS of the TCI state and the RS triggering CLTM, as below: If QCL RS of the TCI state is the same as triggering CLTM, or If QCL RS of the TCI state is QCLed with the SSB triggering CLTM. However, a TCI state may have two QCL RSs, where one is for TypeA and the other is for TypeD. Under this situation, it is unclear which QCL RS is used for determining the TCI state for communication in target cell. |
> |  |  |
> | Summary of change: | Describe that QCL RS for TypeD is used for determining a TCI state for CLTM, if there are two QCL RSs in the TCI state. This change follows the same design principle elsewhere in the specification, and the proposed texts follow the same style of the texts in TS 38.213 for link recovery (BFR). |
> |  |  |
> | Consequences if not approved: | Ambiguous and incomplete UE behavior on determining TCI state for CLTM. |
> | 21 L1/L2-triggered Mobility procedures < Unchanged parts are omitted > After RACH-based conditional LTM cell switch is triggered, all activated TCI states are deactivated. For RACH-less conditional LTM cell switch, the UE determines a TCI state in CandidateTCI-State or CandidateTCI-UL-State to apply for receptions or transmissions on the candidate cell before a new TCI state is applied for the candidate cell, where the QCL RS of the TCI state is same as the RS resource selected in the RACH-less conditional LTM cell switch or is QCLed with the SS/PBCH block selected in the RACH-less conditional LTM cell switch as described in clause 5.36.3 [11, TS 38.321]. After RACH-less conditional LTM cell switch is triggered, all activated TCI states, other than the TCI state, are deactivated. < Unchanged parts are omitted > |
> Final CR is endorsed in R1-2601632

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601559](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601559.zip) · `[124-R19-others]`

**Agreement** · `8.8` Maintenance on others · `RAN1#124:8.8:005` · 후보

> Endorse the following TP to TS38.214 Section 5 as alignment CR
> | Reason for change | Two ASN.1 parameter names have changed from Release 18 to Release 19. These are not reflected in the procedural text. |
> | Summary of change | Change these parameter names according to the Release 19 ASN.1 naming |
> | Consequences if not approved | Mismatch between the ASN.1 parameter names and their usage in this specification |
> | TS38.214 Chapter 5.2.1.2 Resource settings <omitted texts> Each LTM CSI Resource Setting LTM-CSI-ResourceConfig contains either configuration of a ltm-CSI-SSB-ResourceSet ltm-SSB-ResourceSet or a ltm-NZP-CSI-RS-ResourceSet. - A ltm-CSI-SSB-ResourceSet ltm-SSB-ResourceSet comprises of a list of Z ≥ 1 SS/PBCH blocks indices (given by ltm-CSI-SSB-ResourceList ltm-SSB-ResourceList) and a list of Z LTM-CandidateIds (given by ltm-CandidateIdList) referring to candidate cells associated with the SS/PBCH block indices. For each candidate cell, the UE determines the time domain behavior of a SS/PBCH block from ssb-Periodicity and ssb-PositionsInBurst and the frequency domain behavior of a SS/PBCH block is determined by the higher layer parameters subcarrierSpacing, ssb-Frequency. - A ltm-NZP-CSI-RS-ResourceSet comprises of a list of Z ≥ 1 NZP CSI-RS resource indices (given by ltm-CSI-RS-ResourceList) and a list of Z LTM-CandidateIds (given by ltm-CandidateIdList) referring to candidate cells associated with the NZP CSI-RS resource indices. The UE shall expect that ltm-NZP-CSI-RS-ResourceSet are configured with the higher layer parameter repetition set to ‘off’ when LTM-ReportContent configured within the LTM-CSI-ReportConfig associated with the LTM CSI Resource Setting is set to ‘cri-RSRP’. For a report setting ltm-CSI-ReportConfig configured with ltm-ReportConfigType set to ‘periodic’ or ‘semiPersistentOnPUCCH’ or ‘semiPersistentOnPUSCH’ or ‘aperiodic’, the time domain behavior of the NZP CSI-RS resources within a ltm-NZP-CSI-RS-ResourceSet are indicated by the higher layer parameter resourceType. <omitted texts> Chapter 5.2.1.4.2 Report quantity configuration <omitted texts> If a UE is configured with a ltm-CSI-ReportConfig with ltm-ReportConfigType which is set to ‘periodic’ or ‘semiPersistentOnPUCCH’ or ‘semiPersistentOnPUSCH’ or ‘aperiodic’, - if the UE is configured with spCellInclusion with reportQuantity set to 'ssb-Index-RSRP', the UE shall report in a single reporting instance nrOfReportedRS-PerCell different SSBRI for the current SpCell and each of the nrOfReportedCells -1 candidate cells. Otherwise, the UE shall report in a single reporting instance nrOfReportedRS-PerCell different SSBRI for each of the nrOfReportedCells candidate cells, - where SSBRI k (k ≥ 0) corresponds to the configured (k+1)-th entry of the associated ltm-CSI-SSB-ResourceList ltm-SSB-ResourceList in the corresponding ltm-CSI-SSB-ResourceSet ltm-SSB-ResourceSet, - if spCellInclusion is configured, SSB resources in ltm-CSI-SSB-ResourceList ltm-SSB-ResourceList associated with the current SpCell are the entries where PCI (given by ltm-CandidatePCI) and frequency information (given by ssb-Frequency) of the candidate cell associated with the LTM-CandidateId (given by the corresponding entry in ltm-CandidateIdList) is equal to the PCI and center frequency of cell-defining SSB of the current SpCell. <omitted texts> Chapter 5.2.1.5.4.2 UE Initiated LTM reporting For a report setting ltm-CSI-ReportConfig configured with ltm-ReportConfigType set to 'eventTriggered', the UE may expect that the time domain behavior of the NZP CSI-RS resources within a ltm-NZP-CSI-RS-ResourceSet is periodic when the LTM-CSI-ResourceConfig contains a configuration of a ltm-NZP-CSI-RS-ResourceSet. When the UE is configured with dl-OrJointTCI-StateList or ul-TCI-StateList, for the L1-RSRP of the serving cell RS - if the LTM-CSI-ResourceConfig contains a configuration of a ltm-NZP-CSI-RS-ResourceSet, the UE measures the L1-RSRP of the reference signal in the indicated TCI state provided in a NZP-CSI-RS-ResourceSet configured with repetition. - if the LTM-CSI-ResourceConfig contains a configuration of a ltm-CSI-SSB-ResourceSet ltm-SSB-ResourceSet, the UE measures the L1-RSRP of the SS/PBCH block which is QCLed with the reference signal in the indicated TCI state. where the reference signal in the indicated TCI state is the reference signal w.r.t. QCL-TypeD, if there are two QCL RSs in the indicated TCI state. | TS38.214 Chapter 5.2.1.2 Resource settings <omitted texts> Each LTM CSI Resource Setting LTM-CSI-ResourceConfig contains either configuration of a ltm-CSI-SSB-ResourceSet ltm-SSB-ResourceSet or a ltm-NZP-CSI-RS-ResourceSet. - A ltm-CSI-SSB-ResourceSet ltm-SSB-ResourceSet comprises of a list of Z ≥ 1 SS/PBCH blocks indices (given by ltm-CSI-SSB-ResourceList ltm-SSB-ResourceList) and a list of Z LTM-CandidateIds (given by ltm-CandidateIdList) referring to candidate cells associated with the SS/PBCH block indices. For each candidate cell, the UE determines the time domain behavior of a SS/PBCH block from ssb-Periodicity and ssb-PositionsInBurst and the frequency domain behavior of a SS/PBCH block is determined by the higher layer parameters subcarrierSpacing, ssb-Frequency. - A ltm-NZP-CSI-RS-ResourceSet comprises of a list of Z ≥ 1 NZP CSI-RS resource indices (given by ltm-CSI-RS-ResourceList) and a list of Z LTM-CandidateIds (given by ltm-CandidateIdList) referring to candidate cells associated with the NZP CSI-RS resource indices. The UE shall expect that ltm-NZP-CSI-RS-ResourceSet are configured with the higher layer parameter repetition set to ‘off’ when LTM-ReportContent configured within the LTM-CSI-ReportConfig associated with the LTM CSI Resource Setting is set to ‘cri-RSRP’. For a report setting ltm-CSI-ReportConfig configured with ltm-ReportConfigType set to ‘periodic’ or ‘semiPersistentOnPUCCH’ or ‘semiPersistentOnPUSCH’ or ‘aperiodic’, the time domain behavior of the NZP CSI-RS resources within a ltm-NZP-CSI-RS-ResourceSet are indicated by the higher layer parameter resourceType. <omitted texts> Chapter 5.2.1.4.2 Report quantity configuration <omitted texts> If a UE is configured with a ltm-CSI-ReportConfig with ltm-ReportConfigType which is set to ‘periodic’ or ‘semiPersistentOnPUCCH’ or ‘semiPersistentOnPUSCH’ or ‘aperiodic’, - if the UE is configured with spCellInclusion with reportQuantity set to 'ssb-Index-RSRP', the UE shall report in a single reporting instance nrOfReportedRS-PerCell different SSBRI for the current SpCell and each of the nrOfReportedCells -1 candidate cells. Otherwise, the UE shall report in a single reporting instance nrOfReportedRS-PerCell different SSBRI for each of the nrOfReportedCells candidate cells, - where SSBRI k (k ≥ 0) corresponds to the configured (k+1)-th entry of the associated ltm-CSI-SSB-ResourceList ltm-SSB-ResourceList in the corresponding ltm-CSI-SSB-ResourceSet ltm-SSB-ResourceSet, - if spCellInclusion is configured, SSB resources in ltm-CSI-SSB-ResourceList ltm-SSB-ResourceList associated with the current SpCell are the entries where PCI (given by ltm-CandidatePCI) and frequency information (given by ssb-Frequency) of the candidate cell associated with the LTM-CandidateId (given by the corresponding entry in ltm-CandidateIdList) is equal to the PCI and center frequency of cell-defining SSB of the current SpCell. <omitted texts> Chapter 5.2.1.5.4.2 UE Initiated LTM reporting For a report setting ltm-CSI-ReportConfig configured with ltm-ReportConfigType set to 'eventTriggered', the UE may expect that the time domain behavior of the NZP CSI-RS resources within a ltm-NZP-CSI-RS-ResourceSet is periodic when the LTM-CSI-ResourceConfig contains a configuration of a ltm-NZP-CSI-RS-ResourceSet. When the UE is configured with dl-OrJointTCI-StateList or ul-TCI-StateList, for the L1-RSRP of the serving cell RS - if the LTM-CSI-ResourceConfig contains a configuration of a ltm-NZP-CSI-RS-ResourceSet, the UE measures the L1-RSRP of the reference signal in the indicated TCI state provided in a NZP-CSI-RS-ResourceSet configured with repetition. - if the LTM-CSI-ResourceConfig contains a configuration of a ltm-CSI-SSB-ResourceSet ltm-SSB-ResourceSet, the UE measures the L1-RSRP of the SS/PBCH block which is QCLed with the reference signal in the indicated TCI state. where the reference signal in the indicated TCI state is the reference signal w.r.t. QCL-TypeD, if there are two QCL RSs in the indicated TCI state. |

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601559](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601559.zip) · `[124-R19-others]`

**Agreement** · `8.9` Maintenance on UE features · `RAN1#124:8.9:006` · 후보

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-3-1 | CJTC Dd report | 1. Configured minimum quantization range for CJTC Dd reporting 2. Configured maximum resolution (number of steps) for the quantization alphabet for CJTC Dd reporting 3. Supported value of scaling factor X for OCPU calculation | 2-35 | yes | n/a | CJTC Dd report is not supported | Per band and per BC | n/a | n/a | n/a FR1 only | Component 1 candidate values: {half cyclic prefix, full cyclic prefix} Component 2 candidate values: {32, 64, 128, 256} Note: For component 1 and 2, the larger granularity considering component 1 and 2 reported value is the lower capability Component 3 candidate values: {1, 2} Note: For component 3, the larger value is the lower capability Note：OCPU =X.NTRP | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-3-1a | CJTC Dd report processing | 1. Maximum number of configured TRS resource sets for delay offset report 2. Maximum number of configured TRS resource sets for delay offset report across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC 3. Maximum number of simultaneously active CSI-RS resources for delay offset report per CC 4. Maximum number of simultaneously active CSI-RS resources for delay offset report across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC 5. Value of X for CPU occupation (OCPU=XNTRP) | 59-2-3-1 | yes | n/a |  | Per band and Per BC | n/a | n/a | n/a FR1 only | Component 1 candidate values: {2, 4, 6, 8, 10, 12} Component 2 candidate values: {2, 4, 6, 8, 12, … 64} Component 3 candidate values: {2, 4, 6, 8, 12, 16, 20, 24, 28, 32} Component 4 candidate values: {2, 4, 6, 8, 12, 16, 20, 24, 28, 32, …, 64} Component 5 candidate values: {1, 2} | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-3-2 | CJTC FO report | 1. Configured minimum quantization range for CJTC FO reporting 2. Configured maximum resolution (number of steps) for the quantization alphabet for CJTC FO reporting 3. Supported value of scaling factor X for OCPU calculation | 2-35 | yes | n/a | CJTC FO report is not supported | Per band and per BC | n/a | n/a | n/a FR1 only | Component 1 candidate values: {0.1ppm, 0.2ppm} Component 2 candidate values: {16, 32, 256} Note: For component 1 and 2, the larger granularity considering component 1 and 2 reported value is the lower capability Component 3 candidate values: {1, 2} Note: For component 3, the larger value is the lower capability Note：OCPU =X.NTRP Note: parts per million (ppm) of the carrier frequency | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-3-2a | CJTC FO report processing | 1. Maximum number of configured TRS resource sets for frequency offset report 2. Maximum number of configured TRS resource sets for frequency offset report across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC 3. Maximum number of simultaneously active CSI-RS resources for frequency offset report per CC 4. Maximum number of simultaneously active CSI-RS resources for frequency offset report across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC 5. Value of X for CPU occupation (OCPU=XNTRP) | 59-2-3-2 | yes | n/a | CJTC FO report is not supported | Per band and Per BC | n/a | n/a | n/a FR1 only | Component 1 candidate values: {2, 4, 6, 8, 10, 12} Component 2 candidate values: {2, 4, 6, 8, 12, … 64} Component 3 candidate values: {2, 4, 6, 8, 12, 16, 20, 24, 28, 32} Component 4 candidate values: {2, 4, 6, 8, 12, 16, 20, 24, 28, 32, …, 64} Component 5 candidate values: {1, 2} | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-3-3 | CJTC wideband PO report | 1. Configured maximum resolution (number of steps) for the quantization alphabet for CJTC WB PO reporting 2. Supported value of scaling factor X for OCPU calculation 3. Supported maximum slot duration for NTRP P/SP CSI-RS occasions being confined in | 2-35 | yes | n/a | CJTC PO report is not supported | Per band and per BC | n/a | n/a | n/a FR1 only | Component 1 candidate values: {16, 32} Component 2 candidate values: {1, 2} Component 3 candidate values: {1, 2} Note：OCPU =X.NTRP | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-3-3a | CJTC wideband PO report processing | 1. Maximum number of configured CSI-RS resources for phase offset report 2. Maximum number of configured CSI-RS resources for phase offset report across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC 3. Maximum number of simultaneously active CSI-RS resources for phase offset report per CC 4. Maximum number of simultaneously active CSI-RS resources for phase offset report across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC 5. Value of X for CPU occupation (OCPU=XNTRP) | 59-2-3-3 | yes | n/a | CJTC PO report is not supported | Per band and Per BC | n/a | n/a | n/a FR1 only | Component 1 candidate values: {2, 4, 6, 8, 10, 12} Component 2 candidate values: {2, 4, 6, 8, 12, … 64} Component 3 candidate values: {2, 4, 6, 8, 12, 16, 20, 24, 28, 32} Component 4 candidate values: {2, 4, 6, 8, 12, 16, 20, 24, 28, 32, …, 64} Component 5 candidate values: {1, 2} | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-3-4 | CJTC subband PO report | 1. Configured maximum resolution (number of steps) for the quantization alphabet for CJTC SB PO reporting 2. Configured minimum subband size in resource blocks for the CJTC subband PO report 3. Supported value of scaling factor X for OCPU calculation 4. Supported maximum slot duration for NTRP P/SP CSI-RS occasions being confined in | 2-35 | yes | n/a | CJTC subband PO report is not supported | Per band and Per BC | n/a | n/a | n/a FR1 only | Component 1 candidate values: {16, 32} Component 2 candidate values: {1, 2, 4, 8, 16} Component 3 candidate values: {1, 2} Component 4 candidate values: {1, 2} Note：OCPU =X.NTRP | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-3-5 | CJTC Dd+FO report | 1. Configured minimum quantization range for CJTC Dd reporting 2. Configured maximum resolution (number of steps) for the quantization alphabet for CJTC Dd reporting 3. Configured minimum quantization range for CJTC FO reporting 4. Configured maximum resolution (number of steps) for the quantization alphabet for CJTC FO reporting 5. Supported value of scaling factor X for OCPU calculation | 2-35, 59-2-3-1, 59-2-3-2 | yes | n/a | CJTC Dd+FO report is not supported | Per band and Per BC | n/a | n/a | n/a FR1 only | Component 1 candidate values: {half cyclic prefix, full cyclic prefix} Component 2 candidate values: {32, 64, 128, 256} Note: For component 1 and 2, the larger granularity considering component 1 and 2 reported value is the lower capability Component 3 candidate values: {0.1ppm, 0.2ppm} Component 4 candidate values: {16, 32, 256} Note: For component 3 and 4, the larger granularity considering component 3 and 4 reported value is the lower capability Component 5 candidate values: {1, 2} Note: For component 5, the larger value is the lower capability Note: OCPU =2X.NTRP Note: parts per million (ppm) of the carrier frequency | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-3-5a | CJTC Dd+FO report processing | 1. Maximum number of configured TRS resource sets for joint delay and frequency offset report 2. Maximum number of configured TRS resource sets for joint delay and frequency offset report across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC 4. Maximum number of simultaneously active CSI-RS resources for joint delay and frequency offset report per CC 4. Maximum number of simultaneously active CSI-RS resources for joint delay and frequency offset report across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC 5. Value of X for CPU occupation (OCPU=2XNTRP) | 59-2-3-5 | yes | n/a | CJTC Dd+FO report is not supported | Per band and Per BC | n/a | n/a | n/a FR1 only | Component 1 candidate values: {2, 4, 6, 8, 10, 12} Component 2 candidate values: {2, 4, 6, 8, 12, … 64} Component 3 candidate values: {2, 4, 6, 8, 12, 16, 20, 24, 28, 32} Component 4 candidate values: {2, 4, 6, 8, 12, 16, 20, 24, 28, 32, …, 64} Component 5 candidate values: {1, 2} | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-3-6a | New CJT QCL assumptions for PDSCH pre-compensation for Scheme-C | The PDSCH DMRS port(s) are QCLed with the DL-RS associated with the first TCI state with respect to QCL-TypeA and QCLed with the DL-RS in the second TCI state with respect to QCL-TypeA except for {Doppler shift} | 40-1-1 | yes | n/a | New QCL assumptions for PDSCH pre-compensation is not supported for Scheme-C | Per band | n/a | n/a | n/a FR1 only |  | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-3-6b | New CJT QCL assumptions for PDSCH pre-compensation for Scheme-D | 1. The PDSCH DMRS port(s) are QCLed with the DL-RS associated with the first TCI state with respect to QCL-TypeA and QCLed with the DL-RS in the second TCI state with respect to QCL-TypeA except for {average delay} | 40-1-1 | yes | n/a | New QCL assumptions for PDSCH pre-compensation is not supported for Scheme-D | Per band | n/a | n/a | n/a FR1 only |  | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-3-6c | New CJT QCL assumptions for PDSCH pre-compensation for Scheme-E | 1.The PDSCH DMRS port(s) are QCLed with the DL-RS associated with the first TCI state with respect to QCL-TypeA and QCLed with the DL-RS in the second TCI state with respect to QCL-TypeA except for {Doppler shift, average delay} | 40-1-1 | yes | n/a | New QCL assumptions for PDSCH pre-compensation is not supported for Scheme-E | Per band | n/a | n/a | n/a FR1 only |  | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-3-7 | Linkage of CJTC Dd and Rel-18 eType-II CJT with joint triggering | 1. Support of joint triggering for linked CJTC Delay offset reporting and Rel-18 eType-II CJT CSI | 59-2-3-1 and 40-3-1-1 | yes | n/a | Linkage of CJTC Dd and Rel-18 eType-II CJT with joint triggering is not supported | Per band and Per BC | n/a | n/a | n/a FR1 only |  | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-3-7a | Linkage of CJTC Dd and Rel-18 eType-II CJT with separate triggering | Support separate triggering for linked CJTC Delay offset reporting and Rel-18 eType-II CJT CSI | 59-2-3-1 and 40-3-1-1 | yes | n/a | Separate triggering for linked CJTC Delay offset reporting and Rel-18 eType-II CJT CSI is not supported | Per band and Per BC | n/a | n/a | n/a FR1 only |  | Optional with capability signalling |
> | 59. NR_MIMO_Ph5 | 59-2-3-8 | Separate triggering with configuration of 1-bit indicator per CSI trigger state | Support of 1 bit indicate per trigger state for separate triggering of linked DO reporting and Type II CJT reporting | 59-2-3-7a | yes | n/a | Separate triggering with configuration of 1-bit indicator per CSI trigger state is not supported | Per band and Per BC | n/a | n/a | n/a FR1 only |  | Optional with capability signalling |

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601216](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601216.zip) · `[124-R19-UE features]`

### RAN1#123 — 9건

**Agreement** · `7` Pre-Rel-19 NR Maintenance · `RAN1#123:7:011` · 후보

> The following TPs for TS38.213 for Rel.18 are endorsed.
> The final CRs capturing the following TPs for 38.213 for Rel-18 and Rel-19 (mirror) are R1-2509603 and R1-2509604, respectively, are endorsed.
> | 7.1.1 UE behaviour ============== unchanged parts are omitted =============== - is a downlink pathloss estimate in dB calculated by the UE using reference signal (RS) index for the active DL BWP, as described in clause 12, of carrier of serving cell - If the UE is not provided PUSCH-PathlossReferenceRS and enableDefaultBeamPL-ForSRS, or before the UE is provided dedicated higher layer parameters, the UE calculates - using a RS resource from an SS/PBCH block with same SS/PBCH block index as the one the UE uses to obtain MIB, or using the SS/PBCH block the UE acquired the time and frequency synchronization for a secondary cell. - if the UE is provided RACH-LessHO in ReconfigurationWithSync [12. TS 38.331], using a RS resource from an SS/PBCH block with same SS/PBCH block index as the one with same quasi co-location properties as for PDCCH receptions for scheduling an initial PUSCH transmission, as described in Clause 10.1, in controlResourceSetZero provided in ServingCellConfigCommon of ReconfigurationWithSync, or using a RS resource from the pathlossReferenceRS-Id-r17 configured by a TCI state associated with tci-StateID. ============== unchanged parts are omitted =============== |
> | 22 PUSCH transmission in NTN RACH-less handover 22.1 Configured-grant PUSCH transmission ============== unchanged parts are omitted =============== A PUSCH occasion is valid if it does not overlap with a valid PRACH occasion as described in clause 8.1. For unpaired spectrum and for SS/PBCH blocks with indexes provided by rrc-SSB-Subset in cg-RRC-Configuration, or ssb-PositionsInBurst in ServingCellConfigCommon if rrc-SSB-Subset is not provided - if a UE is not provided tdd-UL-DL-ConfigurationCommon, a PUSCH occasion is valid if the PUSCH occasion - does not precede a SS/PBCH block in the PUSCH slot, and - starts at least symbols after a last SS/PBCH block symbol, where is provided in Table 8.1-2 - if a UE is provided tdd-UL-DL-ConfigurationCommon, a PUSCH occasion is valid if the PUSCH occasion - is within UL symbols - starts at least symbols after a last downlink symbol, and at least symbols after a last SS/PBCH block symbol, where is provided in Table 8.1-2. A UE determines a power of a PUSCH transmission as described in clause 7.1.1, where the UE obtains using a RS resource from an SS/PBCH block with index associated with the PUSCH transmission or the pathlossReferenceRS-Id-r17 configured by a TCI state associated with tci-StateID. |
> | 22.2 Dynamic-grant PUSCH transmission If ssb-Index or tci-StateID is provided in RACH-LessHO, the UE may assume that the DM-RS antenna port associated with the PDCCH receptions for scheduling initial PUSCH transmission and the SS/PBCH block indicated by ssb-Index or the DL RS configured by a TCI state associated with tci-StateID are quasi co-located with respect to average gain and quasi co-location 'typeA' or 'typeD' properties. |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509534](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509534.zip)

**Agreement** · `8.5` Maintenance on Enhancements of network energy savings for NR · `RAN1#123:8.5:004` · 후보

> Adopt the following TP for TS 38.214 Clause 5.1.5.
> Reason for change: UE behavior on using a different beam for OD-SSB from AO-SSB or for different OD-SSBs (when AO-SSB is not present) is not specified.
> Summary of changes: Add UE behavior on using a different beam for OD-SSB from AO-SSB or for different OD-SSBs (when AO-SSB is not present).
> Consequence if not approved: UE behavior on using a different beam for OD-SSB from AO-SSB or for different OD-SSBs (when AO-SSB is not present) is confusing.
> =========================== Start of TP =================================
> 5.1.5	Antenna ports quasi co-location
> ====================== Unchanged Text Omitted ============================
> When a UE is configured with dl-OrJointTCI-StateList and is having two indicated TCI-states, when the offset between the reception of the scheduling/activation DCI format 1_0/1_1/1_2 and the scheduled or activated PDSCH reception is less than timeDurationForQCL in frequency range 2, and if the PDSCH and a PDCCH overlaps in at least one symbol
> -	If the UE does not report its capability of defaultQCL-TwoTCI, and if the 'QCL-TypeD' of the PDSCH DMRS is different from any one of those of PDCCH DMRS, the UE is expected to prioritize the reception of PDCCH. This also applies to the intra-band CA case (when PDSCH and the PDCCH are in different component carriers).
> For a UE configured with both od-ssb-absoluteFrequency in OD-SSB-Config and absoluteFrequencySSB for a SCell, when the UE applies a TCI state wherein an SS/PBCH block index, provided by SSB-index in the TCI state or QCLed with a reference signal in the TCI state, corresponds to an actually transmitted SS/PBCH block index provided by od-ssb-PositionsInBurst in the OD-SSB-Config but does not correspond to an actually transmitted SS/PBCH block index provided by ssb-PositionsInBurst associated with the absoluteFrequencySSB, the UE does not expect that the transmission of the SS/PBCH blocks corresponding to the SS/PBCH block index is deactivated.
> For a UE configured with OD-SSB-Config and not configured with absoluteFrequencySSB for a SCell, when the UE applies a TCI state wherein an SS/PBCH block index is provided by SSB-index in the TCI state or QCLed with a reference signal in the TCI state, the UE does not expect that the transmission of the SS/PBCH blocks corresponding to the SS/PBCH block index is deactivated.
> ============================ End of TP =================================

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2508896](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2508896.zip) · `[123-R19-NES]`

**Agreement** · `8.6` Maintenance on Low-power wake-up signal and receiver for NR (LP-WUS/WUR) · `RAN1#123:8.6:004` · 후보

> Adopt the following TP to section 5.1.6.1 and 5.2.2.5, TS 38.214 in principle.
> | ----------------------------------------- Text proposal for TS38.214-j00 clause 5.1.6.1-------------------------------- 5.1.6.1 CSI-RS reception procedure <omitted text> If the UE is configured with DRX and, - if the UE is configured to monitor DCI format 2_6 or WUS and configured by higher layer parameter ps-TransmitOtherPeriodicCSI or lpwus-TransmitOtherPeriodicCSI to report CSI with the higher layer parameter reportConfigType set to 'periodic' and reportQuantity set to quantities other than 'cri-RSRP', 'cri-RSRP-Index', 'ssb-Index-RSRP' and 'ssb-Index-RSRP-Index' when drx-onDurationTimer in DRX-Config [or lpwus_PDCCHMonitoringTimer in [XYZxxx]] is not started, the most recent CSI measurement occasion occurs in DRX active time or during the time duration indicated by drx-onDurationTimer in DRX-Config also outside DRX active time for CSI to be reported; - if the UE is configured to monitor DCI format 2_6 or WUS and configured by higher layer parameter ps-TransmitPeriodicL1-RSRP or lpwus-TransmitPeriodicL1-RSRP to report L1-RSRP with the higher layer parameter reportConfigType set to 'periodic' and reportQuantity set to 'cri-RSRP' or 'cri-RSRP-Index' when drx-onDurationTimer in DRX-Config [or lpwus_PDCCHMonitoringTimer [in XYZxxx]] is not started, the most recent CSI measurement occasion occurs in DRX active time or during the time duration indicated by drx-onDurationTimer in DRX-Config also outside DRX active time for CSI to be reported; - otherwise, the most recent CSI measurement occasion occurs in DRX active time for CSI to be reported. --------------------------------------------- End of Text proposal for TS38.214 sec 5.1.6.1--------------------------- ------------------------------------------ Text proposal for TS38.214-j00 clause5.2.2.5 ------------------------------ 5.2.2.5 CSI reference resource definition <omitted text> When the UE is configured to monitor DCI format 2_6 or WUS, - if the UE configured by higher layer parameter ps-TransmitOtherPeriodicCSI or lpwus-TransmitOtherPeriodicCSI to report CSI with the higher layer parameter reportConfigType set to 'periodic' and reportQuantity set to quantities other than 'cri-RSRP', 'ssb-Index-RSRP', 'cri-RSRP- Index', and 'ssb-Index-RSRP- Index ' when drx-onDurationTimer [or lpwus_PDCCHMonitoringTimer] is not started, the UE shall report CSI with the reportQuantity not set to ‘ssb-Index-SINR’ or ‘ssb-Index-SINR-Index’ during the time duration indicated by drx-onDurationTimer in DRX-Config also outside active time according to the procedure described in Clause 5.2.1.4 if receiving at least one CSI-RS transmission occasion for channel measurement and CSI-RS and/or CSI-IM occasion for interference measurement during the time duration indicated by drx-onDurationTimer in DRX-Config outside DRX active time or in DRX Active Time no later than CSI reference resource and drops the report otherwise; - if the UE is configured with a CSI report configuration containing a list of sub-configurations provided by csi-ReportSubConfigToAddModList, and if the UE configured by higher layer parameter ps-TransmitOtherPeriodicCSI or lpwus-TransmitOtherPeriodicCSI to report CSI with the higher layer parameter reportConfigType set to 'periodic' and reportQuantity set to quantities other than 'cri-RSRP', 'ssb-Index-RSRP', 'cri-RSRP- Index', and 'ssb-Index-RSRP- Index' when drx-onDurationTimer [or lpwus PDCCHMonitoringTimer] is not started, UE shall report a CSI report including one or more sub-reports only during the time duration indicated by drx-onDurationTimer in DRX-Config also outside active time according to the procedure described in Clause 5.2.1.4 if receiving at least one CSI-RS transmission occasion for channel measurement and CSI-RS and/or CSI-IM occasion for interference measurement during the time duration indicated by drx-onDurationTimer in DRX-Config outside DRX active time or in DRX Active Time, per sub-configuration, no later than CSI reference resource and drops the report otherwise, where the sub-configuration is the configured one for P-CSI reporting; - if the UE configured by higher layer parameter ps-TransmitPeriodicL1-RSRP or lpwus-TransmitOtherPeriodicL1-RSRP to report L1-RSRP with the higher layer parameter reportConfigType set to 'periodic' and reportQuantity set to 'cri-RSRP', 'ssb-Index-RSRP', 'cri-RSRP- Index', or 'ssb-Index-RSRP- Index' when drx-onDurationTimer [or lpwus_PDCCHMonitoringTimer] is not started, the UE shall report L1-RSRP during the time duration indicated by drx-onDurationTimer in DRX-Config also outside active time according to the procedure described in clause 5.2.1.4 and when reportQuantity set to 'cri-RSRP' or 'cri-RSRP- Index' if receiving at least one CSI-RS transmission occasion for channel measurement during the time duration indicated by drx-onDurationTimer in DRX-Config outside DRX active time or in DRX Active Time no later than CSI reference resource and drops the report otherwise. --------------------------------------- End of Text proposal for TS38.214 clause 5.2.2.5------------------------------ |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · `[123-R19-LP-WUS]`

**Agreement** · `8.8` Maintenance on others · `RAN1#123:8.8:006` · 후보

> Endorse the following TP to TS38.213 Section 21
> | Reasons of change: For a UE not supporting CSI-RS for BM as Type-D QCL source RS of LTM TCI state, it is not possible for the UE to find a TCI state whose QCL RS has the same value as RS signalled from higher layer that meets the C-LTM execution condition. Summary of change: Additionally allow UE to determine a TCI state whose QCL RS is QCLed with the RS signalled from higher layer that meets the C-LTM execution condition. Consequences if not approved: A UE not supporting CSI-RS for BM as Type-D QCL source RS of LTM TCI state cannot perform C-LTM. |
> | 21 L1/L2-triggered mobility procedures < Unchanged parts are omitted > For RACH-based LTM cell switch [19, TS 38.300], the UE applies the CandidateTCI-State for receptions on the candidate cell, and applies a spatial domain filter corresponding to the CandidateTCI-State or the CandidateTCI-UL-State for transmissions on the candidate cell, that are after the completion of the random access procedure associated with the PRACH transmission on the candidate cell and before a new TCI state is applied for the candidate cell. For RACH-less LTM cell switch [19, TS 38.300], the UE applies the CandidateTCI-State for receptions on the candidate cell and applies a spatial domain filter corresponding to the CandidateTCI-State or the CandidateTCI-UL-State for transmissions on the candidate cell before a new TCI state is applied for the candidate cell. After RACH-based conditional LTM cell switch, all activated TCI states are deactivated. For RACH-less conditional LTM cell switch, the UE determines a TCI state in CandidateTCI-State or CandidateTCI-UL-State to apply for receptions or transmissions on the candidate cell, where QCL RS of the TCI state is same as SS/PBCH block selected in the RACH-less conditional LTM cell switch as described in clause 5.36.3 [11, TS 38.321]. After RACH-less conditional LTM cell switch, all activated TCI states, other than the TCI state, are deactivated. < Unchanged parts are omitted > |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509086](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509086.zip)

**Agreement** · `8.8` Maintenance on others · `RAN1#123:8.8:008` · 후보

> Endorse the following TP to TS38.213 Section 21
> | Reason for change: As agreed, for both RACH-based and RACH-less CLTM, activated TCI states (except the determined TCI state, if present) are deactivated, after RACH-based or RACH-less CLTM is performed. However, current SPEC wordings can mislead reader that activated TCI states (except the determined TCI state, if present) are deactivated, after RACH-based or RACH-less CLTM is completed, which prolongs the time of deactivating TCI states. Summary of change: Clarify that for both RACH-based and RACH-less CLTM, activated TCI states (except the determined TCI state, if present) are deactivated, after RACH-based or RACH-less CLTM is performed. Consequences if not approved: Incorrect behavior, which is not aligned with corresponding agreements. |
> | 21 L1/L2-triggered mobility procedures < Unchanged parts are omitted > After RACH-based conditional LTM cell switch, all activated TCI states are deactivated. For RACH-less conditional LTM cell switch, the UE determines a TCI state in CandidateTCI-State or CandidateTCI-UL-State to apply for receptions or transmissions on the candidate cell, where a QCL RS index of the TCI state is same as a SS/PBCH block index or a CSI-RS resource index selected in the RACH-less conditional LTM cell switch as described in clause 5.36.3 [11, TS 38.321]. After RACH-less conditional LTM cell switch, all activated TCI states, other than the TCI state, are deactivated. < Unchanged parts are omitted > |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509087](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509087.zip)

**Agreement** · `8.8` Maintenance on others · `RAN1#123:8.8:009` · 후보

> Endorse the following TP to TS38.213 Section 21
> | Reason for change: The currently agreed CR (R1-2508229) does not explicitly define the application duration for the TCI state determined by the UE after a RACH-less CLTM cell switch. Summary of change: Add “before a new TCI state is applied for the candidate cell” as an ending condition of the candidate TCI state application. Consequences if not approved: UE may apply mismatched TCI states, resulting in incorrect cell measurements and degraded mobility performance. |
> | ==================================unchanged omitted=================================== 21 L1/L2-triggered mobility procedures ==================================unchanged omitted=================================== The UE does not expect to be indicated quasi co-location 'typeA' properties when a SS/PBCH block is configured as a source RS of the TCI state. The UE applies the CandidateTCI-State and/or CandidateTCI-UL-State, if indicated by the MAC CE, no later than after the last symbol of a PUCCH or PUSCH with HARQ-ACK information for the PDSCH providing the MAC CE, where , , and are defined in [10, TS 38.133]. For RACH-based LTM cell switch [19, TS 38.300], the UE applies the CandidateTCI-State for receptions on the candidate cell, and applies a spatial domain filter corresponding to the CandidateTCI-State or the CandidateTCI-UL-State for transmissions on the candidate cell, that are after the completion of the random access procedure associated with the PRACH transmission on the candidate cell and before a new TCI state is applied for the candidate cell. For RACH-less LTM cell switch [19, TS 38.300], the UE applies the CandidateTCI-State for receptions on the candidate cell and applies a spatial domain filter corresponding to the CandidateTCI-State or the CandidateTCI-UL-State for transmissions on the candidate cell before a new TCI state is applied for the candidate cell. After RACH-based conditional LTM cell switch, all activated TCI states are deactivated. For RACH-less conditional LTM cell switch, the UE determines a TCI state in CandidateTCI-State or CandidateTCI-UL-State to apply for receptions or transmissions on the candidate cell, where a QCL RS index of the TCI state is same as a SS/PBCH block index or a CSI-RS resource index selected in the RACH-less conditional LTM cell switch as described in clause 5.36.3 [11, TS 38.321]. After RACH-less conditional LTM cell switch, all activated TCI states, other than the TCI state, are deactivated. ==================================unchanged omitted=================================== |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509087](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509087.zip)

**Agreement** · `9.2` UE features Batch B · `RAN1#123:9.2:014` · 후보

> Introduce the following FG 66-14/14a:
> | 66-14 | Unified TCI with joint DL/UL TCI update by DCI format 1_3 for intra-cell and inter-cell beam management with more than one MAC-CE activated joint TCI state per CC with different SCS and/or different carrier type | 1: TCI state indication for update and activation MAC-CE+DCI-based TCI state indication (use of DCI formats 1_3 with DL assignment for at least one serving cell in a scheduledCellListDCI-1-3 to provide indicated unified TCI state(s) for the CC(s) in the scheduledCellListDCI-1-3) 2: The minimum beam application time in Y symbols per SCS 3: The maximum number of MAC-CE activated joint TCI states per CC in a band | 23-1-1, 66-1 |  |  |  | Per band | N/A | N/A | N/A | Component 2 candidate values: {1, 2, 4, 7, 14, 28, 42, 56, 70, 84, 98, 112, 224, 336}, where {84, 98, 112, 224, 336} only can be indicated in FR2 Component 3 candidate values: {2, 3, 4, 5, 6, 7, 8} Note: The maximum number of MAC-CE activated joint TCI states across all CC(s) in a band for more than one MAC-CE activated joint TCI state is signaled in 23-1-1, component 5 Note: activated joint TCI state(s) include all PDCCH/PDSCH receptions and PUSCH/PUCCH Note: For component 2 and 3, same values as for FG23-1-1b are reported (if the UE also report FG23-1-1b) | Optional with capability signaling |
> | 66-14a | Unified TCI with separate DL/UL TCI update by DCI format 1_3 for intra-cell beam management with more than one MAC-CE activated separate TCI state per CC with different SCS and/or different carrier type | 1. TCI state indication for update and activation MAC-CE+DCI-based TCI state indication (use of DCI formats 1_3 with DL assignment for at least one serving cell in a scheduledCellListDCI-1-3 to provide indicated unified TCI state(s) for the CC(s) in the scheduledCellListDCI-1-3) 2. The minimum beam application time in Y symbols per SCS 3. The maximum number of MAC-CE activated DL TCI states per CC in a band 4. The maximum number of MAC-CE activated UL TCI states per CC in a band | 23-10-1, 66-1 |  |  |  | Per band | N/A | N/A | N/A | If a UE supports FG 23-10-1m, the signalled component values also apply to inter-cell beam management Candidate values of component 2: {n1, n2, n4, n7, n14, n28, n42, n56, n70, n84, n98, n112, n224, n336} Candidate values of component 3: {2, …, 8} Candidate values of component 4: {2, …, 8} Note: For component 2, 3 and 4, same values as for FG23-10-1b are reported (if the UE also report FG23-10-1b) | Optional with capability signaling |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx)

**Agreement** · `9.3` UE features Batch C · `RAN1#123:9.3:006` · 후보

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-1 | Increased number of reported RSs for beam management | 1. Support of reporting format for L1-RSRP measurements not including CRI/SSBRI other than one for the largest measured L1-RSRP in a reporting instance, if the number of reported L1-RSRPs is equal to the size of the measurement resource set. 2. Support of reporting format for L1-RSRPs and corresponding beam information of Top M beam(s) with largest M measured value(s) of L1-RSRP(s) of a measurement resource set, where M is configured by gNB, if the number of reported L1-RSRPs is smaller than the size of the measurement resource set 3. Maximum number of M reported RSs, M>4 | {2-21, 2-22} or {2-23, 2-23a} or {2-29 or 2-24}2-24 or 2-29 | yes | n/a | Increased number of reported beams for beam management is not supported | Per band | n/a | n/a | n/a | Component 3 candidate values: {6,8} | Optional with capability signalling |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx)

**Agreement** · `9.3` UE features Batch C · `RAN1#123:9.3:010` · 후보

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-1-1 | UE-initiated/event-driven beam management for Event-2 based measurement and report for Mode A | 1. Support of UE-initiated/event-driven beam report based on one event instance 2. Support of Event-2 based measurement and report 3. Support of Mode A UE-initiated/event-driven beam report 4. Maximum number of the configured RS(s) for new beam in the RS resource set 5. Support of current beam measurement by using QCL RS in the indicated TCI state and the corresponding QCL SSB for Scheme-1 and Scheme-2, respectively 6. Support the first PUCCH and second PUSCH from the same PUCCH group | 2-22, 2-24 | yes | n/a | UEI/ED beam report is not supported for Event-2 and Mode A | Per band | n/a | n/a | n/a | Component 4 candidate values: {1, 2, …, 64} Note For Component 4 and Component 5, an SSB can be associated with the serving cell PCI or a PCI other than the serving cell PCI Note: Regarding Event-2, QCL RS(s) in indicated TCI state(s) and resources configured for component 4 are also counted in FG 16-1g, and 16-1g-1 | Optional with capability signalling |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx)

### RAN1#122bis — 11건

**Agreement** · `8.3` Maintenance on Evolution of NR duplex operation: Sub-band full duplex (SBFD) · `RAN1#122bis:8.3:001` · 후보

> Adopt the following TP in principle to Clause 11.1, TS 38.213.
> | 11.1 Slot configuration *** Unchanged parts are omitted *** A downlink or flexible symbol provided by tdd-UL-DL-ConfigurationCommon can include an UL sub-band provided by ul-SubbandlocationAndBandwidth, a first DL sub-band provided by firstDL-SubbandlocationAndBandwidth and may additionally include a second DL sub-band provided by secondDL-SubbandlocationAndBandwidth, for a SCS configuration of any configured UL BWP or DL BWP, respectively, as provided by scs-SpecificCarrierList [4, TS 38.211]. The downlink or flexible symbol is then referred to as an SBFD symbol; otherwise, it is referred to as a non-SBFD symbol. Unless otherwise stated, the UE considers symbols in a slot indicated as downlink and as SBFD by tdd-UL-DL-ConfigurationCommon to be available for transmissions. Uplink symbols by tdd-UL-DL-ConfigurationCommon are non-SBFD symbols. An SBFD symbol or a non-SBFD symbol provided by tdd-UL-DL-ConfigurationCommon cannot change to a non-SBFD symbol or to an SBFD symbol, respectively, by other information. The UE is not provided coresetPoolIndex and is not configured to receive PDSCH according to more than one TCI states mapped to one TCI codepoint [6, TS 38.214] for a serving cell where the UE is provided SBFD symbols. For an UL sub-band, a first DL sub-band or a second DL sub-band, the frequency location of the sub-band is provided by the corresponding parameters, respectively: a common RB and a number of contiguous RBs provided by ul-SubbandlocationAndBandwidth, or firstDL-SubbandlocationAndBandwidth or secondDL-SubbandlocationAndBandwidth that indicates an offset and a length as RIV according to [6, TS 38.214], setting , and a value provided by offsetToCarrier for the subcarrierSpacing. *** Unchanged parts are omitted *** |
> Send an LS to RAN2 to inform that the assumptions of firstDL-subbandlocationAndBandwidth, secondDL-subbandlocationAndBandwidth and ul-subbandlocationAndBandwidth highlighted below are described in TS 38.213, clause 11.1 instead of clause 12.
> | firstDL-subbandlocationAndBandwidth Configures frequency domain location and bandwidth of the first DL subband. The value of the field shall be interpreted as resource indicator value (RIV) as defined in TS 38.214 with assumptions as described in TS 38.213 [13], clause 12. The network does not configure this field for UL carriers. |
> | secondDL-subbandlocationAndBandwidth Configures frequency domain location and bandwidth of the second DL subband. The value of the field shall be interpreted as resource indicator value (RIV) as defined in TS 38.214 with assumptions as described in TS 38.213 [13], clause 12. The network does not configure this field for UL carriers. |
> | ul-subbandlocationAndBandwidth Configures frequency domain location and bandwidth of UL subband. The value of the field shall be interpreted as resource indicator value (RIV) as defined in TS 38.214 with assumptions as described in TS 38.213 [13], clause 12. The network does not configure this field for DL carriers. |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · `[122bis-R19-SBFD]`

**Agreement** · `8.3` Maintenance on Evolution of NR duplex operation: Sub-band full duplex (SBFD) · `RAN1#122bis:8.3:011` · 후보

> Adopt the following TP in principle to Clause 6.1.2.1, TS 38.214.
> | 6.1.2.1 Resource allocation in time domain *** Unchanged parts are omitted *** For PUSCH repetition Type B, the UE determines invalid symbol(s) for PUSCH repetition Type B transmission as follows: - A symbol that is indicated as downlink by tdd-UL-DL-ConfigurationCommon or tdd-UL-DL-ConfigurationDedicated, and, when applicable, not indicated as SBFD symbols by tdd-UL-DL-ConfigurationCommon, is considered as an invalid symbol for PUSCH repetition Type B transmission. - For operation in unpaired spectrum, symbols indicated by ssb-PositionsInBurst in SIB1 or ssb-PositionsInBurst in ServingCellConfigCommon for reception of SS/PBCH blocks are considered as invalid symbols for PUSCH repetition Type B transmission. - For a reduced capability half-duplex UE in paired spectrum, symbols that do not start or end at least or , respectively, from the last or first symbol of an SS/PBCH block with index indicated by ssb-PositionsInBurst in SIB1 or by ssb-PositionsInBurst in ServingCellConfigCommon or by NonCellDefiningSSB, or by ssb-PositionsInBurst in SSB-MTC-AdditionalPCI associated to physical cell ID with active TCI states for PDCCH or PDSCH, or for a set of symbols of a slot corresponding to SS/PBCH blocks configured for L1 beam measurement/reporting for reception of SS/PBCH blocks are considered as invalid symbols for PUSCH repetition Type B transmission. - For operation in unpaired spectrum, symbol(s) indicated by pdcch-ConfigSIB1 in MIB for a CORESET for Type0-PDCCH CSS set are considered as invalid symbol(s) for PUSCH repetition Type B transmission. - For operation in unpaired spectrum, if numberOfInvalidSymbolsForDL-UL-Switching is configured, numberOfInvalidSymbolsForDL-UL-Switching symbol(s) after the last symbol that is indicated as downlink in each consecutive set of all symbols that are indicated as downlink by tdd-UL-DL-ConfigurationCommon or tdd-UL-DL-ConfigurationDedicated are considered as invalid symbol(s) for PUSCH repetition Type B transmission. The symbol(s) given by numberOfInvalidSymbolsForDL-UL-Switching are defined using the reference SCS configuration referenceSubcarrierSpacing provided in tdd-UL-DL-ConfigurationCommon. *** Unchanged parts are omitted *** |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · `[122bis-R19-SBFD]`

**Agreement** · `8.6` Maintenance on Low-power wake-up signal and receiver for NR (LP-WUS/WUR) · `RAN1#122bis:8.6:001` · 후보

> Adopt the following TP to Section 10.4D, TS 38.213 for alignment.
> ---------------------------------Start of Text Proposal on 3GPP TS 38.213 V19.0.0-----------------------
> 10.4D PDCCH monitoring activation by WUS in RRC_CONNECTED
> <Unchanged Text Omitted>
> If a UE is provided ABC, the UE receives WUS based on the quasi co-location information of the TCI states indicated by a most recent DCI format or MAC CE, after a respective application time in clause 5.1.5 [6, TS 38.214]; otherwise, the UE receives WUS based on the quasi co-location information of the TCI states for a CORESET with controlResourceSetId value that is same as the one indicated by WUS_TCI_states_CONNECTED.
> <Unchanged Text Omitted>
> ---------------------------------End of Text Proposal on 3GPP TS 38.213 V19.0.0-----------------------

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · `[122bis-R19-LP-WUS]`

**Agreement** · `8.6` Maintenance on Low-power wake-up signal and receiver for NR (LP-WUS/WUR) · `RAN1#122bis:8.6:003` · 후보

> Adopt the following TP to Section 10.4D, TS 38.213 in principle.
> | 10.4D PDCCH monitoring activation by WUS in RRC_CONNECTED *** Unchanged parts are omitted *** A UE configured with DRX mode operation and operating in the RRC_CONNECTED state can be provided for WUS reception on the primary cell of a cell group - a number of OOK symbols per OFDM symbol, a first RB, and overlaid OFDM sequences per OOK symbol for WUS reception [4, TS 38.211], and - a number of codepoints provided for the UE by the WUS [6, TS 38.212], by WUS-codepointCONNECTED A UE assumes that a WUS is quasi co-located with an SS/PBCH block or a CSI-RS with respect to quasi co-location 'typeC' or 'typeD' properties, when applicable. If a UE is provided ABC, the UE receives WUS based on the quasi co-location information of the TCI states provided by ABC, indicated by a most recent DCI format or MAC CE, after a respective application time; otherwise, the UE receives WUS based on the quasi co-location information of the TCI states for a CORESET with controlResourceSetId value that is same as the one indicated by WUS_TCI_states_CONNECTED. *** Unchanged parts are omitted *** |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · `[122bis-R19-LP-WUS]`

**Conclusion** · `8.6` Maintenance on Low-power wake-up signal and receiver for NR (LP-WUS/WUR) · `RAN1#122bis:8.6:010` · 후보

> If the CORESET ID provided for a UE to derive the active TCI state for LP-WUS where the CORESET has two activated TCI states, it is up to UE implementation which/how to use the active TCI states of the CORESET for LP-WUS reception.

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · `[122bis-R19-LP-WUS]`

**Agreement** · `8.8` Maintenance on others · `RAN1#122bis:8.8:008` · 후보

> - After RACH-based CLTM is performed, all activated candidate TCI states are deactivated.

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508156](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508156.zip)

**Agreement** · `8.8` Maintenance on others · `RAN1#122bis:8.8:009` · 후보

> For C-LTM, after the LTM cell switch is triggered,
> - For RACH-less LTM, the UE determines an indicated TCI state in CandidateTCI-State or CandidateTCI-UL-State whose QCL RS has the same value as the RS signaled from higher layer to lower layer that meets the C-LTM execution condition.
> - Upon RACH-less CLTM procedure being triggered, activated Candidate TCI state(s), other than the indicated TCI state, should be deactivated.

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508156](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508156.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122bis:9.1:007` · 후보

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-1 | Increased number of reported RSs for beam management | 1. Support of reporting format for L1-RSRP measurements not including CRI/SSBRI other than one for the largest measured L1-RSRP in a reporting instance, if the number of reported L1-RSRPs is equal to the size of the measurement resource set. 2. Support of reporting format for L1-RSRPs and corresponding beam information of Top M beam(s) with largest M measured value(s) of L1-RSRP(s) of a measurement resource set, where M is configured by gNB, if the number of reported L1-RSRPs is smaller than the size of the measurement resource set 3. Maximum number of M reported RSs, M>4 | FFS {2-21, 2-22} or {2-23, 2-23a} or 2-29 or 2-24 | yes | n/a | Increased number of reported beams for beam management is not supported | Per UE Per band | No n/a | No n/a | No n/a | Component 3 candidate values: {6,8} | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508080](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508080.zip)

**Agreement** · `9.6` UE features for NR mobility enhancements Phase 4 · `RAN1#122bis:9.6:001` · 후보

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 63. NR_Mob_Ph4 | 63-1 | NW triggered intra-frequency L1-RSRP measurement based on periodic CSI-RS (s) for L1-L2 Triggered Mobility (LTM) procedure | 1. Support of intra-frequency L1- RSRP measurement and reporting based on periodic CSI-RS(s) of candidate cell(s) 2. Maximum number of RRC configured candidate cells for intra-frequency L1-RSRP measurement on CSI-RS resource 3. Support of up to L candidate cells and M beams in one report where a CRI-RSRP pair is used for each beam report for intra-frequency L1-RSRP measurement 4. Maximum number of LTM CSI report configs using periodic CSI-RS as measurement resource | 45-1 | Yes | No | NW triggered intra-frequency L1-RSRP measurement based on periodic CSI-RS (s) for L1-L2 Triggered Mobility (LTM) procedure is not supported | Per BC | n/a | n/a | n/a | Component 2 candidate values: {1,2,3,4,5,6,7,8} Component 3 candidate values: L: {1, 2,3,4} M: {1, 2,3,4} M L: {1,2,3,4, 6, 8, 9, 12, 16} Component 4 candidate values: Aperiodic: {0,1,2,3,4} Periodic: {1,2,3,4} Semi-persistent: {0,1,2,3,4} | Optional with capability signaling |
> | 63. NR_Mob_Ph4 | 63-1a | NW triggered inter-frequency L1-RSRP measurement based on periodic CSI-RS (s) for L1-L2 Triggered Mobility (LTM) procedure | 1. Support of inter-frequency L1- RSRP measurement and reporting based on periodic CSI-RS(s) of candidate cell(s) 2. Maximum number of RRC configured candidate cells for inter-frequency L1-RSRP measurement on CSI-RS resource 3. Support of up to L candidate cells and M beams in one report where a CRI-RSRP pair is used for each beam report for inter-frequency L1-RSRP measurement 4. Maximum number of LTM CSI report configs using periodic CSI-RS as measurement resource | 45-1a | Yes | No | NW triggered inter-frequency L1-RSRP measurement based on periodic CSI-RS (s) for L1-L2 Triggered Mobility (LTM) procedure is not supported | Per BC | n/a | n/a | n/a | Component 2 candidate values: {1,2,3,4,5,6,7,8} Component 3 candidate values: L: {1, 2,3,4} M: {1, 2,3,4} M L: {1,2,3,4, 6, 8, 9, 12, 16} Component 4 candidate values: Aperiodic: {0,1,2,3,4} Periodic: {1,2,3,4} Semi-persistent: {0,1,2,3,4} | Optional with capability signaling |
> | 63. NR_Mob_Ph4 | 63-2 | NW triggered intra-frequency L1-RSRP measurement based on semi-persistent CSI-RS (s) for L1-L2 Triggered Mobility (LTM) procedure | 1. Support of intra-frequency L1- RSRP measurement and reporting based on semi-persistent CSI-RS(s) of candidate cell(s) 2. Maximum number of LTM CSI report configs using semi-persistent CSI-RS as measurement resource | 63-1 | Yes | No | NW triggered intra-frequency L1-RSRP measurement based on semi-persistent CSI-RS (s) for L1-L2 Triggered Mobility (LTM) procedure is not supported | Per BC | n/a | n/a | n/a | Component 2 candidate values: Aperiodic: {0,1,2,3,4} Semi-persistent: {0,1,2,3,4} Note: For component 4, the UE must support a non-zero value for at least one of aperiodic and semi-persistent | Optional with capability signaling |
> | 63. NR_Mob_Ph4 | 63-2a | NW triggered inter-frequency L1-RSRP measurement based on semi-persistent CSI-RS (s) for L1-L2 Triggered Mobility (LTM) procedure | 1. Support of inter-frequency L1- RSRP measurement and reporting based on semi-persistent CSI-RS(s) of candidate cell(s) 2. Maximum number of LTM CSI report configs using semi-persistent CSI-RS as measurement resource | 63-1a | Yes | No | NW triggered inter-frequency L1-RSRP measurement based on semi-persistent CSI-RS (s) for L1-L2 Triggered Mobility (LTM) procedure is not supported | Per BC | n/a | n/a | n/a | Component 2 candidate values: Aperiodic: {0,1,2,3,4} Semi-persistent: {0,1,2,3,4} Note: For component 4, the UE must support a non-zero value for at least one of aperiodic and semi-persistent | Optional with capability signaling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508083](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508083.zip)

**Agreement** · `11.1` Overview of 6GR air interface · `RAN1#122bis:11.1:003` · 후보

> - The aspects to consider for supporting NTN include, but not limited to
>   - Initial access, including cell search and SSB periodicity
>   - Coverage
>   - Duplexing
>   - Capacity
>   - Signalling overhead
>   - GNSS-less/resilient/based operation
>   - Large/varying doppler and propagation delay
>   - Beamforming / beam management / beam hopping
> Note:
> - High-level aspects to consider to enable lower CAPEX/OPEX with respect to current networks include, but not limited to
>   - UE/NW implementation complexity
>   - UE/NW energy efficiency
>   - MRSS
>   - Spectrum efficiency

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · `[122bis-R20-6GR-Overall]`

**Agreement** · `11.5` Energy efficiency · `RAN1#122bis:11.5:005` · 후보

> Study and evaluate NW energy savings and the impact on UE performance and user experience with respect to 20ms and longer periodicities of sync signal(s) at least for initial access with the following consideration, but not limited to:
> BS assumptions:
> - Cell-common signaling (e.g., sync signal(s), broadcast PDCCH, SIB-1, SIB, paging, PRACH), e.g.,
>   - Clustered provisioning of different cell-common signaling,
>   - On-demand provisioning of different cell-common signaling,
> - UE-specific signaling (for low, light, medium loads), e.g.,
>   - Clustered provisioning with cell-common signaling,
>   - Unclustered provisioning with cell-common signaling,
> UE impact:
> - Cell search complexity and latency, including frequency search latency,
> - UE Power consumption,
> - Sync signal detection, coverage and tracking performance,
> - RRM, mobility,
> - Beam management,
> - Other properties are not precluded,
> - Improvements to address identified impact, e.g.,
>   - Additional sync signal needs,
>   - Adaptation of sync signal transmission periodicity,
>   - Sparser synch raster.

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · `[122bis-R20-6GR-Energy efficiency]`

### RAN1#122 — 14건

**Agreement** · `5` Incoming Liaison Statements · `RAN1#122:5:002` · 후보

> The following contents are included in the reply LS on CSI-RS based CFRA using SBFD RO.
> | RAN1 thanks RAN2 for the LS on CSI-RS based CFRA using SBFD RO. RAN1 would like to provide the following feedback to RAN2. RAN1 agrees that CBRA and CFRA in SBFD symbols are supported for SBFD-aware UEs in RRC_CONNECTED. For L3 HO and BFR, CSI-RS-based CFRA using SBFD RO is considered to have no impact on RAN1 specifications. |
> Send LS to inform RAN2 about this agreement.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip)

**Agreement** · `8.3.1` SBFD TX/RX/measurement procedures · `RAN1#122:8.3.1:002` · 후보

> Adopt the following TP to TS 38.213 Clause 7.1.1.
> | Reason for change According to TS38.214 Clause 6.1.2.2.1, only the resource blocks that are both in the active UL BWP and in the UL sub-band are used for PUSCH transmission in SBFD symbol(s). Accordingly, the PUSCH transmission power in SBFD symbols should be calculated based on the resource blocks that are both in the active UL BWP and in the UL sub-band only. Summary of change Clarify that the PUSCH transmission power in SBFD symbols should be calculated based on the resource blocks that are both in the active UL BWP and in the UL sub-band only. |
> | 7.1.1 UE behaviour If a UE transmits a PUSCH on active UL BWP of carrier of serving cell using parameter set configuration with index and PUSCH power control adjustment state with index - if the UE is indicated a first TCI-State or TCI-UL-State and a second TCI-State or TCI-UL-State, and is configured with multipanelSchemeSDM or multipanelSchemeSFN or sTx-2Panel, and the UE determines to apply both the first TCI-State or TCI-UL-State and the second TCI-State or TCI-UL-State in PUSCH transmission occasion , the UE determines the PUSCH transmission power for the k-th indicated TCI-State or TCI-UL-State as [dBm] <omitted texts> - is the bandwidth of the PUSCH resource assignment expressed in number of resource blocks for PUSCH transmission occasion on active UL BWP of carrier of serving cell and is a SCS configuration defined in [4, TS 38.211]. If PUSCH transmission occasion is in SBFD symbols, is the number of assigned RBs for PUSCH transmission occasion on active UL BWP of carrier of serving cell that are both in the active UL BWP and in the UL sub-band as described in Clause 6.1.2.2.1 in [6, TS 38.214]. <omitted texts> |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip)

**Agreement** · `8.5.1` On-demand SSB SCell operation · `RAN1#122:8.5.1:006` · 후보

> - Adopt the following TP for TS 38.213 Clause 10
> Reason for change: Puncturing of SSB bandwidth can be applicable for OD-SSB.
> Summary of changes: Add “after puncturing if applicable”.
> Consequence if not approved: Specification is confusing for puncturing of SSB.
> | 10 UE procedure for receiving control information *** Unchanged parts are omitted *** For monitoring of a PDCCH candidate by a UE, if the UE - has received ssb-PositionsInBurst in SIB1 and has not received ssb-PositionsInBurst in ServingCellConfigCommon for a serving cell, and - does not monitor PDCCH candidates in a Type0-PDCCH CSS set, and - at least one RE for a PDCCH candidate overlaps with at least one RE of a candidate SS/PBCH block, after puncturing if applicable, corresponding to a SS/PBCH block index provided by ssb-PositionsInBurst in SIB1, the UE is not required to monitor the PDCCH candidate. For monitoring of a PDCCH candidate by a UE, if the UE - has received ssb-PositionsInBurst in ServingCellConfigCommon for a serving cell, and - does not monitor PDCCH candidates in a Type0-PDCCH CSS set, and - at least one RE for a PDCCH candidate overlaps with at least one RE of a candidate SS/PBCH block, after puncturing if applicable, corresponding to a SS/PBCH block index provided by ssb-PositionsInBurst in ServingCellConfigCommon, the UE is not required to monitor the PDCCH candidate. For monitoring of a PDCCH candidate by a UE, if the UE - has received an indication for transmission of second SS/PBCH blocks on a serving cell as described in Clause 4.4, and - at least one RE for a PDCCH candidate overlaps with at least one RE of a candidate SS/PBCH block, from the second SS/PBCH blocks, corresponding to a SS/PBCH block index provided as described in Clause 4.4, the UE is not required to monitor the PDCCH candidate. For monitoring of a PDCCH candidate by a UE, if the UE - has received ssb-PositionsInBurst in SSB-MTCAdditionalPCI for a serving cell, and - at least one RE for a PDCCH candidate overlaps with at least one RE of a candidate SS/PBCH block, after puncturing if applicable, corresponding to a SS/PBCH block index provided by ssb-PositionsInBurst in SSB-MTCAdditionalPCI with same physical cell identity as the one associated with a RS having same quasi-collocation properties as a CORESET for the PDCCH candidate, the UE is not required to monitor the PDCCH candidate. A UE is not required to monitor PDCCH candidates for a Type0/0A/0B/1/1A /2/2A -PDCCH CSS set when the active TCI state for a corresponding CORESET is not associated with physCellId in ServingCellConfigCommon. *** Unchanged parts are omitted *** |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506494](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506494.zip)

**Agreement** · `8.5.1` On-demand SSB SCell operation · `RAN1#122:8.5.1:007` · 후보

> Adopt the following TP for TS 38.213 Clause 11.1.1.
> --------------------------------------------------- Start of Text Proposal for TS 38.213 ---------------------------------------------
> 11.1.1	UE procedure for determining slot format
> < Unchanged parts are omitted >
> For a set of symbols of a slot corresponding to SS/PBCH blocks with candidate SS/PBCH block indices corresponding to the SS/PBCH block indexes indicated to a UE by ssb-PositionsInBurst in SIB1, or by ssb-PositionsInBurst in ServingCellConfigCommon, as described in clause 4.1, or as described in Clause 4.4, or by NonCellDefiningSSB or, if the UE is not provided dl-OrJointTCI-StateList, by ssb-PositionsInBurst in SSB-MTCAdditionalPCI associated to physical cell ID with active TCI states for PDCCH or PDSCH, or for a set of symbols of a slot corresponding to SS/PBCH blocks configured for L1 beam measurement/reporting, the UE does not expect to detect a DCI format 2_0 with an SFI-index field value indicating the set of symbols of the slot as uplink.
> < Unchanged parts are omitted >
> ------------------------------------------------------- End of Text Proposal --------------------------------------------------------

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506494](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506494.zip)

**Agreement** · `8.5.2` On-demand SIB1 for idle/inactive mode Ues · `RAN1#122:8.5.2:002` · 후보

> Adopt the following TP for Clause 5.3.2 and 6.3.3.1 in TS38.211 to clarify the PRACH transmission for SIB1 request.
> --------------------------------- start of TP for 38.211-------------------------------------
> 5.3.2	OFDM baseband signal generation for PRACH
> <omitted text>
> -	 is the subcarrier spacing of the initial uplink bandwidth part during initial access. If the PRACH transmission is for a candidate cell  is provided by ltm-PRACH-SubcarrierSpacing in EarlyUL-SyncConfig. Otherwise,  is the subcarrier spacing of the active uplink bandwidth part;
> -	 is the largest  value among the subcarrier spacing configurations by the higher-layer parameter scs-SpecificCarrierList;
> -	 is the lowest numbered resource block of the initial uplink bandwidth part and is derived by the higher-layer parameter initialUplinkBWP or initialUplinkBWP-RedCap during initial access and from the higher-layer parameters bwp-GenericParameters in EarlyUL-SyncConfig if the PRACH transmission is for a candidate cell. Otherwise,  is the lowest numbered resource block of the active uplink bandwidth part and is derived by the higher-layer parameter BWP-Uplink;
> <omitted text>
> 6.3.3.1	Sequence generation
> <omitted text>
> There are 64 preambles defined in each time-frequency PRACH occasion, enumerated in increasing order of first increasing cyclic shift  of a logical root sequence, and then in increasing order of the logical root sequence index, starting with the index obtained from the higher-layer parameter prach-RootSequenceIndex or rootSequenceIndex-BFR or by msgA-PRACH-RootSequenceIndex if configured and a type-2 random-access procedure is initiated as described in clause 8.1 of [5, TS 38.213] or by prach-RootSequenceIndex in EarlyUL-SyncConfig if the PRACH transmission is for a candidate cell or. Additional preamble sequences, in case 64 preambles cannot be generated from a single root Zadoff-Chu sequence, are obtained from the root sequences with the consecutive logical indexes until all the 64 sequences are found. The logical root sequence order is cyclic; the logical index 0 is consecutive to . The sequence number  is obtained from the logical root sequence index according to Tables 6.3.3.1-3 to 6.3.3.1-4B.
> --------------------------------- end of TP for 38.211-------------------------------------

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506400](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506400.zip)

**Conclusion** · `8.6.3` LP-WUS operation in CONNECTED modes · `RAN1#122:8.6.3:011` · 후보

> - For the RRC parameter LP-WUS_unifiedTCI_CONNECTED,
>   - This parameter is not necessary, and legacy RRC parameter dl-OrJointTCI-StateList is used to apply the unified TCI for LP-WUS reception

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip)

**Agreement** · `8.8` Maintenance on channel modelling enhancements for 7-24GHz for NR · `RAN1#122:8.8:006` · 후보

> Adopt the following TP to TR38.901
> - Reason for change: Breaking up the cluster and ray scaling angles for CDL angle scaling, such that other WG may be able to reference the TR easily. Also improves readability of the angle scaling for CDL models.
> - Summary of change: introduce an intermediate variable to represent cluster angles, which are the angles being scaled by the model.
> - Consequences if not approved: Difficult for WGs to identify scaled angle component in CDL models.
> ===== Start of TP for TR38.901=====
> 7.7.5.1	CDL extension: Scaling of angles
> The angle values of CDL models are fixed, which is not very suitable for MIMO simulations for several reasons; The PMI statistics can become biased, and a fixed precoder may perform better than open-loop and on par with closed-loop or reciprocity beamforming. Furthermore, a CDL only represents a single channel realization. The predefined angle values in the CDL models can be generalized by introducing angular translation and scaling. By translation, mean angle  can be changed to   and angular spread  can be changed to match  by scaling. The translated and scaled ray angles can be obtained according to the following equation:
> (7.7-5)
> (7.7-5a)
> (7.7-5b)
> (7.7-5c)
> (7.7-5d)
> in which:
> < Unchanged text omitted >
> -		is the desired rms cluster angular spread,
> -		is the scaled CDL cluster angle of the nth cluster,
> -	 is the resulting scaled ray angle that corresponds to mth subpath angle of nth cluster,
> < Unchanged text omitted >
> Alternatively, for CDL-D and CDL-E, if maintaining the LOS angle is desired, the translated and scaled ray angles can be obtained according to the following equation instead of using equation (7.7-5) and (7.7-5a):
> (7.7-6)
> (7.7-6a)
> (7.7-6b)
> in which:
> -	 is the LOS path angle of the model.
> -	 is the scaled CDL cluster angle of the nth cluster,
> < Unchanged text omitted >
> ===== End of TP for TR38.901=====

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · `[122-R19-7-24GHz]`

**Agreement** · `8.9.1` Measurements related enhancements for LTM · `RAN1#122:8.9.1:002` · 후보

> Following TP to TS38.213 Section 21 is endorsed as editorial change.
> - Reason for change: RAN1 agreed that CSI-RS for BM as the referenceSignal with QCL-TypeD is supported for an LTM TCI state, where TRS is configured as referenceSignal with QCL-TypeA. The agreement has been captured in above texts in TS 38.213. However, in current texts, it is said that the TRS and the CSI-RS resources to provide QCL 'typeA' and 'typeD' properties, which is incorrect. There should be only one CSI-RS resource for indicating QCL 'typeD' property. Hence, we propose to adopt the Text Proposal 2 as below.
> - Summary of change: Remove unnecessary “s”.
> - Consequences if not approved: Incorrect UE and/or NW behavior.
> | Text Proposal 2 for TS 38.213 Clause 21 < Unchanged parts are omitted > A UE can be provided by an LTM Cell Switch Command MAC CE in a PDSCH reception on the serving cell [11, TS 38.321] a TCI state ID and/or an UL TCI state ID indicating a CandidateTCI-State and/or CandidateTCI-UL-State from ltm-DL-OrJointTCI-StateToAddModList and/or ltm-UL-TCI-StateToAddModList [6, TS 38.214] for applicable receptions or transmissions on a candidate cell from the number of candidate cells. The UE may assume that DM-RS antenna ports for PDCCH receptions and for PDSCH receptions are quasi co-located either with the SS/PBCH block or the TRS in the TCI state with respect to quasi co-location 'typeA' and 'typeD' properties, when applicable, or with the TRS and the CSI-RS resources in the CSI-RS resource set configured with repetition in the TCI state with respect to quasi co-location 'typeA' and 'typeD' properties, respectively, when applicable. < Unchanged parts are omitted > |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122:9.1:002` · 후보

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-1 | Increased number of reported RSs for beam management | 1. Support of reporting format for L1-RSRP measurements not including CRI/SSBRI other than one for the largest measured L1-RSRP in a reporting instance, if the number of reported L1-RSRPs is equal to the size of the measurement resource set. 2. Support of reporting format for L1-RSRPs and corresponding beam information of Top M beam(s) with largest M measured value(s) of L1-RSRP(s) of a measurement resource set, where M is configured by gNB, if the number of reported L1-RSRPs is smaller than the size of the measurement resource set 3. Maximum number of M reported RSs, M>4 | FFS | yes | n/a | Increased number of reported beams for beam management is not supported | FFS Per UE | FFS N/A | FFS N/A | FFS N/A | Component 3 candidate values: {6,8} | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506605](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506605.zip)

**Agreement** · `9.6` UE features for NR mobility enhancements Phase 4 · `RAN1#122:9.6:006` · 후보

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 63. NR_Mob_Ph4 | 63-3 | CSI-RS as Type-D QCL source RS in the indicated joint LTM TCI state | Support CSI-RS for BM as Type-D QCL source RS and TRS as Type-A QCL source RS in the indicated joint LTM TCI states | FFS 45-3 | Yes | No | UE does not support CSI-RS for BM as Type-D QCL source RS and TRS as Type-A QCL source RS in the indicated joint LTM TCI states | Per band | n/a | n/a | n/a |  | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506608](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506608.zip)

**Agreement** · `9.6` UE features for NR mobility enhancements Phase 4 · `RAN1#122:9.6:007` · 후보

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 63. NR_Mob_Ph4 | 63-3a | CSI-RS as Type-D QCL source RS for MAC-CE activated joint LTM TCI states | Support CSI-RS for BM as Type-D QCL source RS and TRS as Type-A QCL source RS for MAC-CE activated joint LTM TCI states | FFS 45-3a, 63-3 | Yes | No | UE does not support CSI-RS for BM as Type-D QCL source RS and TRS as Type-A QCL source RS for MAC-CE activated joint LTM TCI states | Per band | n/a | n/a | n/a |  | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506608](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506608.zip)

**Agreement** · `9.6` UE features for NR mobility enhancements Phase 4 · `RAN1#122:9.6:008` · 후보

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 63. NR_Mob_Ph4 | 63-4 | CSI-RS as Type-D QCL source RS in the indicated separate DL/UL LTM TCI states | Support CSI-RS for BM as Type-D QCL source RS and TRS as Type-A QCL source RS in the indicated separate DL/UL LTM TCI states | FFS 45-4 | Yes | No | UE does not support CSI-RS for BM as Type-D QCL source RS and TRS as Type-A QCL source RS in the indicated separate DL/UL LTM TCI states | Per band | n/a | n/a | n/a |  | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506608](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506608.zip)

**Agreement** · `9.6` UE features for NR mobility enhancements Phase 4 · `RAN1#122:9.6:009` · 후보

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 63. NR_Mob_Ph4 | 63-4a | CSI-RS as Type-D QCL source RS for MAC-CE activated separate DL/UL LTM TCI states | Support CSI-RS for BM as Type-D QCL source RS and TRS as Type-A QCL source RS for MAC-CE activated separate DL/UL LTM TCI states | FFS 45-4a, 63-4 | Yes | No | UE does not support CSI-RS for BM as Type-D QCL source RS and TRS as Type-A QCL source RS for MAC-CE activated separate DL/UL LTM TCI states | Per band | n/a | n/a | n/a |  | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506608](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506608.zip)

**Agreement** · `9.6` UE features for NR mobility enhancements Phase 4 · `RAN1#122:9.6:010` · 후보

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 63. NR_Mob_Ph4 | 63-2 | NW triggered intra-frequency L1-RSRP measurement based on semi-persistent CSI-RS (s) for L1-L2 Triggered Mobility (LTM) procedure | 1. Support of intra-frequency L1- RSRP measurement and reporting based on semi-persistent CSI-RS(s) of candidate cell(s) 42. Maximum number of LTM CSI report configs using semi-persistent CSI-RS as measurement resource | 63-1 | Yes | No | NW triggered intra-frequency L1-RSRP measurement based on semi-persistent CSI-RS (s) for L1-L2 Triggered Mobility (LTM) procedure is not supported | Per BC | n/a | n/a | n/a | Component 42 candidate values: Aperiodic: {0,1,2,3,4} Semi-persistent: {0,1,2,3,4} Note: For component 4, the UE must support a non-zero value for at least one of aperiodic and semi-persistent | Optional with capability signaling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506608](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506608.zip)
