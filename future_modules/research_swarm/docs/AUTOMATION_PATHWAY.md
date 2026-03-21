# Automation Pathway

Progression from manual workflow to one-line command. Each step must be proven before combining.

---

## Current State

Manual proven flow:

1. Source packet (built with transcript)
2. Extraction (extractor prompt → extraction report)
3. Evaluation (evaluator prompt → evaluation report)
4. Archive (archivist prompt → archive entry, when applicable)

Two manual runs completed. Contracts and schemas stable.

---

## Target State

Eventually support:

- One command to run a source through: transcript acquisition → extraction → evaluation → archive flow
- Clear failure handling at each step
- Manual override when automation fails or operator prefers manual control

---

## Required Progression

Do not compress multiple unstable steps into one command before each step is proven independently.

| Stage | Step | Description |
|-------|------|-------------|
| **1** | Manual proven flow | Current state: operator runs each step by hand |
| **2** | Extractor API integration | API generates extraction; operator reviews; evaluator/archivist manual |
| **3** | Transcript acquisition automation | Automated fetch + fallbacks; populates source packet |
| **4** | Semi-manual wrapper | Script or module that chains transcript → extraction; evaluator/archivist still manual |
| **5** | Full one-line command | Single command runs full pipeline with review gates |
| **6** | Later optional scheduling | Cron or scheduler; out of scope for initial automation |

---

## Important Rule

**Do not compress multiple unstable steps into one command before each step is proven independently.**

Proof order:

1. Extractor API output meets quality bar (compare to manual).
2. Transcript acquisition produces usable packets (compare to manual).
3. Only then combine into a single run command.

---

## Example Future Command

Illustrative only — not yet approved for implementation:

```
python scripts/run_research_swarm_once.py --source youtube --url "<url>"
```

Behavior (hypothetical):

- Attempt transcript acquisition for URL
- Run extractor (API or manual)
- Run evaluator (manual)
- Run archivist if archive recommendation (manual)
- Write outputs to `outputs/`

This example is for planning clarity. Implementation details TBD.

---

## Preconditions Before One-Line Command

All of the following must hold:

- **Stable transcript acquisition** — primary + fallback paths tested
- **Stable extractor output quality** — API output matches or approximates manual baseline
- **Stable evaluator/archive contracts** — no schema or flow changes mid-automation
- **Clear failure handling** — each step has defined failure behavior
- **Manual override path** — operator can intervene or re-run any step manually
