#!/usr/bin/env python3
"""
Stock Module v1 — manual run path for first viable slice.

Reads a watchlist packet, enforces exactly-one-symbol rule, generates one research brief
via LLM, validates against schema, writes JSON to disk.

No market data integration. No risk gate. Manual invocation only.
"""

import argparse
import json
import sys
from pathlib import Path

_SCRIPT_DIR = Path(__file__).resolve().parent
_STOCK_MODULE_ROOT = _SCRIPT_DIR.parent


def _load_json(path: Path) -> dict:
    """Load and parse JSON. Raises on failure."""
    if not path.exists():
        print(f"Error: File not found: {path}", file=sys.stderr)
        sys.exit(1)
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON: {e}", file=sys.stderr)
        sys.exit(1)
    if not isinstance(data, dict):
        print(f"Error: Expected JSON object, got {type(data).__name__}", file=sys.stderr)
        sys.exit(1)
    return data


def _validate_packet(packet: dict) -> None:
    """Validate packet against watchlist_packet schema. Exit on failure."""
    schema_path = _STOCK_MODULE_ROOT / "schemas" / "watchlist_packet.schema.json"
    if not schema_path.exists():
        print(f"Error: Schema not found: {schema_path}", file=sys.stderr)
        sys.exit(1)
    try:
        import jsonschema
    except ImportError:
        print("Error: jsonschema required. Install with: pip install jsonschema", file=sys.stderr)
        sys.exit(1)
    with open(schema_path, encoding="utf-8") as f:
        schema = json.load(f)
    try:
        jsonschema.validate(instance=packet, schema=schema)
    except jsonschema.ValidationError as e:
        print(f"Error: Packet validation failed: {e}", file=sys.stderr)
        sys.exit(1)


def _enforce_one_symbol(packet: dict) -> None:
    """Enforce first viable slice: exactly one symbol. Exit on failure."""
    symbols = packet.get("symbols", [])
    if not isinstance(symbols, list) or len(symbols) != 1:
        print(
            f"Error: First viable slice requires exactly one symbol. Got {len(symbols) if isinstance(symbols, list) else 'non-list'}.",
            file=sys.stderr,
        )
        sys.exit(1)
    if not symbols[0] or not str(symbols[0]).strip():
        print("Error: Symbol must be non-empty.", file=sys.stderr)
        sys.exit(1)


def _load_prompt() -> str:
    """Load research brief prompt from prompts dir."""
    prompt_path = _STOCK_MODULE_ROOT / "prompts" / "research_brief_prompt.md"
    if not prompt_path.exists():
        print(f"Error: Prompt not found: {prompt_path}", file=sys.stderr)
        sys.exit(1)
    with open(prompt_path, encoding="utf-8") as f:
        return f.read()


def _build_system_content(prompt_text: str) -> str:
    """Build system message with schema contract."""
    return f"""{prompt_text}

## Output Contract

Return exactly one raw JSON object. No markdown code fences, no commentary.
Your JSON must have these exact top-level keys: report_id, packet_id, created_at, symbols, briefs.
- packet_id: copy from the watchlist packet
- created_at: ISO 8601 timestamp (e.g. 2026-03-21T12:00:00Z)
- symbols: copy from the watchlist packet (will be one symbol for first viable slice)
- report_id: e.g. sm-brief-<packet_id>
- briefs: array with one object per symbol; each object must include symbol, thesis_or_watch_reason, catalyst_summary, risk_summary, confidence_band (low|medium|high), review_recommendation (monitor|dig deeper|pass|flag for discussion). Include evidence_sources and open_questions when you have them.
"""


def _build_user_content(packet: dict) -> str:
    """Build user message with packet content."""
    return f"Watchlist packet:\n{json.dumps(packet, indent=2)}"


def _generate_brief(packet: dict, model: str) -> dict:
    """Call LLM, return parsed research brief dict."""
    import os

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key or not str(api_key).strip():
        print("Error: OPENAI_API_KEY environment variable not set.", file=sys.stderr)
        sys.exit(1)

    try:
        from openai import OpenAI
    except ImportError:
        print("Error: openai package required. Install with: pip install openai", file=sys.stderr)
        sys.exit(1)

    prompt_text = _load_prompt()
    system_content = _build_system_content(prompt_text)
    user_content = _build_user_content(packet)

    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_content},
        ],
        response_format={"type": "json_object"},
    )

    if not response.choices:
        print("Error: API returned no choices.", file=sys.stderr)
        sys.exit(1)
    choice = response.choices[0]
    content = choice.message.content if choice.message else None
    if not content or not str(content).strip():
        print("Error: API returned empty content.", file=sys.stderr)
        sys.exit(1)

    text = str(content).strip()
    if text.startswith("```"):
        print("Error: API returned markdown-fenced content instead of raw JSON.", file=sys.stderr)
        sys.exit(1)

    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        print(f"Error: API returned invalid JSON: {e}", file=sys.stderr)
        sys.exit(1)


def _validate_brief(brief: dict) -> None:
    """Validate brief against stock_research_brief schema. Exit on failure."""
    schema_path = _STOCK_MODULE_ROOT / "schemas" / "stock_research_brief.schema.json"
    if not schema_path.exists():
        print(f"Error: Schema not found: {schema_path}", file=sys.stderr)
        sys.exit(1)
    try:
        import jsonschema
    except ImportError:
        print("Error: jsonschema required. Install with: pip install jsonschema", file=sys.stderr)
        sys.exit(1)
    with open(schema_path, encoding="utf-8") as f:
        schema = json.load(f)
    try:
        jsonschema.validate(instance=brief, schema=schema)
    except jsonschema.ValidationError as e:
        print(f"Error: Brief validation failed: {e}", file=sys.stderr)
        sys.exit(1)


def _default_output_path(packet_path: Path) -> Path:
    """Default: outputs/stock_research_brief_<stem>.json alongside stock_module root."""
    stem = packet_path.stem
    out_dir = _STOCK_MODULE_ROOT / "outputs"
    return out_dir / f"stock_research_brief_{stem}.json"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate one research brief from a watchlist packet (first viable slice: exactly one symbol)."
    )
    parser.add_argument("--packet", required=True, type=Path, help="Path to watchlist packet JSON")
    parser.add_argument("--out", type=Path, default=None, help="Output path (default: outputs/stock_research_brief_<packet_stem>.json)")
    parser.add_argument("--model", type=str, default="gpt-4o-mini", help="OpenAI model (default: gpt-4o-mini)")
    args = parser.parse_args()

    packet_path = args.packet.resolve()
    output_path = args.out.resolve() if args.out else _default_output_path(packet_path)
    model = args.model.strip() if args.model else "gpt-4o-mini"

    print(f"Packet: {packet_path}")
    packet = _load_json(packet_path)

    _validate_packet(packet)
    print("Packet validation: PASS")

    _enforce_one_symbol(packet)
    symbol = packet["symbols"][0]
    print(f"Symbol: {symbol} (first viable slice)")

    print(f"Model: {model}")
    brief = _generate_brief(packet, model)

    _validate_brief(brief)
    print("Brief validation: PASS")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(brief, f, indent=2, ensure_ascii=False)
    except OSError as e:
        print(f"Error: Failed to write output: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Output: {output_path}")
    print()
    print("--- MANUAL REVIEW REQUIRED ---")
    print("Review research brief before any use. Output is advisory only.")
    print("---")

    return 0


if __name__ == "__main__":
    sys.exit(main())
