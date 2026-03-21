import {
  getResearchSwarmLatestRun,
  getResearchSwarmLedgerRows,
} from "@/lib/data";
import { HudMetricCard } from "@/components/HudMetricCard";

export const dynamic = "force-dynamic";
export const fetchCache = "force-no-store";

function outcomeColor(outcome: string): string {
  switch (outcome) {
    case "success":
      return "text-teal-400";
    case "partial":
      return "text-amber-400";
    case "fail":
      return "text-red-400";
    case "skipped":
      return "text-slate-500";
    default:
      return "text-slate-400";
  }
}

export default async function ResearchSwarmPage() {
  const [summary, ledgerRows] = await Promise.all([
    getResearchSwarmLatestRun(),
    getResearchSwarmLedgerRows(25),
  ]);

  if (!summary) {
    return (
      <div className="space-y-6">
        <h2 className="text-xl font-semibold tracking-tight text-cyan-100">
          Research Swarm
        </h2>
        <div className="hud-panel p-6">
          <p className="text-amber-400/90">
            No Phase A collection run data found. Run the collector first:
          </p>
          <pre className="mt-3 overflow-x-auto rounded bg-slate-900/50 p-3 font-mono text-xs text-slate-300">
            {`cd future_modules/research_swarm/scripts
python run_phase_a_collector.py --urls-file ../docs/Example URLs.txt`}
          </pre>
          <p className="mt-3 text-sm text-slate-500">
            Outputs expected in{" "}
            <code className="rounded bg-slate-800 px-1 py-0.5 font-mono text-xs">
              future_modules/research_swarm/outputs/
            </code>
          </p>
        </div>
      </div>
    );
  }

  const supported = summary.github + summary.article;
  const bottleneck =
    summary.recurring_failures?.[0]?.reason ?? "None identified in this run";

  return (
    <div className="space-y-6">
      <div className="flex items-end justify-between gap-4 border-b border-cyan-500/20 pb-4">
        <h2 className="text-xl font-semibold tracking-tight text-cyan-100">
          Research Swarm
        </h2>
        <div className="text-right text-xs text-slate-500">
          Run: {summary.run_id} | {new Date(summary.started_at).toLocaleString()}
        </div>
      </div>

      <div className="rounded border border-cyan-500/20 bg-cyan-500/5 p-3">
        <div className="text-xs font-medium uppercase tracking-wider text-cyan-400/80">
          Input
        </div>
        <div className="mt-1 truncate text-sm text-slate-300">
          {summary.urls_file ?? "—"}
        </div>
        {summary.queries_file && (
          <div className="mt-1 text-xs text-slate-500">
            Discovery: {summary.queries_file}
          </div>
        )}
      </div>

      <div className="grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-6">
        <HudMetricCard label="Raw from list" value={summary.raw_from_list} />
        <HudMetricCard label="After dedup" value={summary.after_merge_dedup} />
        <HudMetricCard label="Supported" value={supported} />
        <HudMetricCard
          label="Unsupported"
          value={summary.unsupported_video + summary.unsupported_other}
        />
        <HudMetricCard
          label="Success"
          value={summary.success}
          variant={summary.success > 0 ? "healthy" : "default"}
        />
        <HudMetricCard label="Partial" value={summary.partial} />
        <HudMetricCard label="Fail" value={summary.fail} />
        <HudMetricCard label="Skipped (restricted)" value={summary.skipped_restricted} />
        <HudMetricCard label="Skipped (unsupported)" value={summary.skipped_unsupported} />
      </div>

      <div className="hud-panel p-4">
        <h3 className="mb-2 text-xs font-medium uppercase tracking-widest text-cyan-400/80">
          Source class breakdown
        </h3>
        <div className="flex flex-wrap gap-4 text-sm">
          <span>
            GitHub: <span className="text-cyan-200">{summary.github}</span>
          </span>
          <span>
            Article: <span className="text-cyan-200">{summary.article}</span>
          </span>
          <span>
            Unsupported video:{" "}
            <span className="text-slate-500">{summary.unsupported_video}</span>
          </span>
          <span>
            Unsupported other:{" "}
            <span className="text-slate-500">{summary.unsupported_other}</span>
          </span>
        </div>
      </div>

      <div className="hud-panel p-4">
        <h3 className="mb-2 text-xs font-medium uppercase tracking-widest text-cyan-400/80">
          Primary bottleneck / failure pattern
        </h3>
        <p className="truncate text-sm text-slate-300">{bottleneck}</p>
      </div>

      <div className="hud-panel p-4">
        <h3 className="mb-3 text-xs font-medium uppercase tracking-widest text-cyan-400/80">
          Recent ledger items (latest {ledgerRows.length})
        </h3>
        {ledgerRows.length === 0 ? (
          <p className="text-sm text-slate-500">No ledger entries yet.</p>
        ) : (
          <div className="overflow-x-auto">
            <table className="min-w-full divide-y divide-slate-700/50">
              <thead>
                <tr>
                  <th className="px-3 py-2 text-left text-xs font-medium text-slate-500">
                    Outcome
                  </th>
                  <th className="px-3 py-2 text-left text-xs font-medium text-slate-500">
                    Class
                  </th>
                  <th className="px-3 py-2 text-left text-xs font-medium text-slate-500">
                    URL
                  </th>
                  <th className="px-3 py-2 text-left text-xs font-medium text-slate-500">
                    Usefulness
                  </th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-700/30">
                {ledgerRows.map((row, i) => (
                  <tr key={i} className="text-sm">
                    <td className={`whitespace-nowrap px-3 py-2 font-medium ${outcomeColor(row.outcome)}`}>
                      {row.outcome}
                    </td>
                    <td className="px-3 py-2 text-slate-400">{row.source_class}</td>
                    <td className="max-w-[320px] truncate px-3 py-2 text-slate-300">
                      {row.source_url}
                    </td>
                    <td className="px-3 py-2 text-slate-500">
                      {row.usefulness ?? "—"}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
}
