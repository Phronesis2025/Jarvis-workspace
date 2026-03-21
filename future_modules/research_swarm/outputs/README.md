# Research Swarm Outputs

## Purpose

This directory stores artifacts from manual Research Swarm runs.

Artifacts include:

- source intake packets
- extraction reports
- evaluation reports
- archive entries

## File Naming Convention

Use:

- `source_packet_<runid>.json`
- `extraction_report_<runid>.json`
- `evaluation_report_<runid>.json`
- `archive_entry_<runid>.json`

Where `<runid>` = timestamp or packet_id.

## Retention

- outputs are append-only
- no overwriting prior runs
- corrections should produce a new run artifact

v1 manual runs produce full output sets only for `archive` and `archive_with_warning`. If decision is `skip_archive`, the run stops before archive entry creation. v1 does not persist skip records in outputs.

## Validation

All JSON artifacts must validate against the corresponding schema in:

```
future_modules/research_swarm/schemas/
```
