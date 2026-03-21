# Research Swarm Scripts

**Status:** Placeholder. No scripts implemented yet.

## Likely Future Scripts

When implementation begins, scripts in this folder may include:

- `collect_source.py` — Fetch transcript/post/README from URL (YouTube, Reddit, GitHub)
- `run_extractor.py` — Invoke extractor prompt with source packet, output extraction report
- `run_evaluator.py` — Invoke evaluator prompt with extraction report, output evaluation report
- `run_archivist.py` — Invoke archivist prompt with extraction + evaluation, output archive entry
- `run_pipeline.py` — End-to-end: intake → extract → evaluate → archive (manual invocation)

## Conventions

- Scripts run manually only (no scheduled execution)
- Input: path to packet or report JSON
- Output: path to output file or stdout
- All scripts must support `--help` and clear error messages

## Do Not Implement Yet

Per build rules, implementation scripts are deferred until schemas, prompts, and examples are validated.
