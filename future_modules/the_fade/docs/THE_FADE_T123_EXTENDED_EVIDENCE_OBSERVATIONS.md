# THE FADE — T123 extended evidence observations

**Prompt #:** 431  
**Label:** `THE_FADE_BUILD_EXTENDED_EVIDENCE_SLICE`  
**Tranche #:** 123 (PATH B — more evidence before any repair)  
**Updated:** 2026-04-10T15:51:13+00:00  

**Recovery (#432):** Slice artifacts were first produced on the wrong git branch; they were **recovered onto `the-fade-phase1-tranche1-foundation`**, and `first_real_scanner_rule_reevidence_summary.json` was **regenerated** with the locked rollup script on this branch so the JSON matches the three-run evidence (same row aggregates as stated below). **T117/T118** script bodies were **not** modified.

**Authority:** Factual extension after locked T120 re-evidence and #429 checkpoint. **No** change to T117/T118 rule logic or allowlist in this slice. Companion rollup: `outputs/local_happy_path_runs/first_real_scanner_rule_reevidence_summary.json` (regenerate via `rollup_first_real_scanner_evaluations_for_reevidence.py`). Baseline T120 human-facing record remains `THE_FADE_T120_REEVIDENCE_OBSERVATIONS.md` (not rewritten here).

---

## Observed

- **Three** qualifying runs under `outputs/local_happy_path_runs/`, each with **`source_records_snapshot.json`** and **`first_real_scanner_rule_evaluation.json`**:
  - `run_20260408T125708Z` (T120 baseline)
  - `run_20260410T143649Z` (T120 baseline)
  - `run_20260410T153739Z` (**new** for T123)
- All three use the same `fetch_url_used`: `https://www.federalregister.gov/api/v1/documents.json?per_page=5&order=newest`.
- **Run 1:** five rows, all FR `type` **`Presidential Document`**; **`eligible_count` = 0**, **`excluded_count` = 5**; reasons **`document_type_not_allowed`** only.
- **Run 2:** mixed types — one **`Presidential Document`** (excluded), one **`Proposed Rule`**, three **`Notice`**; **`eligible_count` = 4**, **`excluded_count` = 1**.
- **Run 3 (new):** **same five `document_number` values and titles as run 2** (same FR “newest five” slice at this capture time): again **4** eligible / **1** excluded with the same type mix and reason pattern as run 2.
- Refreshed `first_real_scanner_rule_reevidence_summary.json`: **`runs_with_source_records_snapshot` = 3**, **`runs_with_first_real_scanner_rule_evaluation` = 3**, **`t120_diversity_gate_satisfied` = true**, aggregate row-level histogram **`document_type_not_allowed`:** 7, **`meets_first_real_scanner_rule`:** 8 (15 rows total).
- **T117/T118 logic:** No edits were made to governed rule semantics; evaluations use the locked **`build_first_real_scanner_rule_from_run_folder.py`** on **`the-fade-phase1-tranche1-foundation`** (#432 branch recovery; see Recovery note above).

---

## Inferred

- Adding a **third** run increases the **row-level** evidence mass and keeps the rollup’s diversity gate **true** on distinct `fetch_timestamp_utc` across runs.
- **Homogeneous vs mixed:** **One of three** runs is **homogeneous** (all Presidential, all type-excluded). **Two of three** are **mixed** allowlisted + Presidential; those two runs are **observationally duplicate slices** (same documents), so diversity across runs is **timestamp/run-folder** diversity more than **distinct FR content** diversity for the third pull.
- The first rule continues to **separate** allowlisted types from Presidential rows when both appear in the same snapshot.

---

## Unknown

- How often a **new** happy-path pull returns a **different** set of five documents vs repeating the same “newest” page while FR listings are stable.
- Whether **three** runs materially reduce uncertainty for operator usefulness vs **two** when two mixed runs are **redundant** content-wise.

---

## Run coverage summary

| Run folder | `source_records_snapshot` | `first_real_scanner_rule_evaluation` | `fetch_timestamp_utc` (snapshot) | Rows | Eligible | Excluded |
|------------|---------------------------|--------------------------------------|-----------------------------------|-----:|---------:|---------:|
| `run_20260408T125708Z` | yes | yes | `2026-04-09T20:19:40Z` | 5 | 0 | 5 |
| `run_20260410T143649Z` | yes | yes | `2026-04-10T14:37:50Z` | 5 | 4 | 1 |
| `run_20260410T153739Z` | yes | yes | `2026-04-10T15:37:49Z` | 5 | 4 | 1 |

---

## Aggregate reason histogram (rollup JSON, row-level)

| `scanner_rule_reasons` code | Count |
|----------------------------|------:|
| `document_type_not_allowed` | 7 |
| `meets_first_real_scanner_rule` | 8 |

---

## Homogeneous vs mixed pulls (explicit)

| Pull pattern | Runs | Notes |
|--------------|-----:|-------|
| **Homogeneous** (single FR `type` across all rows) | 1 | Run 1 — all Presidential Document. |
| **Mixed** (allowlisted types + at least one non-allowlisted) | 2 | Runs 2 and 3 — same underlying five documents in this evidence set. |

---

## T117 / T118 unchanged (explicit)

- **T117** governance text was **not** edited in #431.
- **T118** script body was **not** modified for #431; evaluations rely on the **locked** mechanical rule already governed on the fade foundation branch.
