# THE FADE — T117 First Real Scanner Rule (Acceptance Criteria)

**Label:** `THE_FADE_PHASE3_T117_GOVERNANCE_LOCK_FIRST_REAL_SCANNER_RULE`  
**Prompt #:** 417  
**Tranche #:** 117  
**Updated:** 2026-04-09T22:00:00+00:00

**Authority:** Executable work is **not** in **T117**. A **future** single build tranche **PASS**es only if **all** criteria below are met.

**Governance:** `THE_FADE_T117_FIRST_REAL_SCANNER_RULE_GOVERNANCE.md`  
**Pointer:** `future_modules/the_fade/config/phase3_t117_first_real_scanner_rule.json`

---

## A. Mandatory scope (implementation tranche)

1. **Exactly one** primary script: `future_modules/the_fade/review/local_run/build_first_real_scanner_rule_from_run_folder.py`.
2. **At most one** optional README: `future_modules/the_fade/review/local_run/README_first_real_scanner_rule.md`.
3. **At most one** optional helper `*.py` in the **same** directory — only if strictly necessary; name **must** appear in README or file header comment.
4. **No** other new Python entrypoints under `future_modules/the_fade/` for this slice.
5. Per successful run: **exactly one** **`first_real_scanner_rule_evaluation.json`** in the specified run folder.

---

## B. Input / read rules

1. CLI accepts **one** argument: run folder name or absolute path; must resolve to **`outputs/local_happy_path_runs/run_<YYYYMMDDTHHMMSSZ>/`**.
2. **Required file:** `source_records_snapshot.json` with **`artifact_kind`** **`the_fade_t115_source_records_snapshot_v1`** and array **`source_records`**.
3. **`source_snapshot.json`:** **do not** read in the default implementation path unless this file is amended in the **same** tranche with **exact** allowed keys; **recommended:** derive **`run_id`** from **`source_records_snapshot.json`** top-level **`run_id`** if present, else from **`run_folder_name`**, else **`null`** — **no** `source_snapshot.json` read.

---

## C. Network rules

**Zero** HTTP requests. **No** subprocess to ingress or T116 capture script. **Fail** if network attempted.

---

## D. Rule implementation (mechanical)

Apply governance **§5** exactly:

- Type allowlist: **`Rule`**, **`Proposed Rule`**, **`Notice`** (case-sensitive).
- Recency: **`D_pub` ∈ { `D_fetch`, `D_fetch`-1 day, `D_fetch`-2 days }** in UTC calendar arithmetic from **`fetch_timestamp_utc`**.
- **`publication_date` parse:** If string length ≥ 10 and characters 0–9 match `YYYY-MM-DD` and form a valid Gregorian date, use that date as **`D_pub`**. Otherwise use `datetime.date.fromisoformat` on the date portion of the string when possible; if parsing fails → **`invalid_publication_date`** (and **`missing_publication_date`** if empty).

---

## E. Output JSON (minimum fields)

| Field | Rule |
|--------|------|
| `generated_at_utc` | ISO-8601 UTC |
| `rule_schema_version` | `t117_v1` |
| `run_id` | string or null per §B.3 |
| `run_folder_name` | basename |
| `source_name` | from snapshot or `Federal Register` default |
| `fetch_timestamp_utc` | verbatim from input snapshot |
| `rule_metadata` | includes `rule_id`: `first_real_scanner_rule_t117_v1` |
| `eligible_count`, `excluded_count` | integers |
| `eligible_records`, `excluded_records` | arrays |
| Per-row | `scanner_rule_status` ∈ {`eligible_by_rule`,`excluded_by_rule`}; `scanner_rule_reasons` per governance §7 |
| `explicit_non_engine_statement` | Exact literal from governance §6 |

Per-row copies: only **`document_number`**, **`publication_date`**, **`title`**, **`document_type`**, **`type`**, **`html_url`**, **`pdf_url`** when present on input row (no invention).

---

## F. Success (PASS)

- Script exits **0**; writes valid JSON; counts match input length; every input row appears in **exactly one** of **`eligible_records`** / **`excluded_records`**; vocab closed; statement present.

## G. Failure (FAIL)

- Missing or invalid **`source_records_snapshot.json`**; missing **`fetch_timestamp_utc`**; unparsable **`fetch_timestamp_utc`** for **`D_fetch`**; write failure.

## H. Scope violation

- Any network call; second output file; LLM use; extra rules; reading forbidden files; registry/approval edits.

---

## I. T117 confirmation

**T117** (Prompt **#417**) adds governance + config pointer + control-doc updates only. **No** executable rule code in **T117**.
