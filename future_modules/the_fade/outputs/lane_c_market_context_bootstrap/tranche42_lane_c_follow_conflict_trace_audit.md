# Tranche 42 - Lane C FOLLOW conflict-mismatch trace audit

Bounded THE FADE-local fixture audit only. No network, no live market-data integration, no approval change.

## Case verdicts

| case_id | policy_outcome | primary_direction | market_context_direction | conflict_status | omission_reason | omission_explicit | no_hidden_override | case_pass |
|---|---|---|---|---|---|---:|---:|---:|
| `case_1_fresh_valid_agrees_with_primary` | `accepted_follow` | `bullish` | `bullish` | `aligned` | `none` | false | true | true |
| `case_2_fresh_valid_conflicts_with_primary` | `invalidated_omit` | `bullish` | `bearish` | `direction_mismatch` | `direction_conflict_with_primary` | true | true | true |
| `case_3_stale_conflicts_invalidated_by_policy` | `invalidated_omit` | `bullish` | `bearish` | `not_evaluated_stale_first` | `stale_market_context` | true | true | true |
| `case_4_missing_no_silent_influence` | `invalidated_omit` | `bullish` | `null` | `none` | `missing_market_context` | true | true | true |
| `case_5_invalid_shape_no_silent_influence` | `invalidated_omit` | `bullish` | `null` | `none` | `invalid_market_context_shape` | true | true | true |

## Proved now

- Explicit agreement vs direction-mismatch handling for fresh-valid Lane C context under FOLLOW.
- Stale/missing/invalid-shape paths omit with explicit reasons; no silent dominance of market over primary.
- `no_hidden_override` holds across bounded cases.

## Not proved yet

- Live market-data integration or provider reliability.
- Full Lane C gate closure or MVP approval.
- Phase 3 readiness.
