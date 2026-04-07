# T87 Offline Contract Validator

## Scope

This tool is the T87 implementation of the T86-governed second slice:
offline validation of existing universe-scanner I/O contract artifacts.

It validates:
- `examples/universe_scanner_request.example.json` against `schemas/universe_scanner_request.schema.json`
- `examples/universe_scanner_result.example.json` against `schemas/universe_scanner_result.schema.json`
- Optional files in `fixtures_invalid/` (if present), expected to fail by reason class.

## Run

From repo root:

```bash
python future_modules/the_fade/contracts/phase3_universe_scanner_io/tools/validate_universe_scanner_io_contracts.py
```

Exit codes:
- `0` = all checks passed
- `1` = validation failure
- `2` = missing local `jsonschema` dependency in current Python env

## Fixture naming (optional)

If you add optional invalid fixtures under `fixtures_invalid/`, keep total fixture count <= 5.
Each filename must include:
- target token: `_request_` or `_result_`
- reason token: one of `_type_`, `_required_`, `_format_`, `_enum_`, `_additionalProperties_`, `_minLength_`, `_pattern_`, `_anyOf_`

Example: `invalid_request_required_missing_request_id.json`

## Boundary (must stay true)

- Local/offline only: no network calls, no providers, no runtime orchestration.
- Read-only for governed contract artifacts: do not edit `schemas/`, `examples/`, `types/`, or contract package `README.md` in this slice.
- No scanner semantics: no request-to-result generation, no scan loop, no scheduling/jobs/workers.
- Single tool surface only: this validator script is the only implementation entrypoint in this slice.
