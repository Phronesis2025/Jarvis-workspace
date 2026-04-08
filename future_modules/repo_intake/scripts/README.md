# Repo Intake Scripts

**Updated:** 2026-04-08

Concise usage for the bounded local repo-intake runtime.

## Commands

Single repo:

`py -3 future_modules/repo_intake/scripts/run_repo_intake.py --input future_modules/repo_intake/inputs/example_repo_intake_input.json`

Batch repo:

`py -3 future_modules/repo_intake/scripts/run_repo_intake_batch.py --input future_modules/repo_intake/inputs/example_repo_intake_batch.json`

## Required input files

- single input shape: `future_modules/repo_intake/contracts/repo_intake_input.schema.json`
- single example input: `future_modules/repo_intake/inputs/example_repo_intake_input.json`
- batch example input (`items` list of single-item shape): `future_modules/repo_intake/inputs/example_repo_intake_batch.json`

## Output locations

- per-repo JSON results: `future_modules/repo_intake/outputs/`
- per-repo markdown reports: `future_modules/repo_intake/reports/`
- batch summary JSON: `future_modules/repo_intake/outputs/`
- batch summary markdown: `future_modules/repo_intake/reports/`

## Batch failure handling

Batch runner continues on error:

- processes all items even if some fail
- records failed item details (`repo_url`, `profile_used` if available, `status=failed`, `error_message`)
- includes total items, success count, and failure count in summary outputs
