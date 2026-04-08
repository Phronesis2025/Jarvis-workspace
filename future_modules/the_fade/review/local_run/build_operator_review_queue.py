#!/usr/bin/env python3
"""T110 mechanical local operator review queue from existing run-folder JSON.

Scans only direct run_* children under outputs/local_happy_path_runs/, reads only
operator_review_gate.json and run_summary.json per folder, writes a single
operator_review_queue.json. No network, no pipeline invocation.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

THE_FADE_ROOT = Path(__file__).resolve().parents[2]
RUNS_ROOT = THE_FADE_ROOT / "outputs" / "local_happy_path_runs"
QUEUE_REL_ROOT = "future_modules/the_fade/outputs/local_happy_path_runs"
QUEUE_FILENAME = "operator_review_queue.json"

EXPLICIT_NON_SCANNER_STATEMENT = (
    "This queue is a mechanical index of local run folders and existing "
    "operator_review_gate.json files. It is not a universe scanner execution "
    "result and not a scanner decision artifact."
)
EXPLICIT_NON_TRADING_SIGNAL_STATEMENT = (
    "This queue is not a trading signal, investment recommendation, or "
    "prioritization of markets or instruments."
)

QUEUE_SCHEMA_VERSION = "t109_v1"

_RUN_TS = re.compile(r"^run_(\d{8}T\d{6}Z)$")


def _read_json_object(path: Path) -> dict[str, Any] | None:
    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError, TypeError, UnicodeDecodeError):
        return None
    return data if isinstance(data, dict) else None


def _parse_run_timestamp(folder_name: str) -> str | None:
    m = _RUN_TS.fullmatch(folder_name)
    return m.group(1) if m else None


def _run_folder_paths() -> list[Path]:
    if not RUNS_ROOT.is_dir():
        return []
    out: list[Path] = []
    for p in RUNS_ROOT.iterdir():
        if p.is_dir() and p.name.startswith("run_"):
            out.append(p)
    return out


def _copy_gate_fields(gate: dict[str, Any]) -> dict[str, Any]:
    row: dict[str, Any] = {}
    for key in (
        "run_id",
        "review_gate_status",
        "review_gate_reasons",
        "request_id",
        "source_name",
        "scanner_status",
        "candidate_outputs_count",
        "deferred_count",
    ):
        if key not in gate:
            continue
        val = gate[key]
        if key == "review_gate_reasons" and isinstance(val, list):
            row[key] = val
        elif key in ("candidate_outputs_count", "deferred_count") and isinstance(val, int):
            row[key] = val
        elif key in (
            "run_id",
            "request_id",
            "source_name",
            "scanner_status",
            "review_gate_status",
        ) and isinstance(val, str):
            row[key] = val
    if "results_count" in gate and isinstance(gate["results_count"], int):
        row["results_count"] = gate["results_count"]
    return row


def build_queue_payload() -> dict[str, Any]:
    run_dirs = _run_folder_paths()
    total_run_folders = len(run_dirs)

    missing_operator_review_gate = 0
    rows_with_operator_review_gate = 0
    open_for_operator_review = 0
    do_not_open_mechanical_failure = 0

    # Folders with a parsed gate object (included in `runs` per T110).
    gated: list[tuple[Path, dict[str, Any], bool, str | None]] = []

    for run_dir in run_dirs:
        gate_path = run_dir / "operator_review_gate.json"
        summary_path = run_dir / "run_summary.json"
        gate = _read_json_object(gate_path) if gate_path.is_file() else None
        run_summary_present = summary_path.is_file()
        summary_status: str | None = None
        if run_summary_present:
            summary = _read_json_object(summary_path)
            if summary is not None:
                st = summary.get("status")
                if isinstance(st, str):
                    summary_status = st

        if gate is None:
            missing_operator_review_gate += 1
            continue

        rows_with_operator_review_gate += 1
        st = gate.get("review_gate_status")
        if st == "open_for_operator_review":
            open_for_operator_review += 1
        elif st == "do_not_open_mechanical_failure":
            do_not_open_mechanical_failure += 1

        gated.append((run_dir, gate, run_summary_present, summary_status))

    # Stable sort: parseable timestamps descending, then unparseable names descending.
    parseable: list[tuple[str, tuple[Path, dict[str, Any], bool, str | None]]] = []
    unparseable: list[tuple[Path, dict[str, Any], bool, str | None]] = []
    for item in gated:
        run_dir, gate, rsp, ss = item
        ts = _parse_run_timestamp(run_dir.name)
        if ts is not None:
            parseable.append((ts, item))
        else:
            unparseable.append(item)

    parseable.sort(key=lambda x: x[0], reverse=True)
    unparseable.sort(key=lambda x: x[0].name, reverse=True)
    ordered = [t[1] for t in parseable] + unparseable

    runs: list[dict[str, Any]] = []
    for run_dir, gate, run_summary_present, summary_status in ordered:
        folder_name = run_dir.name
        gate_rel = f"{QUEUE_REL_ROOT}/{folder_name}/operator_review_gate.json"
        folder_rel = f"{QUEUE_REL_ROOT}/{folder_name}"

        row: dict[str, Any] = {
            "run_folder_name": folder_name,
            "operator_review_gate_present": True,
            "run_summary_present": run_summary_present,
            "operator_review_gate_path": gate_rel,
            "run_folder_path": folder_rel,
        }
        row.update(_copy_gate_fields(gate))
        rgs = gate.get("review_gate_status")
        if isinstance(rgs, str):
            row["review_gate_partition"] = rgs
        if summary_status is not None:
            row["run_summary_status"] = summary_status
        runs.append(row)

    return {
        "generated_at_utc": datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z"),
        "queue_schema_version": QUEUE_SCHEMA_VERSION,
        "runs_root_relative": QUEUE_REL_ROOT,
        "counts": {
            "total_run_folders": total_run_folders,
            "rows_with_operator_review_gate": rows_with_operator_review_gate,
            "open_for_operator_review": open_for_operator_review,
            "do_not_open_mechanical_failure": do_not_open_mechanical_failure,
            "missing_operator_review_gate": missing_operator_review_gate,
        },
        "runs": runs,
        "explicit_non_scanner_statement": EXPLICIT_NON_SCANNER_STATEMENT,
        "explicit_non_trading_signal_statement": EXPLICIT_NON_TRADING_SIGNAL_STATEMENT,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Write operator_review_queue.json under local_happy_path_runs."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print JSON to stdout only; do not write the queue file.",
    )
    args = parser.parse_args()

    payload = build_queue_payload()
    text = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"

    if args.dry_run:
        sys.stdout.write(text)
        return 0

    out_path = RUNS_ROOT / QUEUE_FILENAME
    try:
        RUNS_ROOT.mkdir(parents=True, exist_ok=True)
        out_path.write_text(text, encoding="utf-8")
    except OSError as e:
        print(f"error: cannot write {out_path}: {e}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
