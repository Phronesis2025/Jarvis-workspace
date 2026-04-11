# THE FADE — T129 Lane reopen operator-actionability (acceptance criteria)

**Label:** `THE_FADE_GOVERN_LANE_REOPEN_FOR_OPERATOR_ACTIONABILITY_QUESTION`  
**Prompt #:** 442  
**Tranche #:** 129  
**Updated:** 2026-04-10T19:30:00+00:00  

**Authority:** **T129** is governance-only. **#443** / **#444** / **#445** / **#446** **PASS** / **FAIL** per section below.

**Governance:** `THE_FADE_T129_LANE_REOPEN_OPERATOR_ACTIONABILITY_GOVERNANCE.md`  
**Pointer:** `future_modules/the_fade/config/phase3_t129_lane_reopen_operator_actionability_governance.json`

---

## A. Path locked

- **PATH B — REOPEN FOR ONE BOUNDED QUESTION** is authorized **only** for: **Lane B Federal Register operator-actionability contract** (what to surface, what not, why — **markdown documentation**).
- **PATH A — KEEP THE LANE PAUSED** is **not** selected for **#442** — **scanner mechanics work** remains **paused** except this **documented** exception.

---

## B. #443 mandatory outcomes (all required for PASS)

1. **Git:** One commit containing **only**:
   - `future_modules/the_fade/docs/THE_FADE_T129_LANE_REOPEN_OPERATOR_ACTIONABILITY_GOVERNANCE.md`
   - `future_modules/the_fade/docs/THE_FADE_T129_LANE_REOPEN_OPERATOR_ACTIONABILITY_ACCEPTANCE_CRITERIA.md`
   - `future_modules/the_fade/config/phase3_t129_lane_reopen_operator_actionability_governance.json`
2. **Push:** That commit is pushed to the governed THE FADE branch.

---

## C. #444 (forward reference — not judged by T129 file alone)

- **#444** must **fix** the **exact** output paths and **outline** for **#445**; **FAIL** if **#444** adds code or **mandates** FR runs.

---

## D. #445 mandatory outcomes (when executed)

- **At least one** governed markdown artifact (paths **from #444**) that **explicitly** covers:
  - **Operator-actionable** FR record patterns for **Lane B** (positive criteria).
  - **Not worth surfacing** (negative criteria) with **plain-language** **why**.
  - **Explicit** note how this **relates** to **T117/T118 allowlist** (**descriptive** comparison, **no** rule edit).
- **No** `.py` changes, **no** new `run_*`, **no** T118 edits.

---

## E. #446

- **Git lock** of **only** **#445** deliverables per **#446** prompt.

---

## F. FAIL conditions (cross-cutting)

- **#443** commit includes **any** path outside §B.1.
- **#445** ships **scanner code**, **repair**, or **second rule** under the **actionability** label.
- Contradiction: claiming **general** lane reopen **beyond** the **single** documentation basis.

---

## G. Non-claims

Acceptance does **not** require **mvp_lane** edits or **registry** updates.
