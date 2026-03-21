"""
Content Acquisition Layer — source type classifier.

First build: GitHub only. Aligned with source_intake.schema.json source_type enum
(youtube, reddit, github). Article/webpage deferred until schema supports it.
"""

from urllib.parse import urlparse


# First build: GitHub only. Article deferred (not in schema source_type enum).
SUPPORTED_TYPES = frozenset({"github"})


def classify_from_url(url: str) -> str:
    """
    Infer source_type from URL. First build: GitHub only.

    Args:
        url: Source URL string.

    Returns:
        "github" for GitHub URLs.

    Raises:
        ValueError: If URL is malformed or not a supported (GitHub) URL.
    """
    url = (url or "").strip()
    if not url:
        raise ValueError("Source URL is empty. Could not resolve source.")

    try:
        parsed = urlparse(url)
    except Exception as e:
        raise ValueError(f"Could not parse URL: {e}") from e

    if not parsed.scheme or not parsed.netloc:
        raise ValueError("Invalid or ambiguous URL. Provide a full URL (e.g. https://...).")

    host = parsed.netloc.lower()

    if "github.com" in host:
        return "github"

    raise ValueError(
        "Source type not supported for first build. First build supports GitHub URLs only. "
        "Article/webpage deferred until packet contract (source_intake) supports it."
    )


def is_supported(source_type: str) -> bool:
    """Check if source type is supported in first build."""
    return source_type in SUPPORTED_TYPES
