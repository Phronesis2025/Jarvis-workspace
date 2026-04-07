# Offline ingress request packet validator

**Script:** `validate_ingress_request_packets.py` (T91)

## What it does

- Validates **every** `*.json` file in the **root** of `future_modules/the_fade/inputs/phase3_universe_scanner_requests/` against `schemas/universe_scanner_request.schema.json` (read-only).
- If `inputs/.../fixtures_invalid/` exists: each `*.json` there must **fail** schema validation; the filename must include `_request_` and a **reason token** (same convention as contract `fixtures_invalid/`, e.g. `_type_`, `_required_`).
- Prints one line per check and **SUMMARY: PASS** or **SUMMARY: FAIL**; exit code **0** or **1**.

## What it does not do

- No writes, no network, no scanner, no result packets.

## Run (from repo root)

```bash
python future_modules/the_fade/contracts/phase3_universe_scanner_io/tools/validate_ingress_request_packets.py
```

## Fixtures in this repo

| File | Expected failure class |
|------|------------------------|
| `fixtures_invalid/fr_request_fixture_type_case.json` | `type` |
| `fixtures_invalid/fr_request_fixture_required_case.json` | `required` |
