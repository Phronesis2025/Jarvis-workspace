# JARVIS_THE_FADE_MASTER_BUILD_CHECKLIST.md

**Document Type:** Master Build Checklist  
**Status:** Proposed Canonical Control Checklist (live progress below)  
**Version:** 2.00  
**Last Updated:** 2026-04-08T22:28:11+00:00
**Owner:** Jason  
**Project Context:** Jarvis future worker / stock intelligence side quest

**Live use:** Re-read **Live Progress Snapshot** and **Live phase-status table** on major checkpoints; they override stale assumptions elsewhere in this file until that section is revised.

---

## Live Progress Snapshot (authoritative)

Workspace branch: `the-fade-phase1-tranche1-foundation`.

The **eight THE FADE design canon** Markdown files (`JARVIS_THE_FADE_*.md`) **must remain** in `future_modules/stock_module/` -- foundational module docs; **do not move or delete** (index: `future_modules/the_fade/docs/CANON_INDEX.md`).

| Item | Current truth |
|------|----------------|
| MVP gate | **Phase 2** -- MVP lane approval and source reliability |
| `mvp_lane_approval.json` | **`approved`: true**; **`approved_mvp_lanes`:** **`lane_b_official_disclosure`**, **`lane_a_public_signal`**, **`lane_c_market_context`**, **`lane_e_research_swarm_context`** (verify order on disk). Signoff: **`t80_scoped_mvp_approval_decision.json`** (**#336**) |
| Active lane focus | **None by default** for **new** live evidence — **post–T80** (**#336**): scoped MVP approval **on disk**; **Lanes A/C/E** **stopped**; **Lane B** default freeze for **new** evidence tranches **unchanged**. **Not** Phase **3**; **not** production maturity |
| Phase 3 (Universe Scanner) | **Not started** (executable scanner/runtime) |
| Phase 3 unlock | **T85** static I/O contracts + **T87** contract-tree validator + **T89** Federal Register ingress + **T91** **`validate_ingress_request_packets.py`** + **T94** **`validate_universe_scanner_result_packets.py`** + **T96** **`build_universe_scanner_result_from_single_request.py`** + **T98** **`runner/local_happy_path/run_local_end_to_end_happy_path.py`** + **T100** **`operator/local_run/run_clean_local_happy_path.py`** + **T102** **`review/local_run/build_operator_review_from_run_folder.py`** + **T104** **`review/local_run/build_source_snapshot_from_run_folder.py`** + **T106** **`review/local_run/build_source_backed_operator_review_from_run_folder.py`** + **T108** **`review/local_run/build_operator_review_gate_signal_from_run_folder.py`** on disk (with post-#387 clean-next-run repair, per-run `operator_review.md`, `source_snapshot.json`, `source_backed_operator_review.md`, and `operator_review_gate.json` when scripts run); **T95** bridge governance, **T97** runner governance, **T99** operator-surface governance, **T101** review-surface governance, **T103** source-snapshot preservation governance, **T105** source-backed operator review governance, **T107** operator review gate signal governance, **T109** local operator review queue governance + **T110** **`review/local_run/build_operator_review_queue.py`** + **`outputs/local_happy_path_runs/operator_review_queue.json`** on disk; **T111** first operator-meaningful filtering signal governance on disk (**`build_operator_attention_signal_from_run_folder.py`** **not** built until a later tranche); **T93 Model B** cap for result root `*.json` unchanged in meaning; AI/scanner/real scan/result **production** path/runtime/dashboard/providers still **blocked** without new governance |
| Lane B vs gate sufficiency | **Scoped MVP approval granted** (**T80**) under **T74+T76+T78+T80** — **not** full strict-dimensional production closure; **Federal Register** full **Tranche 21** window on disk: **22** counted / **22** successes / **0** failures (**`t30_valid_002`** smoke **excluded**); **0.8** threshold **numeric** comparison **eligible for that slice only** (count floor met); **Phase 3** **not** started |
| Reliability vs `required_reliability_threshold` (0.8) | **Full-window slice:** **22** counted / **22** successes / **0** failures on disk → honest **`reliability = successes/counted`** vs **0.8** **may be stated for that slice** (**22/22**); **does not** prove **strict whole-gate production closure**. **Historical:** Tranche **16** mixed URLs, Tranche **24** pilot (**8** counted), micro-samples — **do not** merge into one statistic. **Other MVP dimensions** remain **partial** in registry |
| Lane B MVP disclosure **provider** | **Not locked** -- `mvp_lane_approval.json` **`TBD_OFFICIAL_DISCLOSURE_PROVIDER`**. Tranche **19** clarified mixed URLs (Federal Register vs SEC vs issuer IR) are **not** one provider path. |
| Lane B post-pilot decision (Tranche **26**) + full window (Tranche **30**) | **Parked** -- promising-but-unapproved (`approved:false`). **Full Tranche 21** FR window **executed on disk** + **Prompt #102** doc reconciliation complete. **Operator full-dimension gate review** completed (Prompt **#113** lock). **Tranche 31** + **Tranche 32** freshness evidence **executed** (Prompts **#121**, **#129**). Update **`mvp_lane_approval.json`** only on future signoff — **not** Phase 3 |
| Tranche 30 gate-decision alignment (Prompt **#103**) | **Doc-alignment only** -- interjection ideas triaged conservatively: **current-review-now** = critic/adversarial + audit-before-trust + risk-first scrutiny; **future guardrails only** = auth/permissions, isolated sub-account, MCP-first infra filter/anti-affiliate, sim-first bridge, sizing/drawdown; **parking lot only** = critic-agent build, MCP tooling build, exchange/live execution, execution-adjacent implementation |
| Tranche 30 final signoff lock (Prompt **#113**) | **Final signoff review completed** -- FR slice remains **22/22/0** (**`t30_valid_002`** excluded), lane B remains **promising-but-unapproved**, whole-gate closure remains **not justified**, `mvp_lane_approval.json` remains **false**, and Phase 3 remains **blocked** |
| Tranche 31 freshness evidence (Prompt **#121**) | **EXECUTED:** **22** full-window lines (`t30_valid_002` excluded) -- **12** **fresh**, **0** **stale**, **10** **cannot classify honestly** (see `MVP_LANE_EVIDENCE_LOG.md`). **Does not** satisfy stale/outage **system** behavior, normalization breadth, conflict permutations, context-dominance proof, production runtime, or approval |
| Tranche 32 ambiguity resolution (Prompt **#129**) | **EXECUTED:** **10**-row cohort -- bounded document API for **`2026-06133`**; **all 10** **still cannot classify honestly** under strict T31 rule; explicit limitation in `MVP_LANE_EVIDENCE_LOG.md`; **not** approval; **not** Phase 3 |
| Tranche 33 freshness policy comparator (Prompt **#131**) | **TOOL ON DISK:** `compare_tranche31_freshness_policies.py` + outputs under `outputs/lane_b_real_observation/tranche33_freshness_policy_comparison.*` — explicit **policy** comparison on stored evidence (**no** network); **not** approval; **not** Phase 3 |
| Tranche 33 freshness policy decision (Prompt **#132**) | **DECIDED:** **Adopt** **`strict_midnight_utc`** as **operator-facing** Phase **2** interpretation (`config/lane_b_phase2_freshness_policy_decision.json`); **not** adopt **`publication_day_fresh`** / **`publication_end_of_day_utc`** as primary; **park** freshness-only tranches — **not** approval; **not** Phase 3 |
| Tranche 34 normalization breadth audit (Prompt **#133**) | **EXECUTED:** `audit_lane_b_normalization_breadth.py` + `tranche34_normalization_breadth_audit.*` — JSONL/snapshot **solid**; preview **truncated** (full parse **0**/**22**); regex **`document_number`** **22**/**22**; **breadth partial** — **not** approval; **not** Phase 3 |
| Phase 2 remaining gate plan (Prompt **#134** / Tranche **34A**) | **LOCKED:** `future_modules/the_fade/docs/THE_FADE_PHASE2_REMAINING_GATE_PLAN.md` — **through T86 second-slice governance on disk**; Phase **2** governance context active; **scoped MVP approval** **T80**; **T85** static contracts + **T86** offline-validation boundary; **not** Phase 3 **executable** scanner |
| Tranche 35 stale/outage + escalation alignment audit | **EXECUTED:** `audit_lane_b_stale_outage_escalation_alignment.py` + `tranche35_stale_outage_escalation_audit.json` + `tranche35_stale_outage_escalation_audit.md` — FR full-window slice has only successes (no escalation negative examples); outage policy coverage remains partial; **not** approval; **not** Phase 3 |
| Tranche 36 cross-lane gate dimension rollup | **EXECUTED:** `build_phase2_cross_lane_gate_rollup.py` + `phase2_cross_lane_gate_rollup.{json,md}` — A/B/C/E matrix shows Lane B deepest but still partial, A/C/E mostly absent; **not** approval; **not** Phase 3 |
| Tranche 36A operator decision stop lock | **LOCKED:** **PATH B** selected — next Phase 2 bootstrap lane is `lane_e_research_swarm_context`; decision pass only (**no** tranche execution), `mvp_lane_approval.json` unchanged, **Phase 3 blocked** |
| Tranche 37 Lane E context non-dominance audit | **EXECUTED:** `audit_lane_e_context_non_dominance.py` + `examples/lane_e_context_bootstrap/tranche37_cases.json` + `outputs/lane_e_context_bootstrap/tranche37_lane_e_non_dominance_audit.{json,md}` — three bounded THE FADE-local cases (missing/support/conflict) confirm Lane E stayed context-only/non-primary with explicit omission when missing; **not** approval; **not** Phase 3 |
| Tranche 38 Lane E freshness + omission trace audit | **EXECUTED:** `audit_lane_e_freshness_omission_trace.py` + `examples/lane_e_context_bootstrap/tranche38_cases.json` + `outputs/lane_e_context_bootstrap/tranche38_lane_e_freshness_omission_audit.{json,md}` — bounded fresh/stale/missing/window-edge semantics with explicit omission tracing and no primary override; **not** approval; **not** Phase 3 |
| Tranche 39 Lane E normalization + omission-reason trace audit | **EXECUTED:** `audit_lane_e_normalization_omission_reason_trace.py` + `examples/lane_e_context_bootstrap/tranche39_cases.json` + `outputs/lane_e_context_bootstrap/tranche39_lane_e_normalization_omission_reason_trace_audit.{json,md}` — bounded normalized/omitted outcomes with explicit stale/missing/invalid-shape omission reasons and no primary override; **not** approval; **not** Phase 3 |
| Post-T39 decision stop (Tranche **39A**, Prompt **#165**) | **LOCKED (PATH B):** Lane E bootstrap paused for now after bounded T37/T38/T39 value capture; return to broader Phase 2 governance for next spend decision; **not** approval; **not** Phase 3 |
| Tranche 40 governance/registry truth-closure (Prompt **#171**) | **EXECUTED:** machine-readable governance state reconciled to executed T31-T39 artifacts + T39A stop (`mvp_lane_evidence_registry.json` updated); **no new evidence**, **no approval change**, **no Phase 3 unlock** |
| Tranche 41 Lane C FOLLOW + stale-policy trace audit (Prompt **#176**) | **EXECUTED:** THE FADE-local fixture audit confirms fresh-valid Lane C context can be accepted under FOLLOW while stale/missing/invalid-shape context is explicitly invalidated/omitted (`tranche41_lane_c_follow_stale_policy_trace_audit.{json,md}`); **not** approval; **not** Phase 3 |
| Tranche 42 Lane C FOLLOW conflict-mismatch trace audit (Prompt **#181**) | **EXECUTED:** THE FADE-local fixture audit traces primary vs market direction (aligned vs explicit bullish/bearish mismatch), stale-first omission, and missing/invalid omission with no hidden override (`tranche42_lane_c_follow_conflict_trace_audit.{json,md}`); **not** approval; **not** Phase 3 |
| Tranche 43 post-T42 Lane C decision stop (Prompt **#185**) | **LOCKED (PATH B):** Lane C bounded bootstrap paused for now after bounded T41/T42 value capture; return to broader Phase 2 governance for next spend decision; **not** approval; **not** Phase 3 |
| Tranche 44 post-T43 governance truth-closure (Prompt **#187**) | **EXECUTED:** `mvp_lane_evidence_registry.json` + control docs reconciled to post-T43 dual-pause checkpoint (T39A Lane E pause + T43 Lane C pause); **no** new lane evidence; **no** approval change; **not** Phase 3 |
| Tranche 45 Lane B failure-path / stale-outage trace audit (Prompt **#192**) | **EXECUTED:** `audit_lane_b_failure_path_stale_outage_trace.py` + `tranche45_cases.json` + `tranche45_lane_b_failure_path_stale_outage_trace_audit.{json,md}` — **local fixtures only**; explicit policy traces; **not** live FR collection; **not** approval; **not** Phase 3 |
| Tranche 47 Lane B conflict / fusion precedence trace audit (Prompt **#200**) | **EXECUTED:** `audit_lane_b_conflict_fusion_precedence_trace.py` + `examples/lane_b_conflict_fusion_bootstrap/tranche47_cases.json` + `tranche47_lane_b_conflict_fusion_precedence_trace_audit.{json,md}` — **local fixtures only**; explicit precedence + boundary/gap notes; **not** full conflict closure; **not** approval; **not** Phase 3 |
| Tranche 50 Lane B normalization viability / silent-drop trace audit (Prompt **#213**) | **EXECUTED:** `audit_lane_b_normalization_viability_silent_drop_trace.py` + `examples/lane_b_normalization_bootstrap/tranche50_cases.json` + `tranche50_lane_b_normalization_viability_silent_drop_trace_audit.{json,md}` — **local fixtures only**; representative outcomes explicit; **no** silent drop observed in bounded cases; **not** full normalization closure; **not** approval; **not** Phase 3 |
| Tranche 52 Lane B stale-context conflict omission trace audit (Prompt **#221**) | **ADOPTED AS PRE-EXISTING BOUNDED EVIDENCE:** `audit_lane_b_stale_context_conflict_omission_trace.py` + `examples/lane_b_stale_context_conflict_bootstrap/tranche52_cases.json` + `tranche52_lane_b_stale_context_conflict_omission_trace_audit.{json,md}` — **pre-existing local fixtures only**; stale-context omission explicit; stale context does **not** override primary truth in bounded cases; fresh valid context remains in the conflict branch; **does not** prove minimal `conflict` freshness consumption; **not** approval; **not** Phase 3 |
| Tranche 54 Lane B stale/outage residual policy coverage trace audit (Prompt **#226**) | **EXECUTED:** `audit_lane_b_stale_outage_residual_policy_coverage_trace.py` + `examples/lane_b_stale_outage_residual_policy_bootstrap/tranche54_cases.json` + `tranche54_lane_b_stale_outage_residual_policy_coverage_trace_audit.{json,md}` — **local fixtures plus prior T35/T45 outputs only**; explicitly covers residual escalation-policy classes `UNDEFINED_DIRECTION_MODEL` and `MISSING_REQUIRED_LANE`; **not** live FR outage evidence; **not** production closure for standard **#4**; **not** approval; **not** Phase 3 |
| Tranche 56 Lane B minimal conflict freshness-consumption truth pass (Prompt **#235**) | **EXECUTED:** `audit_lane_b_minimal_conflict_freshness_consumption_truth.py` + `examples/lane_b_minimal_conflict_freshness_truth_bootstrap/tranche56_cases.json` + `tranche56_lane_b_minimal_conflict_freshness_consumption_truth_audit.{json,md}` — **local code-path inspection plus bounded replay only**; proves the current minimal `conflict` path does **not** consume freshness-like fields and stale omission remains wrapper-only relative to that path; **not** live FR conflict freshness evidence; **not** full conflict/runtime closure; **not** approval; **not** Phase 3 |
| Tranche 58 Lane B real-slice normalization truth pass (Prompt **#246**) | **EXECUTED:** `audit_lane_b_real_slice_normalization_truth.py` + `tranche58_lane_b_real_slice_normalization_truth_audit.{json,md}` — **stored 22-slot FR slice only**; exact collector retention plus partial normalization support are evidenced, but full `normalized_signal_event` materialization remains unproved because raw-body preservation is truncated and several required normalized fields are absent or only partial; **not** approval; **not** Phase 3 |
| Tranche 60 Lane B real-slice conflict / fusion truth pass (Prompt **#255**) | **EXECUTED:** `audit_lane_b_real_slice_conflict_fusion_truth.py` + `tranche60_lane_b_real_slice_conflict_fusion_truth_audit.{json,md}` — **stored 22-slot FR slice + local `context_only_contra.example.json`**; explicit conflict/fusion boundary on disk (no observe lane JSON; no top-level `source_lane`/`direction_hint` in snapshots; `cmd_conflict` mismatch boundary vs contra); **not** full conflict closure; **not** approval; **not** Phase 3 |
| Tranche 61 Lane B conflict-replay `direction_hint` policy (Prompt **#276**) | **DECIDED:** `lane_b_phase2_conflict_replay_policy_decision.json` — **Phase 2 operator-facing** replay policy for **`lane_b_real_observation_slice.py conflict`** on **stored 22-slot** collector artifacts; classifies **slice-derived** vs **policy_fill** vs **unknown/omit**; policy-filled **`direction_hint`** and mismatch conclusions that depend on it **must** be labeled; **does not** close **conflict_handling** or **context_dominance_risk**; **not** approval; **not** Phase 3 |
| Tranche 62 Lane B Protocol A controlled stale/unavailable pass (Prompt **#283**) | **EXECUTED:** `lane_b_controlled_evidence_harness.py` Protocol A + `t62_protocol_a_*.json`; one timestamped `LANE_B_STALE_UNAVAILABLE_CONTROLLED_REPLAY_V1` observation (**no** vendor fetch); log embed + local outputs mirror (gitignored `*.json`); **controlled** only; **not** production stale/outage closure; **not** approval; **not** Phase 3 |
| Tranche 63 Lane B real observe-path pass (Prompt **#288**) | **EXECUTED:** `lane_b_real_observation_slice.py observe` — **one** HTTPS fetch to FR **`documents.json`**; **success-only** on this run (`normalized_signal_event`, HTTP **200**); local `t63_real_observe_20260404T130000Z_normalized_signal_event.json` (gitignored `*.json`; log embed); **not** scout_failure/timeout/empty on this run; **not** stale/outage standard **#4** closure; **not** approval; **not** Phase 3 |
| Tranche 64 Lane A bounded evidence charter + doc lock (Prompt **#294**) | **EXECUTED:** `docs/LANE_A_PHASE2_EVIDENCE_CHARTER_T64.md`; **Lane B default freeze**; **not** approval; **not** Phase 3 |
| Tranche 65 Lane A first bounded live observe (Prompt **#298**) | **EXECUTED:** `lane_b_real_observation_slice.py observe` + **`--source-lane lane_a_public_signal`**; Coinbase public JSON (charter URL lock); **success-only** on this run; **not** approval; **not** Phase 3 |
| Tranche 66 Lane A slice-1 stop + Lane C charter (Prompt **#302**) | **EXECUTED:** `docs/LANE_C_PHASE2_EVIDENCE_CHARTER_T66.md`; Lane A §9 stop; **no** observation in T66; **not** approval; **not** Phase 3 |
| Tranche 67 Lane C first bounded live observe (Prompt **#307**) | **EXECUTED:** `lane_b_real_observation_slice.py observe` + **`--source-lane lane_c_market_context`**; Frankfurter URL lock; **success-only** on this run; **not** approval; **not** Phase 3 |
| Tranche 68 Lane C slice-1 stop governance lock (Prompt **#311**) | **EXECUTED:** `LANE_C_PHASE2_EVIDENCE_CHARTER_T66.md` §11; **no** collection; **`partial`** preserved, not closed; **not** approval; **not** Phase 3 |
| Tranche 69 Lane E bounded evidence charter (Prompt **#314**) | **EXECUTED:** `LANE_E_PHASE2_EVIDENCE_CHARTER_T69.md`; **no** live observe in T69; **not** approval; **not** Phase 3 |
| Tranche 70 Lane E first bounded live observe (Prompt **#317**) | **EXECUTED:** `lane_b_real_observation_slice.py observe` + **`--source-lane lane_e_research_swarm_context`**; Crossref URL lock (charter §2); **`scout_failure`** (HTTP **404**) on this run; registry **`partial`**; **not** approval; **not** Phase 3 |
| Tranche 71 Lane E slice-1 stop governance lock (Prompt **#321**) | **EXECUTED:** `LANE_E_PHASE2_EVIDENCE_CHARTER_T69.md` §12; **no** collection; **`partial`** preserved, not closed; **no** default next lane; **not** approval; **not** Phase 3 |
| Tranche 73 MVP approval-scope decision lock (Prompt **#325**) | **EXECUTED:** first scope lock in `phase2_mvp_approval_scope_decision.json` (**superseded in-file by T74**) |
| Tranche 74 Amend MVP approval scope to scoped MVP path (Prompt **#326**) | **EXECUTED:** **same** `phase2_mvp_approval_scope_decision.json` **amended** — **subset-of-lanes-eligible**; **governance only**; **`mvp_lane_approval.json` unchanged**; **not** approval; **not** Phase 3 |
| Tranche 75 Lane B primary-eligibility charter (Prompt **#327**; repaired **#328**) | **EXECUTED:** `LANE_B_PRIMARY_ELIGIBILITY_CHARTER_T75.md`; **governance-acceptance pack** (**four** dimensions); **`stale_outage_behavior` out of scope**; **`mvp_lane_approval.json` unchanged**; **not** approval; **not** Phase 3 |
| Tranche 76 Lane B scoped MVP governance acceptance pack (Prompt **#329**) | **EXECUTED:** `lane_b_t76_scoped_mvp_governance_acceptance_pack.json` + `LANE_B_T76_SCOPED_MVP_GOVERNANCE_ACCEPTANCE_MEMO.md`; **`subset_acceptance_established`** for **four** dimensions; **`stale_outage_behavior` not** accepted at T76 alone; **no** new evidence; **`mvp_lane_approval.json` unchanged**; **not** approval; **not** Phase 3 |
| Tranche 78 Lane B reliability + stale_outage scoped MVP governance acceptance pack (Prompt **#334**) | **EXECUTED:** `lane_b_t78_scoped_mvp_governance_acceptance_pack.json` + `LANE_B_T78_SCOPED_MVP_GOVERNANCE_ACCEPTANCE_MEMO.md`; **`subset_acceptance_established`**; **does not** revisit T76 four dimensions; **`primary_lane_eligibility_met_after_this_pack`:** **`true`** **with T76**; **no** new evidence in T78 |
| Tranche 80 Scoped MVP approval decision (Prompt **#336**) | **EXECUTED:** `t80_scoped_mvp_approval_decision.json` (**`scoped_mvp_approval_decision`:** **`YES`**) + `mvp_lane_approval.json` **`approved: true`** + `phase2_mvp_approval_scope_decision.json` **`as_of_t80_on_disk_assessment`**; **no** evidence; **no** code; **no** lane reopen; **scoped MVP approval granted**; **not** Phase **3**; **not** production maturity |
| Prompt **#337** T80 repair (timestamps + `deferred_lanes`) | **EXECUTED:** `effective_utc` / `as_of_t80.effective_utc` / `approved_at` → **2026-04-06T19:40:51Z**; registry **`approval_state.deferred_lanes: []`**; **`current_approval_truth.deferred_lanes: []`**; **YES** unchanged; **no** lane reopen; **not** Phase **3** |
| Tranche 82 Post-T80 Phase 3 entry governance lock (Prompt **#342**) | **EXECUTED:** `phase2_mvp_approval_scope_decision.json` **`post_t82_on_disk_governance_lock`** + **`phase3_entry_planning_only_definition`** + amended **`next_tranche_authorization_rule`** / **`anti_drift_rule`**; **no** `mvp_lane_approval.json`; **no** registry; **no** code; **no** lane reopen; **planning-only** next class **allowed**; **implementation** **forbidden** until later governance |
| Tranche 83 Phase 3 entry planning lock (Prompt **#345**) | **EXECUTED:** `future_modules/the_fade/docs/THE_FADE_PHASE3_ENTRY_PLAN_T83.md` + `future_modules/the_fade/docs/THE_FADE_PHASE3_IMPLEMENTATION_BOUNDARY_T83.md`; **`post_t83_phase3_entry_planning_package`** in `phase2_mvp_approval_scope_decision.json`; **planning only**; **no** implementation code; **no** lane reopen; **later** explicit **Phase 3 implementation governance** required before executable Phase **3** |
| Tranche 84 First implementation slice governance lock (Prompt **#346**) | **EXECUTED:** `future_modules/the_fade/docs/THE_FADE_T84_FIRST_IMPLEMENTATION_SLICE_GOVERNANCE.md` + `future_modules/the_fade/docs/THE_FADE_T84_FIRST_IMPLEMENTATION_SLICE_ACCEPTANCE_CRITERIA.md`; **`post_t84_first_implementation_slice_governance`** in `phase2_mvp_approval_scope_decision.json`; **governance only**; **no** code in **T84**; **no** lane reopen; **one** **future** tranche **only** for **static** contract artifacts per **T84** |
| Tranche 85 Static universe-scanner I/O contract slice (Prompt **#350**) | **EXECUTED:** `future_modules/the_fade/contracts/phase3_universe_scanner_io/`; **`post_t85_static_universe_scanner_io_contract_slice`** in `phase2_mvp_approval_scope_decision.json`; **static** schemas/examples/`.pyi`/README **only**; **not** runnable scanner; **no** lane reopen |
| Tranche 86 Second implementation slice governance — offline validation (Prompt **#354**) | **EXECUTED:** `THE_FADE_T86_SECOND_SLICE_GOVERNANCE_OFFLINE_VALIDATION.md` + `THE_FADE_T86_SECOND_SLICE_ACCEPTANCE_CRITERIA.md`; **`post_t86_second_slice_governance_offline_validation`** in `phase2_mvp_approval_scope_decision.json`; **governance only** — **no** validator code in **T86**; **no** lane reopen; **one** **future** **offline** validation tranche **authorized** |
| Tranche 87 Offline contract validation harness build (Prompt **#358**) | **EXECUTED:** `contracts/phase3_universe_scanner_io/tools/validate_universe_scanner_io_contracts.py` + `contracts/phase3_universe_scanner_io/tools/README.md`; **`post_t87_offline_contract_validation_harness`** in `phase2_mvp_approval_scope_decision.json`; local validation only; no scanner/request-to-result/runtime/provider/dashboard/lane-reopen work |
| Tranche 88 First live ingress slice governance lock (Prompt **#359**) | **EXECUTED:** `THE_FADE_T88_FIRST_LIVE_INGRESS_SLICE_GOVERNANCE.md` + `THE_FADE_T88_FIRST_LIVE_INGRESS_SLICE_ACCEPTANCE_CRITERIA.md`; **`post_t88_first_live_ingress_slice_governance`** in `phase2_mvp_approval_scope_decision.json`; governance only; no ingress code in T88; one future Federal Register ingress slice authorized |
| Tranche 89 First live Federal Register ingress slice (Prompt **#360**) | **EXECUTED:** `ingress/federal_register/build_universe_scanner_request_from_federal_register.py` + `ingress/federal_register/README.md`; **`post_t89_first_live_federal_register_ingress_slice`**; read-only FR fetch + schema-valid request packet under `inputs/phase3_universe_scanner_requests/`; not scanner execution |
| Tranche 90 Offline ingress-request validation governance (Prompt **#365**) | **EXECUTED:** `THE_FADE_T90_OFFLINE_VALIDATION_OF_INGRESS_REQUEST_PACKETS_GOVERNANCE.md` + `THE_FADE_T90_OFFLINE_VALIDATION_OF_INGRESS_REQUEST_PACKETS_ACCEPTANCE_CRITERIA.md`; **`post_t90_offline_validation_of_ingress_request_packets_governance`**; governance only; **`validate_ingress_request_packets.py`** not built in T90; one future tranche authorized for that validator only |
| Tranche 91 Ingress-request offline validator (Prompt **#366**) | **EXECUTED:** `contracts/phase3_universe_scanner_io/tools/validate_ingress_request_packets.py` + `README_ingress_request_packets.md`; **`post_t91_offline_ingress_request_packet_validator`**; optional `inputs/phase3_universe_scanner_requests/fixtures_invalid/`; ingress-request validation only |
| Tranche 93 Offline UniverseScannerResult packet validation governance (Prompt **#368**; **#369** Model B repair) | **EXECUTED:** `THE_FADE_T93_OFFLINE_VALIDATION_OF_UNIVERSE_SCANNER_RESULT_PACKETS_GOVERNANCE.md` + `THE_FADE_T93_OFFLINE_VALIDATION_OF_UNIVERSE_SCANNER_RESULT_PACKETS_ACCEPTANCE_CRITERIA.md`; **`post_t93_offline_validation_of_universe_scanner_result_packets_governance`**; governance only in T93; authorizes **T94** implementation slice |
| Tranche 94 Offline UniverseScannerResult packet validator (Prompt **#374**) | **EXECUTED:** `contracts/phase3_universe_scanner_io/tools/validate_universe_scanner_result_packets.py` + `README_universe_scanner_result_packets.md`; **`post_t94_offline_universe_scanner_result_packet_validator`**; optional static root seed + **`fixtures_invalid/`** (documented); validation only — **not** scanner or result production path |
| Tranche 95 First request→result bridge governance (Prompt **#375**) | **EXECUTED:** `THE_FADE_T95_FIRST_REQUEST_TO_RESULT_BRIDGE_GOVERNANCE.md` + `THE_FADE_T95_FIRST_REQUEST_TO_RESULT_BRIDGE_ACCEPTANCE_CRITERIA.md`; **`post_t95_first_request_to_result_bridge_governance`**; **governance only** in T95; authorizes **T96** bridge build |
| Tranche 96 First request→result bridge build (Prompt **#378**; **#379** timestamp/artifact clarity) | **EXECUTED:** `bridge/first_request_to_result/build_universe_scanner_result_from_single_request.py` + `README.md`; **`post_t96_first_request_to_result_bridge`**; **one** **`bridge_universe_scanner_result_*.json`** on disk from T96 verification — **bounded local tranche artifact**; **not** scanner; mechanical bridge only — **not** production pipeline |
| Tranche 97 Local end-to-end happy-path runner governance (Prompt **#381**) | **EXECUTED:** `THE_FADE_T97_LOCAL_END_TO_END_HAPPY_PATH_RUNNER_GOVERNANCE.md` + `THE_FADE_T97_LOCAL_END_TO_END_HAPPY_PATH_RUNNER_ACCEPTANCE_CRITERIA.md`; **`post_t97_local_end_to_end_happy_path_runner_governance`**; **governance only**; **one** future tranche may add **`runner/local_happy_path/run_local_end_to_end_happy_path.py`** only (+ optional `README.md` + optional one tiny helper in same dir); **no** runner code in T97 |
| Tranche 98 Local end-to-end happy-path runner build (Prompt **#384**) | **EXECUTED:** `runner/local_happy_path/run_local_end_to_end_happy_path.py`; **`post_t98_local_end_to_end_happy_path_runner_build`**; local-only sequential orchestration of existing tools (T89→T91→T96→T94), console-only summary, request/result path reporting, non-zero failure propagation; **not** scanner/runtime/provider/dashboard code |
| Tranche 107 Operator review gate signal governance (Prompt **#399**) | **EXECUTED (governance only):** `THE_FADE_T107_OPERATOR_REVIEW_GATE_SIGNAL_GOVERNANCE.md` + `THE_FADE_T107_OPERATOR_REVIEW_GATE_SIGNAL_ACCEPTANCE_CRITERIA.md`; **`post_t107_operator_review_gate_signal_governance`** in `phase2_mvp_approval_scope_decision.json`; **not** scanner/ranking/runtime/provider expansion |
| Tranche 108 Operator review gate signal build (Prompt **#400**) | **EXECUTED:** `review/local_run/build_operator_review_gate_signal_from_run_folder.py`; **`post_t108_operator_review_gate_signal_build`**; per-run `operator_review_gate.json`; mechanical JSON gate only; **not** scanner/ranking/runtime/provider expansion |
| Tranche 109 Local operator review queue governance (Prompt **#402**) | **EXECUTED (governance only):** `THE_FADE_T109_LOCAL_OPERATOR_REVIEW_QUEUE_GOVERNANCE.md` + `THE_FADE_T109_LOCAL_OPERATOR_REVIEW_QUEUE_ACCEPTANCE_CRITERIA.md`; **`post_t109_local_operator_review_queue_governance`**; **not** scanner/ranking/runtime/provider expansion |
| Tranche 110 Local operator review queue build (Prompt **#403**) | **EXECUTED:** `review/local_run/build_operator_review_queue.py`; **`post_t110_local_operator_review_queue_build`**; **`outputs/local_happy_path_runs/operator_review_queue.json`**; mechanical queue only; **not** scanner/ranking/runtime/provider expansion |
| Tranche 111 First operator-meaningful filtering signal governance (Prompt **#405**) | **EXECUTED (governance only):** `THE_FADE_T111_FIRST_OPERATOR_MEANINGFUL_FILTERING_SIGNAL_GOVERNANCE.md` + `THE_FADE_T111_FIRST_OPERATOR_MEANINGFUL_FILTERING_SIGNAL_ACCEPTANCE_CRITERIA.md`; **`post_t111_first_operator_meaningful_filtering_signal_governance`**; **one** future tranche may add **`review/local_run/build_operator_attention_signal_from_run_folder.py`** → per-run **`operator_attention_signal.json`**; **no** attention script in T111; **not** scanner/ranking/runtime/provider expansion |

**Phase 2 work completed and committed (checkpoint list):** approval gate prep; deferred approval decision; lane B evidence pack + refinement passes; honest blocker documentation; controlled evidence protocol; minimal harness build + hardening; simulated rehearsal + correction + reproducibility cleanup; real evidence path audit; minimal real evidence path spec + correction; lane B real observation slice build; canon recovery from stash snapshot into `future_modules/stock_module/`; post-canon dirty-state cleanup (registry/log/contra alignment); **Tranche 18** reliability-window honesty pass (`docs/MVP_LANE_EVIDENCE_LOG.md`, `docs/MVP_SOURCE_RELIABILITY_AUDIT.md` -- four countable `observe` tries in one session; **no** valid 0.8 gate statistic); **Tranche 19** lane B provider/source class clarification (log + audit + `LANE_B_MINIMAL_REAL_EVIDENCE_PATH_SPEC.md` -- **one** source class per reliability pass; provisional next target **Federal Register API** only for that pass, not mixed with SEC/issuer); **Tranche 20** single-source reliability pass (Federal Register API only; 5 attempts / 5 successes / 0 failures; still **no** honest comparison to 0.8 yet); **Tranche 21** pre-audit reliability window protocol defined (Federal Register API-only; 48h UTC window; 2h cadence; count normalized_signal_event as success vs scout_failure as failure; compare to 0.8 only after >=20 counted attempts) -- **stricter target preserved** in audit; **Tranche 22-23** -- **2** counted attempts on original UTC grid (`t22_fr_000`, `t22_fr_001`); **Tranche 24** -- **availability-constrained interim pilot** (**CDT** schedule; **<=8** ceiling); Prompts **#75/#78/#80/#82/#86/#88** -- all six pilot slots observed (`t24_fr_pilot_01`, `t24_fr_pilot_02`, `t24_fr_pilot_03`, `t24_fr_pilot_04`, `t24_fr_pilot_05`, `t24_fr_pilot_06`); cumulative **8** counted / **8** successes / **0** failures in this slice; **final interim pilot result** only; **not** full pre-audit gate window; **no** 0.8 conclusion; **Tranche 25 closeout audit complete** (interim pilot done: 6/6 slots, 8/8 successes; proved positive interim success-path signal; did **not** satisfy the original Tranche 21 gate protocol; therefore does **not** justify any `required_reliability_threshold` **0.8** comparison or any approval re-evaluation; approval remains **not justified**); **Tranche 26** post-pilot go/no-go: lane B **parked** promising-but-unapproved; **Tranche 27-30** bounded slot collector (`run_tranche21_fr_slot.py`); **full Tranche 21** FR window **complete on disk** (**22** counted / **22** successes / **0** failures; **`t30_valid_002`** smoke excluded); **Prompt #102** governed markdown reconciliation (**no** approval change); **NO-GO** on Phase 3 until full gate satisfied).

**Real observation slice:** implemented (`lane_b_real_observation_slice.py`) -- **does not** justify approval re-evaluation or MVP lane selection by itself.

**Registry nuance:** **Lane A** — **slice-1 STOP** (T66); **`partial`**; further Lane A only under **new Lane A charter**. **Lane C** — **slice-1 STOP** (T68); **`partial`**; further Lane C live evidence only under **new Lane C charter**. **Lane E** — **T71** **slice-1 STOP** (Prompt **#321**); **T70** live **`scout_failure`** on record; **`evidence_status` `partial`** (**preserved, not closed**); further Lane E **live** evidence only under **new Lane E charter**; T37–T39 fixtures on disk (**not** this live slice). **Lane B** — **new tranches frozen by default** post–T64 (reopen via new Lane B charter); Lane B **Federal Register** full-window **reliability slice** is **documented** (**22**/**22**/**0**); **freshness** — **Prompt #132** **adopts** **`strict_midnight_utc`** (**12**/**0**/**10** **cannot_classify_honestly**); **freshness-only** tranche line **parked**; **normalization** — **Prompt #133** breadth audit remains **partial** (**preview truncated**), **Prompt #213** adds a bounded explicit silent-drop trace with **no** silent drop observed in representative local cases, and **Prompt #246 / T58** now proves the stored 22-slot real slice preserves exact collector retention plus partial normalization support while still not proving full normalized-event materialization; **conflict/stale-context handling** — adopted pre-existing **Prompt #221 / T52** artifacts add a bounded stale-first omission wrapper, **Prompt #235 / T56** now proves the current minimal `lane_b_real_observation_slice.py conflict` subcommand itself does **not** consume freshness-like fields and does **not** stale-omit valid context, so that omission remains wrapper-only relative to the minimal path, **Prompt #255 / T60** now proves the parallel **real-slice** boundary: collector artifacts do **not** include observe lane JSON or top-level `source_lane` / `direction_hint`, so `cmd_conflict` mismatch vs local contra requires explicit policy fill for `direction_hint`, and **Prompt #276 / T61** locks **`lane_b_phase2_conflict_replay_policy_decision.json`** so operator replay **must** label slice-derived vs **policy_fill** vs unknown for that path — still **not** **conflict_handling** or **context_dominance_risk** closure; **stale/outage** — **Prompt #226 / T54** adds bounded explicit coverage for residual escalation-policy classes `UNDEFINED_DIRECTION_MODEL` and `MISSING_REQUIRED_LANE`; **Prompt #283 / T62** adds **one** **Protocol A controlled harness** observation with explicit UTC timestamps and **`observed_behavior`** (**no** vendor fetch) — **partial** incremental evidence only; **Prompt #288 / T63** adds **one** **real** **`lane_b_real_observation_slice.py observe`** HTTPS success-only attempt (HTTP **200**, `normalized_signal_event`) — **does not** evidence **`scout_failure`**, timeout, or empty-row on that run, **not** production standard **#4** closure. **Overall** MVP gate remains **`partial`** in registry `dimension_evidence_status`. **T76** + **T78** governance packs document explicit scoped MVP **(b)** for all six dimensions — **`primary_lane_rule` per-dimension (a)|(b)** **supportable** on disk per T78 **`primary_lane_eligibility_rationale`**. **T80** records **`scoped_mvp_approval_decision`:** **`YES`** and sets **`mvp_lane_approval.json`** **`approved: true`** (four lanes) under **`eligibility_rule_single_reading`** — **scoped** path only; **not** Phase **3**; **not** production maturity; partialities above **unchanged** as honest record.

**Discipline:** Use this master checklist for periodic checkpointing to avoid scope drift.

**Gate-review-now discipline (Prompt #103):** this checkpoint is a **review-and-doc-alignment hold**, not new build scope. Keep scrutiny adversarial and risk-first against over-reading one strong FR slice; keep guardrail concepts as future-only; keep any execution-adjacent build in parking lot until a later governed prompt.

---

## Live phase-status table (master phases)

| Phase (see §5 Locked Tranche Order) | Status |
|-------------------------------------|--------|
| Phase 0 -- Canon Lock + Build Map | **COMPLETE** (effective for current build path) |
| Phase 1 -- Scout Contracts and Policy Foundations | **COMPLETE FOR CURRENT PROOF PATH** |
| Phase 2 -- MVP Data Stack and Source Reliability Pre-Audit | **ACTIVE** — **scoped MVP approval granted** (**T80**); binding **`mvp_lane_approval.json`** **`approved: true`** |
| Phases 3-16 -- Universe Scanner through Tiny Live Pilot | **NOT STARTED** (executable scanner/runtime) — **T85** static I/O contracts on disk; **T87** contract-tree validator on disk; **T91** ingress-request offline validator on disk; **T93** governs result-packet offline validation + **#369** **Model B** valid-root rule (**not** built in T93); **T98** local sequential runner is implemented but remains bounded orchestration only; executable scanner/runtime/pilot still blocked pending new governance |

---

# 1. Purpose of This Document

This document is the **locked master build checklist** for THE FADE system.

It exists to prevent:

* scope drift
* architecture drift
* dashboard drift
* premature autonomy
* paper-trade fantasy before signal proof
* random new ideas from derailing the build sequence

This is the control document for the full build.

It defines:

* the full tranche order
* what uses Plan Mode
* what uses step-by-step execution
* where proof gates exist
* what is deferred
* what must not be built early

---

# 2. Master Build Rule

## Use both Cursor modes, but at different levels

* **Plan Mode** = for **tranche planning**, dependency mapping, scope cutting, proof-gate design, and file/module ordering
* **Step-by-step mode** = for **actual implementation**, proof, doc-lock, dashboard update when needed, and bounded commit/push

That is the hybrid build method.

## Hard rule

Do **not** use Plan Mode to try to build the whole system in one giant shot.

Do **not** use step-by-step mode with no architecture map.

The correct process is:

1. plan the tranche
2. review the plan
3. build the tranche step-by-step
4. prove the tranche
5. update docs/dashboard if needed
6. commit the tranche
7. move to the next tranche

---

# 3. Legend

* **\[PLAN]** = use Cursor Plan Mode
* **\[STEP]** = execute in normal step-by-step mode
* **\[DOC]** = doc-lock required
* **\[DASH]** = dashboard must be checked/updated if operator visibility changes
* **\[PROOF]** = hard proof gate before next tranche
* **\[DEFER]** = explicitly not in scope yet

---

# 4. Absolute Red-Line Rules

These rules apply across the whole build.

* \[ ] Do not skip the scout proof slice
* \[ ] Do not build paper trading before the signal packet layer is trustworthy
* \[ ] Do not build autonomy before paper proof and hardening
* \[ ] Do not let dashboard work outrun backend truth
* \[ ] Do not let shadow lanes pretend to be primary evidence
* \[ ] Do not let synthetic feedback outrank real paper-trade results
* \[ ] Do not let Safety Governor become advisory only
* \[ ] Do not let "fewest steps" turn into giant risky build chunks
* \[ ] Do not outrun Jarvis phase discipline
* \[ ] Do not treat initial weights/thresholds as proven truth
* \[ ] Do not let new ideas override the locked tranche order without deliberate review

Future-only guardrail (not active in current tranche, does not unlock Phase 3): Lane E remains context-only/non-dominant, and paid signal rails (`x402`/A2A), ChainCash/agent-payment rails, and tokenized-equity/prediction-market/execution-stack concepts remain deferred architecture research only.

---

# 5. Locked Tranche Order

This is the master order.

1. Phase 0 -- Canon Lock + Build Map
2. Phase 1 -- Scout Contracts and Policy Foundations
3. Phase 2 -- MVP Data Stack and Source Reliability Pre-Audit
4. Phase 3 -- Universe Scanner
5. Phase 4 -- Event Normalization
6. Phase 5 -- Lane Scoring
7. Phase 6 -- Contra-Signal Engine
8. Phase 7 -- Fusion / Conflict / Signal Packet
9. Phase 8 -- Signal Review Dashboard
10. Phase 9 -- Research Handoff + Downstream Analyst Layer
11. Phase 10 -- Paper Trade Engine
12. Phase 11 -- Daily Summary and Operator Review Loop
13. Phase 12 -- Learning / Calibration
14. Phase 13 -- Hardening / Replay / Health
15. Phase 14 -- Autonomous Transition
16. Phase 15 -- Live-Readiness Review
17. Phase 16 -- Tiny Live Pilot

---

# Phase 0 -- Canon Lock + Build Map

**Mode:** \[PLAN]  
**Why first:** if the architecture is not locked now, the build will drift later.

## Purpose

Turn the document set into a real implementation graph.

## Checklist

* \[ ] Confirm canonical document set is the source of truth
* \[ ] Resolve any remaining contradictions across docs
* \[ ] Freeze the first bounded proof slice
* \[ ] Freeze the Minimal Viable Data Stack
* \[ ] Freeze the module boundary:

  * \[ ] THE FADE scout
  * \[ ] downstream research/risk
  * \[ ] paper trading
  * \[ ] daily summaries
  * \[ ] learning
  * \[ ] later autonomy/live-readiness
* \[ ] Create dependency map
* \[ ] Identify dashboard impacts by tranche
* \[ ] Identify schema/contracts needed first
* \[ ] Identify reusable old stock side-quest work
* \[ ] Identify obsolete old stock framing

## Plan Mode output required

* \[ ] tranche list
* \[ ] dependency graph
* \[ ] file/module creation order
* \[ ] proof gates
* \[ ] dashboard impact notes
* \[ ] deferred list

## Proof gate \[PROOF]

* \[ ] The whole build can be described in ordered tranches without contradiction
* \[ ] The first proof slice is narrow and explicit
* \[ ] No downstream phase is pretending to be MVP

---

# Phase 1 -- Scout Contracts and Policy Foundations

**Mode:** \[PLAN] then \[STEP]

## Purpose

Define the scout-layer contracts and policy foundations.

## Plan Mode focus

* schemas
* config registries
* lane registry
* direction-model registry
* threshold/weight defaults
* escalation matrix
* output artifact contracts

## Step-by-step checklist

* \[ ] Define `fade_task_packet` contract
* \[ ] Define `scanner_candidate_set` contract
* \[ ] Define `normalized_signal_event` contract
* \[ ] Define `lane_scorecard` contract
* \[ ] Define `contra_signal_result` contract
* \[ ] Define `signal_packet` contract
* \[ ] Define `conflict_packet` contract
* \[ ] Define failure artifact contract
* \[ ] Define lane registry
* \[ ] Define direction-model registry
* \[ ] Define threshold/weight policy registry
* \[ ] Define scanner policy
* \[ ] Define escalation policy
* \[ ] Define Safety Governor baseline structure
* \[ ] Define Heartbeat Monitor contract placeholders
* \[ ] Mark all weights/thresholds as initial defaults

## Deliverables

* \[ ] scout schemas
* \[ ] policy/config files
* \[ ] validation rules
* \[ ] failure-state definitions

## Proof gate \[PROOF]

* \[ ] Every core scout artifact has a schema
* \[ ] Direction models are explicit
* \[ ] Failure conditions are explicit
* \[ ] No downstream code is needed yet

---

# Phase 2 -- MVP Data Stack and Source Reliability Pre-Audit

**Mode:** \[PLAN] then \[STEP]

## Purpose

Constrain the system to a realistic MVP data stack.

## Plan Mode focus

* exact MVP sources
* exact deferred sources
* fallback logic
* field availability
* reliability risks

## Step-by-step checklist

* \[ ] Pick one official/disclosure lane for MVP
* \[ ] Pick one market-data lane for MVP
* \[ ] Pick one curated public-signal lane for MVP
* \[ ] Define Research Swarm as context-only
* \[ ] Create source reliability scorecard for each MVP source
* \[ ] Define freshness windows per lane
* \[ ] Define lag classes per lane
* \[ ] Define trust tiers per lane
* \[ ] Define deferred source list
* \[ ] Define outage behavior per lane
* \[ ] Define stale-data behavior per lane

## Deliverables

* \[ ] MVP lane source list
* \[ ] source reliability audit
* \[ ] deferred source register
* \[ ] freshness/trust rules

## Proof gate \[PROOF]

* \[ ] MVP data stack is small enough to build
* \[ ] No phase-1 dependence on vendor sprawl
* \[ ] Missing/stale source behavior is defined before adapter implementation

---

# Phase 3 -- Universe Scanner

**Mode:** \[PLAN] then \[STEP]

## Purpose

Create the candidate-generation front end.

## Plan Mode focus

* candidate generation rules
* scanner passes
* daily cap
* scanner output artifact
* proof cases

## Step-by-step checklist

* \[ ] Implement candidate-set contract
* \[ ] Implement first-pass scanner policy
* \[ ] Build Pass A
* \[ ] Build Pass B
* \[ ] Build Pass C only if it is inside MVP scope
* \[ ] Defer non-MVP passes
* \[ ] Implement scanner output writer
* \[ ] Implement candidate exclusion rules
* \[ ] Implement candidate cap
* \[ ] Implement scanner logging

## Deliverables

* \[ ] scanner script
* \[ ] scanner output artifacts
* \[ ] scanner validation

## Proof gate \[PROOF]

* \[ ] Scanner produces bounded candidate lists
* \[ ] No invented candidates
* \[ ] Output is reusable by the scout layer

---

# Phase 4 -- Event Normalization

**Mode:** \[STEP]

## Purpose

Convert raw evidence into one normalized event structure.

## Step-by-step checklist

* \[ ] Implement normalized event schema validator
* \[ ] Implement raw → normalized mapping for official lane
* \[ ] Implement raw → normalized mapping for market lane
* \[ ] Implement raw → normalized mapping for curated public-signal lane
* \[ ] Implement context-only normalization for Research Swarm enrichment
* \[ ] Implement duplicate/derivative detection fields
* \[ ] Implement parser-confidence handling
* \[ ] Implement failed-normalization artifact writer
* \[ ] Implement evidence-path preservation

## Deliverables

* \[ ] normalized event writer
* \[ ] failed event writer
* \[ ] lane-specific mapping logic

## Proof gate \[PROOF]

* \[ ] One source event from each MVP lane can be normalized
* \[ ] Normalization failures are explicit
* \[ ] Evidence traceability is intact

---

# Phase 5 -- Lane Scoring

**Mode:** \[STEP]

## Purpose

Convert normalized events into lane-level scorecards.

## Step-by-step checklist

* \[ ] Implement lane scorecard contract
* \[ ] Implement Lane A scoring
* \[ ] Implement Lane B scoring
* \[ ] Implement Lane C scoring
* \[ ] Implement Lane E enrichment limits
* \[ ] Apply v2 direction models as canonical
* \[ ] Apply freshness penalties
* \[ ] Apply lag penalties
* \[ ] Apply trust modifiers
* \[ ] Apply duplicate penalties
* \[ ] Record conditions hit/missed
* \[ ] Record score rationale

Future-only insertion point: add data-trust/token-risk screening and explicit Lane E lag/freshness/trust/duplication penalties at scoring time after current Phase 2 gate closure; not active now.

## Deliverables

* \[ ] lane scorecard writer
* \[ ] score validation
* \[ ] score rationale output

## Proof gate \[PROOF]

* \[ ] One ticker can receive lane scorecards from available lanes
* \[ ] Scoring is explainable
* \[ ] Undefined direction models escalate instead of silently scoring

---

# Phase 6 -- Contra-Signal Engine

**Mode:** \[STEP]

## Purpose

Add adversarial / contradiction checks before fusion.

## Step-by-step checklist

* \[ ] Implement contra-result contract
* \[ ] Define contra checks
* \[ ] Implement contradiction detection
* \[ ] Implement weakening factors
* \[ ] Implement market-behavior contradiction checks
* \[ ] Implement forced conflict conditions
* \[ ] Implement contra artifact output
* \[ ] Link contra output to signal packet pipeline

Future-only insertion point: add critic/adversarial/dissent-memory controls and Lane E contra-coupling safeguards before any autonomy escalation work; not active in the current tranche.

## Deliverables

* \[ ] contra-result artifacts
* \[ ] forced-conflict behavior
* \[ ] auditable contra reasons

## Proof gate \[PROOF]

* \[ ] The engine can produce a non-trivial contra result
* \[ ] A candidate can be downgraded or forced into conflict
* \[ ] Contra logic is visible, not hidden

---

# Phase 7 -- Fusion / Conflict / Signal Packet

**Mode:** \[PLAN] then \[STEP]

## Purpose

Produce the first real scout output.

## Plan Mode focus

* fusion order
* conflict thresholds
* regime-aware weighting policy
* shadow-lane treatment
* final signal classes
* packet output sequence
* proof scenarios

## Step-by-step checklist

* \[ ] Implement fusion engine
* \[ ] Implement conflict logic
* \[ ] Implement bearish and bullish classifications
* \[ ] Implement no-signal/weak outputs
* \[ ] Implement regime-aware weighting defaults
* \[ ] Implement shadow-lane confidence caps
* \[ ] Implement signal packet writer
* \[ ] Implement conflict packet writer
* \[ ] Implement escalation path for invalid output
* \[ ] Implement heartbeat production metrics for scout output

Future-only insertion point: enforce Lane E enrichment limits and explicit non-dominance checks at fusion/conflict output boundaries; not active in current Phase 2 scope.

## Deliverables

* \[ ] valid signal packet
* \[ ] valid conflict packet
* \[ ] scout health signals

## Proof gate \[PROOF]

* \[ ] First full scout proof slice passes
* \[ ] Conflict is explicit
* \[ ] Weak/no-signal paths work
* \[ ] Scout output is operator-reviewable

---

# Phase 8 -- Signal Review Dashboard

**Mode:** \[PLAN] then \[STEP] \[DASH]

## Purpose

Make scout outputs reviewable by the operator.

## Plan Mode focus

* review page
* review index/state loader
* packet detail layout
* conflict callout
* health warnings
* empty/partial states

## Step-by-step checklist

* \[ ] Build signal review index loader
* \[ ] Build `/fade-signals`
* \[ ] Show signal classes
* \[ ] Show source breakdown
* \[ ] Show evidence links
* \[ ] Show conflict state
* \[ ] Show contra summary
* \[ ] Show freshness
* \[ ] Show triage state
* \[ ] Build minimal `/fade-health`
* \[ ] Add stale-source warning display
* \[ ] Add invalid-packet warning display

## Deliverables

* \[ ] operator-reviewable signal page
* \[ ] minimal health page

## Proof gate \[PROOF]

* \[ ] Operator can review signal packets cleanly
* \[ ] Dashboard shows actual packet truth
* \[ ] No fake analytics

---

# Phase 9 -- Research Handoff + Downstream Analyst Layer

**Mode:** \[PLAN] then \[STEP]

## Purpose

Connect strong signals to research brief and risk gate.

## Plan Mode focus

* signal → research handoff
* reuse of existing brief/risk-gate work
* linkage fields
* file/path migration if needed
* dashboard consequences

## Step-by-step checklist

* \[ ] Define research handoff packet
* \[ ] Link signal packet → brief trigger
* \[ ] Link brief → risk gate trigger
* \[ ] Link signal packet IDs through downstream artifacts
* \[ ] Reposition existing brief/risk-gate logic as downstream analyst layer
* \[ ] Validate linkage from signal packet to downstream outputs
* \[ ] Build `/fade-research`
* \[ ] Show brief + risk gate linked to selected signal

Future-only insertion point: Research Scout / repo-watchlist style research lane can be considered only after the core proof loop is stable; not active in the current tranche.

## Deliverables

* \[ ] one linked signal → brief → risk gate path
* \[ ] research review surface

## Proof gate \[PROOF]

* \[ ] One signal packet successfully flows into downstream review
* \[ ] No orphaned brief/risk outputs
* \[ ] Research is clearly downstream

---

# Phase 10 -- Paper Trade Engine

**Mode:** \[PLAN] then \[STEP]

## Purpose

Start simulated execution.

## Plan Mode focus

* trade candidate contract
* entry/exit assumptions
* fill rules
* position lifecycle
* P\&L accounting
* portfolio snapshots
* safety limits

## Step-by-step checklist

* \[ ] Define trade candidate packet
* \[ ] Define entry rule structure
* \[ ] Define stop/invalidation rule
* \[ ] Define target rule
* \[ ] Define time-stop rule
* \[ ] Implement paper trade open logic
* \[ ] Implement paper trade close logic
* \[ ] Implement spread model
* \[ ] Implement slippage model
* \[ ] Implement fee model
* \[ ] Implement overnight gap rule
* \[ ] Implement stale-quote behavior
* \[ ] Implement position tracker
* \[ ] Implement portfolio snapshot writer
* \[ ] Implement paper-trade hard limits
* \[ ] Link every trade back to signal packet + brief/risk artifacts

Future-only insertion point: paper-mode-first remains mandatory before any real execution path, with liquidity/slippage/execution-reality constraints required before any later live-readiness consideration.

## Deliverables

* \[ ] paper trade records
* \[ ] open/closed position tracking
* \[ ] reliable P\&L logic

## Proof gate \[PROOF]

* \[ ] First paper trade lifecycle is reproducible
* \[ ] P\&L is believable under explicit simulation assumptions
* \[ ] No trade exists without upstream linkage

---

# Phase 11 -- Daily Summary and Operator Review Loop

**Mode:** \[PLAN] then \[STEP] \[DASH]

## Purpose

Create the daily review surface the operator wants.

## Plan Mode focus

* summary schema
* daily aggregation logic
* dashboard view
* plain-English summary
* autonomy metrics later if relevant

## Step-by-step checklist

* \[ ] Define daily summary schema
* \[ ] Compute starting balance
* \[ ] Compute ending balance
* \[ ] Compute realized/unrealized P\&L
* \[ ] Compute daily/cumulative P\&L
* \[ ] Count opened/closed trades
* \[ ] Count winners/losers
* \[ ] Count signals by class
* \[ ] Count conflicts
* \[ ] Compute lane contribution summary
* \[ ] Generate markdown summary
* \[ ] Generate JSON summary
* \[ ] Build `/fade-daily-summary`
* \[ ] Make positive/negative day obvious
* \[ ] Add plain-English operator summary block

## Deliverables

* \[ ] daily summary artifacts
* \[ ] daily summary page

## Proof gate \[PROOF]

* \[ ] One full day can be summarized from artifacts alone
* \[ ] End-of-day balance is obvious
* \[ ] Operator can see what traded and why

---

# Phase 12 -- Learning / Calibration

**Mode:** \[PLAN] then \[STEP]

## Purpose

Start learning without losing control.

## Plan Mode focus

* learning report contract
* hit-rate analysis
* false-positive analysis
* conflict usefulness
* half-life logic
* synthetic feedback role
* sandbox boundaries

## Step-by-step checklist

* \[ ] Define learning report schema
* \[ ] Compute lane hit rates
* \[ ] Compute conflict usefulness
* \[ ] Compute false-positive patterns
* \[ ] Compute regime-segmented results
* \[ ] Add half-life tracking
* \[ ] Add look-ahead bias protections
* \[ ] Implement synthetic LLM feedback as heuristic-only
* \[ ] Implement calibration suggestion output
* \[ ] Require explicit approval for non-final-stage changes
* \[ ] Log every recommended change

## Deliverables

* \[ ] learning reports
* \[ ] policy-calibration suggestions
* \[ ] approval workflow for changes

## Proof gate \[PROOF]

* \[ ] System can explain which lanes help or hurt
* \[ ] Learning does not silently mutate policy
* \[ ] Real outcomes outrank synthetic feedback

---

# Phase 13 -- Hardening / Replay / Health

**Mode:** \[PLAN] then \[STEP]

## Purpose

Make the system stable enough for longer paper operation.

## Plan Mode focus

* replay pack
* regression coverage
* outage handling
* health checks
* heartbeat monitoring
* failure artifact policy

## Step-by-step checklist

* \[ ] Build replay cases
* \[ ] Build expected-output checks
* \[ ] Add stale-data alarms
* \[ ] Add malformed-event alarms
* \[ ] Add source outage handling
* \[ ] Add signal packet validation regression tests
* \[ ] Add paper-trade regression tests
* \[ ] Add daily summary validation checks
* \[ ] Implement Alpha/Beta scout heartbeat monitoring
* \[ ] Implement failover event recording
* \[ ] Surface health state in `/fade-health`

Future-only insertion point: multi-machine monitoring and observability expansion belongs to later hardening only; not active during current Phase 2 execution.

## Deliverables

* \[ ] replay/test pack
* \[ ] health artifacts
* \[ ] failover monitoring
* \[ ] stronger operational trust

## Proof gate \[PROOF]

* \[ ] Replay runs are reproducible
* \[ ] Engine failover works in test
* \[ ] Major failure states surface cleanly

---

# Phase 14 -- Autonomous Transition

**Mode:** \[PLAN] then \[STEP]

## Purpose

Transition from fully human-gated paper operation into bounded policy-driven autonomy.

## Plan Mode focus

* Policy Agent / MAB Router
* autonomy thresholds
* Safety Governor interaction
* shadow-lane rules
* Ghost Lane control group
* sandboxed autonomous calibration
* autonomy metrics

## Step-by-step checklist

* \[ ] Deploy MAB Policy Agent for auto-routing
* \[ ] Define route-selection thresholds
* \[ ] Validate routing against historical performance
* \[ ] Activate Virtual / Shadow Lane redundancy
* \[ ] Cap shadow-lane certainty
* \[ ] Implement Ghost Lane registry
* \[ ] Implement autonomous policy calibration sandbox
* \[ ] Ensure Safety Governor overrides routing
* \[ ] Ensure Heartbeat Monitor can fail over Alpha → Beta
* \[ ] Add autonomy metrics to daily summary/dashboard
* \[ ] Force manual fallback when safety gates fire

Future-only insertion point: require runtime pause authority (`tester-can-pause-trader`), assistant-first operator stance, and critic/adversarial gating before any future autonomy escalation; not active now.

## Deliverables

* \[ ] bounded autonomous routing
* \[ ] resilience controls
* \[ ] autonomy metrics
* \[ ] control-group analysis artifacts

## Proof gate \[PROOF]

* \[ ] Policy routing works in bounded mode
* \[ ] Safety Governor wins over autonomy
* \[ ] Shadow lanes do not fake primary confidence
* \[ ] Autonomy is measurable, not vague

---

# Phase 15 -- Live-Readiness Review

**Mode:** \[PLAN] then \[STEP]

## Purpose

Decide whether the system deserves tiny live trading permission.

## Plan Mode focus

* review artifact set
* threshold validation
* safety-governor checks
* kill-switch requirements
* operator override path
* broker-adapter contract

## Step-by-step checklist

* \[ ] Verify paper-trade count threshold
* \[ ] Verify paper duration threshold
* \[ ] Verify regime coverage threshold
* \[ ] Verify expectancy threshold
* \[ ] Verify drawdown threshold
* \[ ] Verify no recent data-quality failures
* \[ ] Verify learning stability
* \[ ] Define live size limits
* \[ ] Define daily live loss limit
* \[ ] Define kill switch
* \[ ] Define manual override path
* \[ ] Create live-readiness review artifact
* \[ ] Explicit pass/fail review

## Deliverables

* \[ ] live-readiness review report
* \[ ] pass/fail recommendation
* \[ ] blockers list

## Proof gate \[PROOF]

* \[ ] Hard gates are actually met
* \[ ] Operator can reject live pilot even if metrics pass

---

# Phase 16 -- Tiny Live Pilot

**Mode:** \[PLAN] then \[STEP]

## Purpose

Run the smallest possible real-money proof.

## Plan Mode focus

* broker adapter
* tiny-size rules
* manual confirmation
* logging
* paper vs live comparison
* abort conditions

## Step-by-step checklist

* \[ ] Connect one broker in safe/sandbox-first manner
* \[ ] Keep max single position tiny
* \[ ] Keep max total exposure tiny
* \[ ] Require explicit operator confirmation
* \[ ] Log every order/fill
* \[ ] Compare every live trade to paper expectation
* \[ ] Review 30-day pilot
* \[ ] Decide continue / revise / kill

## Deliverables

* \[ ] tiny live trade artifacts
* \[ ] live vs paper comparison reports
* \[ ] pilot review report

## Proof gate \[PROOF]

* \[ ] No uncontrolled behavior
* \[ ] Kill switch works
* \[ ] Operator can stop instantly
* \[ ] No scaling until extended review passes

---

# 6. Immediate Start Point

## Start with:

* \[ ] Phase 0
* \[ ] Phase 1
* \[ ] Phase 2
* \[ ] Phase 3
* \[ ] Phase 4
* \[ ] Phase 5
* \[ ] Phase 6
* \[ ] Phase 7

In plain English:

1. lock canon and dependencies
2. define contracts
3. constrain MVP data stack
4. build scanner
5. normalize events
6. score lanes
7. run contra logic
8. fuse and emit real signal packets

## Explicitly do not start with:

* \[ ] paper trading
* \[ ] daily summary
* \[ ] autonomy routing
* \[ ] live readiness
* \[ ] dashboard work beyond signal review

---

# 7. Final Summary

This is the locked master build checklist for THE FADE.

Use it to control:

* phase order
* scope discipline
* dashboard timing
* proof gates
* autonomy timing
* overall implementation direction

The build method is locked:

**Plan Mode at tranche start → Step-by-step execution inside the tranche → proof gate → docs/dashboard update if needed → commit → next tranche**

If the process follows this checklist, the system stays:

* bounded
* coherent
* auditable
* phase-disciplined
* resistant to shiny-object drift

---


