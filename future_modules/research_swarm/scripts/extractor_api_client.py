"""
Extractor API v1 — bounded LLM API client for extraction generation.

Accepts source packet dict, calls OpenAI API, returns extraction report dict.
"""

import json
import os
from typing import Any


# Bounded extraction instructions (aligned with extractor prompt contract)
_EXTRACTION_SYSTEM = """You are the Extractor for Research Swarm. Produce one complete JSON extraction report from raw source content.

Response format:
- Return exactly one raw JSON object. No markdown code fences, no commentary, no surrounding text, no partial JSON.
- Omission of any required top-level field is invalid.
- Your JSON must have these exact top-level keys: report_id, packet_id, source_url, created_at, summary, methods_tools_patterns, key_claims, hype_signals, open_questions.

Required top-level fields (all must be present):

Metadata (copy or derive from source packet):
- report_id: unique identifier for this report (e.g. rs-extract-<packet_id>)
- packet_id: copy exactly from the source packet
- source_url: copy exactly from the source packet
- created_at: ISO 8601 timestamp (e.g. 2025-03-20T12:00:00Z)

Content sections:
- summary: 2–4 sentences capturing the main point
- methods_tools_patterns: array of objects with name, description, evidence, category (method|tool|pattern)
- key_claims: array of objects with claim, evidence, confidence (stated|inferred|speculative)
- hype_signals: array of strings — phrases that indicate overclaim or hype
- open_questions: array of strings — unresolved or unclear points

Rules:
- packet_id and source_url must match the source packet exactly.
- Every methods_tools_patterns and key_claims item MUST have evidence (quote or paraphrase from source).
- Do not invent content. Only extract what is in the source.
- hype_signals must be exact phrases or clear paraphrases from the source.
- open_questions must reflect actual missing details, not speculation."""


def _build_user_content(packet: dict[str, Any]) -> str:
    """Build user message from packet fields."""
    parts = [
        f"Packet ID: {packet.get('packet_id', '')}",
        f"Source URL: {packet.get('source_url', '')}",
        f"Source type: {packet.get('source_type', '')}",
    ]
    if packet.get("content_completeness"):
        parts.append(f"Content completeness: {packet['content_completeness']}")
    if packet.get("raw_content_format"):
        parts.append(f"Raw content format: {packet['raw_content_format']}")
    if packet.get("metadata"):
        meta = packet["metadata"]
        meta_str = ", ".join(f"{k}={v}" for k, v in meta.items() if v)
        if meta_str:
            parts.append(f"Metadata: {meta_str}")

    parts.append("\n---\nRaw content:\n---")
    parts.append(packet.get("raw_content", ""))
    return "\n".join(parts)


def _ensure_packet_valid(packet: dict[str, Any]) -> None:
    """Validate required packet fields. Raises ValueError on failure."""
    required = ["packet_id", "source_url", "source_type", "raw_content", "created_at"]
    for field in required:
        if field not in packet:
            raise ValueError(f"Source packet missing required field: {field}")

    raw = packet.get("raw_content")
    if raw is None or (isinstance(raw, str) and not raw.strip()):
        raise ValueError("Source packet raw_content is missing or blank")


# Required top-level fields per extraction_report schema (validator is source of truth; this is a quick structural check)
_REQUIRED_RESPONSE_FIELDS = [
    "report_id", "packet_id", "source_url", "created_at", "summary",
    "methods_tools_patterns", "key_claims", "hype_signals", "open_questions",
]


def _parse_response(response_text: str) -> dict[str, Any]:
    """Parse API response as JSON. Raises on failure. No repair or coercion."""
    text = response_text.strip()
    if text.startswith("```"):
        raise ValueError(
            "API returned markdown-fenced content instead of raw JSON; "
            "extraction output must be a bare JSON object (no code blocks)"
        )

    try:
        parsed = json.loads(text)
    except json.JSONDecodeError as e:
        raise ValueError(f"API returned invalid JSON: {e}") from e

    if not isinstance(parsed, dict):
        raise ValueError(f"API returned non-dict: {type(parsed).__name__}")

    for field in _REQUIRED_RESPONSE_FIELDS:
        if field not in parsed:
            raise ValueError(f"API response missing required field: {field}")

    return parsed


def generate_extraction(packet: dict[str, Any], model: str) -> dict[str, Any]:
    """
    Generate extraction report from source packet via OpenAI API.

    Args:
        packet: Source intake packet dict (packet_id, source_url, source_type, raw_content, etc.)
        model: OpenAI model name (e.g. gpt-4o-mini, gpt-4o)

    Returns:
        Extraction report dict (report_id, packet_id, summary, methods_tools_patterns, etc.)

    Raises:
        ValueError: Invalid packet, invalid response, or missing raw_content
        RuntimeError: API key missing or API call failed
    """
    _ensure_packet_valid(packet)
    if not model or not str(model).strip():
        raise ValueError("model must be a non-empty string")

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key or not api_key.strip():
        raise RuntimeError(
            "OPENAI_API_KEY environment variable is not set. "
            "Set it before running the extractor."
        )

    try:
        from openai import OpenAI
    except ImportError as e:
        raise ImportError(
            "OpenAI API requires the 'openai' package. Install with: pip install openai"
        ) from e

    client = OpenAI(api_key=api_key)
    user_content = _build_user_content(packet)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": _EXTRACTION_SYSTEM},
            {"role": "user", "content": user_content},
        ],
        response_format={"type": "json_object"},
    )

    if not response.choices:
        raise ValueError("API returned no choices")
    choice = response.choices[0]
    if not choice.message:
        raise ValueError("API returned choice with no message")
    if not choice.message.content or not str(choice.message.content).strip():
        raise ValueError("API returned message with blank content")

    result = _parse_response(choice.message.content)

    if result["packet_id"] != packet["packet_id"]:
        raise ValueError(
            f"Extraction report packet_id does not match source packet: "
            f"got {result['packet_id']!r}, expected {packet['packet_id']!r}"
        )
    if result["source_url"] != packet["source_url"]:
        raise ValueError(
            f"Extraction report source_url does not match source packet: "
            f"got {result['source_url']!r}, expected {packet['source_url']!r}"
        )

    return result
