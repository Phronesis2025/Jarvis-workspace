#!/usr/bin/env python3
"""T96 mechanical bridge: one UniverseScannerRequest JSON in, one UniverseScannerResult JSON out.

Governed by THE_FADE_T95_FIRST_REQUEST_TO_RESULT_BRIDGE_GOVERNANCE.md.
No network, no scanner, no ranking/selection — placeholder candidate_outputs only.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

try:
    from jsonschema import Draft7Validator
except Exception:
    print(
        "ERROR: jsonschema is required. Install in your local Python environment.",
        file=sys.stderr,
    )
    sys.exit(2)

# first_request_to_result/ -> the_fade/
_THE_FADE_ROOT = Path(__file__).resolve().parents[2]
INPUTS_DIR = _THE_FADE_ROOT / "inputs" / "phase3_universe_scanner_requests"
OUTPUTS_DIR = _THE_FADE_ROOT / "outputs" / "phase3_universe_scanner_results"
SCHEMA_DIR = _THE_FADE_ROOT / "contracts" / "phase3_universe_scanner_io" / "schemas"
REQUEST_SCHEMA_PATH = SCHEMA_DIR / "universe_scanner_request.schema.json"
RESULT_SCHEMA_PATH = SCHEMA_DIR / "universe_scanner_result.schema.json"

OMISSION_LITERAL = "bridge_T95_placeholder_not_a_scan"
OMISSION_OPAQUE = "bridge_T95_placeholder_not_a_scan_opaque_candidate_ref"
OPAQUE_SYMBOL = "BRIDGE_OPAQUE_CANDIDATE_REF"

_MAX_ROOT_RESULT_JSON = 3


def _read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _validator(schema_path: Path) -> Draft7Validator:
    return Draft7Validator(_read_json(schema_path))


def _errors(v: Draft7Validator, data: Any) -> List[str]:
    return [f"{list(e.path)}: {e.message}" for e in sorted(v.iter_errors(data), key=lambda e: e.path)]


def _require_under_inputs(request_path: Path) -> Path:
    req = request_path.resolve()
    base = INPUTS_DIR.resolve()
    try:
        req.relative_to(base)
    except ValueError:
        raise ValueError(f"Request path must be under {base}")
    if not req.is_file():
        raise ValueError(f"Not a file: {req}")
    if req.suffix.lower() != ".json":
        raise ValueError("Request file must be .json")
    if req.parent != base:
        raise ValueError("Request must be root-level under inputs/phase3_universe_scanner_requests/ (not fixtures_invalid/)")
    return req


def _count_root_result_json() -> int:
    if not OUTPUTS_DIR.is_dir():
        return 0
    return len(list(OUTPUTS_DIR.glob("*.json")))


def _build_result(request: Dict[str, Any], produced_at_utc: str) -> Dict[str, Any]:
    symbols = request.get("candidate_symbols")
    if isinstance(symbols, list) and len(symbols) > 0:
        rows = [
            {
                "symbol": str(s),
                "row_status": "deferred",
                "omission_reason": OMISSION_LITERAL,
            }
            for s in symbols
        ]
    else:
        rows = [
            {
                "symbol": OPAQUE_SYMBOL,
                "row_status": "deferred",
                "omission_reason": OMISSION_OPAQUE,
            }
        ]

    return {
        "request_id": request["request_id"],
        "produced_at_utc": produced_at_utc,
        "scanner_status": "pending",
        "contract_version": request["contract_version"],
        "candidate_outputs": rows,
        "warnings": [
            "T96 mechanical bridge output only — not a universe scanner execution.",
        ],
    }


def _output_filename(request_id: str, when: datetime) -> str:
    rid = request_id.replace("-", "")
    ts = when.strftime("%Y%m%dT%H%M%SZ")
    return f"bridge_universe_scanner_result_{rid}_{ts}.json"


def main() -> int:
    p = argparse.ArgumentParser(description="T96 one-request-in one-result-out mechanical bridge.")
    p.add_argument(
        "request_filename",
        help="Filename only (e.g. fr_universe_scanner_request_20260407T143643Z.json) under inputs/phase3_universe_scanner_requests/",
    )
    args = p.parse_args()

    if ".." in args.request_filename or Path(args.request_filename).name != args.request_filename:
        print("ERROR: provide basename only, no path components.", file=sys.stderr)
        return 1

    request_path = _require_under_inputs(INPUTS_DIR / args.request_filename)

    if not REQUEST_SCHEMA_PATH.is_file() or not RESULT_SCHEMA_PATH.is_file():
        print("ERROR: missing schema file(s).", file=sys.stderr)
        return 1

    req_v = _validator(REQUEST_SCHEMA_PATH)
    res_v = _validator(RESULT_SCHEMA_PATH)

    request_data = _read_json(request_path)
    req_errs = _errors(req_v, request_data)
    if req_errs:
        print("ERROR: request failed schema validation:", file=sys.stderr)
        for e in req_errs:
            print(f"  {e}", file=sys.stderr)
        return 1

    existing = _count_root_result_json()
    if existing >= _MAX_ROOT_RESULT_JSON:
        print(
            f"ERROR: Model B cap — outputs root already has {_MAX_ROOT_RESULT_JSON} *.json; cannot add another.",
            file=sys.stderr,
        )
        return 1

    when = datetime.now(timezone.utc)
    produced_at = when.strftime("%Y-%m-%dT%H:%M:%SZ")
    result = _build_result(request_data, produced_at)

    out_errs = _errors(res_v, result)
    if out_errs:
        print("ERROR: built result failed schema validation before write:", file=sys.stderr)
        for e in out_errs:
            print(f"  {e}", file=sys.stderr)
        return 1

    out_name = _output_filename(str(request_data["request_id"]), when)
    out_path = OUTPUTS_DIR / out_name

    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(result, f, indent=2)
        f.write("\n")

    roundtrip = _read_json(out_path)
    rt_errs = _errors(res_v, roundtrip)
    if rt_errs:
        print("ERROR: written result failed schema validation after read-back:", file=sys.stderr)
        for e in rt_errs:
            print(f"  {e}", file=sys.stderr)
        return 1

    print(f"Wrote {out_path.relative_to(_THE_FADE_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
