# Tranche 58 — Lane B real-slice normalization truth audit

**Scope:** stored 22-slot Lane B full-window artifacts only. No network. No new collection. No approval change.

## Exact question answered

This tranche tests what the stored 22-slot Federal Register slice can and cannot honestly prove about Lane B `normalized_signal_event` viability.

## Population

- Counted rows: **22**
- Window: **`2026-03-27T16:00:00Z`** → **`2026-03-29T16:00:00Z`**
- Excluded: **`t30_valid_002`**
- All counted rows kept a snapshot artifact: **22 / 22**

## Stored normalization-relevant fields present on disk

- `response_preview_utf8`: **22 / 22**
- `response_sha256`: **22 / 22**
- `results[0].document_number`: **22 / 22**
- `results[0].publication_date`: **22 / 22**
- `results[0].title`: **22 / 22**
- `results[0].type`: **22 / 22**
- `results[0].html_url`: **22 / 22**
- `results[0].pdf_url`: **22 / 22**
- `results[0].public_inspection_pdf_url`: **20 / 22**
- `results[0].abstract` token present in preview: **22 / 22**
- `results[0].agencies` token present in preview: **22 / 22**
- `results[0].excerpts` token present in preview: **22 / 22**
- Full preview JSON parse succeeds: **0 / 22**

## Required normalized field truth

- Direct on disk for all 22: **`evidence_path`, `evidence_url`, `ingested_at`, `task_id`**
- Derivable exactly from stored fields: **`event_id`**
- Partial only: **`event_time`, `freshness_hours`, `lag_class`, `notes`, `parsed_summary`, `raw_text`, `source_lane`, `source_name`**
- Not evidenced from the real stored slice: **`asset_type`, `direction_hint`, `parser_confidence`, `ticker`, `trust_tier`**

## Honest verdict

- The real stored slice is strong enough to prove collector-level retention and partial normalization support.
- The real stored slice is not strong enough to prove full `normalized_signal_event` materialization without policy fill-ins or invented values.
- Silent-drop risk is reduced at the collector retention layer, but still unprovable for full normalized-event materialization from this stored slice alone.

## Gate impact

- Lane B `normalization_viability` remains **partial**.
- T58 strengthens the exact real-slice truth boundary for that dimension.
- T58 does **not** justify approval and does **not** unlock Phase 3.

Machine-readable artifact: `tranche58_lane_b_real_slice_normalization_truth_audit.json`
