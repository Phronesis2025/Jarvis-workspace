"""
Discovery layer — candidate filtering and deduplication.

Filters obvious junk; dedupes by URL.
"""

from discovery.github_search import RepoCandidate


def filter_and_dedupe(candidates: list[RepoCandidate]) -> list[RepoCandidate]:
    """
    Filter and dedupe candidates.

    - Dedupe by source_url
    - Exclude obviously irrelevant (empty description + very low stars)
    - Keep borderline; operator reviews.
    """
    if not candidates:
        return []

    seen: set[str] = set()
    out: list[RepoCandidate] = []
    for c in candidates:
        url = (c.source_url or "").strip().lower()
        if not url or url in seen:
            continue
        seen.add(url)

        # Light filter: skip if no description and 0 stars (likely junk/placeholder)
        if not (c.description or "").strip() and c.stars == 0:
            continue

        out.append(c)

    return out
