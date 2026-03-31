# Tranche 34 — Lane B normalization breadth audit

**Not approval.** Does **not** close the MVP gate. **Phase 3** blocked. **`mvp_lane_approval.json`** unchanged.

## Grounded field set

- **JSONL:** `task_id`, `slot_identity`, `run_identity`, schedule/window UTC, `source_class`, `endpoint_url`, HTTP + success flags, `observed_result_type`, `artifact_path` (from `run_tranche21_fr_slot.py` ingestion contract).
- **Snapshot shell:** `artifact_version`, ids, `endpoint_url`, `captured_at_utc`, `http_status`, `response_preview_utf8`, `response_sha256`, success flags.
- **Source document (preview):** `results[0]` `document_number`, `publication_date` (per evidence log freshness path); optional `title`, `type`, `html_url` via regex after `"results":[{`.

## Summary

- Rows audited: **22** (`t30_valid_002` excluded).
- Full JSON parse of `response_preview_utf8`: **0** / **22** (truncation expected).
- Regex `document_number` in `results[0]` region: **22** / **22**.
- Distinct `document_number` values: **3** — `2026-05939, 2026-06079, 2026-06133`.

## Verdict

- **Solid:** Collector JSONL + snapshot metadata support consistent identity, timing, and outcome typing for the window.
- **Partial:** Normalization from **full** API JSON is **not** available when preview is truncated; regex extraction matches current evidence practice.
- **Not closed:** Normalization **breadth** for rich fields (full agencies, excerpts, full title) is **not** proven from stored snapshots alone.

Machine-readable: `tranche34_normalization_breadth_audit.json`
