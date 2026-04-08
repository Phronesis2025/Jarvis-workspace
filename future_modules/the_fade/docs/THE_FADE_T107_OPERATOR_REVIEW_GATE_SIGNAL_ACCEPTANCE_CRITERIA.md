# THE FADE — T107 Operator Review Gate Signal (Acceptance Criteria)

**Label:** `THE_FADE_PHASE3_T107_OPERATOR_REVIEW_GATE_SIGNAL_ACCEPTANCE_CRITERIA`  
**Prompt #:** 399  
**Tranche #:** 107  
**Updated:** 2026-04-08T20:30:00+00:00

**Paired governance:** `THE_FADE_T107_OPERATOR_REVIEW_GATE_SIGNAL_GOVERNANCE.md`

This document defines **PASS / FAIL / scope violation** for the **single** future implementation tranche that may add **`build_operator_review_gate_signal_from_run_folder.py`**.

---

## 1. Success criteria (PASS)

The implementation tranche **PASSes** only if **all** hold:

1. **Single entrypoint:** Exactly **one** new runnable script at  
   `future_modules/the_fade/review/local_run/build_operator_review_gate_signal_from_run_folder.py`  
   (plus **optional** `README_operator_review_gate.md` in the same directory, plus **optional** **one** explicitly named tiny helper `*.py` in that directory **only** if strictly necessary).

2. **One folder in, one artifact out:** Each invocation targets **exactly one** run folder under  
   `future_modules/the_fade/outputs/local_happy_path_runs/run_<YYYYMMDDTHHMMSSZ>/`  
   and writes **exactly one** file **`operator_review_gate.json`** in **that** folder.

3. **Read boundary:** Reads **only** (inside that folder):  
   `run_summary.json`, exactly one `fr_universe_scanner_request_*.json`, exactly one `bridge_universe_scanner_result_*.json`, and `source_snapshot.json`.  
   **Does not** read `source_backed_operator_review.md` or `operator_review.md` in the first gate-signal implementation tranche unless a **new** governance tranche explicitly expands the read list.

4. **No network:** No `urllib`, `requests`, sockets, subprocess to network tools, or any new HTTP I/O.

5. **No pipeline replacement:** Does not invoke or reimplement ingress, validators, bridge, or T98 runner; does not modify copied request/result/summary/snapshot files.

6. **Factual extraction:** Field values are copied or mechanically counted from parsed JSON only (string equality, array lengths, filtered counts with a documented predicate).

7. **Gate enum and reasons:** Output JSON includes **`review_gate_status`** with **exactly** one of:
   - `open_for_operator_review`
   - `do_not_open_mechanical_failure`  
   and **`review_gate_reasons`**: array of zero or more strings drawn **only** from the vocabulary in §3 below.

8. **Required disclaimers:** Output includes **`explicit_non_scanner_statement`** and **`explicit_non_trading_signal_statement`** as **exact** string literals defined in §4.

9. **Mechanical gate rule (normative):**  
   Set `review_gate_status` to **`open_for_operator_review`** **if and only if** all of the following are true; otherwise set **`do_not_open_mechanical_failure`** and append **all applicable** reason codes from §3:
   - `run_summary.json` parses as a JSON object, contains string key `status`, and `status == "PASS"`.
   - `source_snapshot.json` exists and parses as a JSON object.
   - Exactly one `fr_universe_scanner_request_*.json` and exactly one `bridge_universe_scanner_result_*.json` exist; both parse as JSON objects.
   - Result object contains string key `scanner_status` with value **`pending`**.
   - Result object contains key `candidate_outputs` whose value is a JSON array with **length > 0**.
   - `deferred_count` computed as: number of elements `x` in `candidate_outputs` where `x` is a JSON object and `x.get("status") == "deferred"` satisfies **`deferred_count > 0`** (if `candidate_outputs` is missing or not an array, use failure reasons; do not emit a misleading deferred count).

   **`results_count` in output:** Include key `results_count` **only** when `source_snapshot.json` contains key `results_count` with a JSON number value that is an integer (e.g. `isinstance` check in Python); copy that integer. Otherwise **omit** `results_count` from the gate artifact.

10. **Operator-facing clarity:** Script exits with non-zero on usage errors (bad path, wrong folder parent, missing files for gate computation) **or** document in README if gate always writes JSON with `do_not_open_mechanical_failure` — **pick one** behavior and document it; default expectation is **non-zero exit** when the run folder is invalid or required inputs for parsing are missing.

11. **Registry/approval:** No edits to `mvp_lane_approval.json` or `mvp_lane_evidence_registry.json`.

---

## 2. Failure criteria (implementation FAIL)

- More than one new entrypoint script for this slice (excluding one optional helper module).
- Gate artifact name or path differs from **`operator_review_gate.json`** in the run folder.
- Reads any file outside the allowed list (including Markdown reviews in the authorized gate-signal tranche).
- Performs network I/O or invokes ingress/bridge/runner/validators.
- Emits free-form prose in `review_gate_reasons` or adds undefined `review_gate_status` values.
- Implements ranking, scoring, selection, or “AI” features.

---

## 3. Machine reason vocabulary (closed set)

Implementations **may** emit **only** these reason strings (subset as applicable):

| Code | Meaning |
|------|--------|
| `missing_run_summary` | `run_summary.json` absent |
| `run_summary_not_pass` | `status` missing or not `PASS` |
| `run_summary_invalid_json` | Parse error |
| `missing_source_snapshot` | `source_snapshot.json` absent |
| `source_snapshot_invalid_json` | Parse error |
| `request_file_not_exactly_one` | Not exactly one `fr_universe_scanner_request_*.json` |
| `result_file_not_exactly_one` | Not exactly one `bridge_universe_scanner_result_*.json` |
| `request_invalid_json` | Request JSON parse error |
| `result_invalid_json` | Result JSON parse error |
| `scanner_status_not_pending` | `scanner_status` missing or not `pending` |
| `candidate_outputs_missing_or_empty` | Missing, not array, or length 0 |
| `deferred_count_zero` | No deferred rows per §1 rule |

When `review_gate_status` is **`open_for_operator_review`**, `review_gate_reasons` **should** be `[]` or omit optional informational codes — **do not** invent ad-hoc success messages; use fixed literals only in disclaimer fields.

---

## 4. Required fixed disclaimer strings

Use **exactly** these values in the gate artifact:

**`explicit_non_scanner_statement`:**  
`This artifact is a mechanical operator triage signal derived only from local run-folder JSON files. It is not a universe scanner execution result and not a scanner decision artifact.`

**`explicit_non_trading_signal_statement`:**  
`This artifact is not a trading signal, investment recommendation, or prioritization of markets or instruments.`

---

## 5. Scope violation (process FAIL)

Any of the following is a **scope violation** (revert / redo):

- Changes to `future_modules/the_fade/config/mvp_lane_approval.json` or `mvp_lane_evidence_registry.json` under the guise of this slice.
- Bundling additional “nice to have” reports, dashboards, or multi-run batch gates in the same tranche.
- Widening read paths to global `inputs/` or `outputs/` roots beyond the single run folder.

---

## 6. T107-specific note

**Tranche T107 (this prompt):** governance and acceptance criteria **only** — **no** implementation code. **Executable** gate work is **explicitly not done** until a later build tranche that cites these documents.
