"""
Discovery layer — candidate queue writer.

Writes triaged candidate queue to JSON.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

from discovery.triage_helper import TriageCandidate


def write_queue(
    candidates: list[TriageCandidate],
    query: str,
    output_path: Path,
) -> None:
    """Write candidate queue JSON."""
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    payload = {
        "query": query,
        "discovered_at": now,
        "source_class": "github",
        "freshness_ranking": "sort=updated desc (most recent first); freshness_signal from pushed_at",
        "candidates": [
            {
                "source_url": c.source_url,
                "source_class": c.source_class,
                "selection_reason": c.selection_reason,
                "priority": c.priority,
                "freshness_signal": c.freshness_signal,
                "metadata": c.metadata,
            }
            for c in candidates
        ],
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
