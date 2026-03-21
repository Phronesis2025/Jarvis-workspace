"""
Content Acquisition Layer — completeness labeling helper.

Assigns content_completeness from handler hint and raw_content inspection.
Enforces minimum threshold; refuses metadata_only.
"""

MIN_RAW_CONTENT_CHARS = 200

# Schema-compatible values (source_intake.schema.json enum)
COMPLETENESS_FULL = "full"
COMPLETENESS_PARTIAL = "partial"
COMPLETENESS_SUMMARY_ONLY = "summary_only"


def assign_completeness(
    raw_content: str,
    handler_hint: str | None,
) -> str:
    """
    Assign content_completeness label.

    Args:
        raw_content: The captured text.
        handler_hint: Optional hint from handler (e.g. "page_text", "readme", "summary").

    Returns:
        One of: full, partial, summary_only

    Raises:
        ValueError: If content is too thin (below MIN_RAW_CONTENT_CHARS).
    """
    text = (raw_content or "").strip()
    length = len(text)

    if length < MIN_RAW_CONTENT_CHARS:
        raise ValueError(
            f"Content too thin for extraction ({length} chars < {MIN_RAW_CONTENT_CHARS}). "
            "Refusing packet creation."
        )

    # Map handler hints to schema-compatible labels
    hint = (handler_hint or "").lower()
    if "summary" in hint or "description_only" in hint:
        return COMPLETENESS_SUMMARY_ONLY
    if "partial" in hint or "truncated" in hint:
        return COMPLETENESS_PARTIAL
    # Default: we have substantial content
    return COMPLETENESS_FULL


def is_content_too_thin(raw_content: str | None) -> bool:
    """Check if content is below minimum threshold."""
    return len((raw_content or "").strip()) < MIN_RAW_CONTENT_CHARS
