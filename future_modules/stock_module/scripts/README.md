# Stock Module Scripts

**Status:** First viable slice + risk gate + `/stock-briefs` review surface proven. **Last updated:** 2026-03-23 (doc-lock Prompt #109).

## Implemented

### confirm_watchlist_symbol.py

Manual confirm/copy bridge: one symbol from RS draft watchlist → one Stock Module input packet.

**Command:**
```bash
cd future_modules/stock_module/scripts
python confirm_watchlist_symbol.py --symbol <SYMBOL> [--source <path>] [--out <path>]
```

**Requirements:** `jsonschema` package.

**Input:** Reads `research_swarm/outputs/draft_watchlist_packet_from_rs.json` by default (override with `--source`). Operator passes exactly one approved symbol via `--symbol`.

**Output:** Writes `inputs/confirmed_watchlist_packet_<symbol>.json` by default (override with `--out`). Packet conforms to `watchlist_packet.schema.json` and has exactly one symbol.

**Example:**
```bash
python confirm_watchlist_symbol.py --symbol AAPL
python run_research_brief.py --packet ../inputs/confirmed_watchlist_packet_aapl.json
```

**Proof output:** `inputs/confirmed_watchlist_packet_aapl.json`

### run_research_brief.py

Manual run path for first viable slice: one watchlist packet with **exactly one symbol** → one research brief JSON.

**Command:**
```bash
cd future_modules/stock_module/scripts
python run_research_brief.py --packet <path-to-watchlist-packet.json> [--out <output-path>] [--model gpt-4o-mini]
```

**Requirements:** `OPENAI_API_KEY` env var, `openai` and `jsonschema` packages.

**Input:** Watchlist packet JSON conforming to `schemas/watchlist_packet.schema.json`. Must have exactly one symbol (first viable slice).

**Output:** Research brief JSON written to `outputs/stock_research_brief_<packet_stem>.json` by default, or `--out` path.

**Example:**
```bash
python run_research_brief.py --packet ../examples/example_watchlist_packet_single.json
# Or use confirmed packet from RS draft:
python run_research_brief.py --packet ../inputs/confirmed_watchlist_packet_aapl.json
```

**Proof output:** `outputs/stock_research_brief_confirmed_watchlist_packet_aapl.json`

**Dashboard:** `/stock-briefs` loads the newest `stock_research_brief_*.json` by mtime and shows that brief; if a paired `risk_gate_review_<suffix>.json` exists for the same suffix, it shows that too (see `dashboard/src/lib/data.ts`).

### run_risk_gate.py

Manual risk gate step: one stock research brief JSON → one risk gate review JSON.

**Command:**
```bash
cd future_modules/stock_module/scripts
python run_risk_gate.py --brief <path-to-stock-research-brief.json> [--out <output-path>] [--model gpt-4o-mini]
```

**Requirements:** `OPENAI_API_KEY` env var, `openai` and `jsonschema` packages.

**Input:** Research brief JSON conforming to `schemas/stock_research_brief.schema.json`.

**Output:** Risk gate review JSON written to `outputs/risk_gate_review_<suffix>.json` by default (suffix is the brief filename stem with optional `stock_research_brief_` prefix stripped), or `--out` path.

**Example:**
```bash
python run_risk_gate.py --brief ../outputs/stock_research_brief_confirmed_watchlist_packet_aapl.json
```

**Proof output:** `outputs/risk_gate_review_confirmed_watchlist_packet_aapl.json`

**Dashboard:** `/stock-briefs` reads the paired file next to the latest brief (same suffix rule). If you skip this step, the page still shows the brief and tells you to run this script.

## Not yet implemented

- `run_pipeline.py` — Optional single entrypoint to chain watchlist → brief → risk gate (still manual review; not started)

## Conventions

- Scripts run manually only (no scheduled execution)
- No broker or market data API integration in v1
- All scripts support `--help` and clear error messages
