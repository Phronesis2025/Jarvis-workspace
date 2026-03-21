"""
Content Acquisition Layer — handler base and result type.
"""

from dataclasses import dataclass


@dataclass
class HandlerResult:
    """Result from a source-type handler."""

    raw_content: str
    metadata: dict
    raw_content_format: str  # plain_text, markdown, etc.
    handler_hint: str | None = None  # page_text, readme, summary, etc.


class BaseHandler:
    """Base for source-type handlers."""

    def fetch(self, url: str) -> HandlerResult:
        """Fetch and normalize content. Subclasses implement."""
        raise NotImplementedError
