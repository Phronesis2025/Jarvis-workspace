#!/usr/bin/env python3
"""
Content Acquisition Layer — CLI entrypoint.

Accepts source URL, acquires content, writes normalized source packet.
First build: GitHub only. Article deferred (source_intake schema alignment).
"""

import argparse
import sys
from pathlib import Path

# Resolve script dir for imports
_SCRIPT_DIR = Path(__file__).resolve().parent
_MODULE_ROOT = _SCRIPT_DIR.parent
_DEFAULT_OUTPUTS = _MODULE_ROOT / "outputs"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Acquire content from a chosen source and produce a normalized source packet."
    )
    parser.add_argument("--url", required=True, help="Source URL")
    parser.add_argument(
        "--type",
        choices=["github"],
        default=None,
        help="Source type (default: infer from URL). First build: github only.",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Output path (default: outputs/source_packet_<run_id>.json)",
    )
    args = parser.parse_args()

    url = args.url.strip()
    if not url:
        print("Error: URL is empty.", file=sys.stderr)
        return 1

    # Add scripts to path for acquisition imports
    sys.path.insert(0, str(_SCRIPT_DIR))

    try:
        from acquisition.source_classifier import classify_from_url, is_supported
        from acquisition.handlers import get_handler
        from acquisition.packet_builder import build_packet, write_packet
        from acquisition.validate_packet import validate_packet
        from acquisition.packet_builder import _generate_run_id
    except ImportError as e:
        print(f"Error: Failed to import acquisition modules: {e}", file=sys.stderr)
        print("Ensure you are running from future_modules/research_swarm/ or jarvis-workspace.", file=sys.stderr)
        return 1

    # Determine source type
    source_type = args.type
    if not source_type:
        try:
            source_type = classify_from_url(url)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1

    if not is_supported(source_type):
        print(f"Error: Source type '{source_type}' not yet supported. First build: github only.", file=sys.stderr)
        return 1

    # Fetch
    try:
        handler = get_handler(source_type)
        result = handler.fetch(url)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: Acquisition failed: {e}", file=sys.stderr)
        return 1

    # Build packet
    try:
        packet = build_packet(
            source_url=url,
            source_type=source_type,
            raw_content=result.raw_content,
            metadata=result.metadata,
            raw_content_format=result.raw_content_format,
            handler_hint=result.handler_hint,
        )
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    # Validate
    errors = validate_packet(packet)
    if errors:
        for err in errors:
            print(f"Error: {err}", file=sys.stderr)
        return 1

    # Output path
    if args.out:
        output_path = Path(args.out).resolve()
    else:
        run_id = _generate_run_id()
        output_path = _DEFAULT_OUTPUTS / f"source_packet_{run_id}.json"

    # Write
    try:
        write_packet(packet, output_path)
    except OSError as e:
        print(f"Error: Failed to write packet: {e}", file=sys.stderr)
        return 1

    print("Success")
    print(f"Packet path: {output_path}")
    print(f"Content completeness: {packet['content_completeness']}")
    print(f"Raw content length: {len(packet['raw_content'])} chars")

    return 0


if __name__ == "__main__":
    sys.exit(main())
