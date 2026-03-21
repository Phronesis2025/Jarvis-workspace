"""
Content Acquisition Layer — handler registry.

First build: GitHub only. Article deferred (source_intake schema has no article type).
"""

from acquisition.handlers.github_handler import GitHubHandler

_HANDLERS = {
    "github": GitHubHandler(),
}


def get_handler(source_type: str):
    """Get handler for source type. Raises if unsupported."""
    handler = _HANDLERS.get(source_type)
    if handler is None:
        raise ValueError(
            f"Source type '{source_type}' not yet supported. "
            f"First build supports: github only."
        )
    return handler
