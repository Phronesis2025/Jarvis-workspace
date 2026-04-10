# THE FADE — T128 Scanner lane reopen decision (acceptance criteria)

**Label:** `THE_FADE_GOVERN_SCANNER_LANE_REOPEN_DECISION`  
**Prompt #:** 440  
**Tranche #:** 128  
**Updated:** 2026-04-10T19:00:00+00:00  

**Authority:** **T128** is governance-only. **#441** implementation **PASS** / **FAIL** below.

**Governance:** `THE_FADE_T128_SCANNER_LANE_REOPEN_DECISION_GOVERNANCE.md`  
**Pointer:** `future_modules/the_fade/config/phase3_t128_scanner_lane_reopen_decision_governance.json`

---

## A. Path locked

- **PATH A — KEEP THE LANE PAUSED** is the only authorized outcome of **#440** / **T128**.
- **PATH B — REOPEN THE LANE FOR ONE NARROW NEW QUESTION** is **not** selected until a **future** governance prompt **explicitly** chooses it and **names one** bounded reopening basis.

---

## B. #441 mandatory outcomes (all required for PASS)

1. **Git:** One commit containing **only**:
   - `future_modules/the_fade/docs/THE_FADE_T128_SCANNER_LANE_REOPEN_DECISION_GOVERNANCE.md`
   - `future_modules/the_fade/docs/THE_FADE_T128_SCANNER_LANE_REOPEN_DECISION_ACCEPTANCE_CRITERIA.md`
   - `future_modules/the_fade/config/phase3_t128_scanner_lane_reopen_decision_governance.json`
2. **Push:** Commit pushed to the branch’s remote (default: **`the-fade-phase1-tranche1-foundation`**).
3. **Coherence:** **No** contradiction of **T127** pause or **T126** usefulness conclusions in commit scope or **#441** report.

---

## C. #441 FAIL conditions

- Any **extra** path in the **#441** commit.
- Any **scanner build**, **rollup**, **run folder**, or **T118** change in the **#441** commit.
- Messaging that **reopens** the lane **without** a **separate** future **PATH B** governance prompt.

---

## D. Not in #441

- **PATH B** reopen governance (future prompt).
- **#442–#444** sequences — **out of scope** until **PATH B** is **explicitly** chosen later.

---

## E. After #441

- Scanner lane remains **paused** per **T128 PATH A** until a **future** prompt **explicitly** reopens with **one** bounded question.
