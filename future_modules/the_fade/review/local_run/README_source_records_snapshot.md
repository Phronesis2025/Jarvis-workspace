# Run-scoped Federal Register source-record snapshot (T116)

One script: `build_source_records_snapshot_from_run_folder.py`.

## Usage

From repo root (or any cwd):

```bash
python future_modules/the_fade/review/local_run/build_source_records_snapshot_from_run_folder.py run_<YYYYMMDDTHHMMSSZ>
```

Requires in that run folder under `future_modules/the_fade/outputs/local_happy_path_runs/`:

- `source_snapshot.json`
- exactly one `fr_universe_scanner_request_*.json`

Optional: `run_summary.json` (used only for `run_id` when present).

Writes `source_records_snapshot.json` in the same folder. **One** HTTP GET to the Federal Register documents API URL taken only from `candidate_source_packet_ref` in the request JSON. Not scanner output; see artifact `explicit_non_scanner_statement`.

Governance: `docs/THE_FADE_T115_RUN_SCOPED_SOURCE_RECORD_CAPTURE_GOVERNANCE.md` and acceptance criteria sibling doc.
