# Offline validation — `UniverseScannerResult` packets (T94)

**Tranche:** 94  
**Script:** `validate_universe_scanner_result_packets.py`

## What it does

- Validates every root-level `*.json` under `future_modules/the_fade/outputs/phase3_universe_scanner_results/` against `schemas/universe_scanner_result.schema.json` (read-only).
- **Empty root:** zero such files → exit **0** with an explicit stdout line (T93 empty-root PASS).
- **Model B:** at most **three** root `*.json` files; more → non-zero exit.
- If `fixtures_invalid/` exists: each `*.json` must be **invalid** for the schema; expected failure **class** is encoded in the filename (see below). At most **five** fixture files.

## What it does **not** do

- No HTTP, sockets, or subprocess calls to remote tools.
- No reads of `UniverseScannerRequest` or `inputs/phase3_universe_scanner_requests/`.
- No writes to result JSON, schemas, or contracts (no `open(..., "w")` on those paths).
- No scanner, request→result pipeline, ranking, or runtime/orchestration.

## Run

From repo root (or any cwd; paths are resolved from the script location):

```bash
python future_modules/the_fade/contracts/phase3_universe_scanner_io/tools/validate_universe_scanner_result_packets.py
```

Requires `jsonschema` in the active Python environment (same as T87/T91 validators).

## Valid root seeds (static / copy-only)

| File | Source |
|------|--------|
| `t94_result_static_seed_contract_example.json` | Copy of `contracts/phase3_universe_scanner_io/examples/universe_scanner_result.example.json` — hand-placed for offline validation only; does not imply scanner execution. |

## Invalid fixtures (`fixtures_invalid/`)

| File | Expected failure class | Intent |
|------|------------------------|--------|
| `fr_result_fixture_type_case.json` | `type` | `request_id` is a number, not a string. |
| `fr_result_fixture_required_case.json` | `required` | Omits required `candidate_outputs`. |
