import {
  getResearchSwarmLatestRun,
  getResearchSwarmAllLedgerRows,
} from "@/lib/data";
import { HudMetricCard } from "@/components/HudMetricCard";

export const dynamic = "force-dynamic";
export const fetchCache = "force-no-store";

function outcomeColor(outcome: string): string {
  switch (outcome) {
    case "success":
      return "text-success";
    case "partial":
      return "text-warning";
    case "fail":
      return "text-destructive";
    case "skipped":
      return "text-muted-foreground";
    default:
      return "text-muted-foreground";
  }
}

export default async function ResearchSwarmPage() {
  const [summary, ledgerRows] = await Promise.all([
    getResearchSwarmLatestRun(),
    getResearchSwarmAllLedgerRows(),
  ]);
  const recentLedgerRows = ledgerRows.slice(0, 25);

  if (!summary) {
    return (
      <div className="space-y-6">
        <h2 className="text-xl font-semibold tracking-tight text-foreground">
          Research Swarm
        </h2>
        <div className="hud-panel p-6">
          <p className="text-warning">
            No Phase A collection run data found. Run the collector first:
          </p>
          <pre className="mt-3 overflow-x-auto rounded-lg border border-border bg-muted p-3 font-mono text-xs text-foreground">
            {`cd future_modules/research_swarm/scripts
python run_phase_a_collector.py --urls-file ../docs/Example URLs.txt`}
          </pre>
          <p className="mt-3 text-sm text-muted-foreground">
            Outputs expected in{" "}
            <code className="rounded bg-muted px-1 py-0.5 font-mono text-xs text-foreground">
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
      <div className="flex items-end justify-between gap-4 border-b border-border pb-4">
        <h2 className="text-xl font-semibold tracking-tight text-foreground">
          Research Swarm
        </h2>
        <div className="text-right text-xs text-muted-foreground">
          Run: {summary.run_id} | {new Date(summary.started_at).toLocaleString()}
        </div>
      </div>

      <div className="rounded-lg border border-border bg-card p-3">
        <div className="text-xs font-medium uppercase tracking-wider text-muted-foreground">
          Input
        </div>
        <div className="mt-1 truncate text-sm text-foreground">
          {summary.urls_file ?? "—"}
        </div>
        {summary.queries_file && (
          <div className="mt-1 text-xs text-muted-foreground">
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
          value={summary.unsupported}
        />
        <HudMetricCard
          label="Success"
          value={summary.success}
          variant={summary.success > 0 ? "healthy" : "default"}
        />
        <HudMetricCard label="Partial" value={summary.partial} />
        <HudMetricCard label="Fail" value={summary.fail} />
        <HudMetricCard label="Skipped" value={summary.skipped} />
      </div>

      <div className="hud-panel p-4">
        <h3 className="mb-2 text-xs font-medium uppercase tracking-widest text-muted-foreground">
          Source class breakdown
        </h3>
        <div className="flex flex-wrap gap-4 text-sm">
          <span>
            GitHub: <span className="text-foreground">{summary.github}</span>
          </span>
          <span>
            Article: <span className="text-foreground">{summary.article}</span>
          </span>
          <span>
            Unsupported:{" "}
            <span className="text-muted-foreground">{summary.unsupported}</span>
          </span>
        </div>
      </div>

      <div className="hud-panel p-4">
        <h3 className="mb-2 text-xs font-medium uppercase tracking-widest text-muted-foreground">
          Primary bottleneck / failure pattern
        </h3>
        <p className="truncate text-sm text-foreground">{bottleneck}</p>
      </div>

      <div className="hud-panel p-4">
        <h3 className="mb-3 text-xs font-medium uppercase tracking-widest text-muted-foreground">
          Recent ledger items (latest {recentLedgerRows.length})
        </h3>
        {recentLedgerRows.length === 0 ? (
          <p className="text-sm text-muted-foreground">No ledger entries yet.</p>
        ) : (
          <div className="overflow-x-auto">
            <table className="min-w-full divide-y divide-border">
              <thead>
                <tr>
                  <th className="px-3 py-2 text-left text-xs font-medium text-muted-foreground">
                    Outcome
                  </th>
                  <th className="px-3 py-2 text-left text-xs font-medium text-muted-foreground">
                    Class
                  </th>
                  <th className="px-3 py-2 text-left text-xs font-medium text-muted-foreground">
                    URL
                  </th>
                  <th className="px-3 py-2 text-left text-xs font-medium text-muted-foreground">
                    Usefulness
                  </th>
                </tr>
              </thead>
              <tbody className="divide-y divide-border">
                {recentLedgerRows.map((row, i) => (
                  <tr key={i} className="text-sm">
                    <td className={`whitespace-nowrap px-3 py-2 font-medium ${outcomeColor(row.outcome)}`}>
                      {row.outcome}
                    </td>
                    <td className="px-3 py-2 text-muted-foreground">{row.source_class}</td>
                    <td className="max-w-[320px] truncate px-3 py-2 text-foreground">
                      {row.source_url}
                    </td>
                    <td className="px-3 py-2 text-muted-foreground">
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
