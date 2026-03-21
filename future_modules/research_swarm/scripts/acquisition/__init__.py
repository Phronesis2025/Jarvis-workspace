"""
Content Acquisition Layer — first-build implementation.

Converts chosen source URLs into normalized source packets for Research Swarm extraction.
First build: github only. Article deferred (source_intake schema alignment).
"""

from acquisition.source_classifier import classify_from_url, is_supported
from acquisition.packet_builder import build_packet, write_packet
from acquisition.completeness_helper import assign_completeness, is_content_too_thin
from acquisition.validate_packet import validate_packet
from acquisition.handlers import get_handler

__all__ = [
    "classify_from_url",
    "is_supported",
    "build_packet",
    "write_packet",
    "assign_completeness",
    "is_content_too_thin",
    "validate_packet",
    "get_handler",
]
