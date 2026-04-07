#!/usr/bin/env python3
"""T89 single-source live ingress: Federal Register -> UniverseScannerRequest.

Bounded behavior:
- One read-only fetch from Federal Register documents API.
- Build one request packet only (no result packet).
- Validate packet against T85 request schema before write.
- Write one packet under inputs/phase3_universe_scanner_requests/.
"""

from __future__ import annotations

import argparse
import json
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen

try:
    from jsonschema import Draft7Validator
except Exception:
    print(
        "ERROR: jsonschema dependency is required for schema validation in T89 ingress.",
        file=sys.stderr,
    )
    sys.exit(2)


REPO_ROOT = Path(__file__).resolve().parents[4]
REQUEST_SCHEMA_PATH = (
    REPO_ROOT
    / "future_modules"
    / "the_fade"
    / "contracts"
    / "phase3_universe_scanner_io"
    / "schemas"
    / "universe_scanner_request.schema.json"
)
DEFAULT_OUTPUT_DIR = (
    REPO_ROOT
    / "future_modules"
    / "the_fade"
    / "inputs"
    / "phase3_universe_scanner_requests"
)

FR_BASE_URL = "https://www.federalregister.gov/api/v1/documents.json"
UNIVERSE_SOURCE_REF = "federal_register:documents_api_v1"
SCAN_POLICY_VERSION = "federal_register_ingress_t89_v1"
CONTRACT_VERSION = "1.0.0"


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _utc_iso(dt: datetime) -> str:
    return dt.isoformat().replace("+00:00", "Z")


def _build_query_url(per_page: int) -> str:
    query = urlencode({"per_page": per_page, "order": "newest"})
    return f"{FR_BASE_URL}?{query}"


def _fetch_fr_documents(query_url: str) -> dict:
    with urlopen(query_url, timeout=20) as response:
        if response.status != 200:
            raise RuntimeError(f"Federal Register HTTP status {response.status}")
        return json.loads(response.read().decode("utf-8"))


def _build_request_packet(query_url: str, results_count: int) -> dict:
    now = _utc_now()
    return {
        "request_id": str(uuid.uuid4()),
        "as_of_utc": _utc_iso(now),
        "universe_source_ref": UNIVERSE_SOURCE_REF,
        "contract_version": CONTRACT_VERSION,
        "scan_policy_version": SCAN_POLICY_VERSION,
        "candidate_source_packet_ref": f"federal_register_query:{query_url}",
        "operator_notes": (
            "T89 ingress packet from Federal Register only; "
            f"results_count={results_count}; no scanner execution."
        ),
    }


def _validate_packet(packet: dict) -> None:
    schema = json.loads(REQUEST_SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft7Validator(schema)
    errors = sorted(validator.iter_errors(packet), key=lambda e: list(e.path))
    if errors:
        first = errors[0]
        raise ValueError(
            "Packet failed request schema validation at "
            f"path={list(first.path)} message={first.message}"
        )


def _build_output_path(output_dir: Path, now: datetime) -> Path:
    timestamp = now.strftime("%Y%m%dT%H%M%SZ")
    return output_dir / f"fr_universe_scanner_request_{timestamp}.json"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build one UniverseScannerRequest packet from Federal Register."
    )
    parser.add_argument(
        "--per-page",
        type=int,
        default=5,
        help="Federal Register documents per page (bounded 1..20, default 5).",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Output directory for one request packet.",
    )
    args = parser.parse_args()

    if args.per_page < 1 or args.per_page > 20:
        print("ERROR: --per-page must be in range 1..20", file=sys.stderr)
        return 2

    if not REQUEST_SCHEMA_PATH.exists():
        print(f"ERROR: missing request schema: {REQUEST_SCHEMA_PATH}", file=sys.stderr)
        return 1

    query_url = _build_query_url(args.per_page)
    print(f"INFO: Fetching Federal Register from: {query_url}")

    try:
        payload = _fetch_fr_documents(query_url)
        results = payload.get("results", [])
        results_count = len(results) if isinstance(results, list) else 0
        packet = _build_request_packet(query_url=query_url, results_count=results_count)
        _validate_packet(packet)
    except Exception as exc:
        print(f"FAIL: unable to build schema-valid request packet: {exc}", file=sys.stderr)
        return 1

    args.output_dir.mkdir(parents=True, exist_ok=True)
    output_path = _build_output_path(args.output_dir, _utc_now())
    output_path.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")

    print(f"PASS: wrote one schema-valid request packet: {output_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
