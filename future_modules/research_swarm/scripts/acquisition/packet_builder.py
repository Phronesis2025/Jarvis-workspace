"""
Content Acquisition Layer — packet builder and serializer.

Assembles normalized fields into source packet dict, writes JSON.
"""

import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

from acquisition.completeness_helper import assign_completeness, is_content_too_thin


def _generate_packet_id() -> str:
    """Generate unique packet ID."""
    return f"rs-acq-{datetime.now(timezone.utc).strftime('%Y%m%d')}-{uuid.uuid4().hex[:8]}"


def _generate_run_id() -> str:
    """Short ID for default output filename."""
    return datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")


def build_packet(
    source_url: str,
    source_type: str,
    raw_content: str,
    metadata: dict | None = None,
    raw_content_format: str = "plain_text",
    handler_hint: str | None = None,
    packet_id: str | None = None,
) -> dict:
    """
    Build source packet dict.

    Args:
        source_url: Canonical URL.
        source_type: One of: github (first build). Article deferred.
        raw_content: Normalized text content.
        metadata: Optional structured metadata.
        raw_content_format: transcript, markdown, plain_text, code, mixed.
        handler_hint: Completeness hint from handler.
        packet_id: Override generated ID.

    Returns:
        Packet dict ready for JSON serialization.

    Raises:
        ValueError: If content too thin or invalid.
    """
    if is_content_too_thin(raw_content):
        raise ValueError("Content too thin for extraction. Refusing packet creation.")

    completeness = assign_completeness(raw_content, handler_hint)
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    return {
        "packet_id": packet_id or _generate_packet_id(),
        "source_url": source_url,
        "source_type": source_type,
        "raw_content": (raw_content or "").strip(),
        "metadata": metadata or {},
        "content_completeness": completeness,
        "raw_content_format": raw_content_format,
        "created_at": now,
        "captured_at": now,
    }


def write_packet(packet: dict, output_path: Path) -> None:
    """Write packet to JSON file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(packet, f, indent=2, ensure_ascii=False)
