# Repo Intake Scripts

**Updated:** 2026-04-08

Concise usage for the bounded local repo-intake runtime.

## Commands

Single repo:

`py -3 future_modules/repo_intake/scripts/run_repo_intake.py --input future_modules/repo_intake/inputs/example_repo_intake_input.json`

Batch repo:

`py -3 future_modules/repo_intake/scripts/run_repo_intake_batch.py --input future_modules/repo_intake/inputs/example_repo_intake_batch.json`

TXT batch repo URLs (one GitHub URL per line):

`py -3 future_modules/repo_intake/scripts/run_repo_intake_batch.py --txt future_modules/repo_intake/inputs/example_repo_urls.txt`

## Required input files

- single input shape: `future_modules/repo_intake/contracts/repo_intake_input.schema.json`
- single example input: `future_modules/repo_intake/inputs/example_repo_intake_input.json`
- batch example input (`items` list of single-item shape): `future_modules/repo_intake/inputs/example_repo_intake_batch.json`
- txt example input (one URL per line, `#` comments allowed): `future_modules/repo_intake/inputs/example_repo_urls.txt`

## Output locations

- per-repo JSON results: `future_modules/repo_intake/outputs/` — filenames include `{owner}_{repo}_{profile}_{run_id}_repo_intake_result.json`
- per-repo markdown reports: `future_modules/repo_intake/reports/` — same `run_id` suffix
- single-repo runs: `run_id` is generated per invocation (UTC timestamp token)
- batch runs: all items in a batch share the batch id as `run_id` so artifacts align with that batch’s summary
- each result JSON/report body includes `run_id` for audit
- batch summary JSON: `future_modules/repo_intake/outputs/`
- batch summary markdown: `future_modules/repo_intake/reports/`

## Fetch failures

If GitHub cannot be reached or evidence cannot be fetched:

- classification is `too_fuzzy` (not `reject`)
- `stop_condition` is set (e.g. `repo URL invalid or unreachable`)
- `fetch_evaluation_skipped` is `true`
- batch summaries list these under **Fetch-limited**, separate from evaluated items and from hard errors

## Batch failure handling

Batch runner continues on error:

- processes all items even if some fail
- summary sections: **evaluated** (scored), **fetch-limited** (no evidence), **failed** (exceptions)
- failed rows include `repo_url`, `profile_used` if known, `status=failed`, `error_message`

## Auto profile behavior

- If `profile` is omitted, blank, or set to `auto`, the runner auto-selects one of:
  - `generic_repo_triage`
  - `workflow_tooling`
  - `prediction_market_execution`
- Auto-selection is deterministic and keyword/structure based (no black-box model).
- Strong prediction-market execution signals (for example `polymarket`, `kalshi`, `arbitrage`, `copy-trading`, `orderbook`, `market making`, `positions`, `clob`, `execution`) take precedence over generic workflow terms.
- Result outputs include:
  - `profile_selected_automatically`
  - `auto_profile_confidence`
  - `auto_profile_reasons`
