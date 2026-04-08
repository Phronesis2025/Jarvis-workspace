# THE FADE — T109 Local Operator Review Queue (Acceptance Criteria)

**Label:** `THE_FADE_PHASE3_T109_LOCAL_OPERATOR_REVIEW_QUEUE_ACCEPTANCE_CRITERIA`  
**Prompt #:** 402  
**Tranche #:** 109  
**Updated:** 2026-04-08T22:30:00+00:00

**Paired governance:** `THE_FADE_T109_LOCAL_OPERATOR_REVIEW_QUEUE_GOVERNANCE.md`

This document defines **PASS / FAIL / scope violation** for the **single** future implementation tranche that may add **`build_operator_review_queue.py`**.

---

## 1. Success criteria (PASS)

The implementation tranche **PASSes** only if **all** hold:

1. **Single entrypoint:** Exactly **one** new runnable script at  
   `future_modules/the_fade/review/local_run/build_operator_review_queue.py`  
   (plus **optional** `README_operator_review_queue.md` in the same directory, plus **optional** **one** explicitly named tiny helper `*.py` in that directory **only** if strictly necessary).

2. **One queue artifact out:** Each invocation writes **exactly one** file at  
   `future_modules/the_fade/outputs/local_happy_path_runs/operator_review_queue.json`  
   (overwrite on success).

3. **Bounded scan:** The script **only** enumerates **direct** child directories of  
   `future_modules/the_fade/outputs/local_happy_path_runs/`  
   whose names start with `run_`. **No** deeper directory walks, **no** reads outside that directory tree except writing the queue file path above.

4. **Per-run read boundary:** For each candidate folder, **only**:
   - `operator_review_gate.json` (if present)
   - `run_summary.json` (if present)  
   **Do not** read `source_snapshot.json`, Markdown, copied request/result JSON, or any other paths in the first queue build.

5. **No network:** No HTTP, DNS, subprocess to network tools, or sockets.

6. **No pipeline invocation:** Does not call ingress, bridge, runner, validators, or `build_operator_review_gate_signal_from_run_folder.py` (queue is **read-only** aggregation of existing disk state).

7. **Top-level queue shape:** Root JSON object includes at minimum:
   - `generated_at_utc` (string, UTC, ISO-8601 from local clock)
   - `queue_schema_version`: **exactly** `t109_v1`
   - `runs_root_relative`: **exactly** `future_modules/the_fade/outputs/local_happy_path_runs`
   - `runs` (array)
   - `counts` (object with non-negative integer values only, see §2)
   - `explicit_non_scanner_statement` (exact string from §4)
   - `explicit_non_trading_signal_statement` (exact string from §4)

8. **Row shape:** Each element of `runs` corresponds to **one** candidate run folder **after** sorting per §1 item 9 and §3. Each row includes at minimum:
   - `run_folder_name` (string, basename)
   - `operator_review_gate_present` (boolean)
   - `run_summary_present` (boolean)  
   When `operator_review_gate.json` parsed successfully as a JSON object, also copy (when keys exist with correct types):  
   `review_gate_status`, `review_gate_reasons`, `request_id` (string), `source_name` (string), `scanner_status` (string), `candidate_outputs_count` (integer), `deferred_count` (integer), `results_count` (integer **only** if present as JSON integer in gate file).  
   When gate present, include `operator_review_gate_path` as repo-relative forward-slash path:  
   `future_modules/the_fade/outputs/local_happy_path_runs/<run_folder_name>/operator_review_gate.json`  
   When `run_summary.json` parses and has string `status`, include `run_summary_status` (verbatim copy).

9. **Ordering (normative):** Sort rows by parsing `run_folder_name`: strip prefix `run_`; if remainder matches `YYYYMMDDTHHMMSSZ` (UTC Zulu pattern per existing run convention), use that string for **descending** lexicographic sort (newer folder names first). Folders that **do not** parse go **after** all parseable rows, sorted by **descending** full `run_folder_name`.

10. **Registry/approval:** No edits to `mvp_lane_approval.json` or `mvp_lane_evidence_registry.json`.

11. **Exit code:** Process exits `0` after successful write; non-zero on usage errors or unrecoverable I/O failure (document in README).

---

## 2. `counts` object (mechanical)

**Required keys** (non-negative integers):

| Key | Rule |
|-----|------|
| `total_run_folders` | Number of `run_*` direct children |
| `rows_with_operator_review_gate` | Rows where gate file existed and parsed as object |
| `open_for_operator_review` | Rows where `review_gate_status` **equals** `open_for_operator_review` |
| `do_not_open_mechanical_failure` | Rows where `review_gate_status` **equals** `do_not_open_mechanical_failure` |
| `missing_operator_review_gate` | Rows where gate file absent or unreadable |

**Note:** Rows without a readable gate file increment `missing_operator_review_gate`. Rows with a parsed gate object increment `rows_with_operator_review_gate`. Increment `open_for_operator_review` **only** when `review_gate_status` **equals** `open_for_operator_review`; increment `do_not_open_mechanical_failure` **only** when it **equals** `do_not_open_mechanical_failure`. If `review_gate_status` is missing or any other string, do **not** increment those two keys (still count `rows_with_operator_review_gate`).

---

## 3. Ordering — implementation detail

Parse regex: after `run_`, require `^\d{8}T\d{6}Z$` on the remainder for “parseable.” Else “unparseable” bucket.

---

## 4. Required fixed disclaimer strings

**`explicit_non_scanner_statement`:**  
`This queue is a mechanical index of local run folders and existing operator_review_gate.json files. It is not a universe scanner execution result and not a scanner decision artifact.`

**`explicit_non_trading_signal_statement`:**  
`This queue is not a trading signal, investment recommendation, or prioritization of markets or instruments.`

---

## 5. Failure criteria (implementation FAIL)

- More than one new entrypoint for this slice (excluding one optional helper module).
- Queue file path or name differs from **`future_modules/the_fade/outputs/local_happy_path_runs/operator_review_queue.json`**.
- Reads any file outside §1 item 4 per run, or outside the scan root except the queue write path.
- Performs network I/O or subprocesses pipeline tools.
- Emits scores, ranks (beyond §1 item 9 **sort order** as mechanical ordering, not merit), recommendations, or free-form prose beyond fixed literals.
- Implements “AI” features.

---

## 6. Scope violation (process FAIL)

- Bundling batch gates for other modules, dashboards, or multi-repo scans.
- Editing lane/registry/approval files.
- Widening scan to `inputs/`, global `outputs/`, or other lanes.

---

## 7. T109-specific note

**Tranche T109 (this prompt):** governance and acceptance criteria **only** — **no** queue script code. Executable queue work is **explicitly not done** until a later build tranche that cites these documents.
