# THE FADE — T120 re-evidence observations

**Prompt #:** 424  
**Label:** `THE_FADE_BUILD_FIRST_RULE_REEVIDENCE_SLICE`  
**Tranche #:** 120 (re-evidence build)  
**Updated:** 2026-04-10T14:25:00+00:00  

**Authority:** Factual record for PATH A (re-evidence first). **No** change to T117/T118 rule logic. Companion rollup: `outputs/local_happy_path_runs/first_real_scanner_rule_reevidence_summary.json` (regenerate via `rollup_first_real_scanner_evaluations_for_reevidence.py`).

---

## Run coverage summary

| Metric | Value (as of this doc) |
|--------|-------------------------|
| `run_*` directories scanned | 1 under `outputs/local_happy_path_runs/` |
| Runs with `source_records_snapshot.json` | 1 (`run_20260408T125708Z`) |
| Runs with `first_real_scanner_rule_evaluation.json` | 1 (same) |
| T120 diversity gate (≥2 distinct qualifying runs + diversity) | **Not satisfied** |

---

## Observed

- Single qualifying run: **`run_20260408T125708Z`**.
- Snapshot: `fetch_url_used` = `https://www.federalregister.gov/api/v1/documents.json?per_page=5&order=newest`; `fetch_timestamp_utc` = `2026-04-09T20:19:40Z`; `api_response_metadata.results_length` = 5; five `source_records` rows.
- All five rows have FR `type` **`Presidential Document`** (no `document_type` field).
- Locked T118 evaluation: **`eligible_count` = 0**, **`excluded_count` = 5**; every row **`scanner_rule_reasons`** = `["document_type_not_allowed"]` only.
- Rollup script `rollup_first_real_scanner_evaluations_for_reevidence.py` produces `first_real_scanner_rule_reevidence_summary.json` with matching per-run and aggregate histogram: **`document_type_not_allowed`: 5** row-level mentions across the run.
- No `eligible_by_rule` rows in any evaluation on disk.

---

## Inferred

- On this feed slice, the **type allowlist** (`Rule`, `Proposed Rule`, `Notice`) is the **only** active filter; field and recency clauses did not surface as failure reasons for these rows.
- The rollup is **stable for reuse**: when a second run folder appears with snapshot (+ optional auto T118 via rollup), re-running the script will refresh histograms and diversity flag without redesign.

---

## Unknown

- Whether a **second** local run with a different FR query will yield mixed `type` values or any **`eligible_by_rule`** rows under the **unchanged** rule.
- Whether “newest” small-`per_page` pulls are **representative** of operator disclosure interest.

---

## Reason histograms

### Aggregate (all evaluated runs in summary JSON)

| `scanner_rule_reasons` code (row-level) | Count |
|----------------------------------------|------:|
| `document_type_not_allowed` | 5 |

### Per run

| Run folder | Rows | Eligible | Excluded | Histogram |
|------------|-----:|---------:|---------:|-----------|
| `run_20260408T125708Z` | 5 | 0 | 5 | `document_type_not_allowed`: 5 |

---

## Operator: add a second run (no slice redesign)

1. Complete a **new** happy-path run so `outputs/local_happy_path_runs/run_<new>/` exists with the usual artifacts.
2. **`python future_modules/the_fade/review/local_run/build_source_records_snapshot_from_run_folder.py run_<new>`** (bounded T116 GET).
3. **`python future_modules/the_fade/review/local_run/build_first_real_scanner_rule_from_run_folder.py run_<new>`** (or rely on rollup to subprocess T118 if evaluation missing).
4. **`python future_modules/the_fade/review/local_run/rollup_first_real_scanner_evaluations_for_reevidence.py`**
5. Update **this** doc’s Observed / histogram sections or add a dated addendum after #425 if governance requires.

---

## T118 unchanged

- **`build_first_real_scanner_rule_from_run_folder.py`** was **not** modified in #424.
