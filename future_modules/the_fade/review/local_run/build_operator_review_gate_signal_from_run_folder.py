#!/usr/bin/env python3
"""T108 mechanical operator review gate signal for one completed run folder.

Reads only JSON inside the run directory. Writes operator_review_gate.json.
Deferred rows: per universe_scanner_result.schema.json, each candidate row uses
key row_status with enum value deferred (on-disk bridge output matches this).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

THE_FADE_ROOT = Path(__file__).resolve().parents[2]
RUNS_ROOT = THE_FADE_ROOT / "outputs" / "local_happy_path_runs"
OUTPUT_NAME = "operator_review_gate.json"

EXPLICIT_NON_SCANNER_STATEMENT = (
    "This artifact is a mechanical operator triage signal derived only from local "
    "run-folder JSON files. It is not a universe scanner execution result and not a "
    "scanner decision artifact."
)
EXPLICIT_NON_TRADING_SIGNAL_STATEMENT = (
    "This artifact is not a trading signal, investment recommendation, or "
    "prioritization of markets or instruments."
)


def _read_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise TypeError("expected JSON object at root")
    return data


def _resolve_run_dir(run_arg: str) -> Path:
    candidate = Path(run_arg)
    if candidate.is_absolute():
        run_dir = candidate
    else:
        run_dir = RUNS_ROOT / run_arg
    run_dir = run_dir.resolve()
    runs_root_resolved = RUNS_ROOT.resolve()
    if run_dir.parent != runs_root_resolved:
        raise ValueError(
            "Run folder must be one direct child under outputs/local_happy_path_runs/"
        )
    if not run_dir.name.startswith("run_"):
        raise ValueError("Run folder name must start with run_")
    if not run_dir.is_dir():
        raise ValueError(f"Run folder not found: {run_dir}")
    return run_dir


def _single_glob_count_paths(run_dir: Path, pattern: str) -> list[Path]:
    return sorted(run_dir.glob(pattern))


def _deferred_count(candidate_outputs: Any) -> int:
    """Count deferred rows per schema: row_status == deferred."""
    if not isinstance(candidate_outputs, list):
        return 0
    n = 0
    for x in candidate_outputs:
        if isinstance(x, dict) and x.get("row_status") == "deferred":
            n += 1
    return n


def build_gate_artifact(run_dir: Path) -> tuple[dict[str, Any], int]:
    """Return (artifact dict, exit_code). exit_code 0 = open gate, 1 = mechanical failure."""
    reasons: list[str] = []
    run_id = run_dir.name.removeprefix("run_") if run_dir.name.startswith("run_") else run_dir.name

    summary_path = run_dir / "run_summary.json"
    snapshot_path = run_dir / "source_snapshot.json"

    summary: dict[str, Any] | None = None
    snapshot: dict[str, Any] | None = None
    request: dict[str, Any] | None = None
    result: dict[str, Any] | None = None

    request_paths = _single_glob_count_paths(run_dir, "fr_universe_scanner_request_*.json")
    result_paths = _single_glob_count_paths(run_dir, "bridge_universe_scanner_result_*.json")

    if not summary_path.is_file():
        reasons.append("missing_run_summary")
    else:
        try:
            summary = _read_json(summary_path)
        except (OSError, json.JSONDecodeError, TypeError, UnicodeDecodeError):
            reasons.append("run_summary_invalid_json")
            summary = None
        else:
            st = summary.get("status")
            if not isinstance(st, str) or st != "PASS":
                reasons.append("run_summary_not_pass")
            rid = summary.get("run_id")
            if isinstance(rid, str) and rid.strip():
                run_id = rid

    if not snapshot_path.is_file():
        reasons.append("missing_source_snapshot")
    else:
        try:
            snapshot = _read_json(snapshot_path)
        except (OSError, json.JSONDecodeError, TypeError, UnicodeDecodeError):
            reasons.append("source_snapshot_invalid_json")
            snapshot = None

    if len(request_paths) != 1:
        reasons.append("request_file_not_exactly_one")
    else:
        try:
            request = _read_json(request_paths[0])
        except (OSError, json.JSONDecodeError, TypeError, UnicodeDecodeError):
            reasons.append("request_invalid_json")

    if len(result_paths) != 1:
        reasons.append("result_file_not_exactly_one")
    else:
        try:
            result = _read_json(result_paths[0])
        except (OSError, json.JSONDecodeError, TypeError, UnicodeDecodeError):
            reasons.append("result_invalid_json")

    scanner_status: str | None = None
    candidate_outputs_count = 0
    deferred = 0

    if result is not None:
        ss = result.get("scanner_status")
        scanner_status = ss if isinstance(ss, str) else None
        if scanner_status != "pending":
            reasons.append("scanner_status_not_pending")

        co = result.get("candidate_outputs")
        if not isinstance(co, list) or len(co) == 0:
            reasons.append("candidate_outputs_missing_or_empty")
        else:
            candidate_outputs_count = len(co)
            deferred = _deferred_count(co)
            if deferred <= 0:
                reasons.append("deferred_count_zero")

    artifact: dict[str, Any] = {
        "run_id": run_id,
        "review_gate_status": "open_for_operator_review",
        "review_gate_reasons": [],
        "explicit_non_scanner_statement": EXPLICIT_NON_SCANNER_STATEMENT,
        "explicit_non_trading_signal_statement": EXPLICIT_NON_TRADING_SIGNAL_STATEMENT,
    }

    if request is not None:
        rid = request.get("request_id")
        if isinstance(rid, str):
            artifact["request_id"] = rid

    if snapshot is not None:
        sn = snapshot.get("source_name")
        if isinstance(sn, str):
            artifact["source_name"] = sn
        rc = snapshot.get("results_count")
        if isinstance(rc, int):
            artifact["results_count"] = rc

    if scanner_status is not None:
        artifact["scanner_status"] = scanner_status

    if candidate_outputs_count or result is not None:
        artifact["candidate_outputs_count"] = candidate_outputs_count
        artifact["deferred_count"] = deferred

    # Dedupe reasons preserving order
    seen: set[str] = set()
    uniq: list[str] = []
    for r in reasons:
        if r not in seen:
            seen.add(r)
            uniq.append(r)

    if uniq:
        artifact["review_gate_status"] = "do_not_open_mechanical_failure"
        artifact["review_gate_reasons"] = uniq
        return artifact, 1

    artifact["review_gate_reasons"] = []
    return artifact, 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Write operator_review_gate.json for one local_happy_path run folder."
    )
    parser.add_argument(
        "run_folder",
        help="Run folder name (e.g. run_20260408T125708Z) or absolute path under local_happy_path_runs/",
    )
    args = parser.parse_args()

    try:
        run_dir = _resolve_run_dir(args.run_folder)
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    artifact, code = build_gate_artifact(run_dir)
    out_path = run_dir / OUTPUT_NAME
    out_path.write_text(
        json.dumps(artifact, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(str(out_path))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
