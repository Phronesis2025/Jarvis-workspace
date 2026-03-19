import { getTasks, getRuns, getModuleStatus, getPathfinderCases, getLastExportTime } from "@/lib/data";

export const dynamic = "force-dynamic";
import type { DashboardRun, OperatorCheckpoints } from "@/lib/types";
import { MermaidDiagram } from "@/components/MermaidDiagram";
import { SystemPulse } from "@/components/SystemPulse";
import { HudMetricCard } from "@/components/HudMetricCard";

function TrustPill({ status }: { status: string }) {
  const s = (status || "unknown").toLowerCase();
  const color =
    s === "pass"
      ? "text-teal-400"
      : s === "fail"
        ? "text-amber-400"
        : s === "skipped"
          ? "text-slate-500"
          : "text-slate-400";
  return <span className={color}>{s}</span>;
}

function WcsTrustSection({ run }: { run: DashboardRun }) {
  const cp = (run.operator_checkpoints ?? {}) as OperatorCheckpoints;
  return (
    <div className="mt-4 rounded border border-cyan-500/20 bg-cyan-500/5 p-3">
      <div className="mb-2 text-xs font-medium uppercase tracking-wider text-cyan-400/80">
        Latest WCS run trust
      </div>
      <div className="flex flex-wrap items-center gap-x-4 gap-y-1 text-sm">
        <span>
          Build: <TrustPill status={cp.build?.status ?? "unknown"} />
        </span>
        <span>
          Smoke: <TrustPill status={cp.smoke?.status ?? "unknown"} />
        </span>
        <span>
          Page-smoke: <TrustPill status={cp.page_smoke?.status ?? "unknown"} />
          {cp.page_smoke?.route && (
            <span className="ml-1 font-mono text-cyan-300">
              ({cp.page_smoke.route})
            </span>
          )}
        </span>
        {run.stop_reason && (
          <span className="w-full truncate text-amber-400/90">
            Stop: {run.stop_reason}
          </span>
        )}
      </div>
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

export default async function OverviewPage() {
  const [tasks, runs, modules, pathfinderCases, lastExport] =
    await Promise.all([
      getTasks(),
      getRuns(100),
      getModuleStatus(),
      getPathfinderCases(100),
      getLastExportTime(),
    ]);

  const today = new Date().toDateString();

  const runsToday = runs.filter((r) => isToday(r.started_at));
  const wcsRunsToday = runsToday.filter((r) => r.module === "wcs");
  const pathfinderRunsToday = runsToday.filter(
    (r) => r.module === "pathfinder"
  );
  const tasksDoneToday = tasks.filter(
    (t) => t.status === "done" && isToday(t.updated_at)
  );
  const tasksBlockedToday = tasks.filter(
    (t) =>
      (t.status === "blocked" || t.status === "escalated") &&
      isToday(t.updated_at)
  );
  const pathfinderCasesToday = pathfinderCases.filter((c) =>
    isToday(c.created_at)
  );

  const workSessionsToday = runsToday.length;
  const tasksCompletedToday = tasksDoneToday.length;
  const researchHandledToday = pathfinderCasesToday.length;
  const awaitingReview = tasks.filter(
    (t) => t.status === "awaiting_operator"
  ).length;
  const blocked = tasks.filter((t) => t.status === "blocked").length;
  const escalated = tasks.filter((t) => t.status === "escalated").length;
  const totalNeedingAttention = awaitingReview + blocked + escalated;

  const wcsSuccessful = runs.filter(
    (r) =>
      r.module === "wcs" &&
      ((r.outcome ?? "").toLowerCase().includes("complete") ||
        (r.outcome ?? "").toLowerCase().includes("worker_complete"))
  );
  const lastSuccessfulWcs = wcsSuccessful[0];
  const latestWcsRun = runs.find((r) => r.module === "wcs") ?? null;
  const tasksCompletedTotal = tasks.filter((t) => t.status === "done").length;

  const aiAssistedReviews = pathfinderCases.filter(
    (c) => c.synthesis_source === "llm"
  ).length;
  const readyForWork = pathfinderCases.filter(
    (c) => c.confidence === "ready_for_implementation"
  ).length;
  const needsMoreInfo = pathfinderCases.filter(
    (c) => c.confidence === "needs_more_context"
  ).length;
  const draftBacklogItems = pathfinderCases.filter(
    (c) => c.backlog_candidate_title != null
  ).length;

  const jarvisCore =
    modules.find((m) => m.module_id === "jarvis_core") ?? {
      name: "Jarvis Core",
      status: "active",
      milestone_summary: "Foreman loop live.",
    };
  const wcsModule =
    modules.find((m) => m.module_id === "wcs") ?? {
      name: "WCS Code Module",
      status: "active",
      milestone_summary: "Task cycles proven.",
    };
  const pathfinderModule =
    modules.find((m) => m.module_id === "pathfinder") ?? {
      name: "Pathfinder",
      status: "active",
      milestone_summary: "Read-only discovery worker.",
    };

  const activeModules: string[] = [];
  if (wcsRunsToday.length > 0) activeModules.push("Code work");
  if (pathfinderRunsToday.length > 0) activeModules.push("Research");
  const summaryParts: string[] = [];
  if (tasksCompletedToday > 0)
    summaryParts.push(
      `${tasksCompletedToday} task${tasksCompletedToday === 1 ? "" : "s"} completed`
    );
  if (workSessionsToday > 0)
    summaryParts.push(
      `${workSessionsToday} work session${workSessionsToday === 1 ? "" : "s"}`
    );
  if (researchHandledToday > 0)
    summaryParts.push(
      `${researchHandledToday} research item${researchHandledToday === 1 ? "" : "s"} reviewed`
    );
  if (tasksBlockedToday.length > 0)
    summaryParts.push(
      `${tasksBlockedToday.length} item${tasksBlockedToday.length === 1 ? "" : "s"} blocked or escalated`
    );
  const whatHappened =
    summaryParts.length > 0
      ? summaryParts.join("; ") + "."
      : activeModules.length > 0
        ? `${activeModules.join(" and ")} ran today, but no tasks were completed yet.`
        : "No activity recorded today.";

  const recentEvents = runs.slice(0, 8).map((r) => {
    const mod =
      r.module === "wcs"
        ? "Code work"
        : r.module === "pathfinder"
          ? "Research"
          : r.module;
    const outcome = (r.outcome ?? "").toLowerCase();
    const ok =
      outcome.includes("complete") || outcome.includes("worker_complete");
    return {
      run: r,
      label: mod,
      ok,
      time: formatTimeAgo(r.started_at),
    };
  });

  const exportFreshness = formatExportFreshness(
    lastExport?.exported_at ?? null
  );

  const overallStatus =
    totalNeedingAttention > 0 ? "Attention required" : "Operational";

  const milestones = [
    "Single-task loop proven",
    "Sequential runner proven",
    "Pathfinder research proven",
    "Dashboard live",
  ];

  function moduleStatusPill(status: string) {
    const isActive = status.toLowerCase().includes("active");
    return (
      <span
        className={`inline-flex items-center rounded-full border px-2.5 py-1 text-xs font-medium ${
          isActive
            ? "border-teal-500/50 bg-teal-500/10 text-teal-300"
            : "border-cyan-500/30 bg-cyan-500/5 text-slate-400"
        }`}
      >
        {status}
      </span>
    );
  }

  return (
    <div className="-mx-4 min-h-screen bg-[#0a0e17] px-4 text-slate-200 sm:-mx-6 sm:px-6">
      {/* Header */}
      <div className="mb-6 flex items-end justify-between gap-4 border-b border-cyan-500/20 pb-4">
        <h2 className="text-xl font-semibold tracking-tight text-cyan-100">
          Overview
        </h2>
        <div className="text-right text-xs uppercase tracking-wider text-slate-500">
          {today}
        </div>
      </div>

      {/* Hero: System Pulse */}
      <section className="mb-6">
        <SystemPulse
          overallStatus={overallStatus}
          tasksCompletedToday={tasksCompletedToday}
          workSessionsToday={workSessionsToday}
          lastUpdateText={exportFreshness.text}
          lastUpdateStale={exportFreshness.stale}
          lastUpdateUnavailable={exportFreshness.text === "Unavailable"}
        />
      </section>

      {/* Instrument row */}
      <section className="mb-6">
        <div className="mb-3 text-xs font-medium uppercase tracking-widest text-cyan-400/80">
          Today at a glance
        </div>
        <div className="grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-6">
          <HudMetricCard label="Work sessions" value={workSessionsToday} />
          <HudMetricCard label="Tasks completed" value={tasksCompletedToday} />
          <HudMetricCard
            label="Items needing attention"
            value={totalNeedingAttention}
            variant={totalNeedingAttention > 0 ? "warning" : "healthy"}
          />
          <HudMetricCard
            label="Research reviewed"
            value={researchHandledToday}
          />
          <HudMetricCard
            label="Last dashboard update"
            value={
              exportFreshness.text === "Unavailable" ? (
                <span className="text-slate-500">{exportFreshness.text}</span>
              ) : exportFreshness.stale ? (
                <span className="text-amber-400">{exportFreshness.text}</span>
              ) : (
                <span className="text-teal-400">{exportFreshness.text}</span>
              )
            }
          />
          <HudMetricCard
            label="Overall status"
            value={overallStatus}
            variant={totalNeedingAttention > 0 ? "warning" : "healthy"}
          />
        </div>
      </section>

      {/* Supporting panels: left = summary, right = attention + activity */}
      <div className="mb-8 grid grid-cols-1 gap-6 lg:grid-cols-2">
        {/* Left: What happened + Milestones */}
        <div className="space-y-6">
          <div className="hud-panel p-4">
            <h3 className="mb-2 text-xs font-medium uppercase tracking-widest text-cyan-400/80">
              What happened today
            </h3>
            <p className="text-sm leading-relaxed text-slate-300">
              {whatHappened}
            </p>
          </div>
          <div className="hud-panel p-4">
            <h3 className="mb-3 text-xs font-medium uppercase tracking-widest text-cyan-400/80">
              Milestones reached
            </h3>
            <ul className="flex flex-wrap gap-2">
              {milestones.map((m) => (
                <li
                  key={m}
                  className="rounded border border-teal-500/30 bg-teal-500/5 px-3 py-1.5 text-sm text-teal-300"
                >
                  {m}
                </li>
              ))}
            </ul>
          </div>
        </div>

        {/* Right: Needs attention + Recent activity */}
        <div className="space-y-6">
          <div
            className={`hud-panel p-4 ${
              totalNeedingAttention > 0
                ? "border-amber-500/30 shadow-[0_0_20px_rgba(251,191,36,0.08)]"
                : ""
            }`}
          >
            <div className="mb-3 flex items-center justify-between">
              <h3 className="text-xs font-medium uppercase tracking-widest text-cyan-400/80">
                Needs your attention
              </h3>
              <span
                className={`rounded-full border px-2.5 py-1 text-xs font-medium ${
                  totalNeedingAttention > 0
                    ? "border-amber-500/50 bg-amber-500/10 text-amber-400"
                    : "border-teal-500/30 bg-teal-500/10 text-teal-400"
                }`}
              >
                {totalNeedingAttention}
              </span>
            </div>
            <div className="grid grid-cols-3 gap-2">
              <div className="hud-metric p-2">
                <div className="text-xs text-slate-500">Waiting for review</div>
                <div className="text-lg font-semibold text-cyan-200">
                  {awaitingReview}
                </div>
              </div>
              <div className="hud-metric p-2">
                <div className="text-xs text-slate-500">Blocked</div>
                <div className="text-lg font-semibold text-cyan-200">
                  {blocked}
                </div>
              </div>
              <div className="hud-metric p-2">
                <div className="text-xs text-slate-500">Escalated</div>
                <div className="text-lg font-semibold text-cyan-200">
                  {escalated}
                </div>
              </div>
            </div>
            {totalNeedingAttention === 0 && (
              <p className="mt-3 text-sm text-slate-500">
                Nothing waiting. You’re all clear.
              </p>
            )}
          </div>
          <div className="hud-panel p-4">
            <h3 className="mb-3 text-xs font-medium uppercase tracking-widest text-cyan-400/80">
              Recent activity
            </h3>
            {recentEvents.length === 0 ? (
              <p className="text-sm text-slate-500">No recent activity.</p>
            ) : (
              <div className="relative pl-4">
                <div className="pointer-events-none absolute left-1.5 top-0 bottom-0 w-px bg-cyan-500/20" />
                <ul className="space-y-2">
                  {recentEvents.map((e) => (
                    <li key={e.run.id} className="relative flex gap-3">
                      <span
                        className={`mt-1.5 h-2 w-2 shrink-0 rounded-full ${
                          e.ok ? "bg-teal-400 shadow-[0_0_6px_rgba(45,212,191,0.5)]" : "bg-slate-600"
                        }`}
                      />
                      <div className="min-w-0">
                        <div className="flex items-baseline gap-2">
                          <span className="truncate text-sm font-medium text-slate-200">
                            {e.label}
                          </span>
                          <span className="text-xs text-slate-500">
                            {e.time}
                          </span>
                        </div>
                        <div className="truncate text-xs text-slate-500">
                          {e.run.run_id}
                        </div>
                      </div>
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Module sections */}
      <div className="space-y-6">
        {/* Jarvis Core */}
        <section className="hud-panel p-5">
          <div className="grid grid-cols-1 gap-6 lg:grid-cols-12">
            <div className="lg:col-span-7">
              <div className="mb-3 flex items-center justify-between gap-3">
                <h3 className="text-lg font-semibold text-cyan-100">
                  Jarvis Core
                </h3>
                {moduleStatusPill(jarvisCore.status)}
              </div>
              <p className="mb-4 text-sm leading-relaxed text-slate-400">
                What it did today: {workSessionsToday} work session
                {workSessionsToday === 1 ? "" : "s"}, {tasksCompletedToday}{" "}
                task{tasksCompletedToday === 1 ? "" : "s"} completed.
              </p>
              <div className="mb-4 hud-metric p-3 text-sm text-slate-400">
                <strong className="font-semibold text-cyan-200">
                  What to do next:
                </strong>{" "}
                Run the export when you’ve made local changes. Check the Task
                Board for ready work. Run Pathfinder for new research requests.
              </div>
              <div className="mb-4 rounded border border-cyan-500/20 bg-cyan-500/5 p-3">
                <div className="mb-2 text-xs font-medium uppercase tracking-wider text-cyan-400/80">
                  Exporter health
                </div>
                <div className="grid grid-cols-1 gap-2 text-sm sm:grid-cols-3">
                  <div>
                    <span className="text-slate-500">Dry-run available:</span>{" "}
                    <span className="text-teal-400">yes</span>
                  </div>
                  <div>
                    <span className="text-slate-500">Dry-run proof:</span>{" "}
                    <span className="text-teal-400">payload/env OK</span>
                  </div>
                  <div>
                    <span className="text-slate-500">Live export:</span>{" "}
                    <span className="text-slate-400">
                      separate proof surface
                    </span>
                  </div>
                </div>
              </div>
              <div className="grid grid-cols-1 gap-3 sm:grid-cols-3">
                <HudMetricCard
                  label="Work sessions (today)"
                  value={workSessionsToday}
                />
                <HudMetricCard
                  label="Tasks completed (today)"
                  value={tasksCompletedToday}
                />
                <HudMetricCard
                  label="Items needing attention"
                  value={totalNeedingAttention}
                  variant={totalNeedingAttention > 0 ? "warning" : "healthy"}
                />
              </div>
            </div>
            <div className="lg:col-span-5">
              <div className="hud-process-panel p-4">
                <div className="mb-2 text-xs font-medium uppercase tracking-wider text-cyan-400/70">
                  Process reference
                </div>
                <MermaidDiagram
                  code={`flowchart TB
    A[Backlog/Intake] --> B[Select Task]
    B --> C[Prepare Packet/Branch]
    C --> D[Launch Worker]
    D --> E[QA/Checkpoint]
    E --> F[Finalize/Reconcile]
    F --> G[Export Dashboard]`}
                />
              </div>
            </div>
          </div>
        </section>

        {/* WCS Code Module */}
        <section className="hud-panel p-5">
          <div className="grid grid-cols-1 gap-6 lg:grid-cols-12">
            <div className="lg:col-span-7">
              <div className="mb-3 flex items-center justify-between gap-3">
                <h3 className="text-lg font-semibold text-cyan-100">
                  WCS Code Module
                </h3>
                {moduleStatusPill(wcsModule.status)}
              </div>
              <p className="mb-4 text-sm leading-relaxed text-slate-400">
                What it did today: {wcsRunsToday.length} coding session
                {wcsRunsToday.length === 1 ? "" : "s"}. Total tasks completed so
                far: {tasksCompletedTotal}.
              </p>
              <div className="mb-4 hud-metric p-3 text-sm text-slate-400">
                <strong className="font-semibold text-cyan-200">
                  What to do next:
                </strong>{" "}
                Pick a ready task from the Task Board. Run prep and launch.
                Complete commit, QA, and manual verification. Finalize and
                reconcile.
              </div>
              <div className="grid grid-cols-1 gap-3 sm:grid-cols-3">
                <HudMetricCard
                  label="Sessions today"
                  value={wcsRunsToday.length}
                />
                <HudMetricCard
                  label="Tasks completed so far"
                  value={tasksCompletedTotal}
                />
                <div className="hud-metric p-3">
                  <div className="text-xs uppercase tracking-wider text-slate-500">
                    Last successful run
                  </div>
                  <div className="mt-1 truncate text-sm text-cyan-200">
                    {lastSuccessfulWcs ? lastSuccessfulWcs.run_id : "—"}
                  </div>
                </div>
              </div>
              {latestWcsRun && (
                <WcsTrustSection run={latestWcsRun} />
              )}
            </div>
            <div className="lg:col-span-5">
              <div className="hud-process-panel p-4">
                <div className="mb-2 text-xs font-medium uppercase tracking-wider text-cyan-400/70">
                  Process reference
                </div>
                <MermaidDiagram
                  code={`flowchart TB
    A[Task Selected] --> B[Branch Prep]
    B --> C[Cursor Execution]
    C --> D[Build/Smoke]
    D --> E[Manual Verification]
    E --> F[Finalize]
    F --> G[Reconcile]`}
                />
              </div>
            </div>
          </div>
        </section>

        {/* Pathfinder */}
        <section className="hud-panel p-5">
          <div className="grid grid-cols-1 gap-6 lg:grid-cols-12">
            <div className="lg:col-span-7">
              <div className="mb-3 flex items-center justify-between gap-3">
                <h3 className="text-lg font-semibold text-cyan-100">
                  Pathfinder
                </h3>
                {moduleStatusPill(pathfinderModule.status)}
              </div>
              <p className="mb-4 text-sm leading-relaxed text-slate-400">
                What it did today: {pathfinderCasesToday.length} research item
                {pathfinderCasesToday.length === 1 ? "" : "s"} reviewed.{" "}
                {readyForWork} ready for implementation, {needsMoreInfo} needing
                more context.
              </p>
              <div className="mb-4 hud-metric p-3 text-sm text-slate-400">
                <strong className="font-semibold text-cyan-200">
                  What to do next:
                </strong>{" "}
                Run Pathfinder on new research requests. Review findings and
                draft backlog. Open an implementation task when the scope is
                clear.
              </div>
              <div className="grid grid-cols-1 gap-3 sm:grid-cols-2">
                <HudMetricCard
                  label="Research items reviewed"
                  value={pathfinderCases.length}
                />
                <HudMetricCard
                  label="AI-assisted reviews"
                  value={aiAssistedReviews}
                />
                <HudMetricCard
                  label="Ready for implementation"
                  value={readyForWork}
                />
                <HudMetricCard
                  label="Draft backlog items"
                  value={draftBacklogItems}
                />
              </div>
            </div>
            <div className="lg:col-span-5">
              <div className="hud-process-panel p-4">
                <div className="mb-2 text-xs font-medium uppercase tracking-wider text-cyan-400/70">
                  Process reference
                </div>
                <MermaidDiagram
                  code={`flowchart TB
    A[Intake Packet] --> B[Validate]
    B --> C[Gather Evidence]
    C --> D[Rule Checks]
    D --> E[Optional LLM Synthesis]
    E --> F[Validate Output]
    F --> G[Result / Draft Backlog / Escalation]`}
                />
              </div>
            </div>
          </div>
        </section>

        {/* B1 Local Website Defect Watcher */}
        <section className="hud-panel p-5">
          <div className="grid grid-cols-1 gap-6 lg:grid-cols-12">
            <div className="lg:col-span-7">
              <div className="mb-3 flex items-center justify-between gap-3">
                <h3 className="text-lg font-semibold text-cyan-100">
                  B1 Local Website Defect Watcher
                </h3>
                {moduleStatusPill("active")}
              </div>
              <p className="mb-2 text-sm leading-relaxed text-slate-400">
                Bounded read-only watcher for visible website defects.
                Config-driven, Playwright-based. v1 checks direct route
                reachability only (no nav-link clicking).
              </p>
              <p className="mb-4 text-sm text-cyan-300/90">
                First monitored site:{" "}
                <span className="font-mono">https://www.wcsbasketball.site/</span>
              </p>
              <div className="mb-4 rounded border border-teal-500/20 bg-teal-500/5 p-3">
                <div className="mb-2 text-xs font-medium uppercase tracking-wider text-teal-400/80">
                  Last known proof (after signal hardening)
                </div>
                <div className="grid grid-cols-2 gap-2 text-sm sm:grid-cols-4">
                  <div>
                    <span className="text-slate-500">Findings:</span>{" "}
                    <span className="text-teal-400">0</span>
                  </div>
                  <div>
                    <span className="text-slate-500">Proposed packets:</span>{" "}
                    <span className="text-teal-400">0</span>
                  </div>
                  <div>
                    <span className="text-slate-500">Screenshots:</span>{" "}
                    <span className="text-teal-400">4</span>
                  </div>
                  <div>
                    <span className="text-slate-500">Console errors:</span>{" "}
                    <span className="text-teal-400">0</span>
                  </div>
                </div>
                <div className="mt-2 text-sm">
                  <span className="text-slate-500">Recommended action:</span>{" "}
                  <span className="text-teal-400">dismiss</span>
                </div>
              </div>
              <div className="grid grid-cols-1 gap-3 sm:grid-cols-2 lg:grid-cols-4">
                <HudMetricCard label="Routes checked" value="4" />
                <HudMetricCard label="Findings" value={0} />
                <HudMetricCard label="Proposed packets" value={0} />
                <HudMetricCard label="Recommended action" value="dismiss" variant="healthy" />
              </div>
            </div>
            <div className="lg:col-span-5">
              <div className="hud-process-panel p-4">
                <div className="mb-2 text-xs font-medium uppercase tracking-wider text-cyan-400/70">
                  B1 process reference
                </div>
                <MermaidDiagram
                  code={`flowchart TB
    A[Watcher Config] --> B[Route Checks]
    B --> C[Evidence Capture]
    C --> D[Noise Filter / Dedupe]
    D --> E[Proposed Defect Packets]
    E --> F[Operator Review]`}
                />
              </div>
            </div>
          </div>
        </section>
      </div>
    </div>
  );
}
