# AI/ML CSI — RAN1 CSI 결정

> 원본 DB 마지막 업데이트 **2026-10-21 09:04 KST** · [요약으로 돌아가기](../README.md)

주된 주제가 AI/ML CSI인 확정 188건 (Agreement 178 · WA 0 · Conclusion 10), 후보 5건. 결정 본문은 Chair notes 원문 그대로입니다(요약 없음). 최신 회의부터 보여줍니다.
주된 주제가 다른 결정 중 이 주제가 관련 주제로 붙은 것은 맨 아래 '관련 결정'에 모았습니다.

## RAN1#126bis — 9건

**Conclusion** · `9.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#126bis:9.1.1:001` · 🆕 신규 · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

구현 영향: 측정·보고량

> For CSI feedback via two-sided model, there is no consensus on the need for RAN1 specification impact of CQI.
> - Note: The calculation of the CQI reported by the UE is upto UE implementation
> - Note: It is upto RAN4 to decide whether to adopt a different performance requirement for CQI testing.

출처: [Chair notes RAN1#126bis_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom1.docx)

**Agreement** · `9.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#126bis:9.1.1:002` · 🆕 신규 · 관련 주제: CSI 보고/codebook, CSI-RS · 규격 작업 (WI)

구현 영향: 포트·자원·레이어 수

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> Support following configuration for NW data collection
> - Resources for channel and interference measurement (i.e., resourcesForChannelMeasurement, csi-IM-ResourcesForInterference, nzp-CSI-RS-ResourcesForInterference)
>   - resourcesForChannelMeasurement is mandatory
> - Port configuration (N1/N2)
> - Port mapping method  for > 32 ports
> - Rank configuration
>   - Mandatory
> - Subband configuration (i.e., csi-ReportingBand)
> - FFS other parameters depending on discussion of CBSR, data quality indicator and event trigger

FFS 1줄

출처: [Chair notes RAN1#126bis_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom1.docx)

**Agreement** · `9.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#126bis:9.1.1:003` · 🆕 신규 · 규격 작업 (WI)

> With respect to RAN2 LS in R1-2606980 (R2-2606052), the draft LS response in R1-2608768 is endorsed.
> The corresponding final reply LS in R1-2608769 is endorsed.

출처: [Chair notes RAN1#126bis_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom1.docx) · [R1-2608402](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2608402.zip)

**Agreement** · `9.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#126bis:9.1.1:004` · 🆕 신규 · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

구현 영향: 처리 시간·CPU, UE capability·FG

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> For CSI feedback via two-sided model, for inference only, reuse the legacy R19 APU and CPU framework considering
> - Dedicated AI/ML PU (  or ) and/or legacy CPU () are occupied and the occupation is upto UE capability
>   - UE report  0 or  as capability
>   - UE report  0 or  as capability where  or .
>   - The same occupation duration is reused for  and
>   - Note: Combination of = 0 and =0 is not allowed
>   - Note:  and  are separately signalled per CC and across all CCs

출처: [Chair notes RAN1#126bis_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom1.docx) · [R1-2608403](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2608403.zip)

**Agreement** · `9.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#126bis:9.1.1:005` · 🆕 신규 · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

구현 영향: 처리 시간·CPU, UE capability·FG, 포트·자원·레이어 수

> For CSI feedback via two-sided model, for inference only, support CSI processing timeline {Z+t’, Z’+t’} where t’ is reported as UE capability.
> - If <=32 ports, {Z, Z’} is equal to {Z2, Z2’} in table 5.4-2 of TS38.214
> - If >32 ports, {Z, Z’} is equal to {Z2, Z2’} or {Z2, Z2} according to UE capability 1 or 2, and {Z2, Z2’} is in table 5.4-2 of TS38.214
> - FFS the same t’ is reported for <=32 ports and >32 ports in UE feature session
> - Note: t’ is reported per SCS

FFS 1줄

출처: [Chair notes RAN1#126bis_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom1.docx) · [R1-2608403](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Docs/R1-2608403.zip)

**Conclusion** · `9.1.2` Inter-vendor training collaboration for two-sided AI/ML models · `RAN1#126bis:9.1.2:001` · 🆕 신규 · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> For Option 4-1 under Direction A in AI/ML based CSI compression, there is no consensus to support additional CSI feedback metadata to indicate when specific scalability option is used in model design (e.g. truncation/masking) is used as CSI feedback payload scalability option.

출처: [Chair notes RAN1#126bis_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom1.docx)

**Agreement** · `9.1.2` Inter-vendor training collaboration for two-sided AI/ML models · `RAN1#126bis:9.1.2:002` · 🆕 신규 · 규격 작업 (WI)

> Regarding RAN2 LS R1-2606975 (R2-2605892), the draft LS R1-2608708 is endorsed after making the following changes in red.
> For Q1, theThe number of pairing ID values fully standardized reference models for Direction C is out of RAN1 scope.  [RAN1 is discussing on pairing related aspects for a model based on Direction C and Direction A.]
> The final LS in R1-2608709 is endorsed.

출처: [Chair notes RAN1#126bis_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom1.docx)

**Agreement** · `9.1.2` Inter-vendor training collaboration for two-sided AI/ML models · `RAN1#126bis:9.1.2:003` · 🆕 신규 · 규격 작업 (WI)

> - For model applicability procedure for inference, supports Option A and option B.
>   - FFS: Corresponding inference related parameters for option B in otherConfig

FFS 1줄

출처: [Chair notes RAN1#126bis_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom1.docx)

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126bis:10.5.3.1:009` · 🆕 신규 · 관련 주제: CSI 보고/codebook · Study

> For the study of time-domain CSI prediction at UE side in 6GR, among UE-side prediction schemes, consider N4=1 as the baseline for evaluation, where N4 is the number of time occasions in the prediction window.

출처: [Chair notes RAN1#126bis_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom1.docx) · `[126bis-R20-6GR-Aspects of DL based CSI acquisition]`

## RAN1#126 — 10건

**Agreement** · `8.1` Maintenance on AI/ML for NR Air interface, NR MIMO Phase 5,  NES and NTN for NR and IoT · `RAN1#126:8.1:002` · 관련 주제: SRS, CSI 보고/codebook · 유지보수 (CR)

구현 영향: 측정·보고량 · 규격: TS 38.214 5.2.3

> The following TP for TS 38.214 Clause 5.2.3 is endorsed.
> The corresponding CR for Rel-19, TS 38.214 in R1-2606870 is endorsed.
> | Reason for change | Clause 5.2.3 of TS38.214 explicitly identifies the reportQuantity values for which CSI feedback consists of a single part. Rel-19 AI/ML introduced new report quantities for AI/ML-based CSI report for inference and performance monitoring. But these new quantity values remain unspecified in terms of whether support single part CSI. As a result, it is currently unclear whether AI/ML-based CSI reports support single CSI part. |
> | Summary of change | Adding Rel-19 AI/ML reportQuantity values to clarify that CSI reports for AI/ML support single CSI part. |
> | Consequences if not approved | Ambiguity occurs on whether Rel-19 AI/ML CSI reports support single CSI part or two-part CSI reporting. |
> | 5.2.3 CSI reporting using PUSCH ============================= unchanged parts are omitted ============================ When the higher layer parameter reportQuantity is configured with one of the values 'cri-RSRP', 'ssb-Index-RSRP', 'cri-SINR' or 'ssb-Index-SINR', or 'cri-RSRP-Index', 'ssb-Index-RSRP-Index', 'cri-SINR-Index', 'ssb-Index-SINR-Index', 'tdcp', 'cli-RSSI', 'cli-SRS-RSRP', 'cjtc-Dd', 'cjtc-F', 'cjtc-Dd-F', 'cjtc-P', 'p-CRI-r19', 'p-CRI-RSRP-r19', 'p-SSB-Index-r19', 'p-SSB-Index-RSRP-r19', 'rs-pai-r19', 'csi-pai-r19', the CSI feedback consists of a single part. ============================= unchanged parts are omitted ============================ |

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606794](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606794.zip) · `[126-R19-AI 8.1]`

**Agreement** · `9.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#126:9.1.1:001` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> Send LS to RAN2 to study, and if deemed feasible, specify L3 signaling for performance monitoring, including the following aspects
> - Reporting of pair-wise of target CSI sample and the corresponding CSI feedback sample of the corresponding inference report
> - Full and partial target CSI reporting is allowed, where partial target CSI = subset of subbands / layers of the CSI feedback of the inference report)
> - Same set of layers are considered for target CSI sample and CSI feedback sample.
> - Mechanism to collect multiple samples
> - Sample is a pair of target CSI and CSI feedback sample
> - Linking to corresponding inference configuration (detailed solution upto RAN2)

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606361](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606361.zip)

**Agreement** · `9.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#126:9.1.1:002` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> Support L1 signaling for performance monitoring, down-selection from the following alternatives:
> - Alt1: NW side monitoring via legacy eType II format with potential spec impact
> - Alt2: NW side monitoring via partial / full target CSI reporting via same format as NW data collection
> - Alt3: UE assisted monitoring via SGCS / monitoring output reporting
> - Alt 4: NW side monitoring via legacy eType II without spec impact
> - Note: From RAN1 point of view, monitoring based on L3 signalling and L1 signalling are independently considered.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606361](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606361.zip)

**Agreement** · `9.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#126:9.1.1:003` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> The following text for Draft LS in R1-2606881 is endorsed.
> Regarding performance monitoring, RAN1 has the following agreement on using L3 signaling to collect pair-wise of target CSI sample and CSI feedback sample.
> | Agreement: Send LS to RAN2 to study, and if deemed feasible, specify L3 signaling for performance monitoring, including the following aspects Reporting of pair-wise of target CSI sample and the corresponding CSI feedback sample of the corresponding inference report Full and partial target CSI reporting is allowed, where partial target CSI = subset of subbands / layers of the CSI feedback of the inference report) Same set of layers are considered for target CSI sample and CSI feedback sample. Mechanism to collect multiple samples Sample is a pair of target CSI and CSI feedback sample Linking to corresponding inference configuration (detailed solution upto RAN2) |
> RAN1 asks RAN2 if they would be so kind as to consider the agreement above in their future work.
> The corresponding final LS in R1-2606893 is endorsed.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606362](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606362.zip)

**Agreement** · `9.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#126:9.1.1:004` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

구현 영향: 측정·보고량

> Support following configuration for inference configuration
> - Pairing ID
> - Subband configuration (reuse csi-ReportingBand)
> - Resources for channel and interference measurement (reuse legacy configuration)
> - portMappingMethod (reuse legacy configuraiton)
> - codebookConfig-r20
> - Payload parameter combination configuration
> - N1, N2 configuration
> - Rank restriction (reuse legacy)
> - FFS: reportQuantity

FFS 1줄

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606362](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606362.zip)

**Agreement** · `9.1.2` Inter-vendor training collaboration for two-sided AI/ML models · `RAN1#126:9.1.2:001` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> For the association between Target CSI and CSI feedback in Option 4-1, support CSI feedback rank as part of each CSI feedback set metadata.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606012](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606012.zip)

**Agreement** · `9.1.2` Inter-vendor training collaboration for two-sided AI/ML models · `RAN1#126:9.1.2:002` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> For Option 4-1, for a CSI feedback set associated with the -th Target CSI set andthe m-th payload size configuration,
> - the NMSE value associated with the l-th layer of the s-th CSI feedback sample is defined by
> where  is the generated CSI feedback vector for the l-th layer, the m-th payload size configuration, and the -th Target CSI set corresponding to .  is the floating-point CSI feedback vector for the same l-th layer, the same m-th payload size configuration, and the same -th Target CSI set provided in the exchanged dataset.
> The average NMSE and X-percentile of NMSE are derived based on the  .

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606012](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606012.zip)

**Agreement** · `9.1.2` Inter-vendor training collaboration for two-sided AI/ML models · `RAN1#126:9.1.2:003` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> For Option 4-1 under Direction A in AI/ML based CSI compression, for the format of the NMSE and SGCS performance target, use the 32-bit floating point representation.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606012](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606012.zip)

**Agreement** · `9.1.2` Inter-vendor training collaboration for two-sided AI/ML models · `RAN1#126:9.1.2:004` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> For Direction A, Option 3a-1, combination(s) of the configuration parameters to which the exchanged model parameters apply are provided along with the model parameters. These configuration parameters include:
> - The port number configuration of N1 and N2, subband size and BWP info (NR ARFCN of the lowest PRB of the BWP and BWP size and the SCS),
> - CSI payload size configuration per layer
> - Subband configuration
> - Rank
> Note: The port mapping method is separately discussed for both Option 3a-1 and Option 4-1 whether to be applied to either or both or none of them.

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · [R1-2606012](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Docs/R1-2606012.zip)

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#126:10.5.3.1:009` · 관련 주제: CSI 보고/codebook · Study

> For the study of non-AI/AI based CSI prediction in frequency/spatial/time domain at UE or NW side, adopt the templates in the following documents for collecting companies’ results.
> - LLS: [10.5.3.1] CSI prediction simulation result collection template _LLS_v1_Mod.xlsx in R1-2605468
> - SLS: [10.5.3.1] CSI prediction simulation result collection template _SLS_v1_Mod.xlsx in R1-2605468
> Email discussion for collecting companies’ results. Setp. 23, Oct. 8

출처: [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Aspects of DL based CSI acquisition]`

## RAN1#125 — 13건

**Agreement** · `9.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#125:9.1.1:001` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> For quantization of target CSI for NW side data collection, support amplitude and phase quantization with 3-bit for amplitude and 4-bit for phase for each complex number of the target CSI.
> - Reuse eType II amplitude quantization table.
> - Reuse eType II phase quantization table
> - Support normalization Alt2-1:
> - At least one element among the elements in the per-layer and per-subband target precoding matrix correspond to the strongest value in the amplitude quantization levels.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2604677](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2604677.zip)

**Agreement** · `9.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#125:9.1.1:002` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

구현 영향: 메모리·복잡도

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> Decide the necessity of target CSI restriction in RAN1 #126 considering the following cases:
> - Case A: No restriction on target CSI , NW further filter out the unwanted beams on the reconstructed CSI  such that , where  and
> - Case B: Target CSI restriction is applied on  unwanted beams such that , NW further filter out the unwanted beams on the reconstructed CSI  such that , where  and
> Metric: Investigate the resultant spectral efficiency or throughput of the two cases.
> Note1: Models in both cases are trained without considering target CSI restriction as baseline. Companies to report if target CSI restriction is assumed in training for Case B.
> Note2: Consider  as baseline (other values are not precluded) and different unwanted beams can be assumed for different samples (upto companies to report how to determine the unwanted beams for each sample)
> Note3: non-oversampling beams are considered.
> Note4: Companies to report UE side complexity analysis for both cases.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2604677](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2604677.zip)

**Agreement** · `9.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#125:9.1.1:003` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> In NW data collection, UE reports target CSI according to the configured rank by the NW.
> - FFS whether when the rank observed by UE is different from the configured rank, UE can report its suggested rank per reported target CSI sample
> - FFS whether define data logging event
> - FFS whether UE report data quality indicator and its type
> - Note: Companies are encouraged to justify the usefulness of the above suggested rank, data logging event or data quality indicator via evaluations.

FFS 3줄

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2604678](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2604678.zip)

**Agreement** · `9.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#125:9.1.1:004` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

구현 영향: 포트·자원·레이어 수

> Support following configuration for candidate UE data collection
> - Pairing ID
>   - FFS:  whether it is optional or mandatory
> - Resources for channel and interference measurement
>   - Optional parameter
> - Port configuration including n1-n2 and port mapping method (for > 32 ports)
>   - If <=32 ports, configure N1-N2 from table 5.2.2.2.1-2 of TS38.214
>   - If > 32 ports, configure N1-N2 from table 5.2.2.2.5a-1 of TS38.214, and configure port mapping method
>   - Optional parameter
> - Subband configuration (i.e., csi-ReportingBand)
>   - Optional parameter

FFS 1줄

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2604679](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2604679.zip)

**Agreement** · `9.1.2` Inter-vendor training collaboration for two-sided AI/ML models · `RAN1#125:9.1.2:001` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> For Option 4-1 under Direction A in AI/ML based CSI compression, for CSI feedback type and format, supports:
> - The exchanged CSI feedback is the latent message before quantization represented using floating format, e.g., float 32.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2603839](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2603839.zip)

**Agreement** · `9.1.2` Inter-vendor training collaboration for two-sided AI/ML models · `RAN1#125:9.1.2:002` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

구현 영향: 포트·자원·레이어 수

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> For Option 4-1 under Direction A in AI/ML based CSI compression, when the target CSI is precoding matrix with port-subband domain representation and the target CSI set k is associated with  set of CSI feedback set,
> - The number of layers in the CSI feedback set is <= the number of layers in the target CSI set.
> - Note: This does not mean network side data collection is rank agnostic. Data quality for network side data collection is a separate discussion.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2603839](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2603839.zip)

**Agreement** · `9.1.2` Inter-vendor training collaboration for two-sided AI/ML models · `RAN1#125:9.1.2:003` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> For Option 4-1, for a CSI feedback set associated with the -th Target CSI set andthe m-th payload size configuration, and a given subband configuration including N subbands,
> - the SGCS value associated with the l-th layer of the s-th CSI feedback sample is defined by
> where  is the reconstructed precoding vector for the l-th layer, the m-th payload size configuration, and the n-th subband, corresponding to  , and  is the precoder represented by the s-th Target CSI sample of the k-th Target CSI set for the same l-th layer and the n-th subband.
> The average SGCS and X-percentile of SGCS are derived based on the .

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2603839](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2603839.zip)

**Agreement** · `9.1.2` Inter-vendor training collaboration for two-sided AI/ML models · `RAN1#125:9.1.2:004` · 규격 작업 (WI)

> Draft LS response in R1-2605088, is endorsed with the following changes in red, and updating the fields in heading for “to: SA5”, and “CC: RAN2/RAN3”.
> | Regarding “Are there any requirements or assumptions related to scenarios where a gNB generates multiple datasets (e.g. impact on pairing ID association or reuse)”, and “Additionally, once a dataset is generated and transferred to the UE-side training entity, what is the expected behaviour of the pairing ID if the dataset is updated (e.g. unchanged, replaced, or re-assigned)?”, for the above questions, “Based on RAN1 agreements, a different pairing ID shall be assigned to each of the dataset, including the updated dataset. If the dataset is updated, the updated dataset is considered as a separate dataset from RAN1 perspective. “ |
> The corresponding final LS in R1-2605089 is endorsed.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2603840](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2603840.zip)

**Agreement** · `9.1.2` Inter-vendor training collaboration for two-sided AI/ML models · `RAN1#125:9.1.2:005` · 규격 작업 (WI)

> Draft LS response in R1-2605099, is endorsed with the following changes in red, and updating the fields in heading for “to: RAN2”, CC: -”.
> | Regarding “Q3: Besides the pairing ID, what other parameters are necessary in the candidate UE-side data collection configuration?”, RAN1 has the following agreement. On With respect to Q1 and Q2, RAN1 is currently discussing related aspects will reply once RAN1 reach agreement. |
> The corresponding final LS in R1-2605100 is endorsed.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · [R1-2603840](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Docs/R1-2603840.zip)

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#125:10.5.3.1:001` · 관련 주제: CSI 보고/codebook, CSI-RS · Study

구현 영향: 측정·보고량

> For the study of non-AI/AI based CSI prediction in frequency/spatial domain at UE side, consider the following aspects
> - Prediction input (UE side Input): reduced CSI-RS measurement
> - Additional information to be used by UE side for CSI prediction, if applicable
>   - Option 1: Long-term channel information derived from full-dimensional CSI-RS measurement
>   - Option 2: Reconstruction information (indicated by BS) applied on the measured channel based on non-precoded CSI-RS,
>   - Option 3: Reconstruction information based on precoded CSI-RS (indicated by BS), e.g., precoder applied on CSI-RS
>   - Option 4: DMRS based CSI measurement
>   - Other options or combination of above options are not precluded
>   - Companies are encouraged to study whether there is performance impact caused by aging/temporary unavailability of the additional information
> - Prediction output (UE side Output): Predicted CSI to be used for CSI report
>   - Note: UE side Output does not necessarily equal the CSI report quantity
>   - Companies to report the details of the predicted CSI for CSI report

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#125:10.5.3.1:007` · 관련 주제: CSI 보고/codebook, CSI-RS · Study

> For the study of non-AI/AI based CSI prediction in frequency/spatial domain at NW side, consider the following aspects
> - Prediction input:
>   - Option 1-1: UE reported channel matrix derived from reduced dimension CSI-RS measurement
>   - Option 1-2: UE reported coefficient matrix, which is based on the multiplication of a downloaded matrix and the channel matrix derived from reduced dimension CSI-RS measurement
>   - Option 1-3: UE reported precoding matrix derived from reduced dimension CSI-RS measurement
>   - Option 1-4: UE reported coefficient matrix, which is based on the multiplication of a downloaded matrix and the precoding matrix derived from reduced dimension CSI-RS measurement
>   - Other options are not precluded
>   - Note: Performance impact caused by quantization of the UE reported CSI is part of the study
> - Additional information to be used by NW side for CSI prediction, if applicable
>   - Option 2-1: Long-term channel information corresponding to full dimension CSI reported by UE
>   - Option 2-2: Channel information corresponding to full dimension CSI derived from UL measurement
>   - Option 2-3: Channel measurement based on DL DMRS reported by UE
>   - For spatial domain, “dimension” is defined in terms of ports
>   - For frequency domain, companies to report the assumed granularity to define “full dimension”
> - Prediction output: Full-dimension CSI to be used by BS
>   - Note: companies are encouraged to report the details of the full-dimension CSI
> - Note: companies to report the assumption of rank and MCS determination in the simulation

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#125:10.5.3.1:010` · 관련 주제: CSI 보고/codebook, CSI-RS · Study

구현 영향: 포트·자원·레이어 수

> For the study of non-AI/AI based CSI prediction in time domain at UE side, consider the following aspects
> - Prediction input: RS measurement from one or multiple occasions in the observation window
>   - The RS includes at least CSI-RSs
>   - Study the impact of RS with longer periodicity (e.g., 10ms, 20ms, for evaluation), and potential solutions, if needed
> - Study whether additional information is beneficial for UE side time domain CSI prediction, e.g., DMRS based measurement, IMR
> - Prediction output: CSI in the prediction window to be reported by UE
>   - The CSI includes at least channel prediction, study whether/how to enable interference prediction
>   - Study whether to support both N4=1 and N4>1 in the prediction window, and associated UE reporting mechanism
>     - The definition of N4 is same as NR
> - NR Rel-18/Rel-19 UE side CSI prediction as a start point
>   - Study the extension to >32 ports
> - Note: At least for CSI prediction without interference prediction, UE side time domain CSI prediction is to be compared with NW side time domain CSI prediction

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#125:10.5.3.1:016` · 관련 주제: SRS, Beam management, CSI 보고/codebook, CSI-RS · Study

구현 영향: 메모리·복잡도, 측정·보고량

> For the study on channel property information (CPI), the evaluation at least considering the following:
> Category of use cases:
> - CSI configuration/report adaptation for overhead/complexity reduction, CSI feedback with more accuracy, and/or CSI prediction
> - Reference signal configuration adaptation (e.g., CSI-RS for CSI, DMRS, SRS)
> - DL/UL transmission scheduling and configuration (e.g., coordinated beamforming/scheduling for inter-TRP/cell/user interference suppression)
> - Note: the above categories can be applicable to sTRP/mTRP.
> Basic categories of channel properties
> - Spatial-domain (SD)
> - Frequency-domain (FD)
> - Time-domain (TD)
> - Any combination of the above domains
> Measurement definition and/or reporting formats, for example:
> - Correlation information (e.g., time-/frequency/spatial-domain correlation)
> - Spectrum (e.g., channel statistics in a transform domain, basis indices and power)
> - Channel covariance matrix
> - Explicit channel matrix
> - Explicit system parameters (e.g. codebook parameters, RS parameters)
> - Other formats are not precluded.
> Note: Strive for common report quantities for use cases, if applicable.
> Note: The related testability issue is up to RAN 4.
> Note: LS to RAN 4 is to be considered for RAN 4 testability issues, when mature.

출처: [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of DL based CSI acquisition]`

## RAN1#124bis — 16건

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#124bis:8.1:001` · 관련 주제: CSI 보고/codebook · 유지보수 (CR)

규격: TS 38.212 6.3.1.1.2

> The following TP for TS 38.212 Clause 6.3.1.1.2 is endorsed.
> The corresponding final CR for Rel-19 TS 38.212 in R1-2603378 is endorsed
> Reason for change: For P/SP CSI reporting on PUCCH for performance monitoring, it is possible that the number of information bits of RS-PAI becomes less than 3 bits. However, NR specifications do not support PUCCH carrying 1 or 2 information bits other than HARQ-ACK/SR.
> Summary of change: For P/SP CSI reporting on PUCCH for performance monitoring, the number of information bits of related CSI is zero padded to 3 bits.
> Consequences if not approved: For P/SP CSI reporting on PUCCH for performance monitoring, 1-bit or 2-bit payload size of RS-PAI is not supported.
> | 6.3.1.1.2 CSI only <omitted texts> If none of the CSI reports for transmission on a PUCCH is of two parts, the CSI fields of all CSI reports, in the order from upper part to lower part in Table 6.3.1.1.2-12, are mapped to the UCI bit sequence starting with . The most significant bit of each field is mapped to the lowest order information bit for that field, e.g. the most significant bit of the first field is mapped to. If the length of UCI bit sequence is less than 3 bits, zeros shall be appended to the UCI bit sequence until its length equals 3. Table 6.3.1.1.2-12: Mapping order of CSI reports to UCI bit sequence , without two-part CSI report(s) <omitted texts> |

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2603260](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603260.zip) · `[124b-R19-AI/ML]`

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#124bis:8.1:002` · 관련 주제: Beam management, CSI 보고/codebook, CSI-RS · 유지보수 (CR)

구현 영향: 처리 시간·CPU, 측정·보고량 · 규격: TS 38.214 5.2.1.6

> The following TP for TS 38.214 Clause 5.2.1.6 is endorsed.
> The corresponding final CR for Rel-19 TS 38.214 in R1-2603379 is endorsed
> Reason for change: CPU duration for beam management related UE-side data collection is not captured correctly. In current specification, periodic CSI report for UE-side data collection for beam management is not supported.
> | Agreement For UE-sided model, regarding the resource type for data collection purpose, only always-on SSB and P/SP CSI-RS are supported. Agreement For UE-sided model, regarding a CSI-ReportConfig for data collection, Reuse the existing CPU occupation time for a CSI report with CSI-ReportConfig with reportQuantity set to 'none' and TRS-info not configured |
> Summary of change: Reflect the RAN1 agreements accurately in Section 5.2.1.6 of TS 38.214. Include periodic CSI report for UE-side data collection for beam management.
> Consequence if not approved: Incorrect UE behaviour for CPU duration for UE-side data collection for training.
> | 5.2.1.6 CSI processing criteria < Unchanged parts are omitted > For a CSI report with CSI-ReportConfig with higher layer parameter reportQuantity set to 'none' and CSI-RS-ResourceSet with higher layer parameter trs-Info not configured, or reportQuantity set to 'none-bm-r19', the CPU(s) are occupied for a number of OFDM symbols as follows: - A semi-persistent CSI report (excluding an initial semi-persistent CSI report on PUSCH after the PDCCH triggering the report) occupies CPU(s) from the first symbol of the earliest one of each transmission occasion of periodic or semi-persistent CSI-RS/SSB resource for channel measurement for L1-RSRP computation, until symbols after the last symbol of the latest one of the CSI-RS/SSB resource for channel measurement for L1-RSRP computation in each transmission occasion. - An aperiodic CSI report occupies CPU(s) from the first symbol after the PDCCH triggering the CSI report until the last symbol between symbols after the first symbol after the PDCCH triggering the CSI report and symbols after the last symbol of the latest one of each CSI-RS/SSB resource for channel measurement for L1-RSRP computation. For a CSI report with CSI-ReportConfig with higher layer parameter reportQuantity set to 'none-csi-r19', the CPU(s) are occupied for a number of OFDM symbols as follows: - CSI report occupies CPU(s) from the first symbol of each transmission occasion of periodic or semi-persistent CSI-RS resource for channel measurement, until symbols after the transmission occasion of periodic or semi-persistent CSI-RS resource for channel measurement. where are defined in the table 5.4-2. For a CSI report with CSI-ReportConfig with higher layer parameter reportQuantity set to 'none-bm-r19', the CPU(s) are occupied for a number of OFDM symbols as follows: - CSI report occupies CPU(s) from the first symbol of the earliest one of each transmission occasion of periodic or semi-persistent CSI-RS/SSB resource for channel measurement for L1-RSRP computation, until symbols after the last symbol of the latest one of the CSI-RS/SSB resource for channel measurement for L1-RSRP computation in each transmission occasion. where are defined in the table 5.4-2. < Unchanged parts are omitted > |

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2603260](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603260.zip) · `[124b-R19-AI/ML]`

**Conclusion** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#124bis:8.1:003` · 관련 주제: CSI 보고/codebook, CSI-RS · 유지보수 (CR)

> There is no RAN1 consensus on the following:
> - For virtual resource blocks mapping of PDSCH in TS38.211, rate matching of the resource elements in the corresponding physical resource blocks are not performed around the NZP CSI-RS only configured in Set A for CSI report for inference.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2603260](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2603260.zip) · `[124b-R19-AI/ML]`

**Agreement** · `9.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#124bis:9.1.1:001` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> For the standardized SQ codebook when NW does not exchange a codebook, support [1/8, 3/8, 5/8, 7/8] for Q=2 and [1/4, 3/4] for Q=1.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx)

**Agreement** · `9.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#124bis:9.1.1:002` · 규격 작업 (WI)

구현 영향: 포트·자원·레이어 수

> For precoding matrix feedback via two-sided model, support upto 128 ports, upto rank 4 and upto 19 subbands.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx)

**Agreement** · `9.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#124bis:9.1.1:003` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

구현 영향: 측정·보고량

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> Support two-part UCI for CSI feedback via two-sided model, where
> - UCI part 1 contains CQI, RI and CRI
> - UCI part 2 contains the PMI (i.e., CSI feedback of all layers).
> - Layer 1 to  are mapped to Group 1, Layer  to layer  are mapped to Group 2
> - Note: The bits sequence is mapped based on their indices inside each layer, followed by the bit sequence of the next layer. The layers are ordered from the strongest to the weakest.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx)

**Agreement** · `9.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#124bis:9.1.1:004` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> For NW side data collection, support target CSI quantization
> - Down-selection between 1a (real-imaginary) and 1b (amplitude-phase), i.e., {1a-33, 1b-34}.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx)

**Agreement** · `9.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#124bis:9.1.1:005` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

구현 영향: 측정·보고량

> For performance monitoring:
> - Support using paired CSI feedback and target CSI samples for performance monitoring, and further investigate the feasibility of following options and downselect one,
>   - Option 1: Support using L3 signaling framework to collect target CSI samples.
>     - Companies to report details about how to associate target CSI sample with CSI feedback sample.
>   - Option 2: Support using L1 signalling, considering
>   - UE assisted monitoring
>   - CSI reporting via L1 signaling with legacy PMI codebook
>   - CSI reporting using L1 signaling with high resolution quantization of partial target CSI

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx)

**Agreement** · `9.1.2` Inter-vendor training collaboration for two-sided AI/ML models · `RAN1#124bis:9.1.2:001` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

구현 영향: 포트·자원·레이어 수

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> For Option 4-1 under Direction A in AI/ML based CSI compression, when the target CSI is precoding matrix with port-subband domain representation and the target CSI set k is associated with  set of CSI feedback set
> - Support per-layer CSI feedback payload parameter pair
>   - For layer 1/2/3, support {32, 2}, {64, 2}, {96,2}, {128, 2}, {192, 2}, {32,1}
>   - For layer 4, support {32, 2}, {64, 2}, {96,2}, {32,1}
>   - FFS: The number of layers in the CSI feedback set is <= the number of layers in the target CSI set.
> - Note: NW may only exchange a subset of the CSI feedback payload from the list.

FFS 1줄

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx)

**Agreement** · `9.1.2` Inter-vendor training collaboration for two-sided AI/ML models · `RAN1#124bis:9.1.2:002` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> For Option 4-1 under Direction A in AI/ML based CSI compression, the performance targets are exchanged per layer  per CSI feedback set (), where the CSI feedback set () is the mth out of Mk CSI feedbacks set corresponding to the kth target CSI set.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx)

**Agreement** · `9.1.2` Inter-vendor training collaboration for two-sided AI/ML models · `RAN1#124bis:9.1.2:003` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> For Option 4-1 under Direction A in AI/ML based CSI compression,
> - One-to-one mapping between pairing ID and exchanged dataset. There is no linkage between different data sets.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · [R1-2602692](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Docs/R1-2602692.zip)

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#124bis:10.5.3.1:003` · 관련 주제: CSI 보고/codebook, CSI-RS · Study

> For spatial domain CSI prediction, Baseline #2 is Linear interpolation, where the channel of an unmeasured port uses the channel of the nearest measured ports based on CSI-RS port indexing (for evaluation purpose, 5G NR port indexing is assumed) in the same polarization, without using assistance information derived from full-dimensional measurement.
> - Companies to report remaining details if any, including other baselines

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#124bis:10.5.3.1:009` · 관련 주제: CSI 보고/codebook, CSI-RS · Study

구현 영향: 메모리·복잡도, 측정·보고량

> For the study of non-AI/AI based time domain CSI prediction at UE or NW side, consider
> - Intermediate metric: Subband-level per layer per predicted time instance eigenvector/precoder SGCS, NMSE calculated between predicted channel and ground-truth channel
>   - To compare NW side prediction with UE side prediction, the impact of CSI reporting shall be considered
>   - FFS WB SGCS/NMSE
> - System-level metric: UPT (mean, 5%tile), CSI reporting overhead
>   - CSI-RS overhead is considered in UPT calculation
>   - To evaluate CSI report overhead, companies to report how the PMI/channel of the predicted time instance(s) is reported
> - Link-level metric: BLER/SE/throughput
> - Complexity metrics: FLOPs/M
>   - For AI based prediction: number of parameters/M
> - Baseline: Sample & Hold
> - Additional EVM assumption
>   - Channel modelling: Spatial consistency with mobility procedure A
>   - UE distribution: 100% outdoors with speed 10, 20, 30, 60, 120km/h
>     - Other speeds are not precluded
>   - UE Rx antenna phase discontinuity modelling: Companies to report the used model
>   - Observation window (number/distance between adjacent CSI-RS occasions): e.g., 5/10ms, 5/20ms for periodic CSI-RS; and 12/2ms, 8/2ms, 4/2ms for aperiodic CSI-RS;
>     - other values can be additionally submitted
>   - Prediction window (number/length of each predicted instances/gap from the last observation instance to the 1st predicted instance):  e.g., 1/10ms/5ms, 4/10ms/5ms;
>     - other values can be additionally submitted.

FFS 1줄

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#124bis:10.5.3.1:010` · 관련 주제: CSI 보고/codebook · Study

구현 영향: 측정·보고량

> For the study on JSCM-based CSI compression, at least considering the following aspects on top of previous agreement for AI-based CSI compression:
> - Performance of Projection-matrix-based compression (compress target CSI by multiplying with a projection matrix at UE) or encoder-based (e.g., transformer-based), and reconstruct the CSI at NW with a NW-sided model
>   - Companies to report method for obtaining projection matrix/encoder
>   - Companies to report non-AI/ML operations (if any) before/after multiplying with a projection matrix.
> - Study the potential RF related impact (e.g., PAPR) and potential solutionsat least including
>   - Map the output to certain discrete constellation with, at least considering
>     - NR modulation constellations, e.g., 16QAM, 64QAM, 256QAM, 1024QAM
>     - Other modulation constellations, e.g., 64APSK, other customized (fixed) constellations
>   - Map/restrict the output, e.g., with restricted amplitude(s)
>   - PAPR restriction during training as part of loss function
>   - Note: the above operation is fixed/known by NW
> - Both precoding matrix and explicit H can be considered as the target CSI for inference
> - For performance evaluation related to error detection,
>   - For benchmark of SSCC and eType II/Type I, when CSI error is detected, previous CSI is adopted to derive the precoder for downlink transmission
>   - For JSCM, details of error detection, if any, companies report the assumption in the evaluation
> - Study on generalization and scalability performance
> - Study on LCM for JSCM-based CSI compression
> - Note: Companies to report how to multiplex JSCM-compressed precoding matrix/explicit H with other UCI, e.g., RI or CQI, and/or UL-SCH
> - Note: The related testability issue is up to RAN 4.
> - Note: LS to RAN 4 is to be considered for RAN 4 potential related impacts, e.g., EVM, ACLR, SEM, PAPR, testability, arbitrary constellation, when mature.
> - Note: Companies to report I/Q imbalance assumption, if any

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#124bis:10.5.3.1:013` · 관련 주제: CSI 보고/codebook · Study

> For AI based CSI prediction, evaluate generalization/scalability performances of prediction models at least across one or more of the following scenarios/configurations
> - Various deployment scenarios, e.g., UMa, InH
> - Various carrier frequencies
> - Various indoor/outdoor distributions
> - Various BS antenna configurations, e.g., antenna spacing, antenna virtualization/TxRU mapping, antenna port layouts, antenna port numbers
> - Various sampling ratios and/or sampling patterns
> - Various UE side parameters, e.g., UE speeds, SNR/SINR, UE channel estimation errors, UE antenna configurations
> - Various report resolution
> - Companies are encouraged to evaluate generalization/scalability performance across multiple scenario/configuration combinations.
> - The above is at least applicable to frequency/spatial/time domain prediction. FFS other sub-use case specific generalization aspects, if any

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#124bis:10.5.3.1:016` · 관련 주제: SRS, CSI 보고/codebook · Study

구현 영향: 메모리·복잡도, 측정·보고량

> For the study on channel property information (CPI), at least the following is considered.
> - Potential use cases, e.g., assisting RS configuration; assisting CSI report configuration; assisting scheduling coordination at spatial domain; how to be used for event/condition definition for event-triggered CSI computation and reporting; determining CSI report; assisting CSI prediction
>   - Note: examples are for the purpose of discussion. Other use cases are not excluded.
>   - Note: assisting SRS based CSI acquisition is to be discussed in 10.5.3.3
> - For each potential use case, studying details of
>   - Benchmark
>   - KPI
>   - Report quantities/updating occasion, and associated time domain computation assumptions, if applicable
>   - measurement RS
>   - UE computation complexity for CPI, and corresponding CSI feedback complexity, if applicable.
> - Note: Strive for common report quantities for use cases, if applicable.
> - Note: The related testability issue is up to RAN 4.
> - Note: LS to RAN 4 is to be considered for RAN 4 testability issues, when mature.

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Aspects of DL based CSI acquisition]`

## RAN1#124 — 21건

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#124:8.1:001` · 관련 주제: Beam management, CSI 보고/codebook, CSI-RS · 유지보수 (CR)

구현 영향: 측정·보고량 · 규격: TS 38.214 5.2.1.4.2

> The following TP for TS 38.214 Clause 5.2.1.4.2 for Rel-19 is endorsed.
> The corresponding final CR for Rel-19, TS 38.214 in R1-2601645 is endorsed.
> Reason for change: There is a bracket related to Set A description. Report quantity name and RRC parameters name are not aligned with the latest TS38.331.
> Summary of change: Remove the bracket related to Set A description and align the report quantity name and RRC parameters name.
> Consequences if not approved: The description related to Set A is unclear.
> | 5.2.1.4.2 Report quantity configurations <omitted texts> If the UE is configured with a CSI-ReportConfig with reportQuantity-r19 set to 'p-cri-r19p-CRI-r19', 'p-cri-RSRP-r19p-CRI-RSRP-r19', 'p-ssb-index-r19p-SSB-Index-r19' or 'p-ssb-index-RSRP-r19p-SSB-Index-RSRP-r19', and with nrofreportedpredictedrs-r19nrofReportedPredictedRS-r19 and/or nroftimeinstance-r19nrofTimeInstance-r19, the following applies: the UE is not required to update measurements for more than 64 CSI-RS or SSB resources given by resourcesForChannelMeasurement,[ and is not expected to predict for more than 64 CSI-RS or SSB resources given by resourcesForSetA-r19]resourcesForChannelPrediction-r19, the UE shall report one of the following in a single report: - nrofreportedpredictedrs-r19nrofReportedPredictedRS-r19 different P-CRIs or P-SSBRIs of the second Resource Setting, if nroftimeinstance-r19nrofTimeInstance-r19 is not configured and reportQuantity-r19 is set to ' p-cri-r19p-CRI-r19' or ' p-ssb-index-r19p-SSB-Index-r19', - nrofreportedpredictedrs-r19nrofReportedPredictedRS-r19 different P-CRIs or P-SSBRIs of the second Resource Setting, with corresponding predicted L1-RSRP(s), if nroftimeinstance-r19nrofTimeInstance-r19 is not configured and reportQuantity-r19 set to ' p-cri-RSRP-r19p-CRI-RSRP-r19' or ' p-ssb-index-RSRP-r19p-SSB-Index-RSRP-r19', - nrofreportedpredictedrs-r19nrofReportedPredictedRS-r19 different P-CRIs or P-SSBRIs of the second Resource Setting for each of nroftimeinstance-r19nrofTimeInstance-r19 time instance(s), if nroftimeinstance-r19nrofTimeInstance-r19 is configured and reportQuantity-r19 set to 'p-cri-r19' or ' p-ssb-index-RSRP-r19p-SSB-Index-RSRP-r19', - nrofreportedpredictedrs-r19nrofReportedPredictedRS-r19 different P-CRIs or P-SSBRIs of the second Resource Setting for each of nroftimeinstance-r19nrofTimeInstance-r19 time instance(s), with corresponding predicted L1-RSRP(s), if nroftimeinstance-r19nrofTimeInstance-r19 is configured and reportQuantity-r19 set to ' p-cri-RSRP-r19p-CRI-RSRP-r19' or ' p-ssb-index-RSRP-r19p-SSB-Index-RSRP-r19'. <omitted texts> |

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2600736](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2600736.zip) · `[124-R19-AI/ML]`

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#124:8.1:002` · 관련 주제: CSI 보고/codebook, CSI-RS · 유지보수 (CR)

구현 영향: 처리 시간·CPU, 측정·보고량 · 규격: TS 38.214 5.2.1.6

> Adopt the following TP for TS 38.214 Clause 5.2.1.6.
> The corresponding final CR for Rel-19, TS 38.214 in R1-2601645 is endorsed.
> Reason for change: The notation of “and/or ” is mistakenly used to describe occupied CPU for CPU occupation time for CSI report for monitoring.
> Summary of change: Adding correct notation of occupied CPU for CPU occupation time for CSI report for monitoring.
> Consequences if not approved: The notation of occupied CPU for CPU occupation time for CSI report for monitoring is incorrect.
> | 5.2.1.6 CSI processing criteria <omitted texts> For a CSI report with CSI-ReportConfig with higher layer parameter reportQuantity not set to 'none', or a CSI report with LTM-CSI-ReportConfig, or reportQuantity not set to 'none-bm-r19' or 'none-csi-r19', the CPU(s) (including and/or , for CSI reports with reportQuantity set to 'p-cri-r19', 'p-cri-RSRP-r19', 'p-ssb-index-r19', or 'p-ssb-index-RSRP-r19', or ‘csi-pai-r19’, or ‘rs-pai-r19’, and CSI reports configured with the higher layer parameter csi-InferencePrediction-r19, and for CSI report with reportQuantity set to ‘rs-pai-r19’ or ‘csi-pai-r19’) are occupied for a number of OFDM symbols as follows: - A periodic or semi-persistent CSI report (excluding an initial semi-persistent CSI report on PUSCH after the PDCCH triggering the report, a semi-persistent CSI report on PUSCH configured with reportQuantity set to 'csi-pai-r19', and a semi-persistent CSI report on PUSCH configured with the higher layer parameter codebookType set to 'typeII-Doppler-r18' or 'typeII-Doppler-PortSelection-r18') occupies CPU(s) from the first symbol of the earliest one of each CSI-RS/CSI-IM/SSB resource, or each CSI-RS/CSI-IM resource associated with all configured sub-configurations for periodic CSI report corresponding to a CSI-ReportConfig that contains a list of sub-configurations provided by csi-ReportSubConfigToAddModList, or each CSI-RS/CSI-IM resource associated with all activated/triggered sub-configurations for semi-persistent CSI report corresponding to a CSI-ReportConfig that contains a list of sub-configurations provided by csi-ReportSubConfigToAddModList, for channel or interference measurement, respective latest CSI-RS/CSI-IM/SSB occasion no later than the corresponding CSI reference resource, until the last symbol of the configured PUSCH/PUCCH carrying the report. <omitted texts> |

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2600736](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2600736.zip) · `[124-R19-AI/ML]`

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#124:8.1:003` · 관련 주제: CSI 보고/codebook, CSI-RS · 유지보수 (CR)

구현 영향: 측정·보고량 · 규격: TS 38.214 5.2.1.4.6

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> Adopt the following TP for TS 38.214 Clause 5.2.1.4.6.
> The corresponding final CR for Rel-19, TS 38.214 in R1-2601635 is endorsed.
> | Reason for change | In current TS 38.214, for CSI-PAI reporting, the non-predicted PMI (ground-truth) is corresponding to the S-th time instance of the report of the first Reporting Setting, based on the CSI-RS resource(s) whose transmission occasion is contained within the same slot of the S-th time instance of the report of the first Reporting Setting (inference report). However, for CSI prediction, the reported predicted PMI refers to the precoder matrix for slot interval(s) rather than for individual slot(s). |
> | Summary of change | Correct the definition of the CSI-RS resource(s) corresponding to the non-predicted PMI. |
> | Consequences if not approved | There is misalignment between the descriptions in CSI-PAI reporting and predicted PMI reporting. |
> | 5.2.1.4.6 CSI-PAI reporting <Unchanged part omitted> - to report CSI-PAI for the second Reporting Setting, the UE is expected to be configured in the second Report Setting with codebookType set to 'typeII-r16' and it shall: determine predicted PMI (see Clause 5.2.2.2.10 or Clause 5.2.2.2.11) for each of the subband(s) configured by csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband for the -th time instance configured by timeinstanceforCSImonitoring-r19 in the second Reporting Setting ( , with >1 provided in the first Reporting Setting), based on the CSI prediction performed by the UE using the channel measurement corresponding to the first Reporting Setting, determine non-predicted PMI for each of the subband(s) configured by csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband, which is corresponding to the -th time instance of the report of the first Reporting Setting, based on the CSI-RS resource(s) whose transmission occasion is contained within the same slot interval of the S-th time instance of the report of the first Reporting Setting in the resource set for channel measurement for the report corresponding to the second Reporting Setting. <Unchanged part omitted> | 5.2.1.4.6 CSI-PAI reporting <Unchanged part omitted> - to report CSI-PAI for the second Reporting Setting, the UE is expected to be configured in the second Report Setting with codebookType set to 'typeII-r16' and it shall: determine predicted PMI (see Clause 5.2.2.2.10 or Clause 5.2.2.2.11) for each of the subband(s) configured by csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband for the -th time instance configured by timeinstanceforCSImonitoring-r19 in the second Reporting Setting ( , with >1 provided in the first Reporting Setting), based on the CSI prediction performed by the UE using the channel measurement corresponding to the first Reporting Setting, determine non-predicted PMI for each of the subband(s) configured by csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband, which is corresponding to the -th time instance of the report of the first Reporting Setting, based on the CSI-RS resource(s) whose transmission occasion is contained within the same slot interval of the S-th time instance of the report of the first Reporting Setting in the resource set for channel measurement for the report corresponding to the second Reporting Setting. <Unchanged part omitted> |

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601565](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601565.zip) · `[124-R19-AI/ML]`

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#124:8.1:004` · 관련 주제: CSI 보고/codebook, CSI-RS · 유지보수 (CR)

구현 영향: 측정·보고량 · 규격: TS 38.214 5.2.1.4.6

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> Adopt the following TP for TS 38.214 Clause 5.2.1.4.6.
> The corresponding final CR for Rel-19, TS 38.214 in R1-2601635 is endorsed.
> | Reason for change | 1. when N4=1, CSI-PAI report is not possible, performance monitoring is not supported; 2. Misalignment between timeinstanceforCSImonitoring-r19 used in TS 38.214 and timeInstanceForCSI-PAI-r19 used in TS 38.331 |
> | Summary of change | 1. Add CSI-PAI report when N4=1; 2. Change timeinstanceforCSImonitoring to timeInstanceForCSI-PAI-r19 |
> | Consequences if not approved | 1. Performance monitoring is not supported for CSI prediction when N4=1; 2. Misaligned parameters for indicating the time instance between TS 38.214 and TS38.331 |
> | 5.2.1.4.6 CSI-PAI reporting <Unchanged part omitted> - to report CSI-PAI for the second Reporting Setting, the UE is expected to be configured in the second Report Setting with codebookType set to 'typeII-r16' and it shall: determine predicted PMI (see Clause 5.2.2.2.10) for each of the subband(s) configured by csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband if 1, or determine predicted PMI (see Clause 5.2.2.2.10 or Clause 5.2.2.2.11) for each of the subband(s) configured by csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband for the -th time instance configured by timeInstanceForCSI-PAI-r19timeinstanceforCSImonitoring-r19 in the second Reporting Setting ( , with >1 provided in the first Reporting Setting), based on the CSI prediction performed by the UE using the channel measurement corresponding to the first Reporting Setting, determine non-predicted PMI for each of the subband(s) configured by csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband, which is corresponding to the time instance of the report of the first Reporting Setting if 1 or the -th time instance of the report of the first Reporting Setting if >1, based on the CSI-RS resource(s) whose transmission occasion is contained within the same slot of the time instance of the report of the first Reporting Setting if 1 or the S-th time instance of the report of the first Reporting Setting if >1 in the resource set for channel measurement for the report corresponding to the second Reporting Setting. <Unchanged part omitted> | 5.2.1.4.6 CSI-PAI reporting <Unchanged part omitted> - to report CSI-PAI for the second Reporting Setting, the UE is expected to be configured in the second Report Setting with codebookType set to 'typeII-r16' and it shall: determine predicted PMI (see Clause 5.2.2.2.10) for each of the subband(s) configured by csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband if 1, or determine predicted PMI (see Clause 5.2.2.2.10 or Clause 5.2.2.2.11) for each of the subband(s) configured by csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband for the -th time instance configured by timeInstanceForCSI-PAI-r19timeinstanceforCSImonitoring-r19 in the second Reporting Setting ( , with >1 provided in the first Reporting Setting), based on the CSI prediction performed by the UE using the channel measurement corresponding to the first Reporting Setting, determine non-predicted PMI for each of the subband(s) configured by csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband, which is corresponding to the time instance of the report of the first Reporting Setting if 1 or the -th time instance of the report of the first Reporting Setting if >1, based on the CSI-RS resource(s) whose transmission occasion is contained within the same slot of the time instance of the report of the first Reporting Setting if 1 or the S-th time instance of the report of the first Reporting Setting if >1 in the resource set for channel measurement for the report corresponding to the second Reporting Setting. <Unchanged part omitted> |

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601565](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601565.zip) · `[124-R19-AI/ML]`

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#124:8.1:005` · 관련 주제: CSI 보고/codebook · 유지보수 (CR)

구현 영향: 처리 시간·CPU · 규격: TS 38.214 5.2.1.6

> Adopt the following TP for TS 38.214 Clause 5.2.1.6.
> The corresponding final CR for Rel-19, TS 38.214 in R1-2601635 is endorsed.
> Reason for change: CPU duration for UE-sided data collection for CSI prediction is not captured correctly.
> Summary of change: Reflect the RAN1 agreements accurately in Section 5.2.1.6 of TS 38.214.

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601565](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601565.zip) · `[124-R19-AI/ML]`

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#124:8.1:006` · 관련 주제: Beam management, CSI 보고/codebook, CSI-RS · 유지보수 (CR)

구현 영향: 처리 시간·CPU, 측정·보고량

> For CSI prediction using UE-side model, for data collection for training,
> - OCPU=1
> the CPU occupancy starts from the first symbol of each P/SP-CSI-RS occasion till Z3’ symbols after the P/SP-CSI-RS occasion.
> Consequence if not approved: Incorrect behaviour for CPU duration.
> | 5.2.1.6 CSI processing criteria < Unchanged parts are omitted > For a CSI report with CSI-ReportConfig with higher layer parameter reportQuantity set to 'none' and CSI-RS-ResourceSet with higher layer parameter trs-Info not configured, or reportQuantity set to 'none-bm-r19', the CPU(s) are occupied for a number of OFDM symbols as follows: - A semi-persistent CSI report (excluding an initial semi-persistent CSI report on PUSCH after the PDCCH triggering the report) occupies CPU(s) from the first symbol of the earliest one of each transmission occasion of periodic or semi-persistent CSI-RS/SSB resource for channel measurement for L1-RSRP computation, until symbols after the last symbol of the latest one of the CSI-RS/SSB resource for channel measurement for L1-RSRP computation in each transmission occasion. - An aperiodic CSI report occupies CPU(s) from the first symbol after the PDCCH triggering the CSI report until the last symbol between symbols after the first symbol after the PDCCH triggering the CSI report and symbols after the last symbol of the latest one of each CSI-RS/SSB resource for channel measurement for L1-RSRP computation. For a CSI report with CSI-ReportConfig with higher layer parameter reportQuantity set to 'none-csi-r19', the CPU(s) are occupied for a number of OFDM symbols as follows: - CSI report occupies CPU(s) from the first symbol of each transmission occasion of periodic or semi-persistent CSI-RS resource for channel measurement, until symbols after the transmission occasion of periodic or semi-persistent CSI-RS resource for channel measurement in each transmission occasion. where are defined in the table 5.4-2. < Unchanged parts are omitted > |

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601565](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601565.zip) · `[124-R19-AI/ML]`

**Conclusion** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#124:8.1:007` · 관련 주제: CSI 보고/codebook, CSI-RS · 유지보수 (CR)

> There is no consensus in RAN1 to further discuss on CMR configuration alignment between CSI-pai report and inference report for CSI prediction.

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601565](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601565.zip) · `[124-R19-AI/ML]`

**Agreement** · `9.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#124:9.1.1:001` · 규격 작업 (WI)

> For precoding matrix feedback via two-sided model, support following payload combination for the payload of 384 bits of rank 1. The layers are reported in the order of decreasing strength.
> | Rank1 | Rank2 | Rank3 | Rank4 |
> | {192, 2} | {192, 2}, {192, 2} | {96, 2}, {96, 2}, {192, 2} | {96, 2}, {96, 2}, {96, 2}, {96, 2} |

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx)

**Agreement** · `9.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#124:9.1.1:002` · 규격 작업 (WI)

구현 영향: UE capability·FG

> For precoding matrix feedback via two-sided model, support following payload combination for the payload of 32/64 bits of rank 1. The layers are reported in the order of decreasing strength.
> | Rank1 | Rank2 | Rank3 | Rank4 |
> | {32, 1} | {32, 1}, {32, 1} | N/A | N/A |
> | {32, 2} | {32, 2}, {32, 2} | {32, 1}, {32, 1}, {32, 2} | {32, 1}, {32, 1}, {32, 1}, {32, 1} |
> Note: UE should report whether or not the UE supports parameter combination or per-layer payload pair {32,1} or Q=1.  Details of the reporting method is to be discussed in corresponding UE feature discussion.

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx)

**Agreement** · `9.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#124:9.1.1:003` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> Down-select up to two options from the following options for target CSI format for NW side data collection at RAN1#124bis.
> - Option 1a-33: real / imaginary part quantization via 3-bit, i.e., k1=k2=3
> - Option 1a-55: real / imaginary part quantization via 5-bit, i.e., k1=k2=5
> - Option 1b-34: amplitude quantization via 3-bit, phase quantization via 4-bit, k1=3, k2=4
> - Option 1b-46: amplitude quantization via 4-bit, phase quantization via 6-bit, k1=4, k2=6
> Note1: SGCS metric 1 is used as the metric, i.e., SGCS between target CSI FL32 and reconstructed CSI inferred by model trained using target CSI of the respective format.
> Note2: Companies should try to optimize the normalization methods to minimize the quantization error, e.g., for each target CSI sample on a subband and a layer, normalized according to the amplitude of the strongest coefficients or real/imaginary part (Alt2-1).
> Note3: If two options are selected  they should belong to the same category (i.e. 1a or 1b).

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601253](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601253.zip)

**Agreement** · `9.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#124:9.1.1:004` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> Support layer-based UCI mapping and omission.
> - FFS the details of layer-grouping to facilitate CSI mapping and omission.
> - Note: Partial omission of layers is not supported.

FFS 1줄

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601253](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601253.zip)

**Agreement** · `9.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#124:9.1.1:005` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> For the evaluation of the target CSI format options for NW side data collection, consider following quantization values:
> - For real / image part quantization of option 1a, consider
> - CB1:  for , j=1, 2
>   - Companies are encouraged to apply different scaling factor for CB1.
> - For amplitude / phase quantization of option 1b, consider
> - Amplitude: Reuse e-Type II quantization tables. Replace the value of reserved codepoints to (1/2)15/4.
> - Phase: uniform distribution, , for

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601254](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601254.zip)

**Conclusion** · `9.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#124:9.1.1:006` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

구현 영향: 측정·보고량

> There is no consensus on determining the actual payload size of the inference report based on UE indications other than RI.

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601254](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601254.zip)

**Conclusion** · `9.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#124:9.1.1:007` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> Configuration of pairing ID in the CSI report for inference is sufficient to distinguish the CSI feedback with two-sided model with other legacy CSI reports.

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601254](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601254.zip)

**Agreement** · `9.1.2` Inter-vendor training collaboration for two-sided AI/ML models · `RAN1#124:9.1.2:001` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> For Option 4-1 under Direction A in AI/ML based CSI compression, for target CSI format, adopt scalar quantization (same format as NW side data collection).
> - FFS: Larger k1 and k2 values can be considered as opposed to NW data collection.

FFS 1줄

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601150](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601150.zip)

**Agreement** · `9.1.2` Inter-vendor training collaboration for two-sided AI/ML models · `RAN1#124:9.1.2:002` · 규격 작업 (WI)

> For model pairing procedure at least for inference, a pairing ID corresponding to Direction C is associated with a fully standardized reference model.

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601150](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601150.zip)

**Agreement** · `9.1.2` Inter-vendor training collaboration for two-sided AI/ML models · `RAN1#124:9.1.2:003` · 규격 작업 (WI)

> For Direction A Option 3a-1, support exchange of single pairing ID along with model parameter exchange corresponding to the standardized reference encoder model structure.

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601151](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601151.zip)

**Conclusion** · `9.1.2` Inter-vendor training collaboration for two-sided AI/ML models · `RAN1#124:9.1.2:004` · 규격 작업 (WI)

> For the signaling discussion of direction A option 3a-1, RAN1 assumes the same model parameter description format for parameter exchange as RAN4 will use to describe the reference model in Direction C.
> Note: RAN1 will not discuss dedicated model parameter description format for option 3a-1.

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601152](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601152.zip)

**Agreement** · `9.1.2` Inter-vendor training collaboration for two-sided AI/ML models · `RAN1#124:9.1.2:005` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

구현 영향: UE capability·FG, 포트·자원·레이어 수

> The draft LS R1-2601717 is endorsed with the following changes and re-arrangement of the paragraph before the table.
> The final LS in R1-2601718 is endorsed.
> Based on the above RAN4 LS, RAN1 will work on the signaling design and parameter set exchange to support Direction A option 3a-1, RAN1 assumes that the RAN4 specified reference model structure(s) will be scalable across different number of Tx ports, and/or different subbands configurations, and/or different CSI payload size configurations.
> RAN1 agreed the following CSI payload size configurations of different {d, Q} for SQ, where d denotes the length of latent message and Q denotes the number of quantization bit(s) per element in the latent message. Support of {32,1} is up to UE capability.

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · [R1-2601152](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Docs/R1-2601152.zip)

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#124:10.5.3.1:002` · 관련 주제: CSI 보고/codebook, CSI-RS · Study

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> Adopt the following table as the assumptions for LLS for DL based CSI acquisition.
> | Parameters | Value |
> | #1 Carrier frequency | Around 700MHz (FDD) Around 2 GHz (FDD) Around 4 GHz (TDD) Around 7 GHz (TDD) |
> | #2 RB allocation for PDSCH | 24RB, 48RB, others are not precluded |
> | #2a Channel BW | Depend on carrier frequency. Companies to report the assumed channel BW. |
> | #3 Waveform and numerology for DL | CP-OFDM, 15 kHz for FDD, 30 kHz for others |
> | #4 Channel model | CDL-A/B/C/D/E in TR 38.901 Possible DS values = {10, 30, 100, 300, 1000} ns. ASA, ASD, ZSA, ZSD follow the values in sec 7.7.1 in TR 38.901 Companies to report how randomization is performed if considered For time domain CSI prediction, companies to report whether CDL or TDL is used. Note: it does not mean it is mandatory for companies to evaluate time domain CSI prediction in LLS If UL transmission is simulated, companies to report the assumption for UL channel model. |
> | #5 UE speed | 3 km/h, 30 km/h, 120km/h, 350km/h, 500km/h |
> | #6 PRG | 2 RBs, 4 RBs as start point for evaluation Other values are not precluded |
> | #7 BS antenna configuration | Reuse the assumption under AI 10.5.2.2 when applicable, otherwise refer to AI 10.1 |
> | #8 UE antenna configuration | Follow agreements in agenda 10.1 |
> | #9 MIMO scheme | SU-MIMO, MU-MIMO. |
> | #10 Receiver type | MMSE-IRC or rML for DL. MMSE-IRC for UL |
> | #11 CW to layer mapping | NR CW to layer mapping (baseline) Other codeword-to-layer mapping options are not precluded |
> | #12 Channel coding | LDPC for PDSCH, Polar for CSI (for evaluation benchmark), when applicable |
> | #13 MCS | For PDSCH: QPSK (1/5, 1/3), 16QAM (2/5, 1/2, 3/4), 64QAM (1/2, 2/3, 5/6), 256QAM (2/3, 5/6) |
> | #14 Channel estimation | Realistic as baseline Companies to report the detailed CSI-RS channel estimation. |
> | #15 Link adaptation | AMC/fixed MCS |
> | #16 KPIs | Intermediate KPIs: SGCS/NMSE BLER, SE/throughput |
> | #17 Other CSI-RS parameters | Specified by proponent, e.g., CDM-group sizes, CDM group layout, PDSCH/CSI-RS multiplexing, etc. |
> | #18 Maximum CSI-RS power boosting | 6dB (cf. R1-103331.FFS other values pending RAN4 feedback) |
> | #19 CSI-RS periodicity | 10, 20 ms |
> | #20 Scheduling delay | Minimum [4ms] from CSI measurement to CSI application Companies to report if other assumptions are used |
> | #21 CSI reception | At least for the CSI feedback without channel coding, e.g. JSCM, JSCC related study: Simulate CSI receiver performance with realistic channel/interference+noise estimation under realistic assumptions. Companies to report the detailed assumptions for UL channel/interference |
> | #22 Phase errors for radios with uncalibrated antennas (for 4 TXRUs) | Wideband phase error between Tx antenna port 0 and Tx antenna port () can be modeled: Independent random phase offset uniformly distributed between 0 and 2π between any two Tx antenna ports. |
> Note: additional necessary evaluation assumptions for CSI feedback without channel coding, e.g. JSCM, JSCC, are to be discussed separately.

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · `[124-R20-6GR-Aspects of DL based CSI acquisition]`

**Agreement** · `10.5.3.1` Aspects of downlink-based CSI acquisition · `RAN1#124:10.5.3.1:003` · 관련 주제: CSI 보고/codebook, CSI-RS · Study

구현 영향: 메모리·복잡도

> To evaluate the performance of non-AI/AI based CSI prediction at UE side or NW side, consider
> - Intermediate metric: Subband/RB-level per layer eigenvector/precoder SGCS, NMSE calculated between predicted channel and ground-truth channel
>   - To compare NW side prediction with UE side prediction, the impact of CSI reporting shall be considered
>   - FFS: other intermediate KPI
> - System-level metric: UPT (mean, 5%tile), CSI reporting overhead
>   - CSI-RS overhead is considered in UPT calculation
>   - Companies to report how to calculate CSI report overhead and CSI report mechanism
> - Link-level metric: BLER/SE/throughput
> - Complexity metrics: FLOPs/M
> - For AI based prediction: number of parameters/M
> - Baseline:
>   - Baseline#1: CSI measurement/report based on full CSI-RS ports/density
>   - Baseline#2:
>     - Sample & Hold for frequency domain, companies to report how Sample & Hold is performed
>     - FFS for spatial domain
> - Other baselines are not precluded
> - Companies to report sampling ratio and sampling pattern
>   - Definition of sampling ratio and sampling pattern subjects to detailed domain for reduction
> - FFS calibration error for BS antenna arrays other than 4TXRUs
> - Companies to report the assumptions for spatial consistency modelling, if applicable
> - The above is at least applicable to frequency/spatial domain prediction. Companies to report other sub-use case specific parameters, if applicable

FFS 3줄

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · `[124-R20-6GR-Aspects of DL based CSI acquisition]`

## RAN1#123 — 17건

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#123:8.1:001` · 관련 주제: CSI 보고/codebook · 유지보수 (CR)

구현 영향: UE capability·FG, 측정·보고량 · 규격: TS 38.214 5.2.1.6, TS 38.214 5.2.5

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> Adopt the following TPs for TS 38.214 Clause 5.2.1.6.
> Reason for change: The release of CPU1 and CPUx for a CSI report not considered within any of  and  is unclear.
> Summary of change: Clarify that the CPU1 and CPUx for a CSI report not considered within any of  and  are not occupied.
> Consequences if not approved: gNB and UE may have different understanding on the release of CPU1 and CPUx for a CSI report not considered within any of  and .
> | TP for TS 38.214 Clause 5.2.1.6 CSI processing criteria <omitted texts> For CSI reports with reportQuantity set to 'p-cri-r19', 'p-cri-RSRP-r19', 'p-ssb-index-r19', or 'p-ssb-index-RSRP-r19', and CSI reports configured with the higher layer parameter csi-InferencePrediction-r19, the UE may indicate a second value for the number of supported simultaneous CSI calculations with parameter SecondValuesSimultaneousCSI-ReportsPerCC in a component carrier, and SecondValuesSimultaneousCSI-ReportsAllCC across all component carriers, and if applicable, a third value for the number of supported simultaneous CSI calculations with parameter ThirdValuesSimultaneousCSI-ReportsPerCC in a component carrier, and ThirdValuesSimultaneousCSI-ReportsAllCC across all component carriers, in addition to . If a UE supports simultaneous CSI calculations it is said to have CSI processing units for processing CSI reports. If CPUs are occupied for calculation of CSI reports in a given OFDM symbol, the UE has unoccupied CPUs. If CSI reports start occupying their respective CPUs on the same OFDM symbol on which CPUs are unoccupied, where each CSI report corresponds to , the UE is not required to update the requested CSI reports with lowest priority (according to Clause 5.2.5), where is the largest value such that holds. If only the second value is indicated, x = 2. If both of the second value and the third value are indicated, x = 2, 3 where the CSI reports with reportQuantity set to 'p-cri-r19', 'p-cri-RSRP-r19', 'p-ssb-index-r19', or 'p-ssb-index-RSRP-r19' corresponds to either x = 2 or x = 3 subject to UE capability and the CSI reports configured with the higher layer parameter the higher layer parameter csi-InferencePrediction-r19 corresponds to either x = 2 or x = 3 subject to UE capability. For CSI reports with reportQuantity set to 'p-cri-r19', 'p-cri-RSRP-r19', 'p-ssb-index-r19', or 'p-ssb-index-RSRP-r19', and CSI reports configured with the higher layer parameter csi-InferencePrediction-r19, and are considered for determining and , and if a CSI report is not considered within any of and , the values for the CPUs corresponding to and of the CSI report are not occupied considered to be 0, for the procedure previously described in this clause, and the UE is not required to update the CSI report. <omitted texts> |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2508772](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2508772.zip) · `[123-R19-AI/ML]`

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#123:8.1:004` · 관련 주제: Beam management, CSI 보고/codebook, CSI-RS · 유지보수 (CR)

구현 영향: 처리 시간·CPU, 측정·보고량 · 규격: TS 38.214 5.2.1.6

> The following TP is endorsed for TS 38.214.
> | Reason for change | CPU duration for CSI prediction related data collection is not captured correctly. |
> | Summary of change | Reflect the RAN1 agreements accurately in Section 5.2.1.6 of TS 38.214. |
> | Consequences if not approved | Incorrect UE behaviour for CPU duration for data collection for training. |
> | 5.2.1.6 CSI processing criteria < Unchanged parts are omitted > For a CSI report with CSI-ReportConfig with higher layer parameter reportQuantity set to 'none' and CSI-RS-ResourceSet with higher layer parameter trs-Info not configured, or reportQuantity set to 'none-bm-r19' or 'none-csi-r19', the CPU(s) are occupied for a number of OFDM symbols as follows: - A semi-persistent CSI report (excluding an initial semi-persistent CSI report on PUSCH after the PDCCH triggering the report) occupies CPU(s) from the first symbol of the earliest one of each transmission occasion of periodic or semi-persistent CSI-RS/SSB resource for channel measurement for L1-RSRP computation, until symbols after the last symbol of the latest one of the CSI-RS/SSB resource for channel measurement for L1-RSRP computation in each transmission occasion. - An aperiodic CSI report occupies CPU(s) from the first symbol after the PDCCH triggering the CSI report until the last symbol between symbols after the first symbol after the PDCCH triggering the CSI report and symbols after the last symbol of the latest one of each CSI-RS/SSB resource for channel measurement for L1-RSRP computation. For a CSI report with CSI-ReportConfig with higher layer parameter reportQuantity set to 'none-csi-r19', the CPU(s) are occupied for a number of OFDM symbols as follows: - CSI report occupies CPU(s) from the first symbol of each transmission occasion of periodic or semi-persistent CSI-RS resource for channel measurement, until symbols after the transmission occasion of periodic or semi-persistent CSI-RS resource for channel measurement. < Unchanged parts are omitted > | 5.2.1.6 CSI processing criteria < Unchanged parts are omitted > For a CSI report with CSI-ReportConfig with higher layer parameter reportQuantity set to 'none' and CSI-RS-ResourceSet with higher layer parameter trs-Info not configured, or reportQuantity set to 'none-bm-r19' or 'none-csi-r19', the CPU(s) are occupied for a number of OFDM symbols as follows: - A semi-persistent CSI report (excluding an initial semi-persistent CSI report on PUSCH after the PDCCH triggering the report) occupies CPU(s) from the first symbol of the earliest one of each transmission occasion of periodic or semi-persistent CSI-RS/SSB resource for channel measurement for L1-RSRP computation, until symbols after the last symbol of the latest one of the CSI-RS/SSB resource for channel measurement for L1-RSRP computation in each transmission occasion. - An aperiodic CSI report occupies CPU(s) from the first symbol after the PDCCH triggering the CSI report until the last symbol between symbols after the first symbol after the PDCCH triggering the CSI report and symbols after the last symbol of the latest one of each CSI-RS/SSB resource for channel measurement for L1-RSRP computation. For a CSI report with CSI-ReportConfig with higher layer parameter reportQuantity set to 'none-csi-r19', the CPU(s) are occupied for a number of OFDM symbols as follows: - CSI report occupies CPU(s) from the first symbol of each transmission occasion of periodic or semi-persistent CSI-RS resource for channel measurement, until symbols after the transmission occasion of periodic or semi-persistent CSI-RS resource for channel measurement. < Unchanged parts are omitted > |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509188](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509188.zip) · `[123-R19-AI/ML]`

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#123:8.1:005` · 관련 주제: CSI 보고/codebook · 유지보수 (CR)

구현 영향: 측정·보고량

> The following TP is endorsed for TS 38.214.
> | Reason for change | In current TS 38.214, if the UE is configured with a CSI-ReportConfig that contains a list of sub-configurations, provided by csi-ReportSubConfigToAddModList, the report quantities that UE does not expect to be configured introduced are specified. In Rel-19 AI/ML, some new report quantities are introduced. Specifically, the following new report quantities are introduced in Rel-19 AI/ML: 'p-cri-r19', 'p-cri-RSRP-r19', 'p-ssb-index-r19', 'p-ssb-index-RSRP-r19', 'rs-pai-r19', 'csi-pai-r19', 'none-csi-r19', 'none-bm-r19'. Then the current description should cover the new report quantities. |
> | Summary of change | Include the report quantities in Rel-19 that UE does not expect to be configured with when UE is configured with sub-configurations. |
> | Consequences if not approved | Incorrect UE behaviour when UE is configured with sub-configurations. |
> | 5.2.1.4.2 Report quantity configurations <Unrelated parts are omitted> If the UE is configured with a CSI-ReportConfig that contains a list of sub-configurations, provided by csi-ReportSubConfigToAddModList: <Unrelated parts are omitted> - The UE does not expect the higher layer parameter reportQuantity to be set to 'cri-RSRP', 'cri-SINR', 'cri-SINR- Index', 'cri-RSRP-Index', 'none', 'ssb-Index-RSRP', 'ssb-Index-SINR', 'ssb-Index-RSRP- Index', 'ssb-Index-SINR- Index', or 'tdcp'., 'p-cri-r19', 'p-cri-RSRP-r19', 'p-ssb-index-r19', 'p-ssb-index-RSRP-r19', 'rs-pai-r19', 'csi-pai-r19', 'none-csi-r19', or 'none-bm-r19'. <Unrelated parts are omitted> | 5.2.1.4.2 Report quantity configurations <Unrelated parts are omitted> If the UE is configured with a CSI-ReportConfig that contains a list of sub-configurations, provided by csi-ReportSubConfigToAddModList: <Unrelated parts are omitted> - The UE does not expect the higher layer parameter reportQuantity to be set to 'cri-RSRP', 'cri-SINR', 'cri-SINR- Index', 'cri-RSRP-Index', 'none', 'ssb-Index-RSRP', 'ssb-Index-SINR', 'ssb-Index-RSRP- Index', 'ssb-Index-SINR- Index', or 'tdcp'., 'p-cri-r19', 'p-cri-RSRP-r19', 'p-ssb-index-r19', 'p-ssb-index-RSRP-r19', 'rs-pai-r19', 'csi-pai-r19', 'none-csi-r19', or 'none-bm-r19'. <Unrelated parts are omitted> |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509188](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509188.zip) · `[123-R19-AI/ML]`

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#123:8.1:006` · 관련 주제: CSI 보고/codebook, CSI-RS · 유지보수 (CR)

구현 영향: 측정·보고량

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> The following TP for TS 38.214 is endorsed.
> | Reason for change | In current specification, it is ambiguous which prediction instance the UE should monitor for CSI-PAI. |
> | Summary of change | Specify that the monitoring report is linked to the S-th time instance contains the same slot of the transmission occasion of the CSI-RS resources for CSI-PAI report. |
> | Consequences if not approved | Incomplete UE behaviour for CSI-PAI reporting. |
> | 5.2.1.4.6 CSI-PAI reporting << Unchanged parts are omitted >> to report CSI-PAI for the second Reporting Setting, the UE shall: - determine predicted PMI (see Clause 5.2.2.2.10 or Clause 5.2.2.2.11) for each of the subband(s) configured by csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband for the -th time instance configured by timeinstanceforCSImonitoring-r19 in the second Reporting Setting ( , with >1 provided in the first Reporting Setting), based on the CSI prediction performed by the UE using the channel measurement corresponding to the first Reporting Setting, - determine non-predicted PMI for each of the subband(s) configured by csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband, which is corresponding to the -th time instance of the report of the first Reporting Setting, based on the CSI-RS resource(s) whose transmission occasion is contained within the same slot of the S-th time instance of the report of the first Reporting Setting in the resource set for channel measurement for the report corresponding to the second Reporting Setting. - determine non-predicted PMI for each of the subband(s) configured by csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband, based on the latest CSI-RS resource transmission occasion, no later than the CSI reference resource of the CSI report, corresponding to the first Reporting Setting - for , is the RI reported for the CSI report corresponding to the first Reporting Setting, calculate SGCS value(s) as, << Unchanged parts are omitted >> | 5.2.1.4.6 CSI-PAI reporting << Unchanged parts are omitted >> to report CSI-PAI for the second Reporting Setting, the UE shall: - determine predicted PMI (see Clause 5.2.2.2.10 or Clause 5.2.2.2.11) for each of the subband(s) configured by csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband for the -th time instance configured by timeinstanceforCSImonitoring-r19 in the second Reporting Setting ( , with >1 provided in the first Reporting Setting), based on the CSI prediction performed by the UE using the channel measurement corresponding to the first Reporting Setting, - determine non-predicted PMI for each of the subband(s) configured by csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband, which is corresponding to the -th time instance of the report of the first Reporting Setting, based on the CSI-RS resource(s) whose transmission occasion is contained within the same slot of the S-th time instance of the report of the first Reporting Setting in the resource set for channel measurement for the report corresponding to the second Reporting Setting. - determine non-predicted PMI for each of the subband(s) configured by csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband, based on the latest CSI-RS resource transmission occasion, no later than the CSI reference resource of the CSI report, corresponding to the first Reporting Setting - for , is the RI reported for the CSI report corresponding to the first Reporting Setting, calculate SGCS value(s) as, << Unchanged parts are omitted >> |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509188](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509188.zip) · `[123-R19-AI/ML]`

**Conclusion** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#123:8.1:007` · 유지보수 (CR)

> There is no consensus in RAN1 to further discuss active resource/port counting value for inference report if associated performance monitoring is configured.

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509188](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509188.zip) · `[123-R19-AI/ML]`

**Conclusion** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#123:8.1:008` · 관련 주제: CSI 보고/codebook · 유지보수 (CR)

구현 영향: 처리 시간·CPU

> There is no consensus in RAN1 to further discuss on enhancement of timeline for AP CSI-PAI report (Z, Z’) and SP CSI-PAI report.

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509188](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509188.zip) · `[123-R19-AI/ML]`

**Agreement** · `10.1.1.1` Inference related aspects · `RAN1#123:10.1.1.1:001` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> Support NW side optionally exchanges codebook to the UE side.
> - If NW side exchanges a codebook, the exchanged codebook is associated to the pairing ID.
>   - FFS SQ / VQ / both is supported
>   - FFS the details, e.g., whether exchange the NW-defined codebook or the  ID of a standardized SQ codebook in case of multiple standardized codebooks.
> - If NW side does not exchange a codebook or an ID of a standardized SQ codebook in case of multiple standardized codebooks, a standardized SQ codebook is associated to the pairing ID.
> - Note: For the same quantization resolution, a common codebook is used for all the scalars/segment(s), all the layers of pre-coding matrix and all parameter pairs/triplets for the associated pairing ID.

FFS 2줄

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509215](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509215.zip)

**Agreement** · `10.1.1.1` Inference related aspects · `RAN1#123:10.1.1.1:002` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> If target CSI type is pre-coder matrix, at least support per-layer payload parameter pairs {32, 2}, {64, 2}, {128, 2}, {192, 2}
> - FFS: Whether support per-layer payload parameter pairs {32, 1}, {48, 2}, {96, 1}, {96, 2}, {192, 1}, {128,10/128}
> - Note: The above pair refers to the pair of latent dimension and quantization resolution, i.e., {d, Q} for SQ or {d, Q/L} for VQ.

FFS 1줄

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509215](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509215.zip)

**Agreement** · `10.1.1.1` Inference related aspects · `RAN1#123:10.1.1.1:003` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> If target CSI type is pre-coder matrix, at least for SQ, for the PC with rank-1 payload of 128 bits, support the following payload combinations across layers and ranks. The layers are reported in the order of decreasing strength.
> | Rank1 | Rank2 | Rank3 | Rank4 |
> | {64, 2} | {64, 2}, {64, 2} | {32, 2}, {32, 2}, {64, 2} | {32, 2}, {32, 2}, {32, 2}, {32, 2} |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509215](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509215.zip)

**Agreement** · `10.1.1.1` Inference related aspects · `RAN1#123:10.1.1.1:004` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> If target CSI type is pre-coder matrix, at least for SQ, for the PC with rank-1 payload of 256 bits, support the following payload combinations across layers and ranks. The layers are reported in the order of decreasing strength.
> | Rank1 | Rank2 | Rank3 | Rank4 |
> | {128, 2} | {128, 2}, {128, 2} | {64, 2}, {64, 2}, {128, 2} | {64, 2}, {64, 2}, {64, 2}, {64, 2} |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509215](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509215.zip)

**Agreement** · `10.1.1.1` Inference related aspects · `RAN1#123:10.1.1.1:005` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> If target CSI type is pre-coder matrix, at least for SQ, for the PC with rank-1 payload of 64 bits, select one alternative from following alternatives in RAN1 #124.
> - The layers are reported in the order of decreasing strength.
> - Note: For the purpose of comparison, consider the following:
>   - For comparing Alt.1 and Alt. 2, consider payload scalability.
> |  | Rank1 | Rank2 | Rank3 | Rank4 |
> | Alt1 | {32, 2} | {32, 2}, {32, 2} | NA | NA |
> | Alt2 | {32, 2} | {32, 2}, {32, 2} | {32, 1}, {32, 1}, {32, 2} | {32, 1}, {32, 1}, {32, 1}, {32, 1} |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509215](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509215.zip)

**Agreement** · `10.1.1.1` Inference related aspects · `RAN1#123:10.1.1.1:006` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> If target CSI type is pre-coder matrix, at least for SQ, for the PC with rank-1 payload of 384 bits, select one alternative from following alternatives in RAN1 #124.
> - The layers are reported in the order of decreasing strength.
> |  | Rank1 | Rank2 | Rank3 | Rank4 |
> | Alt1.1 | {192, 2} | {192, 2}, {192, 2} | {96, 2}, {96, 2}, {192, 2} | {96, 2}, {96, 2}, {96, 2}, {96, 2} |
> | Alt1.2 | {192, 2} | {192, 2}, {192, 2} | {192, 1}, {192, 1}, {192, 2} | {192, 1}, {192, 1}, {192, 1}, {192, 1} |
> | Alt2 | {192, 2} | {192, 2}, {192, 2} | {128, 2}, {128, 2}, {128, 2} | {64, 2}, {64, 2}, {128, 2}, {128, 2} |
> | Alt3.1 | {192, 2} | {192, 2}, {192, 2} | {128, 2}, {128, 2}, {128, 2} | {96, 2}, {96, 2}, {96, 2}, {96, 2} |
> | Alt3.2 | {192, 2} | {192, 2}, {192, 2} | {128, 2}, {128, 2}, {128, 2} | {192, 1}, {192, 1}, {192, 1}, {192, 1} |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509215](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509215.zip)

**Agreement** · `10.1.1.2` Other aspects · `RAN1#123:10.1.1.2:001` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> For NW side data collection with higher layer reporting, regarding Target CSI quantization, Option 1 (Scalar quantization) is supported.
> Note: Supporting target CSI payload size greater than single RRC message may need RAN2 justification.

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509507](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509507.zip)

**Agreement** · `10.1.1.2` Other aspects · `RAN1#123:10.1.1.2:002` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

구현 영향: 포트·자원·레이어 수, 메모리·복잡도

> For Option 1 (scalar quantization) of NW side data collection with higher layer reporting, down select between Option 1a and Option 1b:
> - Option 1a: Each complex element of the Target CSI sample is quantized to real value and imaginary value
>   - Further study at least k1=k2=3, 4, 5, 6, and 8 to ensure the performance (e.g., the minimum value that achieves the close performance to upperbound).
>   - Further study the quantized value of each codepoint.
> - Option 1b: Each complex element of the Target CSI sample is quantized to amplitude value and phase value
>   - Further study at least k1+k2=6, 7, 8, 12, and 16 with k1>k2, k1<k2 or k1=k2 to ensure the performance (e.g., the minimum value that achieves the close performance to upperbound).
>   - Further study the quantized value of each codepoint.
> - Further study the potential UE complexity between Option 1a and Option 1b, e.g., considering the potential conversion to amplitude/phase domain of Option 1b.
> - Consider Metric#1 (SGCS for a trained model) for the evaluation.
> - The study at least considers 32 ports, 64 ports, and 128 ports; 19 subbands; rank 4.
> - It is up to companies to study mixed Target CSIs subject to multiple {k1, k2} values each corresponding to a specific port/subband/layer configuration, for training scalable model.
> - Study the necessity of RRC signaling enhancement, e.g., for a large k1, k2 pair if needed.
> - Further study whether/how to perform normalization for Option 1a and Option 1b, e.g., the ranges of both [T1min, T1max] and [T2min, T2max] are fixed and specified as [-1, 1] for real/imag quantization, or [0, 1]/[0, 2π) for amplitude/phase quantization. Select one among the alternatives:
>   - Alt.1: It is UE implementation to perform scale up/down to fit the fixed range.
>   - Alt.2: Additional specification on the quantization, e.g.,
>     - Alt.2-1: At least one element among all real and imag elements in the Target CSI matrix (FFS per layer and/or per subband) correspond to any of Tmin (where Tmin=T1min=T2min) and Tmax (where Tmax=T1max=T2max) in the quantization table or at least one element among all amplitude elements in the Target CSI matrix (FFS per layer and/or per subband) correspond to T1max
>     - Alt.2-2: Reporting scaling factor and offset factor used for denormalization.
>     - Alt.2-3: Fixed scaling factor used for normalization.

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509507](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509507.zip)

**Agreement** · `10.1.1.2` Other aspects · `RAN1#123:10.1.1.2:003` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> Support providing Pairing ID(s) in CSI-ReportConfig for UE side data collection
> - FFS mandatory or optional
> - FFS whether to configure Pairing ID for NW side data collection
> - FFS whether multiple Pairing IDs provided in one CSI-ReportConfig for UE side data collection

FFS 3줄

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509507](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509507.zip)

**Agreement** · `10.1.2` Inter-vendor training collaboration for two-sided AI/ML models · `RAN1#123:10.1.2:001` · 관련 주제: CSI 보고/codebook, CSI-RS · 규격 작업 (WI)

구현 영향: 포트·자원·레이어 수

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> When the target CSI is precoding matrix with port-subband domain representation, for the association between target CSI and CSI feedback in the exchanged dataset,
>     - A pairing ID has  target CSI sets,
>       - Each target CSI set has  target CSI samples, >1.
>       - Each target CSI sample within the same target CSI set k has a port dimension of N1x N2x2, and the maximum number of subbands, and a rank Vk
>       - Each target CSI sample within the same target CSI set k has Vk layers, ordered from the strongest to the weakest layer, where Vk is the rank
>     - Target CSI set k is associated with  CSI feedback sets,
>       - Each CSI feedback set corresponds to a specific per layer CSI payload size configuration for a rank and subband configuration
>   - FFS: rank (CSI feedback rank can be different compared to target CSI rank)
>   - FFS: whether per layer CSI payload size is the same for all the layers of all the samples of the same CSI feedback set.
>       - Each CSI feedback sample within the set includes CSI feedback per layer, ordered from the strongest to the weakest layer.
>       - The target CSI set and each of the corresponding CSI feedback set has the same number of samples
>     - Metadata:
>       - Per Target CSI set metadata: for each   set, number of samples , the port configuration of N1 and N2, subband size and BWP info (NR ARFCN of the lowest PRB of the BWP and BWP size and the SCS), rank Vk, number of associated CSI feedback set
>   - FFS: the number of aggregated CSI-RS resources for total number of antenna ports larger than 32, and the portMappingMethod applicable to aggregated resources
> - For each CSI feedback set metadata: CSI payload size configuration, subband configuration
>   - FFS: Additional CSI feedback metadata to indicate when specific scalability option is used in model design (e.g. truncation/masking) is used as CSI feedback payload scalability option.
>   - FFS: rank
>       - Other metadata are not precluded.
>       - How the association between the kth target CSI set and Mk CSI feedback sets is indicated is up to SA WG.

FFS 5줄

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509097](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509097.zip)

**Agreement** · `10.1.2` Inter-vendor training collaboration for two-sided AI/ML models · `RAN1#123:10.1.2:002` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> For Option 4-1 under Direction A in AI/ML based CSI compression:
> - Discuss whether to introduce linkage between multiple data sets having their own pairing IDs.
> - Discuss whether to introduce delivery of additional data set appending new samples on top of previously exchanged data set.

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509097](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509097.zip)

## RAN1#122bis — 44건

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#122bis:8.1:001` · 관련 주제: CSI 보고/codebook · 유지보수 (CR)

규격: TS 38.214 5.2.1.4.3

> The following TP for TS 38.214 Clause 5.2.1.4.3b is endorsed.
> Reason for change: The slot of transmission occasion for monitoring is unclear for the linkage of the corresponding CSI report for inference.
> Summary of change: Clarify the first slot of transmission occasion for monitoring is used for the linkage.
> Consequences if not approved: gNB and UE may have different understanding on the linkage.
> | TS 38.214 Clause 5.2.1.4.3b RS-PAI Reporting <omitted texts> - check a condition : - for the transmission occasion of the second CSI Reporting Setting, there is a linked report of the first CSI Reporting Setting. When nroftimeinstance-r19 is not configured in the first Reporting Setting, the linking is determined if CSI reference resource of a report of the first CSI Reporting Setting has a minimal slot offset, no larger than 64 slots, from the first slot of the transmission occasion of the corresponding Resource Set for channel measurement of the second CSI Reporting Setting. When nroftimeinstance-r19 is configured in the first Reporting Setting, timeinstanceformonitoring-r19 configured in the second CSI Reporting Setting indicates the timeinstanceformonitoring-r19-th time instance among nroftimeinstance-r19 time instance(s), and the linking is determined if the slot corresponding to the time instance indicated by timeinstanceformonitoring-r19 of a report of the first CSI Reporting Setting has a minimal slot offset, no larger than 64 slots, from the first slot of the transmission occasion of the corresponding Resource Set for channel measurement of the second CSI Reporting Setting; <omitted texts> |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2507998](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2507998.zip) · `[122bis-R19-AI/ML]`

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#122bis:8.1:002` · 관련 주제: SRS, Beam management, CSI 보고/codebook · 유지보수 (CR)

구현 영향: 측정·보고량 · 규격: TS 38.214 6.2.1.3

> The following TP for 38.214 Clause 6.2.1.3 is endorsed.
> Reason for change: P-CRI/P-SSBRI/RS-PAI/P-L1-RSRP is missing in the prioritization rules between a transmission of SRS and transmission of a physical signal/channel.
> Summary of change: Add P-CRI/P-SSBRI/RS-PAI/P-L1-RSRP in the prioritization rules.
> Consequences if not approved: the prioritization rules between a transmission of SRS and transmission of a physical signal/channel with P-CRI/P-SSBRI/RS-PAI/P-L1-RSRP is unclear.
> | 6.2.1.3 UE sounding procedure between component carriers <omitted text> The following prioritization rules shall be applied in case of collision between a transmission of SRS over carrier and transmission of a physical signal/channel over a carrier of a serving cell in set - the UE shall not transmit SRS whenever SRS transmission (including any interruption due to uplink or downlink RF retuning time [11, TS 38.133] as defined by higher layer parameters switchingTimeUL and switchingTimeDL of SRS-SwitchingTimeNR) on the carrier of the serving cell and PUSCH/PUCCH transmission carrying HARQ-ACK/positive SR/RI/CRI/SSBRI/P-CRI/P-SSBRI/RS-PAI and/or PRACH on a carrier of a serving cell in set happen to overlap in the same symbol - the UE shall not transmit a periodic/semi-persistent SRS whenever periodic/semi-persistent SRS transmission (including any interruption due to uplink or downlink RF retuning time [11, TS 38.133] as defined by higher layer parameters switchingTimeUL and switchingTimeDL of SRS-SwitchingTimeNR) on the carrier of the serving cell and PUSCH transmission carrying aperiodic CSI on a carrier of a serving cell in set happen to overlap in the same symbol - the UE shall drop PUCCH/PUSCH transmission carrying periodic/semi-persistent CSI comprising only CQI/PMI/L1-RSRP/L1-SINR/P-L1-RSRP, and/or SRS transmission on a carrier of a serving cell in set configured for PUSCH/PUCCH transmission whenever the transmission and SRS transmission (including any interruption due to uplink or downlink RF retuning time [11, TS 38.133] as defined by higher layer parameters switchingTimeUL and switchingTimeDL of SRS-SwitchingTimeNR) on the carrier of the serving cell happen to overlap in the same symbol - the UE shall drop PUSCH transmission carrying aperiodic CSI comprising only CQI/PMI/L1-RSRP/L1-SINR/TDCP/cjtc-Dd/cjtc-F/cjtc-Dd-F/cjtc-P/P-L1-RSRP on a carrier of a serving cell in set whenever the transmission and aperiodic SRS transmission (including any interruption due to uplink or downlink RF retuning time [11, TS 38.133]) as defined by higher layer parameters switchingTimeUL and switchingTimeDL of SRS-SwitchingTimeNR) on the carrier of the serving cell happen to overlap in the same symbol. <omitted text> |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2507998](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2507998.zip) · `[122bis-R19-AI/ML]`

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#122bis:8.1:003` · 관련 주제: SRS, Beam management, CSI 보고/codebook · 유지보수 (CR)

구현 영향: 측정·보고량 · 규격: TS 38.214 6.2.1, TS 38.213 9.2.4

> The following TP for 38.214 Clause 6.2.1 is endorsed.
> Reason for change: P-CRI/P-SSBRI/RS-PAI/P-L1-RSRP is missing in the collision handling procedure between a transmission of SRS and transmission of a physical signal/channel.
> Summary of change: Add P-CRI/P-SSBRI/RS-PAI/P-L1-RSRP in the collision handling procedure.
> Consequences if not approved: the collision handling procedure between a transmission of SRS and transmission of a physical signal/channel P-CRI/P-SSBRI/RS-PAI/P-L1-RSRP is unclear.
> | 6.2.1 UE sounding procedure <omitted text> For PUCCH and SRS on the same carrier, a UE shall not transmit SRS when semi-persistent or periodic SRS is configured in the same symbol(s) with PUCCH carrying only CSI report(s), or only L1-RSRP report(s), or only L1-SINR report(s), or only P-CRI/P-SSBRI/P-L1-RSRP report(s), or only RS-PAI report(s). A UE shall not transmit SRS when semi-persistent or periodic SRS is configured or aperiodic SRS is triggered to be transmitted in the same symbol(s) with PUCCH carrying HARQ-ACK, link recovery request (as defined in clause 9.2.4 of [6, 38.213]) and/or SR. In the case that SRS is not transmitted due to overlap with PUCCH, only the SRS symbol(s) that overlap with PUCCH symbol(s) are dropped. PUCCH shall not be transmitted when aperiodic SRS is triggered to be transmitted to overlap in the same symbol with PUCCH carrying semi-persistent/periodic CSI report(s) or semi-persistent/periodic L1-RSRP report(s) only, or only L1-SINR report(s), or only P-CRI/P-SSBRI/P-L1-RSRP report(s), or only RS-PAI report(s) and the PUCCH starts no earlier than after the last symbol of the PDCCH carrying the triggering command for the aperiodic SRS, where is the PUSCH preparation time for the corresponding UE processing capability assuming and corresponds to the smallest SCS configuration between the SCS configuration of the PDCCH carrying the triggering command and the SCS configuration of the PUCCH. <omitted text> |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2507998](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2507998.zip) · `[122bis-R19-AI/ML]`

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#122bis:8.1:004` · 유지보수 (CR)

> Regarding the RAN2 LS from R1-2506715, for the UE-side candidate data collection configuration for BM-Case2, include the following IEs along with the already agreed IEs in RAN2:
> - TimeGap-r19, i.e., the expected time gap between two consecutive predicted time instances and between the reference time and the earliest predicted time instance.
> - nroftimeinstance-r19, i.e., number of expected predicted time instances.

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2507998](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2507998.zip) · `[122bis-R19-AI/ML]`

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#122bis:8.1:005` · 유지보수 (CR)

> Regarding the RAN2 LS R1-2506720, the answer to the question in the LS is as below:
> | From RAN1 perspective, Option 2 is best option and can resolve the issue. No additional RAN 1 impact was identified for Option 2. |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2507999](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2507999.zip) · `[122bis-R19-AI/ML]`

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#122bis:8.1:006` · 관련 주제: CSI 보고/codebook, CSI-RS · 유지보수 (CR)

구현 영향: 측정·보고량 · 규격: TS 38.214 5.2.1.4.2

> The following TP for TS 38.214 Clause 5.2.1.4.2 is endorsed.
> Reason for change: The configuration restriction of AP RS resource set with no more than 16 resources is too restrictive for Set A for inference.
> Summary of change: For Set A for inference, relax the configuration restriction of AP RS resource set with no more than 16 resources.
> Consequences if not approved: The configuration of more than 16 resource within Set A for inference is not possible.
> | TS 38.214 Clause 5.2.1.4.2 Report quantity configurations <omitted texts> If the UE is configured with a CSI-ReportConfig with the higher layer parameter reportQuantity set to 'cri-RI-LI-PMI-CQI', UE does not expect the CSI-ReportConfig to be configured with higher layer parameter codebookType set to 'typeII-r16' or 'typeII-PortSelection-r16', 'typeII-PortSelection-r17', 'typeII-CJT-r18', 'typeII-CJT-PortSelection-r18', 'typeII-Doppler-r18', 'typeII-Doppler-PortSelection-r18', 'eTypeII-r19', 'TypeII-FePortSelection-r19' or 'typeII-Doppler-r19'. If the UE is configured with a CSI-ReportConfig with higher layer parameter reportQuantity set to 'cri-RSRP', 'cri-SINR', 'none', 'cri-RSRP- Index', 'cri-SINR- Index, 'p-cri-r19', 'p-cri-RSRP-r19', 'p-ssb-index-r19', 'p-ssb-index-RSRP-r19', or ‘rs-pai-r19', and the CSI-ReportConfig is linked to a resource setting not configured by resourcesForSetA-r19 and configured with the higher layer parameter resourceType set to 'aperiodic', then the UE is not expected to be configured with more than 16 CSI-RS resources in a CSI-RS resource set contained within the resource setting. <omitted texts> |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2507999](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2507999.zip) · `[122bis-R19-AI/ML]`

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#122bis:8.1:007` · 유지보수 (CR)

> The draft response LS in R1-2508121 is endorsed. Final LS in R1-2508122

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2507999](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2507999.zip) · `[122bis-R19-AI/ML]`

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#122bis:8.1:010` · 관련 주제: CSI 보고/codebook, CSI-RS · 유지보수 (CR)

구현 영향: 측정·보고량 · 규격: TS 38.214 5.1.6.1

> The following TP for TS 38.214 is endorsed.
> | Reason for change | During non-active periods of cell DTX, UE is not expected to receive P/SP CSI-RS for CSI report associated with report quantity comprising at least RI which means this can be applied to SP inference report. However, whether it is applied for monitoring report is not clear. |
> | Summary of change | Report quantity ‘csi-pai-r19’ is added. |
> | Consequences if not approved | Inconsistent UE behaviour during non-active periods of cell DTX. |
> | TS38.214 5.1.6.1 CSI-RS reception procedure << Unchanged parts are omitted >> During non-active periods of cell DTX if cell DTX is activated for a serving cell, the UE is not expected to receive the periodic CSI-RS and semi-persistent CSI-RS on the serving cell configured in CSI report configuration in CSI-ReportConfig associated with the higher layer parameter reportQuantity comprising at least 'RI' or 'cjtc-P' or ‘csi-pai-r19’. If the cell DTX is activated for a serving cell [10, TS 38.321], the most recent CSI measurement occasion of semi-persistent CSI-RS resource or periodic CSI-RS resource on the serving cell occurs in active periods of cell DTX for CSI report configured by CSI-ReportConfig associated with the higher layer parameter reportQuantity comprising at least 'RI' or 'cjtc-P' or ‘csi-pai-r19’. << Unchanged parts are omitted >> | TS38.214 5.1.6.1 CSI-RS reception procedure << Unchanged parts are omitted >> During non-active periods of cell DTX if cell DTX is activated for a serving cell, the UE is not expected to receive the periodic CSI-RS and semi-persistent CSI-RS on the serving cell configured in CSI report configuration in CSI-ReportConfig associated with the higher layer parameter reportQuantity comprising at least 'RI' or 'cjtc-P' or ‘csi-pai-r19’. If the cell DTX is activated for a serving cell [10, TS 38.321], the most recent CSI measurement occasion of semi-persistent CSI-RS resource or periodic CSI-RS resource on the serving cell occurs in active periods of cell DTX for CSI report configured by CSI-ReportConfig associated with the higher layer parameter reportQuantity comprising at least 'RI' or 'cjtc-P' or ‘csi-pai-r19’. << Unchanged parts are omitted >> |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508061](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508061.zip) · `[122bis-R19-AI/ML]`

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#122bis:8.1:011` · 관련 주제: CSI 보고/codebook · 유지보수 (CR)

> Regarding the RAN2 LS from R1-2506715, for the UE-side candidate data collection configuration for CSI prediction, include the following IEs:
> - CSI-ResourceConfigId
> - FFS: whether to include other parameters

FFS 1줄

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508061](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508061.zip) · `[122bis-R19-AI/ML]`

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#122bis:8.1:012` · 관련 주제: CSI 보고/codebook, CSI-RS · 유지보수 (CR)

구현 영향: 측정·보고량 · 규격: TS 38.214 5.2.1.4.6

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> Adopt the following TP for TS 38.214.
> | Reason for change | According to the agreement, Rel-16 eType II codebook is used for calculating both the precoder represented by PMI based on the channel measurement corresponding to the monitoring report and the precoder represented by PMI based on the latest CSI-RS resource transmission occasion, no later than CSI reference resource, corresponding to the inference report. However, the codebook for calculating was not clearly captured by the specification. |
> | Summary of change | Add the corresponding description of the codebook for calculating in TS 38.214. |
> | Consequences if not approved | How to select the codebook for calculating is not clearly defined in TS 38.214, which is not aligned with the agreement. |
> | TS38.214 5.2.1.4.6 CSI-PAI reporting << Unchanged parts are omitted >> - to report CSI-PAI for the second Reporting Setting, the UE is expected to be configured in the second Report Setting with codebookType set to ‘etypeII-r16’ and it shall: <Unrelated part omitted> for , is the RI reported for the CSI report corresponding to the first Reporting Setting, calculate SGCS value(s) as, , , where is the predicted precoder represented by predicted PMI for -th layer, n-th subband and for -th time instance corresponding to the report of the first Reporting Setting, is the precoder represented by non-predicted PMI for -th layer, n-th subband based on the channel measurement corresponding to the second Reporting Setting, and is the precoder represented by PMI for -th layer and n-th subband, , corresponds to the subbands configured by csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband, based on the latest CSI-RS resource transmission occasion, no later than CSI reference resource, corresponding to the report of the first Reporting Setting. Both and are calculated based on the codebookConfig within the second Reporting Setting. The UE is expected to be configured with same csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband configurations for the first CSI Reporting Setting and the second CSI Reporting Setting. << Unchanged parts are omitted >> | TS38.214 5.2.1.4.6 CSI-PAI reporting << Unchanged parts are omitted >> - to report CSI-PAI for the second Reporting Setting, the UE is expected to be configured in the second Report Setting with codebookType set to ‘etypeII-r16’ and it shall: <Unrelated part omitted> for , is the RI reported for the CSI report corresponding to the first Reporting Setting, calculate SGCS value(s) as, , , where is the predicted precoder represented by predicted PMI for -th layer, n-th subband and for -th time instance corresponding to the report of the first Reporting Setting, is the precoder represented by non-predicted PMI for -th layer, n-th subband based on the channel measurement corresponding to the second Reporting Setting, and is the precoder represented by PMI for -th layer and n-th subband, , corresponds to the subbands configured by csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband, based on the latest CSI-RS resource transmission occasion, no later than CSI reference resource, corresponding to the report of the first Reporting Setting. Both and are calculated based on the codebookConfig within the second Reporting Setting. The UE is expected to be configured with same csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband configurations for the first CSI Reporting Setting and the second CSI Reporting Setting. << Unchanged parts are omitted >> |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508062](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508062.zip) · `[122bis-R19-AI/ML]`

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#122bis:8.1:013` · 관련 주제: CSI 보고/codebook, CSI-RS · 유지보수 (CR)

구현 영향: 처리 시간·CPU, UE capability·FG, 측정·보고량 · 규격: TS 38.214 5.2.1.4.2, TS 38.214 5.2.1.4.6, TS 38.214 5.2.1.6, TS 38.214 5.4, TS 38.214 5.2.5 외 1

> Following TP is endorsed as editorial corrections for TS 38.214 for Clauses 5.2.1.4.2, 5.2.1.4.6, 5.2.1.6 and 5.4.
> | TS38.214 5.2.1.4.2 Report quantity configurations << Unchanged parts are omitted >> If the UE is configured with a CSI-ReportConfig with reportQuantity-r19 set to ‘csi-pai-r19’, - the UE shall be configured with inferenceReportConfigId-r19 to link another CSI-ReportConfig configured with the higher layer parameter [RRC_name-r19] csi-InferencePrediction-r19, - when semi-persistent Reporting Setting is configured for the CSI-ReportConfig configured with the higher layer parameter [RRC_name-r19] csi-InferencePrediction-r19, the UE is not expected to be configured with a periodic Reporting Setting for the CSI-ReportConfig with reportQuantity-r19 set to ‘csi-pai-r19’. - when aperiodic Reporting Setting is configured for the CSI-ReportConfig configured with the higher layer parameter [RRC_name-r19] csi-InferencePrediction-r19, the UE is not expected to be configured with a periodic or semi-persistent Reporting Setting for the CSI-ReportConfig with reportQuantity-r19 set to ‘csi-pai-r19’. << Unchanged parts are omitted >> 5.2.1.4.6 CSI-PAI reporting When the UE is configured with a first CSI Reporting Setting for reporting CSI prediction, based on a CSI-ReportConfig configured with the higher layer parameter [RRC_name-r19] csi-InferencePrediction-r19 and a second CSI Reporting Setting for reporting CSI-PAI, based on a CSI-ReportConfig with reportQuantity-r19 set to ‘csi-pai-r19’, and the second Reporting Setting is linked to the first Reporting Setting by inferenceReportConfigId-r19, the reporting of CSI-PAI corresponding to the second CSI Reporting Setting shall consider the following: << Unchanged parts are omitted >> 5.2.1.6 CSI processing criteria The UE indicates the number of supported simultaneous CSI calculations with parameter simultaneousCSI-ReportsPerCC or simultaneousCSI-SubReportsPerCC-r18 in a component carrier, and simultaneousCSI-ReportsAllCC or simultaneousCSI-SubReportsAllCC-r18 across all component carriers. If UE is configured with at least one CSI report setting with sub-configuration in a component carrier, UE shall use parameter simultaneousCSI-SubReportsPerCC-r18 in the component carrier; otherwise, UE shall use simultaneousCSI-ReportsPerCC in the component carrier. If UE is configured with at least one CSI reporting setting with sub-configuration in any component carrier, UE shall use simultaneousCSI-SubReportsAllCC-r18; otherwise, UE shall use simultaneousCSI-ReportsAllCC. If a UE supports simultaneous CSI calculations it is said to have CSI processing units for processing CSI reports. If L CPUs are occupied for calculation of CSI reports in a given OFDM symbol, the UE has unoccupied CPUs. If N CSI reports start occupying their respective CPUs on the same OFDM symbol on which CPUs are unoccupied, where each CSI report corresponds to , the UE is not required to update the requested CSI reports with lowest priority (according to Clause 5.2.5), where is the largest value such that holds. For CSI reports with reportQuantity set to ‘p-cri-r19’, ‘p-cri-RSRP-r19’, ‘p-ssb-index-r19’, or ‘p-ssb-index-RSRP-r19’, or CSI reports configured with the higher layer parameter [RRC_name-r19] csi-InferencePrediction-r19, is considered. For CSI reports with reportQuantity set to ‘p-cri-r19’, ‘p-cri-RSRP-r19’, ‘p-ssb-index-r19’, or ‘p-ssb-index-RSRP-r19’, and CSI reports configured with the higher layer parameter [RRC_name-r19] csi-InferencePrediction-r19, the UE may indicate a second value for the number of supported simultaneous CSI calculations with parameter SecondValuesSimultaneousCSI-ReportsPerCC in a component carrier, and SecondValuesSimultaneousCSI-ReportsAllCC across all component carriers, and if applicable, a third value for the number of supported simultaneous CSI calculations with parameter ThirdValuesSimultaneousCSI-ReportsPerCC in a component carrier, and ThirdValuesSimultaneousCSI-ReportsAllCC across all component carriers, in addition to . If a UE supports simultaneous CSI calculations it is said to have CSI processing units for processing CSI reports. If Lx CPUs are occupied for calculation of CSI reports in a given OFDM symbol, the UE has unoccupied CPUs. If CSI reports start occupying their respective CPUs on the same OFDM symbol on which CPUs are unoccupied, where each CSI report corresponds to , the UE is not required to update the requested CSI reports with lowest priority (according to Clause 5.2.5), where is the largest value such that holds. If only the second value is indicated, x = 2. If both of the second value and the third value are indicated, x = 2, 3 where the CSI reports with reportQuantity set to ‘p-cri-r19’, ‘p-cri-RSRP-r19’, ‘p-ssb-index-r19’, or ‘p-ssb-index-RSRP-r19’ corresponds to either x = 2 or x = 3 subject to UE capability and the CSI reports configured with the higher layer parameter [RRC_name-r19] csi-InferencePrediction-r19 corresponds to either x = 2 or x = 3 subject to UE capability. For CSI reports with reportQuantity set to ‘p-cri-r19’, ‘p-cri-RSRP-r19’, ‘p-ssb-index-r19’, or ‘p-ssb-index-RSRP-r19’, and CSI reports configured with the higher layer parameter [RRC_name-r19] csi-InferencePrediction-r19 if a CSI report is not considered within any of and , the values for and are considered to be 0, for the procedure previously described in this clause and the UE is not required to update the CSI report. A UE is not expected to be configured with an aperiodic CSI trigger state containing more than Reporting Settings. Processing of a CSI report occupies a number of CPUs for a number of symbols as follows: << Unchanged parts are omitted >> - and , for a CSI report configured with the higher layer parameter [RRC_name-r19] csi-InferencePrediction-r19, where the values of and are reported by UE capability. For a CSI report with CSI-ReportConfig with higher layer parameter reportQuantity not set to ‘none’, or a CSI report with LTM-CSI-ReportConfig, or reportQuantity not set to ‘none-bm-r19’ or ‘none-csi-r19’, the CPU(s) (including and/or , for CSI reports with reportQuantity set to ‘p-cri-r19’, ‘p-cri-RSRP-r19’, ‘p-ssb-index-r19’, or ‘p-ssb-index-RSRP-r19’, or ‘csi-pai-r19’, or ‘rs-pai-r19’, and CSI reports configured with the higher layer parameter [RRC_name-r19] csi-InferencePrediction-r19 are occupied for a number of OFDM symbols as follows: << Unchanged parts are omitted >> In any slot, the UE is not expected to have more active CSI-RS ports or active CSI-RS resources in active BWPs than reported as capability. NZP CSI-RS resource is active in a duration of time defined as follows. For aperiodic CSI-RS, (excluding the case in which the corresponding aperiodic CSI Reporting Setting is configured with the higher layer parameter [RRC_name-r19] csi-InferencePrediction-r19 and is linked to another aperiodic CSI Reporting Setting with reportQuantity-r19 set to ‘csi-pai-r19’), starting from the end of the PDCCH containing the request and ending at the end of the scheduled PUSCH containing the report associated with this aperiodic CSI-RS. When the PDCCH candidates are associated with a search space set configured with searchSpaceLinkingId, for the purpose of determining the NZP CSI-RS resource active duration, the PDCCH candidate that ends later in time among the two linked PDCCH candidates is used. For semi-persistent CSI-RS, starting from the end of when the activation command is applied, and ending at the end of when the deactivation command is applied. For periodic CSI-RS, starting when the periodic CSI-RS is configured by higher layer signalling, and ending when the periodic CSI-RS configuration is released. << Unchanged parts are omitted >> For aperiodic CSI-RS, when the corresponding aperiodic CSI Reporting Setting is configured with the higher layer parameter [RRC_name-r19] csi-InferencePrediction-r19 and is linked to another aperiodic CSI Reporting Setting with reportQuantity-r19 set to ‘csi-pai-r19’, NZP CSI-RS resource is active in a duration starting from the end of the PDCCH containing the request for the report of the corresponding CSI Reporting Setting and ending at the end of the scheduled PUSCH containing the report associated with the report of the linked CSI Reporting Setting. 5.4 UE CSI computation time << Unchanged parts are omitted >> , with of table 5.4-2, if the CSI report is configured with , codebookType is set to ‘typeII-Doppler-r18’ or ‘typeII-Doppler-PortSelection-r18’ and the corresponding NZP-CSI-RS-ResourceSet for channel measurement is aperiodic with CSI-RS resources, and is according to UE reported capability as defined in [13, TS 38.306] when the higher layer parameter [RRC_name-r19] csi-InferencePrediction-r19 is configured in CSI-ReportConfig, otherwise , or - , with of table 5.4-2, where or symbols, according to the reported UE capability, where the value of ∈{1,2,4} is indicated by UE capability, if the CSI report is configured with , codebookType is set to ‘typeII-Doppler-r18’ or ‘typeII-Doppler-PortSelection-r18’ and the corresponding NZP-CSI-RS-ResourceSet for channel measurement is periodic or semi-persistent with a single CSI-RS resource, and is according to UE reported capability as defined in [13, TS 38.306] when the higher layer parameter [RRC_name-r19] csi-InferencePrediction-r19 is configured in CSI-ReportConfig, otherwise , or - or , according to UE reported capability, with of table 5.4-2, if the CSI report is configured with , codebookType is set to ‘typeII-Doppler-r18’ and the corresponding NZP-CSI-RS-ResourceSet for channel measurement is aperiodic with CSI-RS resources, and is according to UE reported capability as defined in [13, TS 38.306] when the higher layer parameter [RRC_name-r19] csi-InferencePrediction-r19 is configured in CSI-ReportConfig, otherwise , or - or , according to UE reported capability, with of table 5.4-2, if the CSI report is configured with , codebookType is set to ‘typeII-Doppler-r18’ and the corresponding NZP-CSI-RS-ResourceSet for channel measurement is periodic or semi-persistent with a single CSI-RS resource, and is according to UE reported capability as defined in [13, TS 38.306] when the higher layer parameter [RRC_name-r19] csi-InferencePrediction-r19 is configured in CSI-ReportConfig, otherwise , or << Unchanged parts are omitted >> |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508062](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508062.zip) · `[122bis-R19-AI/ML]`

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#122bis:8.1:014` · 관련 주제: CSI 보고/codebook · 유지보수 (CR)

> Regarding the RAN2 LS from R1-2506715:
> For the UE-side candidate data collection configuration for CSI prediction, include the following IEs:
> - CSI-ResourceConfigId
> For candidate UE-side data collection, following IE(s) in addition to CSI-ResourceConfigId can be provided.
> - CodebookConfig-r18 set to ‘typeII-Doppler-r18’
> The draft response LS in R1-2508139 is endorsed. The Final LS is agreed in R1-2508140.

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508062](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508062.zip) · `[122bis-R19-AI/ML]`

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#122bis:8.1:015` · 관련 주제: CSI 보고/codebook · 유지보수 (CR)

구현 영향: 측정·보고량

> Support the configuration of following parameter in a CSI-ReportConfig with the higher layer parameter reportQuantity set to 'none-CSI-r19'
> - CodebookConfig-r18 set to ‘typeII-Doppler-r18’

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508142](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508142.zip) · `[122bis-R19-AI/ML]`

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122bis:9.1:006` · 관련 주제: CSI 보고/codebook · UE features (FG)

구현 영향: 처리 시간·CPU, UE capability·FG

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-0-1 | CSI report framework for UE-side inference | 1. Number of APU CPU,x pools N 2. Maximum number of APU CPU,x in each APU CPU,x pool of UE-sided inference for CSI report(s) for simultaneously in a CC 3. Maximum number of APU CPU,x in each APU CPU,x pool of UE-sided inference for CSI report(s) simultaneously across all CCs | FFS 2-35 | yes | n/a | Maximum number of APUs for UE-sided inference is unknown to the network | Per UE Per band and per BC | No n/a | No n/a | No n/a | Component 1 candidate values: {1,2} Component 2candidate values: {1…8} Component 3 candidate values: {1…32} Note: Component 2 and 3 candidate values are signalled separately for each pool [A UE that does not support this FG should not report non-zero occupied CPU,2 or CPU,3 values in any dependency FG reuses the CPU] | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508080](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508080.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122bis:9.1:007` · 관련 주제: Beam management · UE features (FG)

구현 영향: 포트·자원·레이어 수, 측정·보고량

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-1 | Increased number of reported RSs for beam management | 1. Support of reporting format for L1-RSRP measurements not including CRI/SSBRI other than one for the largest measured L1-RSRP in a reporting instance, if the number of reported L1-RSRPs is equal to the size of the measurement resource set. 2. Support of reporting format for L1-RSRPs and corresponding beam information of Top M beam(s) with largest M measured value(s) of L1-RSRP(s) of a measurement resource set, where M is configured by gNB, if the number of reported L1-RSRPs is smaller than the size of the measurement resource set 3. Maximum number of M reported RSs, M>4 | FFS {2-21, 2-22} or {2-23, 2-23a} or 2-29 or 2-24 | yes | n/a | Increased number of reported beams for beam management is not supported | Per UE Per band | No n/a | No n/a | No n/a | Component 3 candidate values: {6,8} | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508080](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508080.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122bis:9.1:008` · 관련 주제: CSI 보고/codebook, CSI-RS · UE features (FG)

구현 영향: 처리 시간·CPU, UE capability·FG, 포트·자원·레이어 수

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-2 | UE-side beam prediction for BM Case1 for inference | 1. Support of beam prediction with reporting of predicted beam index for BM-Case1 for inference with UE-side model 3. Maximum number of inference report(s) configured for BM-Case1 per BWP 3a. Maximum number of inference report(s) configured for BM-Case1 across all CCs 6. Support of SSB as RS type for Set B 6a. Support of CSI-RS as RS type for Set B 6b. Support of SSB as RS type for Set A 6c. Support of CSI-RS as RS type for Set A 7a: Supported maximum number of resources for Set B 7b: Supported maximum number of resources for Set A 8. Supported CSI-RS resource types for Set B 9. Supported inference report types 11. Supported BM-Case 1 sub-usecase(s): {setB-subset-of-setA, setB-different-from-setA, both}] 12. Supported maximum number of predicted beams in each reporting instance FFS: whether/how to merge this FG with other FG(s) for performance monitoring and/or data collection 13. Supported number of occupied CPU 14. Supported number of occupied APU CPU,2/CPU,3 15. Supported value of d for the relaxation of Z3 timeline 16. Supported value of d’ for the relaxation of Z’3 timeline 17. Index of the Occupied APU resource pool between CPU,2 and CPU,3 | FFS 2-35 | yes | n/a | UE-sided beam prediction for BM Case 1 for inference is not supported | Per UE Per band | No n/a | No n/a | No n/a | Component 3 candidate values: Periodic reporting: {1, 2, 3, 4} Aperiodic reporting: {1, 2, 3, 4} Semi-persistent reporting: {1, 2, 3, 4} Component 3a candidate values: {1, 2, 3, 4, 8, 10, 12, 16} Component 7a candidate values: {4, 8, 16} Component 7b candidate values: {8, 16, 32, 64} Component 8 candidate values: {Periodic CSI-RS, Semi-persistent CSI-RS, Aperiodic CSI-RS} Component 9 candidate values: {Periodic CSI report, Aperiodic CSI report, semi-persistent CSI report} Component 11 candidate values: {setB-subset-of-setA, setB-different-from-setA, both} Component 12 candidate values: {1, 2, 3, 4} Component 13 candidate values: {0, 1, 2, …, 8} Component 14 candidate values: {0, 1, 2, …, 8} Note: The values of component 13 and 14 are not allowed to be 0 simultaneously Component 15 candidate values: FFS Component 16 candidate values: FFS Component 17 candidate values: {1, 2} representing the first APU pool (i.e., CPU,2) and the second APU pool (i.e., CPU,3), respectively Note: “CPU” corresponds to “CPU,1” in TS 38.214, and “APU” corresponds to “CPU,x” in TS 38.214, x = 2, 3 FFS: candidate values for components | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508080](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508080.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122bis:9.1:009` · UE features (FG)

구현 영향: 포트·자원·레이어 수

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-3 | UE-side beam prediction for BM Case1 with predicted RSRP for inference | 1. Support of beam prediction, reporting of predicted beam index and predicted RSRP, for BM-Case1 for inference 2. Supported maximum number of predicted beams with RSRP in each reporting instance | 58-1-2 | yes | n/a | UE-side beam prediction for BM Case 1 with predicted RSRP for inference is not supported | Per UE Per band | No n/a | No n/a | No n/a | Component 2 candidate values: {1, 2, 3, 4} | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508080](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508080.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122bis:9.1:010` · 관련 주제: CSI 보고/codebook, CSI-RS · UE features (FG)

구현 영향: 처리 시간·CPU, UE capability·FG, 포트·자원·레이어 수

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-4 | UE-side beam prediction for BM Case2 for inference | 1. Support of beam prediction with reporting of predicted beam index for BM-Case2 for inference with UE-side model 3. Maximum number of inference report(s) configured for BM-Case2 per BWP 3a. Maximum number of inference report(s) configured for BM-Case2 across all CCs 6. Support of SSB as RS type for Set B 6a. Support of CSI-RS as RS type for Set B 6b. Support of SSB as RS type for Set A 6c. Support of CSI-RS as RS type for Set A 7a: Supported maximum number of resources for Set B 7b: Supported maximum number of resources for Set A 8. Supported CSI-RS resource types for Set B 9. Supported inference report types 11. Supported maximum number of predicted beams in each predicted time instance 12. Supported maximum number of predicted time instances 13. Supported maximum total number of reported predicted beams for predicted time instances in one report 14. Supported combinations of supported value(s) of valid time duration for each predicted time instance and number of predicted beams for each value of valid time duration 15. Supported value(s) of time gap between predicted time instances and between reference time to the first future time instance 21. supported number of occupied CPU 22. supported number of occupied APU CPU,2/CPU,3 23. supported value of d for the relaxation of Z3 timeline 24. supported value of d’ for the relaxation of Z’3 timeline 25. Index of the Occupied APU resource pool between CPU,2 and CPU,3 | FFS 2-35 | yes | n/a | UE-side beam prediction for BM-Case2 for inference is not supported | Per UE Per band | No n/a | No n/a | No n/a | Component 3 candidate values: Periodic reporting: {1, 2, 3, 4} Aperiodic reporting: {1, 2, 3, 4} Semi-persistent reporting: {1, 2, 3, 4} Component 3a candidate values: {1, 2, 3, 4, 8, 10, 12, 16} Component 7a candidate values: {4, 8, 16, 32, 64} Component 7b candidate values: {4, 8, 16, 32, 64} Component 8 candidate values: {Periodic CSI-RS, Semi-persistent CSI-RS} Component 9 candidate values: {Periodic CSI report, Aperiodic CSI report, semi-persistent CSI report}FFS: candidate values for components Component 11 candidate values: {1, 2, 3, 4} Component 12 candidate values: {1, 2, 4, 8} Component 13 candidate values: {1, 2, 4, 6, 8, 12, 16, 32} Component 15 candidate values: {10ms, 20ms, 40ms, 80ms, 160ms} Component 21 candidate values: {0, 1, 2, … 8} Component 22 candidate values: {0, 1, 2, … 8} Note: The values of component 21 and 22 are not allowed to be 0 simultaneously. Component 23 candidate values: FFS Component 24 candidate values: FFS Component 25 candidate values: {1, 2} representing the first APU pool (i.e., CPU,2) and the second APU pool (i.e., CPU,3), respectively Note: “CPU” corresponds to “CPU,1” in TS 38.214, and “APU” corresponds to “CPU,x” in TS 38.214, x = 2, 3 Note: UE should not report non-zero value for Component 22 if FG 58-0-1 is not signalled | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508080](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508080.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122bis:9.1:011` · UE features (FG)

구현 영향: 포트·자원·레이어 수

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-5 | UE-side beam prediction for BM-Case2 with predicted RSRP for inference | 1. Support of beam prediction, reporting of predicted beams and predicted RSRP, for BM-Case2 (spatial and time domain beam prediction) for inference 2. Supported maximum number of predicted beams in each predicted time instance 3. Supported maximum number of predicted time instances 4. Supported maximum total number of reported predicted beams for predicted time instances in one report | 58-1-4 | yes | n/a | UE-side beam prediction for BM-Case2 for inference is not supported | Per UE Per band | No n/a | No n/a | No n/a | Component 2 candidate values: {1, 2, 3, 4} Component 3 candidate values: {1, 2, 4, 8} Component 4 candidate values: {1, 2, 3, 4, 8, 12, 16, 32} | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508080](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508080.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122bis:9.1:012` · 관련 주제: CSI 보고/codebook, CSI-RS · UE features (FG)

구현 영향: 포트·자원·레이어 수

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-6 | Performance monitoring for UE-sided model | 1. Support of performance monitoring with RS-PAI of AI/ML model for beam prediction. 2. Maximum total number of the configured SSB resources and/or CSI-RS resources for monitoring RS resource set 3. Maximum number of monitoring report(s) configured per BWP 4. Maximum number of monitoring report(s) configured across all CCs 5. Maximum number of monitoring occasions for RS-PAI calculation 6. Support of SSB as RS type for monitoring 7. Support of CSI-RS as RS type for monitoring 8. Supported monitoring resource types 9. Supported monitoring report types | FFS 58-1-2 or 58-1-4 | yes | n/a | Performance monitoring for UE-sided model is not supported | FFS Per band | FFS n/a | FFS n/a | FFS n/a | Component 2 candidate values: {4, 8, 16, 32, 64} Component 3 candidate values: Periodic reporting: {1, 2, 3, 4,} Aperiodic reporting: {1, 2, 3, 4} Semi-persistent reporting: {1, 2, 3, 4} Component 4 candidate values: {1, 2, 4, 8} Component 5 candidate values: {1, 3, 7, 15} Component 8 candidate values: {Periodic CSI-RS, Semi-persistent CSI-RS} Component 9 candidate values: {Periodic CSI report, Aperiodic CSI report, semi-persistent CSI report} FFS: candidate values for components | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508080](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508080.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122bis:9.1:013` · 관련 주제: CSI-RS · UE features (FG)

구현 영향: UE capability·FG, 포트·자원·레이어 수

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-7 | Data collection for UE-side beam prediction | 1. Support of data collection for UE-side beam prediction 2. Support of SS/PBCH block and 1-port CSI-RS based RSRP measurements for measurement RS resource sets (Set B and Set A) for data collection 3. Supported sub-use cases 6: Supported maximum number of resources for Set B 7: Supported maximum number of resources for Set A 8. Support of SSB as RS type for Set B 9. Support of CSI-RS as RS type for Set B 10. Support of SSB as RS type for Set A 11. Support of CSI-RS as RS type for Set A | FFS 2-35 | yes | n/a | Data collection for UE-side beam prediction is not supported | Per UE Per band | No n/a | No n/a | No n/a | Component 3 candidate values: {‘Set B equal to Set A’, ‘Set B subset of Set A’,’Set B not a subset of Set A’} Component 6 candidate values: {4, 8, 16, 32, 64} Component 7 candidate values: {8, 16, 32, 64} Note: it is up to RAN2 whether this FG is merged into data collection FG defined by RAN2 | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508080](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508080.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122bis:9.1:014` · 관련 주제: CSI 보고/codebook · UE features (FG)

구현 영향: 처리 시간·CPU, UE capability·FG, 포트·자원·레이어 수, 측정·보고량

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_Air | 58-3-1 | CSI prediction for UE-sided inference when N4=1 | 1. Support of CSI prediction for UE-sided inference when N4=1 2. Support for reporting predicted PMI with N4=1 3. A list of supported combinations, each combination is { Max # of Tx ports in one resource, Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 4. Support of Rel-16 eType-II regular codebook refinement for predicted PMI with PMI subband R=1 5. Support parameter combinations with L=2,4 6. Support for rank = 1,2 7. Support for the size of DD-basis, N4=1 8. Support X=1 CQI based on the first/earliest slot of the CSI reporting window and the first/earliest predicted PMI (TDCQI=’1-1’) 11. Scaling factor for active resource counting Kp 12. supported value of t for the relaxation of Z and Z’ timeline 13. supported number of occupied CPU 14. supported number of occupied APU CPU,2/CPU,3 15. Index of the Occupied APU resource pool between CPU,2 and CPU,3 | 58-0-1 2-35 | yes | n/a | CSI prediction for N4=1 for inference is not supported | Per band and Per BC | n/a | n/a | n/a | Component 3 candidate values: a. {4,8,12,16,24,32} b. {2,3,4 … 64} c. {4, …, 256} Component 11 candidate values: {1,2,4} Component 12 candidate values: FFS Component 13 candidate values: {0, 1, 2, … 8} Component 14 candidate values: {0, 1, 2, … 8} Component 15 candidate values: {1, 2} representing the first APU pool (i.e., CPU,2) and the second APU pool (i.e., CPU,3), respectively. Note: “CPU” corresponds to “CPU,1” in TS 38.214, and “APU” corresponds to “CPU,x” in TS 38.214, x = 2, 3 Note: UE should not report non-zero value for Component 14 if FG 58-0-1 is not signaled | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508080](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508080.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122bis:9.1:015` · 관련 주제: CSI 보고/codebook, CSI-RS · UE features (FG)

구현 영향: 처리 시간·CPU, UE capability·FG, 포트·자원·레이어 수, 측정·보고량

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_Air | 58-3-2 | CSI prediction for UE-sided inference when N4>1 | 1. Support of CSI prediction for UE-sided inference when N4>1 2. Support for reporting predicted PMI with N4>1 3. A list of supported combinations, each combination is {Max N4, Max # of Tx ports in one resource, Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 4. Value of d=m for the DD unit size when A-CSI-RS is configured for CMR 5. Support for the size of DD-basis, N4>1 6. A list of supported combinations, each combination is {Max N4, Max # of Tx ports in one resource, Max # of resources and total # of Tx ports} for one CSI report setting 7. Supported number of occupied CPU 8. Supported number of occupied APU CPU,2/CPU,3 9. Index of the Occupied APU resource pool between CPU,2 and CPU,3 | 58-3-1 | yes | n/a | CSI prediction for N4>1 for inference is not supported | Per band and Per BC | N/A | N/A | N/A | Component 3 candidate values: a. {1,2,4,8} b. {4,8,12,16,24,32} c. {2,3,4 … 64} d. {4, …, 256} Component 6 candidate values: a. {1,2,4,8} b. {4,8,12,16,24,32} c. {4,8,12} d.{4, …, 256} Component 7 candidate values: {0, 1, 2, …8} Component 8 candidate values: {0, 1, 2, … 8} Component 9 candidate values: {1, 2} representing the first APU pool (i.e., CPU,2) and the second APU pool (i.e., CPU,3), respectively Note: “CPU” corresponds to “CPU,1” in TS 38.214, and “APU” corresponds to “CPU,x” in TS 38.214, x = 2, 3 Note: UE should not report non-zero value for Component 8 if FG 58-0-1 is not signalled | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508080](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508080.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122bis:9.1:016` · 관련 주제: CSI 보고/codebook · UE features (FG)

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_Air | 58-3-4 | UE side data collection for CSI prediction | 1. Support of data collection for CSI prediction | FFS 2-35 | yes | n/a | UE side data collection for CSI prediction is not supported | Per band and Per BC | N/A | N/A | N/A |  | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508080](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508080.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122bis:9.1:017` · 관련 주제: CSI 보고/codebook · UE features (FG)

구현 영향: 처리 시간·CPU, 포트·자원·레이어 수

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_Air | 58-3-5 | Performance monitoring for CSI prediction model | 1. Support of two performance metric SGCS 2. Support of one wideband frequency granularity SGCS per layer 3. Support of one configured time instance for N4>1 4. A list of supported combinations, each combination is {Max # of Tx ports in one resource, Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 5. Supported number of occupied CPU | 58-3-1 | Yes | n/a | Performance monitoring for CSI prediction model is not supported | Per Band and Per BC | N/A | N/A | N/A | Component 4 candidate values: - Maximum 16 triplets - Max # of Tx ports in one resource: {4,8,12,16,24,32} - Max # resources: {1 to 64} - Max # total ports: {4 to 256} Component 5 candidate values: {1, 2} Note: The summation of the value reported by Component 5 and the one reported by Component 13 of FG58-3-1 (or Component 7 of FG58-3-2) should not significant than the N_CPU UE reported | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508080](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508080.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122bis:9.1:018` · 관련 주제: CSI 보고/codebook · UE features (FG)

구현 영향: 처리 시간·CPU, UE capability·FG

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-0-1 | CSI report framework for UE-side inference | 1. Number of CPU,x pools N 2. Maximum number of CPU,x in each CPU,x pool of UE-sided inference for CSI report(s) for simultaneously in a CC 3. Maximum number of CPU,x in each CPU,x pool of UE-sided inference for CSI report(s) simultaneously across all CCs | 2-35 | yes | n/a | Maximum number of APU CPU,x for UE-sided inference is unknown to the network | Per band and per BC | n/a | n/a | n/a | Component 1 candidate values: {1,2} Component 2candidate values: {1…8} Component 3 candidate values: {1…32} Note: Component 2 and 3 candidate values are signalled separately for each pool A UE that does not support this FG should not report non-zero occupied CPU,2 or CPU,3 values in any dependency FG | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508080](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508080.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122bis:9.1:019` · 관련 주제: CSI 보고/codebook · UE features (FG)

구현 영향: 처리 시간·CPU, UE capability·FG

> In FG 58-1-2, 58-1-4, 58-3-1, 58-3-2, in the Notes column, delete the following note: “CPU” corresponds to “CPU,1” in TS 38.214, and “APU” corresponds to “CPU,x” in TS 38.214, x = 2, 3

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508080](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508080.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122bis:9.1:020` · 관련 주제: CSI 보고/codebook · UE features (FG)

구현 영향: 처리 시간·CPU, UE capability·FG

> In FG 58-1-2, 58-1-4, in the notes column, for component 17 candidate values, replace “APU pool” with “CPU pool”

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508080](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508080.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122bis:9.1:021` · 관련 주제: CSI 보고/codebook · UE features (FG)

구현 영향: 처리 시간·CPU, UE capability·FG

> In FGs 58-1-2, 58-1-4, 58-3-1, 58-3-2, in the notes column, replace “APU pool” with “CPU pool”

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508080](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508080.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122bis:9.1:022` · 관련 주제: CSI 보고/codebook, CSI-RS · UE features (FG)

구현 영향: 처리 시간·CPU, 포트·자원·레이어 수

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-2 | UE-side beam prediction for BM Case1 for inference | 1. Support of beam prediction with reporting of predicted beam index for BM-Case1 for inference with UE-side model 3. Maximum number of inference report(s) configured for BM-Case1 per BWP 3a. Maximum number of inference report(s) configured for BM-Case1 across all CCs 6. Support of SSB as RS type for Set B 6a. Support of CSI-RS as RS type for Set B 6b. Support of SSB as RS type for Set A 6c. Support of CSI-RS as RS type for Set A 7a: Supported maximum number of resources for Set B 7b: Supported maximum number of resources for Set A 8. Supported CSI-RS resource types for Set B 9. Supported inference report types 11. Supported BM-Case 1 sub-usecase(s) 12. Supported maximum number of predicted beams in each reporting instance 13. Supported number of occupied CPU 14. Supported number of occupied CPU,2/CPU,3 15. Supported value of d for the relaxation of Z3 timeline, where i is the index of SCS, i=1,2,3,4,5,6 corresponding to 15,30,60,120,480,960 kHz SCS 16. Supported value of d’ for the relaxation of Z’3 timeline, where i is the index of SCS, i=1,2,3,4,5,6 corresponding to 15,30,60,120,480,960 kHz SCS 17. Occupied resource pool between CPU,2 and CPU,3 | 2-35 | yes | n/a | UE-sided beam prediction for BM Case 1 for inference is not supported | Per band | n/a | n/a | n/a | Component 3 candidate values: Periodic reporting: {1, 2, 3, 4} Aperiodic reporting: {1, 2, 3, 4} Semi-persistent reporting: {1, 2, 3, 4} Component 3a candidate values: {1, 2, 3, 4, 8, 10, 12, 16} Component 7a candidate values: {4, 8, 16} Component 7b candidate values: {8, 16, 32, 64} Component 8 candidate values: {Periodic CSI-RS, Semi-persistent CSI-RS, Aperiodic CSI-RS} Component 9 candidate values: {Periodic CSI report, Aperiodic CSI report, semi-persistent CSI report} Component 11 candidate values: {setB-subset-of-setA, setB-different-from-setA, both} Component 12 candidate values: {1, 2, 3, 4} Component 13 candidate values: {0, 1, 2, …, 8} Component 14 candidate values: {0, 1, 2, …, 8} Note: The values of component 13 and 14 are not allowed to be 0 simultaneously Component 15 candidate values: d1 is FFS d2 is FFS d3 is FFS d4 is FFS d5 is FFS d6 is FFS Component 16 candidate values: d'1 is FFS d’2 is FFS d’3 is FFS d’4 is FFS d’5 is FFS d’6 is FFS Component 17 candidate values: {1, 2} representing the first APU pool (i.e., CPU,2) and the second APU pool (i.e., CPU,3), respectively Note: “CPU” corresponds to “CPU,1” in TS 38.214, and “APU” corresponds to “CPU,x” in TS 38.214, x = 2, 3 | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508080](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508080.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122bis:9.1:023` · 관련 주제: CSI 보고/codebook, CSI-RS · UE features (FG)

구현 영향: 처리 시간·CPU, UE capability·FG, 포트·자원·레이어 수

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-4 | UE-side beam prediction for BM Case2 for inference | 1. Support of beam prediction with reporting of predicted beam index for BM-Case2 for inference with UE-side model 3. Maximum number of inference report(s) configured for BM-Case2 per BWP 3a. Maximum number of inference report(s) configured for BM-Case2 across all CCs 6. Support of SSB as RS type for Set B 6a. Support of CSI-RS as RS type for Set B 6b. Support of SSB as RS type for Set A 6c. Support of CSI-RS as RS type for Set A 7a: Supported maximum number of resources for Set B 7b: Supported maximum number of resources for Set A 8. Supported CSI-RS resource types for Set B 9. Supported inference report types 11. Supported maximum number of predicted beams in each predicted time instance 12. Supported maximum number of predicted time instances 13. Supported maximum total number of reported predicted beams for predicted time instances in one report 15. Supported value(s) of time gap between predicted time instances and between reference time to the first future time instance 21. supported number of occupied CPU 22. supported number of occupied CPU,2/CPU,3 23. supported value of d for the relaxation of Z3 timeline, where i is the index of SCS, i=1,2,3,4,5,6 corresponding to 15,30,60,120,480,960 kHz SCS 24. supported value of d’ for the relaxation of Z’3 timeline, where i is the index of SCS, i=1,2,3,4,5,6 corresponding to 15,30,60,120,480,960 kHz SCS 25. Occupied resource pool between CPU,2 and CPU,3 | 2-35 | yes | n/a | UE-side beam prediction for BM-Case2 for inference is not supported | Per band | n/a | n/a | n/a | Component 3 candidate values: Periodic reporting: {1, 2, 3, 4} Aperiodic reporting: {1, 2, 3, 4} Semi-persistent reporting: {1, 2, 3, 4} Component 3a candidate values: {1, 2, 3, 4, 8, 10, 12, 16} Component 7a candidate values: {4, 8, 16, 32, 64} Component 7b candidate values: {4, 8, 16, 32, 64} Component 8 candidate values: {Periodic CSI-RS, Semi-persistent CSI-RS} Component 9 candidate values: {Periodic CSI report, Aperiodic CSI report, semi-persistent CSI report} Component 11 candidate values: {1, 2, 3, 4} Component 12 candidate values: {1, 2, 4, 8} Component 13 candidate values: {1, 2, 4, 6, 8, 12, 16, 32} Component 15 candidate values: {10ms, 20ms, 40ms, 80ms, 160ms} Component 21 candidate values: {0, 1, 2, … 8} Component 22 candidate values: {0, 1, 2, … 8} Note: The values of component 21 and 22 are not allowed to be 0 simultaneously. Component 23 candidate values: d1 is FFS d2 is FFS d3 is FFS d4 is FFS d5 is FFS d6 is FFS Component 24 candidate values: d'1 is FFS d’2 is FFS d’3 is FFS d’4 is FFS d’5 is FFS d’6 is FFS Component 25 candidate values: {1, 2} representing the first APU pool (i.e., CPU,2) and the second APU pool (i.e., CPU,3), respectively Note: “CPU” corresponds to “CPU,1” in TS 38.214, and “APU” corresponds to “CPU,x” in TS 38.214, x = 2, 3 Note: UE should not report non-zero value for Component 22 if FG 58-0-1 is not signalled | Optional with capability signalling |

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508080](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508080.zip)

**Agreement** · `10.1.1.1` Inference related aspects · `RAN1#122bis:10.1.1.1:001` · 관련 주제: CSI 보고/codebook, CSI-RS · 규격 작업 (WI)

구현 영향: 측정·보고량

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> Support precoding matrix with port-subband domain representation as target CSI type.
> - For a certain layer , a precoding matrix on N_sb subband and P CSI-RS ports is  with  being a  vector.
> - Note: Only sub-band PMI reporting is supported.

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508021](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508021.zip)

**Agreement** · `10.1.1.1` Inference related aspects · `RAN1#122bis:10.1.1.1:002` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> For determining the payload parameters combinations  or   across all layers and ranks, consider following general principles for precoding matrix-based target CSI
> - Rank-common and layer-common model with payload-scalable design is considered as the baseline implementation for discussion purpose.
>   - Note: layer-specific / rank-specific (if supported) payload parameters are supported by this rank-common and layer-common model with payload-scalable design.
> - Limiting the total number of (per-layer) payload parameters combinations  or   across all layers and all ranks.
> - At least for medium to high per-layer payload regime, the total payload size of rank 2, rank 3 and 4 are comparable to each other.
> - Spectral efficiency or system throughput and trade-off with feedback overhead are considered as the performance metric.

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508021](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508021.zip)

**Agreement** · `10.1.1.1` Inference related aspects · `RAN1#122bis:10.1.1.1:003` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

구현 영향: 메모리·복잡도

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> When the Target CSI is precoder matrix, in order to down-select to N per-layer payload parameter combinations (PC) of  or  based on performance, overhead and complexity trade-off results, consider the following candidate values:
> - Candiate values for : 32, 64, 96, 128, 192
> - Candidate values for : 1, 2, 3, 4, (8, 10 only for VQ)
>   - 2 is considered as the baseline assumption for SQ.
> - Candidate values for L: L=2, 4,
> - Candidate values for N: 4, 5, 6
> - Note: These N payload PCs of  or  are considered as the pool for the payload PC for each layer and each rank.
> - Note: The above is for discussion purpose, how to configure the PCs (across layers and ranks) is a separate discussion.
> - Note: Rank-common and layer-common model with payload scalable design is considered.
> - Note: The above does not mean support of both SQ and VQ.
> - Note: The number of parameters combinations configurations (Y) does not exceed 8.

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508022](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508022.zip)

**Agreement** · `10.1.1.1` Inference related aspects · `RAN1#122bis:10.1.1.1:004` · 규격 작업 (WI)

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> For payload parameter combinations (PC), consider followings
> - Support Y configurable PCs (across layers and ranks) as below, where X_n, Xn_31, Xn_32, Xn_33, Xn_41, Xn_42, Xn_43, Xn_44 represent a pair of  or a triplet of   chosen from the per-layer PC pool.
> |  | Rank1 | Rank2 | Rank3 | Rank4 |
> | PC1 | X1 | X1, X1 | X1_31, X1_32, X1_33 | X1_41, X1_42, X1_43, X1_44 |
> | PC2 | X2 | X2, X2 | X2_31, X2_32, X2_33 | X2_41, X2_42, X2_43, X2_44 |
> | … |  |  |  |  |
> - For rank 1 and rank 2, layer-common and rank-common payload is supported.
> - For rank 3, consider alternatives of {Xn_31, Xn_32, Xn_33} = {a, a, a}, {a, a, b}, {a, b, b} for potential down selection.
> - For rank 4, consider alternatives of {Xn_41, Xn_42, Xn_43, Xn_44} = {a, a, a, a}, {a, a, b, b}, {a, b, b, c}, {a, a, b, c} or {a, b, c, c} for potential down selection.
> - Note: The table is for discussion purpose, how to configure the PCs (across layers and ranks) is a separate discussion.
> - Note: a, b values in rank3 can be different from that in rank 4.

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508022](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508022.zip)

**Agreement** · `10.1.1.1` Inference related aspects · `RAN1#122bis:10.1.1.1:005` · 규격 작업 (WI)

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> Consider following for evaluation:
> - For down-selection of per-layer pairs of  or a triplets of  , average SGCS across per layer can be considered as performance metric.
> - For down-selection of the rank-specific and layer-specific patterns (e.g., {Xn_31, Xn_32, Xn_33} and {Xn_41, Xn_42, Xn_43, Xn_44}), spectral efficiency or throughput should be considered.

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508023](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508023.zip)

**Agreement** · `10.1.1.1` Inference related aspects · `RAN1#122bis:10.1.1.1:006` · 관련 주제: CSI 보고/codebook, CSI-RS · 규격 작업 (WI)

> For CSI feedback via two-sided AIML models, reuse legacy CSI reporting framework
> - Support CSI report based on periodic, semi-persistent and aperiodic CSI-RS resources with legacy measurement resource configurations.
> - Support aperiodic report and semi-persistent CSI report on PUSCH and reuse legacy triggering mechanism.

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508023](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508023.zip)

**Agreement** · `10.1.1.2` Other aspects · `RAN1#122bis:10.1.1.2:001` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> For NW side data collection with higher layer reporting, for further study of Option 1 (scalar quantization), consider the following definition for evaluation:
> - Content: for a number of S=1 (as baseline) Target CSI samples each with the dimensions of 2N1N2 ports, N3 subbands, v layers for precoding matrix, and real+imaginary (or amplitude+phase) parts, which has overall 2N1N2*N3*v complex elements, and any complex element has a real (or amplitude) part of x1 and an imaginary (or phase) part of x2.
>   - Note: Companies to report whether  real value and imaginary value are quantized, or amplitude value and phase value are quantized.
> - Format: x1 is quantized to k1 bits within range of [T1min, T1max], and x2 is quantized to k2 bits within range of [T2min, T2max]. E.g., for Scalar8, k1=8 bits for quantizing the real part, and k2=8 bits for quantizing the imaginary part. Uniform quantization is assumed.
>   - Note: Companies to report whether/how the normalization is performed, and whether it is normalized within or across 2N1N2 ports/ N3 subbands/ v layers/ real and imaginary (or amplitude and phase) parts.
> - Fixed parameter values of k1/k2/T1min/T1max/T2min/T2max across complex elements, as a baseline for evaluations. Companies to report the values.
> - Note: It is up to company to use number of samples S>1 in their evaluations. In this case, companies need to provide information how S samples are quantized in their evaluation.

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508028](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508028.zip)

**Agreement** · `10.1.1.2` Other aspects · `RAN1#122bis:10.1.1.2:002` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> For NW side data collection with higher layer reporting, regarding Option 4 (eType II like codebook with new parameter), further study the following candidate enhanced parameter values with potential down selection.
> - L= 4/6/12/16/(N1*N2), pv=0.6/0.75/1, Beta = 0.5/0.8/1. Reference amplitude = 4bits/6bits, differential amplitude = 3bits/4bits, and phase = 4bits/6bits
>   - Company to report the quantization step for reference amplitude for 6bits.
> - No restriction to the total number of non-zero coefficients for a specific rank.
> - Other combinations can be considered and reported by companies.

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508030](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508030.zip)

**Agreement** · `10.1.1.2` Other aspects · `RAN1#122bis:10.1.1.2:003` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

구현 영향: 처리 시간·CPU, 메모리·복잡도

> For the study of NW side data collection with higher layer reporting, following evaluation assumptions are considered:
> - Benchmark#1: FP32 (k1=k2=32 bits)
> - Benchmark#2: legacy eType II with PC6 (for layer 1/2/3/4), PC8(for layer 1/2)
> - CSI payload size: at least consider large CSI payload Z ≥ 230 bits per layer, optionally consider low/medium CSI payload size X/Y per layer.
> - Tx port: 32, 64, or 128 up to companies.
> - Subband number: 13, or 19 up to companies.
> - Performance metric:
>   - Metric#1: SGCS for specific layer(s) between Target CSI of FP32 and recovery CSI, for a model trained with quantized Target CSI with a specific quantization option.
>   - Metric#2: SGCS for specific layer(s) between the Target CSI of FP32 with its quantized version subject to a specific quantization solution
>   - Overhead per sample and per layer SGCS results are reported per layer
> - Note: Complexity should be analysed.
> - For Option 1, consider k1+k2=4, 6 ,7, 8, 16, 32
> - Other assumptions follow R18 study EVM

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508030](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508030.zip)

**Agreement** · `10.1.1.2` Other aspects · `RAN1#122bis:10.1.1.2:004` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

구현 영향: 처리 시간·CPU

> For CPU counting of UE side data collection,
> - OCPU=1
> - FFS: The CPU occupancy duration

FFS 1줄

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2508031](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2508031.zip)

**Conclusion** · `10.1.2` Inter-vendor training collaboration for two-sided AI/ML models · `RAN1#122bis:10.1.2:001` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> For Option 4-1 under Direction A in AI/ML based CSI compression, there is no consensus to further study the necessity of sharing assisted information to align model design aspects.

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2507666](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2507666.zip)

**Agreement** · `10.1.2` Inter-vendor training collaboration for two-sided AI/ML models · `RAN1#122bis:10.1.2:002` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> - For Option 4-1 under Direction A in AI/ML based CSI compression, both average SGCS and average NMSE as performance target in the exchanged dataset are supported. Both average SGCS and average NMSE are provided.
>   - NW side can optionally send NMSE and/or SGCS values at X-percentiles.

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2507666](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2507666.zip)

**Agreement** · `10.1.2` Inter-vendor training collaboration for two-sided AI/ML models · `RAN1#122bis:10.1.2:003` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

구현 영향: 포트·자원·레이어 수

> For Option 4-1 under Direction A in AI/ML based CSI compression, for the association between target CSI and CSI feedback in the exchanged dataset.
> - Support 1:M mapping between one target CSI sample/set of samples to M CSI feedback samples/sets of samples associated with different CSI payload size configurations
> - FFS: Association between Target CSI and CSI feedback, including scalability related information for different number of Tx port, sub bands related information.
> - FFS: Whether/how Target CSI samples/set of samples within an exchanged dataset, with different Tx port and sub-band related information are organized.
> - FFS: Whether the Target CSI is per layer or per rank when Target CSI is precoder matrix.
> - FFS: Whether and how to support CSI feedback structure with different payload scalability options
> - FFS: Other details

FFS 5줄

출처: [Chair notes RAN1#122b eom4](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Inbox/Chair_Notes/Chair%20notes%20RAN1%23122b%20eom4.docx) · [R1-2507668](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122b/Docs/R1-2507668.zip)

## RAN1#122 — 58건

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#122:8.1:001` · 유지보수 (CR)

> ⚠️ 실제 변경 내용은 TDoc에 있습니다.

> TP included in R1-250xxxx for TR 38.843 is endorsed in principle.
> Corresponding CR in R1-2506677 for TR 38.843 is endorsed.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · `[122-R19-AI/ML]`

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#122:8.1:002` · 관련 주제: CSI 보고/codebook · 유지보수 (CR)

규격: TS 38.214 5.2.1.6

> Adopt the following TP in section 5.2.1.6, TS 38.214.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506557](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506557.zip) · `[122-R19-AI/ML]`

**Agreement** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#122:8.1:003` · 유지보수 (CR)

> ⚠️ 실제 변경 내용은 TDoc에 있습니다.

> The Draft CR in R1-2506171 for TR 38.843 is endorsed.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506171](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506171.zip) · `[122-R19-AI/ML]`

**Agreement** · `8.1.1` Specification support for beam management · `RAN1#122:8.1.1:001` · 관련 주제: Beam management, CSI 보고/codebook, CSI-RS · 유지보수 (CR)

구현 영향: 측정·보고량 · 규격: TS 38.214 5.2.1.4.3

> Adopt the following TP for the clarification of ranking information.
> Reason for change: The description of ranking information for P-CRIs or P-SSBRIs is unclear.
> Summary of change: Clarify that the ranking information is for P-CRIs or P-SSBRIs.
> Consequences if not approved: UE cannot generate the ranking information.
> | TP for TS 38.214 Clause 5.2.1.4.3a P-CRI, P-SSBRI, and P-L1-RSRP reporting <omitted texts> For a CSI-ReportConfig with reportQuantity-r19 set to 'p-cri-r19', 'p-cri-RSRP-r19', 'p-ssb-index-r19' or 'p-ssb-index-RSRP-r19', if nroftimeinstance-r19 is configured, the UE is configured with TimeGap-r19 indicating a time gap between a reference time and the earliest time instance of nroftimeinstance-r19 time instance(s) (defined in slot(s)). If nroftimeinstance-r19 is greater than 1, the same time gap is considered between two consecutive time instances. The UE considers the reference time to be the slot of the latest one of each CSI-RS/SSB resource, for channel measurement, respective latest CSI-RS/SSB transmission occasion no later than the corresponding CSI reference resource of the CSI report. For P-CRI or P-SSBRI reporting without P-L1-RSRP, the ranking information of the nrofreportedpredictedrs-r19 P-CRIs or P-SSBRIs (per time instance, if nroftimeinstance-r19 is configured) is conveyed by the order of the P-CRIs or P-SSBRIs reported in the CSI report, where the first reported P-CRI or P-SSBRI ranks first. <omitted texts> |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506451](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506451.zip)

**Agreement** · `8.1.1` Specification support for beam management · `RAN1#122:8.1.1:002` · 관련 주제: CSI 보고/codebook, CSI-RS · 유지보수 (CR)

구현 영향: 측정·보고량 · 규격: TS 38.214 5.2.1.4.3

> Adopt the following TP for CSI reporting for monitoring.
> Reason for change: The condition associated with CSI reporting for RS-PAI is unclear.
> Summary of change: Clarify that the timeinstanceformonitoring-r19-th time instance is used in case of BM-Case2 for condition check. Adding the description on resource mapping methods depending on the size of the set for monitoring is smaller than or the same as the size of Set A.
> Consequences if not approved: gNB and UE may have different understanding on the condition associated with CSI reporting for RS-PAI.
> | TP for TS 38.214 Clause 5.2.1.4.3b RS-PAI Reporting 5.2.1.4.3b RS-PAI Reporting <omitted texts> - at least one of the nrofBestBeamforMonitoring-r19 identified CSI-RS resources, or SS/PBCH Block resources is mapped one of the nrofreportedpredictedrs-r19 reported P-CRI(s) or P-SSBRI(s), if nroftimeinstance-r19 is not configured, or for the timeinstanceformonitoring-r19-th time instance if nroftimeinstance-r19 is configured, of the linked report of the first CSI Reporting Setting, wherein the mapping between CSI-RS resources, or SS/PBCH Block resources of Resource Set for channel measurement of the second CSI Reporting Setting and CSI-RS resources, or SS/PBCH Block resources of Resource Set given by resourcesForSetA-r19 of the first CSI Reporting Setting is provided by the higher layer parameter RSMappingtoSetA in the second CSI Reporting Setting; - if this condition is met, the transmission occasion is counted as an accurate reference signal prediction instance; otherwise, it is not counted as an accurate reference signal prediction instance; determine RS-PAI as the total count of accurate reference signals prediction instance(s), and the UE shall report RS-PAI for the second Reporting Setting, with a -bit field (M is given by nroftransmissionOccasion-r19). <omitted texts> |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506451](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506451.zip)

**Agreement** · `8.1.1` Specification support for beam management · `RAN1#122:8.1.1:003` · 관련 주제: CSI 보고/codebook, CSI-RS · 유지보수 (CR)

구현 영향: 처리 시간·CPU, 측정·보고량 · 규격: TS 38.214 5.2.1.6

> Adopt the following TP in section 5.2.1.6, TS 38.214.
> Reason for change: The CPU occupation time of the monitoring report is unclear.
> Summary of change: For UE-sided model, regarding a CSI report with CSI-ReportConfig for monitoring, Rel-15 CPU occupation time is reused for CPU occupation time of the CSI report for all types of CSI reports (i.e., AP/SP/P CSI report).
> Consequence if not approved: The CPU occupation time of the monitoring report is not aligned between the gNB and UE, leading to inefficient CSI report scheduling.
> | 5.2.1.6 CSI processing criteria <Unchanged part is omitted> For a CSI report with CSI-ReportConfig with higher layer parameter reportQuantity not set to 'none', or a CSI report with LTM-CSI-ReportConfig, or reportQuantity not set to 'none-bm-r19' or 'none-csi-r19', the CPU(s) (including and/or , for CSI reports with reportQuantity set to 'p-cri-r19', 'p-cri-RSRP-r19', 'p-ssb-index-r19', or 'p-ssb-index-RSRP-r19' or 'rs-pai-r19', and CSI reports configured with the higher layer parameter [RRC_name-r19] are occupied for a number of OFDM symbols as follows: - A periodic or semi-persistent CSI report (excluding an initial semi-persistent CSI report on PUSCH after the PDCCH triggering the report and a semi-persistent CSI report on PUSCH configured with the higher layer parameter codebookType set to 'typeII-Doppler-r18' or 'typeII-Doppler-PortSelection-r18') occupies CPU(s) from the first symbol of the earliest one of each CSI-RS/CSI-IM/SSB resource, or each CSI-RS/CSI-IM resource associated with all configured sub-configurations for periodic CSI report corresponding to a CSI-ReportConfig that contains a list of sub-configurations provided by csi-ReportSubConfigToAddModList, or each CSI-RS/CSI-IM resource associated with all activated/triggered sub-configurations for semi-persistent CSI report corresponding to a CSI-ReportConfig that contains a list of sub-configurations provided by csi-ReportSubConfigToAddModList, for channel or interference measurement, respective latest CSI-RS/CSI-IM/SSB occasion no later than the corresponding CSI reference resource, until the last symbol of the configured PUSCH/PUCCH carrying the report. <Unchanged part is omitted> |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506451](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506451.zip)

**Agreement** · `8.1.1` Specification support for beam management · `RAN1#122:8.1.1:004` · 관련 주제: CSI 보고/codebook · 유지보수 (CR)

구현 영향: 측정·보고량 · 규격: TS 38.212 6.3.1.1.2

> Adopt the following TP for Clause 6.3.1.1.2 in TS 38.212.
> Reason for change: For NW-sided model, for a CSI-ReportConfig with the number of reported RS is the same as the size of the corresponding resource set for channel measurement, the mapping between the reported RSRPs and the resources within the resource set is unclear.
> Summary of change: Clarify the mapping between the reported RSRPs and the resources within the resource set when the number of reported RS of a CSI-ReportConfig is the same as the size of the corresponding resource set for channel measurement.
> Consequence if not approved: The understanding of resources corresponding to reported RSRPs is not aligned between the gNB and UE.
> | Table 6.3.1.1.2-8G: Mapping order of CSI fields of one report for CRI/RSRP or SSBRI/RSRP reporting, if nrofReportedRS is configured |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506451](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506451.zip)

**Agreement** · `8.1.1` Specification support for beam management · `RAN1#122:8.1.1:005` · 관련 주제: CSI 보고/codebook · 유지보수 (CR)

> For one CSI resource setting for Set A for CSI report for inference for UE-side model
> - Only a single resource set can be configured for the CSI resource setting.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506452](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506452.zip)

**Agreement** · `8.1.1` Specification support for beam management · `RAN1#122:8.1.1:006` · 관련 주제: CSI 보고/codebook · 유지보수 (CR)

구현 영향: UE capability·FG

> Support the following on the reporting condition of CSI reporting for inference
> - For BM-Case2, after the CSI report (re)configuration, serving cell activation, BWP change, or activation of SP-CSI, UE transmit a CSI report for inference only if receiving at least K latest consecutive transmission occasion for each of the RS resources in Set B no later than the corresponding CSI reference resource, where K is indicated by a new UE capability.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506452](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506452.zip)

**Agreement** · `8.1.1` Specification support for beam management · `RAN1#122:8.1.1:007` · 관련 주제: CSI 보고/codebook · 유지보수 (CR)

> Support the following on the reporting condition of CSI reporting for monitoring
> - After the CSI report (re)configuration, serving cell activation, BWP change, or activation of SP-CSI, UE transmit a CSI report for monitoring only if receiving at least nroftransmissionOccasion-r19 latest transmission occasion for each of the RS resources in the resource set for monitoring no later than the corresponding CSI reference resource.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506452](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506452.zip)

**Agreement** · `8.1.1` Specification support for beam management · `RAN1#122:8.1.1:008` · 관련 주제: CSI 보고/codebook · 유지보수 (CR)

> For AP CSI report for inference, regarding the associated ID for aperiodic CSI resource setting with multiple resource sets for Set B
> - Associated ID in CSI report configuration is for the resource set(s) for Set B
>   - Note: This does not have impact on RAN1 specifications

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506452](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506452.zip)

**Agreement** · `8.1.1` Specification support for beam management · `RAN1#122:8.1.1:009` · 관련 주제: CSI 보고/codebook, CSI-RS · 유지보수 (CR)

구현 영향: UE capability·FG, 측정·보고량 · 규격: TS 38.214 5.2.2.5

> Adopt the following TP for TS 38.214 Clause 5.2.2.5.
> Reason for change: The condition of reporting CSI report for inference for BM-Case2 is unclear.
> Summary of change: Adding the condition of reporting CSI report for inference for BM-Case2.
> Consequences if not approved: gNB and UE may have different understanding on the condition of reporting CSI report for inference for BM-Case2.
> | 5.2.2.5 CSI reference resource definition <omitted texts> For a CSI-ReportConfig configured with the higher layer parameter reportQuantity set to 'etypeII-Doppler-r19', after the CSI report (re)configuration, serving cell activation, BWP change, or activation of SP-CSI, the UE reports a CSI report only after receiving at least one aperiodic or 𝐾𝑝 consecutive periodic/semi-persistent CSI-RS transmission occasion(s) for each of the CSI-RS resources in each CSI-RS resource group in the corresponding CSI-RS resource set for channel measurement and at least one CSI-RS and/or CSI-IM resource transmission occasion for each of the CSI-RS and/or CSI-IM resources in the corresponding resource set for interference measurement no later than the CSI reference resource and within the same DRX active time, when DRX is configured, and drops the report otherwise. The value of 𝐾𝑝∈{1,2,4} is indicated by UE capability, as defined in clause 5.2.1.6. For a CSI-ReportConfig configured with the higher layer parameter reportQuantity set to 'p-cri-r19', 'p-cri-RSRP-r19', 'p-ssb-index-r19' or 'p-ssb-index-RSRP-r19' and with nroftimeinstance-r19 is configured, after the CSI report (re)configuration, serving cell activation, BWP change, or activation of SP-CSI, the UE reports a CSI report only if receiving at least 𝐾BM latest consecutive transmission occasion(s) for each of the CSI-RS resources or SS/PBCH Block resources in the corresponding resource set for channel measurement no later than the CSI reference resource, and drops the report otherwise. The value of 𝐾BM is indicated by UE capability. <omitted texts> |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506453](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506453.zip)

**Agreement** · `8.1.1` Specification support for beam management · `RAN1#122:8.1.1:010` · 관련 주제: CSI 보고/codebook, CSI-RS · 유지보수 (CR)

구현 영향: UE capability·FG, 측정·보고량 · 규격: TS 38.214 5.2.2.5

> Adopt the following TP for TS 38.214 Clause 5.2.2.5.
> Reason for change: The condition of reporting RS-PAI is unclear.
> Summary of change: Adding the condition of reporting RS-PAI.
> Consequences if not approved: gNB and UE may have different understanding on the condition of reporting RS-PAI.
> | 5.2.2.5 CSI reference resource definition <omitted texts> For a CSI-ReportConfig configured with the higher layer parameter reportQuantity set to 'etypeII-Doppler-r19', after the CSI report (re)configuration, serving cell activation, BWP change, or activation of SP-CSI, the UE reports a CSI report only after receiving at least one aperiodic or 𝐾𝑝 consecutive periodic/semi-persistent CSI-RS transmission occasion(s) for each of the CSI-RS resources in each CSI-RS resource group in the corresponding CSI-RS resource set for channel measurement and at least one CSI-RS and/or CSI-IM resource transmission occasion for each of the CSI-RS and/or CSI-IM resources in the corresponding resource set for interference measurement no later than the CSI reference resource and within the same DRX active time, when DRX is configured, and drops the report otherwise. The value of 𝐾𝑝∈{1,2,4} is indicated by UE capability, as defined in clause 5.2.1.6. For a CSI-ReportConfig configured with the higher layer parameter reportQuantity set to 'rs-pai-r19', after the CSI report (re)configuration, serving cell activation, BWP change, or activation of SP-CSI, the UE reports a CSI report only if receiving at least nroftransmissionOccasion-r19 latest transmission occasion(s) for each of the CSI-RS resources or SS/PBCH Block resources in the corresponding resource set for channel measurement no later than the CSI reference resource, and drops the report otherwise. <omitted texts> |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506453](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506453.zip)

**Agreement** · `8.1.1` Specification support for beam management · `RAN1#122:8.1.1:011` · 관련 주제: CSI 보고/codebook · 유지보수 (CR)

구현 영향: 처리 시간·CPU, UE capability·FG, 측정·보고량 · 규격: TS 38.214 5.2.1.6

> Adopt the following TP in section 5.2.1.6, TS 38.214.
> Reason for change: To capture the agreement to support two AI/ML PU pools.
> Summary of change: Adding the description to support two AI/ML PU pools.
> Consequences if not approved: two AI/ML PU pools are not supported.
> | 5.2.1.6 CSI processing criteria <Unchanged part is omitted> For CSI reports with reportQuantity set to 'p-cri-r19', 'p-cri-RSRP-r19', 'p-ssb-index-r19', or 'p-ssb-index-RSRP-r19', and CSI reports configured with the higher layer parameter [RRC_name-r19], the UE may indicate a second value for the number of supported simultaneous CSI calculations with parameter SecondValuesSimultaneousCSI-ReportsPerCC in a component carrier, and SecondValuesSimultaneousCSI-ReportsAllCC across all component carriers, and if applicable, a third value for the number of supported simultaneous CSI calculations with parameter ThirdValuesSimultaneousCSI-ReportsPerCC in a component carrier, and ThirdValuesSimultaneousCSI-ReportsAllCC across all component carriers, in addition to . If a UE supports simultaneous CSI calculations it is said to have CSI processing units for processing CSI reports. If L Lx CPUs are occupied for calculation of CSI reports in a given OFDM symbol, the UE has Lx unoccupied CPUs. If CSI reports start occupying their respective CPUs on the same OFDM symbol on which Lx CPUs are unoccupied, where each CSI report corresponds to , the UE is not required to update the requested CSI reports with lowest priority (according to Clause 5.2.5), where is the largest value such that Lx holds. If only the second value is indicated, x = 2. If both of the second value and the third value are indicated, x = 2,3 where the CSI reports with reportQuantity set to 'p-cri-r19', 'p-cri-RSRP-r19', 'p-ssb-index-r19', or 'p-ssb-index-RSRP-r19' corresponds to either x = 2 or x = 3 subject to UE capability and the CSI reports configured with the higher layer parameter [RRC_name-r19] corresponds to either x = 2 or x = 3 subject to UE capability. For CSI reports with reportQuantity set to 'p-cri-r19', 'p-cri-RSRP-r19', 'p-ssb-index-r19', or 'p-ssb-index-RSRP-r19', and CSI reports configured with the higher layer parameter [RRC_name-r19] if a CSI report is not considered within any of and , the values for and are considered to be 0, for the procedure previously described in this clause and the UE is not required to update the CSI report. <Unchanged part is omitted> - for a CSI report with CSI-ReportConfig with reportQuantity-r19 set to 'p-cri-r19', 'p-cri-RSRP-r19', 'p-ssb-index-r19', or 'p-ssb-index-RSRP-r19', - if nroftimeinstance-r19 is not configured, and , where the value of and are reported by UE capability. - if nroftimeinstance-r19 is configured, and , where the value of and are reported by UE capability. - and , for a CSI report configured with the higher layer parameter [RRC_name-r19], where the values of and are reported by UE capability. For a CSI report with CSI-ReportConfig with higher layer parameter reportQuantity not set to 'none', or a CSI report with LTM-CSI-ReportConfig, or reportQuantity not set to 'none-bm-r19' or 'none-csi-r19', the CPU(s) (including and/or , for CSI reports with reportQuantity set to 'p-cri-r19', 'p-cri-RSRP-r19', 'p-ssb-index-r19', or 'p-ssb-index-RSRP-r19', and CSI reports configured with the higher layer parameter [RRC_name-r19]) are occupied for a number of OFDM symbols as follows: <Unchanged part is omitted> |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506453](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506453.zip)

**Agreement** · `8.1.1` Specification support for beam management · `RAN1#122:8.1.1:012` · 관련 주제: CSI 보고/codebook · 유지보수 (CR)

구현 영향: 측정·보고량

> Support the configuration of following parameters in a CSI-ReportConfig with the higher layer parameter reportQuantity set to'none-bm-r19':
> - TimeGap-r19, i.e., the time gap between two consecutive predicted time instances and between the reference time and the earliest predicted time instance.
> - nroftimeinstance-r19, i.e., number of predicted time instances for BM-Case 2.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506453](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506453.zip)

**Agreement** · `8.1.3` Specification support for CSI prediction · `RAN1#122:8.1.3:001` · 관련 주제: CSI 보고/codebook · 유지보수 (CR)

규격: TS 38.214 5.2.1.4.6

> Adopt following TPs for TS38.214 Section 5.2.1.4.6.
> | Reason for change | In current specification, there is no SGCS quantization mapping table. |
> | Summary of change | SGCS quantization mapping table is added. |
> | Consequences if not approved | Incomplete capture of the agreement. |
> | TS38.214 5.2.1.4.6 CSI-PAI reporting << Unchanged parts are omitted >> each calculated SGCS value is quantized to a 4-bit field, where the first codepoint ‘0000’ is used to indicate (0 0.3] value range, and the value range [0.3, 1] is quantized in a linear scale with 0.05 step size. Detailed mapping is specified in [xx, TS 38.abc]Table 5.2.1.4.6-1. Table 5.2.1.4.6-1: SGCS Quantization Mapping << Unchanged parts are omitted >> | TS38.214 5.2.1.4.6 CSI-PAI reporting << Unchanged parts are omitted >> each calculated SGCS value is quantized to a 4-bit field, where the first codepoint ‘0000’ is used to indicate (0 0.3] value range, and the value range [0.3, 1] is quantized in a linear scale with 0.05 step size. Detailed mapping is specified in [xx, TS 38.abc]Table 5.2.1.4.6-1. Table 5.2.1.4.6-1: SGCS Quantization Mapping << Unchanged parts are omitted >> |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506501](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506501.zip)

**Agreement** · `8.1.3` Specification support for CSI prediction · `RAN1#122:8.1.3:002` · 관련 주제: CSI 보고/codebook, CSI-RS · 유지보수 (CR)

구현 영향: 측정·보고량 · 규격: TS 38.214 5.2.1.4.6, TS 38.214 5.2.2.2.10, TS 38.214 5.2.2.2.11

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> Adopt following TPs for TS38.214 Section 5.2.1.4.6.
> | Reason for change | Based on the agreement, the reported wideband SGCS is the average of SGCS values across all subbands, not directly derived from the average precoder. |
> | Summary of change | The definition of SGCS needs to be changed to the average of SGCS values across all subbands. |
> | Consequences if not approved | Incorrect capture of the agreement. |
> | TS38.214 5.2.1.4.6 CSI-PAI reporting << Unchanged parts are omitted >> to report CSI-PAI for the second Reporting Setting, the UE shall: - determine predicted PMI (see Clause 5.2.2.2.10 or Clause 5.2.2.2.11) for each of the subband(s) configured by csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband for the -th time instance configured by timeinstanceforCSImonitoring-r19 in the second Reporting Setting ( , with provided in the first Reporting Setting), based on the CSI prediction performed by the UE using the channel measurement corresponding to the first Reporting Setting, - determine non-predicted PMI for each of the subband(s) configured by csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband, which is corresponding to the -th time instance of the report of the first Reporting Setting, based on the CSI-RS resource(s) in the resource set for channel measurement for the report corresponding to the second Reporting Setting. - determine non-predicted PMI for each of the subband(s) configured by csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband, based on the latest CSI-RS resource transmission occasion, no later than the CSI reference resource of the CSI report, corresponding to the first Reporting Setting - for , is the RI reported for the CSI report corresponding to the first Reporting Setting, calculate SGCS value(s) as, , , , , where is the predicted precoder represented by predicted PMI for -th layer, averaged over all the subbands configured by csi-ReportingBand, -th subband, and for -th time instance corresponding to the report of the first Reporting Setting, is the precoder represented by non-predicted PMI for -th layer, averaged over all the subbands configured by csi-ReportingBand, -th subband, based on the channel measurement corresponding to the second Reporting Setting, and is the precoder represented by PMI for -th layer and averaged over all the subbands configured by csi-ReportingBand -th subband, corresponds to the subbands configured by csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband, based on the latest CSI-RS resource transmission occasion, no later than CSI reference resource, corresponding to the report of the first Reporting Setting. << Unchanged parts are omitted >> | TS38.214 5.2.1.4.6 CSI-PAI reporting << Unchanged parts are omitted >> to report CSI-PAI for the second Reporting Setting, the UE shall: - determine predicted PMI (see Clause 5.2.2.2.10 or Clause 5.2.2.2.11) for each of the subband(s) configured by csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband for the -th time instance configured by timeinstanceforCSImonitoring-r19 in the second Reporting Setting ( , with provided in the first Reporting Setting), based on the CSI prediction performed by the UE using the channel measurement corresponding to the first Reporting Setting, - determine non-predicted PMI for each of the subband(s) configured by csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband, which is corresponding to the -th time instance of the report of the first Reporting Setting, based on the CSI-RS resource(s) in the resource set for channel measurement for the report corresponding to the second Reporting Setting. - determine non-predicted PMI for each of the subband(s) configured by csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband, based on the latest CSI-RS resource transmission occasion, no later than the CSI reference resource of the CSI report, corresponding to the first Reporting Setting - for , is the RI reported for the CSI report corresponding to the first Reporting Setting, calculate SGCS value(s) as, , , , , where is the predicted precoder represented by predicted PMI for -th layer, averaged over all the subbands configured by csi-ReportingBand, -th subband, and for -th time instance corresponding to the report of the first Reporting Setting, is the precoder represented by non-predicted PMI for -th layer, averaged over all the subbands configured by csi-ReportingBand, -th subband, based on the channel measurement corresponding to the second Reporting Setting, and is the precoder represented by PMI for -th layer and averaged over all the subbands configured by csi-ReportingBand -th subband, corresponds to the subbands configured by csi-ReportingBand and numberOfPMI-SubbandsPerCQI-Subband, based on the latest CSI-RS resource transmission occasion, no later than CSI reference resource, corresponding to the report of the first Reporting Setting. << Unchanged parts are omitted >> |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506501](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506501.zip)

**Agreement** · `8.1.3` Specification support for CSI prediction · `RAN1#122:8.1.3:003` · 관련 주제: CSI 보고/codebook · 유지보수 (CR)

> For CSI-PAI report, UE is expected to be configured with the same subband configuration with that of inference report.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506501](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506501.zip)

**Agreement** · `8.1.3` Specification support for CSI prediction · `RAN1#122:8.1.3:004` · 관련 주제: CSI 보고/codebook · 유지보수 (CR)

> For CSI prediction, for monitoring report, SP CSI report is only supported on PUSCH.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506501](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506501.zip)

**Agreement** · `8.1.3` Specification support for CSI prediction · `RAN1#122:8.1.3:005` · 관련 주제: CSI 보고/codebook, CSI-RS · 유지보수 (CR)

구현 영향: 측정·보고량 · 규격: TS 38.214 5.2.1.4.6, TS 38.214 5.2.1.4.2

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> The following TP2.6-1 and TP2.6-2 are endorsed as editorial corrections for TS 38.214 for Clauses 5.2.1.4.6 and 5.2.1.4.2, respectively.
> | TP 2.6-1 < Unchanged parts are omitted > 5.2.1.4.6 CSI-PAI reporting When the UE is configured with a first CSI Reporting Setting for reporting CSI prediction, based on a CSI-ReportConfig configured with the higher layer parameter [RRC_name-r19] and a second CSI Reporting Setting for reporting CSI-PAI, based on a CSI-ReportConfig with reportQuantity-r19 set to 'csi-pai-r19', and the second Reporting Setting is linked to the first Reporting Setting by inferenceReportConfigId-r19, the reporting of CSI-PAI corresponding to the second CSI Reporting Setting shall consider the following: - when aperiodic Reporting Setting is configured for both first and second Reporting Settings: - if aperiodic CSI-RS resources are configured for channel measurement for the first Reporting Setting, the UE is expected to receive the PDCCH triggering a CSI report of the second Reporting Setting, if any, no later than the first symbol of the earliest occasion of, , aperiodic CSI-RS resources in the resource set for channel measurement for the first Reporting Setting. - if a single periodic or semi-persistent CSI-RS resource is configured for channel measurement for the first Reporting Setting, the UE is expected to receive the PDCCH triggering a CSI report of second Reporting Setting, if any, no later than the first symbol of the earliest transmission occasion of the most recent, , periodic or semi-persistent CSI-RS resource, no later than the CSI reference resource of the CSI report, corresponding to the first Reporting Setting. - to report CSI-PAI for the second Reporting Setting, the UE shall: - determine predicted PMI (see Clause 5.2.2.2.10 or Clause 5.2.2.2.11) for each of the subband(s) configured by csi-ReportingBand for the -th time instance configured by timeinstanceforCSImonitoring-r19 in the second Reporting Setting ( , with provided in the first Reporting Setting), based on the CSI prediction performed by the UE using the channel measurement corresponding to the first Reporting Setting, - determine non-predicted PMI for each of the subband(s) configured by csi-ReportingBand, which is corresponding to the -th time instance of the report of the first Reporting Setting, based on the CSI-RS resource(s) in the resource set for channel measurement for the report corresponding to the second Reporting Setting. - determine non-predicted PMI for each of the subband(s) configured by csi-ReportingBand, based on the latest CSI-RS resource transmission occasion, no later than the CSI reference resource of the CSI report, corresponding to the first Reporting Setting < Unchanged parts are omitted > --------------------------------------- End of Text Proposal ------------------------------------ |
> | TP 2.6-2 < Unchanged parts are omitted > 5.2.1.4.2 Report quantity configurations If the UE is configured with a CSI-ReportConfig with reportQuantity-r19 set to 'csi-pai-r19', - the UE shall be configured with inferenceReportConfigId-r19 to link another CSI-ReportConfig configured with a higher layer parameter [RRC_name-r19], - when semi-persistent Reporting Setting is configured for the CSI-ReportConfig configured with the higher layer parameter [RRC_name-r19], the UE is not expected to be configured with a periodic Reporting Setting for the CSI-ReportConfig with reportQuantity-r19 set to 'csi-pai-r19'. - when aperiodic Reporting Setting is configured for the CSI-ReportConfig configured with the higher layer parameter [RRC_name-r19], the UE is not expected to be configured with a periodic or semi-persistent Reporting Setting for the CSI-ReportConfig with reportQuantity-r19 set to 'csi-pai-r19'. < Unchanged parts are omitted > --------------------------------------- End of Text Proposal ------------------------------------ |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506501](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506501.zip)

**Agreement** · `8.1.3` Specification support for CSI prediction · `RAN1#122:8.1.3:006` · 관련 주제: CSI 보고/codebook · 유지보수 (CR)

구현 영향: 측정·보고량

> For CSI-PAI report, when the UE is configured with two linked CSI report configurations, adopt UCI padding to fixed size
> - based on the maximum rank determined from configuration of RI restriction (for simplicity denoted by max_rank here), the size of the CSI-PAI report is 2×max_rank×4 irrespective of the reported rank ‘v’ in the inference report.
> - When the linked inference report indicates rank ‘v’, all ones is padded to LSB of the UCI sequence for each of max_rank-v fields of SGCS#1 or SGCS#2

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506501](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506501.zip)

**Agreement** · `8.1.3` Specification support for CSI prediction · `RAN1#122:8.1.3:007` · 관련 주제: CSI 보고/codebook · 유지보수 (CR)

구현 영향: 측정·보고량

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> For PMI assumption on SGCS calculation of  and  ,support Rel-16 eType II CSI.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506502](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506502.zip)

**Agreement** · `8.1.3` Specification support for CSI prediction · `RAN1#122:8.1.3:008` · 관련 주제: CSI 보고/codebook, CSI-RS · 유지보수 (CR)

구현 영향: 처리 시간·CPU, UE capability·FG

> For CSI-PAI report, support
> - OCPU =X, X is reported by UE capability
> - For AP monitoring report, CPU occupancy starts from the first symbol after the PDCCH triggering the CSI report until the last symbol of the scheduled PUSCH carrying the CSI-PAI report
> - For SP monitoring report, CPU occupancy starts from the first symbol of the latest periodic/semi-persistent CSI-RS occasion of the inference report not later than CSI reference resource of the inference report, until the last symbol of the configured PUSCH carrying the CSI-PAI report

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506502](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506502.zip)

**Agreement** · `8.1.3` Specification support for CSI prediction · `RAN1#122:8.1.3:009` · 관련 주제: CSI 보고/codebook · 유지보수 (CR)

> For CSI prediction using UE-side model, for UE assisted performance monitoring,
> - If the inference report is semi-persistent and the monitoring report is aperiodic or semi-persistent, UE is expected to receive the DCI triggering the monitoring report if any, no later than the first symbol of the earliest occasion of the most recent periodic or semi-persistent inference measurement resource transmission occasions that are no later than the CSI reference resource of the associated inference report.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506572](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506572.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122:9.1:001` · 관련 주제: CSI 보고/codebook · UE features (FG)

구현 영향: 처리 시간·CPU, UE capability·FG

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-0-1 | CSI report framework for UE-side inference | 1. Number of APU pools N 12. Maximum number of APUs in each APU pool for all types of UE-sided inference for CSI report(s) for simultaneously in a CC 23. Maximum number of APUs in each APU pool for all types of UE-sided inference for CSI report(s) simultaneously across all CCs | FFS | yes | n/a | Maximum number of APUs for UE-sided inference is unknown to the network | FFS Per UE | FFS N/A | FFS N/A | FFS N/A | Component 1 candidate values: {1,2} Component 12 candidate values: FFS{1…8} Component 23 candidate values: FFS{1…32} Note: Component 2 and 3 candidate values are signalled separately for each pool [A UE that does not support this FG reuses the CPU] | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506605](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506605.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122:9.1:002` · 관련 주제: Beam management · UE features (FG)

구현 영향: 포트·자원·레이어 수, 측정·보고량

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-1 | Increased number of reported RSs for beam management | 1. Support of reporting format for L1-RSRP measurements not including CRI/SSBRI other than one for the largest measured L1-RSRP in a reporting instance, if the number of reported L1-RSRPs is equal to the size of the measurement resource set. 2. Support of reporting format for L1-RSRPs and corresponding beam information of Top M beam(s) with largest M measured value(s) of L1-RSRP(s) of a measurement resource set, where M is configured by gNB, if the number of reported L1-RSRPs is smaller than the size of the measurement resource set 3. Maximum number of M reported RSs, M>4 | FFS | yes | n/a | Increased number of reported beams for beam management is not supported | FFS Per UE | FFS N/A | FFS N/A | FFS N/A | Component 3 candidate values: {6,8} | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506605](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506605.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122:9.1:003` · 관련 주제: CSI 보고/codebook, CSI-RS · UE features (FG)

구현 영향: 처리 시간·CPU, UE capability·FG, 포트·자원·레이어 수

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-2 | UE-side beam prediction for BM Case1 [for inference] | 1. Support of beam prediction with reporting of predicted beam index for BM-Case1 [for inference] with UE-side model 3. Maximum number of inference report(s) configured for BM-Case1 per BWP 3a. Maximum number of inference report(s) configured for BM-Case1 across all CCs [4. Maximum number of inference report(s) activated for BM-Case1 per BWP] [4a. Maximum number of inference report(s) activated for BM-Case1 across all CCs] [5. Maximum number of inference report(s) triggered for BM-Case1 per BWP] [5a. Maximum number of inference report(s) triggered for BM-Case1 across all CCs] 6. Support of SSB as RS type for Set B 6a. Support of CSI-RS as RS type for Set B 6b. Support of SSB as RS type for Set A 6c. Support of CSI-RS as RS type for Set A [7. Supported combinations of the number of resources for Set B and the number of resources for Set A] [7a: Supported maximum number of resources for Set B] [7b: Supported maximum number of resources for Set A] [8. Supported CSI-RS resource types: Periodic CSI-RS, Semi-persistent CSI-RS, Aperiodic CSI-RS] [9. Supported inference report types: Periodic CSI report, Aperiodic CSI report, semi-persistent CSI report] [10. Supported options for performance monitoring for beam case 1 with UE side model] [11. Supported BM-Case 1 sub-usecase(s): {setB-subset-of-setA, setB-different-from-setA, both} 12. Supported maximum number of predicted beams in each reporting instanceFFS: whether/how to merge this FG with other FG(s) for performance monitoring and/or data collection 13. Supported number of occupied CPU 14. Supported number of occupied APU 15. Supported value of d for the relaxation of Z3 timeline 16. Supported value of d’ for the relaxation of Z’3 timeline 17. Index of the occupied APU pool | FFS | yes | n/a | UE-sided beam prediction for BM Case 1 [for inference] is not supported | FFS | FFS | FFS | FFS | FFS: CPU/AIMLPU related information | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506605](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506605.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122:9.1:004` · 관련 주제: CSI 보고/codebook · UE features (FG)

구현 영향: 처리 시간·CPU, 포트·자원·레이어 수

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-3 | UE-side beam prediction for BM Case1 with predicted RSRP [for inference] | 1. Support of beam prediction, reporting of predicted beam index and predicted RSRP, for BM-Case1 [for inference] 2. Supported maximum number of predicted beams with RSRP in each reporting instance | 58-1-2 | yes | n/a | UE-side beam prediction for BM Case 1 with predicted RSRP [for inference] is not supported | FFS | FFS | FFS | FFS | Component 2 candidate values: {1, 2, 3, 4} FFS: CPU/AIMLPU related information | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506605](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506605.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122:9.1:005` · 관련 주제: CSI 보고/codebook, CSI-RS · UE features (FG)

구현 영향: 처리 시간·CPU, 포트·자원·레이어 수

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-4 | UE-side beam prediction for BM Case2 [for inference] | 1. Support of beam prediction with reporting of predicted beam index for BM-Case2 [for inference] with UE-side model 3. Maximum number of inference report(s) configured for BM-Case2 per BWP 3a. Maximum number of inference report(s) configured for BM-Case2 across all CCs [4. Maximum number of inference report(s) activated for BM-Case2 per BWP] [4a. Maximum number of inference report(s) activated for BM-Case2 across all CCs] [5. Maximum number of inference report(s) triggered for BM-Case2 per BWP] [5a. Maximum number of inference report(s) triggered for BM-Case2 across all CCs] 6. Support of SSB as RS type for Set B 6a. Support of CSI-RS as RS type for Set B 6b. Support of SSB as RS type for Set A 6c. Support of CSI-RS as RS type for Set A [7. Supported combinations of the number of resources for Set B and the number of resources for Set A] [7a: Supported maximum number of resources for Set B] [7b: Supported maximum number of resources for Set A] [8. Supported CSI-RS resource types: Periodic CSI-RS, Semi-persistent CSI-RS] [9. Supported inference report types: Periodic CSI report, Aperiodic CSI report, semi-persistent CSI report] [10. Supported options for performance monitoring for beam case 2 with UE side model] 11. Supported maximum number of predicted beams in each predicted time instance 12. Supported maximum number of predicted time instances [13. Supported maximum total number of reported predicted beams for predicted time instances in one report] 14. Supported combinations of supported value(s) of valid time duration for each predicted time instance and number of predicted beams for each value of valid time duration [20. Supported BM-Case 2 sub usecase(s): e.g., setB-equals-to-setA, setB-subset-of-setA, setB-different-from-setA, or merged version(s)] 21. supported number of occupied CPU 22. supported number of occupied APU 23. supported value of d for the relaxation of Z3 timeline 24. supported value of d’ for the relaxation of Z’3 timeline 17. Index of the occupied APU pool | FFS | yes | n/a | UE-side beam prediction for BM-Case2 [for inference] is not supported | FFS | FFS | FFS | FFS | FFS: CPU/AIMLPU related information FFS: candidate values for components | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506605](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506605.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122:9.1:006` · 관련 주제: CSI 보고/codebook · UE features (FG)

구현 영향: 처리 시간·CPU

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-5 | UE-side beam prediction for BM-Case2 with predicted RSRP [for inference] | 1. Support of beam prediction, reporting of predicted beams and predicted RSRP, for BM-Case2 (spatial and time domain beam prediction) [for inference] | 58-1-4 | yes | n/a | UE-side beam prediction for BM-Case2 [for inference] is not supported | FFS | FFS | FFS | FFS | FFS: CPU/AIMLPU related information | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506605](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506605.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122:9.1:007` · 관련 주제: CSI-RS · UE features (FG)

구현 영향: UE capability·FG, 포트·자원·레이어 수

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-7 | Data collection for UE-side beam prediction [for BM case 1] | 1. Support of data collection for UE-side beam prediction [for BM case 1] 2. Support of SS/PBCH block and 1-port CSI-RS based RSRP measurements for measurement RS resource sets (Set B and Set A) for data collection [3. Supported sub-use cases: {‘Set B equal to Set A’, ‘Set B subset of Set A’,’Set B not a subset of Set A’}] [6: Supported maximum number of resources for Set B] [7: Supported maximum number of resources for Set A] 8. Support of SSB as RS type for Set B 9. Support of CSI-RS as RS type for Set B 10. Support of SSB as RS type for Set A 11. Support of CSI-RS as RS type for Set A | FFS | yes | n/a | Data collection for UE-side beam prediction is not supported [for BM case 1] | FFS Per UE | FFS N/A | FFS N/A | FFS N/A | Component 3 candidate values: {‘Set B equal to Set A’, ‘Set B subset of Set A’,’Set B not a subset of Set A’} Component 6 candidate values: {4, 8, 16, 32, 64} Component 7 candidate values: {8, 16, 32, 64} Note: it is up to RAN2 whether this FG is merged into data collection FG defined by RAN2 | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506605](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506605.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122:9.1:008` · 관련 주제: CSI 보고/codebook, CSI-RS · UE features (FG)

구현 영향: 처리 시간·CPU, 포트·자원·레이어 수, 측정·보고량

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_Air | 58-3-1 | CSI prediction for UE-sided inference when N4=1 | 1. Support of CSI prediction for UE-sided inference when N4=1 2. Support for reporting predicted PMI with N4=1 3. A list of supported combinations, each combination is { Max # of Tx ports in one resource, Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 4. Support of Rel-16 eType-II regular codebook refinement for predicted PMI with PMI subband R=1 5. Support parameter combinations with L=2,4 6. Support for rank = 1,2 7. Support for the size of DD-basis, N4=1 8. Support X=1 CQI based on the first/earliest slot of the CSI reporting window and the first/earliest predicted PMI (TDCQI=’1-1’) [9. Value for CPU occupation, when P/SP-CSI-RS is configured for CMR] [10. Value for CPU occupation, when A-CSI-RS is configured for CMR] 11. Scaling factor for active resource counting Kp 12. supported value of t for the relaxation of Z and Z’ timeline 13. supported number of occupied CPU 14. supported number of occupied APU 15. Index of the occupied APU pool | 2-35 58-0-1 | yes | n/a | CSI prediction for N4=1 for inference is not supported | [Per band and Per BC] | n/a | n/a | n/a | Component 3 candidate values: a. {4,8,12,16,24,32} b. {2,3,4 … 64} c. {4, …, 256} | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506605](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506605.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122:9.1:009` · 관련 주제: CSI 보고/codebook, CSI-RS · UE features (FG)

구현 영향: 포트·자원·레이어 수

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_Air | 58-3-1-7 | Active CSI-RS resources and ports for mixed R16 based doppler codebook for CSI prediction via UE side model with other codebooks in any slot | 1. List of codebook combinations of two types 2. List of {max number of ports per resource, max number of resources, max number of total ports} for each codebook combination | 23-9-1, 16-3a, 2-36, 2-40, 2-41, 23-9-2, 23-9-4, 40-3-2-1, 40-3-2-1a, 40-3-2-2, X-1-1, X-1-1a, X-1-2 | Yes | n/a | Active CSI-RS resources and ports for mixed R16 based doppler codebook for CSI prediction via UE side model with other codebooks in any slot is not supported | Per band and Per BC | n/a | n/a | n/a | Component 1 candidate values: FFS {Type I SP, CSI prediction for UE-sided inference when N4=1 and R=1} {Type I SP, CSI prediction for UE-sided inference when N4>1 and R=1} {eType II R=1, CSI prediction for UE-sided inference when N4=1 and R=1} {eType II R=1, CSI prediction for UE-sided inference when N4>1 and R=1} Component 2 candidate values: FFS - Maximum 16 triplets - Max # of Tx ports in one resource: {4,8,12,16,24,32} - Max # resources: {1 to 64} - Max # total ports: {4 to 256} Note: if a UE reports one or more codebook combinations in 58-3-1-7, then usage of active CSI-RS resources and ports for multiple codebooks in any slot is allowed only within those combinations Note: For coexisting of mixed codebooks in any slot, gNB need to honor 16-8, 23-9-5, 58-3-1-7 and per-codebook capability 2-36/40/41, 16-3a, and 23-9-1/23-9-2/23-9-4. [Note: Up to 4 combinations for component 1] | Optional with capability signaling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506605](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506605.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122:9.1:010` · 관련 주제: CSI 보고/codebook, CSI-RS · UE features (FG)

구현 영향: 처리 시간·CPU, 포트·자원·레이어 수, 측정·보고량

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_Air | 58-3-2 | CSI prediction for UE-sided inference when N4>1 | 1. Support of CSI prediction for UE-sided inference when N4>1 2. Support for reporting predicted PMI with N4>1 3. A list of supported combinations, each combination is {Max N4, Max # of Tx ports in one resource, Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 4. Value of d=m for the DD unit size when A-CSI-RS is configured for CMR 5. Support for the size of DD-basis, N4>1 76. A list of supported combinations, each combination is {Max N4, Max # of Tx ports in one resource, Max # of resources and total # of Tx ports} for one CSI report setting 7. Supported number of occupied CPU 8. Supported number of occupied APU 9. Index of the occupied APU pool [8. Supported values of the Maximum number of observation number] | 58-3-1 | yes | n/a | CSI prediction for N4>1 for inference is not supported | [Per band and Per BC] | FFS N/A | FFS N/A | FFS N/A | FFS: CPU/AIMLPU related information Component 3 candidate values: FFS a. {1,2,4,8} b. {4,8,12,16,24,32} c. {2,3,4 … 64} d. {4, …, 256} Component 6 candidate values: a. {1,2,4,8} b. {4,8,12,16,24,32} c. {4,8,12} d.{4, …, 256} | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506605](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506605.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122:9.1:011` · 관련 주제: CSI 보고/codebook · UE features (FG)

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_Air | 58-3-4 | UE side data collection for CSI prediction | 1. Support of data collection for CSI prediction | FFS | yes | n/a | UE side data collection for CSI prediction is not supported | FFS Per band and Per BC | FFS N/A | FFS N/A | FFS N/A |  | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506605](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506605.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122:9.1:012` · 관련 주제: CSI 보고/codebook · UE features (FG)

구현 영향: UE capability·FG, 포트·자원·레이어 수

> Introduce the following Rel. 19 UE FGs (yellow highlighting, if any, shows text that’s not yet agreed)
> | 58. NR_AIML_Air | 58-3-5 | Performance monitoring for CSI prediction model | 1. Supported number of performance metric SGCS 2. Support of one wideband frequency granularity SGCS per layer 3. Support of one configured time instance for N4>1 4. A list of supported combinations, each combination is {Max # of Tx ports in one resource, Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously | 58-3-1 | Yes | n/a | Performance monitoring for CSI prediction model is not supported | Per Band and Per BC | N/A | N/A | N/A | Component 1 candidate values: {1,2} Component 4 candidate values: - Maximum 16 triplets - Max # of Tx ports in one resource: {4,8,12,16,24,32} - Max # resources: {1 to 64} - Max # total ports: {4 to 256} Note: If the UE reports candidate value ‘1’ for component 1 then the SGCS is for the predicted CSI | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506605](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506605.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122:9.1:024` · 관련 주제: CSI 보고/codebook, CSI-RS · UE features (FG)

구현 영향: 처리 시간·CPU, UE capability·FG, 포트·자원·레이어 수

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-2 | UE-side beam prediction for BM Case1 [for inference] | 1. Support of beam prediction with reporting of predicted beam index for BM-Case1 [for inference] with UE-side model 3. Maximum number of inference report(s) configured for BM-Case1 per BWP 3a. Maximum number of inference report(s) configured for BM-Case1 across all CCs [4. Maximum number of inference report(s) activated for BM-Case1 per BWP] [4a. Maximum number of inference report(s) activated for BM-Case1 across all CCs] [5. Maximum number of inference report(s) triggered for BM-Case1 per BWP] [5a. Maximum number of inference report(s) triggered for BM-Case1 across all CCs] 6. Support of SSB as RS type for Set B 6a. Support of CSI-RS as RS type for Set B 6b. Support of SSB as RS type for Set A 6c. Support of CSI-RS as RS type for Set A [7. Supported combinations of the number of resources for Set B and the number of resources for Set A] [7a: Supported maximum number of resources for Set B] [7b: Supported maximum number of resources for Set A] 8. Supported CSI-RS resource types: Periodic CSI-RS, Semi-persistent CSI-RS, Aperiodic CSI-RS 9. Supported inference report types: Periodic CSI report, Aperiodic CSI report, semi-persistent CSI report 11. Supported BM-Case 1 sub-usecase(s): {setB-subset-of-setA, setB-different-from-setA, both} 12. Supported maximum number of predicted beams in each reporting instanceFFS: whether/how to merge this FG with other FG(s) for performance monitoring and/or data collection 13. Supported number of occupied CPU 14. Supported number of occupied APU 15. Supported value of d for the relaxation of Z3 timeline 16. Supported value of d’ for the relaxation of Z’3 timeline 17. Index of the occupied APU pool | FFS | yes | n/a | UE-sided beam prediction for BM Case 1 [for inference] is not supported | FFS Per UE | FFS No | FFS No | FFS No | Component 8 candidate values: {Periodic CSI-RS, Semi-persistent CSI-RS, Aperiodic CSI-RS} Component 9 candidate values: {Periodic CSI report, Aperiodic CSI report, semi-persistent CSI report} FFS: candidate values for components | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506605](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506605.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122:9.1:025` · 관련 주제: CSI 보고/codebook, CSI-RS · UE features (FG)

구현 영향: 처리 시간·CPU, 포트·자원·레이어 수

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-4 | UE-side beam prediction for BM Case2 [for inference] | 1. Support of beam prediction with reporting of predicted beam index for BM-Case2 [for inference] with UE-side model 3. Maximum number of inference report(s) configured for BM-Case2 per BWP 3a. Maximum number of inference report(s) configured for BM-Case2 across all CCs [4. Maximum number of inference report(s) activated for BM-Case2 per BWP] [4a. Maximum number of inference report(s) activated for BM-Case2 across all CCs] [5. Maximum number of inference report(s) triggered for BM-Case2 per BWP] [5a. Maximum number of inference report(s) triggered for BM-Case2 across all CCs] 6. Support of SSB as RS type for Set B 6a. Support of CSI-RS as RS type for Set B 6b. Support of SSB as RS type for Set A 6c. Support of CSI-RS as RS type for Set A [7. Supported combinations of the number of resources for Set B and the number of resources for Set A] [7a: Supported maximum number of resources for Set B] [7b: Supported maximum number of resources for Set A] 8. Supported CSI-RS resource types: Periodic CSI-RS, Semi-persistent CSI-RS 9. Supported inference report types: Periodic CSI report, Aperiodic CSI report, semi-persistent CSI report 11. Supported maximum number of predicted beams in each predicted time instance 12. Supported maximum number of predicted time instances 13. Supported maximum total number of reported predicted beams for predicted time instances in one report 14. Supported combinations of supported value(s) of valid time duration for each predicted time instance and number of predicted beams for each value of valid time duration 21. supported number of occupied CPU 22. supported number of occupied APU 23. supported value of d for the relaxation of Z3 timeline 24. supported value of d’ for the relaxation of Z’3 timeline 2517. Index of the occupied APU pool | FFS | yes | n/a | UE-side beam prediction for BM-Case2 [for inference] is not supported | FFS Per UE | FFS No | FFS No | FFS No | Component 8 candidate values: {Periodic CSI-RS, Semi-persistent CSI-RS} Component 9 candidate values: {Periodic CSI report, Aperiodic CSI report, semi-persistent CSI report} FFS: candidate values for components | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506605](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506605.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122:9.1:026` · UE features (FG)

구현 영향: 포트·자원·레이어 수

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-3 | UE-side beam prediction for BM Case1 with predicted RSRP [for inference] | 1. Support of beam prediction, reporting of predicted beam index and predicted RSRP, for BM-Case1 [for inference] 2. Supported maximum number of predicted beams with RSRP in each reporting instance | 58-1-2 | yes | n/a | UE-side beam prediction for BM Case 1 with predicted RSRP [for inference] is not supported | FFS Per UE | FFS No | FFS No | FFS No | Component 2 candidate values: {1, 2, 3, 4} | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506605](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506605.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122:9.1:027` · UE features (FG)

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-5 | UE-side beam prediction for BM-Case2 with predicted RSRP [for inference] | 1. Support of beam prediction, reporting of predicted beams and predicted RSRP, for BM-Case2 (spatial and time domain beam prediction) [for inference] | 58-1-4 | yes | n/a | UE-side beam prediction for BM-Case2 [for inference] is not supported | FFS Per UE | FFS No | FFS No | FFS No |  | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506605](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506605.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122:9.1:028` · 관련 주제: CSI-RS · UE features (FG)

구현 영향: UE capability·FG, 포트·자원·레이어 수

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_air | 58-1-7 | Data collection for UE-side beam prediction [for BM case 1] | 1. Support of data collection for UE-side beam prediction [for BM case 1] 2. Support of SS/PBCH block and 1-port CSI-RS based RSRP measurements for measurement RS resource sets (Set B and Set A) for data collection 3. Supported sub-use cases 6: Supported maximum number of resources for Set B 7: Supported maximum number of resources for Set A 8. Support of SSB as RS type for Set B 9. Support of CSI-RS as RS type for Set B 10. Support of SSB as RS type for Set A 11. Support of CSI-RS as RS type for Set A | FFS | yes | n/a | Data collection for UE-side beam prediction is not supported [for BM case 1] | Per UE | N/A | N/A | N/A | Component 3 candidate values: {‘Set B equal to Set A’, ‘Set B subset of Set A’, ’Set B not a subset of Set A’} Component 6 candidate values: {4, 8, 16, 32, 64} Component 7 candidate values: {8, 16, 32, 64} Note: it is up to RAN2 whether this FG is merged into data collection FG defined by RAN2 | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506605](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506605.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122:9.1:029` · 관련 주제: CSI-RS · UE features (FG)

구현 영향: UE capability·FG, 포트·자원·레이어 수

> Introduce the following Rel. 19 UE FGs (yellow highlighting, if any, shows text that’s not yet agreed)
> | 58. NR_AIML_air | 58-1-6 | Performance monitoring for UE-sided model | 1. Support of performance monitoring with RS-PAI of AI/ML model for beam prediction. 2. Maximum total number of the configured CSI-RS resources for monitoring RS resource set 3. Maximum number of monitoring report(s) configured per BWP 4. Maximum number of monitoring report(s) configured across all CCs 5. Maximum number of monitoring occasions for RS-PAI calculation | FFS | yes | n/a | Performance monitoring for UE-sided model is not supported | FFS | FFS | FFS | FFS | FFS: component candidate values | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506605](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506605.zip)

**Agreement** · `9.1` UE features for AI/ML for NR Air Interface · `RAN1#122:9.1:030` · 관련 주제: CSI 보고/codebook · UE features (FG)

구현 영향: 포트·자원·레이어 수

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_Air | 58-3-5 | Performance monitoring for CSI prediction model | 1. Supported number of two performance metric SGCS 2. Support of one wideband frequency granularity SGCS per layer 3. Support of one configured time instance for N4>1 4. A list of supported combinations, each combination is {Max # of Tx ports in one resource, Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously | 58-3-1 | Yes | n/a | Performance monitoring for CSI prediction model is not supported | Per Band and Per BC | N/A | N/A | N/A | Component 1 candidate values: {1,2} Component 4 candidate values: - Maximum 16 triplets - Max # of Tx ports in one resource: {4,8,12,16,24,32} - Max # resources: {1 to 64} - Max # total ports: {4 to 256} Note: If the UE reports candidate value ‘1’ for component 1 then the SGCS is for the predicted CSI | Optional with capability signalling |

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506605](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506605.zip)

**Agreement** · `10.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#122:10.1.1:001` · 관련 주제: SRS, CSI 보고/codebook · 규격 작업 (WI)

> For CSI feedback via two-sided model, support at least precoding matrix as target CSI type.
> - FFS whether consider raw channel matrix as further improvement, starting with evaluations, e.g. potential fusion with SRS measurement (SRS period/hopping, DL/UL reciprocity), frequency granularity of channel matrix, number of Rx antennas, etc.

FFS 1줄

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506496](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506496.zip)

**Agreement** · `10.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#122:10.1.1:002` · 규격 작업 (WI)

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> Specify the precoding matrix feedback via two-sided model as follows: For a certain layer  and rank ,
> - A precoding matrix is mapped with a latent message , with l = 1, ..., v where l is the layer index.
>   - The mapping is subject to [at least] a pairing ID configured by high-layer signalling.
>   - FFS  is common or specific for different layers or ranks
>   - Note: the terminology “latent message” is used for discussion purposes, the detailed name can be discussed further
> - is quantized and mapped to bit sequence before reporting.

FFS 1줄

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506496](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506496.zip)

**Agreement** · `10.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#122:10.1.1:003` · 규격 작업 (WI)

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> For precoding matrix feedback, for a certain layer  of rank , the latent message  contains  real values
> - If scalar quantization (SQ) supported, it refers to the quantization of each real value independently,
>   - The payload size for layer  and rank  is determined by , where  is the number of bits per scalar.
> - If vector quantization (VQ) is supported, it refers to the quantization of a segment of L (L>1) consecutive real values jointly, and the segment(s) are separately quantized.
>   - The payload size for layer  and rank  is determined by , where  is the length of the vector segment,   is the number of bits per segment
>   - Note: Combining two real-values as a complex value and performing amplitude-phase quantization is precluded.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506497](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506497.zip)

**Agreement** · `10.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#122:10.1.1:004` · 규격 작업 (WI)

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> For precoding matrix feedback, consider the following aspects for payload determination
> - Support only SQ, or only VQ or both
> - and / or  and / or  are fixed values or determined from multiple values based on NW configuration or UE reporting.
> - and / or  is layer-common or layer-specific, rank-common or rank-specific.
> - If configured, and / or  and / or  above are configured separately from pairing ID, or configured by Pairing ID.
>   - The configuration may be via other parameters which are used to derive , L and .
> Note: Consider limiting the total number of possible payload sizes considering the inter-vendor training challenges.
> Note: ,  and  are independent on subband and port configurations,
> - FFS each combination of ,  and is applicable to a certain set of subband and port configurations

FFS 1줄

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506497](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506497.zip)

**Agreement** · `10.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#122:10.1.1:005` · 규격 작업 (WI)

> For inference report configuration, support separate configuration of subband, Tx port and payload size from pairing ID.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506498](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506498.zip)

**Agreement** · `10.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#122:10.1.1:006` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> For quantization codebook used for quantizing the feedback,
> - For inter-vendor collaboration Direction A, select one of the following:
>   - Alt1: Exchange quantization codebook from NW-side to UE-side along with each exchanged dataset or model parameters
>   - Alt2: Use a standardized quantization codebook decided by RAN1.
> Including NW and UE data collection for training, performance monitoring, as well as model pairing related issues.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506498](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506498.zip)

**Agreement** · `10.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#122:10.1.1:007` · 관련 주제: Beam management, CSI 보고/codebook · 규격 작업 (WI)

> For model pairing procedure for inference, consider the applicability report procedure of Rel-19 AI/ML beam management for UE side model as a starting point.
> - Pairing ID(s) (i.e., ID for pairing related discussion) is indicated (e.g., in CSI-reportConfig) in Step 3.
>   - FFS whether/how to link the Pairing ID with the inter-vendor collaboration
>   - FFS whether/how Paring ID(s) are reported in Step 4
> - FFS whether to support both Option A (CSI-ReportConfig for inference configuration) and Option B (sets of inference related parameters for applicability report only).
>   - FFS CSI compression specific inference configuration or inference related parameters.

FFS 4줄

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506482](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506482.zip)

**Agreement** · `10.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#122:10.1.1:008` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> For NW side data collection of CSI compression, discuss the content and format of the collected data by assuming higher layer based signalling.
> - Details on signaling is up to RAN2.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506482](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506482.zip)

**Agreement** · `10.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#122:10.1.1:009` · 관련 주제: CSI 보고/codebook, CSI-RS · 규격 작업 (WI)

> To enable UE side data collection, CSI-ReportConfig can be used for configuring the resources for data collection purpose without CSI report
> - P-CSI-RS and /SP CSI-RS are supported

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506482](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506482.zip)

**Agreement** · `10.1.1` CSI spatial/frequency compression without temporal aspects (“Case 0”) · `RAN1#122:10.1.1:010` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

구현 영향: 메모리·복잡도

> For NW side data collection, study the solution for quantizing Target CSI, from the aspects of overhead, quantization loss/performance, and complexity. E.g.,:
> - Option 0: Reusing legacy e-Type II codebook
> - Option 1: Scalar quantization to the Target CSI. FFS number of bits for real/imaginary, whether coefficients for quantization are obtained from transformation of Target CSI.
> - Option 2: Enhanced methods to reduce the SVD/EVD decomposition complexity, reduce frequency/spatial/beam domain basis searching, with potentially relaxed overhead, e.g., Type II like codebook with scalar quantized W2 similar to Option 1 scalar quantization.
> - Option 3: Enhanced method for improved overhead saving, e.g., reporting the dominant eigenvalues/eigenvectors of per layer precoding matrix.
> - Option 4: eType II like codebook with new parameter values (e.g. larger L, pv, beta, amplitude, phase)
> - Note: the quantizaton format should consider the maximum payload size per reporting (e.g., 9KBytes) of the current higher layer signaling.
> - Note: At least take precoding matrix as Target CSI type. FFS channel matrix.
> - FFS: EVM, metric, benchmark (e.g., FP32, eT2 with PC6/8), by reusing R18 study EVM as baseline.

FFS 1줄

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506485](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506485.zip)

**Agreement** · `10.1.2` Inter-vendor training collaboration for two-sided AI/ML models · `RAN1#122:10.1.2:001` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

구현 영향: 포트·자원·레이어 수

> For Option 4-1 under Direction A in AI/ML based CSI compression, support at least target CSI and CSI feedback in the exchanged dataset(s).
> - FFS: Target CSI type and format
> - FFS: CSI feedback type and format
> - FFS: Association between Target CSI and CSI feedback, including mapping for different number of Tx port, number of sub bands, and CSI payload size.

FFS 3줄

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506468](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506468.zip)

**Agreement** · `10.1.2` Inter-vendor training collaboration for two-sided AI/ML models · `RAN1#122:10.1.2:002` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> For Option 4-1 under Direction A in AI/ML based CSI compression, consider  the following methods for performance target in the exchanged dataset,
> - SGCS
>   - FFS: Average SGCS
>   - FFS: SGCS values at X-percentiles
> - NMSE:
>   - FFS: When the exchanged CSI feedback is the floating-point values at the input of quantization
>   - FFS: When the exchanged CSI feedback is the binary bit sequence at the output of quantization, the binary sequence will be mapped back to the floating-point values via quantization codebook
> - FFS: Multiple performance targets for different layer when the target CSI type is precoding matrix, different configurations such as antenna ports, subband configuration and payload size configuration

FFS 5줄

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506468](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506468.zip)

**Agreement** · `10.1.2` Inter-vendor training collaboration for two-sided AI/ML models · `RAN1#122:10.1.2:003` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> For Option 4-1 under Direction A in AI/ML based CSI compression, for CSI feedback type and format, down select one of the following options:
> - Option 1: The exchanged CSI feedback is the latent message before quantization.
> - Option 2: The exchanged CSI feedback is the binary sequence at the output of quantization.
> - Note: Quantization codebook is exchanged in addition if not specified in the spec.
> - Note: Whether or not using the Quantization codebook for model training, is up to UE implementation.

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506470](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506470.zip)

**Agreement** · `10.1.2` Inter-vendor training collaboration for two-sided AI/ML models · `RAN1#122:10.1.2:004` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

구현 영향: 포트·자원·레이어 수

> For Option 4-1 under Direction A in AI/ML based CSI compression, support exchange of single pairing ID along with dataset exchange.
> - One pairing ID is assigned to one dataset.
>   - The dataset can have different number of Tx port, number of subbands, and CSI payload size configurations (including different quantization codebooks if needed).
> - From RAN1 perspective, the uniqueness of the pairing ID needs further studied.
> - FFS: the impact on pairing ID(s) when additional data samples are added to an exchanged dataset, if supported.

FFS 1줄

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506470](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506470.zip)

**Agreement** · `10.1.2` Inter-vendor training collaboration for two-sided AI/ML models · `RAN1#122:10.1.2:005` · 관련 주제: CSI 보고/codebook · 규격 작업 (WI)

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> For Option 4-1 under Direction A in AI/ML based CSI compression,  if the quantization codebook for CSI feedback is not fixed by the specification, support exchange of quantization codebook along with dataset exchange,
> - FFS: Quantization codebook exchange method (e.g, look up table, , or how to exchange quantization codebook related information, or other methods)
> - FFS: Common or different quantization codebook for different CSI payload size
> - Note: leveraging the discussion in agenda item 10.1.1.1 when applied

FFS 2줄

출처: [Chair notes RAN1#122 eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Inbox/Chair_notes/Chair%20notes%20RAN1%23122%20eom.zip) · [R1-2506470](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_122/Docs/R1-2506470.zip)

---

## 관련 결정 14건 (주된 주제는 다른 주제)

원문에 AI/ML CSI 관련 표현이 있지만 주된 주제가 다른 확정 결정입니다. 전문은 각 주된 주제 리포트에 있습니다.

| 회의 | 구분 | 주된 주제 | Agenda | 원문 첫 줄 | 출처 |
|---|---|---|---|---|---|
| RAN1#126bis | Agreement | [Beam management](beam.md) | 10.5.3.4 Beam management for downlink and uplink | For the study on frequency domain beam measurement/prediction (cross-frequency), study both NW-side predictio… | [Chair notes RAN1#126bis_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom1.docx) · `[126bis-R20-6GR-Beam management]` |
| RAN1#126bis | Agreement | [Beam management](beam.md) | 10.5.3.4 Beam management for downlink and uplink | For the study on spatial/temporal domain DL Tx beam prediction and management on multi-TRP/cell(intra/inter-c… | [Chair notes RAN1#126bis_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom1.docx) · `[126bis-R20-6GR-Beam management]` |
| RAN1#126bis | Agreement | [SRS](srs.md) | 10.5.3.2 Aspects of uplink-based CSI acquisition | For the study of AI based receiver for SRS overhead reduction, the following template is used as a starting p… | [Chair notes RAN1#126bis_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom1.docx) · `[126bis-R20-6GR-Aspects of UL based CSI acquisition]` |
| RAN1#126bis | Agreement | [Beam management](beam.md) | 10.5.1.1 Synchronization acquisition and beam measurement | Study Sub-case D in R1-2600986 with focusing on potential spec impact of AI/ML based spatial/temporal beam pr… | [Chair notes RAN1#126bis_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126b/Inbox/Chair_notes/Chair%20notes%20RAN1%23126bis_eom1.docx) · `[126bis-R20-6GR-Synchronization and Beam Measurement]` |
| RAN1#126 | Agreement | [Beam management](beam.md) | 10.5.3.4 Beam management for downlink and uplink | For the study on spatial/temporal/frequency domain beam measurement/prediction (relevant to AI/ML or non-AI/a… | [Chair notes RAN1#126_eom1](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_126/Inbox/Chair_notes/Chair%20notes%20RAN1%23126_eom1.docx) · `[126-R20-6GR-Beam management]` |
| RAN1#125 | Agreement | [SRS](srs.md) | 10.5.3.2 Aspects of uplink-based CSI acquisition | For the evaluation of scalability/generalization of AI/ML-based UL-based CSI acquisition, the evaluation meth… | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of UL based CSI acquisition]` |
| RAN1#125 | Agreement | [SRS](srs.md) | 10.5.3.2 Aspects of uplink-based CSI acquisition | For the evaluation of AI/ML-based UL-based CSI acquisition, | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of UL based CSI acquisition]` |
| RAN1#125 | Agreement | [SRS](srs.md) | 10.5.3.2 Aspects of uplink-based CSI acquisition | Study the following cases for AI/ML UL-based CSI, and strive to support the unified SRS patterns/designs/fram… | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Aspects of UL based CSI acquisition]` |
| RAN1#125 | Agreement | [Beam management](beam.md) | 10.5.2.4 Beam management for downlink and uplink | For the study on spatial/temporal/frequency domain beam measurement/prediction (relevant to AI/ML or non-AI/a… | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Beam management]` |
| RAN1#125 | Agreement | [Beam management](beam.md) | 10.5.2.4 Beam management for downlink and uplink | Regarding DL beam measurement and report procedure | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Beam management]` |
| RAN1#125 | Agreement | [Beam management](beam.md) | 10.5.2.4 Beam management for downlink and uplink | For the study on DL beam measurement and report (AI/ML-based or non-AI/ML-based) on the deployment scenarios … | [Chair notes RAN1#125_eom](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_125/Inbox/Chair_notes/Chair%20notes%20RAN1%23125_eom.docx) · `[125-R20-6GR-Beam management]` |
| RAN1#124bis | Agreement | [Beam management](beam.md) | 10.5.2.4 Beam management for downlink and uplink | For the study on spatial/temporal/frequency domain beam measurement/prediction (relevant to AI/ML or non-AI/a… | [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Beam management]` |
| RAN1#124 | Agreement | [Beam management](beam.md) | 10.5.2.4 Beam management for downlink and uplink | Study of UE-initiated/event-driven beam management (UEIBM) mechanisms for 6GR, covering at least the followin… | [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · `[124-R20-6GR-Beam management]` |
| RAN1#124 | Agreement | [Beam management](beam.md) | 10.5.2.4 Beam management for downlink and uplink | Study TCI/QCL-related aspects, e.g., definition of QCL/TCI-state, QCL property/chain | [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · `[124-R20-6GR-Beam management]` |

---

## 후보 5건 (키워드 일치 · 확인 필요)

포함 Agenda 밖에서 키워드로 잡힌 결정입니다. CSI 범위가 아닐 수 있습니다.

### RAN1#124bis — 1건

**Agreement** · `10.5.2.2` Downlink transmission scheme(s) for downlink shared channels · `RAN1#124bis:10.5.2.2:016` · 후보 · 관련 주제: CSI 보고/codebook, CSI-RS · Study

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> - Study PDSCH and RS for PDSCH based on the following SLS EVM assumptions
>   - Note: Additional EVM assumptions for AI/ML based DMRS overhead reduction can be further discussed.
>   - Note: EVM assumption for HST scenarios will be treated separately
> | Parameter | Value |
> | Carrier frequency and duplex | Around 0.7 GHz, FDD Around 2 GHz, FDD Around 4 GHz, TDD Around 7 GHz, TDD Around 30 GHz, TDD |
> | Subcarrier spacing | 15 kHz for FDD 30 kHz for TDD and around 2—7 GHz 120 kHz for TDD and around 30 GHz |
> | Waveform | CP-OFDM |
> | Channel model | TR 38.901 (Rel-19) |
> | Scenario | Suburban macro, 1732 m ISD (for around 0.7—4 GHz) Urban macro, 500 m ISD (for around 0.7—30 GHz) Dense urban, 200 m ISD (for around 4—30 GHz) Other scenarios are not precluded (companies to report) |
> | Bandwidth | 20 MHz (baseline) 100 MHz (for 4—7 GHz) (optional) Other bandwidths are not precluded (companies to report) |
> | Deployment | 7 x 3, single layer, hex grid (baseline) 19 x 3, single layer, hex grid (optional) |
> | BS transmit power (for 20 MHz) | For around 0.7—7 GHz 49 dBm for Suburban macro, 1732 m 46 dBm for Urban macro, 500 m 44 dBm for Dense urban, 200 m Note: BS Tx power scales up with bandwidth proportionally under the limitation of the maximum BS Tx power is 56 dBm for outdoor and 33 dBm for indoor for the above carrier frequencies. For around 30 GHz 33 dBm for all scenarios Other BS transmit powers are not precluded (companies to report) |
> | BS transmit power constraint | Total transmit power constraint (baseline) Per-TXRU transmit power constraint (optional) |
> | BS antenna configuration | Around 0.7 GHz: 4 TXRUs, 32AEs, (M, N, P, Mg, Ng; Mp, Np) = (8, 2, 2, 1, 1; 1, 2), (dH, dV) = (0.5, 0.5), (“Baseline Configuration”) Around 2 GHz: 4 TXRUs, 32 AEs, (M, N, P, Mg, Ng; Mp, Np) = (8, 2, 2, 1, 1; 1, 2), (dH, dV) = (0.5, 0.5), (“Outdoor Combination 1”) 32 TXRUs, 128 AEs, (M, N, P, Mg, Ng; Mp, Np) = (8, 8, 2, 1, 1; 2, 8), (dH, dV) = (0.5, 0.5) 64 TXRUs, 192 AEs, (M, N, P, Mg, Ng; Mp, Np) = (12, 8, 2, 1, 1; 4, 8), (dH, dV) = (0.5, 0.5), (“Outdoor Combination 2”) Around 4 GHz: 4 TXRUs, 32 AEs, (M, N, P, Mg, Ng, Mp, Np) = (8, 2, 2, 1, 1; 1, 2), (dH, dV) = (0.5, 0.8), (“Outdoor Combination 0”) 32 TXRUs, 128 AEs, (M, N, P, Mg, Ng, Mp, Np) = (8, 8, 2, 1 ,1; 2, 8), (dH, dV) = (0.5, 0.8) , (“Indoor Combination 1”) 64 TXRUs, 192AEs, (M, N, P, Mg, Ng; Mp, Np) = (12, 8, 2, 1, 1, 4, 8). (dH, dV) = (0.5, 0.8), (“Outdoor Combination 1”) Around 7 GHz: Details follow corresponding agreements in Agenda 10.1 Around 30 GHz 4 TXRUs, 1024 AEs, (M, N, P, Mg, Ng, Mp, Np) = (16, 16, 2, 2, 1; 1, 1), (dH, dV) = (0.5, 0.5) , (“Outdoor Combination 3”) 16 TXRUs, 2048 AEs, (M, N, P, Mg, Ng, Mp, Np) = (16, 8, 2, 4, 2; 1, 1), (dH, dV) = (0.5, 0.5) , (“Outdoor Combination 1”) Other antenna configurations are not precluded (companies to report) |
> | BS mechanical/electrical tilt | Mechanical tilt: 90° in GCS Electrical tilt: Company to report Other mechanical tilts are not precluded (companies to report) |
> | UE antenna configuration (IoT) | Details follow corresponding agreements in Agenda 10.1 |
> | UE antenna configuration (handheld) | Details follow corresponding agreements in Agenda 10.1 |
> | CPE configuration | Details follow corresponding agreements in Agenda 10.1/10.5.2.3 |
> | UE speed (handheld) | Urban macro and dense urban: 80% indoor in buildings (3 km/h), 20% outdoor in cars (30km/h) Suburban macro: 80% indoor in buildings (3 km/h), 20% outdoor in cars (40km/h) |
> | Traffic model | NFB FTP model 1/3 with 500 kB packet size 20%, 50%, and 70% resource utilization FTP 3-extension 1 model can be optionally considered 10 or 30 UEs per cell for applicable models FB model can be optionally considered, for technical performance requirements (TPR) Other traffic models and packet sizes are not precluded (companies to report) |
> | Scheduler | PF |
> | MIMO scheme | Reported by companies |
> | Receiver | MMSE-IRC (baseline) R-ML (Reported by companies) |
> | DMRS channel estimation | Realistic |
> | CSI-RS channel estimation | Realistic |
> | Inter-cell interference estimation | Realistic |
> | Inter-cell interference model | Explicit |
> | CSI-RS periodicity | 10 ms (optional) 20 ms (baseline) |
> | CSI delay | 4 ms |
> | Phase errors for radios with uncalibrated antennas (for 4 TXRUs) | Wideband phase error between Tx antenna port 0 and Tx antenna port () can be modeled as follows: Independent random phase offset uniformly distributed between 0 and 2π between any two Tx antenna ports. |
> | Backhaul assumption | Ideal backhaul (baseline) Non-ideal backhaul (optional) |
> | Performance metric | Throughput Other performance metrics are not precluded (companies to report) |
> | Multi-TRP (e.g., CJT) scenario | For evaluation of multi-TRP under single layer deployment, consider multi-TRP Scenario 1, 2, and 3, with Same antenna configuration and Tx power is assumed across TRPs. Note: other multi-TRP scenarios are not precluded Note: TRP assumption for HST scenarios will be treated separately |
> | Multi-TRP Scenario 1: Intra-cell scenario, with 4 TRPs/RRHs per multi-TRP set | Multi-TRP Scenario 2: Intra-site, inter-cell, with 3 TRPs per cooperative set (as baseline) | Multi-TRP Scenario 3: Inter/intra-site, inter-cell with TRPs per cooperative set |
> |  |  | Companies report the setting when N>1 |

출처: [Chair notes RAN1#124bis_eom5](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124b/Inbox/Chair_notes/Chair%20notes%20RAN1%23124bis_eom5.docx) · `[124b-R20-6GR-Transmission scheme for DL shared channel]`

### RAN1#124 — 1건

**Agreement** · `10.5.2.2` Downlink transmission scheme(s) for downlink shared channels · `RAN1#124:10.5.2.2:001` · 후보 · 관련 주제: CSI 보고/codebook, CSI-RS · Study

> ⚠️ 수식 누락 의심 — 원본 추출에서 Word 수식(변수·기호)이 빠졌을 수 있습니다. Chair notes 원문으로 확인하세요.

> - Study PDSCH and RS for PDSCH based on the following SLS EVM assumptions
>   - Note: Additional EVM assumptions for AI/ML based DMRS overhead reduction can be further discussed.
>   - Note: EVM assumption for HST scenarios will be treated separately
> | Parameter | Value |
> | Carrier frequency and duplex | Around 0.7 GHz, FDD Around 2 GHz, FDD Around 4 GHz, TDD Around 7 GHz, TDD Around 30 GHz, TDD |
> | Subcarrier spacing | 15 kHz for FDD 30 kHz for TDD and around 2—7 GHz 120 kHz for TDD and around 30 GHz |
> | Waveform | CP-OFDM |
> | Channel model | TR 38.901 (Rel-19) |
> | Scenario | Suburban macro, 1732 m ISD (for around 0.7—4 GHz) Urban macro, 500 m ISD (for around 0.7—30 GHz) Dense urban, 200 m ISD (for around 4—30 GHz) Other scenarios are not precluded (companies to report) |
> | Bandwidth | 20 MHz (baseline) 100 MHz (for 4—7 GHz) (optional) Other bandwidths are not precluded (companies to report) |
> | Deployment | 7 x 3, single layer, hex grid (baseline) 19 x 3, single layer, hex grid (optional) |
> | BS transmit power (for 20 MHz) | For around 0.7—7 GHz 49 dBm for Suburban macro, 1732 m 46 dBm for Urban macro, 500 m 44 dBm for Dense urban, 200 m Note: BS Tx power scales up with bandwidth proportionally under the limitation of the maximum BS Tx power is 56 dBm for outdoor and 33 dBm for indoor for the above carrier frequencies. For around 30 GHz 33 dBm for all scenarios Other BS transmit powers are not precluded (companies to report) |
> | BS transmit power constraint | Total transmit power constraint (baseline) Per-TXRU transmit power constraint (optional) |
> | BS antenna configuration | Around 0.7 GHz: 4 TXRUs, 32AEs, (M, N, P, Mg, Ng; Mp, Np) = (8, 2, 2, 1, 1; 1, 2), (dH, dV) = (0.5, 0.5), (“Baseline Configuration”) Around 2 GHz: 4 TXRUs, 32 AEs, (M, N, P, Mg, Ng; Mp, Np) = (8, 2, 2, 1, 1; 1, 2), (dH, dV) = (0.5, 0.5), (“Outdoor Combination 1”) 32 TXRUs, 128 AEs, (M, N, P, Mg, Ng; Mp, Np) = (8, 8, 2, 1, 1; 2, 8), (dH, dV) = (0.5, 0.5) 64 TXRUs, 192 AEs, (M, N, P, Mg, Ng; Mp, Np) = (12, 8, 2, 1, 1; 4, 8), (dH, dV) = (0.5, 0.5), (“Outdoor Combination 2”) Around 4 GHz: 4 TXRUs, 32 AEs, (M, N, P, Mg, Ng, Mp, Np) = (8, 2, 2, 1, 1; 1, 2), (dH, dV) = (0.5, 0.8), (“Outdoor Combination 0”) 32 TXRUs, 128 AEs, (M, N, P, Mg, Ng, Mp, Np) = (8, 8, 2, 1 ,1; 2, 8), (dH, dV) = (0.5, 0.8) , (“Indoor Combination 1”) 64 TXRUs, 192AEs, (M, N, P, Mg, Ng; Mp, Np) = (12, 8, 2, 1, 1, 4, 8). (dH, dV) = (0.5, 0.8), (“Outdoor Combination 1”) FFS: Around 7 GHz: 128 TXRUs, 768 AEs, (M, N, P, Mg, Ng, Mp, Np) = (24, 16, 2, 1, 1; 4, 16), (dH, dV) = (0.5, 0.8), (“Outdoor Combination 1”) 256 TXRUs, 1024 AEs, (M, N, P, Mg, Ng, Mp, Np) = (32, 16, 2, 1, 1; 8, 16), (dH, dV) = (0.5, 0.8), (“Outdoor Combination 2”) 512 TXRUs, 2048AEs, (M, N, P, Mg, Ng; Mp, Np) = (64, 16, 2, 1, 1, 16, 16), (dH, dV) = (0.5, 0.5), (“Outdoor Combination 5”) 256 TXRUs, 1536 AEs, (M, N, P, Mg, Ng; Mp, Np) = (48, 16, 2, 1, 1, 8, 16). (dH, dV) = (0.5, 0.8), (“Outdoor Combination 3”) 128 TXRUs, 2048AEs, (M, N, P, Mg, Ng; Mp, Np) = (64, 16, 2, 1, 1, 8, 8), (dH, dV) = (0.5, 0.5) Around 30 GHz 4 TXRUs, 1024 AEs, (M, N, P, Mg, Ng, Mp, Np) = (16, 16, 2, 2, 1; 1, 1), (dH, dV) = (0.5, 0.5) , (“Outdoor Combination 3”) 16 TXRUs, 2048 AEs, (M, N, P, Mg, Ng, Mp, Np) = (16, 8, 2, 4, 2; 1, 1), (dH, dV) = (0.5, 0.5) , (“Outdoor Combination 1”) Other antenna configurations are not precluded (companies to report) |
> | BS mechanical/electrical tilt | Mechanical tilt: 90° in GCS Electrical tilt: Company to report Other mechanical tilts are not precluded (companies to report) |
> | UE antenna configuration (IoT) | Details follow corresponding agreements in Agenda 10.1 |
> | UE antenna configuration (handheld) | Details follow corresponding agreements in Agenda 10.1 |
> | FFS: CPE configuration | Details follow corresponding agreements in Agenda 10.1 |
> | UE speed (handheld) | Urban macro and dense urban: indoor (3 km/h), outdoor (30km/h) Suburban macro: indoor (3 km/h), outdoor (40km/h) |
> | Traffic model | FFS: NFB, FTP 1, 500 kB FFS: NFB, FTP 3, 500 kB FFS: FB and EFTP Other traffic models and packet sizes are not precluded (companies to report) |
> | Resource utilization | FFS: 20%, 50%, 70% |
> | Number of UEs per cell | FFS: 10 or 30 (for FTP 3) |
> | Scheduler | PF |
> | MIMO scheme | Reported by companies |
> | Receiver | MMSE-IRC (baseline) R-ML (Reported by companies) |
> | DMRS channel estimation | Realistic |
> | CSI-RS channel estimation | Realistic |
> | Inter-cell interference estimation | Realistic |
> | Inter-cell interference model | Explicit |
> | CSI-RS periodicity | 10 ms (optional) 20 ms (baseline) |
> | CSI delay | 4 ms |
> | Phase errors for radios with uncalibrated antennas (for 4 TXRUs) | Wideband phase error between Tx antenna port 0 and Tx antenna port () can be modeled as follows: in following two ways: Case 1: Independent random phase offset uniformly distributed between 0 and 2π between any two Tx antenna ports. |
> | Backhaul assumption | Ideal backhaul (baseline) Non-ideal backhaul (optional) |
> | Performance metric | Throughput Other performance metrics are not precluded (companies to report) |
> | Multi-TRP (e.g., CJT) scenario | Reuse AI 10.5.3.1 (DL CSI) as reference and consider potential more TRPs than 3 |

출처: [Chair notes RAN1#124 - eom_03](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_124/Inbox/Chair_notes/Chair%20notes%20RAN1%23124%20-%20eom_03.docx) · `[124-R20-6GR-Transmission scheme for DL shared channel]`

### RAN1#123 — 3건

**Conclusion** · `8.1` Maintenance on Artificial Intelligence (AI)/Machine Learning (ML) for NR Air Interface · `RAN1#123:8.1:002` · 후보 · 유지보수 (CR)

구현 영향: 처리 시간·CPU

> - No further discussion in RAN1 on APU framework for Rel-19 AI/ML positioning.

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · [R1-2509515](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Docs/R1-2509515.zip) · `[123-R19-AI/ML]`

**Agreement** · `9.3` UE features Batch C · `RAN1#123:9.3:002` · 후보 · 관련 주제: CSI 보고/codebook · UE features (FG)

구현 영향: 처리 시간·CPU, UE capability·FG, 포트·자원·레이어 수, 측정·보고량

> ⚠️ 색 표시 손실 — 원문은 추가·삭제를 색으로 표시했지만 추출된 글에는 색이 없습니다. TDoc에서 확인하세요.

> Adopt the following changes highlighted in chromatic fonts, while keeping the yellow highlighting, if any, as shown
> | 58. NR_AIML_Air | 58-3-1 | CSI prediction for UE-sided inference when N4=1 | 1. Support of CSI prediction for UE-sided inference when N4=1 2. Support for reporting predicted PMI with N4=1 3. A list of supported combinations, each combination is { Max # of Tx ports in one resource, Max # of resources and total # of Tx ports} across all CCs in a band when reported per band, and across all CCs in a band combination when reported per BC simultaneously 4. Support of Rel-16 eType-II regular codebook refinement for predicted PMI with PMI subband R=1 5. Support parameter combinations with L=2,4 6. Support for rank = 1,2 7. Support for the size of DD-basis, N4=1 8. Support X=1 CQI based on the first/earliest slot of the CSI reporting window and the first/earliest predicted PMI (TDCQI=’1-1’) 11. Scaling factor for active resource counting Kp 12. supported value of ti for the relaxation of Z and Z’ timeline, where i is the index of SCS, i=1,2,3,4,5,6 corresponding to 15,30,60,120,480,960 kHz SCS 13. supported number of occupied CPU 14. supported number of occupied CPU,2/CPU,3 15. Occupied resource pool between CPU,2 and CPU,3 16. Inference report type | 2-35 | yes | n/a | CSI prediction for N4=1 for inference is not supported | Per band and Per BC | n/a | n/a | n/a | Component 3 candidate values: a. {4,8,12,16,24,32} b. {2,3,4 … 64} c. {4, …, 256} Component 11 candidate values: {1,2,4} Component 12 candidate values: FFS t1 is {14, 28, 56, 112} t2 is {28, 56, 112, 224} t3 is {56, 112, 224, 448} t4 is {112, 224, 448} t5 is {448, 896, 1792} t6 is {896, 1792} Component 13 candidate values: {0, 1, 2, … 8} Component 14 candidate values: {0, 1, 2, … 8} Component 15 candidate values: {1, 2} representing the first CPU pool (i.e., CPU,2) and the second CPU pool (i.e., CPU,3), respectively. Component 15 candidate values: {aperiodic, semi-persistent} Note: UE should not report non-zero value for Component 14 if FG 58-0-1 is not signaled | Optional with capability signalling |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx)

**Agreement** · `11.6` AI/ML in 6GR interface · `RAN1#123:11.6:001` · 후보 · 관련 주제: SRS, Beam management, CSI 보고/codebook, CSI-RS · Study

> From RAN 1 perspective, the following use cases can be matched to the identified primary agendas of RAN1
> | Use cases | Use cases | Use cases | Primary agendas |
> | Low overhead CSI-RS or CSI prediction with AI/ML | Low overhead CSI-RS or CSI prediction with AI/ML | Low overhead CSI-RS or CSI prediction with AI/ML | CSI-RS and CSI acquisition |
> | Low overhead DMRS with AI/ML receiver | Low overhead DMRS with AI/ML receiver | Low overhead DMRS with AI/ML receiver | UL & DL DMRS associated with PUSCH/PDSCH Note: Sub-Case C: DMRS-free may be related to modulation |
> | CSI compression and feedback | CSI compression and feedback | CSI compression and feedback | CSI acquisition Note: this may be related to uplink control |
> | AI/ML for beam management and extension | AI/ML for beam management and extension | AI/ML for beam management and extension | Initial access for Sub-case D Beam management for other sub-cases Note: sub-case A/B/D maybe related to mobility |
> | AI/ML for SRS | AI/ML for SRS | Low overhead SRS with AI/ML | SRS |
> | AI/ML for SRS | AI/ML for SRS | Low PAPR SRS sequence design | SRS |
> | AI/ML for SRS | AI/ML for SRS | AI/ML based SRS power imbalance compensation | Not RAN1-led |
> | AI-enabled UL precoder indication | AI-enabled UL precoder indication | AI-enabled UL precoder indication | UL MIMO |
> | AI-based non-linearity handling at transmitter or receiver | AI-based non-linearity handling at transmitter or receiver | AI-based non-linearity handling at transmitter or receiver | Not RAN1-led Note: this may be related to DMRS, SRS, Power control in RAN 1 |
> | AI/ML for (de)modulation | AI/ML for (de)modulation | AI/ML for (de)modulation | modulation Note: Sub-case B may be related to MIMO Note: assuming no change to DMRS |
> | AI/ML based waveform for PAPR reduction | AI/ML based waveform for PAPR reduction | AI/ML based waveform for PAPR reduction | Waveform |
> | AI/ML based HARQ-ACK feedback | AI/ML based HARQ-ACK feedback | AI/ML based HARQ-ACK feedback | Channel coding Note: this may be related to uplink control |
> | PDCCH related | PDCCH related | Prior-Information-Aided DCI Decoding | DL control |
> | PDCCH related | PDCCH related | Lossless DCI Compression | DL control |
> | Power control related | Power control related | UL closed-loop power control | Power control |
> | Power control related | Power control related | Pathloss prediction | Power control |
> | RACH related design | RACH related design | Early contention resolution in RACH | Random access/PRACH |
> | RACH related design | RACH related design | Low PAPR PRACH sequence design | Random access/PRACH |
> | Site Specific Learning for AI/ML using RAN Digital Twin | Site Specific Learning for AI/ML using RAN Digital Twin | Site Specific Learning for AI/ML using RAN Digital Twin | Depending on corresponding use case where site specific learning is applicable, e.g., DMRS |
> | Digital twin construction related use cases | AI/ML-enabled RAN digital twin with distributed model | AI/ML-enabled RAN digital twin with distributed model | ISAC |
> | Digital twin construction related use cases | Sensing based RAN digital twin construction with NW-side AI/ML model | Sensing based RAN digital twin construction with NW-side AI/ML model | ISAC |
> | AI for positioning | AI for positioning | AI for positioning | Positioning related agenda, if any |
> | To accommodate AI/ML service, e.g., token traffic | if any impact, most likely scheduling/HARQ |
> | To accommodate AI/ML service, e.g., token traffic | if any impact, most likely scheduling/HARQ |

출처: [Chair notes RAN1#123 - eom3](https://www.3gpp.org/ftp/tsg_ran/WG1_RL1/TSGR1_123/Inbox/Chair_notes/Chair%20notes%20RAN1%23123%20-%20eom3.docx) · `[123-R20-6GR-AI/ML]`
