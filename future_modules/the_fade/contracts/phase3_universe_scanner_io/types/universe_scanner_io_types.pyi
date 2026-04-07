"""Static type shapes for UniverseScanner I/O (contract only).

This module is a stub (.pyi): no runtime implementation, no I/O, no imports
that perform work. Use for type-checking against JSON that conforms to the
schemas in ../schemas/.
"""

from typing import List, Literal, NotRequired, TypedDict

ScannerStatus = Literal["pending", "completed", "partial", "failed"]

RowStatus = Literal["included", "excluded", "deferred"]


class UniverseScannerRequest(TypedDict, total=False):
    """Input packet. Must include either candidate_symbols (non-empty) or candidate_source_packet_ref."""

    request_id: str
    as_of_utc: str
    universe_source_ref: str
    contract_version: str
    scan_policy_version: str
    candidate_symbols: List[str]
    candidate_source_packet_ref: str
    operator_notes: NotRequired[str]


class CandidateOutputRow(TypedDict, total=False):
    symbol: str
    row_status: RowStatus
    normalized_label: NotRequired[str]
    omission_reason: NotRequired[str]


class UniverseScannerResult(TypedDict, total=False):
    """Output packet referencing the request_id of the originating request."""

    request_id: str
    produced_at_utc: str
    scanner_status: ScannerStatus
    contract_version: str
    candidate_outputs: List[CandidateOutputRow]
    warnings: NotRequired[List[str]]
    exclusions: NotRequired[List[str]]
    notes: NotRequired[str]
