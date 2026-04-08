#!/usr/bin/env python3
"""T106 source-backed factual operator review for one completed run folder.

Merges bounded run/pipeline facts with bounded source_snapshot.json fields.
Reads only files inside the run directory. No network, no scanner semantics.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

THE_FADE_ROOT = Path(__file__).resolve().parents[2]
RUNS_ROOT = THE_FADE_ROOT / "outputs" / "local_happy_path_runs"
OUTPUT_NAME = "source_backed_operator_review.md"
OPERATOR_REVIEW_NAME = "operator_review.md"
SNAPSHOT_NAME = "source_snapshot.json"


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


def build_source_backed_review(run_dir: Path) -> Path:
    summary_path = run_dir / "run_summary.json"
    operator_review_path = run_dir / OPERATOR_REVIEW_NAME
    snapshot_path = run_dir / SNAPSHOT_NAME

    if not summary_path.is_file():
        raise ValueError(f"Missing run_summary.json in run folder: {run_dir}")
    if not operator_review_path.is_file():
        raise ValueError(f"Missing {OPERATOR_REVIEW_NAME} in run folder: {run_dir}")
    if not snapshot_path.is_file():
        raise ValueError(f"Missing {SNAPSHOT_NAME} in run folder: {run_dir}")

    request_path = _single_match(run_dir, "fr_universe_scanner_request_*.json", "copied request")
    result_path = _single_match(run_dir, "bridge_universe_scanner_result_*.json", "copied result")
    output_path = run_dir / OUTPUT_NAME

    # Read operator_review.md only to satisfy read boundary; do not reinterpret contents.
    operator_review_path.read_text(encoding="utf-8")

    summary = _read_json(summary_path)
    request = _read_json(request_path)
    result = _read_json(result_path)
    snapshot = _read_json(snapshot_path)

    run_id = str(summary.get("run_id", "UNKNOWN"))
    run_status = str(summary.get("status", "UNKNOWN"))
    started_at = str(summary.get("started_at_utc", "UNKNOWN"))
    finished_at = str(summary.get("finished_at_utc", "UNKNOWN"))
    request_src = str(summary.get("source_request_path", "UNKNOWN"))
    result_src = str(summary.get("source_result_path", "UNKNOWN"))

    request_id = str(request.get("request_id", "UNKNOWN"))
    contract_version = str(request.get("contract_version", "UNKNOWN"))

    scanner_status = str(result.get("scanner_status", "UNKNOWN"))
    candidate_outputs = result.get("candidate_outputs")
    candidate_count = len(candidate_outputs) if isinstance(candidate_outputs, list) else 0
    deferred_count = 0
    if isinstance(candidate_outputs, list):
        for row in candidate_outputs:
            if isinstance(row, dict) and row.get("row_status") == "deferred":
                deferred_count += 1
    warnings = _as_list_of_strings(result.get("warnings"))

    source_name = snapshot.get("source_name")
    source_name_str = str(source_name) if source_name is not None else "UNKNOWN"
    universe_source_ref = str(snapshot.get("universe_source_ref", "UNKNOWN"))
    candidate_source_packet_ref = str(snapshot.get("candidate_source_packet_ref", "UNKNOWN"))
    scan_policy_version = str(snapshot.get("scan_policy_version", "UNKNOWN"))
    as_of_utc = str(snapshot.get("as_of_utc", "UNKNOWN"))
    produced_at = str(result.get("produced_at_utc", "UNKNOWN"))

    rc = snapshot.get("results_count")
    results_count_line = ""
    if isinstance(rc, int):
        results_count_line = f"- Ingress results_count (from `source_snapshot.json` only): `{rc}`\n"

    lines: list[str] = [
        "# Source-Backed Operator Review (Factual)",
        "",
        "This artifact merges **factual** run-folder data only. It is **not** a scanner decision artifact "
        "and **not** a decision engine. It does **not** add recommendations, ranking, or trade ideas.",
        "",
        "## Run",
        f"- Run folder: `{run_dir}`",
        f"- Run id: `{run_id}`",
        f"- Run status: `{run_status}`",
        f"- Started at (UTC): `{started_at}`",
        f"- Finished at (UTC): `{finished_at}`",
        "",
        "## Paths",
        f"- Source request path (from run_summary): `{request_src}`",
        f"- Source result path (from run_summary): `{result_src}`",
        f"- Copied request file: `{request_path}`",
        f"- Copied result file: `{result_path}`",
        f"- Prior factual review (T102): `{operator_review_path}`",
        f"- Source snapshot (T104): `{snapshot_path}`",
        "",
        "## Request / contract (from copied request JSON)",
        f"- Request id: `{request_id}`",
        f"- Contract version: `{contract_version}`",
        "",
        "## Source context (from source_snapshot.json)",
        f"- Source name: `{source_name_str}`",
        f"- Universe source ref: `{universe_source_ref}`",
        f"- Candidate source packet ref: `{candidate_source_packet_ref}`",
        f"- Scan policy version: `{scan_policy_version}`",
        f"- Request as_of_utc (snapshot): `{as_of_utc}`",
    ]
    if results_count_line:
        lines.append(results_count_line.rstrip("\n"))

    lines.extend(
        [
            "",
            "## Result envelope (mechanical; not a scan)",
            f"- Scanner status: `{scanner_status}`",
            f"- Produced at (UTC): `{produced_at}`",
            f"- Candidate outputs count: `{candidate_count}`",
            f"- Deferred row count: `{deferred_count}`",
        ]
    )

    if warnings:
        lines.extend(["", "## Warnings (from copied result JSON)"])
        for w in warnings:
            lines.append(f"- {w}")

    lines.extend(
        [
            "",
            "## Explicit statement",
            "This review was built only from `run_summary.json`, copied request/result JSON, "
            "`operator_review.md`, and `source_snapshot.json` in this run folder. "
            "It is not a scanner output or automated decision.",
            "",
        ]
    )

    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return output_path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build one factual source_backed_operator_review.md from one run folder."
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
        output_path = build_source_backed_review(run_dir)
        print(f"SUMMARY: PASS - wrote review: {output_path}")
        return 0
    except Exception as exc:
        print(f"SUMMARY: FAIL - {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
