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
                  <th className="pb-2 pr-3 font-medium text-cyan-400/90">
                    Symbol
                  </th>
                  <th className="pb-2 pr-3 font-medium text-cyan-400/90">
                    Seen In Sources
                  </th>
                  <th className="pb-2 pr-3 font-medium text-cyan-400/90">
                    Times Found
                  </th>
                  <th className="pb-2 pr-3 font-medium text-cyan-400/90">
                    Example Source
                  </th>
                  <th className="pb-2 pr-3 font-medium text-cyan-400/90">
                    Suggested Status
                  </th>
                  <th className="pb-2 pr-3 font-medium text-cyan-400/90">
                    Why It Matters
                  </th>
                </tr>
              </thead>
              <tbody>
                {symbols.map((s) => {
                  const inDraft = draftSymbols.has(s.symbol);
                  const suggestedStatus = inDraft
                    ? "In draft"
                    : s.source_count >= 2
                      ? "Candidate"
                      : "Single source";
                  const why =
                    inDraft
                      ? "Selected for first research step"
                      : s.source_count >= 2
                        ? `Found in ${s.source_count} different sources`
                        : "Only in one source—needs review";
                  const exampleUrl = s.example_source_urls?.[0] ?? "—";
                  return (
                    <tr
                      key={s.symbol}
                      className="border-b border-slate-700/30"
                    >
                      <td className="py-2 pr-3 font-mono text-cyan-200">
                        {s.symbol}
                      </td>
                      <td className="py-2 pr-3 text-slate-300">
                        {s.source_count}
                      </td>
                      <td className="py-2 pr-3 text-slate-300">
                        {s.occurrence_count}
                      </td>
                      <td className="max-w-[180px] truncate py-2 pr-3 text-slate-400">
                        {typeof exampleUrl === "string" && exampleUrl !== "—"
                          ? shortenUrl(exampleUrl)
                          : exampleUrl}
                      </td>
                      <td className="py-2 pr-3">
                        <span
                          className={
                            inDraft
                              ? "rounded bg-teal-500/20 px-1.5 py-0.5 text-xs text-teal-300"
                              : "text-slate-400"
                          }
                        >
                          {suggestedStatus}
                        </span>
                      </td>
                      <td className="max-w-[200px] py-2 pr-3 text-xs text-slate-500">
                        {why}
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        )}
        <div className="mt-3 grid gap-2 border-t border-slate-700/30 pt-3 text-[11px] text-slate-600 sm:grid-cols-2">
          <span>
            <strong>Seen In Sources:</strong> How many different source links
            mentioned this symbol.
          </span>
          <span>
            <strong>Times Found:</strong> How many total reports mentioned this
            symbol. Can be higher than source count if the same source was
            processed more than once.
          </span>
        </div>
      </div>

      <div className="hud-panel p-4">
        <h3 className="mb-1 text-xs font-medium uppercase tracking-widest text-cyan-400/80">
          Draft watchlist
        </h3>
        <p className="mb-3 text-xs text-slate-500">
          A small starter list of symbols being considered for the next stock
          research step.
        </p>
        {!draft || (draft.symbols?.length ?? 0) === 0 ? (
          <p className="text-sm text-slate-500">
            No draft watchlist packet found.
          </p>
        ) : (
          <div className="space-y-3">
            <div>
              <div className="text-xs text-slate-500">
                Current draft symbols
              </div>
              <div className="mt-1 flex flex-wrap gap-2">
                {(draft.symbols ?? []).map((sym) => (
                  <span
                    key={sym}
                    className="rounded bg-cyan-500/15 px-2 py-1 font-mono text-sm text-cyan-200 ring-1 ring-cyan-500/30"
                  >
                    {sym}
                  </span>
                ))}
              </div>
            </div>
            {draft.watch_reason && (
              <div>
                <div className="text-xs text-slate-500">
                  Why these were selected
                </div>
                <p className="mt-1 text-sm text-slate-300">
                  {draft.watch_reason}
                </p>
              </div>
            )}
            {draft.notes && (
              <div>
                <div className="text-xs text-slate-500">Review note</div>
                <p className="mt-1 text-sm text-slate-300">{draft.notes}</p>
              </div>
            )}
            <div className="rounded border border-amber-500/30 bg-amber-500/10 p-3">
              <span className="text-sm font-medium text-amber-400/90">
                Manual review required
              </span>
              <p className="mt-0.5 text-xs text-slate-500">
                A person still needs to approve this before it moves forward.
              </p>
            </div>
          </div>
        )}
      </div>

      <div className="hud-panel p-4">
        <h3 className="mb-1 text-xs font-medium uppercase tracking-widest text-cyan-400/80">
          What happens next
        </h3>
        <ol className="list-inside list-decimal space-y-2 text-sm text-slate-300">
          <li>Review the candidate symbols above</li>
          <li>Confirm the draft watchlist</li>
          <li>Run the first stock research brief (one symbol at a time)</li>
        </ol>
      </div>
    </div>
  );
}
