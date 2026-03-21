#!/usr/bin/env python3
"""
Extractor API v1 — CLI entry point for API-assisted extraction.

Reads source packet, calls extractor API, validates output, writes extraction report.
Manual review required before evaluator step.
"""

import argparse
import json
import sys
from pathlib import Path

# Resolve script location for imports
_SCRIPT_DIR = Path(__file__).resolve().parent


def _load_packet(path: Path) -> dict:
    """Load and parse packet JSON. Raises on failure."""
    if not path.exists():
        print(f"Error: Packet file not found: {path}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in packet file: {e}", file=sys.stderr)
        sys.exit(1)

    if not isinstance(data, dict):
        print(f"Error: Packet must be a JSON object, got {type(data).__name__}", file=sys.stderr)
        sys.exit(1)

    required = ["packet_id", "source_url", "source_type", "raw_content", "created_at"]
    for field in required:
        if field not in data:
            print(f"Error: Packet missing required field: {field}", file=sys.stderr)
            sys.exit(1)

    if not data.get("raw_content", "").strip():
        print("Error: Packet raw_content is missing or blank", file=sys.stderr)
        sys.exit(1)

    return data


def _default_output_path(packet_path: Path) -> Path:
    """Derive default output path alongside packet."""
    stem = packet_path.stem
    if stem.startswith("source_packet_"):
        suffix = stem.replace("source_packet_", "", 1)
        name = f"extraction_report_{suffix}_api.json"
    else:
        name = f"extraction_report_{stem}_api.json"
    return packet_path.parent / name


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run Extractor API v1 on a source packet. Output requires manual review."
    )
    parser.add_argument(
        "--packet",
        required=True,
        type=Path,
        help="Path to source packet JSON file",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output path for extraction report (default: alongside packet, extraction_report_*_api.json)",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="gpt-4o-mini",
        help="OpenAI model name (default: gpt-4o-mini)",
    )
    args = parser.parse_args()

    packet_path = args.packet.resolve()
    output_path = args.output.resolve() if args.output else _default_output_path(packet_path)
    model = args.model
    if not model or not str(model).strip():
        print("Error: model must be non-empty (e.g. --model gpt-4o-mini)", file=sys.stderr)
        sys.exit(1)
    model = model.strip()

    print(f"Packet path: {packet_path}")

    packet = _load_packet(packet_path)
    source_url = packet.get("source_url", "")
    print(f"Source URL: {source_url}")
    print(f"Model: {model}")

    # Import client and validator (late import for clear error messages)
    sys.path.insert(0, str(_SCRIPT_DIR))
    try:
        from extractor_api_client import generate_extraction
        from extractor_api_validate import validate_extraction_report
    except ImportError as e:
        print(f"Error: Failed to import extractor modules: {e}", file=sys.stderr)
        sys.exit(1)

    # Generate extraction
    try:
        result = generate_extraction(packet, model)
    except (ValueError, RuntimeError, ImportError) as e:
        print(f"Error: Extractor API call failed: {e}", file=sys.stderr)
        sys.exit(1)

    # Validate (catch only schema validation failure; let unexpected errors propagate)
    import jsonschema
    try:
        validate_extraction_report(result)
        print("Validation: PASS")
    except jsonschema.ValidationError as e:
        print(f"Error: Schema validation failed (model output does not conform to extraction_report schema): {e}", file=sys.stderr)
        sys.exit(1)

    # Write output
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        print(f"Output path: {output_path}")
    except OSError as e:
        print(f"Error: Failed to write output: {e}", file=sys.stderr)
        sys.exit(1)

    print()
    print("--- MANUAL REVIEW REQUIRED ---")
    print("Review extraction report using EXTRACTOR_API_REVIEW_GATE.md.")
    print("Do NOT proceed to evaluator until review passes.")
    print("Next step: manual review")
    print("---")

    return 0


if __name__ == "__main__":
    sys.exit(main())
