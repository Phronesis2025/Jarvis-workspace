# THE FADE — Phase 2 remaining gate completion plan (LOCKED)

**Prompt #:** 134  
**Phase #:** 2  
**Tranche #:** 34A (plan lock only — no execution in #134)  

**Updated:** 2026-04-01 (Tranche **56**: Prompt **#235** Lane B minimal conflict freshness-consumption truth pass execution)  

**Authority:** This file **does not** change `mvp_lane_approval.json`. Binding approval remains that file only.

---

## Why this exists

Phase 2 work stayed bounded but became **reactive tranche-by-tranche**. This document **locks one ordered sequence** for **remaining** gate work so execution follows a **single plan** (like Phase 1 discipline), not ad-hoc discovery.

---

## Done / locked (do not re-open without governance)

- **Lane B FR full Tranche 21 window** on disk: **22**/**22** successes, **`t30_valid_002`** excluded from full-window tally; governed doc reconciliation (Prompt **#102**).
- **Reliability slice (Lane B, FR window):** honest **22/22** statistic vs count floor; **not** whole-gate approval by itself.
- **Freshness (Lane B):** Tranches **31–32** executed; **Prompt #132** **adopts** **`strict_midnight_utc`**; **10**/**22** **`cannot_classify_honestly`** accepted; **freshness-only** tranches **parked** — `lane_b_phase2_freshness_policy_decision.json`.
- **Freshness policy exploration:** Tranche **33** comparator on disk; **no** alternate policy adopted as primary.
- **Normalization breadth (Lane B, same 22 rows):** Tranche **34** audit on disk — preview truncation documented; regex identity path **solid**; rich object **partial**.
- **Lane B stale/outage & escalation alignment (bounded):** Tranche **35** executed (Prompt **#135**) — `audit_lane_b_stale_outage_escalation_alignment.py` + `tranche35_stale_outage_escalation_audit.*` on disk; standard **#4** still **partial** / not system-closed per artifact verdict.

---

## Still partial (known gaps — not “done”)

- **Lane B freshness:** **10**/**22** **cannot_classify_honestly** under adopted policy — dimension **partial**, not closed.
- **Lane B normalization:** Full API document **not** in stored previews — **breadth partial** per `tranche34_normalization_breadth_audit.*`. Tranche **50** adds a **bounded** normalization viability / silent-drop trace with explicit representative outcomes, but **does not** prove full live normalization breadth or runtime completeness.
- **Lane B stale/outage system behavior:** Not evidenced at **production-equivalent** / **scale** required by approval standard **#4**. Tranche **54** adds bounded explicit policy-row coverage for residual escalation classes `UNDEFINED_DIRECTION_MODEL` and `MISSING_REQUIRED_LANE`, but the dimension remains **partial** because live FR outage evidence and system closure are still not proved.
- **Lane B conflict / context-dominance:** **Partial** — Tranche **47** adds a **bounded** local fixture precedence trace (`tranche47_*`), adopted pre-existing Tranche **52** adds a **bounded** stale-context omission wrapper trace (`tranche52_*`) showing explicit stale-first omission before conflict handling in local cases, and Tranche **56** adds a **bounded** minimal-path truth pass (`tranche56_*`) proving the current `lane_b_real_observation_slice.py conflict` subcommand itself does **not** read freshness-like fields and does **not** stale-omit valid context. Full conflict/runtime closure is still **not** proved.
- **Lanes A, C, E:** **Not** at Lane B evidence depth for MVP promotion.

---

## Not yet justified

- **`approved: true`** or **`approved_mvp_lanes`** non-empty — **not** justified on current live evidence across **all** gate dimensions and **all** in-scope lanes.
- **Phase 3** unlock — **blocked**.
- **Merging** unrelated historical samples into one reliability statistic — **still not** justified (per existing audit discipline).

---

## Remaining gate blockers (what still prevents approval)

Per `MVP_SOURCE_RELIABILITY_AUDIT.md` approval standard — **all** must pass for a candidate lane; **Lane B** is furthest along but **not** closed:

1. **Stale/outage behavior is explicit** (standard **#4**) — **Lane B:** still **partial** after T35 + T45 + T54; not gate-closed at **system** level.
2. **Normalization viability** — **Lane B:** **partial** (Tranche **34** + **Tranche 50** bounded silent-drop trace); full live breadth and full silent-drop guarantees **not** established.
3. **Freshness discipline** — **Lane B:** **policy locked** but outcome **partial** (**10** unresolved rows).
4. **Reliability** — strong for **FR window slice**; **not** a license to ignore other dimensions or other lanes.
5. **No context-only domination** — Lane B / fusion still **partial** even after bounded T47/T52/T56 local traces; T56 clarifies that stale-first omission is wrapper-only relative to the current minimal path. Lane E likewise remains **not** fully proven at gate bar across permutations.
6. **Other MVP lanes (A, C, E)** — **not** evidenced to MVP bar.

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

---

## Do NOT work on yet (unless a new governed prompt explicitly rescopes)

- **Phase 3** scanner / runtime / dashboard.
- **Freshness-only** further tranches (already **parked** per Prompt **#132**).
- **Broker / live execution** / exchange integration.
- **Architecture expansion** (e.g. persist full FR JSON body) **without** a governed prompt that names storage + privacy/retention.
- **Research swarm** or **stock module** scope outside `future_modules/the_fade/`.
- **`mvp_lane_approval.json`** edits without operator evidence + signoff.
- **Ad-hoc** future tranches not listed above — **freeze** unless a new governed prompt explicitly adds them.

---

## File relationships

- Process anchor: `THE_FADE_PROCESS_CHECKLIST.md` (points here).  
- One-screen: `THE_FADE_CONTEXT_ANCHOR.md` (summary bullet).  
- Handoff: `THE_FADE_HANDOFF_BUNDLE_LATEST.md` (path to this file).
