# Source-Backed Operator Review (Factual)

This artifact merges **factual** run-folder data only. It is **not** a scanner decision artifact and **not** a decision engine. It does **not** add recommendations, ranking, or trade ideas.

## Run
- Run folder: `C:\dev\jarvis-workspace\future_modules\the_fade\outputs\local_happy_path_runs\run_20260408T125708Z`
- Run id: `20260408T125708Z`
- Run status: `PASS`
- Started at (UTC): `2026-04-08T12:57:08Z`
- Finished at (UTC): `2026-04-08T12:57:10Z`

## Paths
- Source request path (from run_summary): `C:\dev\jarvis-workspace\future_modules\the_fade\inputs\phase3_universe_scanner_requests\fr_universe_scanner_request_20260408T125709Z.json`
- Source result path (from run_summary): `C:\dev\jarvis-workspace\future_modules\the_fade\outputs\phase3_universe_scanner_results\bridge_universe_scanner_result_913fe5fb96624ff48ff5474871762d10_20260408T125710Z.json`
- Copied request file: `C:\dev\jarvis-workspace\future_modules\the_fade\outputs\local_happy_path_runs\run_20260408T125708Z\fr_universe_scanner_request_20260408T125709Z.json`
- Copied result file: `C:\dev\jarvis-workspace\future_modules\the_fade\outputs\local_happy_path_runs\run_20260408T125708Z\bridge_universe_scanner_result_913fe5fb96624ff48ff5474871762d10_20260408T125710Z.json`
- Prior factual review (T102): `C:\dev\jarvis-workspace\future_modules\the_fade\outputs\local_happy_path_runs\run_20260408T125708Z\operator_review.md`
- Source snapshot (T104): `C:\dev\jarvis-workspace\future_modules\the_fade\outputs\local_happy_path_runs\run_20260408T125708Z\source_snapshot.json`

## Request / contract (from copied request JSON)
- Request id: `913fe5fb-9662-4ff4-8ff5-474871762d10`
- Contract version: `1.0.0`

## Source context (from source_snapshot.json)
- Source name: `Federal Register`
- Universe source ref: `federal_register:documents_api_v1`
- Candidate source packet ref: `federal_register_query:https://www.federalregister.gov/api/v1/documents.json?per_page=5&order=newest`
- Scan policy version: `federal_register_ingress_t89_v1`
- Request as_of_utc (snapshot): `2026-04-08T12:57:09.987991Z`
- Ingress results_count (from `source_snapshot.json` only): `5`

## Result envelope (mechanical; not a scan)
- Scanner status: `pending`
- Produced at (UTC): `2026-04-08T12:57:10Z`
- Candidate outputs count: `1`
- Deferred row count: `1`

## Warnings (from copied result JSON)
- T96 mechanical bridge output only — not a universe scanner execution.

## Explicit statement
This review was built only from `run_summary.json`, copied request/result JSON, `operator_review.md`, and `source_snapshot.json` in this run folder. It is not a scanner output or automated decision.

