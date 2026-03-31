# THE FADE — Phase 2 remaining gate completion plan (LOCKED)

**Prompt #:** 134  
**Phase #:** 2  
**Tranche #:** 34A (plan lock only — no execution in #134)  

**Updated:** 2026-03-31  

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
- **Lane B normalization:** Full API document **not** in stored previews — **breadth partial** per `tranche34_normalization_breadth_audit.*`.
- **Lane B stale/outage system behavior:** Not evidenced at **production-equivalent** / **scale** required by approval standard **#4** (collector + harness slices only).
- **Lane B conflict / context-dominance:** **Partial** bounded runs in log — **not** permutation-complete.
- **Lanes A, C, E:** **Not** at Lane B evidence depth for MVP promotion.

---

## Not yet justified

- **`approved: true`** or **`approved_mvp_lanes`** non-empty — **not** justified on current live evidence across **all** gate dimensions and **all** in-scope lanes.
- **Phase 3** unlock — **blocked**.
- **Merging** unrelated historical samples into one reliability statistic — **still not** justified (per existing audit discipline).

---

## Remaining gate blockers (what still prevents approval)

Per `MVP_SOURCE_RELIABILITY_AUDIT.md` approval standard — **all** must pass for a candidate lane; **Lane B** is furthest along but **not** closed:

1. **Stale/outage behavior is explicit** (standard **#4**) — **Lane B:** not gate-closed at **system** level.
2. **Normalization viability** — **Lane B:** **partial** (Tranche **34**); full silent-drop guarantees **not** established.
3. **Freshness discipline** — **Lane B:** **policy locked** but outcome **partial** (**10** unresolved rows).
4. **Reliability** — strong for **FR window slice**; **not** a license to ignore other dimensions or other lanes.
5. **No context-only domination** — **Lane E** / fusion — **not** fully proven at gate bar across permutations.
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
