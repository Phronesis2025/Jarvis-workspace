# Repo Intake

**Updated:** 2026-04-08  
**Status:** Implemented v1 triage tool (bounded, local, operator-support)  
**Purpose:** Bounded repo-intake / triage tooling for reviewing GitHub repositories and deciding whether they are worth deeper investigation. This remains workflow / operator tooling, not active Jarvis core runtime.

## What it can do now

- Run single-repo bounded static triage against supported profiles
- Run batch triage across multiple repos in one command
- Run batch triage directly from a plain `.txt` list of GitHub URLs
- Write per-repo machine-readable JSON outputs and markdown reports
- Write batch summary JSON + markdown grouped by classification
- Continue batch processing even when one or more batch items fail
- Audit-safe outputs: each run uses a `run_id`; batch runs share the batch id in per-repo filenames so runs do not overwrite each other
- Fetch failures are reported as `too_fuzzy` with an explicit stop condition (not a bogus `reject`)

## What it cannot do yet

- Deep-review runtime execution flow
- Repo cloning or target-repo code execution
- Dashboard, API, or server surface
- Async/concurrent batch execution
- Unbounded web/repo crawling

## Run commands

Single repo:

`py -3 future_modules/repo_intake/scripts/run_repo_intake.py --input future_modules/repo_intake/inputs/example_repo_intake_input.json`

Batch repo:

`py -3 future_modules/repo_intake/scripts/run_repo_intake_batch.py --input future_modules/repo_intake/inputs/example_repo_intake_batch.json`

Batch from `.txt` URLs:

`py -3 future_modules/repo_intake/scripts/run_repo_intake_batch.py --txt future_modules/repo_intake/inputs/example_repo_urls.txt`

Auto profile behavior:

- `profile` omitted/blank/`auto` triggers deterministic auto-selection
- output records chosen profile, confidence, and reasons

## Structure

- `docs/` — design-lock and future human-readable notes
- `contracts/` — machine-readable profile/scoring contract
- `inputs/` — intake input files (single and batch)
- `outputs/` — machine-readable triage results and batch summaries
- `scripts/` — local bounded tooling scripts
- `reports/` — human-readable triage and batch reports
