# THE FADE — T111 First Operator-Meaningful Filtering Signal (Acceptance Criteria)

**Label:** `THE_FADE_PHASE3_T111_FIRST_OPERATOR_MEANINGFUL_FILTERING_SIGNAL_ACCEPTANCE_CRITERIA`  
**Prompt #:** 405  
**Tranche #:** 111  
**Updated:** 2026-04-08T22:28:11+00:00

**Paired governance:** `THE_FADE_T111_FIRST_OPERATOR_MEANINGFUL_FILTERING_SIGNAL_GOVERNANCE.md`

This document defines **PASS / FAIL / scope violation** for the **single** future implementation tranche that may add **`build_operator_attention_signal_from_run_folder.py`**.

---

## 1. Success criteria (PASS)

The implementation tranche **PASSes** only if **all** hold:

1. **Single entrypoint:** Exactly **one** new runnable script at  
   `future_modules/the_fade/review/local_run/build_operator_attention_signal_from_run_folder.py`  
   (plus **optional** `README_operator_attention_signal.md` in the same directory, plus **optional** **one** explicitly named tiny helper `*.py` in that directory **only** if strictly necessary).

2. **One signal artifact out:** Each successful invocation writes **exactly one** file named **`operator_attention_signal.json`** inside the **same** resolved run folder. **No** other output files.

3. **One run folder in:** CLI (or documented single argument) resolves **exactly one** directory that is a **direct child** of `future_modules/the_fade/outputs/local_happy_path_runs/` and whose basename matches `^run_\d{8}T\d{6}Z$`.

4. **Read boundary:** Inside that folder **only**, reads **only**:
   - `operator_review_gate.json`
   - `source_snapshot.json` (if present — may attempt read when file exists)
   - `run_summary.json` (if present — **only** to evaluate §4 mechanical checks)  
   **No** Markdown, **no** request/result JSON, **no** other paths, **no** parent/sibling reads.

5. **No network:** No HTTP, DNS, sockets, or subprocesses that perform network I/O.

6. **No pipeline invocation:** Does **not** call ingress, bridge, runner, validators, `build_operator_review_gate_signal_from_run_folder.py`, or `build_operator_review_queue.py`.

7. **Top-level signal shape:** Root JSON object includes at minimum:
   - `generated_at_utc` (string, UTC ISO-8601)
   - `signal_schema_version`: **exactly** `t111_v1`
   - `run_folder_name` (string)
   - `operator_attention_status` (string; one of §2)
   - `operator_attention_reasons` (array of strings; each ∈ §3)
   - `explicit_non_scanner_statement` (exact string §7)
   - `explicit_non_trading_signal_statement` (exact string §7)

8. **Bounded factual fields (when inputs allow):**  
   When `operator_review_gate.json` parses as an object, copy when present and type-correct:
   - `run_id` (string), `request_id` (string), `source_name` (string), `review_gate_status` (string),
   - `candidate_outputs_count` (integer), `deferred_count` (integer).  
   **`results_count`:** If `source_snapshot.json` parses as an object and has top-level `results_count` as JSON integer, copy that integer into the signal as `results_count`. **Else if** snapshot missing/unparseable **and** gate has integer `results_count`, copy gate’s `results_count`. **Else** omit `results_count` from the signal.

9. **Mechanical decision:** `operator_attention_status` and `operator_attention_reasons` are computed **only** by §4 (no other logic).

10. **Exit code:** Process exits `0` after successful write; non-zero on usage errors or unrecoverable I/O failure.

11. **Registry/approval:** No edits to `mvp_lane_approval.json` or `mvp_lane_evidence_registry.json`.

---

## 2. Closed vocabulary — `operator_attention_status` (normative)

**Exactly one** of:

| Value |
|-------|
| `elevated_manual_attention` |
| `standard_manual_attention` |
| `do_not_elevate_mechanical_failure` |

---

## 3. Closed set — `operator_attention_reasons` (normative)

**Only** the following reason codes may appear (each entry in the array must be **exactly** one of these strings; list may be empty **only** where §4 explicitly allows):

| Code | When allowed (summary) |
|------|-------------------------|
| `missing_operator_review_gate` | Gate file absent. |
| `operator_review_gate_invalid_json` | Gate present but not a JSON object root or unreadable. |
| `review_gate_do_not_open` | Gate parsed and `review_gate_status == "do_not_open_mechanical_failure"`. |
| `run_summary_not_pass` | `run_summary.json` **exists**, parses as object, top-level `status` exists, and is **not** equal to string `PASS`. |
| `elevated_deferred_rows_present` | Gate parsed, `review_gate_status == "open_for_operator_review"`, and integer `deferred_count > 0`. |
| `elevated_snapshot_results_count_positive` | Gate open per §4 and §1 item 8 `results_count` rule yields an integer `> 0`. |
| `standard_open_no_elevation_triggers` | Gate open, §4 run-summary check (if any) passes, and **no** elevation codes apply. |

**Forbidden:** Any string not in the table above; duplicate codes should be deduplicated while preserving a stable order (e.g. sort ascending by code string).

---

## 4. Normative mechanical decision table (deterministic)

Let **G** = parsed `operator_review_gate.json` object, or **invalid**.

Let **run_summary_ok** = true when either `run_summary.json` is **absent**, or it parses as an object with string `status == "PASS"`.  
Let **run_summary_fail** = true when `run_summary.json` **exists** but parses and top-level `status` is missing, not a string, or `!= "PASS"`.

Let **elevated** =  
`(G` valid and `G.review_gate_status == "open_for_operator_review"` and integer `G.deferred_count > 0`)  
**OR**  
`(G` valid and `G.review_gate_status == "open_for_operator_review"` and **`results_count`** per §1 item 8 is an integer **`> 0`).

**Rule A — Gate missing or invalid:**  
If gate file absent → `do_not_elevate_mechanical_failure`, reasons include `missing_operator_review_gate`.  
If gate unreadable or root not object → `do_not_elevate_mechanical_failure`, reasons include `operator_review_gate_invalid_json`.

**Rule B — Gate reports mechanical failure:**  
If `G.review_gate_status == "do_not_open_mechanical_failure"` → `do_not_elevate_mechanical_failure`, reasons **must** include `review_gate_do_not_open`.

**Rule C — Run summary (only when file exists):**  
If **run_summary_fail** → `do_not_elevate_mechanical_failure`, reasons **must** include `run_summary_not_pass`.

**Rule D — Open gate + summary OK (or absent):**  
If Rules A–C do **not** apply and `G.review_gate_status == "open_for_operator_review"` and **run_summary_ok**:  
- If **elevated** → `elevated_manual_attention`; reasons **must** include every applicable code from: `elevated_deferred_rows_present`, `elevated_snapshot_results_count_positive` (both if both true).  
- Else → `standard_manual_attention`; reasons **must** include `standard_open_no_elevation_triggers`.

**Note:** Rules A–C take precedence in order; first matching rule wins.

---

## 5. Failure criteria (implementation FAIL)

- More than one new entrypoint (excluding one optional helper module).  
- Signal filename or location differs from **`operator_attention_signal.json`** in the resolved run folder.  
- Reads any file outside the three allowed basenames in that folder.  
- Network I/O or pipeline/tool invocation.  
- Free-form or non-closed `operator_attention_reasons` entries.  
- `operator_attention_status` outside §2.  
- Scores, ranks (beyond this single-run status), recommendations, or “AI” features.  

---

## 6. Scope violation (process FAIL)

- Multi-run batch in one invocation.  
- Editing lane/registry/approval files.  
- Bundling with queue rebuild, gate rebuild, or scanner work in the same tranche.  

---

## 7. Required fixed disclaimer strings

**`explicit_non_scanner_statement`:**  
`This artifact is a mechanical operator attention signal derived only from local run-folder JSON files. It is not a universe scanner execution result and not a scanner decision artifact.`

**`explicit_non_trading_signal_statement`:**  
`This artifact is not a trading signal, investment recommendation, or prioritization of markets or instruments.`

---

## 8. T111-specific note

**Tranche T111 (this prompt):** governance and acceptance criteria **only** — **no** attention-signal script code. Executable work is **explicitly not done** until a later build tranche.
