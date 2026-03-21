# Discovery smoke test queries

First-build smoke examples for Discovery / Intake layer.

**First build: GitHub only.** Freshness-first ranking (sort=updated, order=desc).

## Example queries

- `python prediction market API`
- `langchain agents`
- `FastAPI production`

## Expected behavior

- Non-empty candidate queue for popular tech topics
- Candidates ordered by most recently updated (pushed_at)
- priority: high (top 3), medium (4–7), low (rest)
- freshness_signal present when API provides pushed_at/updated_at

## Handoff to acquisition

Operator selects candidates from queue; runs acquisition per URL:

```
python scripts/run_acquisition.py --url <source_url from queue>
```
