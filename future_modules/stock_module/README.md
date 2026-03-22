# Stock Module v1

**Status:** prototype, first viable slice proven. Last updated: 2026-03-22.  
**Location:** `future_modules/stock_module/`

## Purpose

Stock Module v1 is a read-only market research worker. It produces bounded research briefs from ticker/watchlist packets. It does not trade, execute orders, or connect to brokers.

## Current Proven Flow

1. **RS Intake** — Dashboard `/stock-intake` shows candidate symbols and draft watchlist from Research Swarm outputs.
2. **Confirm one symbol** — `confirm_watchlist_symbol.py --symbol AAPL` reads draft, writes one-symbol packet to `inputs/`.
3. **Run brief** — `run_research_brief.py --packet ../inputs/confirmed_watchlist_packet_aapl.json` produces research brief JSON.
4. **Review brief** — Dashboard `/stock-briefs` shows the latest brief output (catalyst, risks, evidence, confidence band).

All steps require manual operator approval. One symbol at a time.

## Key Scripts

- `scripts/confirm_watchlist_symbol.py` — RS draft → one-symbol Stock Module packet
- `scripts/run_research_brief.py` — One-symbol packet → research brief JSON

## Proof Artifacts

- `inputs/confirmed_watchlist_packet_aapl.json` — Example confirmed packet (AAPL)
- `outputs/stock_research_brief_confirmed_watchlist_packet_aapl.json` — Example brief output

## Dashboard Routes

- `/stock-intake` — RS→Stock intake state (candidate symbols, draft watchlist)
- `/stock-briefs` — Latest Stock Module research brief output

## Current Scope

- **Read-only** — Consume watchlist packets, produce research briefs
- **No live trading** — No order placement, position management, or execution
- **No broker integration** — No API connections to brokers or exchanges
- **No autonomous execution** — Manual invocation only

## What It Does

1. Accepts a watchlist packet (symbols, watch reason, constraints)
2. Produces a structured research brief per symbol (catalyst summary, risk summary, evidence)
3. Risk gate is not yet implemented
4. Output is for human review only—no automated decisions; not real-time market data

## Remaining Limitations

- Manual operator approval required at each step
- One symbol per brief run (first viable slice)
- No risk gate implementation yet
- No batch flow
- No history/switcher for multiple brief files
- Brief content is advisory, not real-time market data

## Operating Stance

- **Read-only** — No trading, no broker APIs
- **Packet-first** — Watchlist in, research brief out
- **Evidence-backed** — Claims must cite sources
- **Human review** — All output is advisory only
