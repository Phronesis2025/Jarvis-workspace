# First Run Execution Notes

## Source Selected

- **URL:** https://www.youtube.com/watch?v=i3ZlLmYn584
- **Type:** youtube
- **Title reference:** How To Build A Polymarket Trading Bot (With OpenClaw)

## What Is Ready Now

- `source_packet_first_run.json` — Source intake packet with placeholder for raw_content

## Transcript Status

**Transcript is still needed.**

## Exact Next Operator Action

1. Capture the transcript from the video (Show transcript → copy).
2. Open `outputs/source_packet_first_run.json`.
3. Replace the `raw_content` placeholder with the pasted transcript.
4. Save the file.
5. Proceed to the extractor step in `run_packets/FIRST_RUN_OPERATOR_GUIDE.md`.

## Downstream Files

These can only be created after transcript is present and extractor/evaluator/archivist prompts have been run:

- extraction_report_first_run.json
- evaluation_report_first_run.json
- archive_entry_first_run.json

## No Fabrication Rule

No downstream file may be created without actual transcript content. Do not fabricate extraction, evaluation, or archive outputs.
