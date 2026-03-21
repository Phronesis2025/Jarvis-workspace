"""
Content Acquisition Layer — packet validation helper.

Checks packet has required fields and honest completeness.
"""

REQUIRED_FIELDS = frozenset({
    "packet_id",
    "source_url",
    "source_type",
    "raw_content",
    "metadata",
    "content_completeness",
    "raw_content_format",
    "created_at",
})

MIN_RAW_CONTENT_CHARS = 200


def validate_packet(packet: dict) -> list[str]:
    """
    Validate packet. Returns list of error messages; empty if valid.

    Checks:
    - Required fields present
    - raw_content non-blank and above minimum length
    - content_completeness not metadata_only when content exists
    """
    errors = []

    for field in REQUIRED_FIELDS:
        if field not in packet:
            errors.append(f"Missing required field: {field}")

    raw = packet.get("raw_content")
    if raw is None:
        errors.append("raw_content is null")
    elif not isinstance(raw, str):
        errors.append("raw_content must be a string")
    else:
        stripped = raw.strip()
        if not stripped:
            errors.append("raw_content is blank")
        elif len(stripped) < MIN_RAW_CONTENT_CHARS:
            errors.append(
                f"raw_content too thin ({len(stripped)} chars < {MIN_RAW_CONTENT_CHARS})"
            )

    completeness = packet.get("content_completeness")
    if completeness == "metadata_only" and raw and len((raw or "").strip()) >= MIN_RAW_CONTENT_CHARS:
        errors.append("content_completeness is metadata_only but raw_content has substance")

    return errors
