# THE FADE — Phase 3 implementation boundary (T83)

**Prompt #:** 345  
**Tranche #:** 83  
**Label:** `THE_FADE_PHASE3_ENTRY_T83_FOUNDATION_PLANNING_LOCK`  

**Updated:** 2026-04-06T23:45:00+00:00  

---

## Role of this document

This file is the **implementation boundary** companion to `THE_FADE_PHASE3_ENTRY_PLAN_T83.md`. It states **what counts as forbidden Phase 3 implementation** while Phase 3 **entry** is still **planning-only**, and how the **first slice** stays **singular** when code is eventually allowed.

---

## A. Planning vs implementation (hard line)

| Activity | T83 classification |
|----------|-------------------|
| Markdown / checklist updates under governed prompts | **Planning / governance** (when prompt allows) |
| New Python/JS/TS/other **executable** logic for scanner, runtime, dashboard, or live pipelines | **Implementation — forbidden** without later governance |
| New scripts that **collect** lane evidence or **run** scheduled observes | **Implementation + evidence — forbidden** |
| Config that **wires** providers, secrets, or production endpoints | **Implementation — forbidden** |
| **Static** schema/type artifacts **only**, as named in entry plan §2, **after** a future implementation tranche | **Future slice scope** (not T83) |

**T83 adds no implementation artifacts.**

---

## B. Blocked surfaces (unchanged until implementation tranche)

The following remain **out of bounds** for any work **claimed** as Phase 3 **without** a later explicit **Phase 3 implementation** governance tranche:

- **Runtime execution** — workers, cron-driven jobs, long-running services for THE FADE Phase 3.
- **Scanner implementation** — code paths that enumerate “universe” or orchestrate real data acquisition for Phase 3.
- **Dashboard implementation** — UI or API whose purpose is operator-facing Phase 3 monitoring/control.
- **Provider integration** — replacing `TBD_*` placeholders with live integrations.
- **Lane reopen** — any relaxation of `lane_posture_policy` without new charter/governance.
- **Productionization** — deployment manifests, prod config, or maturity claims tied to live rollout.

---

## C. First implementation slice boundary (reference)

When authorized, **only** the **single** candidate in `THE_FADE_PHASE3_ENTRY_PLAN_T83.md` §2 applies as the **default** first slice: **static universe-scanner I/O contract** under `future_modules/the_fade/`, **no** network, **no** loop, **no** dashboard, **no** providers, **no** registry/lane edits.

**Widening** that slice requires a **new** governed tranche; **bundling** contract + runtime + dashboard in one tranche is **not** permitted as “first slice.”

---

## D. Relationship to scoped MVP approval

- **`mvp_lane_approval.json` `approved: true`** = **scoped MVP** for named lanes (see `t80_scoped_mvp_approval_decision.json`).
- **Does not imply:** Phase 3 build OK, scanner OK, dashboard OK, or lane reopen.

**Implementation go-ahead** requires **additional** explicit governance (see entry plan §4).

---

## E. Anti-drift (implementation angle)

- Treat **any** PR/commit that adds **executable** Phase 3 paths **without** the implementation governance tranche as **scope violation**.
- Treat **“small”** scanner/runtime/dashboard additions as **implementation**, not planning.
- **One surface per first slice** — no multi-surface stealth scope.
