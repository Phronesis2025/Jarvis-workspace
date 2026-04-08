# THE FADE — T99 clean local operator run surface (governance lock)

**Prompt #:** 385  
**Phase #:** 3 — **local pipeline governance** (T99 docs only; no operator-surface code in this tranche)  
**Tranche #:** 99  
**Label:** `THE_FADE_PHASE3_T99_GOVERNANCE_LOCK_CLEAN_LOCAL_OPERATOR_RUN_SURFACE`  

**Updated:** 2026-04-08T12:28:27+00:00  

---

## Purpose

T98 delivered a bounded local happy-path runner at `future_modules/the_fade/runner/local_happy_path/run_local_end_to_end_happy_path.py`. Operators can run it, but repeat local runs can leave root packet directories cluttered and force manual hunting for "which request/result came from this run."

**T99** governs exactly one future implementation tranche to add one narrow local operator-facing run surface that wraps T98 and makes each run easier to locate and read, without adding any scanner logic or platform behavior.

**T99 does not implement the operator surface.**

**Companion:** `THE_FADE_T99_CLEAN_LOCAL_OPERATOR_RUN_SURFACE_ACCEPTANCE_CRITERIA.md`  
**Machine-readable note:** `phase2_mvp_approval_scope_decision.json` -> `post_t99_clean_local_operator_run_surface_governance`

---

## 1) Exact governed slice

One future implementation tranche may add:

- one local operator entrypoint that invokes the existing T98 runner (wrapper only),
- one bounded run-output organization convention,
- one concise per-run summary convention.

No new pipeline intelligence, no scanner expansion, no runtime platform.

---

## 2) Exact future artifact allowance

Allowed in the future implementation tranche:

1. **One operator entrypoint script only** at the fixed path in section 5.
2. **Optional README only** in the same directory for usage/constraints.
3. **Optional one tiny helper `.py` only** in the same directory if strictly necessary and explicitly named in README.
4. **One concise run summary artifact format only** (JSON), bounded to one file per run under the governed run-output root.

Forbidden:

- second entrypoint,
- framework buildout,
- package sprawl outside the one operator directory.

---

## 3) What the operator surface may do

The future operator entrypoint may:

- call T98 runner `future_modules/the_fade/runner/local_happy_path/run_local_end_to_end_happy_path.py`,
- create one run directory per invocation using a bounded run id (`YYYYMMDDTHHMMSSZ`),
- copy exactly the run-produced request/result JSON artifacts into that run directory for clean lookup,
- write one concise run summary JSON in that run directory (run id, timestamps, status, source paths, copied paths),
- print a concise console summary pointing to the run directory and summary file,
- exit non-zero if wrapped run fails or required artifacts cannot be identified.

It must remain local-only.

---

## 4) Explicitly forbidden in the future implementation tranche

- scanner execution logic,
- ranking/scoring/selection logic,
- provider adapters/clients,
- dashboard/UI,
- scheduling/jobs/workers,
- orchestration platform buildout,
- multi-source expansion,
- lane reopen,
- evidence collection,
- registry/approval edits,
- multi-slice bundling,
- hidden intelligence creep,
- broad framework/setup churn,
- replacing T98 runner internal pipeline behavior (must wrap, not replace).

---

## 5) Fixed implementation path (singular)

Future operator entrypoint path is fixed to:

`future_modules/the_fade/operator/local_run/run_clean_local_happy_path.py`

No second operator surface is authorized in this slice.

---

## 6) Cleanliness / output organization rule (explicit decision)

T99 chooses a tightly bounded **per-run folder + one manifest** convention:

- run root: `future_modules/the_fade/outputs/local_happy_path_runs/`
- each invocation creates exactly one run folder:
  - `run_<YYYYMMDDTHHMMSSZ>/`
- each run folder may contain only:
  - copied request packet JSON from that run,
  - copied result packet JSON from that run,
  - one summary JSON named `run_summary.json`.

This rule exists so each run starts clean from the operator perspective and run artifacts are discoverable without building a runtime platform.

---

## 7) Anti-drift rules

1. One implementation slice only.  
2. One operator entrypoint path only.  
3. One clean output/summary convention only (section 6).  
4. No "while we're here" additions.  
5. No widening into platform/orchestration work.  
6. Wrap T98 runner only; do not replace core flow logic.

---

## 8) Non-claims

- T99 does not implement operator run-surface code.
- T99 does not authorize scanner/runtime/provider/dashboard expansion.
- T99 does not authorize production orchestration.
