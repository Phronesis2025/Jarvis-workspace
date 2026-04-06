# Lane B — Primary eligibility charter (Tranche 75)

**Tranche:** 75  
**Rollout (canonical):** Prompt **#327**  
**Label:** `THE_FADE_PHASE2_T75_LANE_B_PRIMARY_ELIGIBILITY_CHARTER`  
**Updated:** 2026-04-06T23:00:00+00:00

**Repair note (non-canonical identity):** The objective below was **repaired** after initial charter authoring so the next bounded step matches **`primary_lane_rule`** leverage for the scoped MVP path. The repair was applied under Prompt **#328** (charter repair only); **canonical T75 identity remains Prompt #327 / Tranche #75** as above.

This file **does not** grant MVP approval, **does not** change `approved` or `approved_mvp_lanes` in `mvp_lane_approval.json`, and **does not** unblock Phase 3.

**Binding scope decision:** `future_modules/the_fade/config/phase2_mvp_approval_scope_decision.json` — **`primary_lane_rule`** for **`lane_b_official_disclosure`**.

---

## 1. Goal (what this charter optimizes for)

- **Goal:** Reduce the gap to **`primary_lane_eligibility_met: true`** under **`phase2_mvp_approval_scope_decision.json`** — i.e. move Lane B toward satisfying **`primary_lane_rule`** (per-dimension evidence **or** explicit written governance treatment for each residual gap on the **scoped MVP** path).
- **Non-goal:** “Finish Lane B” or accept **all** six dimensions in one tranche. This charter authorizes **one** sharply bounded next step only.

---

## 2. Exact current blocker (as of post–T74)

- **`primary_lane_eligibility_met`** remains **`false`** per **`primary_lane_rule.as_of_t74_on_disk_assessment`** in `phase2_mvp_approval_scope_decision.json`.
- **Reason:** **`mvp_lane_evidence_registry.json`** shows **`lane_b_official_disclosure.dimension_evidence_status`** **all `partial`** — residual gaps remain **partial**, and there is **not yet** a **written per-dimension governance treatment** strong enough (charter clause, decision JSON, or evidence log) to **accept** named residual gaps for scoped MVP approval under **`primary_lane_rule`** requirement **(b)**.

---

## 3. Objective class (exactly one — repaired)

**Removed (no longer in effect for T75 next tranche):** ~~(A) Stored-slice **`stale_outage_behavior`** evidence audit~~ — that path was strategically **too weak**: it would likely **re-document known limits** (success-only slice cannot show negative-path outage examples) without materially advancing **`primary_lane_eligibility_met`**.

**Chosen (single objective): (B) One bounded governance-acceptance pack for one named subset of Lane B residual gaps**

- The subset is **explicit** and **single-reading** — **four** dimensions only:
  - **`freshness`**
  - **`normalization_viability`**
  - **`conflict_handling`**
  - **`context_dominance_risk`**
- These dimensions are **already evidenced enough** (bounded audits, policies, stored-slice truth passes on disk — see `MVP_LANE_EVIDENCE_LOG.md` and prior tranches) to be **candidates** for **scoped MVP written acceptance** **without** pretending they are **fully closed** at production scale.
- **`stale_outage_behavior` is explicitly OUT OF SCOPE for this charter and for the next tranche authorized here.** It is **not** settled, accepted, or closed by T75 or by the acceptance pack described below. It remains for **future** governed evidence or acceptance work.

**Not chosen here:** Accepting **every** residual gap across **all** six dimensions at once — that would be **mush** and **overreach** (fails sharp bounds).

---

## 4. Why this objective beats the next alternatives

1. **Stale/outage stored-slice audit (removed objective):** **Loses** because the FR full-window slice is **22/22 success-only**; a repeat audit **likely only reproves** that the slice **cannot** exhibit negative-path outage behavior — **little new leverage** on **`primary_lane_eligibility_met`** versus a **written** scoped acceptance where other dimensions already have **substantial** bounded documentation.
2. **Freshness-only follow-on work:** **Loses** because freshness is already **policy-locked** (`lane_b_phase2_freshness_policy_decision.json`); **freshness-only** work is **too narrow** to carry **`primary_lane_rule`** forward compared to a **four-dimension acceptance pack** that matches where the evidence base is already densest **after** reliability.
3. **Full multi-gap acceptance of every Lane B residual at once:** **Loses** because it **collapses** into vague signoff — this charter **limits** acceptance to **four** named dimensions and **explicitly excludes** **`stale_outage_behavior`** from this pack.

---

## 5. Next bounded tranche target (governance only)

**One governance-acceptance pack only** — **no** live collection, **no** new execution code, **no** multi-lane work, **no** approval flip, **no** Phase 3 work.

### 5.1 Exact intended outputs (next tranche — not the T75 charter repair)

Both files must cite **T75** and **Prompt #327** and list the **same four dimensions**; both must state **what is accepted**, **what is NOT accepted**, and that **`stale_outage_behavior`** remains **outside** this pack.

| Artifact | Path |
|----------|------|
| Machine-readable acceptance pack | `future_modules/the_fade/config/lane_b_t75_scoped_mvp_governance_acceptance_pack.json` |
| Human-readable acceptance memo | `future_modules/the_fade/docs/LANE_B_T75_SCOPED_MVP_GOVERNANCE_ACCEPTANCE_MEMO.md` |

**Content requirements (both files):**

- **What is explicitly accepted** for the **scoped MVP path** — per dimension in the subset, **only** to the extent supported by **existing on-disk evidence** (logs, audits, policy JSONs) — with **no** claim of full production closure.
- **What is NOT accepted** — e.g. full runtime scale, **stale_outage_behavior** system closure, **reliability** beyond documented slices, **multi-lane** fusion, Phase 3.
- **Explicit statement:** **`stale_outage_behavior`** is **not** covered, **not** accepted, and **not** settled by this pack.

**May touch (next tranche only):**

- The two paths above; **cross-references** to existing evidence in `MVP_LANE_EVIDENCE_LOG.md`, `phase2_mvp_approval_scope_decision.json`, and prior audit outputs — **read-only** citation, **no** new scripts.

**Explicit non-touch:**

- **`mvp_lane_approval.json`** (no value edits).
- **Lanes A / C / E** — **no** new live evidence, **no** charter reopen.
- **Phase 3** — any runtime/scanner/dashboard work.
- **`stale_outage_behavior`** — **no** new audit or acceptance in this pack.

---

## 6. Stop line

### 6.1 T75 charter (including repair)

- **Success:** This file reflects **only** objective **(B)** and **one** named four-dimension subset; **no** stale/outage objective remains active in this charter.
- **Repair note** appears in prose only (§header); **Prompt #328** is **not** a canonical tranche identity.

### 6.2 Next bounded tranche (governance acceptance pack)

- **Success:** **Both** `lane_b_t75_scoped_mvp_governance_acceptance_pack.json` **and** `LANE_B_T75_SCOPED_MVP_GOVERNANCE_ACCEPTANCE_MEMO.md` exist on disk; they are **bounded** to the **four** dimensions; **no** lane reopen; **no** `mvp_lane_approval.json` flip; **no** registry dimension row rewrite **unless** a **future** tranche explicitly updates registry after operator review.
- **Honest failure:** The next tranche **cannot** justify written acceptance for **one or more** of the four named dimensions **without overclaiming** — must **say so explicitly** in both files and leave **`primary_lane_eligibility_met`** **false** until further work.

### 6.3 Out of scope

- Any **new** live HTTPS evidence, any **support-lane** work, any **`mvp_lane_approval.json`** flip, any **Phase 3** work, any **`stale_outage_behavior`** settlement in this pack.

---

## 7. Preserve existing posture rules

- **Lane A:** **Stopped** — `LANE_A_PHASE2_EVIDENCE_CHARTER_T64.md` §9; **no** new Lane A live evidence unless a **new** Lane A charter.
- **Lane C:** **Stopped** — `LANE_C_PHASE2_EVIDENCE_CHARTER_T66.md` §11; **no** new Lane C live evidence unless a **new** Lane C charter.
- **Lane E:** **Stopped** — `LANE_E_PHASE2_EVIDENCE_CHARTER_T69.md` §12; **no** new Lane E live evidence unless a **new** Lane E charter.
- **Lane B:** This charter is the **only** explicit authorization for the **next bounded tranche class** targeting **`primary_lane_rule`** — **one** objective (**governance-acceptance pack** for the **four** named dimensions **only**), Lane B **only**.

---

## 8. Registry / log expectation (after next governance tranche — not T75 repair)

- **`mvp_lane_evidence_registry.json`:** May be updated **only** in a **future** tranche if the operator aligns registry **`dimension_evidence_status`** / notes with the acceptance pack — **T75 repair does not** rewrite lane or dimension rows.
- **`MVP_LANE_EVIDENCE_LOG.md`:** Next tranche records **governance** artifact pointers and honest limitations.
