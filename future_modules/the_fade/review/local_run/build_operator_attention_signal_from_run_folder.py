#!/usr/bin/env python3
"""T112 mechanical operator attention signal for one completed run folder.

Reads only operator_review_gate.json, source_snapshot.json, and run_summary.json
in that folder. Writes operator_attention_signal.json. No network, no pipeline.
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
OUTPUT_NAME = "operator_attention_signal.json"
SIGNAL_SCHEMA_VERSION = "t111_v1"

_RUN_FOLDER = re.compile(r"^run_\d{8}T\d{6}Z$")

EXPLICIT_NON_SCANNER_STATEMENT = (
    "This artifact is a mechanical operator attention signal derived only from "
    "local run-folder JSON files. It is not a universe scanner execution result "
    "and not a scanner decision artifact."
)
EXPLICIT_NON_TRADING_SIGNAL_STATEMENT = (
    "This artifact is not a trading signal, investment recommendation, or "
    "prioritization of markets or instruments."
)


def _read_json(path: Path) -> Any:
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
        raise ValueError(
            "Run folder must be one direct child under outputs/local_happy_path_runs/"
        )
    if not _RUN_FOLDER.fullmatch(run_dir.name):
        raise ValueError(
            "Run folder basename must match run_<YYYYMMDDTHHMMSSZ> (UTC Zulu suffix)"
        )
    if not run_dir.is_dir():
        raise ValueError(f"Run folder not found: {run_dir}")
    return run_dir


def _run_summary_eval(summary_path: Path) -> tuple[bool, bool]:
    """(run_summary_ok, run_summary_fail) per T111 §4."""
    if not summary_path.is_file():
        return True, False
    try:
        data = _read_json(summary_path)
    except (OSError, json.JSONDecodeError, TypeError, UnicodeDecodeError):
        return False, True
    if not isinstance(data, dict):
        return False, True
    st = data.get("status")
    if isinstance(st, str) and st == "PASS":
        return True, False
    return False, True


def _load_optional_object(path: Path) -> dict[str, Any] | None:
    if not path.is_file():
        return None
    try:
        data = _read_json(path)
    except (OSError, json.JSONDecodeError, TypeError, UnicodeDecodeError):
        return None
    return data if isinstance(data, dict) else None


def _effective_results_count(
    snapshot: dict[str, Any] | None, gate: dict[str, Any]
) -> int | None:
    if snapshot is not None and isinstance(snapshot.get("results_count"), int):
        return snapshot["results_count"]
    if isinstance(gate.get("results_count"), int):
        return gate["results_count"]
    return None


def _copy_gate_fields(gate: dict[str, Any]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key in (
        "run_id",
        "request_id",
        "source_name",
        "review_gate_status",
        "candidate_outputs_count",
        "deferred_count",
    ):
        if key not in gate:
            continue
        val = gate[key]
        if key in ("candidate_outputs_count", "deferred_count") and isinstance(val, int):
            out[key] = val
        elif key in (
            "run_id",
            "request_id",
            "source_name",
            "review_gate_status",
        ) and isinstance(val, str):
            out[key] = val
    return out


def _dedupe_sorted_reasons(codes: list[str]) -> list[str]:
    return sorted(set(codes))


def compute_attention(
    gate: dict[str, Any] | None,
    gate_state: str,
    snapshot: dict[str, Any] | None,
    run_summary_ok: bool,
    run_summary_fail: bool,
) -> tuple[str, list[str]]:
    """Return (operator_attention_status, operator_attention_reasons)."""
    if gate_state == "missing":
        return "do_not_elevate_mechanical_failure", ["missing_operator_review_gate"]
    if gate_state == "invalid":
        return "do_not_elevate_mechanical_failure", ["operator_review_gate_invalid_json"]

    assert gate is not None
    rgs = gate.get("review_gate_status")
    if rgs == "do_not_open_mechanical_failure":
        return "do_not_elevate_mechanical_failure", ["review_gate_do_not_open"]
    if run_summary_fail:
        return "do_not_elevate_mechanical_failure", ["run_summary_not_pass"]

    if rgs != "open_for_operator_review" or not run_summary_ok:
        return "do_not_elevate_mechanical_failure", ["operator_review_gate_invalid_json"]

    rc = _effective_results_count(snapshot, gate)
    dc = gate.get("deferred_count")
    deferred_ok = isinstance(dc, int) and dc > 0
    results_ok = isinstance(rc, int) and rc > 0
    elevated = deferred_ok or results_ok

    if elevated:
        reasons: list[str] = []
        if deferred_ok:
            reasons.append("elevated_deferred_rows_present")
        if results_ok:
            reasons.append("elevated_snapshot_results_count_positive")
        return "elevated_manual_attention", _dedupe_sorted_reasons(reasons)

    return "standard_manual_attention", ["standard_open_no_elevation_triggers"]


def build_signal_payload(run_dir: Path) -> dict[str, Any]:
    gate_path = run_dir / "operator_review_gate.json"
    snapshot_path = run_dir / "source_snapshot.json"
    summary_path = run_dir / "run_summary.json"

    gate: dict[str, Any] | None = None
    gate_state: str
    if not gate_path.is_file():
        gate_state = "missing"
    else:
        try:
            raw = _read_json(gate_path)
        except (OSError, json.JSONDecodeError, TypeError, UnicodeDecodeError):
            gate_state = "invalid"
        else:
            if isinstance(raw, dict):
                gate = raw
                gate_state = "ok"
            else:
                gate_state = "invalid"

    snapshot = _load_optional_object(snapshot_path)
    run_summary_ok, run_summary_fail = _run_summary_eval(summary_path)

    status, reasons = compute_attention(
        gate, gate_state, snapshot, run_summary_ok, run_summary_fail
    )

    payload: dict[str, Any] = {
        "generated_at_utc": datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z"),
        "signal_schema_version": SIGNAL_SCHEMA_VERSION,
        "run_folder_name": run_dir.name,
        "operator_attention_status": status,
        "operator_attention_reasons": reasons,
        "explicit_non_scanner_statement": EXPLICIT_NON_SCANNER_STATEMENT,
        "explicit_non_trading_signal_statement": EXPLICIT_NON_TRADING_SIGNAL_STATEMENT,
    }

    if gate is not None:
        payload.update(_copy_gate_fields(gate))
        rc = _effective_results_count(snapshot, gate)
        if rc is not None:
            payload["results_count"] = rc

    return payload


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Write operator_attention_signal.json for one local_happy_path run folder."
    )
    parser.add_argument(
        "run_folder",
        help="Basename run_<YYYYMMDDTHHMMSSZ> or path under local_happy_path_runs",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print JSON to stdout only; do not write the signal file.",
    )
    args = parser.parse_args()

    try:
        run_dir = _resolve_run_dir(args.run_folder)
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1

    payload = build_signal_payload(run_dir)
    text = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"

    if args.dry_run:
        sys.stdout.write(text)
        return 0

    out_path = run_dir / OUTPUT_NAME
    try:
        out_path.write_text(text, encoding="utf-8")
    except OSError as e:
        print(f"error: cannot write {out_path}: {e}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
