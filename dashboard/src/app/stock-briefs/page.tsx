import { getLatestStockResearchBrief } from "@/lib/data";
import { HudMetricCard } from "@/components/HudMetricCard";

export const dynamic = "force-dynamic";
export const fetchCache = "force-no-store";

export default async function StockBriefsPage() {
  const brief = await getLatestStockResearchBrief();

  if (!brief || !brief.briefs?.length) {
    return (
      <div className="space-y-6">
        <h2 className="text-xl font-semibold tracking-tight text-cyan-100">
          Stock Brief Review
        </h2>
        <p className="text-sm text-slate-500">
          This page shows the latest Stock Module research brief output. This is
          a manual review step, not a trading decision screen.
        </p>
        <div className="hud-panel p-6">
          <p className="text-amber-400/90">
            No stock brief output found yet.
          </p>
          <p className="mt-2 text-sm text-slate-500">
            Run the research brief first:
          </p>
          <pre className="mt-3 overflow-x-auto rounded bg-slate-900/50 p-3 font-mono text-xs text-slate-300">
            {`cd future_modules/stock_module/scripts
python confirm_watchlist_symbol.py --symbol AAPL
python run_research_brief.py --packet ../inputs/confirmed_watchlist_packet_aapl.json`}
          </pre>
        </div>
      </div>
    );
  }

  const b = brief.briefs[0];
  const symbol = b.symbol ?? "—";
  const confidenceBand = b.confidence_band ?? "—";
  const reviewRec = b.review_recommendation ?? "—";
  const evidenceSources = b.evidence_sources ?? [];
  const openQuestions = b.open_questions ?? [];

  return (
    <div className="space-y-6">
      <div className="flex items-end justify-between gap-4 border-b border-cyan-500/20 pb-4">
        <div>
          <h2 className="text-xl font-semibold tracking-tight text-cyan-100">
            Stock Brief Review
          </h2>
          <p className="mt-1 text-sm text-slate-500">
            Latest Stock Module research brief output. Manual review step, not a
            trading decision screen.
          </p>
        </div>
      </div>

      <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
        <HudMetricCard label="Brief files found" value="1" />
        <HudMetricCard label="Latest symbol reviewed" value={symbol} />
        <div className="hud-metric p-3">
          <div className="text-xs uppercase tracking-wider text-slate-500">
            Confidence band
          </div>
          <div className="mt-1 text-xl font-semibold text-cyan-200">
            {confidenceBand}
          </div>
          <p className="mt-0.5 text-[11px] text-slate-600">
            The model&apos;s rough confidence based on the evidence it used. Not a
            guarantee.
          </p>
        </div>
        <div className="hud-metric p-3">
          <div className="text-xs uppercase tracking-wider text-slate-500">
            Review recommendation
          </div>
          <div className="mt-1 text-xl font-semibold text-cyan-200">
            {reviewRec}
          </div>
          <p className="mt-0.5 text-[11px] text-slate-600">
            Suggested watch posture (e.g. monitor, dig deeper). A person still
            decides the real next move.
          </p>
        </div>
      </div>

      <div className="hud-panel p-4">
        <h3 className="mb-1 text-xs font-medium uppercase tracking-widest text-cyan-400/80">
          Brief summary
        </h3>
        <div className="space-y-4">
          <div>
            <div className="text-xs text-slate-500">Symbol</div>
            <p className="mt-1 font-mono text-cyan-200">{symbol}</p>
          </div>
          {b.thesis_or_watch_reason && (
            <div>
              <div className="text-xs text-slate-500">
                Why it is on the watchlist
              </div>
              <p className="mt-1 text-sm text-slate-300">
                {b.thesis_or_watch_reason}
              </p>
            </div>
          )}
          {b.catalyst_summary && (
            <div>
              <div className="text-xs text-slate-500">Main catalysts</div>
              <p className="mt-0.5 text-[11px] text-slate-600">
                Events or conditions that could help move the stock.
              </p>
              <p className="mt-1 text-sm text-slate-300">
                {b.catalyst_summary}
              </p>
            </div>
          )}
          {b.risk_summary && (
            <div>
              <div className="text-xs text-slate-500">Main risks</div>
              <p className="mt-1 text-sm text-slate-300">{b.risk_summary}</p>
            </div>
          )}
          {openQuestions.length > 0 && (
            <div>
              <div className="text-xs text-slate-500">Open questions</div>
              <p className="mt-0.5 text-[11px] text-slate-600">
                Important unknowns to check before acting.
              </p>
              <ul className="mt-1 list-inside list-disc space-y-0.5 text-sm text-slate-300">
                {openQuestions.map((q, i) => (
                  <li key={i}>{q}</li>
                ))}
              </ul>
            </div>
          )}
          {reviewRec && reviewRec !== "—" && (
            <div>
              <div className="text-xs text-slate-500">Suggested next posture</div>
              <p className="mt-1 text-sm text-cyan-200">{reviewRec}</p>
            </div>
          )}
        </div>
      </div>

      {evidenceSources.length > 0 && (
        <div className="hud-panel p-4">
          <h3 className="mb-1 text-xs font-medium uppercase tracking-widest text-cyan-400/80">
            Evidence used
          </h3>
          <p className="mb-3 text-xs text-slate-500">
            Sources referenced in the brief. Titles and dates as provided by the
            model.
          </p>
          <div className="space-y-2">
            {evidenceSources.map((src, i) => (
              <div
                key={i}
                className="flex flex-wrap items-baseline gap-2 rounded border border-slate-700/40 bg-slate-900/30 px-3 py-2 text-sm"
              >
                <span className="font-medium text-slate-400">
                  {src.type ?? "source"}
                </span>
                <span className="text-slate-300">{src.title ?? "—"}</span>
                {src.date && (
                  <span className="text-xs text-slate-600">{src.date}</span>
                )}
              </div>
            ))}
          </div>
        </div>
      )}

      <div className="rounded border border-amber-500/30 bg-amber-500/10 p-4">
        <h3 className="text-sm font-medium text-amber-400/90">
          Manual review required
        </h3>
        <p className="mt-1 text-sm text-slate-300">
          This brief was generated for operator review. It does not execute
          trades. It is not real-time market data. A person still has to decide
          what to do next.
        </p>
      </div>
    </div>
  );
}
