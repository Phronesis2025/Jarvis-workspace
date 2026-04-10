# THE FADE — T120 re-evidence observations

**Prompt #:** 427  
**Label:** `THE_FADE_REFRESH_T120_REEVIDENCE_AFTER_SECOND_RUN`  
**Tranche #:** 121 (refresh after second qualifying run)  
**Updated:** 2026-04-10T14:42:54+00:00  

**Authority:** Factual record for PATH A (re-evidence first). **No** change to T117/T118 rule logic. Companion rollup: `outputs/local_happy_path_runs/first_real_scanner_rule_reevidence_summary.json` (regenerate via `rollup_first_real_scanner_evaluations_for_reevidence.py`).

---

## Observed

- **Two** qualifying runs under `outputs/local_happy_path_runs/`: **`run_20260408T125708Z`** and **`run_20260410T143649Z`**, each with `source_records_snapshot.json` and `first_real_scanner_rule_evaluation.json`.
- **Run 1 (`run_20260408T125708Z`):** `fetch_url_used` = `https://www.federalregister.gov/api/v1/documents.json?per_page=5&order=newest`; `fetch_timestamp_utc` = `2026-04-09T20:19:40Z`; five `source_records` rows; all five FR `type` **`Presidential Document`**; T118 outcome **`eligible_count` = 0**, **`excluded_count` = 5**; every row **`scanner_rule_reasons`** includes **`document_type_not_allowed`** only.
- **Run 2 (`run_20260410T143649Z`):** same `fetch_url_used`; `fetch_timestamp_utc` = `2026-04-10T14:37:50Z`; five rows: **one** `Presidential Document` (excluded, `document_type_not_allowed`), **one** `Proposed Rule`, **three** `Notice` — **four** rows **`eligible_by_rule`** with **`meets_first_real_scanner_rule`**, **one** excluded.
- Rollup `first_real_scanner_rule_reevidence_summary.json` (as regenerated for this doc) lists **`t120_diversity_gate_satisfied`:** **`true`** with note that at least two runs differ on `fetch_url_used`, `fetch_timestamp_utc`, or `api_results_length`.
- **What changed after the second run:** run coverage went from **one** to **two** snapshot+evaluation pairs; diversity gate flipped from **not satisfied** to **satisfied**; aggregate row-level reason counts now include both **`document_type_not_allowed`** (6) and **`meets_first_real_scanner_rule`** (4) across the two runs (10 row evaluations total).

---

## Inferred

- The **unchanged** type allowlist remains decisive where FR `type` is not in `Rule` / `Proposed Rule` / `Notice` (run 1: only Presidential; run 2: one Presidential excluded, allowlisted types passed other rule checks for the four eligible rows).
- The rollup remains **mechanical**: re-running `rollup_first_real_scanner_evaluations_for_reevidence.py` refreshes `per_run`, aggregate histograms, and the diversity flag from on-disk evaluations without changing rule code.

---

## Unknown

- Whether repeated “newest” + `per_page=5` pulls over time stay **useful for operator disclosure** (this refresh proves **heterogeneity is possible** across runs; it does **not** prove stable mix or coverage of topics).
- Whether additional runs would often show **`eligible_by_rule`** or revert to mostly type-excluded rows under the same query shape.

---

## Run coverage summary

| Metric | Value (as of this doc) |
|--------|-------------------------|
| `run_*` directories scanned | 2 under `outputs/local_happy_path_runs/` |
| Runs with `source_records_snapshot.json` | 2 (`run_20260408T125708Z`, `run_20260410T143649Z`) |
| Runs with `first_real_scanner_rule_evaluation.json` | 2 (same) |
| T120 diversity gate (≥2 qualifying runs + tuple diversity) | **Satisfied** (`true` in summary JSON) |

---

## Reason histogram summary

### Aggregate (all evaluated runs in summary JSON)

| `scanner_rule_reasons` code (row-level) | Count |
|----------------------------------------|------:|
| `document_type_not_allowed` | 6 |
| `meets_first_real_scanner_rule` | 4 |

### Per run

| Run folder | Rows | Eligible | Excluded | Histogram |
|------------|-----:|---------:|---------:|-----------|
| `run_20260408T125708Z` | 5 | 0 | 5 | `document_type_not_allowed`: 5 |
| `run_20260410T143649Z` | 5 | 4 | 1 | `document_type_not_allowed`: 1; `meets_first_real_scanner_rule`: 4 |

---

## T118 unchanged

- **`build_first_real_scanner_rule_from_run_folder.py`** was **not** modified in #427.
