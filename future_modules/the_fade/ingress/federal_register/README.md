# T89 Federal Register ingress (single-slice tool)

## Purpose

Build exactly one `UniverseScannerRequest` packet from one read-only Federal Register API fetch.

Tool path:
- `future_modules/the_fade/ingress/federal_register/build_universe_scanner_request_from_federal_register.py`

## Boundaries

- Single source only: Federal Register documents API.
- Single output only: one request packet under:
  `future_modules/the_fade/inputs/phase3_universe_scanner_requests/`.
- No result packet generation.
- No scanner logic, no request-to-result behavior.
- No provider abstraction, no runtime/scheduler/dashboard surfaces.

## Run

From repo root:

```bash
python future_modules/the_fade/ingress/federal_register/build_universe_scanner_request_from_federal_register.py
```

Optional bounded parameters:

```bash
python future_modules/the_fade/ingress/federal_register/build_universe_scanner_request_from_federal_register.py --per-page 5 --output-dir future_modules/the_fade/inputs/phase3_universe_scanner_requests
```

## Output filename pattern

The script writes one file per run:
- `fr_universe_scanner_request_YYYYMMDDTHHMMSSZ.json`

## Validation

The script validates the packet against:
- `future_modules/the_fade/contracts/phase3_universe_scanner_io/schemas/universe_scanner_request.schema.json`

before writing to disk.
