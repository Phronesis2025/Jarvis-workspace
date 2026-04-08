#!/usr/bin/env python3
"""T102 factual post-run operator review builder.

Reads one governed run folder and writes one operator_review.md
using factual fields already on disk plus simple transparent counts.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


THE_FADE_ROOT = Path(__file__).resolve().parents[2]
RUNS_ROOT = THE_FADE_ROOT / "outputs" / "local_happy_path_runs"
OUTPUT_NAME = "operator_review.md"


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


def _as_list_of_strings(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    out: list[str] = []
    for item in value:
        if isinstance(item, str):
            out.append(item)
    return out


def build_review(run_dir: Path) -> Path:
    summary_path = run_dir / "run_summary.json"
    if not summary_path.is_file():
        raise ValueError(f"Missing run_summary.json in run folder: {run_dir}")

    request_path = _single_match(run_dir, "fr_universe_scanner_request_*.json", "copied request")
    result_path = _single_match(run_dir, "bridge_universe_scanner_result_*.json", "copied result")
    output_path = run_dir / OUTPUT_NAME

    summary = _read_json(summary_path)
    request = _read_json(request_path)
    result = _read_json(result_path)

    run_id = str(summary.get("run_id", "UNKNOWN"))
    run_status = str(summary.get("status", "UNKNOWN"))
    started_at = str(summary.get("started_at_utc", "UNKNOWN"))
    finished_at = str(summary.get("finished_at_utc", "UNKNOWN"))
    request_src = str(summary.get("source_request_path", "UNKNOWN"))
    result_src = str(summary.get("source_result_path", "UNKNOWN"))

    request_id = str(request.get("request_id", "UNKNOWN"))
    contract_version = str(request.get("contract_version", "UNKNOWN"))
    universe_source_ref = str(request.get("universe_source_ref", "UNKNOWN"))
    scan_policy_version = str(request.get("scan_policy_version", "UNKNOWN"))
    candidate_source_packet_ref = str(request.get("candidate_source_packet_ref", "UNKNOWN"))

    scanner_status = str(result.get("scanner_status", "UNKNOWN"))
    candidate_outputs = result.get("candidate_outputs")
    candidate_count = len(candidate_outputs) if isinstance(candidate_outputs, list) else 0
    deferred_count = 0
    if isinstance(candidate_outputs, list):
        for row in candidate_outputs:
            if isinstance(row, dict) and row.get("row_status") == "deferred":
                deferred_count += 1
    warnings = _as_list_of_strings(result.get("warnings"))

    lines: list[str] = [
        "# Operator Review (Factual)",
        "",
        "This artifact is factual post-run review only and is **not** a scanner decision artifact.",
        "",
        "## Run",
        f"- Run folder: `{run_dir}`",
        f"- Run id: `{run_id}`",
        f"- Run status: `{run_status}`",
        f"- Started at (UTC): `{started_at}`",
        f"- Finished at (UTC): `{finished_at}`",
        "",
        "## Paths",
        f"- Source request path: `{request_src}`",
        f"- Source result path: `{result_src}`",
        f"- Copied request file: `{request_path}`",
        f"- Copied result file: `{result_path}`",
        "",
        "## Request Facts",
        f"- Request id: `{request_id}`",
        f"- Contract version: `{contract_version}`",
        f"- Universe source ref: `{universe_source_ref}`",
        f"- Scan policy version: `{scan_policy_version}`",
        f"- Candidate source packet ref: `{candidate_source_packet_ref}`",
        "",
        "## Result Facts",
        f"- Scanner status: `{scanner_status}`",
        f"- Candidate outputs count: `{candidate_count}`",
        f"- Deferred row count: `{deferred_count}`",
    ]

    if warnings:
        lines.extend(["", "## Warnings"])
        for w in warnings:
            lines.append(f"- {w}")

    lines.append("")
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return output_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Build one factual operator review from one run folder.")
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
        output_path = build_review(run_dir)
        print(f"SUMMARY: PASS - wrote review: {output_path}")
        return 0
    except Exception as exc:
        print(f"SUMMARY: FAIL - {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
