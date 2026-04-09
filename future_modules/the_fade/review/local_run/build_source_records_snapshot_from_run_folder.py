#!/usr/bin/env python3
"""T116 run-scoped Federal Register source-record snapshot for one completed run folder.

Reads source_snapshot.json + one fr_universe_scanner_request_*.json (+ optional run_summary.json),
performs exactly one bounded GET to the Federal Register documents API URL from the request packet,
writes source_records_snapshot.json in the same run folder. No scanner semantics; no second fetch.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

THE_FADE_ROOT = Path(__file__).resolve().parents[2]
RUNS_ROOT = THE_FADE_ROOT / "outputs" / "local_happy_path_runs"
OUTPUT_NAME = "source_records_snapshot.json"
SOURCE_SNAPSHOT_NAME = "source_snapshot.json"

# Only these keys may be copied from each API results[] item (factual only).
_ALLOWED_RESULT_KEYS = frozenset(
    {
        "document_number",
        "publication_date",
        "title",
        "type",
        "document_type",
        "html_url",
        "pdf_url",
        "abstract",
        "agencies",
    }
)

_ABSTRACT_MAX_LEN = 4000
_MAX_RECORDS = 50

_EXPLICIT_NON_SCANNER = (
    "This is a factual Federal Register source-record snapshot for one local run folder. "
    "It is not scanner output, not ranking or scoring, not selection, and not a recommendation."
)

_USER_AGENT = "JarvisTHEFADE-T116-source-records-snapshot/1.0 (+local operator run)"


def _read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        raw = json.load(f)
    if not isinstance(raw, dict):
        raise ValueError(f"Expected JSON object in {path}")
    return raw


def _resolve_run_dir(run_arg: str) -> Path:
    candidate = Path(run_arg)
    if candidate.is_absolute():
        run_dir = candidate
    else:
        run_dir = RUNS_ROOT / run_arg
    run_dir = run_dir.resolve()
    runs_root_resolved = RUNS_ROOT.resolve()
    if run_dir.parent != runs_root_resolved:
        raise ValueError("Run folder must be one direct child under outputs/local_happy_path_runs/")
    if not run_dir.name.startswith("run_"):
        raise ValueError("Run folder name must start with run_")
    if not run_dir.is_dir():
        raise ValueError(f"Run folder not found: {run_dir}")
    return run_dir


def _single_match(run_dir: Path, pattern: str, label: str) -> Path:
    matches = sorted(run_dir.glob(pattern))
    if len(matches) != 1:
        raise ValueError(
            f"Expected exactly one {label} file in run folder for pattern '{pattern}', found {len(matches)}"
        )
    return matches[0]


def _derive_fetch_url(candidate_source_packet_ref: Any) -> str:
    if not isinstance(candidate_source_packet_ref, str) or not candidate_source_packet_ref.strip():
        raise ValueError("candidate_source_packet_ref must be a non-empty string in request JSON")
    s = candidate_source_packet_ref.strip()
    if s.startswith("federal_register_query:"):
        s = s[len("federal_register_query:") :].strip()
    parsed = urlparse(s)
    if parsed.scheme != "https":
        raise ValueError("Fetch URL must use https")
    host = (parsed.hostname or "").lower()
    if host != "www.federalregister.gov":
        raise ValueError(f"Fetch URL host must be www.federalregister.gov, got {parsed.hostname!r}")
    if parsed.path != "/api/v1/documents.json":
        raise ValueError(f"Fetch URL path must be /api/v1/documents.json, got {parsed.path!r}")
    return s


def _utc_timestamp() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).strftime("%Y-%m-%dT%H:%M:%SZ")


def _one_get(url: str) -> tuple[dict[str, Any], int]:
    req = Request(url, headers={"User-Agent": _USER_AGENT}, method="GET")
    with urlopen(req, timeout=60) as resp:
        status = getattr(resp, "status", 200)
        if status != 200:
            raise ValueError(f"Unexpected HTTP status {status}")
        body = resp.read().decode("utf-8")
    data = json.loads(body)
    if not isinstance(data, dict):
        raise ValueError("Federal Register API response must be a JSON object")
    return data, int(status)


def _sanitize_record(raw: dict[str, Any]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key in _ALLOWED_RESULT_KEYS:
        if key not in raw:
            continue
        val = raw[key]
        if key == "abstract" and isinstance(val, str) and len(val) > _ABSTRACT_MAX_LEN:
            out[key] = val[:_ABSTRACT_MAX_LEN]
            out["truncated"] = True
        else:
            out[key] = val
    return out


def build_source_records_snapshot(run_dir: Path) -> Path:
    snap_path = run_dir / SOURCE_SNAPSHOT_NAME
    if not snap_path.is_file():
        raise ValueError(f"Missing {SOURCE_SNAPSHOT_NAME} in run folder: {run_dir}")

    _read_json(snap_path)  # required presence + JSON object

    request_path = _single_match(run_dir, "fr_universe_scanner_request_*.json", "copied request")
    request = _read_json(request_path)
    ref = request.get("candidate_source_packet_ref")
    fetch_url = _derive_fetch_url(ref)

    run_id: str | None = None
    summary_path = run_dir / "run_summary.json"
    if summary_path.is_file():
        summary = _read_json(summary_path)
        rid = summary.get("run_id")
        if rid is not None and isinstance(rid, str):
            run_id = rid
        elif rid is not None:
            run_id = str(rid)

    try:
        api_json, http_status = _one_get(fetch_url)
    except HTTPError as e:
        raise ValueError(f"HTTP error from Federal Register API: {e.code} {e.reason}") from e
    except URLError as e:
        raise ValueError(f"Network error fetching Federal Register API: {e.reason}") from e
    except json.JSONDecodeError as e:
        raise ValueError("Federal Register API returned non-JSON body") from e

    results = api_json.get("results")
    if not isinstance(results, list):
        raise ValueError("Federal Register API JSON missing results array")

    fetch_ts = _utc_timestamp()
    full_len = len(results)
    truncated_list = full_len > _MAX_RECORDS
    slice_results = results[:_MAX_RECORDS]

    source_records = []
    for item in slice_results:
        if isinstance(item, dict):
            source_records.append(_sanitize_record(item))
        else:
            source_records.append({})

    meta: dict[str, Any] = {
        "results_length": full_len,
        "http_status": http_status,
    }
    for optional_key in ("count", "total_pages", "page"):
        if optional_key in api_json and isinstance(
            api_json[optional_key], (int, str, type(None))
        ):
            meta[optional_key] = api_json[optional_key]

    out_doc: dict[str, Any] = {
        "artifact_kind": "the_fade_t115_source_records_snapshot_v1",
        "source_name": "Federal Register",
        "run_folder_name": run_dir.name,
        "run_id": run_id,
        "request_id": request.get("request_id"),
        "candidate_source_packet_ref": ref,
        "fetch_url_used": fetch_url,
        "fetch_timestamp_utc": fetch_ts,
        "api_response_metadata": meta,
        "source_records": source_records,
        "explicit_non_scanner_statement": _EXPLICIT_NON_SCANNER,
    }
    if truncated_list:
        out_doc["source_records_truncated"] = True

    output_path = run_dir / OUTPUT_NAME
    output_path.write_text(json.dumps(out_doc, indent=2) + "\n", encoding="utf-8")
    return output_path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build one factual source_records_snapshot.json from one run folder (one Federal Register GET)."
    )
    parser.add_argument(
        "run_folder",
        help=(
            "Run folder under outputs/local_happy_path_runs/ (e.g. run_20260408T125708Z) "
            "or absolute path to that folder"
        ),
    )
    args = parser.parse_args()

    try:
        run_dir = _resolve_run_dir(args.run_folder)
        output_path = build_source_records_snapshot(run_dir)
        print(f"SUMMARY: PASS - wrote {output_path}")
        return 0
    except Exception as exc:
        print(f"SUMMARY: FAIL - {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
