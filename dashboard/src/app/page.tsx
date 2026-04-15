import Link from "next/link";
import {
  getTasks,
  getRuns,
  getModuleStatus,
  getPathfinderCases,
  getLastExportTime,
} from "@/lib/data";

export const dynamic = "force-dynamic";
export const fetchCache = "force-no-store";

import type {
  DashboardModuleStatus,
  DashboardPathfinderCase,
  DashboardRun,
  DashboardTaskState,
  OperatorCheckpoints,
} from "@/lib/types";
import { SystemPulse } from "@/components/SystemPulse";
import { HudMetricCard } from "@/components/HudMetricCard";

function TrustPill({ status }: { status: string }) {
  const s = (status || "unknown").toLowerCase();
  const color =
    s === "pass"
      ? "text-success"
      : s === "fail"
        ? "text-warning"
        : s === "skipped"
          ? "text-muted-foreground"
          : "text-muted-foreground";

  return <span className={color}>{s}</span>;
}

function SectionBlock({
  kicker,
  title,
  action,
  children,
}: {
  kicker?: string;
  title: string;
  action?: React.ReactNode;
  children: React.ReactNode;
}) {
  return (
    <section className="hud-panel p-5">
      <div className="mb-4 flex items-start justify-between gap-4">
        <div>
          {kicker ? (
            <div className="text-[11px] font-medium uppercase tracking-[0.24em] text-muted-foreground">
              {kicker}
            </div>
          ) : null}
          <h2 className="mt-1 text-lg font-semibold tracking-tight text-foreground">
            {title}
          </h2>
        </div>
        {action}
      </div>
      {children}
    </section>
  );
}

function AttentionBadge({ status }: { status: string }) {
  const normalized = status.toLowerCase();
  const className =
    normalized === "awaiting_operator"
      ? "border-primary/20 bg-primary/15 text-primary"
      : normalized === "blocked" || normalized === "escalated"
        ? "border-warning/20 bg-warning/15 text-warning"
        : "border-border bg-muted text-muted-foreground";

  return (
    <span className={`inline-flex rounded-full border px-2 py-1 text-[11px] font-medium ${className}`}>
      {formatStatusLabel(status)}
    </span>
  );
}

function ModuleStatusPill({ status }: { status: string }) {
  const normalized = status.toLowerCase();
  const isActive = normalized.includes("active");

  return (
    <span
      className={`inline-flex rounded-full border px-2.5 py-1 text-[11px] font-medium ${
        isActive
          ? "border-success/20 bg-success/15 text-success"
          : "border-border bg-card text-foreground"
      }`}
    >
      {status}
    </span>
  );
}

function WcsTrustSummary({ run }: { run: DashboardRun }) {
  const cp = (run.operator_checkpoints ?? {}) as OperatorCheckpoints;

  return (
    <div className="rounded-2xl border border-border bg-card p-4">
      <div className="mb-2 flex items-center justify-between gap-3">
        <div className="text-sm font-medium text-foreground">
          Latest WCS trust checkpoint
        </div>
        <span className="text-xs text-muted-foreground">{run.run_id}</span>
      </div>
      <div className="flex flex-wrap gap-x-4 gap-y-2 text-sm text-foreground">
        <span>
          Build: <TrustPill status={cp.build?.status ?? "unknown"} />
        </span>
        <span>
          Smoke: <TrustPill status={cp.smoke?.status ?? "unknown"} />
        </span>
        <span>
          Page-smoke: <TrustPill status={cp.page_smoke?.status ?? "unknown"} />
          {cp.page_smoke?.route ? (
            <span className="ml-1 font-mono text-primary">
              ({cp.page_smoke.route})
            </span>
          ) : null}
        </span>
      </div>
      {run.stop_reason ? (
        <p className="mt-3 text-sm text-warning">Stop: {run.stop_reason}</p>
      ) : null}
    </div>
  );
}

function isToday(iso: string): boolean {
  const d = new Date(iso);
  const now = new Date();

  return (
    d.getDate() === now.getDate() &&
    d.getMonth() === now.getMonth() &&
    d.getFullYear() === now.getFullYear()
  );
}

function formatTimeAgo(iso: string): string {
  const d = new Date(iso);
  const now = new Date();
  const mins = Math.floor((now.getTime() - d.getTime()) / 60000);

  if (mins < 1) return "Just now";
  if (mins < 60) return `${mins}m ago`;

  const hrs = Math.floor(mins / 60);
  if (hrs < 24) return `${hrs}h ago`;

  const days = Math.floor(hrs / 24);
  return `${days}d ago`;
}

function formatStatusLabel(status: string): string {
  return status.replace(/_/g, " ");
}

function formatExportFreshness(
  exportedAt: string | null
): { text: string; stale?: boolean } {
  if (!exportedAt) return { text: "Unavailable" };

  const d = new Date(exportedAt);
  const now = new Date();
  const hrs = (now.getTime() - d.getTime()) / 3600000;
  const text = formatTimeAgo(exportedAt);

  return { text, stale: hrs > 24 };
}

function sortNewest<T>(items: T[], getDate: (item: T) => string): T[] {
  return [...items].sort(
    (a, b) => new Date(getDate(b)).getTime() - new Date(getDate(a)).getTime()
  );
}

function buildCurrentPriority(args: {
  awaitingOperatorTasks: DashboardTaskState[];
  escalatedTasks: DashboardTaskState[];
  blockedTasks: DashboardTaskState[];
  activeRuns: DashboardRun[];
  readyCases: DashboardPathfinderCase[];
  exportFreshness: { text: string; stale?: boolean };
}) {
  const {
    awaitingOperatorTasks,
    escalatedTasks,
    blockedTasks,
    activeRuns,
    readyCases,
    exportFreshness,
  } = args;

  if (awaitingOperatorTasks[0]) {
    const task = awaitingOperatorTasks[0];
    return {
      eyebrow: "Current Priority",
      title: task.title,
      summary:
        task.last_result ??
        task.scope_hint ??
        "This task is waiting for operator review before the next step can proceed.",
      meta: `${task.task_id} · ${task.module ?? task.project} · waiting for review`,
      href: "/tasks",
      cta: "Open Task Board",
    };
  }

  if (escalatedTasks[0]) {
    const task = escalatedTasks[0];
    return {
      eyebrow: "Current Priority",
      title: task.title,
      summary:
        task.last_result ??
        task.risk ??
        "An escalated item is waiting for operator attention.",
      meta: `${task.task_id} · ${task.module ?? task.project} · escalated`,
      href: "/tasks",
      cta: "Review Escalations",
    };
  }

  if (blockedTasks[0]) {
    const task = blockedTasks[0];
    return {
      eyebrow: "Current Priority",
      title: task.title,
      summary:
        task.last_result ??
        task.risk ??
        "A blocked task is the clearest current bottleneck on the board.",
      meta: `${task.task_id} · ${task.module ?? task.project} · blocked`,
      href: "/tasks",
      cta: "Review Blockers",
    };
  }

  if (activeRuns[0]) {
    const run = activeRuns[0];
    return {
      eyebrow: "Current Priority",
      title: `Monitor ${run.module} run ${run.run_id}`,
      summary:
        run.stop_reason ??
        run.outcome ??
        `${run.script_name} is the most current active run in the system.`,
      meta: `${run.module} · started ${formatTimeAgo(run.started_at)}`,
      href: "/runs",
      cta: "Open Runs",
    };
  }

  if (readyCases[0]) {
    const item = readyCases[0];
    return {
      eyebrow: "Current Priority",
      title: item.backlog_candidate_title ?? "Review Pathfinder recommendation",
      summary:
        item.likely_next_action ??
        item.intake_summary ??
        "Pathfinder surfaced a case that looks ready for the next decision.",
      meta: `${item.run_id} · ${item.confidence ?? "pathfinder signal"}`,
      href: "/pathfinder",
      cta: "Open Pathfinder",
    };
  }

  return {
    eyebrow: "Current Priority",
    title: "System is clear right now",
    summary: exportFreshness.stale
      ? "No urgent operator item is visible, but the dashboard sync looks stale and should be checked."
      : "No urgent operator item is visible from the current dashboard signals.",
    meta: exportFreshness.stale ? "Last sync looks stale" : "No active blockers surfaced",
    href: exportFreshness.stale ? "/tasks" : undefined,
    cta: exportFreshness.stale ? "Check Task Board" : undefined,
  };
}

export default async function OverviewPage() {
  const [tasks, runs, modules, pathfinderCases, lastExport] = await Promise.all([
    getTasks(),
    getRuns(100),
    getModuleStatus(),
    getPathfinderCases(100),
    getLastExportTime(),
  ]);

  const now = new Date();
  const todayLabel = now.toLocaleDateString(undefined, {
    weekday: "long",
    month: "long",
    day: "numeric",
    year: "numeric",
  });

  const runsToday = runs.filter((r) => isToday(r.started_at));
  const tasksDoneToday = tasks.filter(
    (t) => t.status === "done" && isToday(t.updated_at)
  );
  const pathfinderCasesToday = pathfinderCases.filter((c) =>
    isToday(c.created_at)
  );

  const workSessionsToday = runsToday.length;
  const tasksCompletedToday = tasksDoneToday.length;
  const researchHandledToday = pathfinderCasesToday.length;

  const awaitingOperatorTasks = sortNewest(
    tasks.filter((t) => t.status === "awaiting_operator"),
    (t) => t.updated_at
  );
  const blockedTasks = sortNewest(
    tasks.filter((t) => t.status === "blocked"),
    (t) => t.updated_at
  );
  const escalatedTasks = sortNewest(
    tasks.filter((t) => t.status === "escalated"),
    (t) => t.updated_at
  );
  const tasksNeedingAttention = [
    ...awaitingOperatorTasks,
    ...escalatedTasks,
    ...blockedTasks,
  ].slice(0, 4);

  const awaitingReview = awaitingOperatorTasks.length;
  const blocked = blockedTasks.length;
  const escalated = escalatedTasks.length;
  const totalNeedingAttention = awaitingReview + blocked + escalated;

  const activeRuns = sortNewest(
    runs.filter((r) => !r.ended_at),
    (r) => r.started_at
  ).slice(0, 4);
  const displayedRuns = activeRuns.length > 0 ? activeRuns : runs.slice(0, 4);

  const latestWcsRun = runs.find((r) => r.module === "wcs") ?? null;
  const tasksCompletedTotal = tasks.filter((t) => t.status === "done").length;

  const aiAssistedReviews = pathfinderCases.filter(
    (c) => c.synthesis_source === "llm"
  ).length;
  const readyForWork = sortNewest(
    pathfinderCases.filter((c) => c.confidence === "ready_for_implementation"),
    (c) => c.created_at
  );
  const needsMoreInfo = pathfinderCases.filter(
    (c) => c.confidence === "needs_more_context"
  ).length;
  const draftBacklogItems = pathfinderCases.filter(
    (c) => c.backlog_candidate_title != null
  ).length;

  const recentInsights = sortNewest(
    pathfinderCases.filter(
      (c) => c.backlog_candidate_title || c.likely_next_action || c.intake_summary
    ),
    (c) => c.created_at
  ).slice(0, 3);

  const alertRuns = sortNewest(
    runs.filter((r) => {
      const outcome = (r.outcome ?? "").toLowerCase();
      return outcome.includes("fail") || Boolean(r.stop_reason);
    }),
    (r) => r.started_at
  ).slice(0, 2);

  const alertItems = [
    ...escalatedTasks.slice(0, 2).map((task) => ({
      id: `task-${task.id}`,
      label: "Task escalation",
      title: task.title,
      detail:
        task.last_result ??
        task.risk ??
        `${task.task_id} is escalated and needs operator attention.`,
      href: "/tasks",
    })),
    ...blockedTasks.slice(0, 2).map((task) => ({
      id: `blocked-${task.id}`,
      label: "Blocked work",
      title: task.title,
      detail:
        task.last_result ??
        task.risk ??
        `${task.task_id} is blocked on the current board.`,
      href: "/tasks",
    })),
    ...alertRuns.map((run) => ({
      id: `run-${run.id}`,
      label: "Run issue",
      title: `${run.module} · ${run.run_id}`,
      detail:
        run.stop_reason ??
        run.outcome ??
        "This run has a warning-like signal in the current dashboard data.",
      href: "/runs",
    })),
  ].slice(0, 4);

  const recentActivity = sortNewest(
    [
      ...(lastExport?.exported_at
        ? [
            {
              id: "dashboard-export",
              timestamp: lastExport.exported_at,
              label: "Dashboard sync",
              title: "Dashboard export refreshed",
              detail: `Last sync ${formatTimeAgo(lastExport.exported_at)}.`,
            },
          ]
        : []),
      ...runs.slice(0, 4).map((run) => ({
        id: `run-${run.id}`,
        timestamp: run.started_at,
        label: "Run activity",
        title: `${run.module} · ${run.run_id}`,
        detail:
          run.outcome ??
          run.stop_reason ??
          `${run.script_name} started ${formatTimeAgo(run.started_at)}.`,
      })),
      ...tasks.slice(0, 3).map((task) => ({
        id: `task-${task.id}`,
        timestamp: task.updated_at,
        label: "Task update",
        title: task.title,
        detail: `${task.task_id} moved to ${formatStatusLabel(task.status)}.`,
      })),
      ...pathfinderCases.slice(0, 2).map((item) => ({
        id: `pathfinder-${item.id}`,
        timestamp: item.created_at,
        label: "Pathfinder signal",
        title: item.backlog_candidate_title ?? item.run_id,
        detail:
          item.likely_next_action ??
          item.intake_summary ??
          "Pathfinder added a new research case.",
      })),
    ],
    (item) => item.timestamp
  ).slice(0, 7);

  const exportFreshness = formatExportFreshness(lastExport?.exported_at ?? null);
  const overallStatus =
    totalNeedingAttention > 0 ? "Attention required" : "Operational";

  const currentPriority = buildCurrentPriority({
    awaitingOperatorTasks,
    escalatedTasks,
    blockedTasks,
    activeRuns,
    readyCases: readyForWork,
    exportFreshness,
  });

  const nextBestAction = totalNeedingAttention > 0
    ? {
        title: `${totalNeedingAttention} item${totalNeedingAttention === 1 ? "" : "s"} need operator attention`,
        detail:
          awaitingReview > 0
            ? `${awaitingReview} item${awaitingReview === 1 ? "" : "s"} are waiting for operator review on the Task Board.`
            : escalated > 0
              ? `${escalated} escalated item${escalated === 1 ? "" : "s"} should be reviewed first.`
              : `${blocked} blocked item${blocked === 1 ? "" : "s"} are the clearest current bottleneck.`,
        href: "/tasks",
        cta: "Open Task Board",
      }
    : activeRuns.length > 0
      ? {
          title: "Monitor the currently active run set",
          detail: `${activeRuns.length} active run${activeRuns.length === 1 ? "" : "s"} are still in progress.`,
          href: "/runs",
          cta: "Open Runs",
        }
      : readyForWork.length > 0
        ? {
            title: "Review Pathfinder output ready for implementation",
            detail: `${readyForWork.length} research item${readyForWork.length === 1 ? "" : "s"} are marked ready for implementation.`,
            href: "/pathfinder",
            cta: "Open Pathfinder",
          }
        : {
            title: "Maintain dashboard freshness and watch the queue",
            detail: exportFreshness.stale
              ? "No urgent operator item is visible, but the dashboard sync looks stale."
              : "No urgent blocker is visible. The best next step is to monitor the board and recent runs.",
            href: "/runs",
            cta: "Review Recent Runs",
          };

  return (
    <div className="space-y-6 pb-6 text-foreground">
      <section className="grid gap-6 xl:grid-cols-[minmax(0,1.8fr)_minmax(320px,1fr)]">
        <div className="space-y-4">
          <div>
            <div className="text-[11px] font-medium uppercase tracking-[0.24em] text-muted-foreground">
              Operator View
            </div>
            <h1 className="mt-2 text-3xl font-semibold tracking-tight text-foreground">
              Now
            </h1>
            <p className="mt-2 max-w-3xl text-sm leading-6 text-muted-foreground">
              {todayLabel} · {workSessionsToday} work session
              {workSessionsToday === 1 ? "" : "s"} today · last sync{" "}
              <span
                className={
                  exportFreshness.text === "Unavailable"
                    ? "text-muted-foreground"
                    : exportFreshness.stale
                      ? "text-warning"
                      : "text-primary"
                }
              >
                {exportFreshness.text}
              </span>
            </p>
          </div>

          <div className="hud-panel overflow-hidden border border-border p-6">
            <div className="flex flex-col gap-4 lg:flex-row lg:items-start lg:justify-between">
              <div className="max-w-3xl">
                <div className="text-[11px] font-medium uppercase tracking-[0.24em] text-muted-foreground">
                  {currentPriority.eyebrow}
                </div>
                <h2 className="mt-2 text-2xl font-semibold tracking-tight text-foreground">
                  {currentPriority.title}
                </h2>
                <p className="mt-3 text-sm leading-6 text-foreground">
                  {currentPriority.summary}
                </p>
                <div className="mt-4 text-xs uppercase tracking-[0.22em] text-muted-foreground">
                  {currentPriority.meta}
                </div>
              </div>

              <div className="flex shrink-0 flex-col gap-3">
                <div className="rounded-2xl border border-border bg-card px-4 py-3">
                  <div className="text-[11px] uppercase tracking-[0.22em] text-muted-foreground">
                    Attention count
                  </div>
                  <div className="mt-1 text-2xl font-semibold text-foreground">
                    {totalNeedingAttention}
                  </div>
                </div>
                {currentPriority.href && currentPriority.cta ? (
                  <Link
                    href={currentPriority.href}
                    className="inline-flex items-center justify-center rounded-xl border border-primary/20 bg-primary/15 px-4 py-2.5 text-sm font-semibold text-primary transition-colors hover:bg-primary/20"
                  >
                    {currentPriority.cta}
                  </Link>
                ) : null}
              </div>
            </div>
          </div>
        </div>

        <SystemPulse
          overallStatus={overallStatus}
          tasksCompletedToday={tasksCompletedToday}
          workSessionsToday={workSessionsToday}
          lastUpdateText={exportFreshness.text}
          lastUpdateStale={exportFreshness.stale}
          lastUpdateUnavailable={exportFreshness.text === "Unavailable"}
        />
      </section>

      <section>
        <div className="grid grid-cols-2 gap-3 sm:grid-cols-3 xl:grid-cols-6">
          <HudMetricCard label="Work sessions" value={workSessionsToday} />
          <HudMetricCard label="Tasks completed" value={tasksCompletedToday} />
          <HudMetricCard
            label="Needs attention"
            value={totalNeedingAttention}
            variant={totalNeedingAttention > 0 ? "warning" : "healthy"}
          />
          <HudMetricCard label="Research reviewed" value={researchHandledToday} />
          <HudMetricCard label="AI-assisted reviews" value={aiAssistedReviews} />
          <HudMetricCard
            label="Draft backlog items"
            value={draftBacklogItems}
          />
        </div>
      </section>

      <div className="grid gap-6 xl:grid-cols-[minmax(0,1.7fr)_minmax(320px,1fr)]">
        <div className="space-y-6">
          <SectionBlock
            kicker="Execution"
            title="Active Runs"
            action={
              <Link
                href="/runs"
                className="text-sm font-medium text-cyan-300 transition-colors hover:text-cyan-200"
              >
                View all runs
              </Link>
            }
          >
            {displayedRuns.length === 0 ? (
              <p className="text-sm text-slate-500">No recent runs available.</p>
            ) : (
              <div className="space-y-3">
                {activeRuns.length === 0 ? (
                  <p className="text-sm text-slate-500">
                    No runs are currently active. Showing the latest recent runs instead.
                  </p>
                ) : null}
                {displayedRuns.map((run) => {
                  const outcome = (run.outcome ?? "").toLowerCase();
                  const healthy =
                    !run.ended_at ||
                    outcome.includes("complete") ||
                    outcome.includes("worker_complete");

                  return (
                    <div
                      key={run.id}
                      className="rounded-2xl border border-slate-800 bg-slate-950/60 p-4"
                    >
                      <div className="flex flex-col gap-3 md:flex-row md:items-start md:justify-between">
                        <div className="min-w-0">
                          <div className="flex flex-wrap items-center gap-2">
                            <span className="text-sm font-semibold text-slate-100">
                              {run.module}
                            </span>
                            <span className="rounded-full border border-slate-700 px-2 py-1 text-[11px] uppercase tracking-[0.2em] text-slate-400">
                              {run.run_id}
                            </span>
                          </div>
                          <p className="mt-2 text-sm text-slate-400">
                            {run.script_name}
                          </p>
                          <p className="mt-2 text-sm text-slate-300">
                            {run.stop_reason ??
                              run.outcome ??
                              (run.ended_at
                                ? "Completed without a recorded outcome summary."
                                : "Run is still active.")}
                          </p>
                        </div>
                        <div className="shrink-0 text-left md:text-right">
                          <div
                            className={`text-sm font-medium ${
                              healthy ? "text-teal-300" : "text-amber-300"
                            }`}
                          >
                            {run.ended_at ? "Recent run" : "Active now"}
                          </div>
                          <div className="mt-1 text-xs text-slate-500">
                            started {formatTimeAgo(run.started_at)}
                          </div>
                        </div>
                      </div>
                      <div className="mt-4 flex flex-wrap gap-2 text-xs text-slate-500">
                        <span className="rounded-full border border-slate-800 px-2 py-1">
                          Tasks: {run.task_ids?.length ? run.task_ids.join(", ") : "none linked"}
                        </span>
                        <span className="rounded-full border border-slate-800 px-2 py-1">
                          LLM used: {run.llm_used ? "yes" : "no"}
                        </span>
                      </div>
                    </div>
                  );
                })}
              </div>
            )}
          </SectionBlock>

          <SectionBlock
            kicker="Operator"
            title="Operator Checkpoints"
            action={
              <Link
                href="/tasks"
                className="text-sm font-medium text-cyan-300 transition-colors hover:text-cyan-200"
              >
                Open Task Board
              </Link>
            }
          >
            <div className="space-y-3">
              {tasksNeedingAttention.length === 0 ? (
                <div className="rounded-2xl border border-slate-800 bg-slate-950/60 p-4 text-sm text-slate-500">
                  No explicit operator-review items are visible right now.
                </div>
              ) : (
                tasksNeedingAttention.map((task) => (
                  <div
                    key={task.id}
                    className="rounded-2xl border border-slate-800 bg-slate-950/60 p-4"
                  >
                    <div className="flex flex-col gap-3 md:flex-row md:items-start md:justify-between">
                      <div className="min-w-0">
                        <div className="flex flex-wrap items-center gap-2">
                          <span className="text-sm font-semibold text-slate-100">
                            {task.title}
                          </span>
                          <AttentionBadge status={task.status} />
                        </div>
                        <div className="mt-2 flex flex-wrap gap-2 text-xs uppercase tracking-[0.18em] text-slate-500">
                          <span>{task.task_id}</span>
                          <span>{task.module ?? task.project}</span>
                        </div>
                        <p className="mt-2 text-sm text-slate-400">
                          {task.last_result ??
                            task.risk ??
                            task.scope_hint ??
                            "This item is the closest current operator checkpoint on the board."}
                        </p>
                      </div>
                      <div className="shrink-0 text-xs text-slate-500">
                        updated {formatTimeAgo(task.updated_at)}
                      </div>
                    </div>
                  </div>
                ))
              )}

              {latestWcsRun ? <WcsTrustSummary run={latestWcsRun} /> : null}
            </div>
          </SectionBlock>

          <SectionBlock kicker="Activity" title="Since Last Visit">
            {recentActivity.length === 0 ? (
              <p className="text-sm text-slate-500">No recent activity captured.</p>
            ) : (
              <div className="relative pl-4">
                <div className="pointer-events-none absolute bottom-0 left-1.5 top-0 w-px bg-slate-800" />
                <div className="space-y-4">
                  {recentActivity.map((item) => (
                    <div key={item.id} className="relative flex gap-3">
                      <span className="mt-1.5 h-2 w-2 shrink-0 rounded-full bg-cyan-400 shadow-[0_0_8px_rgba(34,211,238,0.45)]" />
                      <div className="min-w-0">
                        <div className="flex flex-wrap items-baseline gap-2">
                          <span className="text-xs uppercase tracking-[0.2em] text-slate-500">
                            {item.label}
                          </span>
                          <span className="text-xs text-slate-600">
                            {formatTimeAgo(item.timestamp)}
                          </span>
                        </div>
                        <div className="mt-1 text-sm font-medium text-slate-100">
                          {item.title}
                        </div>
                        <p className="mt-1 text-sm text-slate-400">{item.detail}</p>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </SectionBlock>
        </div>

        <div className="space-y-6">
          <SectionBlock kicker="Health" title="Module Health">
            <div className="space-y-3">
              {modules.map((module: DashboardModuleStatus) => (
                <div
                  key={module.id}
                  className="rounded-2xl border border-slate-800 bg-slate-950/60 p-4"
                >
                  <div className="flex items-start justify-between gap-3">
                    <div className="min-w-0">
                      <div className="text-sm font-semibold text-slate-100">
                        {module.name}
                      </div>
                      <p className="mt-1 text-sm text-slate-400">
                        {module.milestone_summary ?? "No milestone summary available."}
                      </p>
                    </div>
                    <ModuleStatusPill status={module.status} />
                  </div>
                </div>
              ))}
            </div>
          </SectionBlock>

          <SectionBlock kicker="Risk" title="Alerts / Blockers">
            {alertItems.length === 0 ? (
              <div className="rounded-2xl border border-teal-500/20 bg-teal-500/5 p-4 text-sm text-teal-300">
                No blocked, escalated, or warning-like signals are visible from the current page data.
              </div>
            ) : (
              <div className="space-y-3">
                {alertItems.map((item) => (
                  <div
                    key={item.id}
                    className="rounded-2xl border border-amber-500/20 bg-amber-500/5 p-4"
                  >
                    <div className="text-[11px] font-medium uppercase tracking-[0.22em] text-amber-400/80">
                      {item.label}
                    </div>
                    <div className="mt-2 text-sm font-semibold text-slate-100">
                      {item.title}
                    </div>
                    <p className="mt-2 text-sm text-slate-300">{item.detail}</p>
                    <Link
                      href={item.href}
                      className="mt-3 inline-flex text-sm font-medium text-amber-300 transition-colors hover:text-amber-200"
                    >
                      Open related surface
                    </Link>
                  </div>
                ))}
              </div>
            )}
          </SectionBlock>

          <SectionBlock kicker="Action" title="Next Best Action">
            <div className="rounded-2xl border border-cyan-500/20 bg-cyan-500/5 p-4">
              <div className="text-sm font-semibold text-cyan-100">
                {nextBestAction.title}
              </div>
              <p className="mt-2 text-sm leading-6 text-slate-300">
                {nextBestAction.detail}
              </p>
              <Link
                href={nextBestAction.href}
                className="mt-4 inline-flex items-center justify-center rounded-xl bg-cyan-600 px-4 py-2.5 text-sm font-semibold text-white transition-colors hover:bg-cyan-500"
              >
                {nextBestAction.cta}
              </Link>
            </div>
          </SectionBlock>

          <SectionBlock kicker="Signals" title="Recent Insights">
            {recentInsights.length === 0 ? (
              <div className="rounded-2xl border border-slate-800 bg-slate-950/60 p-4 text-sm text-slate-500">
                Pathfinder has not surfaced a richer recent insight block from the current page data, so this section stays minimal.
              </div>
            ) : (
              <div className="space-y-3">
                {recentInsights.map((item) => (
                  <div
                    key={item.id}
                    className="rounded-2xl border border-slate-800 bg-slate-950/60 p-4"
                  >
                    <div className="flex flex-wrap items-center gap-2">
                      <span className="rounded-full border border-slate-700 px-2 py-1 text-[11px] uppercase tracking-[0.2em] text-slate-500">
                        Pathfinder
                      </span>
                      <span className="text-xs text-slate-500">
                        {item.confidence ?? "signal"}
                      </span>
                    </div>
                    <div className="mt-2 text-sm font-semibold text-slate-100">
                      {item.backlog_candidate_title ?? item.run_id}
                    </div>
                    <p className="mt-2 text-sm text-slate-400">
                      {item.likely_next_action ??
                        item.intake_summary ??
                        item.omitted_reason ??
                        "Recent Pathfinder activity is available, but detailed insight text is limited."}
                    </p>
                    {item.route ? (
                      <div className="mt-2 text-xs text-slate-500">
                        Route: <span className="font-mono text-slate-400">{item.route}</span>
                      </div>
                    ) : null}
                  </div>
                ))}
                <div className="grid grid-cols-2 gap-3">
                  <HudMetricCard
                    label="Ready for implementation"
                    value={readyForWork.length}
                  />
                  <HudMetricCard
                    label="Need more context"
                    value={needsMoreInfo}
                    variant={needsMoreInfo > 0 ? "warning" : "default"}
                  />
                </div>
              </div>
            )}
          </SectionBlock>

          <SectionBlock kicker="Summary" title="Module Snapshot">
            <div className="grid grid-cols-1 gap-3 sm:grid-cols-2">
              <HudMetricCard
                label="Tasks completed total"
                value={tasksCompletedTotal}
              />
              <HudMetricCard label="Recent research items" value={researchHandledToday} />
            </div>
          </SectionBlock>
        </div>
      </div>
    </div>
  );
}
