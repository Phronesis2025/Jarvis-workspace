"""
Discovery layer — triage helper.

Assigns priority and selection_reason. Freshness-first ranking.
"""

from dataclasses import dataclass

from discovery.github_search import RepoCandidate


@dataclass
class TriageCandidate:
    """Candidate with triage metadata."""

    source_url: str
    source_class: str
    selection_reason: str
    priority: str  # high | medium | low
    freshness_signal: str | None
    metadata: dict


def triage_candidates(candidates: list[RepoCandidate]) -> list[TriageCandidate]:
    """
    Triage candidates: assign priority and selection_reason.

    Freshness-first: candidates are assumed pre-sorted by pushed_at/updated desc.
    First items get higher priority when relevance is comparable.
    """
    out: list[TriageCandidate] = []
    for i, c in enumerate(candidates):
        # Priority: top 3 = high, next 4 = medium, rest = low
        if i < 3:
            priority = "high"
        elif i < 7:
            priority = "medium"
        else:
            priority = "low"

        # Freshness signal from pushed_at (preferred) or updated_at
        freshness = c.pushed_at or c.updated_at
        freshness_signal = f"pushed_at: {freshness}" if freshness else None

        # Selection reason: include freshness when available
        reason_parts = ["Matches query"]
        if c.stars > 100:
            reason_parts.append("notable stars")
        if freshness:
            reason_parts.append("recently updated")
        reason_parts.append("README likely")
        selection_reason = "; ".join(reason_parts)

        metadata = {
            "full_name": c.full_name,
            "description": c.description or "",
            "stars": c.stars,
            "language": c.language,
            "pushed_at": c.pushed_at,
            "updated_at": c.updated_at,
        }

        out.append(
            TriageCandidate(
                source_url=c.source_url,
                source_class="github",
                selection_reason=selection_reason,
                priority=priority,
                freshness_signal=freshness_signal,
                metadata=metadata,
            )
        )

    return out
