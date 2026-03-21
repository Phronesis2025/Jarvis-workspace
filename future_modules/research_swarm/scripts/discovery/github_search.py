"""
Discovery layer — GitHub repository search.

Uses GitHub Search API. Freshness-first: sorts by pushed_at descending.
No auth required (10 req/min limit for search).
"""

import json
from dataclasses import dataclass
from urllib.parse import quote_plus
from urllib.error import HTTPError
from urllib.request import Request, urlopen


@dataclass
class RepoCandidate:
    """Raw candidate from GitHub search."""

    source_url: str
    full_name: str
    description: str | None
    pushed_at: str | None
    updated_at: str | None
    stars: int
    language: str | None


def search_repositories(
    query: str,
    max_results: int = 10,
    sort: str = "updated",  # updated | stars | created
    order: str = "desc",
) -> list[RepoCandidate]:
    """
    Search GitHub repositories. Freshness-first: default sort=updated, order=desc.

    Args:
        query: Search query (topic, tool name, etc.).
        max_results: Max repos to return (cap 30 for first build).
        sort: updated (default, freshness) | stars | created
        order: desc (default) | asc

    Returns:
        List of RepoCandidate, ordered by sort/order.

    Raises:
        ValueError: On API error, rate limit, or empty/invalid response.
    """
    query = (query or "").strip()
    if not query:
        raise ValueError("Search query is empty.")

    max_results = min(max(max_results, 1), 30)

    # GitHub Search API: /search/repositories
    url = (
        f"https://api.github.com/search/repositories"
        f"?q={quote_plus(query)}"
        f"&sort={sort}"
        f"&order={order}"
        f"&per_page={max_results}"
    )

    req = Request(url, headers={"Accept": "application/vnd.github.v3+json", "User-Agent": "ResearchSwarm/1.0"})

    try:
        with urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8", errors="replace"))
    except HTTPError as e:
        if e.code == 403:
            raise ValueError(
                "GitHub API rate limit (403). Unauthenticated search: 10 req/min. "
                "Retry later or use GITHUB_TOKEN for higher limit."
            ) from e
        raise ValueError(f"GitHub search failed: HTTP {e.code}") from e
    except Exception as e:
        raise ValueError(f"GitHub search failed: {e}") from e

    if not isinstance(data, dict) or "items" not in data:
        raise ValueError("GitHub API returned unexpected response.")

    items = data.get("items", [])
    if not items:
        return []

    candidates = []
    for item in items:
        if not isinstance(item, dict):
            continue
        full_name = item.get("full_name") or item.get("name", "")
        if not full_name:
            continue
        html_url = item.get("html_url") or f"https://github.com/{full_name}"
        candidates.append(
            RepoCandidate(
                source_url=html_url,
                full_name=full_name,
                description=item.get("description") or None,
                pushed_at=item.get("pushed_at"),
                updated_at=item.get("updated_at"),
                stars=item.get("stargazers_count") or 0,
                language=item.get("language"),
            )
        )

    return candidates
