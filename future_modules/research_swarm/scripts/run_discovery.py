#!/usr/bin/env python3
"""
Discovery / Intake layer — CLI entrypoint.

Finds GitHub candidate sources for a query; triages; writes candidate queue.
First build: GitHub only. Freshness-first ranking (sort=updated, order=desc).
"""

import argparse
import sys
from pathlib import Path
from datetime import datetime, timezone

_SCRIPT_DIR = Path(__file__).resolve().parent
_MODULE_ROOT = _SCRIPT_DIR.parent
_DEFAULT_OUTPUTS = _MODULE_ROOT / "outputs"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Discover GitHub candidate sources for a query. Outputs triaged candidate queue."
    )
    parser.add_argument("--query", "-q", required=True, help="Search query (topic, tool name, etc.)")
    parser.add_argument(
        "--max",
        type=int,
        default=10,
        help="Max candidates (default 10, cap 30)",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Output path (default: outputs/discovery_queue_<run_id>.json)",
    )
    args = parser.parse_args()

    query = args.query.strip()
    if not query:
        print("Error: Query is empty.", file=sys.stderr)
        return 1

    sys.path.insert(0, str(_SCRIPT_DIR))

    try:
        from discovery.github_search import search_repositories
        from discovery.candidate_filter import filter_and_dedupe
        from discovery.triage_helper import triage_candidates
        from discovery.queue_writer import write_queue
    except ImportError as e:
        print(f"Error: Failed to import discovery modules: {e}", file=sys.stderr)
        return 1

    # Search — freshness-first: sort=updated, order=desc
    try:
        raw = search_repositories(
            query=query,
            max_results=args.max,
            sort="updated",
            order="desc",
        )
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    if not raw:
        print("Error: No candidates found. Try a different query or broaden scope.", file=sys.stderr)
        return 1

    # Filter and dedupe
    filtered = filter_and_dedupe(raw)
    if not filtered:
        print("Error: All candidates filtered. No credible results.", file=sys.stderr)
        return 1

    # Triage
    triaged = triage_candidates(filtered)

    # Output path
    if args.out:
        output_path = Path(args.out).resolve()
    else:
        run_id = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
        output_path = _DEFAULT_OUTPUTS / f"discovery_queue_{run_id}.json"

    # Write
    try:
        write_queue(triaged, query, output_path)
    except OSError as e:
        print(f"Error: Failed to write queue: {e}", file=sys.stderr)
        return 1

    print("Success")
    print(f"Query: {query}")
    print(f"Candidates: {len(triaged)}")
    print(f"Queue path: {output_path}")
    print("Freshness ranking: sort=updated, order=desc (most recent first)")
    for i, c in enumerate(triaged[:5]):
        sig = c.freshness_signal or "n/a"
        print(f"  {i+1}. [{c.priority}] {c.source_url} | {sig}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
