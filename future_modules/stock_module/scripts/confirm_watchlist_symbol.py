#!/usr/bin/env python3
"""
Stock Module v1 — manual confirm/copy bridge from RS draft watchlist.

Reads the Research Swarm draft watchlist packet, requires the operator to pass
exactly one approved symbol via CLI, verifies the symbol exists in the draft,
and writes a valid Stock Module one-symbol packet for run_research_brief.py.

Manual approval is explicit: the operator must choose the symbol.
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

_SCRIPT_DIR = Path(__file__).resolve().parent
_STOCK_MODULE_ROOT = _SCRIPT_DIR.parent
_DEFAULT_SOURCE = _SCRIPT_DIR.parent.parent / "research_swarm" / "outputs" / "draft_watchlist_packet_from_rs.json"
_DEFAULT_INPUTS_DIR = _STOCK_MODULE_ROOT / "inputs"


def _load_json(path: Path) -> dict:
    """Load and parse JSON. Raises on failure."""
    if not path.exists():
        print(f"Error: File not found: {path}", file=sys.stderr)
        sys.exit(1)
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON: {e}", file=sys.stderr)
        sys.exit(1)
    if not isinstance(data, dict):
        print(f"Error: Expected JSON object, got {type(data).__name__}", file=sys.stderr)
        sys.exit(1)
    return data


def _validate_draft(draft: dict, source_path: Path) -> None:
    """Ensure draft has a non-empty symbols list. Exit on failure."""
    symbols = draft.get("symbols")
    if not isinstance(symbols, list):
        print(f"Error: Source draft has invalid symbols field (expected list): {source_path}", file=sys.stderr)
        sys.exit(1)
    if not symbols:
        print(f"Error: Source draft has no symbols: {source_path}", file=sys.stderr)
        sys.exit(1)
    symbols_str = [str(s).strip().upper() for s in symbols if s]
    if not symbols_str:
        print(f"Error: Source draft symbols are empty: {source_path}", file=sys.stderr)
        sys.exit(1)


def _symbol_in_draft(symbol: str, draft: dict) -> bool:
    """Check if symbol exists in draft (case-insensitive)."""
    symbols = draft.get("symbols", [])
    sym_upper = symbol.strip().upper()
    return sym_upper in [str(s).strip().upper() for s in symbols if s]


def _validate_packet(packet: dict) -> None:
    """Validate packet against watchlist_packet schema. Exit on failure."""
    schema_path = _STOCK_MODULE_ROOT / "schemas" / "watchlist_packet.schema.json"
    if not schema_path.exists():
        print(f"Error: Schema not found: {schema_path}", file=sys.stderr)
        sys.exit(1)
    try:
        import jsonschema
    except ImportError:
        print("Error: jsonschema required. Install with: pip install jsonschema", file=sys.stderr)
        sys.exit(1)
    with open(schema_path, encoding="utf-8") as f:
        schema = json.load(f)
    try:
        jsonschema.validate(instance=packet, schema=schema)
    except jsonschema.ValidationError as e:
        print(f"Error: Output packet validation failed: {e}", file=sys.stderr)
        sys.exit(1)


def _build_confirmed_packet(draft: dict, symbol: str) -> dict:
    """Build one-symbol packet from draft, with manually confirmed provenance."""
    sym_upper = symbol.strip().upper()
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    packet_id = f"sm-confirmed-{sym_upper}-from-rs-draft"
    watch_reason = draft.get("watch_reason") or ""
    if watch_reason:
        watch_reason = watch_reason.rstrip() + " (manually confirmed for first brief; one symbol)"
    else:
        watch_reason = "Manually confirmed from RS draft for first brief."

    packet = {
        "packet_id": packet_id,
        "created_at": now,
        "symbols": [sym_upper],
        "watch_reason": watch_reason,
    }

    for key in ("time_horizon", "risk_tolerance", "notes"):
        if key in draft and draft[key] is not None:
            packet[key] = draft[key]

    if "notes" not in packet or not packet["notes"]:
        packet["notes"] = f"Manually confirmed symbol {sym_upper} from RS draft. Intended for run_research_brief.py first-slice path."
    else:
        packet["notes"] = packet["notes"].rstrip() + f" | Manually confirmed {sym_upper} for first brief."

    return packet


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Confirm one symbol from RS draft watchlist and write a Stock Module one-symbol packet for run_research_brief.py."
    )
    parser.add_argument(
        "--symbol",
        required=True,
        type=str,
        help="Approved symbol to confirm (must exist in draft)",
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=_DEFAULT_SOURCE,
        help="Path to RS draft packet (default: research_swarm/outputs/draft_watchlist_packet_from_rs.json)",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Output path (default: inputs/confirmed_watchlist_packet_<symbol>.json)",
    )
    args = parser.parse_args()

    source_path = args.source.resolve()
    symbol = args.symbol.strip()
    if not symbol:
        print("Error: --symbol must be non-empty.", file=sys.stderr)
        sys.exit(1)

    draft = _load_json(source_path)
    _validate_draft(draft, source_path)

    if not _symbol_in_draft(symbol, draft):
        symbols = draft.get("symbols", [])
        print(f"Error: Symbol '{symbol}' not found in draft. Available: {symbols}", file=sys.stderr)
        sys.exit(1)

    packet = _build_confirmed_packet(draft, symbol)
    _validate_packet(packet)

    if args.out:
        output_path = args.out.resolve()
    else:
        _DEFAULT_INPUTS_DIR.mkdir(parents=True, exist_ok=True)
        output_path = _DEFAULT_INPUTS_DIR / f"confirmed_watchlist_packet_{symbol.lower()}.json"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(packet, f, indent=2, ensure_ascii=False)
    except OSError as e:
        print(f"Error: Failed to write output: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Source: {source_path}")
    print(f"Symbol: {symbol} (manually confirmed)")
    print(f"Output: {output_path}")
    print()
    print("--- MANUAL REVIEW REQUIRED ---")
    print("Review packet before running brief. Next command:")
    try:
        rel = output_path.relative_to(_STOCK_MODULE_ROOT)
        hint = f"../{rel}"
    except ValueError:
        hint = str(output_path)
    print(f"  python run_research_brief.py --packet {hint}")
    print("---")

    return 0


if __name__ == "__main__":
    sys.exit(main())
