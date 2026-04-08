#!/usr/bin/env python3
"""Offline validator for on-disk UniverseScannerResult JSON packets (T94).

Scope boundary:
- Reads only outputs/phase3_universe_scanner_results/ (root *.json + optional fixtures_invalid/)
  and schemas/universe_scanner_result.schema.json under this contract package.
- Emits stdout/stderr and process exit code only.
- No network, scanner, request-to-result generation, or writes to outputs/contracts.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, List, Tuple

try:
    from jsonschema import Draft7Validator
except Exception:
    print(
        "ERROR: jsonschema is required for offline validation. "
        "Install locally in your Python environment (no network use by this tool).",
        file=sys.stderr,
    )
    sys.exit(2)

# tools/ -> phase3_universe_scanner_io/
_BASE = Path(__file__).resolve().parents[1]
# phase3_universe_scanner_io/ -> contracts/ -> the_fade/
_THE_FADE_ROOT = Path(__file__).resolve().parents[3]
RESULT_SCHEMA_PATH = _BASE / "schemas" / "universe_scanner_result.schema.json"
OUTPUTS_DIR = _THE_FADE_ROOT / "outputs" / "phase3_universe_scanner_results"
FIXTURES_INVALID_DIR = OUTPUTS_DIR / "fixtures_invalid"

# T93 Model B: at most three valid root-level result JSON seeds (hand-placed/copy-only).
_MAX_VALID_ROOT_JSON = 3


def _read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _build_validator(schema_path: Path) -> Draft7Validator:
    schema = _read_json(schema_path)
    return Draft7Validator(schema)


def _infer_fixture_reason(path: Path) -> str:
    """Derive expected jsonschema validator keyword from filename (T93/T91-style tokens)."""
    name = path.stem.lower()
    if "_result_" not in name:
        raise ValueError(
            f"{path.name}: fixture name must include '_result_' (result-packet scope only)."
        )
    if "_type_" in name:
        return "type"
    if "_required_" in name:
        return "required"
    if "_format_" in name:
        return "format"
    if "_enum_" in name:
        return "enum"
    if "_additionalproperties_" in name or "_additional_props_" in name:
        return "additionalProperties"
    if "_minlength_" in name:
        return "minLength"
    if "_pattern_" in name:
        return "pattern"
    if "_anyof_" in name:
        return "anyOf"
    raise ValueError(
        f"{path.name}: add a reason token in the stem, e.g. _type_, _required_, _format_."
    )


def _validate_root_packets(validator: Draft7Validator) -> List[Tuple[bool, str]]:
    if not OUTPUTS_DIR.is_dir():
        return [(False, f"FAIL: missing outputs directory: {OUTPUTS_DIR}")]

    paths = sorted(OUTPUTS_DIR.glob("*.json"))
    if not paths:
        return [
            (
                True,
                "outputs/phase3_universe_scanner_results/: no root-level *.json (empty-root PASS per T93)",
            )
        ]

    if len(paths) > _MAX_VALID_ROOT_JSON:
        return [
            (
                False,
                f"FAIL: Model B cap — at most {_MAX_VALID_ROOT_JSON} root *.json, found {len(paths)}",
            )
        ]

    outcomes: List[Tuple[bool, str]] = []
    for path in paths:
        data = _read_json(path)
        errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
        if errors:
            first = errors[0]
            outcomes.append(
                (
                    False,
                    f"{path.name}: FAIL at {list(first.path)} -> {first.message}",
                )
            )
        else:
            outcomes.append((True, f"{path.name}: PASS (valid against result schema)"))
    return outcomes


def _validate_invalid_fixtures(validator: Draft7Validator) -> List[Tuple[bool, str]]:
    if not FIXTURES_INVALID_DIR.exists():
        return [(True, "fixtures_invalid/: not present (skipped)")]

    fixtures = sorted(FIXTURES_INVALID_DIR.glob("*.json"))
    outcomes: List[Tuple[bool, str]] = []

    if len(fixtures) > 5:
        outcomes.append(
            (
                False,
                f"fixtures_invalid/: FAIL expected <= 5 files, found {len(fixtures)}",
            )
        )
        return outcomes

    if not fixtures:
        outcomes.append((True, "fixtures_invalid/: empty (skipped)"))
        return outcomes

    for path in fixtures:
        try:
            expected = _infer_fixture_reason(path)
            data = _read_json(path)
            errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
            if not errors:
                outcomes.append(
                    (False, f"{path.name}: FAIL expected invalid, got valid")
                )
                continue
            validators = {e.validator for e in errors}
            if expected not in validators:
                got = " | ".join(sorted(validators))
                outcomes.append(
                    (
                        False,
                        f"{path.name}: FAIL expected reason class '{expected}', got '{got}'",
                    )
                )
                continue
            outcomes.append(
                (
                    True,
                    f"{path.name}: PASS (invalid as expected: {expected})",
                )
            )
        except Exception as exc:
            outcomes.append((False, f"{path.name}: FAIL {exc}"))
    return outcomes


def main() -> int:
    if not RESULT_SCHEMA_PATH.exists():
        print(f"FAIL: missing schema: {RESULT_SCHEMA_PATH}", file=sys.stderr)
        return 1

    validator = _build_validator(RESULT_SCHEMA_PATH)

    checks: List[Tuple[bool, str]] = []
    checks.extend(_validate_root_packets(validator))
    checks.extend(_validate_invalid_fixtures(validator))

    failed = [msg for ok, msg in checks if not ok]
    for _, msg in checks:
        print(msg)

    if failed:
        print(f"SUMMARY: FAIL ({len(failed)} failure(s))", file=sys.stderr)
        return 1

    print("SUMMARY: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
