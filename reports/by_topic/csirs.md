# CSI-RS — RAN1 CSI 결정

> 원본 DB 마지막 업데이트 **2026-10-19 20:12 KST** · [요약으로 돌아가기](../README.md)

확정 41건 (Agreement 36 · WA 1 · Conclusion 4), 후보 15건. 결정 본문은 Chair notes 원문 그대로입니다(요약 없음). 최신 회의부터 보여줍니다.

## RAN1#126bis — 5건

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126bis:10.5.3.1:003` · 🆕 신규

> For 6GR CSI-RS, for discussion purpose of CSI-RS frequency domain behavior,
> - In frequency domain,
>   - The CSI-RS band is defined as a number of consecutive RB sets, where each RB set contains Y consecutive RBs. Within the Y RBs, the number of RBs with CSI-RS REs is M2<=Y. The set of REs within per RB set occupied by CSI-RS does not change across the RB sets.
>   - Mapping granularity of all CSI-RS ports without repetition is a single RB set

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126bis:10.5.3.1:004` · 🆕 신규

> Support PN sequence with QPSK modulation as the 6GR CSI-RS sequence
> - Note: whether other sequence type is supported for certain usages (e.g., PN with Pi/2-BPSK modulation for sensing) is to be discussed separately in corresponding agendas

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126bis:10.5.3.1:016` · 🆕 신규

> - Send an LS to RAN4 requesting guidance on whether there is an update on the limit for CSI-RS power boosting compared with R1-103331.
>   - The LS will include RAN1 agreements on simulation assumptions and candidate CDM types in the Appendix
> - Before RAN4 feedback, RAN1 continues to assume 6dB power boosting limit as indicated in R1-103331

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126bis:10.5.3.1:021` · 🆕 신규

> For the evaluation of precoded CSI-RS:
> - For the benchmark:
>   - Each CDM group of group size , is transmitted by  TXRUs, where , and  is the number of TXRU.
>   - Companies report the mapping between the CDM groups and the associated   TXRUs.
> - For the precoded CSI-RS Options:
>   - Each CDM group is transmitted by all  TXRUs.
> The total transmit power difference per symbol between precoded CSI-RS and benchmark is given by .
> Companies to report , , , number of CSI-RS ports, and frequency density

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.3` Other aspects · `RAN1#126bis:10.5.3.3:007` · 🆕 신규

> Study and evaluate the following assistance information for sub use case 1B
> - Received power difference between UE Rx ports or port groups based on measurement on CSI-RS, and/or NW side spatial domain covariance matrix information
> - Other options are not precluded.
> - Note: the assistance information is reported by the UE to the NW
> - Send a LS to RAN4 to inform the above information relevant to use case 1B and ask about the achievable accuracy of the received power difference between UE Rx ports or port groups based on measurement on CSI-RS.
> Appendix

출처: [Chair notes RAN1#126bis_eom](https://www.3gpp.org/ftp/Meetings_3GPP_SYNC/RAN1/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom.docx) · `[126bis-R20-6GR-Other Aspects related to CSI]`

## RAN1#126 — 10건

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#126:9.2:004`

> The MAC-CE in MSG4, when UE transition from IDLE/INACTIVE to CONNECTED mode, indicates whether aperiodic TRS is triggered or not.
> - Note: The corresponding MAC-CE indication design is up to RAN2.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606465](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606465.zip) · `[126-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#126:9.2:008`

> For CSI-RS frequency-domain density = 1/8, confirm the following working assumption made in RAN1#123:

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606466](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606466.zip) · `[126-R20-MIMO]`

**WA** · `9.2` NR MIMO Phase 6 · `RAN1#126:9.2:009`

>   - K=2 24-port NZP CSI-RS resources in a resource set aggregating 48 CSI-RS ports

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606466](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606466.zip) · `[126-R20-MIMO]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126:10.5.3.1:003`

> - On defining the CSI-RS pattern in M1 slots and M2 RBs, support both M1 and M2 can be larger than or equal to 1
>   - For M1,
>     - For the number of CSI-RS ports smaller than or equal to X, only M1=1 is supported.
>     - For the number of CSI-RS ports larger than X, support M1 can be larger than 1
>     - FFS value of X
>   - FFS for M2

남은 FFS 2건

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126:10.5.3.1:005`

> On the design of CDM group size and type for 6G CSI-RS, study and evaluate the following detailed candidates in addition to the ones supported in NR
> - For Option 2-2: Larger CDM size
>   - Candidate 2-2-1: cdm16-FD4-TD4
>   - Candidate 2-2-2: cdm16-FD2-TD8
>   - Candidate 2-2-3: cdm16-FD8-TD2
>   - Candidate 2-2-4: cdm16-FD16
>   - Candidate 2-2-5: cdm32-FD4-TD8
>   - Candidate 2-2-6: cdm32-FD8-TD4
>   - Candidate 2-2-7: cdm64-FD8-TD8
>   - Candidate 2-2-8: cdm12y-FD12-TDy, where y = {1, 2, 4}
> - For Option 2-3: New CDM type for NR CDM size
>   - Candidate 2-3-1: cdm4-FD4
>   - Candidate 2-3-2: cdm8-FD4-TD2
>   - Candidate 2-3-3: cdm8-FD8
> - Companies to report the applicable number of CSI-RS ports for each candidate in the simulation

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126:10.5.3.1:006`

> For CSI-RS sequence in 6G, take the NR PN sequence and mapping as the baseline for evaluation, further study the following aspects
> - How to achieve low-PAPR for pre-coded CSI-RS by sequence and/or mapping, compared to NR PN sequence and its mapping
> - Handle the case with high inter-cell interference /how to handle the case with high inter-cell interference
> - CSI-RS sharing for different frequency density
> - On sequence initialization, take NR UE specific configuration for initialization as the baseline, study whether other options are needed

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126:10.5.3.1:007`

> For 6G CSI-RS, study the following options to address the potential PAPR issue caused by precoded CSI-RS
> - Option 1: BS implementation-based approach, e.g., use UE-transparent CDM-specific small cyclic shifts, or use small CDM group size
> - Option 2: Map the PN sequence to the global subcarrier indices in the whole bandwidth sequentially
> - Option 3: Multiply the PN sequence with an additional CDM group-specific scrambling sequence
> - Option 4: Multiply the PN sequence with an additional port-specific scrambling sequence
> - Option 5: Apply segmented phase rotation on the PN sequence

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126:10.5.3.1:010`

> For CSI-RS sharing Use case 2: Sharing a common set or subset of REs among CSI-RS with different frequency densities, study the following alternatives for discussing frequency density common sequence mapping
> - Alt 1: Generate sequence for higher frequency density first, from which extract lower frequency density sequence
> - Alt 2: Generate sequences for lower frequency density first, which are concatenated to form higher frequency density sequence

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126:10.5.3.1:011`

> - For CSI-RS sharing Use case 1: Sharing a common set or subset of REs among CSI-RS with different number of ports, taking Level 1 (Sharing granularity is CDM group level) as baseline,
> - Study Level 2 (Sharing granularity can be smaller than a CDM group), with the following sub-levels
> - Level 2-1: CDM group is decoded without assuming the knowledge of
> - Level 2-2: CDM group is decoded assuming the knowledge of

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126:10.5.3.1:014`

> For 6GR CSI-RS, study CSI-RS design to achieve low CSI-RS overhead considering the following possible directions
> - Direction 1: Sparse CSI-RS in frequency/spatial domain
>   - Consider AI and/or non-AI prediction to reconstruct the channel at UE and/or NW side
>   - Study sparse pattern
> - Direction 2: Use non-orthogonal CSI-RS ports
>   - Study the use of cyclic shifts or scrambling sequences across CSI-RS RBs, or non-orthogonal cover code
>   - Inter CSI-RS port interference leakage is to be considered in the evaluations
> - Note: Combinations of the directions can be considered.
> - Note: At least total CSI-RS overhead, performance and UE/NW complexity are to be studied
> - Note: Companies to report the assumed CSI-RS time-domain behavior including CSI-RS periodicity in the evaluations
> - Note: companies to report how CSI-RS overhead can be reduced from system perspective

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of DL based CSI acquisition]`

## RAN1#125 — 10건

**Conclusion** · `9.2` NR MIMO Phase 6 · `RAN1#125:9.2:004`

> For early TRS when UE transition from IDLE/INACTIVE to CONNECTED mode, there is no RAN1 consensus to support that UE additionally reports via MSG3 the number of TRS bursts that the UE needs.
> Note: Number of triggered TRS burst is up to network.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2603720](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2603720.zip) · `[125-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#125:9.2:006`

> For K NZP CSI-RS resources for 48/64/128 CSI-RS ports aggregation, configured with density = 1/3, 1/4, 1/6 or 1/8:
> - The RB allocation of the NZP CSI-RS resources in frequency domain can only be either up to two consecutive RBs or uniform RB allocations.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2603723](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2603723.zip) · `[125-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#125:9.2:009`

> The K NZP CSI-RS resources for 48/64/128 CSI-RS ports aggregation, configured with density = 1/3, 1/4, 1/6 or 1/8, should follow Rel-19 time-domain restriction, i.e., the K NZP CSI-RS resources should be allocated in one or two consecutive slots.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2605114](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2605114.zip) · `[125-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#125:9.2:011`

> The RRC-configured RB-level offset(s) for K NZP CSI-RS resources configured with density  = 1/3, 1/4, 1/6 or 1/8 is configured per NZP CSI-RS resource, and candidate values of the RRC-configured RB-level offset(s) are .

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2605114](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2605114.zip) · `[125-R20-MIMO]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#125:10.5.3.1:008`

> For RE locations of CDM groups in 6GR CSI-RS pattern design, support Option 1-1: Localized CDM group similar to 5G NR, where one CDM group contains adjacent REs.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#125:10.5.3.1:009`

> For OCC sequence used in a 6GR CSI-RS CDM group, study the following options
> - Option 1: Walsh sequence
> - Option 2: DFT sequence

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#125:10.5.3.1:011`

> For the study of 6GR CSI-RS pattern in single or multiple slots/RBs in time/frequency domain
> - The number of slots for defining CSI-RS pattern is M1, and the number of RBs for defining CSI-RS pattern is M2. Study the following further aspects in this case
>   - For RE location in the M1 slots and M2 RBs,
>     - Option 1-1: Restrict that CSI-RS pattern occupies a same set of REs in each of the M1 slots and M2 RBs
>     - Option 1-2: CSI-RS pattern can occupy same or different set of REs in each of the M1 slots and M2 RBs
>       - The number of REs occupied by CSI-RS in the M1 slots and M2 RBs can be same or different
>     - FFS whether the set of REs occupied by CSI-RS changes across occasions
>   - For mapping order of CDM groups in the M1 slots and M2 RBs
>     - Option 2-1: Mapping order of CDM groups in the M1 slots and M2 RBs is fixed across multiple occasions/symbols
>     - Option 2-2: Mapping order of CDM groups in the M1 slots and M2 RBs is switched across multiple occasions/symbols
>   - Whether both or which one from M1 and M2 can be larger than 1 is to be further studied
>   - Study details for M1 and M2, including both the upper bound and detailed values
> - Note: for RAN1 study purpose, whether the CSI-RS pattern mentioned above is from NW or UE perspective is a separate discussion

남은 FFS 1건

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#125:10.5.3.1:012`

> For CSI-RS sharing use case 1 (sharing a common set or subset of REs among CSI-RS with different number of ports) in 6GR, study the following aspects
> - Level 1: Sharing granularity is CDM group level
> - Level 2: Sharing granularity can be smaller than a CDM group

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#125:10.5.3.1:013`

> For CSI-RS sharing use case 2 (Sharing a common set or subset of REs among CSI-RS with different frequency densities), study whether/how to achieve frequency density common sequence mapping.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.3` Other aspects · `RAN1#125:10.5.3.3:001`

> Study and evaluate the following options on the candidate RS(s) for finer time and frequency tracking for connected and/or idle mode, if applicable
> - Option 1: Dedicated RS for finer time and frequency tracking
>   - Periodic/semi-persistent RS, standalone aperiodic RS or combination of them can be considered for finer timing and frequency tracking
> - Option 2: DMRS
>   - PDSCH DMRS, PDCCH DMRS can be considered
> - Option 3: Synchronization signals
>   - SSB and other types of signals/channel structure or reference signal, if applicable
> - Combination of different options can also be considered, e.g., SS + dedicated RS for finer time and frequency tracking, dedicated RS for finer time and frequency tracking + DMRS, SS+DMRS etc.
> - Note 1: Periodic TRS in 5G NR is taken as the baseline for evaluation.
> - Note 2: For comprehensive comparison, companies are encouraged to provide simulation results at least considering the following assumptions for all the options in addition to the agreed simulation assumptions, if applicable
>   - DRX configuration, including DRX periodicity, on duration, etc.
>   - PDSCH is not scheduled in every slot
>     - Provide details on the interval and arrive rate of PDSCH
>       - E.g., PDSCH scheduled in burst of X slots, where X can be as low as 1.
>   - Assumptions for PDSCH DMRS including
>     - Precoding granularity: subband precoding, PRG size is reported by companies
>     - DMRS
>       - When DMRS is used for tracking, at least one additional DMRS symbol should be configured
>       - The frequency domain location of DMRS may be changed across slots
>       - The DMRS has a same bandwidth with PDSCH
>   - SNR range: Low, media, high
>   - Other aspects can be reported by companies

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Other Aspects related to CSI]`

## RAN1#124bis — 4건

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#124bis:9.2:005`

> For CSI-RS frequency-domain density ρ = 1/3, 1/4, 1/6 or 1/8 to the K NZP CSI-RS resources aggregating 48/64/128 CSI-RS ports, support RRC-configured RB-level offset(s) to indicate the occupied RBs of NZP CSI-RS resources.
> - FFS: Candidate value(s) of the RB-level offset
> - FFS: Whether to introduce any RB location restriction for the K aggregated NZP CSI-RS resources.
> - FFS: Whether the RB-level offset(s) is configured per NZP CSI-RS resource or configured per NZP CSI-RS resource set.

남은 FFS 3건

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2602829](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2602829.zip) · `[124b-R20-MIMO]`

**Agreement** · `9.2` NR MIMO Phase 6 · `RAN1#124bis:9.2:006`

> For K NZP CSI-RS resources for 48/64/128 CSI-RS ports aggregation, configured with density = 1/3, 1/4, 1/6 or 1/8,
> - Study and decide in RAN1#125 whether to introduce the frequency-domain restriction of the occupied RBs of the NZP CSI-RS resources, e.g.,
>   - Option-1: The REs occupied by the aggregated NZP CSI-RS resources should be the same as those occupied by one or more ZP CSI-RS resources with frequency density of 1 or 1/2
>   - Option-2: The aggregated low-frequency-density NZP CSI-RS resources should be allocated in one or two consecutive RBs.
>   - Option-3: The K aggregated NZP CSI-RS resources are uniformly distributed evenly within every 1/ρ RBs
> - Study and decide in RAN1#125 whether to follow Rel-19 time-domain restriction, i.e., the K NZP CSI-RS resources should be allocated in one or two consecutive slots

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2602829](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2602829.zip) · `[124b-R20-MIMO]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#124bis:10.5.3.1:008`

> 6GR CSI-RS pattern is defined as aggregation of CDM groups, for which study the following aspects
> - Whether CSI-RS pattern is defined on single or multiple slots/RBs in time/frequency domain
> - For CDM design, consider the following options
>   - RE locations of CDM groups
>     - Option 1-1: Localized CDM group similar to 5G NR, where one CDM group contains adjacent REs
>     - Option 1-2: Comb-based CDM group, where subcarriers in one CDM group are distributed following comb pattern
>   - CDM group size and type
>     - Option 2-1: Reuse/Simplify NR, i.e., CDM 1, 2, 4, 8 with potential reduction of candidates,
>     - Option 2-2: Larger CDM size, e.g., CDM 16
>     - Option 2-3: New CDM type for NR CDM size (e.g., fd-CDM4 or cdm8-FD4-TD2)
> - At least following aspects to be considered for designing CSI-RS pattern
>   - CSI-RS Overhead
>   - CSI-RS coverage
>   - CSI-RS sharing use cases
>   - Channel estimation performance
>   - NES
>   - Coexistence with other signals/channels
>   - Digital precoding/Hybrid precoding structures
>   - MRSS

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.3` Other aspects · `RAN1#124bis:10.5.3.3:004`

> Study and evaluate the following parameters and candidate values to determine the time domain factors of the RS for finer time/frequency tracking for both connected and idle modes
> - Time domain behaviour:
>   - Candidate values: periodic, aperiodic, semi-persistent
>   - Combination of them can be used for tracking
> - Periodicity for semi-persistent and periodic tracking RS, if supported
>   - Candidate values: {Y} ms,
> - Number of symbols in a slot
>   - Candidate values: {N}
> - Time interval between tracking RS symbols for finer time/frequency tracking
>   - Candidate values: {Ssymb} symbols
> - Number of consecutive slots
>   - Candidate values: { Sslot }

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Other Aspects related to CSI]`

## RAN1#124 — 4건

**Conclusion** · `9.2.2` Enhancing DL CSI acquisition · `RAN1#124:9.2.2:001`

> There is no RAN1 consensus to support periodic TRS triggered by a MAC-CE in MSG4 when UE transition from IDLE/INACTIVE to CONNECTED mode.

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2600647](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2600647.zip)

**Agreement** · `9.2.2` Enhancing DL CSI acquisition · `RAN1#124:9.2.2:009`

> MSG4-triggered aperiodic TRS is QCLed with the SSB the UE identified during the initial access procedure, on QCL-Type C.
> - FSS:  Whether to consider QCL Type-D when applicable.

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2600648](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2600648.zip)

**Agreement** · `10.5.3.3` Other aspects · `RAN1#124:10.5.3.3:001`

> Adopt the following simulation assumptions for tracking RS evaluation
> Table 1: LLS assumptions for T/F tracking
> | Parameter | Value |
> | Duplex, Waveform | FDD and TDD, CP-OFDM |
> | Carrier Frequency/SCS | 700MHz/15kHz, 4GHz/30kHz, 7GHz/30kHz, 30GHz/120kHz |
> | Number of TRPs | NTRP=1, 2, 4 Companies should report the transmission assumptions for the RS transmission for tracking in case of more than 1 TRP. |
> | Bandwidth for PDSCH | 5MHz, 20MHz, 100MHz, bandwidth for tracking RS can be reported by companies |
> | MIMO scheme | SU-MIMO, Rank 1,2,3,4 |
> | Modulation | QPSK, 16QAM, 64QAM, 256QAM and 1024QAM |
> | Precoding granularity | PRG = wideband, other value(TBD) |
> | Channel Model | CDL channel in TR38.901 For CDL-C for 4, 7 and 30 GHz - with combination of ASA and ASD scaling values in sec. 7.7.5.1 in TR 38.901, for above 6 GHz cases - ZSA = 5°, ZSD = 1° The CDL table is translated so that the strongest cluster’s AoD and AoA occur at a random angle for both the antenna panels of TRP and UE in the local coordinate. The value of the random angle is selected to be uniformly distributed from +30 to -30 degree. The random value is chosen independently for both AoD and AoA. In mTRP cases, the channel is generated per TRP. |
> | Delay spread | 30ns, 100ns, 300ns, 1000ns |
> | UE speed | 3km/h, 10km/h, 120km/h, 350km/h 500km/h |
> | Initial time offset (TO) | 1/X CP, X= 8 Other values can be reported by companies. |
> | CFO | Initial acquisition TRP: uniform distribution +/- 0.05 ppm UE: uniform distribution +/- 5, 10, 20ppm (each company to choose one) Non-initial acquisition Per TRP: uniform distribution +/- 0.05 ppm UE: uniform distribution [+/- 0.1] ppm Note 1: Those parameters are used for simulation assumptions for synchronization signals/channels in NR (TR38.802). Note 2: Other values can be reported by companies. |
> | Drift rate | 0.2 ppm/sec Other values can be reported by companies. |
> | BS antenna configuration | Around 700MHz carrier frequency 4TXRUs/32AEs: (M,N,P,Mg,Ng; Mp, Np)= (8, 2, 2, 1, 1, 1, 2), (dH,dV) = (0.5, 0.5)λ Around 4GHz carrier frequency 32TXRUs/128AEs: (M, N, P, Mg, Ng; Mp, Np) = (8,8,2,1,1,2,8). (dH, dV) = (0.5, 0.5)λ Around 7GHz carrier frequency 128 TXRUs/728AEs: (M, N, P, Mg, Ng, Mp, Np) = (24,16,2, 1, 1, 4,16). (dH,dV) = (0.5,0.8)λ Around 30GHz carrier frequency 8TXRUs / 512AEs: (M, N, P, Mg, Ng, Mp, Np) = (8, 8, 2, 2, 2; 1, 1), (dH,dV) = (0.5, 0.5)λ |
> | UE antenna configuration | Follow the agreement in 10.1. |
> | Channel estimation | Realistic channel estimation. Companies can report the CE methods. |
> | Performance metric | Estimation error (e.g., CFO/Dopler rmse), BLER, Throughput |

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · `[124-R20-6GR-Other Aspects related to CSI]`

**Agreement** · `10.5.3.3` Other aspects · `RAN1#124:10.5.3.3:005`

> Considering at least the following aspects for the tracking RS design for finer time/frequency tracking
> Set 1 (KPI):
> - Tracking performance
> - Overhead
> - Energy efficiency for NW&UE
> - UE-side complexity
> - Accuracy of QCL parameter(s) estimation

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · `[124-R20-6GR-Other Aspects related to CSI]`

## RAN1#123 — 3건

**Agreement** · `10.2.2` Enhancing DL CSI acquisition · `RAN1#123:10.2.2:003`

> For early TRS reception when UE transition from IDLE/INACTIVE to CONNECTED mode, at least support aperiodic TRS with up to  TRS burst(s) triggered by a MAC-CE in MSG4 of 4-Step RACH.
> - FFS: The value of
> - FFS: Whether to further support periodic TRS triggered by MSG4

남은 FFS 2건

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2508520](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2508520.zip)

**Conclusion** · `10.2.2` Enhancing DL CSI acquisition · `RAN1#123:10.2.2:010`

> There is no RAN1 consensus to support different frequency-domain densities configured to the K NZP CSI-RS resources in the same CSI-RS resource set for 48/64/128 CSI-RS ports aggregation.

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2508520](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2508520.zip)

**Conclusion** · `10.2.2` Enhancing DL CSI acquisition · `RAN1#123:10.2.2:011`

> There is no RAN1 consensus to support cyclic RB position in different transmission occasions for K NZP CSI-RS resources in the same CSI-RS resource set for 48/64/128 CSI-RS ports aggregation.

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2508520](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2508520.zip)

## RAN1#122bis — 1건

**Agreement** · `10.2.2` Enhancing DL CSI acquisition · `RAN1#122bis:10.2.2:004`

> For early TRS reception when UE transition from IDLE/INACTIVE to CONNECTED mode, down-select one from the followings in RAN1#123 meeting:
> - Alt-1: Support aperiodic TRS triggered by MSG4 only
> - Alt-2: Support periodic TRS triggered by MSG4 and aperiodic TRS triggered by MSG4
> - Alt-3: Support periodic TRS triggered by MSG4 only

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2506838](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2506838.zip)

## RAN1#122 — 4건

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:044`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-3-3 | CJTC wideband PO report | 1. Configured maximum resolution (number of steps) for the quantization alphabet for CJTC WB PO reporting 2. Supported value of scaling factor X for OCPU calculation 3. Supported maximum slot duration for NTRP P/SP CSI-RS occasions being confined in | 2-35 | yes | n/a | CJTC PO report is not supported | Per band and per BC | n/a | n/a | n/a | Component 1 candidate values: {16, 32} Component 2 candidate values: {1, 2} Component 3 candidate values: {1, 2} Note：OCPU =X.NTRP | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `9.2` UE features for NR MIMO Phase 5 · `RAN1#122:9.2:045`

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 59. NR_MIMO_Ph5 | 59-2-3-4 | CJTC subband PO report | 1. Configured maximum resolution (number of steps) for the quantization alphabet for CJTC SB PO reporting 2. Configured minimum subband size in resource blocks for the CJTC subband PO report 3. Supported value of scaling factor X for OCPU calculation 4. Supported maximum slot duration for NTRP P/SP CSI-RS occasions being confined in | 2-35 | yes | n/a | CJTC subband PO report is not supported | Per band and Per BC | n/a | n/a | n/a | Component 1 candidate values: {16, 32} Component 2 candidate values: {1, 2, 4, 8, 16} Component 3 candidate values: {1, 2} Component 4 candidate values: {1, 2} Note：OCPU =X.NTRP | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506606](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506606.zip)

**Agreement** · `10.2.2` Enhancing DL CSI acquisition · `RAN1#122:10.2.2:004`

> CSI-RS frequency-domain density ρ = 1/4 can be configured to the K NZP CSI-RS resources at least for the following cases:
>   - K=2 24-port NZP CSI-RS resources in a CSI-RS resource set aggregating 48 CSI-RS ports
>   - K=4 16-port NZP CSI-RS resources in a CSI-RS resource set aggregating 64 CSI-RS ports
>   - K=2 32-port NZP CSI-RS resources in a CSI-RS resource set aggregating 64 CSI-RS ports
>   - K=4 32-port NZP CSI-RS resources in a CSI-RS resource set aggregating 128 CSI-RS ports
> FFS: K=3 16-port NZP CSI-RS resources in a CSI-RS resource set aggregating 48 CSI-RS ports
> Note: It’s not precluded that the frequency-domain density configured to the K NZP CSI-RS resources in the same CSI-RS resource set for 48/64/128 CSI-RS ports aggregation can be different

남은 FFS 1건

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506539](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506539.zip)

**Agreement** · `10.2.2` Enhancing DL CSI acquisition · `RAN1#122:10.2.2:005`

> CSI-RS frequency-domain density ρ = 1/3 and 1/6 can be configured to the K NZP CSI-RS resources at least for the following cases:
>   - K=3 16-port NZP CSI-RS resources in a CSI-RS resource set aggregating 48 CSI-RS ports
> FFS: K=2 24-port NZP CSI-RS resources in a CSI-RS resource set aggregating 48 CSI-RS ports
> Note: It’s not precluded that the frequency-domain density configured to the K NZP CSI-RS resources in the same CSI-RS resource set for 48 CSI-RS ports aggregation can be different

남은 FFS 1건

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506576](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506576.zip)

---

## 후보 15건 (키워드 일치 · 확인 필요)

포함 Agenda 밖에서 키워드로 잡힌 결정입니다. CSI 범위가 아닐 수 있습니다.

### RAN1#126 — 3건

**Agreement** · `8.2` Maintenance on others · `RAN1#126:8.2:010` · 후보

> For Rel-20 LBCA via switching, in terms of collision handling, when Rel-20 LBCA via switching is configured, only the following modification to the existing Rel-19 LBCA via switching collision is needed
> - UE can receive SS/PBCH block, PDSCH, or PDCCH, or CSI-RS, or PRS configured by higher layers on the PCell in a set of symbols of a slot with bit value ‘1’, unless the set of symbols includes at least one symbol that is in the second duration.
> - UE can expect to detect a DCI format scheduling or triggering a PDSCH, or PDCCH, or CSI-RS, or PRS reception on the PCell in a set of symbols of a slot with bit value of ‘1’, unless the set of symbols includes at least one symbol that is in the second duration.
> - Note: CR will be prepared by the editor, and how to capture above is up to editor
> LP-WUS

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606746](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606746.zip) · `[126-R19-AI 8.2]`

**Agreement** · `10.5.5` Other physical layer signals, channels and procedure · `RAN1#126:10.5.5:004` · 후보

> For remote interference management for 6GR:
> - At least support wireless-based RIM framework specified in 5G/NR as starting point for 6GR.
>   - Further study whether to support backhaul-based RIM framework.
> - Support the following two types of RIM-RS:
>   - RIM-RS Type 1: transmitted by victim BS to indicate the existence of remote interference
>   - RIM-RS Type 2: transmitted by aggressor BS to detect if remote interference still exists.
>   - The RIM RS shall carry the following information:
>     - BS group ID
>     - ‘Enough/Not enough’ indication in RIM-RS Type 1
>     - ‘Near/Far’ indication in RIM RS type 1.
>     - FFS: the RIM RS can carry 6G specific information.
>     - FFS: the RIM RS to carry duplex specific information, e.g., TDD frame structure, SBFD  subband/symbol configuration.
>   - FFS the time-domain and frequency domain design of RIM RS, the sequence in RIM RS, and the configuration methods of RIM RS, time location of RIM RS.
>   - FFS whether CSI-RS can be reused as RIM RS.

남은 FFS 4건

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Other signals, channels, and procedures]`

**Agreement** · `10.5.5` Other physical layer signals, channels and procedure · `RAN1#126:10.5.5:005` · 후보

> For BS-to-BS CLI handling in 6GR, recommend to support information exchange between BSs and study the following candidate information exchange content:
> - The slot configuration in TDD and time/frequency configuration of SBFD.
> - The configuration of BS-to-BS CLI measurement RS: CSI-RS and/or 6GR SSB.
> - The BS-to-BS CLI measurement results.
> - DL Tx beam(s) information.
> - Recommended and non-recommended beam.
> - BS-to-BS CLI mitigation request.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Other signals, channels, and procedures]`

### RAN1#125 — 1건

**Agreement** · `10.5.5` Other physical layer signals, channels and procedure · `RAN1#125:10.5.5:004` · 후보

> For BS-to-BS CLI measurement in 6GR:
> - RAN1 recommends to use CSI-RS and synchronization signal (e.g., 6GR SSB) to measure BS-to-BS CLI or Channel.
>   - Further study other channel or RS used for measuring BS-to-BS CLI.
> - Study UL resource muting mechanism for handling BS-to-BS in 6GR
>   - The UL resource muting mechanism specified in 5G/NR is the baseline for study.
>   - Study both transparent and non-transparent UL resource muting mechanisms,
>   - Study the mechanism with flexible UL resource muting symbol position(s) and flexible disable/enable indication.
>   - Study UL resource muting pattern.
> - Study the information exchange between the BSs, at least including the configuration of the CSI-RS and synchronization signal, measurement results, the recommended beam index and non-recommended beam index, the TDD time/frequency resources configuration, the SBFD time/frequency resources configuration.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Other signals, channels, and procedures]`

### RAN1#124bis — 1건

**Agreement** · `10.5.2.2` Downlink transmission scheme(s) for downlink shared channels · `RAN1#124bis:10.5.2.2:007` · 후보

> - Study PDSCH and RS for PDSCH based on the following additional SLS EVM assumptions for HST scenario
>   - Note: Other parameters follow agreements on SLS EVM for non-HST scenario
>   - Note: LLS EVM parameters for HST scenario are separately discussed
> | Parameter | Value |
> | Carrier frequency and duplex | Around 4 GHz, TDD Around 7 GHz, TDD Around 30 GHz, TDD |
> | Channel model | TR 38.901 with spatial consistency (optional) |
> | Scenario and deployment at around 4 and 7 GHz | Rural macro, 500 m or 1732 m ISD between RRH sites, two TRxPs per RRH site, one or more RRH sites connected to a BBU, with RRH site to railway track distance: 100 m Inter-track distance: 6 m Train length: 400 m Train width: 3.38 m |
> | Scenario and deployment at around 30 GHz | Rural macro, 500, 1732 m between BBU sites, one or more RRH sites connected to 1 BBU, one TRxP per RRH site, with RRH site to railway track distance: 5 m Inter-RRH site distance: [580 m, 580 m, 572 m] Inter-track distance: 6 m Train length: 400 m Train width: 3.38 m |
> | UE speed | Rural macro: outdoor (350km/h, 500km/h) |
> | Number of UEs per cell and UE distribution | 300 (assuming 1000 passengers per train and at least 30% activity ratio) 100% of users in train Companies to report how UEs at distributed in train |
> | Resource utilization | 50%, 70%, 90% |
> | Multi-TRP scenario | Maximum number of coordinated TRPs is 2, 4, 8 or 16 Other number of coordinated TRPs are not precluded |
> | CSI-RS periodicity | 10 ms (optional) 20 ms (baseline) 40 ms (optional) 80 ms (optional) |
> | BS transmit power (for 20 MHz) | For around 0.7—7 GHz 49 dBm For around 30 GHz 33 dBm Note: BS Tx power scales up with bandwidth proportionally under the limitation of the maximum BS Tx power is 56 dBm Other BS transmit powers are not precluded (companies to report) |

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Transmission scheme for DL shared channel]`

### RAN1#124 — 1건

**Agreement** · `8.3` Maintenance on Evolution of NR duplex operation: Sub-band full duplex (SBFD) · `RAN1#124:8.3:003` · 후보

> Adopt the following TP to section 7.3.1.5 TS 38.211
> ---
> Reason for change
> According to the latest specifications, PRBs outside of DL BWP and DL sub-band(s) are punctured, rather than rate-matched, which is not aligned with the previous agreement.
> Summary of change
> PDSCH rate matches unavailable VRBs corresponding to PRBs not used for PDSCH reception in SBFD symbols.
> Consequences if not approved
> Rate matching does not work properly in SBFD symbols when the scheduled VRBs include unavailable VRBs corresponding to PRBs not used for PDSCH reception in SBFD symbols.
> | *** Unchanged parts are omitted *** 7.3.1.5 Mapping to virtual resource blocks The UE shall, for each of the antenna ports used for transmission of the physical channel, assume the block of complex-valued symbols conform to the downlink power allocation specified in [6, TS 38.214] and are mapped in sequence starting with to resource elements in the virtual resource blocks assigned for transmission which meet all of the following criteria: - they are in the virtual resource blocks assigned for transmission; - the corresponding physical resource blocks are declared as available for PDSCH according to clause 5.1.4 of [6, TS 38.214]; - the corresponding resource elements in the corresponding physical resource blocks are - not used for transmission of the associated DM-RS or DM-RS intended for other co-scheduled UEs as described in clause 7.4.1.1.2; - not used for non-zero-power CSI-RS, which is according to clause 7.4.1.5 and not configured by the TRS-ResourceSet IE, if the corresponding physical resource blocks are for a PDSCH scheduled by a PDCCH with the CRC scrambled by C-RNTI, MCS-C-RNTI, CS-RNTI, G-RNTI for multicast, G-CS-RNTI, or a PDSCH with SPS, except if the non-zero-power CSI-RS is a CSI-RS configured by the higher-layer parameter CSI-RS-Resource-Mobility in the MeasObjectNR IE or except if the non-zero-power CSI-RS is an aperiodic non-zero-power CSI-RS resource; - not used for PT-RS according to clause 7.4.1.2; - not declared as 'not available for PDSCH according to clause 5.1.4 of [6, TS 38.214];. - not the assigned PRBs that are in the active DL BWP and outside the DL sub-band(s) in SBFD symbols [6, TS38.214]. The mapping to resource elements allocated for PDSCH according to [6, TS 38.214] and not reserved for other purposes shall be in increasing order of first the index over the assigned virtual resource blocks, where is the first subcarrier in the lowest-numbered virtual resource block assigned for transmission, and then the index . *** Unchanged parts are omitted *** |
> Final CR is endorsed in R1-2601721.

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601634](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601634.zip) · `[124-R19-SBFD]`

### RAN1#123 — 3건

**Conclusion** · `8.6` Maintenance on Low-power wake-up signal and receiver for NR (LP-WUS/WUR) · `RAN1#123:8.6:008` · 후보

> - For RRC connected, for the case where measurement resource refers to CSI-RS/SSB or the measurement gap outside active time overlaps with LP-WUS MO, a UE may not monitor LP-WUS.
> - No specification changes.

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · `[123-R19-LP-WUS]`

**Agreement** · `9.2` UE features Batch B · `RAN1#123:9.2:013` · 후보

> Introduce the following FG 66-10/11/12/13:
> | 66-10 | Triggered HARQ-ACK codebook re-transmission for DCI format 1_3 with different SCS and/or different carrier type | 1. Support HARQ-ACK re-transmission from an earlier PUCCH slot based on the triggering information in DCI format 1_3 2. Support the related PHY priority handling in terms of HARQ-ACK codebook selection and the applicable PUCCH configuration (for a UE supporting two HARQ-ACK codebooks / PUCCH config in 66-8) 3. Supported minimum value M for the HARQ re-tx offset 4. Supported maximum value N for the HARQ re-tx offset | 66-1 |  |  |  | Per band | N/A | N/A | N/A | Candidate values for component 3 is: M = {-7, -5, …, 1} Candidate values for component 4 is: N= {4, 6, …, 24} Note: The minimum requirement for Component 3 and Component 4 of this FG is valid for HARQ CBs consisted of HARQ Processes with a single HARQ bit per HARQ Process ID For component 3 and 4, same values as for FG25-7 are reported (if the UE also report FG25-7) | Optional with capability signaling |
> | 66-11 | SCell dormancy indication within active time in DCI format 0_3/1_3 with different SCS and/or different carrier type | Support for SCell dormancy indication sent within the active time on PCell with DCI format 0_3/1_3 | 6-5, at least one of {66-1, 66-2} |  |  |  | Per BC | N/A | N/A | N/A | One dormant BWP and one non-dormant BWP is supported per carrier More than one non-dormant BWP per carrier is supported only if UE feature 6-3/6-4 is also supported One dormant BWP and one non-dormant BWP are UE specific BWPs even for UEs not supporting 6-2 or 6-3 | Optional with capability signaling |
> | 66-12 | Dynamic indication of applicable minimum scheduling restriction by DCI format 0_3/1_3 with different SCS and/or different carrier type | 1) Dynamic indication of applicable minimum scheduling restriction by DCI format 0_3 and 1_3 2) minimumSchedulingOffset K0 configuration for PDSCH and aperiodic CSI-RS triggering offset 3) minimumSchedulingOffset K2 configuration for PUSCH 4) Support of extended value range for aperiodic CSI-RS triggering offset | At least one of {66-1, 66-2} |  |  |  | Per UE | No | No | N/A |  | Optional with capability signaling |
> | 66-13 | PHY priority indication for one-shot HARQ-ACK feedback triggered by DCI format 1_3 with different SCS and/or different carrier type | Support transmission of type 3 HARQ-ACK codebook using the first or second PUCCH configuration based on PHY priority indication in the triggering DCI format 1_3 | 66-7a and 66-8 |  |  |  | Per UE | No | No | N/A |  | Optional with capability signaling |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx)

**Agreement** · `11.5` Energy efficiency · `RAN1#123:11.5:002` · 후보

> Include the following non-sleep states as 6G UE power consumption model.
> - Other power state(s) is not precluded
> - FFS: Configuration and relative power value(s) for EE processing in FR2 (including 24.25 GHz – 52.6 GHz)
> - Note: Pending agreement in 11.2 whether to evaluate 15 GHz
> | Power State | Characteristics | Relative Power in FR1 (including around 7GHz) | Relative Power in FR2 (including 24.25 GHz – 52.6 GHz) |
> | EE Processing | Processing DL WUS of OFDM-based sequence(s) for at least wake-up indication and, if applicable, other 6GR signal(s) of OFDM-based sequence(s) for synchronization and/or measurement, in an energy efficient manner, based on the following configuration: FR1 (including around 7GHz) 5 MHz BW, 1-RX / 2-RX for reception; FFS: Power values for 2-RX, i.e., X1, X2, X3 Residue CFO up to [5] ppm and residue timing offset up to [2] us Noise Figure (NF) = 6GR UE NF Reception time up to one slot Note: Whether/how to scale power values for different reception time setting within one slot to be further discussed/decided FR2 (including 24.25 GHz – 52.6 GHz) FFS Note: No implication on which configuration(s) to be supported by 6GR EE-processing can only be performed during a sleep state with additional relative power value added w.r.t. the sleep state and without triggering UE transition out of the sleep state. Additional energy overhead [15], in unit of (relative power x ms), is included for each time entering or leaving EE processing during ultra-deep/deep sleep. Ramp-up or ramp-down time for EE processing is [2] ms. | 10 / X1 (during micro sleep) 12 / X2 (during light sleep) 15 / X3 (during other sleep) | FFS |
> | PDCCH-only | No PDSCH and same-slot scheduling; this includes time for PDCCH decoding and any micro-sleep within the slot. | 100 | 175 |
> | SSB or CSI-RS proc. | SSB can be used for fine time-frequency sync. and RSRP measurement of the serving/camping cell. TRS is the considered CSI-RS for sync. FFS the power scaling for processing other configurations of CSI-RS. | 100 | 175 |
> | PDCCH + PDSCH | PDCCH + PDSCH. ACK/NACK in long PUCCH is modeled by UL power state. | 300 | 350 |
> | UL | Long PUCCH or PUSCH or PRACH FFS: Power values for more Tx power levels, i.e., X4, X5, X6, X7 | 250 (0 dBm) X4 (10 dBm) X5 (15 dBm) X6 (20 dBm) 700 (23 dBm) X7 (26 dBm) | 350 (FFS Tx power level) |

남은 FFS 1건

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · `[123-R20-6GR-Energy efficiency]`

### RAN1#122bis — 4건

**Agreement** · `8.3` Maintenance on Evolution of NR duplex operation: Sub-band full duplex (SBFD) · `RAN1#122bis:8.3:004` · 후보

> Adopt the following TP in principle to Clause 11.1, TS 38.213.
> | 11.1 Slot configuration <omitted text> If a UE would transmit a PRACH triggered by higher layers in a set of SBFD symbols and would receive a PDCCH, or a PDSCH, or a CSI-RS, or a DL PRS, the UE can select based on its implementation whether to either transmit the PRACH or receive the PDSCH, or the CSI-RS, or the DL PRSPL RS, or the PDCCH. <omitted text> |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · `[122bis-R19-SBFD]`

**Agreement** · `8.3` Maintenance on Evolution of NR duplex operation: Sub-band full duplex (SBFD) · `RAN1#122bis:8.3:013` · 후보

> Adopt the following TP in principle for section 11.1, TS 38.213:
> | 11.1 Slot configuration <Unchanged parts omitted> For a set of symbols of a slot corresponding to a valid PRACH occasion and symbols before the valid PRACH occasion, as described in clause 8.1, the UE does not receive PDCCH, PDSCH, or CSI-RS in the slot if a reception would overlap with any symbol from the set of symbols. The UE does not expect the set of symbols of the slot to be indicated as downlink by tdd-UL-DL-ConfigurationCommon or tdd-UL-DL-ConfigurationDedicated. If a UE would transmit a PRACH triggered by higher layers in a set of SBFD symbols and would receive a PDCCH, or a PDSCH, or a CSI-RS, or a DL PRS, the UE can select based on its implementation whether to either transmit the PRACH or receive the PDSCH, or the CSI-RS, or the PL RS, or the PDCCH. |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · `[122bis-R19-SBFD]`

**Conclusion** · `8.8` Maintenance on others · `RAN1#122bis:8.8:006` · 후보

> Confirm the following UE behavior as RAN1 common understanding:
> - After UE receives the LTM CSC MAC CE, a capable UE can still measure P-CSI-RS and SP CSI-RS resources activated before the LTM CSC MAC-CE, even if these CSI-RS resources are not counted/defined as “active”.

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508156](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508156.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122bis:9.1:013` · 후보

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-7 | Data collection for UE-side beam prediction | 1. Support of data collection for UE-side beam prediction 2. Support of SS/PBCH block and 1-port CSI-RS based RSRP measurements for measurement RS resource sets (Set B and Set A) for data collection 3. Supported sub-use cases 6: Supported maximum number of resources for Set B 7: Supported maximum number of resources for Set A 8. Support of SSB as RS type for Set B 9. Support of CSI-RS as RS type for Set B 10. Support of SSB as RS type for Set A 11. Support of CSI-RS as RS type for Set A | FFS 2-35 | yes | n/a | Data collection for UE-side beam prediction is not supported | Per UE Per band | No n/a | No n/a | No n/a | Component 3 candidate values: {‘Set B equal to Set A’, ‘Set B subset of Set A’,’Set B not a subset of Set A’} Component 6 candidate values: {4, 8, 16, 32, 64} Component 7 candidate values: {8, 16, 32, 64} Note: it is up to RAN2 whether this FG is merged into data collection FG defined by RAN2 | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508080](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508080.zip)

### RAN1#122 — 2건

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122:9.1:007` · 후보

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-7 | Data collection for UE-side beam prediction [for BM case 1] | 1. Support of data collection for UE-side beam prediction [for BM case 1] 2. Support of SS/PBCH block and 1-port CSI-RS based RSRP measurements for measurement RS resource sets (Set B and Set A) for data collection [3. Supported sub-use cases: {‘Set B equal to Set A’, ‘Set B subset of Set A’,’Set B not a subset of Set A’}] [6: Supported maximum number of resources for Set B] [7: Supported maximum number of resources for Set A] 8. Support of SSB as RS type for Set B 9. Support of CSI-RS as RS type for Set B 10. Support of SSB as RS type for Set A 11. Support of CSI-RS as RS type for Set A | FFS | yes | n/a | Data collection for UE-side beam prediction is not supported [for BM case 1] | FFS Per UE | FFS N/A | FFS N/A | FFS N/A | Component 3 candidate values: {‘Set B equal to Set A’, ‘Set B subset of Set A’,’Set B not a subset of Set A’} Component 6 candidate values: {4, 8, 16, 32, 64} Component 7 candidate values: {8, 16, 32, 64} Note: it is up to RAN2 whether this FG is merged into data collection FG defined by RAN2 | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506605](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506605.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122:9.1:028` · 후보

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-7 | Data collection for UE-side beam prediction [for BM case 1] | 1. Support of data collection for UE-side beam prediction [for BM case 1] 2. Support of SS/PBCH block and 1-port CSI-RS based RSRP measurements for measurement RS resource sets (Set B and Set A) for data collection 3. Supported sub-use cases 6: Supported maximum number of resources for Set B 7: Supported maximum number of resources for Set A 8. Support of SSB as RS type for Set B 9. Support of CSI-RS as RS type for Set B 10. Support of SSB as RS type for Set A 11. Support of CSI-RS as RS type for Set A | FFS | yes | n/a | Data collection for UE-side beam prediction is not supported [for BM case 1] | Per UE | N/A | N/A | N/A | Component 3 candidate values: {‘Set B equal to Set A’, ‘Set B subset of Set A’, ’Set B not a subset of Set A’} Component 6 candidate values: {4, 8, 16, 32, 64} Component 7 candidate values: {8, 16, 32, 64} Note: it is up to RAN2 whether this FG is merged into data collection FG defined by RAN2 | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506605](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506605.zip)
