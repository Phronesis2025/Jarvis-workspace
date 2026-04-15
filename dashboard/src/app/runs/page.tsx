import { getRuns } from "@/lib/data";

export const dynamic = "force-dynamic";

import type { DashboardRun, OperatorCheckpoints } from "@/lib/types";
import { HudMetricCard } from "@/components/HudMetricCard";

function formatTimeAgo(iso: string): string {
  const date = new Date(iso);
  const now = new Date();
  const mins = Math.floor((now.getTime() - date.getTime()) / 60000);

  if (mins < 1) return "Just now";
  if (mins < 60) return `${mins}m ago`;

  const hrs = Math.floor(mins / 60);
  if (hrs < 24) return `${hrs}h ago`;

  const days = Math.floor(hrs / 24);
  return `${days}d ago`;
}

function formatDateTime(iso: string | null): string {
  if (!iso) return "—";
  return new Date(iso).toLocaleString();
}

function formatDuration(run: DashboardRun): string {
  const start = new Date(run.started_at).getTime();
  const end = run.ended_at ? new Date(run.ended_at).getTime() : Date.now();
  const totalMinutes = Math.max(0, Math.floor((end - start) / 60000));

  if (totalMinutes < 1) return "<1m";

  const hours = Math.floor(totalMinutes / 60);
  const minutes = totalMinutes % 60;

  if (hours === 0) return `${minutes}m`;
  return `${hours}h ${minutes}m`;
}

function isFailure(run: DashboardRun): boolean {
  const outcome = (run.outcome ?? "").toLowerCase();
  const stopReason = (run.stop_reason ?? "").toLowerCase();

  return (
    outcome.includes("fail") ||
    outcome.includes("error") ||
    stopReason.length > 0
  );
}

function isSuccess(run: DashboardRun): boolean {
  const outcome = (run.outcome ?? "").toLowerCase();

  return (
    outcome.includes("complete") ||
    outcome.includes("worker_complete") ||
    outcome.includes("success")
  );
}

function getRunState(run: DashboardRun): {
  label: string;
  className: string;
} {
  if (!run.ended_at) {
    return {
      label: "active",
      className: "border-primary/20 bg-primary/15 text-primary",
    };
  }

  if (isFailure(run)) {
    return {
      label: "failed",
      className: "border-warning/20 bg-warning/15 text-warning",
    };
  }

  if (isSuccess(run)) {
    return {
      label: "complete",
      className: "border-success/20 bg-success/15 text-success",
    };
  }

  return {
    label: "uncertain",
    className: "border-border bg-muted text-muted-foreground",
  };
}

function getTrustSummary(run: DashboardRun): {
  label: string;
  className: string;
  breakdown: Array<{ label: string; value: string }>;
} {
  const cp = (run.operator_checkpoints ?? {}) as OperatorCheckpoints;
  const breakdown = [
    cp.build ? { label: "Build", value: cp.build.status } : null,
    cp.smoke ? { label: "Smoke", value: cp.smoke.status } : null,
    cp.page_smoke
      ? {
          label: "Page smoke",
          value: cp.page_smoke.route
            ? `${cp.page_smoke.status} (${cp.page_smoke.route})`
            : cp.page_smoke.status,
        }
      : null,
    cp.manual_check ? { label: "Manual", value: cp.manual_check.status } : null,
    cp.screenshot ? { label: "Screenshot", value: cp.screenshot.status } : null,
  ].filter(Boolean) as Array<{ label: string; value: string }>;

  if (breakdown.length === 0) {
    return {
      label: "No explicit trust signal",
      className: "border-border bg-muted text-muted-foreground",
      breakdown: [],
    };
  }

  const values = breakdown.map((item) => item.value.toLowerCase());
  const hasFail = values.some((value) => value.includes("fail") || value.includes("missing"));
  const allPositive = values.every(
    (value) =>
      value.includes("pass") || value.includes("present") || value.includes("captured")
  );

  if (hasFail) {
    return {
      label: "Warning / mixed signal",
      className: "border-warning/20 bg-warning/15 text-warning",
      breakdown,
    };
  }

  if (allPositive) {
    return {
      label: "Verified pass signal",
      className: "border-success/20 bg-success/15 text-success",
      breakdown,
    };
  }

  return {
    label: "Partial signal",
      className: "border-primary/20 bg-primary/15 text-primary",
    breakdown,
  };
}

function sortNewest(runs: DashboardRun[]): DashboardRun[] {
  return [...runs].sort(
    (a, b) => new Date(b.started_at).getTime() - new Date(a.started_at).getTime()
  );
}

function SectionBlock({
  kicker,
  title,
  summary,
  children,
}: {
  kicker?: string;
  title: string;
  summary?: string;
  children: React.ReactNode;
}) {
  return (
    <section className="hud-panel p-5">
      <div className="mb-4">
        {kicker ? (
          <div className="text-[11px] font-medium uppercase tracking-[0.24em] text-muted-foreground">
            {kicker}
          </div>
        ) : null}
        <h2 className="mt-1 text-lg font-semibold tracking-tight text-foreground">
          {title}
        </h2>
        {summary ? (
          <p className="mt-2 text-sm leading-6 text-muted-foreground">{summary}</p>
        ) : null}
      </div>
      {children}
    </section>
  );
}

function RunCard({
  run,
  defaultOpen = false,
}: {
  run: DashboardRun;
  defaultOpen?: boolean;
}) {
  const state = getRunState(run);
  const trust = getTrustSummary(run);
  const outcomeSummary =
    run.stop_reason ??
    run.outcome ??
    (!run.ended_at
      ? "Run is still active."
      : "No final outcome summary was recorded.");

  return (
    <details
      className="group rounded-2xl border border-border bg-card p-4 open:border-border open:bg-card"
      open={defaultOpen}
    >
      <summary className="list-none cursor-pointer">
        <div className="flex flex-col gap-3 md:flex-row md:items-start md:justify-between">
          <div className="min-w-0">
            <div className="flex flex-wrap items-center gap-2">
              <span className="font-mono text-sm text-primary">{run.run_id}</span>
              <span
                className={`inline-flex rounded-full border px-2 py-1 text-[11px] font-medium ${state.className}`}
              >
                {state.label}
              </span>
              <span className="rounded-full border border-border bg-muted px-2 py-1 text-[11px] uppercase tracking-[0.18em] text-muted-foreground">
                {run.module}
              </span>
            </div>

            <div className="mt-2 flex flex-wrap gap-2 text-xs uppercase tracking-[0.18em] text-muted-foreground">
              <span>{run.script_name}</span>
              {run.task_ids?.length ? (
                <span className="font-mono text-muted-foreground">
                  Task: {run.task_ids.join(", ")}
                </span>
              ) : null}
            </div>

            <p className="mt-3 text-sm text-foreground">{outcomeSummary}</p>
          </div>

          <div className="shrink-0 text-left md:text-right">
            <div className="text-xs text-muted-foreground">
              started {formatTimeAgo(run.started_at)}
            </div>
            <div className="mt-1 text-sm font-medium text-foreground">
              duration {formatDuration(run)}
            </div>
          </div>
        </div>

        <div className="mt-4 flex flex-wrap gap-2">
          <span
            className={`inline-flex rounded-full border px-2.5 py-1 text-xs ${trust.className}`}
          >
            {trust.label}
          </span>
          <span className="inline-flex rounded-full border border-border bg-muted px-2.5 py-1 text-xs text-muted-foreground">
            LLM used: {run.llm_used ? "yes" : "no"}
          </span>
          <span className="inline-flex rounded-full border border-border bg-muted px-2.5 py-1 text-xs text-muted-foreground">
            {run.ended_at ? "Ended" : "In progress"}
          </span>
        </div>
      </summary>

      <div className="mt-4 grid gap-4 border-t border-border pt-4 lg:grid-cols-[minmax(0,1.35fr)_minmax(240px,1fr)]">
        <div className="space-y-3">
          <div className="rounded-xl border border-border bg-card p-3">
            <div className="text-[11px] uppercase tracking-[0.22em] text-muted-foreground">
              Execution summary
            </div>
            <p className="mt-2 text-sm text-foreground">{outcomeSummary}</p>
          </div>

          {run.stop_reason ? (
            <div className="rounded-xl border border-warning/20 bg-warning/15 p-3">
              <div className="text-[11px] uppercase tracking-[0.22em] text-warning">
                Failure / escalation signal
              </div>
              <p className="mt-2 text-sm text-foreground">{run.stop_reason}</p>
            </div>
          ) : null}

          {trust.breakdown.length > 0 ? (
            <div className="rounded-xl border border-border bg-card p-3">
              <div className="text-[11px] uppercase tracking-[0.22em] text-muted-foreground">
                Verification signals
              </div>
              <div className="mt-3 space-y-2">
                {trust.breakdown.map((item) => (
                  <div
                    key={`${run.id}-${item.label}`}
                    className="flex items-center justify-between gap-3 text-sm"
                  >
                    <span className="text-muted-foreground">{item.label}</span>
                    <span className="font-medium text-foreground">{item.value}</span>
                  </div>
                ))}
              </div>
            </div>
          ) : (
            <div className="rounded-xl border border-border bg-card p-3 text-sm text-muted-foreground">
              This run does not expose a richer verification breakdown on the current page data.
            </div>
          )}
        </div>

        <div className="space-y-3">
          <div className="rounded-xl border border-border bg-card p-3">
            <div className="text-[11px] uppercase tracking-[0.22em] text-muted-foreground">
              Timeline
            </div>
            <div className="mt-3 space-y-2 text-sm text-foreground">
              <div className="flex items-center justify-between gap-3">
                <span className="text-muted-foreground">Started</span>
                <span>{formatDateTime(run.started_at)}</span>
              </div>
              <div className="flex items-center justify-between gap-3">
                <span className="text-muted-foreground">Ended</span>
                <span>{formatDateTime(run.ended_at)}</span>
              </div>
              <div className="flex items-center justify-between gap-3">
                <span className="text-muted-foreground">Duration</span>
                <span>{formatDuration(run)}</span>
              </div>
            </div>
          </div>

          <div className="rounded-xl border border-border bg-card p-3">
            <div className="text-[11px] uppercase tracking-[0.22em] text-muted-foreground">
              Run metadata
            </div>
            <div className="mt-3 space-y-2 text-sm text-foreground">
              <div className="flex items-center justify-between gap-3">
                <span className="text-muted-foreground">Module</span>
                <span>{run.module}</span>
              </div>
              <div className="flex items-center justify-between gap-3">
                <span className="text-muted-foreground">Task IDs</span>
                <span className="text-right">
                  {run.task_ids?.length ? run.task_ids.join(", ") : "—"}
                </span>
              </div>
              <div className="flex items-center justify-between gap-3">
                <span className="text-muted-foreground">LLM used</span>
                <span>{run.llm_used ? "yes" : "no"}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </details>
  );
}

export default async function RecentRunsPage() {
  const runs = await getRuns(50);
  const sortedRuns = sortNewest(runs);
  const activeRuns = sortedRuns.filter((run) => !run.ended_at);
  const failedRuns = sortedRuns.filter((run) => run.ended_at && isFailure(run));
  const successfulRuns = sortedRuns.filter(
    (run) => run.ended_at && isSuccess(run)
  );
  const uncertainRuns = sortedRuns.filter(
    (run) => run.ended_at && !isFailure(run) && !isSuccess(run)
  );

  const featuredRun =
    activeRuns[0] ?? failedRuns[0] ?? sortedRuns[0] ?? null;
  const recentRuns = sortedRuns
    .filter((run) => featuredRun == null || run.id !== featuredRun.id)
    .slice(0, 8);

  return (
    <div className="space-y-6 pb-6 text-foreground">
      <section className="space-y-4">
        <div>
          <div className="text-[11px] font-medium uppercase tracking-[0.24em] text-muted-foreground">
            Execution Audit Surface
          </div>
          <h1 className="mt-2 text-3xl font-semibold tracking-tight text-foreground">
            Runs
          </h1>
          <p className="mt-2 max-w-3xl text-sm leading-6 text-muted-foreground">
            {runs.length} total run{runs.length === 1 ? "" : "s"} loaded ·{" "}
            {activeRuns.length} active · {failedRuns.length} failed ·{" "}
            {successfulRuns.length} recent success
            {successfulRuns.length === 1 ? "" : "es"}
            {sortedRuns[0]
              ? ` · latest started ${formatTimeAgo(sortedRuns[0].started_at)}`
              : ""}
          </p>
        </div>

        <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
          <HudMetricCard label="Active Runs" value={activeRuns.length} />
          <HudMetricCard
            label="Recent Success"
            value={successfulRuns.length}
            variant="healthy"
          />
          <HudMetricCard
            label="Recent Failures"
            value={failedRuns.length}
            variant={failedRuns.length > 0 ? "warning" : "default"}
          />
          <HudMetricCard
            label="Warning / Uncertain"
            value={uncertainRuns.length}
            variant={uncertainRuns.length > 0 ? "warning" : "default"}
          />
        </div>
      </section>

      {runs.length === 0 ? (
        <div className="rounded-2xl border border-border bg-card p-5 text-sm text-muted-foreground">
          No runs data.
        </div>
      ) : (
        <div className="grid gap-6 xl:grid-cols-[minmax(0,1.7fr)_minmax(320px,1fr)]">
          <div className="space-y-6">
            <SectionBlock
              kicker="Live Queue"
              title="Active / Recent Runs"
              summary="Runs are grouped by live activity first, then recent completions. Expand any card for a lightweight execution preview and verification signals when they exist."
            >
              <div className="space-y-4">
                {activeRuns.length > 0 ? (
                  <div className="space-y-3">
                    <div className="text-[11px] font-medium uppercase tracking-[0.22em] text-muted-foreground">
                      Active
                    </div>
                    {activeRuns.map((run, index) => (
                      <RunCard
                        key={run.id}
                        run={run}
                        defaultOpen={index === 0 && featuredRun?.id === run.id}
                      />
                    ))}
                  </div>
                ) : null}

                {recentRuns.length > 0 ? (
                  <div className="space-y-3">
                    <div className="text-[11px] font-medium uppercase tracking-[0.22em] text-muted-foreground">
                      Recent
                    </div>
                    {recentRuns.map((run) => (
                      <RunCard key={run.id} run={run} />
                    ))}
                  </div>
                ) : null}
              </div>
            </SectionBlock>
          </div>

          <div className="space-y-6">
            <SectionBlock
              kicker="Preview"
              title="Run Detail Preview"
              summary="A lightweight side preview of the highest-priority visible run. This uses only the same run fields already available to the page."
            >
              {featuredRun ? (
                <RunCard run={featuredRun} defaultOpen />
              ) : (
                <div className="rounded-2xl border border-border bg-card p-4 text-sm text-muted-foreground">
                  No featured run is available.
                </div>
              )}
            </SectionBlock>

            <SectionBlock
              kicker="Failure View"
              title="Failures / Escalation Visibility"
              summary="Failed or warning-like runs are surfaced here with module, timing, and real stop reason context."
            >
              {failedRuns.length === 0 ? (
                <div className="rounded-2xl border border-success/20 bg-success/15 p-4 text-sm text-success">
                  No failed runs are visible in the current result set.
                </div>
              ) : (
                <div className="space-y-3">
                  {failedRuns.slice(0, 4).map((run) => (
                    <div
                      key={`failure-${run.id}`}
                      className="rounded-2xl border border-warning/20 bg-warning/15 p-4"
                    >
                      <div className="flex flex-wrap items-center gap-2">
                        <span className="font-mono text-sm text-warning">
                          {run.run_id}
                        </span>
                        <span className="rounded-full border border-warning/20 px-2 py-1 text-[11px] uppercase tracking-[0.18em] text-warning">
                          {run.module}
                        </span>
                      </div>
                      <p className="mt-2 text-sm font-medium text-foreground">
                        {run.stop_reason ?? run.outcome ?? "Failure-like signal detected"}
                      </p>
                      <p className="mt-2 text-xs text-muted-foreground">
                        started {formatTimeAgo(run.started_at)} · duration {formatDuration(run)}
                      </p>
                    </div>
                  ))}
                </div>
              )}
            </SectionBlock>
          </div>
        </div>
      )}
    </div>
  );
}
