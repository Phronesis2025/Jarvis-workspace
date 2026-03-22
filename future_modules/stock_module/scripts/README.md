# Stock Module Scripts

**Status:** First viable slice proven; confirm/copy bridge and brief review page live. Last updated: 2026-03-22.

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

**Review:** Dashboard `/stock-briefs` shows the latest brief output.

## Not Yet Implemented

- `run_risk_gate.py` — Risk gate prompt with research brief
- `run_pipeline.py` — End-to-end: watchlist → brief → risk gate

## Conventions

- Scripts run manually only (no scheduled execution)
- No broker or market data API integration in v1
- All scripts support `--help` and clear error messages
