# T118 — First real scanner rule (mechanical evaluation)

**Updated:** 2026-04-10T14:00:00+00:00

Single script: `build_first_real_scanner_rule_from_run_folder.py`. Reads **only** `source_records_snapshot.json` inside one completed happy-path run folder (T116 output). Writes **`first_real_scanner_rule_evaluation.json`** in that same folder. **No network.**

Governance: `docs/THE_FADE_T117_FIRST_REAL_SCANNER_RULE_GOVERNANCE.md` and acceptance criteria companion.

## Prerequisite

- Run folder: `future_modules/the_fade/outputs/local_happy_path_runs/run_<YYYYMMDDTHHMMSSZ>/`
- File present: `source_records_snapshot.json` with `artifact_kind` `the_fade_t115_source_records_snapshot_v1` (from T116).

## Run (from repo root)

```bash
python future_modules/the_fade/review/local_run/build_first_real_scanner_rule_from_run_folder.py run_20260408T125708Z
```

Or pass an **absolute** path to the `run_*` directory.

Exit **0** on success (writes JSON); **1** on validation or IO error. Stdout ends with `SUMMARY: PASS` or `SUMMARY: FAIL`.

## Output

- **Path:** `<run_folder>/first_real_scanner_rule_evaluation.json`
- **Content:** `rule_id`, timestamps, run metadata, `eligible_records` / `excluded_records`, closed `scanner_rule_status` / `scanner_rule_reasons`, required non-engine statement. Not a scanner engine; not ranking or selection.

## Scope

One rule (T117 §5), one run folder per invocation, no extra Python entrypoints for this slice.
