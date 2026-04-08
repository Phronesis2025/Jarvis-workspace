# Repo Intake Report: discountry/polymarket-trading-bot

- Run ID: `repo_intake_batch_20260408_171347Z`
- Fetch evaluation skipped: False
- Repo URL: https://github.com/discountry/polymarket-trading-bot
- Profile: prediction_market_execution
- Profile Selected Automatically: True
- Auto Profile Confidence: 0.84
- Classification: **marginal**
- Confidence: 0.62
- Repo Reality Score: 35/50
- Our Fit Score: 28/40
- Novelty Flag: 4/10

## Summary
Bounded static triage summary only; no runtime execution performed.

## Auto Profile Reasons
- Strong prediction-market execution signals take precedence.
- Matched strong terms: polymarket, trading bot, orderbook, clob

## Positive Signals
- README exists and provides inspectable context.
- Top-level code artifacts are present.
- Config/build files suggest implementable structure.
- Test-related files/directories appear present.
- Language footprint detected (1 languages).

## Negative Signals
- No major negative signal found in bounded static pass.
- Fatal flag: direct_secret_or_key_sloppiness

## Danger Flags
- Fatal: direct_secret_or_key_sloppiness

## Top Files To Inspect
- README.md
- README_CN.md
- docs
- requirements.txt
- src

## Disposition
- Final Disposition: **marginal**
- Worker Status: `escalated`
- Deeper Review Recommended: `True`
- Escalation Reasons:
  - fatal flag triggered but repo still appears strategically interesting
