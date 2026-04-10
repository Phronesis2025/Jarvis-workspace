# THE FADE — T125 differentiated evidence observations

**Prompt #:** 435  
**Label:** `THE_FADE_BUILD_DIFFERENTIATED_EVIDENCE_SLICE`  
**Tranche #:** 125 (PATH B — differentiated evidence first)  
**Updated:** 2026-04-10T17:41:53+00:00  

**Recovery (#436):** Work was **re-based on `the-fade-phase1-tranche1-foundation`**, **`run_20260410T153739Z`** restored from branch truth, and the rollup was **re-run** so **`first_real_scanner_rule_reevidence_summary.json`** includes **four** qualifying runs (T123 duplicate baseline + differentiated run). **T118 / rollup scripts** were **already** tracked on this branch — not part of this lock commit.

**Authority:** Evidence only per **`THE_FADE_T125_REPAIR_VS_DIFFERENTIATED_EVIDENCE_GOVERNANCE.md`**. **No** T117/T118 logic edits, no second rule, no registry/approval edits. Rollup: `outputs/local_happy_path_runs/first_real_scanner_rule_reevidence_summary.json`.

---

## Differentiation callout — **criterion A**

**A (chosen):** Locked T89 ingress was invoked with **`--per-page 10`** (`N=10`, **N ≠ 5**). The new run’s `source_records_snapshot.json` records  
`fetch_url_used` = `https://www.federalregister.gov/api/v1/documents.json?per_page=10&order=newest` — **not** equal to the baseline `per_page=5&order=newest` URL used by `run_20260410T143649Z`.

**B:** Not used.

---

## Comparison vs `run_20260410T143649Z` (exact)

| Dimension | `run_20260410T143649Z` | `run_20260410T171258Z` (new) |
|-----------|-------------------------|------------------------------|
| `fetch_url_used` | `...per_page=5&order=newest` | `...per_page=10&order=newest` |
| `api_response_metadata.results_length` / rows | 5 | 10 |
| `document_number` set (sorted) | `2026-07030`, `2026-07031`, `2026-07032`, `2026-07033`, `2026-07069` | **Superset:** same five **plus** `2026-07025`, `2026-07026`, `2026-07027`, `2026-07028`, `2026-07029` (five additional FR rows) |
| T118 outcome | 4 eligible, 1 excluded | 9 eligible, 1 excluded |

The new sample is **not** a duplicate “newest five” slice: it widens the window to **ten** newest documents and introduces **five** new `document_number` values not present in the baseline run’s snapshot.

---

## Observed

- New qualifying run folder **`run_20260410T171258Z`** with **`source_snapshot.json`**, **`source_records_snapshot.json`**, **`first_real_scanner_rule_evaluation.json`**, plus copied request/result and **`run_summary.json`** (operator path: manual T89 `--per-page 10` + T96 bridge + root cleanup, documented in `run_summary.wrapped_runner_path`).
- **`fetch_url_used`** documents **criterion A** differentiation from baseline `per_page=5` pulls.
- **`first_real_scanner_rule_evaluation.json`:** **`eligible_count` = 9**, **`excluded_count` = 1**; single excluded row is **`Presidential Document`** (`2026-07069`); allowlisted rows carry **`meets_first_real_scanner_rule`**.
- Regenerated **`first_real_scanner_rule_reevidence_summary.json`** (post-#436): **`run_directories_scanned` = 4**, **`runs_with_source_records_snapshot` = 4**, **`runs_with_first_real_scanner_rule_evaluation` = 4**; includes **`run_20260410T153739Z`** (T123 baseline on branch) plus the differentiated **`run_20260410T171258Z`**.
- **T117 / T118:** No edits to rule logic or allowlist; **`run_20260410T171258Z`** evaluation used the locked **`build_first_real_scanner_rule_from_run_folder.py`** on this branch.

---

## Inferred

- **`per_page=10`** yields a **broader** FR “newest” slice than **`per_page=5`**, which directly addresses the T123/T124 concern about **content-duplicate** third runs under the default happy path.
- The first rule **scales mechanically** to ten rows under the same allowlist/recency semantics (more **`meets_first_real_scanner_rule`** rows when more allowlisted types appear).

---

## Unknown

- Whether **`per_page=10`** is **representative** of operator intent long term vs other differentiation (time-lag, other allowed parameters).
- After **#436**, rollup on a full **`git pull`** of **`the-fade-phase1-tranche1-foundation`** should list the same **four** runs if all folders are present.

---

## Run coverage summary

*(From `first_real_scanner_rule_reevidence_summary.json`, `generated_at_utc` **2026-04-10T17:41:53Z**, post-#436.)*

| Run folder | `fetch_url_used` (per_page) | Rows | Eligible | Excluded |
|------------|----------------------------|-----:|---------:|---------:|
| `run_20260408T125708Z` | 5 | 5 | 0 | 5 |
| `run_20260410T143649Z` | 5 | 5 | 4 | 1 |
| `run_20260410T153739Z` | 5 | 5 | 4 | 1 |
| `run_20260410T171258Z` | **10** | **10** | **9** | **1** |

---

## Aggregate reason histogram (rollup, row-level)

| `scanner_rule_reasons` code | Count |
|------------------------------|------:|
| `document_type_not_allowed` | 8 |
| `meets_first_real_scanner_rule` | 17 |

---

## T117 / T118 unchanged (explicit)

- **T117** governance and allowlist were **not** modified in #435.
- **T118** script body was **not** modified; ingress **`_build_query_url`** was **not** changed — only the existing **`--per-page`** CLI argument was set to **10**.
