# THE FADE — T101 factual post-run operator review (governance lock)

**Prompt #:** 390  
**Phase #:** 3 — **local pipeline governance** (T101 docs only; no review-surface code in this tranche)  
**Tranche #:** 101  
**Label:** `THE_FADE_PHASE3_T101_GOVERNANCE_LOCK_FACTUAL_POST_RUN_OPERATOR_REVIEW`  

**Updated:** 2026-04-08T14:44:04+00:00  

---

## Purpose

T100 provides a clean local operator run surface and per-run folder artifacts. The next smallest operator-meaningful improvement is one bounded factual review artifact for one completed run folder.

T101 governs exactly one future implementation tranche for one local factual post-run review script. It must read only existing run-folder facts and produce one concise operator-readable review artifact. No AI, no speculative analysis, no scanner claims.

T101 does not implement the review surface.

**Companion:** `THE_FADE_T101_FACTUAL_POST_RUN_OPERATOR_REVIEW_ACCEPTANCE_CRITERIA.md`  
**Machine-readable note:** `phase2_mvp_approval_scope_decision.json` -> `post_t101_factual_post_run_operator_review_governance`

---

## 1) Exact governed slice

One future implementation tranche may add one local post-run review script only that:

- reads exactly one existing run folder under  
  `future_modules/the_fade/outputs/local_happy_path_runs/run_<YYYYMMDDTHHMMSSZ>/`
- reads only:
  - `run_summary.json`
  - copied request JSON in that run folder
  - copied result JSON in that run folder
- writes exactly one operator-readable markdown review artifact in that same run folder.

Local-only, factual-only, bounded extraction/counts only.

---

## 2) Exact future artifact allowance

Allowed in the future implementation tranche:

1. One script only at fixed path (section 4).
2. Optional small README only in same directory.
3. Optional one tiny helper `.py` only in same directory if strictly necessary and explicitly named.
4. One review artifact only at fixed name (section 4), one per processed run folder.

Forbidden:

- second entrypoint,
- framework buildout,
- extra reporting surfaces outside this slice.

---

## 3) What the review surface may do

The future review script may:

- open one run folder supplied by path/basename,
- read the three governed files only (`run_summary.json`, copied request, copied result),
- extract factual fields already on disk,
- compute simple transparent derived counts only,
- write one concise markdown review in the same run folder,
- print local PASS/FAIL and output path.

No network, no AI/LLM, no inference-heavy behavior.

---

## 4) Fixed implementation path and artifact name

Implementation path is fixed to:

`future_modules/the_fade/review/local_run/build_operator_review_from_run_folder.py`

Review artifact filename is fixed to:

`operator_review.md`

---

## 5) Allowed review artifact content (bounded)

Allowed content is factual and bounded to on-disk fields, including:

- run id / folder name,
- run status from `run_summary.json`,
- request path and result path,
- request id,
- contract version,
- source reference fields already on disk (`universe_source_ref`, `scan_policy_version`, `candidate_source_packet_ref`),
- `scanner_status` from result JSON,
- count of `candidate_outputs`,
- count of `row_status == deferred`,
- warnings already on disk,
- timestamps already on disk,
- explicit statement: this is factual post-run review, not scanner decision output.

No recommendations, no ranking, no trading advice.

---

## 6) Explicitly forbidden in the future implementation tranche

- AI/LLM summarization,
- recommendations or trade ideas,
- ranking/scoring/selection logic,
- new data fetches / network calls,
- provider adapters/clients,
- dashboard/UI,
- runtime orchestration,
- scheduling/jobs/workers,
- lane reopen,
- evidence collection,
- registry/approval edits,
- multi-slice bundling,
- hidden intelligence creep,
- broad reporting framework buildup.

---

## 7) Anti-drift rules

1. One implementation slice only.  
2. One script only at fixed path.  
3. One review artifact only at fixed name.  
4. One run folder at a time.  
5. No "while we're here" extras.  
6. No widening into intelligence, dashboards, or orchestration.

---

## 8) Non-claims

- T101 does not implement the review script.
- T101 does not authorize scanner/runtime/provider/dashboard expansion.
- T101 does not authorize production orchestration or approval/lane changes.
