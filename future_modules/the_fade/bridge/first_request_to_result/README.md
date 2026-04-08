# First request→result bridge (T96)

**Script:** `build_universe_scanner_result_from_single_request.py`  
**Governance:** `docs/THE_FADE_T95_FIRST_REQUEST_TO_RESULT_BRIDGE_GOVERNANCE.md`

## Run

From repo root:

```bash
python future_modules/the_fade/bridge/first_request_to_result/build_universe_scanner_result_from_single_request.py fr_universe_scanner_request_20260407T143643Z.json
```

- Argument is **basename only** of a file already under `inputs/phase3_universe_scanner_requests/` (root only; not `fixtures_invalid/`).
- Requires `jsonschema`.

## Behavior

- Validates the request against `contracts/phase3_universe_scanner_io/schemas/universe_scanner_request.schema.json`.
- Writes **one** result JSON to `outputs/phase3_universe_scanner_results/` named  
  `bridge_universe_scanner_result_<request_id_no_hyphens>_<produced_at_utc_compact>Z.json`.
- **`scanner_status`:** always `pending`.
- **`candidate_outputs`:** only `deferred` rows; fixed T95 omission literals; no ranking or selection.
- Validates the result in memory before write and again after read-back.
- Refuses to run if the result root already has **3** `*.json` files (Model B cap for that directory).

## Not done here

No HTTP, no scanner, no runtime/orchestration, no lane/registry edits.
