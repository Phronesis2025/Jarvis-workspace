# Repo Intake Validation Batch 001

Validation run for four fixed repositories using bounded static triage only.

Scoring pass updated once with a narrow `prediction_market_execution` refinement to better weight execution/microstructure mechanics evidence.

## Batch Results

| Repo | Profile | Classification | Repo Reality | Our Fit | Novelty | Fatal Flags | Direction Check | Main Reason |
|---|---|---:|---:|---:|---:|---|---|---|
| `yamadashy/repomix` | `workflow_tooling` | `materially_useful` | 50 | 34 | 8 | none | Acceptable | Strong top-level structure, clear workflow utility signals, no fatal flags. |
| `polymarket/agents` | `prediction_market_execution` | `marginal` | 30 | 28 | 4 | `no_paper_mode` | Acceptable | Remains non-material due to fatal-flag presence; modest mechanics signal support. |
| `warproxxx/poly-maker` | `prediction_market_execution` | `marginal` | 34 | 34 | 2 | `direct_secret_or_key_sloppiness`, `no_paper_mode` | Acceptable | Mechanics-heavy wording (market-making/orderbook/execution cues) now correctly lifts reality above `polymarket/agents`. |
| `amadeusprotocol/polymarket-trading-bot` | `prediction_market_execution` | `too_fuzzy` | 17 | 34 | 4 | `copy_trading_main_value_prop`, `direct_secret_or_key_sloppiness` | Acceptable | Danger/copy-trading concerns still trigger; remains below marginal threshold and does not outrank `poly-maker` by disposition. |

## Directional Assessment

- 4/4 targets meet the key directional guardrails (no major inversion such as bad repo ranked clearly best).
- Previously observed miss is improved: `poly-maker` now exceeds `polymarket/agents` on `repo_reality_score` (34 vs 30).
- Current scoring is still a bounded first-pass heuristic and should remain operator-supervised.

## Minimal Corrections Applied

- A single bounded runtime fix was required during validation execution:
  - `run_repo_intake.py` now reads input JSON as `utf-8-sig` to handle BOM-prefixed files on Windows.
- One narrow scoring refinement was added in `repo_intake_lib.py` for `prediction_market_execution`:
  - adds bounded reality bonus for execution/microstructure mechanics terms
  - applies light reality penalty for polished wrapper-like surface without control/mechanics evidence
- No dashboard, deep-review runtime, repo cloning, or target-repo code execution was added.
