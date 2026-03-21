"""
Discovery / Intake layer — first-build implementation.

Finds GitHub candidate sources for a query; triages; outputs candidate queue.
First build: GitHub only. Freshness-first ranking.
"""

from discovery.github_search import search_repositories, RepoCandidate
from discovery.candidate_filter import filter_and_dedupe
from discovery.triage_helper import triage_candidates, TriageCandidate
from discovery.queue_writer import write_queue

__all__ = [
    "search_repositories",
    "RepoCandidate",
    "filter_and_dedupe",
    "triage_candidates",
    "TriageCandidate",
    "write_queue",
]
