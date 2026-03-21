# Acquisition smoke test URLs

First-build smoke examples for Content Acquisition Layer.

**First build: GitHub only.** Article/webpage deferred until source_intake schema supports it.

## GitHub (supported)

- https://github.com/python/cpython (README)
- https://github.com/requests/requests (README)

## Expected failures / deferred

- https://example.com — unsupported; first build supports GitHub URLs only
- https://en.wikipedia.org/wiki/Python_(programming_language) — article type deferred
- YouTube, Reddit, Twitter URLs — not in first-build scope

## Future candidate selection note

For discovery-oriented steps: prioritize most recent relevant sources first (methods/tools/processes change quickly).
