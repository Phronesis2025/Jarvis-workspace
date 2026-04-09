# Foundry Local/Core Registry Engine Scripts

**Updated:** 2026-04-09

Run the Phase 2 local/core engine only.

## Command

`py -3 future_modules/the_foundry/scripts/run_foundry_registry_engine.py --input future_modules/the_foundry/state/indexes/example_engine_input.json`

## Input contract

The input file must contain:
- `source_record` object (Source Record v1 required fields/enums)
- `candidate_ideas` array (Candidate Idea v1 required fields/enums)

## Output locations

- source records: `future_modules/the_foundry/state/source_records/`
- candidate ideas: `future_modules/the_foundry/state/candidate_ideas/`
- registry ideas: `future_modules/the_foundry/state/registry_ideas/`
- queue recommendation runs: `future_modules/the_foundry/state/queue_recommendations/`
- run manifest: `future_modules/the_foundry/state/indexes/foundry_registry_manifest.json`
