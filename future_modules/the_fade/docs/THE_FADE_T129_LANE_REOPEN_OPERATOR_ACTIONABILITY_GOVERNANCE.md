# THE FADE — T129 Lane reopen: operator-actionability question (governance)

**Label:** `THE_FADE_GOVERN_LANE_REOPEN_FOR_OPERATOR_ACTIONABILITY_QUESTION`  
**Prompt #:** 442  
**Tranche #:** 129  
**Updated:** 2026-04-10T19:30:00+00:00  

**Authority:** Governance and boundary only. **No** executable scanner implementation in **T129**. **Does not** revoke **T128**’s prior pause — it **exercises** **T128** §8 **re-entry** for **one** **named** bounded question only.

**Companion:** `THE_FADE_T129_LANE_REOPEN_OPERATOR_ACTIONABILITY_ACCEPTANCE_CRITERIA.md`  
**Pointer:** `future_modules/the_fade/config/phase3_t129_lane_reopen_operator_actionability_governance.json`

---

## 1. Anchors: T126, T127, T128 (no contradiction)

**Already known:** First real scanner rule is **mechanically credible** on locked evidence; **PARTIALLY USEFUL**; **repair** and **expansion** **not** justified on **mechanics alone**; **T127/T128** **paused** optional scanner churn **until** a **future** prompt **reopens** with a **single** bounded basis.

**Still unknown:** What **Lane B** should treat as **operator-actionable** vs **ignore** for **Federal Register** records **in prose** (intent contract), independent of whether T118’s allowlist **matches** that intent long-term.

**Bottleneck thesis:** **Undefined operator actionability** is a **documentation / lane-intent** gap — **not** solved by **another FR pull** or **a second rule** **before** the contract exists.

---

## 2. Path chosen: **PATH B — REOPEN FOR ONE BOUNDED QUESTION**

**PATH A — KEEP THE LANE PAUSED is not selected** for **this** question in **T129**.

**Single reopen basis (only):** **Lane B — Federal Register operator-actionability contract:** what records are **worth surfacing** to an operator, what are **not**, and **why** (criteria in **governed markdown only** in the build tranche).

---

## 3. Why PATH B (least steps, not busywork)

1. **Targeted:** One **written** contract closes the **intent** gap T126 flagged (partial usefulness, Presidential/materiality **unsettled**) **without** T118 edits or new runs.
2. **Not expansion:** The contract is **not** a second rule, **not** ranking/scoring, **not** engine growth — it **informs** future decisions **whether** repair or expansion is **ever** justified.
3. **PATH A** would **refuse** to **name** actionability **while** admitting it is the **likely** leverage — **extra** ambiguity **without** **fewer** downstream prompts.

---

## 4. Exact allowed next-slice scope

| Tranche | Allow |
|---------|--------|
| **#443** | **Git lock only** — commit/push **only** the **T129** governance package files listed in acceptance criteria. |
| **#444** | **Governance only** — **one** narrow doc (path fixed in **#444** prompt) that defines the **exact** markdown files / section outline for the **#445** contract package (**no** implementation in **#444**). |
| **#445** | **Build** — **at most** the **governed markdown contract package** (and **only** paths **#444** lists): definitions, **surfacing / non-surfacing** rules for Lane B FR context, **explicit** boundary vs T117 allowlist (**descriptive**, not changing T117), **no** Python, **no** new `run_*`, **no** T118 change. |

---

## 5. Exact forbidden scope

- **Scanner expansion:** second rule, selection/ranking engine, dashboard, provider, runtime, LLM.
- **First-rule repair** or **T118** / **T117** **code or governance-text** edits **inside** **#445** (contract may **reference** T117 **read-only**).
- **Mandatory** new FR **evidence** runs, **rollup** refresh **as a program requirement** of **#445**.
- **`mvp_lane_approval.json`**, **`mvp_lane_evidence_registry.json`** edits.
- **Smuggling:** framing the contract as **permission** to **silently** expand the scanner **without** a **later** explicit build/lock tranche.

---

## 6. What counts as PASS

- **#443:** T129 three-file package **locked** per acceptance criteria.
- **#444 / #445 / #446:** Per those prompts; **#445** **PASS** requires **deliverable markdown** that answers **only** the operator-actionability question **without** forbidden scope.

---

## 7. What does **not** get built yet (in **T129** / **#443**)

- Any **code**, **T118** change, **second rule**, **FR run**, or **rollup** — **not** part of **#443**; **#445** is **docs-only** per §4.

---

## 8. Relation to T128

**T128 PATH A** remains the **default pause** for **unspecified** scanner work. **T129 PATH B** **narrows** an **exception**: **lane may proceed** **only** on **operator-actionability documentation** until **#446** locks it — **not** a **general** lane reopen.

---

## 9. Non-claims

**T129** does **not** assert the contract **matches** current T118 behavior, does **not** **authorize** repair, and does **not** **resume** evidence gathering — **only** **documentation** of **what “actionable” means** for Lane B FR context.
