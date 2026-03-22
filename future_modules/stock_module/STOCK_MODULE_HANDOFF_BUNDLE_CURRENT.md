# Stock Module Handoff Bundle — Current State

**Last updated:** 2026-03-23 (doc-lock after Prompt #109)

## 1. Purpose

This bundle reconstructs the real current state of the stock-module/dashboard lane and its linked Research Swarm intake. Use it to restart a new chat at the actual implemented state (through `/stock-briefs` brief + risk-gate visibility), without theory or guesswork.

---

## 2. Current verified state

**Implemented:**
- Dashboard `/stock-intake` (`dashboard/src/app/stock-intake/page.tsx`). Reads `stock_symbol_review_summary.json` and `draft_watchlist_packet_from_rs.json` from `future_modules/research_swarm/outputs/`. Symbols table, draft watchlist, status cards, "What happens next."
- `confirm_watchlist_symbol.py` — RS draft → one-symbol packet under `inputs/`. Proven: `inputs/confirmed_watchlist_packet_aapl.json`.
- `run_research_brief.py` — one-symbol packet → brief JSON. Proven: `outputs/stock_research_brief_confirmed_watchlist_packet_aapl.json`.
- `run_risk_gate.py` — brief JSON → risk gate review JSON. Proven: `outputs/risk_gate_review_confirmed_watchlist_packet_aapl.json`.
- Dashboard `/stock-briefs` (`dashboard/src/app/stock-briefs/page.tsx`) with `getLatestStockResearchBrief()` and `getRiskGateReviewForLatestBrief()` in `dashboard/src/lib/data.ts`. Shows latest brief by mtime; loads paired `risk_gate_review_<suffix>.json` when the suffix matches the latest `stock_research_brief_<suffix>.json` (same naming rule as `run_risk_gate.py`). Plain-English pass/caution/flag; missing gate → operator instruction to run `run_risk_gate.py`; explicit manual-review-only / not trade execution copy.

**Verified:** RS intake → confirm → brief → risk gate → review both on `/stock-briefs` is the live manual lane (Prompts through #109 on dashboard follow-up).  
**Still manual:** Every CLI step; one symbol per brief; no `run_pipeline.py`; no multi-file browser; no live market data; no execution.

---

## 3. Current process position

**Done:**
- Stock Module v1 spec, schemas, prompts (incl. risk gate schema + prompt).
- RS `build_stock_symbol_review.py` → `stock_symbol_review_summary.json`.
- `/stock-intake`, `/stock-briefs` as above.
- Scripts: `confirm_watchlist_symbol.py`, `run_research_brief.py`, `run_risk_gate.py` (all proven on AAPL path).
- Proof trio: `inputs/confirmed_watchlist_packet_aapl.json`, `outputs/stock_research_brief_confirmed_watchlist_packet_aapl.json`, `outputs/risk_gate_review_confirmed_watchlist_packet_aapl.json`.

**Not done:**
- `run_pipeline.py` (chained CLI convenience only — not implemented).
- No automation for creating `draft_watchlist_packet_from_rs.json`.
- No batch flow; no history/switcher; pairing is filename/mtime based, not `report_id`.
- Brief and gate output remain advisory; not real-time data.

**Immediate next bounded move:** Implement `run_pipeline.py` as a thin, explicit chain (watchlist packet path → brief → risk gate) with the same manual-review banners — **or** defer that and add a brief/risk switcher **only** when multiple brief files in `outputs/` make the “latest by mtime” rule painful.

---

## 4. File map

### Dashboard
| Path | Why it matters |
|------|----------------|
| `dashboard/src/app/stock-intake/page.tsx` | Stock Intake Review page; status cards, symbols table, draft watchlist, "What happens next" |
| `dashboard/src/app/stock-briefs/page.tsx` | Stock Brief Review: latest brief + paired risk gate; pass/caution/flag copy; missing-gate guidance |
| `dashboard/src/lib/data.ts` | `getStockSymbolReviewSummary`, `getDraftWatchlistPacket`, `getLatestStockResearchBrief`, `getRiskGateReviewForLatestBrief`, types |
| `dashboard/src/components/NavBar.tsx` | Nav includes "Stock Intake" → `/stock-intake`, "Stock Briefs" → `/stock-briefs` |
| `dashboard/src/components/HudMetricCard.tsx` | Reused by Stock Intake and Stock Briefs for status cards |

### Stock Module
| Path | Why it matters |
|------|----------------|
| `future_modules/stock_module/module_spec.md` | Spec: inputs, outputs, workflow, first viable slice |
| `future_modules/stock_module/scripts/confirm_watchlist_symbol.py` | RS draft → one-symbol packet; proven |
| `future_modules/stock_module/scripts/run_research_brief.py` | One symbol → one research brief |
| `future_modules/stock_module/scripts/run_risk_gate.py` | One brief JSON → one risk gate review JSON |
| `future_modules/stock_module/scripts/README.md` | Run instructions for confirm, brief, risk gate |
| `future_modules/stock_module/schemas/watchlist_packet.schema.json` | Watchlist packet schema |
| `future_modules/stock_module/inputs/confirmed_watchlist_packet_aapl.json` | Proof: confirmed AAPL packet |
| `future_modules/stock_module/outputs/stock_research_brief_confirmed_watchlist_packet_aapl.json` | Proof: AAPL brief output |
| `future_modules/stock_module/outputs/risk_gate_review_confirmed_watchlist_packet_aapl.json` | Proof: AAPL risk gate review |
| `future_modules/stock_module/examples/example_watchlist_packet_single.json` | Example one-symbol packet |

### Research Swarm
| Path | Why it matters |
|------|----------------|
| `future_modules/research_swarm/outputs/stock_symbol_review_summary.json` | Source for candidate symbols; built by `build_stock_symbol_review.py` |
| `future_modules/research_swarm/outputs/draft_watchlist_packet_from_rs.json` | Draft watchlist consumed by Stock Intake; can feed Stock Module (after single-symbol slice) |
| `future_modules/research_swarm/scripts/build_stock_symbol_review.py` | Aggregates extraction reports → `stock_symbol_review_summary.json` |

### Supporting docs
| Path | Why it matters |
|------|----------------|
| `JARVIS_CODEBASE_STRUCTURE.md` | Workspace layout; dashboard routes, future_modules |
| `future_modules/stock_module/README.md` | Stock Module overview; documents /stock-intake and /stock-briefs routes |
| `future_modules/research_swarm/outputs/README.md` | Output artifacts including stock symbol summary and draft watchlist |

---

## 5. Critical live files

### dashboard/src/app/stock-intake/page.tsx

```tsx
import {
  getStockSymbolReviewSummary,
  getDraftWatchlistPacket,
} from "@/lib/data";
import { HudMetricCard } from "@/components/HudMetricCard";

export const dynamic = "force-dynamic";
export const fetchCache = "force-no-store";

function shortenUrl(url: string, maxLen = 45): string {
  try {
    const u = new URL(url);
    const host = u.hostname.replace("www.", "");
    const path = u.pathname.replace(/\/$/, "");
    const full = path ? `${host}${path}` : host;
    return full.length > maxLen ? full.slice(0, maxLen - 1) + "…" : full;
  } catch {
    return url.length > maxLen ? url.slice(0, maxLen - 1) + "…" : url;
  }
}

export default async function StockIntakePage() {
  const [summary, draft] = await Promise.all([
    getStockSymbolReviewSummary(),
    getDraftWatchlistPacket(),
  ]);

  const symbols = summary?.symbols ?? [];
  const draftSymbols = new Set(draft?.symbols ?? []);
  const reportCount = summary?.report_count ?? 0;
  const symbolCount = summary?.symbol_count ?? 0;

  const hasData = reportCount > 0 || symbolCount > 0 || (draft?.symbols?.length ?? 0) > 0;

  if (!hasData) {
    return (
      <div className="space-y-6">
        <h2 className="text-xl font-semibold tracking-tight text-cyan-100">
          Stock Intake Review
        </h2>
        <p className="text-sm text-slate-500">
          This page shows which stock symbols were found in Research Swarm and
          the draft watchlist before anything runs through the Stock Module.
        </p>
        <div className="hud-panel p-6">
          <p className="text-amber-400/90">
            No stock intake data found yet.
          </p>
          <p className="mt-2 text-sm text-slate-500">
            Run the symbol review builder and create a draft watchlist packet:
          </p>
          <pre className="mt-3 overflow-x-auto rounded bg-slate-900/50 p-3 font-mono text-xs text-slate-300">
            {`cd future_modules/research_swarm/scripts
python build_stock_symbol_review.py

# Then create draft_watchlist_packet_from_rs.json in outputs/`}
          </pre>
        </div>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <div className="flex items-end justify-between gap-4 border-b border-cyan-500/20 pb-4">
        <div>
          <h2 className="text-xl font-semibold tracking-tight text-cyan-100">
            Stock Intake Review
          </h2>
          <p className="mt-1 text-sm text-slate-500">
            Stock symbols found in Research Swarm. This is a manual review step
            before anything becomes a real stock-module run.
          </p>
        </div>
      </div>

      <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
        <HudMetricCard
          label="Research sources reviewed"
          value={reportCount}
        />
        <HudMetricCard
          label="Candidate symbols found"
          value={symbolCount}
        />
        <HudMetricCard
          label="Draft watchlist ready"
          value={draft?.symbols?.length ?? 0}
          variant={(draft?.symbols?.length ?? 0) > 0 ? "healthy" : "default"}
        />
        <div className="hud-metric p-3">
          <div className="text-xs uppercase tracking-wider text-slate-500">
            Manual review status
          </div>
          <div className="mt-1 text-xl font-semibold text-amber-400/90">
            Required
          </div>
          <p className="mt-0.5 text-[11px] text-slate-600">
            A person still needs to approve this before it moves forward.
          </p>
        </div>
      </div>

      <div className="hud-panel p-4">
        <h3 className="mb-1 text-xs font-medium uppercase tracking-widest text-cyan-400/80">
          Top candidate symbols
        </h3>
        <p className="mb-3 text-xs text-slate-500">
          Symbols extracted from Research Swarm. Sorted by how often they appear
          across different sources.
        </p>
        {symbols.length === 0 ? (
          <p className="text-sm text-slate-500">No symbols in summary yet.</p>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full text-left text-sm">
              <thead>
                <tr className="border-b border-slate-600/50">
                  <th className="pb-2 pr-3 font-medium text-cyan-400/90">Symbol</th>
                  <th className="pb-2 pr-3 font-medium text-cyan-400/90">Seen In Sources</th>
                  <th className="pb-2 pr-3 font-medium text-cyan-400/90">Times Found</th>
                  <th className="pb-2 pr-3 font-medium text-cyan-400/90">Example Source</th>
                  <th className="pb-2 pr-3 font-medium text-cyan-400/90">Suggested Status</th>
                  <th className="pb-2 pr-3 font-medium text-cyan-400/90">Why It Matters</th>
                </tr>
              </thead>
              <tbody>
                {symbols.map((s) => {
                  const inDraft = draftSymbols.has(s.symbol);
                  const suggestedStatus = inDraft ? "In draft" : s.source_count >= 2 ? "Candidate" : "Single source";
                  const why = inDraft ? "Selected for first research step" : s.source_count >= 2 ? `Found in ${s.source_count} different sources` : "Only in one source—needs review";
                  const exampleUrl = s.example_source_urls?.[0] ?? "—";
                  return (
                    <tr key={s.symbol} className="border-b border-slate-700/30">
                      <td className="py-2 pr-3 font-mono text-cyan-200">{s.symbol}</td>
                      <td className="py-2 pr-3 text-slate-300">{s.source_count}</td>
                      <td className="py-2 pr-3 text-slate-300">{s.occurrence_count}</td>
                      <td className="max-w-[180px] truncate py-2 pr-3 text-slate-400">
                        {typeof exampleUrl === "string" && exampleUrl !== "—" ? shortenUrl(exampleUrl) : exampleUrl}
                      </td>
                      <td className="py-2 pr-3">
                        <span className={inDraft ? "rounded bg-teal-500/20 px-1.5 py-0.5 text-xs text-teal-300" : "text-slate-400"}>
                          {suggestedStatus}
                        </span>
                      </td>
                      <td className="max-w-[200px] py-2 pr-3 text-xs text-slate-500">{why}</td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        )}
        <div className="mt-3 grid gap-2 border-t border-slate-700/30 pt-3 text-[11px] text-slate-600 sm:grid-cols-2">
          <span><strong>Seen In Sources:</strong> How many different source links mentioned this symbol.</span>
          <span><strong>Times Found:</strong> How many total reports mentioned this symbol. Can be higher than source count if the same source was processed more than once.</span>
        </div>
      </div>

      <div className="hud-panel p-4">
        <h3 className="mb-1 text-xs font-medium uppercase tracking-widest text-cyan-400/80">Draft watchlist</h3>
        <p className="mb-3 text-xs text-slate-500">
          A small starter list of symbols being considered for the next stock research step.
        </p>
        {!draft || (draft.symbols?.length ?? 0) === 0 ? (
          <p className="text-sm text-slate-500">No draft watchlist packet found.</p>
        ) : (
          <div className="space-y-3">
            <div>
              <div className="text-xs text-slate-500">Current draft symbols</div>
              <div className="mt-1 flex flex-wrap gap-2">
                {(draft.symbols ?? []).map((sym) => (
                  <span key={sym} className="rounded bg-cyan-500/15 px-2 py-1 font-mono text-sm text-cyan-200 ring-1 ring-cyan-500/30">{sym}</span>
                ))}
              </div>
            </div>
            {draft.watch_reason && (
              <div>
                <div className="text-xs text-slate-500">Why these were selected</div>
                <p className="mt-1 text-sm text-slate-300">{draft.watch_reason}</p>
              </div>
            )}
            {draft.notes && (
              <div>
                <div className="text-xs text-slate-500">Review note</div>
                <p className="mt-1 text-sm text-slate-300">{draft.notes}</p>
              </div>
            )}
            <div className="rounded border border-amber-500/30 bg-amber-500/10 p-3">
              <span className="text-sm font-medium text-amber-400/90">Manual review required</span>
              <p className="mt-0.5 text-xs text-slate-500">A person still needs to approve this before it moves forward.</p>
            </div>
          </div>
        )}
      </div>

      <div className="hud-panel p-4">
        <h3 className="mb-1 text-xs font-medium uppercase tracking-widest text-cyan-400/80">What happens next</h3>
        <ol className="list-inside list-decimal space-y-2 text-sm text-slate-300">
          <li>Review the candidate symbols above</li>
          <li>Confirm the draft watchlist</li>
          <li>Run the first stock research brief (one symbol at a time)</li>
          <li>Run risk gate on the brief (`run_risk_gate.py`)</li>
          <li>Review brief + risk gate on dashboard `/stock-briefs`</li>
        </ol>
      </div>
    </div>
  );
}
```

### dashboard/src/app/stock-briefs (behavior summary; full source on disk)

- Loads `getLatestStockResearchBrief()` + `getRiskGateReviewForLatestBrief()` in parallel.
- Risk gate file must pair by suffix with the latest brief filename (`risk_gate_review_` + stem after `stock_research_brief_`).
- UI: risk gate status card, glossary for pass/caution/flag, section for overall status / summary / flags or “no flags”; amber panel if gate file missing with example `run_risk_gate.py` command; footer manual-review-only.

### dashboard/src/lib/data.ts (stock intake section only)

```typescript
/** Stock symbol review summary shape (from stock_symbol_review_summary.json) */
export interface StockSymbolReviewSummary {
  generated_from?: string;
  report_count?: number;
  symbol_count?: number;
  symbols?: Array<{
    symbol: string;
    occurrence_count: number;
    source_count: number;
    example_source_urls?: string[];
    example_packet_ids?: string[];
    stock_relevant_sources?: number;
    all_sources_stock_relevant?: boolean;
  }>;
}

/** Draft watchlist packet shape (from draft_watchlist_packet_from_rs.json) */
export interface DraftWatchlistPacket {
  packet_id?: string;
  created_at?: string;
  symbols?: string[];
  watch_reason?: string;
  time_horizon?: string;
  risk_tolerance?: string;
  notes?: string;
}

export async function getStockSymbolReviewSummary(): Promise<StockSymbolReviewSummary | null> {
  try {
    const workspaceRoot = join(process.cwd(), "..");
    const path = join(workspaceRoot, "future_modules", "research_swarm", "outputs", "stock_symbol_review_summary.json");
    const raw = await readFile(path, "utf-8");
    return JSON.parse(raw) as StockSymbolReviewSummary;
  } catch {
    return null;
  }
}

export async function getDraftWatchlistPacket(): Promise<DraftWatchlistPacket | null> {
  try {
    const workspaceRoot = join(process.cwd(), "..");
    const path = join(workspaceRoot, "future_modules", "research_swarm", "outputs", "draft_watchlist_packet_from_rs.json");
    const raw = await readFile(path, "utf-8");
    return JSON.parse(raw) as DraftWatchlistPacket;
  } catch {
    return null;
  }
}
```

### future_modules/stock_module/module_spec.md

```markdown
# Stock Module v1 Spec

**Status:** prototype | **Last updated:** 2026-03-20

## Purpose
Produce bounded market research briefs from ticker/watchlist packets. Summarize catalysts, risks, and evidence for human review. No trading, no execution.

## Inputs
- packet_id, symbols (required), watch_reason, constraints
- Schema: schemas/watchlist_packet.schema.json

## Outputs
- Stock research brief (per-symbol: thesis, catalysts, risks, evidence, confidence)
- Risk gate review (caution, insufficient evidence, conflicting signals)
- Schemas: stock_research_brief.schema.json, risk_gate_review.schema.json

## Workflow
1. Intake — Watchlist packet
2. Research — Generate brief per symbol
3. Risk gate — Apply caution rules
4. Output — Research brief + risk gate for human review

## First Viable Slice
- Input: One watchlist packet; exactly one symbol
- Process: Research → structured brief → risk gate review
- Output: One research brief; one risk gate review
- Success: Evidence cited; risk gate applied; confidence band; no forbidden language
```

### future_modules/research_swarm/outputs/stock_symbol_review_summary.json (excerpt)

```json
{
  "generated_from": "extraction_report_*_api.json in research_swarm/outputs/",
  "report_count": 7,
  "symbol_count": 13,
  "symbols": [
    {
      "symbol": "AAPL",
      "occurrence_count": 6,
      "source_count": 4,
      "example_source_urls": ["https://github.com/matthewchung74/llm_trader", ...]
    },
    ...
  ]
}
```

### future_modules/research_swarm/outputs/draft_watchlist_packet_from_rs.json

```json
{
  "packet_id": "rs-draft-watch-001",
  "created_at": "2026-03-21T20:00:00Z",
  "symbols": ["AAPL", "MSFT", "NVDA", "QQQ"],
  "watch_reason": "Research Swarm extraction: 4 symbols with source_count ≥ 2 across stock/trading agent repos and articles. First draft from RS→Stock bridge.",
  "time_horizon": "short-term",
  "risk_tolerance": "moderate",
  "notes": "MANUAL REVIEW REQUIRED. Draft from stock_symbol_review_summary.json. Selection: source_count primary, occurrence_count secondary. Included: AAPL (4 src), MSFT (3), NVDA (3), QQQ (2). Excluded: IBKR (broker scope), INFY/TCS/ICICI (non-US), GOOGL/TSLA/SPY/AMZN/XLE (source_count=1). Source: 7 RS extraction reports, 5 distinct URLs."
}
```

---

## 6. Established decisions / constraints

- This is a **review/intake flow**, not a stock analytics terminal.
- Use **plain-English labels** (e.g. "Seen In Sources", "Times Found", "Why It Matters").
- **Do not invent** market data, prices, returns, scores, or confidence metrics.
- **Manual review required** — explicit callout on draft watchlist.
- Stock Intake page reads **current repo truth only** from the two JSON artifacts.
- `/stock-briefs` reads brief + paired risk-gate JSON from disk; **no** invented prices or execution.
- `run_research_brief.py` enforces **exactly one symbol** (first viable slice).
- No Stock Module scripts or Research Swarm extractor logic were modified in Prompt #94.
- Keep intake lane **tightly bounded**; no filters, sorting, charts, fake analytics.

---

## 7. Gaps / missing pieces

- **draft_watchlist_packet_from_rs.json creation:** No script; manual or ad-hoc.
- **Path assumption:** Dashboard assumes `process.cwd()` = dashboard root; `join(process.cwd(), "..")` = workspace root. May fail if dashboard runs with different cwd.
- **Pipeline:** `run_pipeline.py` not implemented (three separate CLI steps).
- **Brief / risk pairing:** Latest brief by mtime; risk gate only if paired filename exists — not validated against `report_id` inside JSON.
- **Brief file switcher:** No history or symbol switcher when multiple brief files exist.
- **Single-symbol constraint:** One symbol per run; operator must run confirm + brief for each symbol.
- **Advisory only:** Brief content is not real-time market data; no trades executed.

---

## 8. Recommended next move

**`run_pipeline.py`:** One bounded script that chains existing steps (same inputs/outputs, same schemas), prints the same manual-review warnings — only if you want less copy-paste between three CLIs. Alternative when pain is real: a **minimal brief/risk switcher** on `/stock-briefs` after multiple `outputs/` files exist.

---

## 9. New-chat starter block

```
We are continuing an existing stock-module effort. Do not restart from theory.

**Read the handoff bundle first:** `future_modules/stock_module/STOCK_MODULE_HANDOFF_BUNDLE_CURRENT.md`

Use it as the source of truth unless repo evidence overrides an outdated claim.

**Last verified checkpoint:** Prompt #109 — Flow proven: `/stock-intake` → `confirm_watchlist_symbol.py` → `run_research_brief.py` → `run_risk_gate.py` → `/stock-briefs` (brief + paired risk gate, or missing-gate guidance). One symbol per brief. Manual only. Not a trading engine.

**Current focus:** Stock-module / dashboard / RS intake lane. Next bounded move: `run_pipeline.py` (optional chain) or brief/risk switcher only if multiple output files justify it.
```
