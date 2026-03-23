#!/usr/bin/env python3
"""
Stock Module v1 — thin manual pipeline wrapper (one symbol only).

This script is intentionally a wrapper:
- calls `run_research_brief.py` on a confirmed one-symbol watchlist packet
- then calls `run_risk_gate.py` on the produced brief output

No reimplementation of core logic.
No batching.
No live market data.
No trade execution.
"""

import argparse
import subprocess
import sys
from pathlib import Path


_SCRIPT_DIR = Path(__file__).resolve().parent
_STOCK_MODULE_ROOT = _SCRIPT_DIR.parent

_BRIEF_FILENAME_PREFIX = "stock_research_brief_"


def _default_brief_output_path(packet_path: Path) -> Path:
    stem = packet_path.stem
    return _STOCK_MODULE_ROOT / "outputs" / f"{_BRIEF_FILENAME_PREFIX}{stem}.json"


def _default_risk_gate_output_path(brief_path: Path) -> Path:
    stem = brief_path.stem
    if stem.startswith(_BRIEF_FILENAME_PREFIX):
        suffix = stem[len(_BRIEF_FILENAME_PREFIX) :]
    else:
        suffix = stem
    return _STOCK_MODULE_ROOT / "outputs" / f"risk_gate_review_{suffix}.json"


def _run_cmd(cmd: list[str]) -> int:
    """
    Run a command with inherited stdout/stderr so the user sees real errors.
    Returns the subprocess exit code.
    """
    proc = subprocess.run(cmd, cwd=_SCRIPT_DIR)
    return int(proc.returncode)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Thin manual pipeline: watchlist packet -> research brief -> risk gate review."
    )
    parser.add_argument("--packet", required=True, type=Path, help="Path to confirmed one-symbol watchlist packet JSON")
    args = parser.parse_args()

    packet_path = args.packet.expanduser().resolve()
    if not packet_path.exists():
        print(f"Error: Packet not found: {packet_path}", file=sys.stderr)
        sys.exit(1)

    print("--- STOCK MODULE PIPELINE (MANUAL) ---")
    print("One-symbol-only lane; manual review required.")
    print(f"Packet: {packet_path}")

    brief_output_path = _default_brief_output_path(packet_path)
    risk_gate_output_path = _default_risk_gate_output_path(brief_output_path)

    # Step 1: research brief (proven script)
    brief_cmd = [
        sys.executable,
        str(_SCRIPT_DIR / "run_research_brief.py"),
        "--packet",
        str(packet_path),
    ]
    brief_exit = _run_cmd(brief_cmd)
    if brief_exit != 0:
        print(f"Error: run_research_brief.py failed (exit code {brief_exit}).", file=sys.stderr)
        sys.exit(brief_exit)

    if not brief_output_path.exists():
        print(
            f"Error: Expected brief output missing: {brief_output_path}",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"Brief output: {brief_output_path}")

    # Step 2: risk gate (proven script)
    risk_cmd = [
        sys.executable,
        str(_SCRIPT_DIR / "run_risk_gate.py"),
        "--brief",
        str(brief_output_path),
    ]
    risk_exit = _run_cmd(risk_cmd)
    if risk_exit != 0:
        print(f"Error: run_risk_gate.py failed (exit code {risk_exit}).", file=sys.stderr)
        sys.exit(risk_exit)

    if not risk_gate_output_path.exists():
        print(
            f"Error: Expected risk gate output missing: {risk_gate_output_path}",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"Risk gate output: {risk_gate_output_path}")

    print()
    print("--- MANUAL REVIEW REQUIRED ---")
    print("Both the research brief and the risk gate review are advisory flags for a person.")
    print("Not a trading engine. No trade execution.")

    return 0


if __name__ == "__main__":
    sys.exit(main())

