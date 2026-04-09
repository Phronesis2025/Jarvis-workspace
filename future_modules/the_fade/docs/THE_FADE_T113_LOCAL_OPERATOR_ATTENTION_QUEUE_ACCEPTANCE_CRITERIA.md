# THE FADE T113 — Local Operator Attention Queue Acceptance Criteria

**Prompt #:** 409  
**Phase #:** 3 — local pipeline implementation governance lock  
**Tranche #:** 113  
**Label:** THE_FADE_PHASE3_T113_GOVERNANCE_LOCK_LOCAL_OPERATOR_ATTENTION_QUEUE  
**Status:** PASS / FAIL / SCOPE-VIOLATION CRITERIA FOR THE FUTURE T113 BUILD TRANCHE  
**Updated:** 2026-04-09T00:25:00+00:00

---

## 1) Scope of this acceptance file

This file defines acceptance for the single future implementation tranche authorized by T113 governance.

T113 governance tranche itself is doc-lock only and does not execute this build.

---

## 2) Required future implementation artifacts

Required in the future build tranche:

1. `future_modules/the_fade/review/local_run/build_operator_attention_queue.py`
2. `future_modules/the_fade/outputs/local_happy_path_runs/operator_attention_queue.json`

Optional only if strictly necessary:

- `future_modules/the_fade/review/local_run/README_operator_attention_queue.md`
- One tiny helper `.py` in the same directory, explicitly named

Anything else is out of scope unless separately governed.

---

## 3) Required future behavior

The future script must:

1. Scan only run folders under:
   `future_modules/the_fade/outputs/local_happy_path_runs/`
2. Read only bounded artifacts:
   - `operator_attention_signal.json`
   - optional `operator_review_gate.json` only when strictly necessary
3. Include only runs with valid parseable `operator_attention_signal.json`
4. Build purely mechanical queue rows from factual fields on disk
5. Write exactly one queue artifact:
   `operator_attention_queue.json` at the fixed root path
6. Perform transparent ordering/filtering only (no fuzzy logic)
7. Include required fixed non-scanner and non-trading-signal statements

---

## 4) Allowed queue content

Allowed queue JSON content is bounded to:

- `generated_at_utc`
- `queue_schema_version`
- `runs_root_relative`
- `counts`
- `runs` rows with factual fields:
  - `run_id`
  - `operator_attention_status`
  - `operator_attention_reasons`
  - `request_id`
  - `source_name`
  - `review_gate_status`
  - `candidate_outputs_count`
  - `deferred_count`
  - `results_count` only if already present in `operator_attention_signal.json`
  - relative path to `operator_attention_signal.json`
  - relative path to run folder
- fixed non-scanner statement
- fixed non-trading-signal statement

---

## 5) Allowed ordering/filtering

Allowed mechanical rules:

- Include only runs with valid `operator_attention_signal.json`
- Stable ordering by run folder timestamp descending
- Optional status partition/group derived only from `operator_attention_status`
- Optional counts by attention status

Not allowed:

- Heuristic ranking
- Scores
- Qualitative prioritization labels
- Fuzzy criteria

---

## 6) Forbidden in the future build tranche

- AI/LLM summarization
- Recommendations/trade ideas
- Ranking/scoring/selection logic
- New network calls/data fetches
- Provider/runtime/dashboard/orchestration code
- Scheduler/job/worker code
- Scanner execution claims or scanner logic
- Pipeline replacement or expansion
- Lane reopen
- Evidence collection additions
- `mvp_lane_approval.json` edits
- `mvp_lane_evidence_registry.json` edits
- Additional entrypoints/surfaces beyond authorized ones

---

## 7) PASS criteria (future build tranche)

PASS requires all true:

1. Exactly one authorized script exists at the fixed path.
2. Exactly one queue artifact is produced at the fixed path/name.
3. Read boundary is respected (local run root + allowed artifacts only).
4. Queue rows are factual and mechanically derived only.
5. Ordering/filtering is transparent and mechanical only.
6. No network/API calls.
7. No AI/LLM behavior.
8. No scanner claims.
9. No provider/dashboard/runtime/orchestration additions.
10. No extra unauthorized artifacts/surfaces.

---

## 8) FAIL criteria (future build tranche)

FAIL if any required artifact is missing, if write path/name is wrong, if parsing fails without handled bounded behavior, or if the artifact shape violates required bounded content.

---

## 9) Scope-violation criteria (future build tranche)

Scope violation if any of the following occurs:

- Reads outside allowed local run-folder boundaries
- New network fetches
- AI/LLM summarization
- Ranking/scoring/selection logic
- Runtime/provider/dashboard buildout
- Scanner or decision-engine claims
- Extra entrypoints/framework surfaces
- Registry/approval edits
- Lane reopen/evidence collection work

