# THE FADE — T109 Local Operator Review Queue (Governance Lock)

**Label:** `THE_FADE_PHASE3_T109_GOVERNANCE_LOCK_LOCAL_OPERATOR_REVIEW_QUEUE`  
**Prompt #:** 402  
**Tranche #:** 109  
**Phase:** 3 — local pipeline (operator tooling adjacent to happy-path runs)  
**Updated:** 2026-04-08T22:30:00+00:00

**Authority:** This file is **governance and boundary only**. It **does not** implement executable code. **T109** locks **exactly one** future implementation slice: a **single** local script that **scans** completed run folders under `outputs/local_happy_path_runs/` and writes **one** machine-readable queue artifact. **No** universe-scanner execution, **no** ranking/scoring/selection semantics, **no** AI/LLM, **no** new network I/O, **no** lane/registry/approval edits.

---

## 1. Slice identity (exactly one implementation tranche later)

| Property | Value |
|----------|--------|
| Slice name | Local operator review queue (mechanical) |
| Future build tranche | **One** tranche only — implement **only** this doc + `THE_FADE_T109_LOCAL_OPERATOR_REVIEW_QUEUE_ACCEPTANCE_CRITERIA.md` |
| Scope | **Local-only** aggregation of **existing** per-run artifacts; **not** a scanner; **not** a trading or investment signal; **not** a decision engine |

---

## 2. Scan root (bounded)

The later script **must** consider **only** direct child directories of:

`future_modules/the_fade/outputs/local_happy_path_runs/`

**Inclusion rule:** A directory is a **candidate run folder** if and only if its **name** starts with the prefix `run_` (same convention as T99–T108 run folders).

**Forbidden:** Recursion into nested directories beyond one level under `local_happy_path_runs/`; reads outside `local_happy_path_runs/` except writing the single queue file at the fixed path below; reading any other repo tree for “queue enrichment.”

---

## 3. Allowed per-run read set (bounded)

For **each** candidate run folder, the implementation **may** read **only**:

1. **`operator_review_gate.json`** (when the file exists) — **primary** source for `review_gate_status`, `review_gate_reasons`, and fields already copied into that artifact by T108 (e.g. `request_id`, `source_name`, `scanner_status`, `candidate_outputs_count`, `deferred_count`, `results_count` when present).
2. **`run_summary.json`** (when the file exists) — for factual run envelope fields (e.g. `run_id`, `status`, timestamps, copied path strings) and to detect a completed run surface without inferring success.

**`source_snapshot.json`:** **Not** read in the **first** governed queue implementation tranche after **T109**. If a future governance tranche documents a **specific** field that cannot be obtained from `operator_review_gate.json` + `run_summary.json`, it may amend this boundary; until then, **no** `source_snapshot.json` reads in the queue builder.

**Forbidden per run:** Markdown (`operator_review.md`, `source_backed_operator_review.md`, …), copied request/result JSON, ingress, bridge, validators, network.

---

## 4. Output: exactly one queue artifact (fixed path)

| Property | Value |
|----------|--------|
| Artifact filename | `operator_review_queue.json` |
| **Fixed path** | `future_modules/the_fade/outputs/local_happy_path_runs/operator_review_queue.json` |
| Overwrite | Implementation overwrites this file on each successful run (idempotent regenerate) |

**No** second queue file, **no** alternate basename, **no** per-run queue fragments.

---

## 5. Fixed implementation path (single entrypoint)

| Property | Value |
|----------|--------|
| **Single script path** | `future_modules/the_fade/review/local_run/build_operator_review_queue.py` |
| Optional README | `future_modules/the_fade/review/local_run/README_operator_review_queue.md` (short usage only) |
| Optional helper | **At most one** additional `*.py` in **the same directory**, **only** if strictly necessary, **must** be explicitly named in the implementation tranche and acceptance criteria |

**Forbidden:** second CLI entrypoint, framework/library extraction for “reporting,” dashboard or HTTP server, scheduled jobs.

---

## 6. Allowed queue artifact content (factual + mechanical only)

Top-level object **may** include **only**:

- **`generated_at_utc`** — ISO-8601 UTC string from the local process clock at write time (transparent; not a network time sync).
- **`queue_schema_version`** — fixed string literal (e.g. `t109_v1`) set in acceptance criteria.
- **`runs_root_relative`** — fixed relative path string from repo root: `future_modules/the_fade/outputs/local_happy_path_runs` (or equivalent single documented literal).
- **`runs`** — JSON array of **row objects** (one per candidate run folder, **after** stable ordering — see §7).
- **`counts`** — optional object with **non-negative integers** only, derived mechanically (e.g. `total_run_folders`, `rows_with_gate_artifact`, `open_for_operator_review`, `do_not_open_mechanical_failure`) — **no** floats, **no** scores.
- **`explicit_non_scanner_statement`** — required fixed literal (see acceptance criteria).
- **`explicit_non_trading_signal_statement`** — required fixed literal (see acceptance criteria).

**Each row object** **may** include **only** bounded fields, such as:

- `run_folder_name` (string; directory basename)
- `operator_review_gate_present` (boolean)
- `operator_review_gate_path` (string; repo-relative or forward-slash path under `runs_root_relative`, **only** when gate file exists)
- `review_gate_status` (string; **only** when copied from gate JSON — must be `open_for_operator_review` or `do_not_open_mechanical_failure`)
- `review_gate_reasons` (array of strings; **only** when copied from gate JSON)
- `request_id`, `source_name`, `scanner_status`, `candidate_outputs_count`, `deferred_count` — **only** when present in `operator_review_gate.json` (copy or omit; **no** recompute from other files in T110)
- `results_count` — **only** when present as a JSON integer in `operator_review_gate.json`
- `run_summary_present` (boolean)
- `run_summary_status` (string; **only** when `run_summary.json` exists and top-level `status` is a string — copy verbatim)
- Optional **path strings** to known review artifacts **only** as fixed relative path templates documented in acceptance (e.g. path to `operator_review.md` **without reading** that file)

**Forbidden in the queue artifact:** priority scores, “confidence,” natural-language recommendations, trade ideas, ranked “top picks,” narrative summaries, URLs fetched at runtime, data not read from allowed files.

---

## 7. Allowed ordering and filtering (purely mechanical)

**Normative rules** (locked in acceptance criteria):

1. **Filter:** Include **all** candidate run folders (`run_*` direct children). **Do not** exclude folders merely because the gate file is missing (record `operator_review_gate_present: false` instead).
2. **Ordering:** Stable **descending** order by run folder timestamp parsed from the suffix after `run_` when it matches `YYYYMMDDTHHMMSSZ`; if a folder name does not parse, place it after parseable rows in **descending lexicographic** order by full folder name (documented tie-break).
3. **Partitioning:** Optional **non-destructive** top-level keys `open_rows` / `blocked_rows` **are forbidden** in the first implementation — use a **single** `runs` array only to avoid duplicate row semantics. The operator may filter client-side by `review_gate_status` when present.

**Forbidden:** fuzzy “importance,” heuristic sorting, ML-based ordering, hidden weights.

---

## 8. Relationship to T108 gate artifacts

The queue **does not** re-run the gate logic. It **reflects** whatever is already in each `operator_review_gate.json`. If the gate file is absent, the row **must not** invent `review_gate_status`; it **must** mark the gate absent and **must not** claim scanner or pipeline success.

---

## 9. Explicitly forbidden (queue implementation tranche and adjacent)

- AI/LLM summarization or “smart” queue commentary  
- Recommendations, trade ideas, prioritization beyond §7  
- Ranking/scoring/selection semantics (ordering in §7 is **not** a merit rank)  
- New network calls, provider clients, credentials  
- Universe scanner execution, ingress, bridge, runner, validator **invocation** from the queue script  
- Dashboard/UI, schedulers, workers, orchestration platforms  
- Lane reopen, evidence collection, edits to `mvp_lane_approval.json` or `mvp_lane_evidence_registry.json`  
- Multi-slice bundling, second entrypoint, reporting framework buildup  
- Pretending the queue is a scanner output, decision engine, or trading signal  

---

## 10. Non-claims

**T109** does not implement the queue script. **T109** does not authorize scanner/runtime/dashboard/provider work. **T109** does not change scoped MVP approval or lane posture. Executable queue work remains **not done** until a **later** governed build tranche that cites these **T109** documents.
