# THE FADE T113 — Local Operator Attention Queue Governance

**Prompt #:** 409  
**Phase #:** 3 — local pipeline implementation governance lock  
**Tranche #:** 113  
**Label:** THE_FADE_PHASE3_T113_GOVERNANCE_LOCK_LOCAL_OPERATOR_ATTENTION_QUEUE  
**Status:** GOVERNANCE ONLY (NO EXECUTION CODE IN T113)  
**Updated:** 2026-04-09T00:25:00+00:00

---

## 1) Purpose and boundary

This tranche governs exactly one future implementation slice that may build a local operator attention queue from already-existing per-run attention artifacts.

This is a mechanical queue surface only. It is not a scanner, not a ranking engine, not a decision engine, and not a trading signal layer.

T113 itself adds governance/doc artifacts only.

---

## 2) Exactly one future implementation slice authorized

Exactly one later implementation tranche is authorized to create:

1. One script only:
   `future_modules/the_fade/review/local_run/build_operator_attention_queue.py`
2. One queue artifact only:
   `future_modules/the_fade/outputs/local_happy_path_runs/operator_attention_queue.json`

Optional only if strictly necessary:

- One small README in the same directory:
  `future_modules/the_fade/review/local_run/README_operator_attention_queue.md`
- One tiny helper `.py` in the same directory only, explicitly named in that future tranche.

No second entrypoint. No framework buildout.

---

## 3) Read/write boundaries for the future build tranche

The future script may:

- Scan completed local run folders only under:
  `future_modules/the_fade/outputs/local_happy_path_runs/`
- Read only bounded per-run artifacts already on disk:
  - `operator_attention_signal.json`
  - optionally `operator_review_gate.json` only if strictly necessary and justified
- Write exactly one artifact:
  `operator_attention_queue.json` at the fixed root path above

The future script may not:

- Read outside the local run root
- Perform cross-system/network fetches
- Parse markdown as a data source
- Invoke scanner, ingress, bridge, runner, validators, gate script, or other pipeline tools

---

## 4) Allowed future queue behavior (mechanical only)

Allowed behavior for the future implementation slice:

- Discover run folders (`run_*`) under the fixed local run root.
- Include only runs with valid parseable `operator_attention_signal.json`.
- Extract factual fields already present in that artifact.
- Build transparent mechanical rows and aggregate counts.
- Apply transparent ordering only (for example timestamp-desc from run folder name).
- Optionally partition/group by `operator_attention_status` derived directly from artifacts.

Not allowed:

- Fuzzy prioritization
- Heuristic scores
- Qualitative intelligence labels
- Recommendations or trade ideas

---

## 5) Allowed queue artifact content (bounded)

The future `operator_attention_queue.json` may include only bounded factual content such as:

- `generated_at_utc`
- `queue_schema_version`
- `runs_root_relative`
- `counts`
- `runs` array rows with:
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

No speculative or inferred fields beyond transparent mechanical derivations.

---

## 6) Forbidden work remains forbidden

Even in the future T113 build tranche, all of the following remain forbidden:

- AI/LLM summarization
- Recommendations or trade ideas
- Ranking/scoring/selection logic
- New data fetches / network calls
- Provider adapters/clients
- Dashboard/UI surfaces
- Runtime orchestration/scheduling/jobs/workers
- Lane reopen
- Evidence collection expansion
- `mvp_lane_approval.json` edits
- `mvp_lane_evidence_registry.json` edits
- Multi-slice bundling
- Hidden intelligence creep
- Broad reporting framework buildup
- Any claim that the queue is scanner output or a decision engine

---

## 7) Anti-drift lock

- One future implementation slice only
- One script only
- One queue artifact only
- No second surface
- No "while we're here" extras
- No widening into scanner/runtime/provider/dashboard/intelligence work

---

## 8) T113 non-claims

T113 does not:

- Implement the queue script
- Create `operator_attention_queue.json`
- Authorize scanner execution
- Authorize ranking/scoring/selection
- Authorize provider/dashboard/runtime expansion
- Change approval state or lane posture

