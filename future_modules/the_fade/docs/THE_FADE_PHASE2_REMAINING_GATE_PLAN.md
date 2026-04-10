# THE FADE — Phase 2 remaining gate completion plan (LOCKED)

**Prompt #:** 417 (checkpoint note — plan file still Phase **2** authority framing)  
**Phase #:** 2  
**Tranche #:** 34A (plan lock only — no execution in #134)  

**Updated:** 2026-04-09T22:00:00+00:00 (post–**T117** **#417** — **`THE_FADE_T117_FIRST_REAL_SCANNER_RULE_GOVERNANCE.md`** + **`THE_FADE_T117_FIRST_REAL_SCANNER_RULE_ACCEPTANCE_CRITERIA.md`** + **`config/phase3_t117_first_real_scanner_rule.json`** + **`post_t117_first_real_scanner_rule_governance`**; **first real scanner rule** governed; **no** **`build_first_real_scanner_rule_from_run_folder.py`** in **T117**; **T116** capture remains on disk; scoped MVP approval unchanged; no lane reopen; AI/scanner loop/runtime **platform**/provider/dashboard **platform** still blocked; broader implementation remains unauthorized without new governance)  

**Authority:** Binding **scoped** MVP approval state is **`mvp_lane_approval.json`** (updated in **T80**; **not** edited in **T82**). This plan file is a **locked historical sequence** and honest partiality accounting — it is **not** the approval flip mechanism.

---

## Why this exists

Phase 2 work stayed bounded but became **reactive tranche-by-tranche**. This document **locks one ordered sequence** for **remaining** gate work so execution follows a **single plan** (like Phase 1 discipline), not ad-hoc discovery.

---

## Done / locked (do not re-open without governance)

- **Lane B FR full Tranche 21 window** on disk: **22**/**22** successes, **`t30_valid_002`** excluded from full-window tally; governed doc reconciliation (Prompt **#102**).
- **Phase 3 T86 second-slice governance (Prompt #354):** **`THE_FADE_T86_SECOND_SLICE_GOVERNANCE_OFFLINE_VALIDATION.md`** + **`THE_FADE_T86_SECOND_SLICE_ACCEPTANCE_CRITERIA.md`**; **`post_t86_second_slice_governance_offline_validation`** — **offline** validation boundary **locked**; **no** validator code in **T86**; **no** lane reopen.
- **Phase 3 T87 second-slice implementation (Prompt #358):** **`contracts/phase3_universe_scanner_io/tools/validate_universe_scanner_io_contracts.py`** + **`contracts/phase3_universe_scanner_io/tools/README.md`**; **`post_t87_offline_contract_validation_harness`** — offline contract validation harness delivered; no scanner/runtime/provider/dashboard code; no lane reopen.
- **Phase 3 T88 first live ingress governance (Prompt #359):** **`THE_FADE_T88_FIRST_LIVE_INGRESS_SLICE_GOVERNANCE.md`** + **`THE_FADE_T88_FIRST_LIVE_INGRESS_SLICE_ACCEPTANCE_CRITERIA.md`**; **`post_t88_first_live_ingress_slice_governance`** — one future Federal Register ingress slice authorized; no ingress implementation in T88; no lane reopen.
- **Phase 3 T89 first live Federal Register ingress slice (Prompt #360):** **`ingress/federal_register/build_universe_scanner_request_from_federal_register.py`** + **`ingress/federal_register/README.md`**; **`post_t89_first_live_federal_register_ingress_slice`** — bounded FR read-only ingress writes schema-valid request packet(s) under **`inputs/phase3_universe_scanner_requests/`**; no scanner/request-to-result/runtime/provider/dashboard code; no lane reopen.
- **Phase 3 T90 offline ingress-request validation governance (Prompt #365):** **`THE_FADE_T90_OFFLINE_VALIDATION_OF_INGRESS_REQUEST_PACKETS_GOVERNANCE.md`** + **`THE_FADE_T90_OFFLINE_VALIDATION_OF_INGRESS_REQUEST_PACKETS_ACCEPTANCE_CRITERIA.md`**; **`post_t90_offline_validation_of_ingress_request_packets_governance`** — **governance only**; one future tranche may add **`contracts/phase3_universe_scanner_io/tools/validate_ingress_request_packets.py`** only (ingress request JSON + request schema read-only); no scanner/result/runtime/provider/dashboard; no lane reopen; **executable** validator **not** in T90.
- **Phase 3 T91 offline ingress-request packet validator (Prompt #366):** **`contracts/phase3_universe_scanner_io/tools/validate_ingress_request_packets.py`** + **`tools/README_ingress_request_packets.md`**; **`post_t91_offline_ingress_request_packet_validator`** — validates root-level ingress `*.json` + optional **`fixtures_invalid/`**; no scanner/result/runtime/provider/dashboard; no lane reopen.
- **Phase 3 T93 offline UniverseScannerResult packet validation governance (Prompt #368, #369 Model B repair):** **`THE_FADE_T93_OFFLINE_VALIDATION_OF_UNIVERSE_SCANNER_RESULT_PACKETS_GOVERNANCE.md`** + **`THE_FADE_T93_OFFLINE_VALIDATION_OF_UNIVERSE_SCANNER_RESULT_PACKETS_ACCEPTANCE_CRITERIA.md`**; **`post_t93_offline_validation_of_universe_scanner_result_packets_governance`** — **governance only** in **T93**; authorizes **one** implementation tranche for the result-packet validator (**T94** executed that slice).
- **Phase 3 T94 offline UniverseScannerResult packet validator (Prompt #374):** **`contracts/phase3_universe_scanner_io/tools/validate_universe_scanner_result_packets.py`** + **`tools/README_universe_scanner_result_packets.md`**; **`post_t94_offline_universe_scanner_result_packet_validator`** — validates **`outputs/phase3_universe_scanner_results/`** root `*.json` + optional **`fixtures_invalid/`**; **empty-root PASS**; **Model B** cap; no request-to-result/scanner/runtime/provider/dashboard; no lane reopen.
- **Phase 3 T95 first request→result bridge governance (Prompt #375):** **`THE_FADE_T95_FIRST_REQUEST_TO_RESULT_BRIDGE_GOVERNANCE.md`** + **`THE_FADE_T95_FIRST_REQUEST_TO_RESULT_BRIDGE_ACCEPTANCE_CRITERIA.md`**; **`post_t95_first_request_to_result_bridge_governance`** — **governance only** in **T95**; authorizes **T96** implementation slice.
- **Phase 3 T96 first request→result bridge build (Prompt #378):** **`bridge/first_request_to_result/build_universe_scanner_result_from_single_request.py`** + **`bridge/first_request_to_result/README.md`**; **`post_t96_first_request_to_result_bridge`** — mechanical **one** request **in** / **one** result **out**; **`pending`** + **deferred** placeholders only; no network/scanner/runtime/provider/dashboard; no lane reopen.
- **Phase 3 T97 local end-to-end happy-path runner governance (Prompt #381):** **`THE_FADE_T97_LOCAL_END_TO_END_HAPPY_PATH_RUNNER_GOVERNANCE.md`** + **`THE_FADE_T97_LOCAL_END_TO_END_HAPPY_PATH_RUNNER_ACCEPTANCE_CRITERIA.md`**; **`post_t97_local_end_to_end_happy_path_runner_governance`** — **governance only** in **T97**; authorizes **one** future implementation tranche for **`runner/local_happy_path/run_local_end_to_end_happy_path.py`** (+ optional **`README.md`** + optional one tiny helper in same dir if strictly necessary); sequential subprocess calls to **T89** ingress → **T91** request validator → **T96** bridge → **T94** result validator; **no** runner code in T97; **no** scanner/runtime/provider/dashboard; **no** lane reopen.
- **Phase 3 T98 local end-to-end happy-path runner build (Prompt #384):** **`runner/local_happy_path/run_local_end_to_end_happy_path.py`**; **`post_t98_local_end_to_end_happy_path_runner_build`** — local-only sequential orchestration of existing tools (T89 ingress → T91 request validator → T96 bridge → T94 result validator), console summary + request/result path reporting + non-zero failure propagation; no scanner/ranking/selection logic; no runtime/provider/dashboard platform code; no lane reopen.
- **Phase 3 T107 operator review gate signal governance (Prompt #399):** **`THE_FADE_T107_OPERATOR_REVIEW_GATE_SIGNAL_GOVERNANCE.md`** + **`THE_FADE_T107_OPERATOR_REVIEW_GATE_SIGNAL_ACCEPTANCE_CRITERIA.md`**; **`post_t107_operator_review_gate_signal_governance`** — **governance only** in **T107**; **no** gate code in **T107**.
- **Phase 3 T108 operator review gate signal build (Prompt #400):** **`review/local_run/build_operator_review_gate_signal_from_run_folder.py`**; **`post_t108_operator_review_gate_signal_build`** — writes **`operator_review_gate.json`** per run folder; mechanical JSON reads only; no network/scanner/runtime/provider/dashboard; no lane reopen; no registry/approval edits.
- **Phase 3 T109 local operator review queue governance (Prompt #402):** **`THE_FADE_T109_LOCAL_OPERATOR_REVIEW_QUEUE_GOVERNANCE.md`** + **`THE_FADE_T109_LOCAL_OPERATOR_REVIEW_QUEUE_ACCEPTANCE_CRITERIA.md`**; **`post_t109_local_operator_review_queue_governance`** — **governance only** in **T109**; authorizes **T110** implementation slice.
- **Phase 3 T110 local operator review queue build (Prompt #403):** **`review/local_run/build_operator_review_queue.py`**; **`post_t110_local_operator_review_queue_build`** — writes **`outputs/local_happy_path_runs/operator_review_queue.json`**; scan **`run_*`** under **`outputs/local_happy_path_runs/`** only; read **`operator_review_gate.json`** + **`run_summary.json`** only (no **`source_snapshot.json`**); includes only folders with parsed gate JSON in **`runs`**; no network/scanner/runtime/provider/dashboard; no lane reopen; no registry/approval edits.
- **Phase 3 T111 first operator-meaningful filtering signal governance (Prompt #405):** **`THE_FADE_T111_FIRST_OPERATOR_MEANINGFUL_FILTERING_SIGNAL_GOVERNANCE.md`** + **`THE_FADE_T111_FIRST_OPERATOR_MEANINGFUL_FILTERING_SIGNAL_ACCEPTANCE_CRITERIA.md`**; **`post_t111_first_operator_meaningful_filtering_signal_governance`** — **governance only** in **T111**; authorizes **T112** implementation slice.
- **Phase 3 T112 first operator-meaningful filtering signal build (Prompt #407):** **`review/local_run/build_operator_attention_signal_from_run_folder.py`**; **`post_t112_first_operator_meaningful_filtering_signal_build`** — writes **`operator_attention_signal.json`** in the same **`run_<YYYYMMDDTHHMMSSZ>/`** folder; reads **`operator_review_gate.json`**, **`source_snapshot.json`**, and optionally **`run_summary.json`** per **T111** acceptance; closed **`operator_attention_status`** vocabulary and closed **`operator_attention_reasons`** codes; no AI/scanner/ranking/runtime/provider/dashboard; no lane reopen; no registry/approval edits.
- **Phase 3 T113 local operator attention queue governance (Prompt #409):** **`THE_FADE_T113_LOCAL_OPERATOR_ATTENTION_QUEUE_GOVERNANCE.md`** + **`THE_FADE_T113_LOCAL_OPERATOR_ATTENTION_QUEUE_ACCEPTANCE_CRITERIA.md`**; **`post_t113_local_operator_attention_queue_governance`** — **governance only** in **T113**; authorizes exactly one later build slice for **`review/local_run/build_operator_attention_queue.py`** writing **`outputs/local_happy_path_runs/operator_attention_queue.json`** from existing per-run attention artifacts only; no AI/scanner/ranking/runtime/provider/dashboard; no lane reopen; no registry/approval edits.
- **Phase 3 T114 local operator attention queue build (Prompt #411):** **`review/local_run/build_operator_attention_queue.py`**; **`post_t114_local_operator_attention_queue_build`** — writes **`outputs/local_happy_path_runs/operator_attention_queue.json`**; scans **`run_*`** under **`outputs/local_happy_path_runs/`** only; reads **`operator_attention_signal.json`** per folder only; stable timestamp-desc ordering; mechanical counts; no network/scanner/runtime/provider/dashboard; no lane reopen; no registry/approval edits.
- **Phase 3 T115 run-scoped source-record capture governance (Prompt #413):** **`THE_FADE_T115_RUN_SCOPED_SOURCE_RECORD_CAPTURE_GOVERNANCE.md`** + **`THE_FADE_T115_RUN_SCOPED_SOURCE_RECORD_CAPTURE_ACCEPTANCE_CRITERIA.md`** + **`config/phase3_t115_run_scoped_source_record_capture.json`**; **`post_t115_run_scoped_source_record_capture_governance`** — **governance only** in **T115**; authorizes **T116** implementation slice.
- **Phase 3 T116 run-scoped source-record capture build (Prompt #415):** **`review/local_run/build_source_records_snapshot_from_run_folder.py`** + **`review/local_run/README_source_records_snapshot.md`**; **`post_t116_run_scoped_source_record_capture_build`** — one read-only GET to Federal Register **`documents.json`** URL from on-disk **`candidate_source_packet_ref`** only; writes per-run **`source_records_snapshot.json`**; bounded factual fields; max **50** records; no pagination/subprocess ingress; no scanner/ranking/selection/AI; no lane reopen; no registry/approval edits.
- **Phase 3 T117 first real scanner rule governance lock (Prompt #417):** **`THE_FADE_T117_FIRST_REAL_SCANNER_RULE_GOVERNANCE.md`** + **`THE_FADE_T117_FIRST_REAL_SCANNER_RULE_ACCEPTANCE_CRITERIA.md`** + **`config/phase3_t117_first_real_scanner_rule.json`**; **`post_t117_first_real_scanner_rule_governance`** — **governance/docs only**; authorizes **exactly one** future implementation tranche for **`review/local_run/build_first_real_scanner_rule_from_run_folder.py`** writing **`first_real_scanner_rule_evaluation.json`** per run folder (mechanical rule over **`source_records_snapshot.json`** only; **no** network; **no** multi-rule engine); **no** rule script in **T117**; no lane reopen; no registry/approval edits.
- **Reliability slice (Lane B, FR window):** honest **22/22** statistic vs count floor; **not** whole-gate approval by itself.
- **Freshness (Lane B):** Tranches **31–32** executed; **Prompt #132** **adopts** **`strict_midnight_utc`**; **10**/**22** **`cannot_classify_honestly`** accepted; **freshness-only** tranches **parked** — `lane_b_phase2_freshness_policy_decision.json`.
- **Freshness policy exploration:** Tranche **33** comparator on disk; **no** alternate policy adopted as primary.
- **Normalization breadth (Lane B, same 22 rows):** Tranche **34** audit on disk — preview truncation documented; regex identity path **solid**; rich object **partial**. Tranche **58** adds a stored-slice truth pass showing exact collector retention plus partial normalization support, while still keeping full normalized-event materialization explicitly out of bounds on the current artifacts.
- **Lane B stale/outage & escalation alignment (bounded):** Tranche **35** executed (Prompt **#135**) — `audit_lane_b_stale_outage_escalation_alignment.py` + `tranche35_stale_outage_escalation_audit.*` on disk; standard **#4** still **partial** / not system-closed per artifact verdict.

---

## Still partial (known gaps — not “done”)

- **Lane B freshness:** **10**/**22** **cannot_classify_honestly** under adopted policy — dimension **partial**, not closed.
- **Lane B normalization:** Full API document **not** in stored previews — **breadth partial** per `tranche34_normalization_breadth_audit.*`. Tranche **50** adds a **bounded** normalization viability / silent-drop trace with explicit representative outcomes, and Tranche **58** adds a **stored real-slice truth pass** proving exact collector retention plus partial normalization support across the 22-slot FR slice. Full normalized-event materialization, full live breadth, and runtime completeness are still **not** proved.
- **Lane B stale/outage system behavior:** Not evidenced at **production-equivalent** / **scale** required by approval standard **#4**. Tranche **54** adds bounded explicit policy-row coverage for residual escalation classes `UNDEFINED_DIRECTION_MODEL` and `MISSING_REQUIRED_LANE`. Tranche **62** (Prompt **#283**) adds **one** **Protocol A controlled harness** observation with explicit UTC timestamps and operator-declared **`observed_behavior`** (**no** vendor HTTP) — **partial** incremental evidence only. Tranche **63** (Prompt **#288**) adds **one** **real** **`lane_b_real_observation_slice.py observe`** HTTPS attempt to Federal Register **`documents.json`** — **success-only** on that run (`normalized_signal_event`, HTTP **200**); **does not** evidence observe-path **`scout_failure`**, timeout, or empty-row on that attempt; live FR outage statistics and production-scale system closure are still **not** proved.
- **Lane B conflict / context-dominance:** **Partial** — Tranche **47** adds a **bounded** local fixture precedence trace (`tranche47_*`), adopted pre-existing Tranche **52** adds a **bounded** stale-context omission wrapper trace (`tranche52_*`) showing explicit stale-first omission before conflict handling in local cases, Tranche **56** adds a **bounded** minimal-path truth pass (`tranche56_*`) proving the current `lane_b_real_observation_slice.py conflict` subcommand itself does **not** read freshness-like fields and does **not** stale-omit valid context, Tranche **60** adds a **stored real-slice** conflict/fusion boundary pass (`tranche60_*`) proving the 22-slot collector artifacts do **not** include observe-output lane JSON files or top-level `source_lane` / `direction_hint` snapshot keys, so `cmd_conflict` mismatch vs local contra is **not** slice-derived without policy-filled `direction_hint`, and Tranche **61** (Prompt **#276**) locks **operator-facing replay policy** in `lane_b_phase2_conflict_replay_policy_decision.json` requiring explicit labeling of slice-derived vs policy_fill vs unknown for replay on that stored slice (still **not** gate closure). Full conflict/runtime closure is still **not** proved.
- **Lane A (post–T66):** **Slice-1 STOP** — T64–T65 complete; **`evidence_status` `partial`**; further Lane A only under **new Lane A charter** (`LANE_A_PHASE2_EVIDENCE_CHARTER_T64.md` §9). **Not** approval; **not** Phase **3**.
- **Lane C (post–T68):** Bounded **live** evidence charter on disk (`docs/LANE_C_PHASE2_EVIDENCE_CHARTER_T66.md`) + **T67** first live observe + **T68** (Prompt **#311**) **slice-1 STOP** (§11) — URL locked §2 (`https://api.frankfurter.app/latest?from=USD`); registry **`evidence_status` `partial`** (**`partiality` preserved, not closed**); further Lane C live evidence **only** under **new explicit Lane C charter**. **Historical** T41/T42 local fixtures on disk — **not** live integration. **Not** approval; **not** Phase **3**.
- **T73 (historical policy, superseded in-file by T74):** **`config/phase2_mvp_approval_scope_decision.json`** first locked **all-lanes-required** + full six-dimension closure (Prompt **#325**).
- **T74 (current policy in same file):** **`config/phase2_mvp_approval_scope_decision.json`** **amended** to **scoped MVP path** — **`subset-of-lanes-eligible`**; **Lane B** = **primary** strict anchor; **≥2** of **A/C/E** = **support** slice-1 minimum (**not** six-dimension closure on support lanes); flip **eligibility** does **not** require all four lanes fully mature; **explicit operator signoff** still required in a later approval-decision tranche. **Governance only** — **no** new evidence; **no** registry lane/dimension rewrites; **`mvp_lane_approval.json` unchanged**; **no** lane reopen. Next tranche must follow **amended** **`next_tranche_authorization_rule`** / **`anti_drift_rule`** (**no** Phase **3** before explicit approval-decision tranche; **does not** sneak all-lanes/full-closure back as the rule).
- **Lane E (post–T71):** Bounded **live** evidence charter on disk (`docs/LANE_E_PHASE2_EVIDENCE_CHARTER_T69.md`) — **T70** (Prompt **#317**) **one** live **`observe`** → **`scout_failure`** (HTTP **404**) on Crossref URL §2; **T71** (Prompt **#321**) **slice-1 STOP** §12 — **no** further Lane E **live** tranches unless **new explicit Lane E charter**; registry **`evidence_status` `partial`** (**`partiality` preserved, not closed**); dimensions unchanged from T70. **Historical** Tranches **37–39** THE FADE-local fixtures on disk — **not** this live HTTPS slice. **Not** approval; **not** Phase **3**. **No** default next active lane.
- **Lane B (post–T64):** Existing partial evidence remains on disk; **new Lane B evidence tranches are frozen by default** — reopen **only** under a **new governed Lane B charter** naming scope and bounds.
- **T75 (post–T74; charter repaired Prompt #328):** **`docs/LANE_B_PRIMARY_ELIGIBILITY_CHARTER_T75.md`** — **Lane B** **only** for the **next bounded governance** tranche; **one** objective **(B)** — **governance-acceptance pack** for **`freshness`**, **`normalization_viability`**, **`conflict_handling`**, **`context_dominance_risk`**; **`stale_outage_behavior` out of scope**; **no** approval flip in T75; **no** A/C/E reopen.
- **T76 (Prompt #329):** **`config/lane_b_t76_scoped_mvp_governance_acceptance_pack.json`** + **`docs/LANE_B_T76_SCOPED_MVP_GOVERNANCE_ACCEPTANCE_MEMO.md`** — **governance only**; **`subset_acceptance_established`** for the **four** named dimensions under explicit limits; **`stale_outage_behavior` not** accepted at T76 alone; **no** new evidence; **`mvp_lane_approval.json` unchanged**; **no** A/C/E reopen.
- **T78 (Prompt #334):** **`config/lane_b_t78_scoped_mvp_governance_acceptance_pack.json`** + **`docs/LANE_B_T78_SCOPED_MVP_GOVERNANCE_ACCEPTANCE_MEMO.md`** — **governance only**; **`reliability`** + **`stale_outage_behavior`**; **does not** revisit T76 four dimensions; **`subset_acceptance_established`**; **`primary_lane_eligibility_met_after_this_pack`:** **`true`** **with T76** per pack rationale; **no** new evidence in T78; **no** A/C/E reopen.
- **T80 (Prompt #336):** **`config/t80_scoped_mvp_approval_decision.json`** — **`scoped_mvp_approval_decision`:** **`YES`**; **`mvp_lane_approval.json`** **`approved: true`** with four named lanes; **`phase2_mvp_approval_scope_decision.json`** reconciled (**`as_of_t80_on_disk_assessment`**; **`as_of_t74_on_disk_assessment`** historical only). **Approval-decision only** — **no** new evidence; **no** execution code; **no** lane reopen. **Scoped MVP approval granted** — **not** Phase **3** readiness; **not** production maturity.
- **T82 (Prompt #342):** **`config/phase2_mvp_approval_scope_decision.json`** — **`post_t82_on_disk_governance_lock`**, **`phase3_entry_planning_only_definition`**, amended **`next_tranche_authorization_rule`** / **`anti_drift_rule`**. **Governance lock only** — **no** `mvp_lane_approval.json` change; **no** registry change; **no** lane reopen; **no** code; **no** evidence. **Splits** pre-T80 combined ban: **one** future **Phase 3 entry planning only** tranche is **explicitly allowed**; **Phase 3 implementation**, scanner/runtime/dashboard **coding**, **provider integration**, **lane reopen**, **evidence collection** remain **forbidden** as **next** moves without further governance.
- **T83 (Prompt #345):** **`docs/THE_FADE_PHASE3_ENTRY_PLAN_T83.md`** + **`docs/THE_FADE_PHASE3_IMPLEMENTATION_BOUNDARY_T83.md`**; **`post_t83_phase3_entry_planning_package`** in **`phase2_mvp_approval_scope_decision.json`**. **Planning only** — **no** implementation code; **no** lane reopen; **no** registry/`mvp_lane_approval.json` edit; **no** evidence. Defines Phase **3** **entry** boundary and **one** candidate first implementation slice (**static** scanner I/O contract only, when a **later** implementation tranche authorizes). **Executable** Phase **3** still requires **later explicit implementation governance**.
- **T84 (Prompt #346):** **`docs/THE_FADE_T84_FIRST_IMPLEMENTATION_SLICE_GOVERNANCE.md`** + **`docs/THE_FADE_T84_FIRST_IMPLEMENTATION_SLICE_ACCEPTANCE_CRITERIA.md`**; **`post_t84_first_implementation_slice_governance`** in **`phase2_mvp_approval_scope_decision.json`**. **Implementation governance only** — **no** code in **T84**; **no** lane reopen; **no** registry/`mvp_lane_approval.json` edit. **Converts** T83 candidate into **one** **governed** first slice: **only** **static** universe-scanner I/O contract artifacts in **one** **future** tranche; **forbids** executable scanner, jobs, network, dashboard, providers, production wiring, multi-slice bundling in that tranche. **Broader** Phase **3** **blocked** until **new** governance after that slice.
- **T85 (Prompt #350):** **`contracts/phase3_universe_scanner_io/`** (schemas, examples, `.pyi`, README); **`post_t85_static_universe_scanner_io_contract_slice`** in **`phase2_mvp_approval_scope_decision.json`**. **Static** contract slice **only** — **no** executable scanner, **no** network, **no** lane reopen, **no** registry/`mvp_lane_approval.json` edit. **Executable** Phase **3** **still blocked** until **new** governance.

---

## Not yet justified

- **Full strict `MVP_SOURCE_RELIABILITY_AUDIT.md` closure** on **every** dimension for **every** lane as **production-mature** — **not** claimed; registry **`dimension_evidence_status`** partialities below remain honest.
- **`approved: true` under the scoped T74 path** — **justified and recorded** in **T80** (`mvp_lane_approval.json` + signoff artifact); this is **distinct** from the bullet above.
- **Phase 3 executable implementation** (scanner loop / runtime / dashboard / production integration / provider wiring) — **not** started; **T85** delivers **only** **static** I/O **contracts**; **broader** Phase **3** requires **new** governance.
- **Merging** unrelated historical samples into one reliability statistic — **still not** justified (per existing audit discipline).

---

## Remaining gate blockers (strict audit accounting — post–T80)

**Note:** **Scoped MVP approval is on disk** (T80). The following is an honest list of **strict** audit / maturity gaps that **T80 does not erase**.

Per `MVP_SOURCE_RELIABILITY_AUDIT.md` approval standard — **all** must pass for a candidate lane **if** treating that lane as **production-closed** at full bar; **Lane B** is furthest along but **not** closed at that strict reading:

1. **Stale/outage behavior is explicit** (standard **#4**) — **Lane B:** still **partial** after T35 + T45 + T54; not gate-closed at **system** level.
2. **Normalization viability** — **Lane B:** **partial** (Tranche **34** + **Tranche 50** + **Tranche 58**). Exact collector retention plus partial normalization support are now evidenced on the stored real slice, but full normalized-event materialization, full live breadth, and full silent-drop guarantees are **not** established.
3. **Freshness discipline** — **Lane B:** **policy locked** but outcome **partial** (**10** unresolved rows).
4. **Reliability** — strong for **FR window slice**; **not** a license to ignore other dimensions or other lanes.
5. **No context-only domination** — Lane B / fusion still **partial** even after bounded T47/T52/T56 local traces, the T60 real-slice conflict/fusion boundary, and the T61 conflict-replay policy file (labeling only); T56 clarifies that stale-first omission is wrapper-only relative to the current minimal path; T60 clarifies that the stored 22-slot slice does not by itself supply `cmd_conflict` lane JSON or direction fields; T61 locks operator-facing replay labeling for policy_fill vs slice-derived vs unknown on that stored slice. Lane E likewise remains **not** fully proven at gate bar across permutations.
6. **Other MVP lanes (A, C, E)** — Lane A **slice-1 stopped**; **`partial`**, not MVP bar. Lane C **slice-1 stopped** (**T68**); **`partial`**, not MVP bar — **do not** mistake **`partial`** for closure. Lane E (**T71** slice-1 STOP + **T70** live record): **`evidence_status` `partial`** — **preserved, not closed**; **not** MVP bar; **no** further Lane E **live** work without **new Lane E charter**.

---

## Ranked rationale (why the locked order)

| Dimension / work | Gate value | Scope risk | Build effort | Decision value |
|------------------|------------|------------|--------------|----------------|
| **Lane B stale/outage & escalation honesty** | **High** (standard **#4**) | **Medium** if bounded to read-only + policy mapping | **Medium** | **High** — clears largest **undedicated** Lane B pillar |
| **Cross-lane gate rollup** | **High** (stops Lane B tunnel vision) | **Low** (docs + registry read) | **Low** | **High** — forces **HOLD / next lane / formal pause** |

---

## LOCKED remaining sequence (execute only under future governed prompts)

### Executed — **Tranche 35** (Prompt **#135**)

**Name:** Lane B **stale/outage & escalation alignment** audit (bounded).  

**Scope (as run):** Read-only: `escalation_policy.json`, collector exit semantics, JSONL/snapshot **failure** vs **success** paths as documented; narrow script + artifacts (same style as Tranche **34**). **No** new scheduled collection; **no** production runtime.  

**Outcome (on disk):** `audit_lane_b_stale_outage_escalation_alignment.py` + `tranche35_stale_outage_escalation_audit.json` / `.md` — honest **thin/partial** verdict for standard **#4** on the Lane B FR full-window slice; **not** gate closure.  

### Executed — **Tranche 36** (Prompt **#143**)

**Name:** Phase **2** **cross-lane gate dimension rollup**.  

**Scope (as run):** Single pass over `mvp_lane_evidence_registry.json` + `MVP_LANE_EVIDENCE_LOG.md` + audit/config truth — four-lane matrix with **done / partial / absent / not yet justified** states. **No** new tranche types inside the rollup; **no** collection.  

**Outcome (on disk):** `scripts/build_phase2_cross_lane_gate_rollup.py` + `outputs/phase2_cross_lane_gate_rollup/phase2_cross_lane_gate_rollup.{json,md}`. Lane B is deepest but still partial; lanes A/C/E remain mostly absent. **Not** approval; **not** Phase **3**.

### Stop / decision point — **after Tranche 36**

**Required:** Operator (or governed prompt) chooses **one**:  

- **A)** Authorize **targeted** Phase **2** evidence for a **named** lane (A, C, or E) or a **named** bounded Lane B follow-up **only if** T35 exposes a justified gap; or  
- **B)** **Pivot to one named non-B lane bootstrap path** (selected in Tranche 36A: `lane_e_research_swarm_context`), with **definition-only** next step before any execution; or  
- **C)** **Formal HOLD** on Phase **2** completion spend; or  
- **D)** **Approval file edit** only with matching evidence + explicit signoff fields — **out of scope** for tranche execution prompts.  

**No Phase 3** unless Phase **2** gate is **satisfied and documented** under existing rules.

### Decision lock — **Tranche 36A** (Prompt **#145**)

- **Selected path:** **PATH B** (pivot).
- **Named next Phase 2 bootstrap lane:** `lane_e_research_swarm_context`.
- **Why now:** cross-lane rollup shows Lane B is deepest but still partial, while A/C/E are absent at gate depth; highest decision value is reducing non-B blind-spot.
- **Decision-pass boundary:** this lock does **not** execute a tranche, does **not** change `mvp_lane_approval.json`, and does **not** unlock Phase **3**.
- **Next step (post-lock):** execute one **bounded** Lane E bootstrap audit under Phase 2 governance with THE FADE-local fixtures only.

### Executed — **Tranche 37** (Prompt **#152**)

**Name:** Lane E **context non-dominance** bounded audit.

**Scope (as run):** THE FADE-local fixture audit only; no network; no Research Swarm integration. Validate Lane E contract semantics from config (`CONTEXT_ONLY`, `enrich_only`, `omit_if_missing`) across three explicit cases: context missing, context supports primary, context conflicts with primary.

**Outcome (on disk):** `scripts/audit_lane_e_context_non_dominance.py` + `examples/lane_e_context_bootstrap/tranche37_cases.json` + `outputs/lane_e_context_bootstrap/tranche37_lane_e_non_dominance_audit.{json,md}`. All three bounded cases pass non-dominance checks; omission is explicit when context is missing; no silent override of primary truth observed. **Not** approval; **not** Phase **3**; **not** live Research Swarm integration.

### Executed — **Tranche 38** (Prompt **#157**)

**Name:** Lane E **freshness + omission trace** bounded audit.

**Scope (as run):** THE FADE-local fixture audit only; no network; no live Research Swarm integration. Apply a bounded freshness window and classify local Lane E context cases as fresh/stale/missing while preserving non-primary behavior and explicit omission traces.

**Outcome (on disk):** `scripts/audit_lane_e_freshness_omission_trace.py` + `examples/lane_e_context_bootstrap/tranche38_cases.json` + `outputs/lane_e_context_bootstrap/tranche38_lane_e_freshness_omission_audit.{json,md}`. Cases cover fresh, stale, missing, and window-edge semantics; stale/missing are explicitly omitted; no primary override observed. **Not** approval; **not** Phase **3**; **not** live Research Swarm integration.

### Executed — **Tranche 39** (Prompt **#162**)

**Name:** Lane E **normalization + omission-reason trace** bounded audit.

**Scope (as run):** THE FADE-local fixture audit only; no network; no live Research Swarm integration. Evaluate four explicit cases (`fresh-valid`, `stale`, `missing`, `invalid-shape`) for explicit normalization status and omission reasons while preserving Lane E context-only/non-primary behavior.

**Outcome (on disk):** `scripts/audit_lane_e_normalization_omission_reason_trace.py` + `examples/lane_e_context_bootstrap/tranche39_cases.json` + `outputs/lane_e_context_bootstrap/tranche39_lane_e_normalization_omission_reason_trace_audit.{json,md}`. All four cases passed bounded checks with explicit verdict fields: `normalization_status`, `omission_reason`, `omission_explicit`, `no_primary_override`, and trace explanations. **Not** approval; **not** Phase **3**; **not** live Research Swarm integration.

### Decision stop — **Tranche 39A** (Prompt **#165**, governance lock only)

- **Selected path:** **PATH B** (post-T39).
- **Operational meaning now:** Lane E bootstrap is formally **paused for now** after bounded value capture in T37/T38/T39; return to **broader Phase 2 governance** for any next spend decision.
- **Hard boundaries:** no T40 definition in this pass; no T40 execution in this pass; no `mvp_lane_approval.json` edit; no Phase 3 unlock.
- **Interpretation guardrail:** this is **not** a Lane E failure claim; it is a scope-control decision that bounded Lane E bootstrap value has been captured for this checkpoint.

### Executed — **Tranche 40** (Prompt **#171**)

**Name:** Governance / registry truth-closure (bounded Phase 2 alignment pass).

**Scope (as run):** Reconcile machine-readable governance state to already-executed Phase 2 truth from Tranches **31-39** and the **39A** stop-lock, with minimal config/doc edits. **No** new lane evidence collection, **no** network, **no** approval edit, and **no** Phase **3** work.

**Outcome (on disk):** `config/mvp_lane_evidence_registry.json` now reflects current partial/deferred lane status truth (Lane B deepest-but-partial; Lane E bounded bootstrap executed then paused). Control docs are aligned to record T40 as governance closure only. `mvp_lane_approval.json` remains unchanged (`approved: false`, `approved_mvp_lanes: []`). **Not** approval; **not** Phase **3**.

### Executed — **Tranche 41** (Prompt **#176**)

**Name:** Lane C **FOLLOW + stale-policy trace** bounded audit.

**Scope (as run):** THE FADE-local fixture audit only; no network; no live market-data integration. Validate `lane_c_market_context` semantics from config (`direction_model_default=FOLLOW`, `failure_policy=invalidate_if_stale_vs_policy`) across four explicit cases: fresh-valid, stale, missing, and invalid-shape market context.

**Outcome (on disk):** `scripts/audit_lane_c_follow_stale_policy_trace.py` + `examples/lane_c_market_context_bootstrap/tranche41_cases.json` + `outputs/lane_c_market_context_bootstrap/tranche41_lane_c_follow_stale_policy_trace_audit.{json,md}`. Fresh-valid context is accepted under FOLLOW; stale/missing/invalid-shape context is explicitly invalidated/omitted with explicit reasons; no hidden override observed. **Not** approval; **not** Phase **3**; **not** live market-data integration.

### Executed — **Tranche 42** (Prompt **#181**)

**Name:** Lane C **FOLLOW conflict-mismatch trace** bounded audit.

**Scope (as run):** THE FADE-local fixture audit only; no network; no live market-data integration. Trace explicit primary direction vs market `direction_hint` under FOLLOW: aligned fresh-valid acceptance; explicit bullish/bearish mismatch omits with `direction_conflict_with_primary`; stale policy applies before conflict resolution where relevant; missing/invalid-shape omit with explicit reasons.

**Outcome (on disk):** `scripts/audit_lane_c_follow_conflict_trace.py` + `examples/lane_c_market_context_bootstrap/tranche42_cases.json` + `outputs/lane_c_market_context_bootstrap/tranche42_lane_c_follow_conflict_trace_audit.{json,md}`. Bounded explicit trace fields per case; no silent FOLLOW of conflicting market over primary. **Not** approval; **not** Phase **3**; **not** live market-data integration.

### Decision stop — **Tranche 43** (Prompt **#185**, governance lock only)

- **Selected path:** **PATH B** (post-T42 Lane C).
- **Operational meaning now:** Lane C bounded bootstrap is formally **paused for now** after bounded value capture in T41/T42; return to **broader Phase 2 governance** for the next spend decision.
- **Hard boundaries:** no T43 execution in this pass; no new Lane C tranche definition in this pass; no `mvp_lane_approval.json` edit; no Phase 3 unlock.
- **Interpretation guardrail:** this is **not** a Lane C failure claim; it is a scope-control decision that bounded Lane C bootstrap value has been captured for this checkpoint.

### Executed — **Tranche 44** (Prompt **#187**, post-T43 governance truth-closure)

**Name:** Governance / registry truth-closure after dual lane pauses (bounded Phase 2 alignment pass).

**Scope (as executed):** Reconcile machine-readable governance state (`mvp_lane_evidence_registry.json` `_meta`/notes and lane notes) to post-T43 truth (T39A Lane E pause + T43 Lane C pause + last lane evidence through T42), with minimal config/doc alignment only. **No** new lane evidence collection, **no** network, **no** live integrations, **no** approval edit, and **no** Phase **3** work.

**Outcome (on disk):** Registry `_meta` and top-level `tranche` reflect Tranche **44**; Lane C and Lane E notes explicitly include T43/T39A pause locks and state that T44 is governance-only; control docs updated to record T44 executed. **`mvp_lane_approval.json` unchanged** (`approved: false`).

**Success criteria (met by this execution):**
- `mvp_lane_evidence_registry.json` reconciled to Tranche 43 decision-stop truth without over-claiming new evidence.
- Control docs consistent on lane posture (Lane E paused, Lane C paused), approval false, Phase 3 blocked.

**Non-success / overclaim guardrails:**
- Any implied approval grant, Phase 3 unlock, or live integration claim.
- Any new lane bootstrap execution framed as part of T44.
- Any architecture/runtime expansion beyond governance alignment.

### Defined next — **Tranche 45** (Prompt **#191**, broader Phase 2 decision — **definition only**)

**Name:** Lane B **failure-path / stale-outage explicit behavior trace** (bounded audit).

**Selected path:** **PATH B** — deepen **one** existing partial lane (**`lane_b_official_disclosure`**) with **one** bounded tranche; **not** a new lane bootstrap; **not** resuming paused Lane E / Lane C bootstraps without a separate governed unpause.

**Why this is next (post-T44):** `MVP_SOURCE_RELIABILITY_AUDIT.md` standard **#4** (stale/outage behavior explicit) remains a **high-value** remaining gate pillar for Lane B. Tranche **35** already showed the **full-window FR success slice** yields **thin** negative-path / escalation examples on disk. The highest honest incremental value is to **exercise explicit failure/stale/unavailable paths** using **THE FADE-local fixtures and/or controlled replay of stored snapshot shapes** only — **no** new network collection, **no** new scheduled collector runs, **no** live integration.

**Exact evidence question:** When Lane B observation is **failure**, **stale per adopted policy**, or **blocked for normalization**, does the path produce **explicit** downgrade / escalate / omit behavior aligned to `escalation_policy.json` (and lane contracts) **without** fabricating primary truth or silent drops?

**Scope (future execution):** Single bounded script + small fixture set + JSON/MD outputs under `future_modules/the_fade/`; update `mvp_lane_evidence_registry.json` + evidence log only on execution. **Not** approval; **not** Phase **3**; **not** production runtime proof.

**Non-success / overclaim guardrails:** Must not claim **gate closure** for standard **#4** at production scale; must not imply **live** Federal Register integration beyond what fixtures replay; must not flip **`mvp_lane_approval.json`**.

### Executed — **Tranche 45** (Prompt **#192**, Lane B failure-path / stale-outage trace)

**Name:** Lane B **failure-path / stale-outage explicit behavior trace** (bounded audit).

**Scope (as run):** THE FADE-local fixtures only (`examples/lane_b_failure_path_bootstrap/tranche45_cases.json`); **no** network; **no** live FR collection; **no** freshness-only tranche (parked line unchanged).

**Outcome (on disk):** `scripts/audit_lane_b_failure_path_stale_outage_trace.py` + `outputs/lane_b_failure_path_bootstrap/tranche45_lane_b_failure_path_stale_outage_trace_audit.{json,md}`. Four explicit cases: **SOURCE_UNAVAILABLE**, **stale** path via **`lane_registry.json`** `failure_policy` (no STALE row in `escalation_policy.json`), **NORMALIZATION_FAILURE**, **INVALID_PACKET_OUTPUT**. **Not** approval; **not** Phase **3**; **not** production outage statistics; **not** full standard **#4** closure.

### Executed — **Tranche 47** (Prompt **#200**, Lane B conflict / fusion precedence trace)

**Name:** Lane B **conflict-handling / fusion precedence** bounded fixture audit (primary vs context-only).

**Scope (as run):** THE FADE-local fixtures only (`examples/lane_b_conflict_fusion_bootstrap/tranche47_cases.json`); **no** network; **no** live FR collection; **no** Research Swarm integration; **no** market-data integration. Read-only use of `fusion_policy.json`; trace semantics aligned to `lane_b_real_observation_slice.py` `conflict` subcommand.

**Outcome (on disk):** `scripts/audit_lane_b_conflict_fusion_precedence_trace.py` + `outputs/lane_b_conflict_fusion_bootstrap/tranche47_lane_b_conflict_fusion_precedence_trace_audit.{json,md}`. Bounded cases: context **contra** vs primary (explicit non-override summary), **aligned** context, **missing** context (explicit CLI boundary), **invalid role**, **stale context** (documents minimal-slice gap: no age check in `conflict`), **tie** case marked **unsupported** under current unequal weights. **Not** approval; **not** Phase **3**; **not** full conflict-handling or fusion-runtime closure.

### Executed — **Tranche 50** (Prompt **#213**, Lane B normalization viability / silent-drop trace)

**Name:** Lane B **normalization viability / silent-drop** bounded fixture audit.

**Scope (as run):** THE FADE-local fixtures only (`examples/lane_b_normalization_bootstrap/tranche50_cases.json`); **no** network; **no** live FR collection; **no** new provider sampling; grounded to `normalized_signal_event.schema.json`, `scout_failure.schema.json`, `lane_registry.json`, and `escalation_policy.json`.

**Outcome (on disk):** `scripts/audit_lane_b_normalization_viability_silent_drop_trace.py` + `outputs/lane_b_normalization_bootstrap/tranche50_lane_b_normalization_viability_silent_drop_trace_audit.{json,md}`. Bounded cases cover normalized success, normalization-blocked explicit `scout_failure`, missing-required-field explicit omission, and invalid-candidate explicit `scout_failure`; **no** silent drop observed in the bounded cases. **Not** approval; **not** Phase **3**; **not** full live normalization breadth or runtime closure.

### Adopted — **Tranche 52** (Prompt **#221**, pre-existing Lane B stale-context conflict omission trace)

**Name:** Lane B **stale-context conflict omission** bounded fixture audit.

**Scope (as adopted):** Pre-existing THE FADE-local fixtures only (`examples/lane_b_stale_context_conflict_bootstrap/tranche52_cases.json`); **no** network; **no** live FR collection; **no** rerun in this pass. Treat the already-on-disk T52 script and audit outputs as bounded Phase **2** evidence.

**Outcome (on disk):** `scripts/audit_lane_b_stale_context_conflict_omission_trace.py` + `outputs/lane_b_stale_context_conflict_bootstrap/tranche52_lane_b_stale_context_conflict_omission_trace_audit.{json,md}`. Bounded cases show explicit stale-context omission before conflict evaluation, no stale-context override of Lane B primary truth in the stale cases, and fresh valid context remaining in the conflict branch. **Not** approval; **not** Phase **3**; **not** live FR evidence; **not** proof that the minimal `lane_b_real_observation_slice.py conflict` subcommand itself consumes freshness fields; **not** full conflict/runtime closure.

### Executed — **Tranche 54** (Prompt **#226**, Lane B stale/outage residual policy coverage trace)

**Name:** Lane B **stale/outage residual policy coverage** bounded fixture audit.

**Scope (as run):** THE FADE-local fixtures plus prior on-disk T35/T45 audit outputs only; **no** network; **no** live FR collection; **no** rerun of Tranche 21 collection. Target only the residual escalation-policy classes still not evidenced in the stored FR slice after T35 and not already covered by T45.

**Outcome (on disk):** `scripts/audit_lane_b_stale_outage_residual_policy_coverage_trace.py` + `examples/lane_b_stale_outage_residual_policy_bootstrap/tranche54_cases.json` + `outputs/lane_b_stale_outage_residual_policy_bootstrap/tranche54_lane_b_stale_outage_residual_policy_coverage_trace_audit.{json,md}`. Bounded cases explicitly cover `UNDEFINED_DIRECTION_MODEL` and `MISSING_REQUIRED_LANE`, reducing the exact residual standard **#4** policy-row coverage gap after T35/T45. **Not** approval; **not** Phase **3**; **not** live FR outage evidence; **not** production-scale stale/outage closure.

### Executed — **Tranche 56** (Prompt **#235**, Lane B minimal conflict freshness-consumption truth pass)

**Name:** Lane B **minimal conflict freshness-consumption truth** bounded audit.

**Scope (as run):** THE FADE-local code-path inspection plus bounded replay of the real `lane_b_real_observation_slice.py conflict` subcommand using local fixtures only; **no** network; **no** live FR collection; **no** rerun of Tranche 21 collection. Target only the exact truth question of whether the current minimal `conflict` path itself consumes freshness-related fields or performs stale-context omission.

**Outcome (on disk):** `scripts/audit_lane_b_minimal_conflict_freshness_consumption_truth.py` + `examples/lane_b_minimal_conflict_freshness_truth_bootstrap/tranche56_cases.json` + `outputs/lane_b_minimal_conflict_freshness_truth_bootstrap/tranche56_lane_b_minimal_conflict_freshness_consumption_truth_audit.{json,md}`. Static inspection plus bounded fresh-vs-stale replay pairs prove the current minimal `conflict` path reads `source_lane`, `semantic_role`/`role`, and `direction_hint`, but **not** freshness-like fields, and valid stale-labeled context still emits the same conflict packet content when directional inputs match. This narrows the exact T47/T52 truth gap by proving stale-first omission remains wrapper-only relative to the current minimal path. **Not** approval; **not** Phase **3**; **not** live FR conflict freshness evidence; **not** full conflict/runtime closure.

### Executed — **Tranche 58** (Prompt **#246**, Lane B real-slice normalization truth pass)

**Name:** Lane B **real-slice normalization truth** bounded audit.

**Scope (as run):** Stored **22-slot** Federal Register full-window artifacts only (`tranche21_fr_slot_runs.jsonl` + per-run snapshot JSONs) plus current schema/collector truth; **no** network; **no** new collection; **no** live integration; **no** approval edit.

**Outcome (on disk):** `scripts/audit_lane_b_real_slice_normalization_truth.py` + `outputs/lane_b_real_slice_normalization_truth_bootstrap/tranche58_lane_b_real_slice_normalization_truth_audit.{json,md}`. The audit proves the stored real slice preserves exact collector retention plus partial normalization support (`task_id`, timing, evidence URL/path, `response_sha256`, and `results[0]` identity fields) and therefore reduces the exact normalization-viability truth gap on the real stored slice. It also proves the boundary: the stored slice never wrote full `normalized_signal_event` artifacts, raw-body preservation is truncated to preview text, and required fields such as `ticker`, `asset_type`, `direction_hint`, `trust_tier`, and `parser_confidence` are absent or only partially evidenced. Silent-drop risk is reduced at the collector-retention layer but still **not** ruled out for full normalized-event materialization from the stored slice alone. **Not** approval; **not** Phase **3**; **not** full normalization closure.

### Executed — **Tranche 60** (Prompt **#255**, Lane B real-slice conflict / fusion truth pass)

**Name:** Lane B **real-slice conflict / fusion truth** bounded audit.

**Scope (as run):** Stored **22-slot** Federal Register full-window artifacts only (`tranche21_fr_slot_runs.jsonl` + per-run snapshot JSONs) plus read-only `fusion_policy.json` and THE FADE-local `inputs/lane_b_real_evidence/context_only_contra.example.json` (**no** new fixture; **no** network; **no** new collection; **no** approval edit).

**Outcome (on disk):** `scripts/audit_lane_b_real_slice_conflict_fusion_truth.py` + `outputs/lane_b_real_slice_conflict_fusion_truth_bootstrap/tranche60_lane_b_real_slice_conflict_fusion_truth_audit.{json,md}`. The audit inventories conflict-adjacent fields present in the collector slice, proves observe-output lane JSON files are **not** part of the stored population, proves snapshot top-level keys do **not** include `source_lane` or `direction_hint`, and documents bounded `cmd_conflict` replay showing **`mismatch=False`** when `direction_hint` is omitted on a synthesized lane artifact vs bearish local contra, versus **`mismatch=True`** when `direction_hint` is observe-default **`neutral`** (policy fill, not slice-derived). Explicit primary/weight wording remains supportable from read-only fusion policy under replay. **Not** approval; **not** Phase **3**; **not** full conflict/runtime closure; **not** live Lane E integration.

### Executed — **Tranche 61** (Prompt **#276**, Lane B conflict-replay `direction_hint` policy decision)

**Name:** Lane B **Phase 2 conflict-replay policy** for **`direction_hint`** when replaying **`lane_b_real_observation_slice.py conflict`** on **stored 22-slot** Federal Register collector artifacts.

**Scope (as run):** **Governance / operator policy only** — new machine-readable file `config/lane_b_phase2_conflict_replay_policy_decision.json` plus aligned updates to `MVP_LANE_EVIDENCE_LOG.md`, `mvp_lane_evidence_registry.json` (Lane B notes + `_meta`), `THE_FADE_CONTEXT_ANCHOR.md`, `THE_FADE_PROCESS_CHECKLIST.md`, `THE_FADE_HANDOFF_BUNDLE_LATEST.md`, `JARVIS_THE_FADE_MASTER_BUILD_CHECKLIST.md`, and this plan. **No** new live Federal Register collection; **no** Tranche 21 scheduler rerun; **no** script edits; **no** new output artifacts under `outputs/`; **no** `mvp_lane_approval.json` edit.

**Outcome (on disk):** `lane_b_phase2_conflict_replay_policy_decision.json` **locks** explicit classification: **slice-derived bytes** vs **policy_fill** vs **unknown/omit**; restates T60 truth that the stored slice **does not** prove **`direction_hint`** and **does not** include observe-output lane JSON or top-level **`source_lane`/`direction_hint`** on snapshots; **`direction_hint` may be omitted** when not evidenced; policy-filled values (including observe defaults) **must** be labeled **policy_fill**, **not** FR-derived truth; mismatch conclusions that depend on policy fill **must** be labeled accordingly. **Does not** close **`conflict_handling`** or **`context_dominance_risk`**; **not** approval; **not** Phase **3**.

### Executed — **Tranche 62** (Prompt **#283**, Lane B Protocol A controlled stale/unavailable timestamped pass)

**Name:** Lane B **`LANE_B_STALE_UNAVAILABLE_CONTROLLED_REPLAY_V1`** — **one** bounded **Protocol A** harness execution with explicit UTC timestamps.

**Scope (as run):** `lane_b_controlled_evidence_harness.py` **Protocol A** only; operator-authored inputs `examples/lane_b_controlled_evidence_harness_inputs/t62_protocol_a_lane_b_evidence.json` + `t62_protocol_a_scenario.json`. **No** network; **no** `lane_b_real_observation_slice.py` observe/conflict; **no** Tranche 21 collector; **no** `mvp_lane_approval.json` edit.

**Outcome (on disk):** Harness stdout captured to `outputs/lane_b_real_observation/t62_protocol_a_lane_b_controlled_observation.json` (directory `*.json` gitignored — full JSON also embedded in `MVP_LANE_EVIDENCE_LOG.md`). Observation includes **`observed_at`**, **`evidence_item_timestamp`**, **`stale_window_definition`**, **`unavailable_condition_definition`**, **`observed_behavior`** (`escalate` for this pass), and harness **`input_fingerprint`**. **Does not** prove live outage, production scout runtime, or standard **#4** closure at scale; **not** approval; **not** Phase **3**.

### Executed — **Tranche 63** (Prompt **#288**, Lane B real observe-path pass)

**Name:** Lane B **real `observe` tool path** — **one** bounded HTTPS execution via **`lane_b_real_observation_slice.py observe`** to Federal Register API.

**Scope (as run):** **Network** — read-only GET pattern to `https://www.federalregister.gov/api/v1/documents.json?per_page=1&order=newest`; **`--task-id`** `t63_real_observe_20260404T130000Z`; **`--timeout`** `45`; output under `outputs/lane_b_real_observation/`. **No** controlled harness substitution; **no** `mvp_lane_approval.json` edit.

**Outcome (on disk):** `t63_real_observe_20260404T130000Z_normalized_signal_event.json` (gitignored — summary embedded in `MVP_LANE_EVIDENCE_LOG.md`). **Observed outcome class:** **success-only** — HTTP **200**, `normalized_signal_event` materialized, **`lag_class`:** `fresh`, response **`sha256`** in `notes`. **Does not** prove **`scout_failure`**, client timeout, empty/no-row, or other non-success observe paths on this run; **does not** close standard **#4**; **not** approval; **not** Phase **3**.

### Executed — **Tranche 64** (implementation rollout Prompt **#294**, Lane A bounded evidence charter + doc lock; charter decision **#293**)

**Name:** Lane A **`lane_a_public_signal`** — Phase **2** **bounded evidence charter** and **control-doc / registry reconciliation**; **Lane B default freeze** declaration.

**Scope (as run):** New file `docs/LANE_A_PHASE2_EVIDENCE_CHARTER_T64.md` plus updates to `mvp_lane_evidence_registry.json`, `MVP_LANE_EVIDENCE_LOG.md`, `THE_FADE_CONTEXT_ANCHOR.md`, `THE_FADE_PROCESS_CHECKLIST.md`, `THE_FADE_HANDOFF_BUNDLE_LATEST.md`, this plan, and `JARVIS_THE_FADE_MASTER_BUILD_CHECKLIST.md`. **No** network observation; **no** new Lane A `outputs/`; **no** execution code; **no** `mvp_lane_approval.json` edit; **no** Lane C / Lane E unpause.

**Outcome (on disk):** Charter locks **one** read-only HTTPS public source class; URL locked in **T65** (see charter §2 and `MVP_LANE_EVIDENCE_LOG.md`). **Lane B:** new tranches **paused by default** until a **new Lane B charter** reopens scope. **Not** approval; **not** Phase **3**.

### Executed — **Tranche 65** (Prompt **#298**, Lane A first bounded live observe-or-honest-failure pass)

**Name:** Lane A **`lane_a_public_signal`** — **one** bounded **HTTPS** **`observe`** execution (reuse `lane_b_real_observation_slice.py` with **`--source-lane lane_a_public_signal`**).

**Scope (as run):** Read-only GET to **`https://api.coinbase.com/v2/exchange-rates?currency=BTC`**; **`--task-id`** `t65_lane_a_first_observe`; **`--timeout`** `30`; output under `outputs/lane_a_public_signal/` (`*.json` gitignored). Minimal script change: optional **`--source-lane`** on **`observe`** so emitted JSON records **`lane_a_public_signal`** (default preserves Lane B). **No** `mvp_lane_approval.json` edit; **no** new Lane B tranches.

**Outcome (on disk):** `t65_lane_a_first_observe_normalized_signal_event.json` (local; gitignored — full command/window/outcome in `MVP_LANE_EVIDENCE_LOG.md`). **Observed outcome class:** **success-only** — HTTP **200**, `normalized_signal_event`. **Does not** prove **`scout_failure`**, timeout, or empty-body on this run; **does not** close Lane A freshness, stale/outage, conflict, or context-dominance; **not** approval; **not** Phase **3**.

### Executed — **Tranche 66** (Prompt **#302**, Lane A slice-1 stop + Lane C bounded evidence charter)

**Name:** **Governance / doc lock** — Lane A **slice-1 STOP** + first **`lane_c_market_context`** Phase **2** **bounded evidence charter**.

**Scope (as run):** New file `docs/LANE_C_PHASE2_EVIDENCE_CHARTER_T66.md`; Lane A charter §9 stop in `LANE_A_PHASE2_EVIDENCE_CHARTER_T64.md`; updates to `mvp_lane_evidence_registry.json`, `MVP_LANE_EVIDENCE_LOG.md`, `THE_FADE_CONTEXT_ANCHOR.md`, `THE_FADE_PROCESS_CHECKLIST.md`, `THE_FADE_HANDOFF_BUNDLE_LATEST.md`, this plan, and `JARVIS_THE_FADE_MASTER_BUILD_CHECKLIST.md`. **No** network observation; **no** Lane C execution code; **no** `mvp_lane_approval.json` edit; **no** Lane B reopen; **no** Lane E unpause.

**Outcome (on disk):** Lane C charter locks **one** read-only HTTPS **market-context** source class; URL **`TBD`** until named before **T67**; **T67** = **one** bounded observe-or-honest-failure pass (**reliability** + **normalization_viability** first). Lane A further work **only** under **new Lane A charter**. Lane B freeze + Lane E pause **unchanged**. **Not** approval; **not** Phase **3**.

### Executed — **Tranche 70** (Prompt **#317**, Lane E first bounded live observe-or-honest-failure pass)

**Name:** Lane E **`lane_e_research_swarm_context`** — **one** bounded **HTTPS** **`observe`** execution (reuse `lane_b_real_observation_slice.py` with **`--source-lane lane_e_research_swarm_context`**).

**Scope (as run):** Read-only GET to **`https://api.crossref.org/works/10.1038/d41586-019-02658-z`** (Crossref public Works API; **no** auth in repo); **`--task-id`** `t70_lane_e_first_observe`; **`--timeout`** `30`; **`--source-name`** `crossref_public_works_api`; output under `outputs/lane_e_research_swarm_context/` (`*.json` gitignored). Charter §2 URL lock in `LANE_E_PHASE2_EVIDENCE_CHARTER_T69.md`. **No** `mvp_lane_approval.json` edit; **no** Lane A/B/C reopen.

**Outcome (on disk):** `t70_lane_e_first_observe_scout_failure.json` (local; gitignored — full command/window/outcome in `MVP_LANE_EVIDENCE_LOG.md`). **Observed outcome class:** **`scout_failure`** — HTTP **404**, `error_type` **`SOURCE_UNAVAILABLE`**. Registry Lane E **`evidence_status` → `partial`**; **`reliability`** + **`normalization_viability`** → **`partial`**. **Does not** prove HTTP **200** / `normalized_signal_event` for this URL on this run; **does not** close remaining Lane E dimensions; **not** approval; **not** Phase **3**.

### Executed — **Tranche 71** (Prompt **#321**, Lane E slice-1 STOP governance lock)

**Name:** Lane E **`lane_e_research_swarm_context`** — **governance / doc lock** — **slice-1 STOP** for **live** HTTPS evidence tranches.

**Scope (as run):** Add **`LANE_E_PHASE2_EVIDENCE_CHARTER_T69.md`** §12; updates to `mvp_lane_evidence_registry.json`, `MVP_LANE_EVIDENCE_LOG.md`, `THE_FADE_CONTEXT_ANCHOR.md`, `THE_FADE_PROCESS_CHECKLIST.md`, `THE_FADE_HANDOFF_BUNDLE_LATEST.md`, this plan, and `JARVIS_THE_FADE_MASTER_BUILD_CHECKLIST.md`. **No** network observation; **no** execution code; **no** `mvp_lane_approval.json` edit; **no** Lane A/B/C reopen; **no** new lane started.

**Outcome (on disk):** **Lane E slice-1 STOP** — further Lane E **live** evidence **only** under **new explicit Lane E charter**. Registry Lane E **`evidence_status` remains `partial`**; dimension states **unchanged** from T70. **`partiality` preserved, not closed** — **not** MVP bar; **not** approval; **not** Phase **3**. **No** default next active MVP lane — **operator-governed** next Phase **2** decision required.

### Executed — **Tranche 73** (Prompt **#325**, MVP approval-scope decision lock)

**Name:** Phase **2** **MVP approval-scope governance lock** — machine-readable decision file only.

**Scope (as run):** New file `future_modules/the_fade/config/phase2_mvp_approval_scope_decision.json`; updates to `mvp_lane_evidence_registry.json` (**`_meta` / top-level `tranche` / `notes` only** — **no** lane `evidence_status` or `dimension_evidence_status` rewrites), `MVP_LANE_EVIDENCE_LOG.md`, `THE_FADE_CONTEXT_ANCHOR.md`, `THE_FADE_PROCESS_CHECKLIST.md`, `THE_FADE_HANDOFF_BUNDLE_LATEST.md`, this plan, and `JARVIS_THE_FADE_MASTER_BUILD_CHECKLIST.md`. **No** network observation; **no** execution code; **no** `mvp_lane_approval.json` **`approved` / `approved_mvp_lanes`** edits; **no** lane reopen.

**Outcome (on disk):** First approval-scope lock (**all-lanes-required** + full closure) — **superseded in-file by T74** (see below). **Not** approval; **not** Phase **3** unlock.

### Executed — **Tranche 74** (Prompt **#326**, amend MVP approval scope to scoped MVP path)

**Name:** **Amend** `phase2_mvp_approval_scope_decision.json` — **subset-of-lanes-eligible** scoped MVP **approval-eligibility** rule.

**Scope (as run):** **Edit only** `future_modules/the_fade/config/phase2_mvp_approval_scope_decision.json` (replace T73 policy shape); updates to `mvp_lane_evidence_registry.json` (**`_meta` / top-level `tranche` / `notes` only**), `MVP_LANE_EVIDENCE_LOG.md`, `THE_FADE_CONTEXT_ANCHOR.md`, `THE_FADE_PROCESS_CHECKLIST.md`, `THE_FADE_HANDOFF_BUNDLE_LATEST.md`, this plan, and `JARVIS_THE_FADE_MASTER_BUILD_CHECKLIST.md`. **No** network observation; **no** execution code; **no** `mvp_lane_approval.json` **`approved` / `approved_mvp_lanes`** edits; **no** lane reopen.

**Outcome (on disk):** **Single-reading** scoped path: **primary_lane_rule** for **`lane_b_official_disclosure`** (stricter; **not** met as of T74 — registry all **`partial`**); **support_lane_rule** for **≥2** of **A/C/E** (bounded live slice + **`partial`** + slice stop — **does not** require six-dimension closure); **`dimension_policy.mode`** = **`primary_lane_strict_plus_support_lane_slice1_minimum`**; **`next_tranche_authorization_rule`** tightened to **Lane B charter** **or** **hold** **or** **approval-decision** when preconditions met; **`anti_drift_rule`** preserves **no Phase 3** before explicit approval-decision tranche **without** reintroducing all-lanes/full-closure. **Not** approval; **not** Phase **3** unlock.

### Executed — **Tranche 75** (Prompt **#327**, Lane B primary-eligibility charter; **repaired** Prompt **#328**)

**Name:** **`LANE_B_PRIMARY_ELIGIBILITY_CHARTER_T75.md`** — **one** bounded **Lane B** objective tied to **`primary_lane_rule`**.

**Scope (as run):** `future_modules/the_fade/docs/LANE_B_PRIMARY_ELIGIBILITY_CHARTER_T75.md` (**repaired**); updates to `mvp_lane_evidence_registry.json` (**`notes` only**), `MVP_LANE_EVIDENCE_LOG.md`, `THE_FADE_CONTEXT_ANCHOR.md`, `THE_FADE_PROCESS_CHECKLIST.md`, `THE_FADE_HANDOFF_BUNDLE_LATEST.md`, this plan, and `JARVIS_THE_FADE_MASTER_BUILD_CHECKLIST.md`. **No** network observation; **no** execution code; **no** `mvp_lane_approval.json` **`approved` / `approved_mvp_lanes`** edits; **no** Lane A/C/E reopen.

**Outcome (on disk):** **Objective class (B):** **one** bounded **governance-acceptance pack** for **`freshness`**, **`normalization_viability`**, **`conflict_handling`**, **`context_dominance_risk`**; **`stale_outage_behavior` explicitly out of scope** (prior stored-slice stale/outage audit objective **removed**). **Lane B** **only** for next bounded **governance** class. **Not** approval; **not** Phase **3** unlock; **no** support-lane live work. **Delivered artifact filenames:** see **Tranche 76** (Prompt **#329**) — on-disk pack uses **`lane_b_t76_*`** paths.

### Executed — **Tranche 76** (Prompt **#329**, Lane B scoped MVP governance acceptance pack)

**Name:** **`THE_FADE_PHASE2_T76_LANE_B_SCOPED_MVP_GOVERNANCE_ACCEPTANCE_PACK`** — governance-only acceptance record for the **four** charter dimensions.

**Scope (as run):** New files `future_modules/the_fade/config/lane_b_t76_scoped_mvp_governance_acceptance_pack.json` + `future_modules/the_fade/docs/LANE_B_T76_SCOPED_MVP_GOVERNANCE_ACCEPTANCE_MEMO.md`; updates to `mvp_lane_evidence_registry.json` (**`_meta` / top-level `tranche` / `notes` + Lane B `notes` append** — **no** `dimension_evidence_status` rewrites), `MVP_LANE_EVIDENCE_LOG.md`, `THE_FADE_CONTEXT_ANCHOR.md`, `THE_FADE_PROCESS_CHECKLIST.md`, `THE_FADE_HANDOFF_BUNDLE_LATEST.md`, this plan, and `JARVIS_THE_FADE_MASTER_BUILD_CHECKLIST.md`. **No** network observation; **no** execution code; **no** `mvp_lane_approval.json` **`approved` / `approved_mvp_lanes`** edits; **no** Lane A/C/E reopen.

**Outcome (on disk):** **`overall_outcome`:** **`subset_acceptance_established`** for **`freshness`**, **`normalization_viability`**, **`conflict_handling`**, **`context_dominance_risk`** under explicit residual limits; **`stale_outage_behavior` not** accepted at T76 alone; **`primary_lane_eligibility_met_after_this_pack`:** **`false`** after T76 only. **Not** approval; **not** Phase **3** unlock.

### Executed — **Tranche 78** (Prompt **#334**, Lane B reliability + stale_outage scoped MVP governance acceptance pack)

**Name:** **`THE_FADE_PHASE2_T78_LANE_B_RELIABILITY_AND_STALE_OUTAGE_SCOPED_MVP_GOVERNANCE_ACCEPTANCE_PACK`** — governance-only acceptance for **`reliability`** and **`stale_outage_behavior`**; **does not** revisit T76 dimensions.

**Scope (as run):** New files `future_modules/the_fade/config/lane_b_t78_scoped_mvp_governance_acceptance_pack.json` + `future_modules/the_fade/docs/LANE_B_T78_SCOPED_MVP_GOVERNANCE_ACCEPTANCE_MEMO.md`; updates to `mvp_lane_evidence_registry.json` (**`_meta` / top-level `tranche` / `notes` + Lane B `notes` append** — **no** `dimension_evidence_status` rewrites), `MVP_LANE_EVIDENCE_LOG.md`, `THE_FADE_CONTEXT_ANCHOR.md`, `THE_FADE_PROCESS_CHECKLIST.md`, `THE_FADE_HANDOFF_BUNDLE_LATEST.md`, this plan, and `JARVIS_THE_FADE_MASTER_BUILD_CHECKLIST.md`. **No** network observation; **no** execution code; **no** `mvp_lane_approval.json` **`approved` / `approved_mvp_lanes`** edits; **no** Lane A/C/E reopen.

**Outcome (on disk):** **`overall_outcome`:** **`subset_acceptance_established`** for **`reliability`** and **`stale_outage_behavior`** under explicit limits; **`primary_lane_eligibility_met_after_this_pack`:** **`true`** when read **with T76** per **`primary_lane_eligibility_rationale`**; **`dimension_evidence_status` may remain `partial`**. **Not** approval; **not** Phase **3** unlock; full **`eligibility_rule_single_reading`** still requires **support_lane_rule** + **approval-decision** tranche.

---

## Do NOT work on yet (unless a new governed prompt explicitly rescopes)

- **Phase 3** scanner / runtime / dashboard.
- **Freshness-only** further tranches (already **parked** per Prompt **#132**).
- **Broker / live execution** / exchange integration.
- **Architecture expansion** (e.g. persist full FR JSON body) **without** a governed prompt that names storage + privacy/retention.
- **Research swarm** or **stock module** scope outside `future_modules/the_fade/`.
- **`mvp_lane_approval.json`** edits without operator evidence + signoff.
- **Ad-hoc** future tranches not listed above — **freeze** unless a new governed prompt explicitly adds them.
- **New Lane B evidence tranches** — **frozen by default** post–T64; reopen only via **new governed Lane B charter**.

---

## File relationships

- Process anchor: `THE_FADE_PROCESS_CHECKLIST.md` (points here).  
- One-screen: `THE_FADE_CONTEXT_ANCHOR.md` (summary bullet).  
- Handoff: `THE_FADE_HANDOFF_BUNDLE_LATEST.md` (path to this file).
