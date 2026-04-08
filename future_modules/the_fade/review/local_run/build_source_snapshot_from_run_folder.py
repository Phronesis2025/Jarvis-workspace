#!/usr/bin/env python3
"""T104 factual Federal Register source snapshot for one completed run folder.

Reads only bounded files inside a single run directory and writes source_snapshot.json.
No network, no cross-folder reads, no scanner semantics.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

THE_FADE_ROOT = Path(__file__).resolve().parents[2]
RUNS_ROOT = THE_FADE_ROOT / "outputs" / "local_happy_path_runs"
OUTPUT_NAME = "source_snapshot.json"

# T89 ingress writes operator_notes containing "results_count=<n>"; fixed mechanical extract only.
_RESULTS_COUNT_PATTERN = re.compile(r"results_count=(\d+)")


def _read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


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


def _parse_results_count(operator_notes: str | None) -> int | None:
    if not operator_notes or not isinstance(operator_notes, str):
        return None
    m = _RESULTS_COUNT_PATTERN.search(operator_notes)
    if not m:
        return None
    return int(m.group(1))


def build_snapshot(run_dir: Path) -> Path:
    summary_path = run_dir / "run_summary.json"
    if not summary_path.is_file():
        raise ValueError(f"Missing run_summary.json in run folder: {run_dir}")

    request_path = _single_match(run_dir, "fr_universe_scanner_request_*.json", "copied request")
    result_path = _single_match(run_dir, "bridge_universe_scanner_result_*.json", "copied result")
    output_path = run_dir / OUTPUT_NAME

    summary = _read_json(summary_path)
    request = _read_json(request_path)
    result = _read_json(result_path)

    operator_notes = request.get("operator_notes")
    if operator_notes is not None and not isinstance(operator_notes, str):
        operator_notes = str(operator_notes)

    snapshot: dict[str, Any] = {
        "source_name": "Federal Register",
        "universe_source_ref": request.get("universe_source_ref"),
        "candidate_source_packet_ref": request.get("candidate_source_packet_ref"),
        "scan_policy_version": request.get("scan_policy_version"),
        "request_id": request.get("request_id"),
        "contract_version": request.get("contract_version"),
        "as_of_utc": request.get("as_of_utc"),
        "operator_notes": operator_notes,
        "results_count": _parse_results_count(operator_notes),
        "run_linkage": {
            "run_id": summary.get("run_id"),
            "started_at_utc": summary.get("started_at_utc"),
            "finished_at_utc": summary.get("finished_at_utc"),
            "status": summary.get("status"),
        },
        "result_envelope_context_only": {
            "produced_at_utc": result.get("produced_at_utc"),
            "scanner_status": result.get("scanner_status"),
            "note": (
                "Result fields are mechanical bridge/envelope context from the copied result JSON only; "
                "not a universe scanner execution or decision."
            ),
        },
        "explicit_statement": (
            "This artifact is a factual source snapshot derived only from on-disk run-folder files. "
            "It is not a scanner decision artifact, not ranking or scoring, and not a recommendation."
        ),
    }

    output_path.write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")
    return output_path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build one factual Federal Register source_snapshot.json from one run folder."
    )
    parser.add_argument(
        "run_folder",
        help=(
            "Run folder name under outputs/local_happy_path_runs/ (e.g. run_20260408T125708Z) "
            "or absolute path to that folder"
        ),
    )
    args = parser.parse_args()

    try:
        run_dir = _resolve_run_dir(args.run_folder)
        output_path = build_snapshot(run_dir)
        print(f"SUMMARY: PASS - wrote snapshot: {output_path}")
        return 0
    except Exception as exc:
        print(f"SUMMARY: FAIL - {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
