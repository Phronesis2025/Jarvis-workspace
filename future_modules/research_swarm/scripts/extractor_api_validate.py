"""
Extractor API v1 — schema validation for extraction report output.

Validates a dict against extraction_report.schema.json.
Raises on validation failure. No file writing.
"""

import json
from pathlib import Path
from typing import Any


def _load_schema() -> dict[str, Any]:
    """Load extraction_report schema from research_swarm schemas dir."""
    script_dir = Path(__file__).resolve().parent
    schema_path = script_dir.parent / "schemas" / "extraction_report.schema.json"
    if not schema_path.exists():
        raise FileNotFoundError(
            f"Extraction schema not found: {schema_path}. "
            "Ensure schemas/extraction_report.schema.json exists."
        )
    with open(schema_path, encoding="utf-8") as f:
        return json.load(f)


def validate_extraction_report(data: dict[str, Any]) -> None:
    """
    Validate extraction dict against extraction_report schema.

    Raises:
        ValueError: If data is not a dict
        ValidationError: If schema validation fails (from jsonschema)
        ImportError: If jsonschema is not installed
    """
    if not isinstance(data, dict):
        raise ValueError(f"Expected dict, got {type(data).__name__}")

    try:
        import jsonschema
    except ImportError as e:
        raise ImportError(
            "JSON schema validation requires the 'jsonschema' package. "
            "Install with: pip install jsonschema"
        ) from e

    schema = _load_schema()
    jsonschema.validate(instance=data, schema=schema)
