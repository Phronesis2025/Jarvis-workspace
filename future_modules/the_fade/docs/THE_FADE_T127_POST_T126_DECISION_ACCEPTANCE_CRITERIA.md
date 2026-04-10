# THE FADE — T127 Post-T126 decision lock (acceptance criteria)

**Label:** `THE_FADE_GOVERN_POST_T126_DECISION_LOCK`  
**Prompt #:** 438  
**Tranche #:** 127  
**Updated:** 2026-04-10T18:30:00+00:00  

**Authority:** **T127** is governance-only. **#439** implementation **PASS** / **FAIL** below.

**Governance:** `THE_FADE_T127_POST_T126_DECISION_GOVERNANCE.md`  
**Pointer:** `future_modules/the_fade/config/phase3_t127_post_t126_decision_governance.json`

---

## A. Path locked

- **PATH B — STOP SCANNER EXPANSION FOR NOW** is the only authorized strategic direction from **T127**.
- **PATH A — CONTINUE DIFFERENTIATED EVIDENCE** is **not** authorized until a **future** governance prompt **explicitly** reopens evidence gathering.

---

## B. #439 mandatory outcomes (all required for PASS)

1. **Git:** One commit on the governed THE FADE branch (default: **`the-fade-phase1-tranche1-foundation`**) containing **only** these paths (no other paths in the same commit):
   - `future_modules/the_fade/docs/THE_FADE_T127_POST_T126_DECISION_GOVERNANCE.md`
   - `future_modules/the_fade/docs/THE_FADE_T127_POST_T126_DECISION_ACCEPTANCE_CRITERIA.md`
   - `future_modules/the_fade/config/phase3_t127_post_t126_decision_governance.json`
2. **Push:** That commit is **pushed** to the branch’s **remote** tracking branch.
3. **Coherence:** Commit message and **#439** report **must not** contradict **T126** (**PARTIALLY USEFUL**, **no repair**, **no expansion now**, **PATH B pause**).

---

## C. #439 FAIL conditions

- Any **additional** file staged in the **#439** commit beyond §B.1.
- Any **new** `run_*` folder, **rollup** refresh, or **T118** change **in the #439 commit**.
- Contradictory messaging (e.g. “pause” plus **mandated** next FR run in same tranche).

---

## D. Not in #439

- Locking **T126** decision doc (**optional** separate prompt; **not** required by **T127**).
- Repair, expansion, or PATH A evidence builds.

---

## E. After #439

- **No** program-mandated scanner/evidence work until **re-entry** per **`THE_FADE_T127_POST_T126_DECISION_GOVERNANCE.md` §8**.
