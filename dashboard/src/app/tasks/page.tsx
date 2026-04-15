import { getTasks } from "@/lib/data";

export const dynamic = "force-dynamic";

import type { DashboardTaskState, TaskStatus } from "@/lib/types";
import { HudMetricCard } from "@/components/HudMetricCard";

function formatStatusLabel(status: string): string {
  return status.replace(/_/g, " ");
}

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

function sortNewest(tasks: DashboardTaskState[]): DashboardTaskState[] {
  return [...tasks].sort(
    (a, b) => new Date(b.updated_at).getTime() - new Date(a.updated_at).getTime()
  );
}

function statusBadgeClass(status: TaskStatus): string {
  switch (status) {
    case "ready":
      return "border-success/20 bg-success/15 text-success";
    case "running":
      return "border-primary/20 bg-primary/15 text-primary";
    case "awaiting_operator":
      return "border-violet-500/40 bg-violet-500/10 text-violet-300";
    case "blocked":
      return "border-warning/20 bg-warning/15 text-warning";
    case "escalated":
      return "border-rose-500/40 bg-rose-500/10 text-rose-300";
    case "done":
      return "border-border bg-muted text-muted-foreground";
    default:
      return "border-border bg-muted text-muted-foreground";
  }
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

function TaskWorkCard({
  task,
  emphasis = "default",
}: {
  task: DashboardTaskState;
  emphasis?: "default" | "attention" | "warning";
}) {
  const emphasisClass =
    emphasis === "attention"
      ? "border-violet-500/20 bg-violet-500/5"
      : emphasis === "warning"
        ? "border-amber-500/20 bg-amber-500/5"
        : "border-border bg-card";

  return (
    <div className={`rounded-2xl border p-4 ${emphasisClass}`}>
      <div className="flex flex-col gap-3 md:flex-row md:items-start md:justify-between">
        <div className="min-w-0">
          <div className="flex flex-wrap items-center gap-2">
            <span className="text-sm font-semibold text-foreground">
              {task.title}
            </span>
            <span
              className={`inline-flex rounded-full border px-2 py-1 text-[11px] font-medium ${statusBadgeClass(
                task.status
              )}`}
            >
              {formatStatusLabel(task.status)}
            </span>
          </div>

          <div className="mt-2 flex flex-wrap gap-2 text-xs uppercase tracking-[0.18em] text-muted-foreground">
            <span className="font-mono text-primary">{task.task_id}</span>
            <span>{task.module ?? "no module"}</span>
            <span>{task.project}</span>
          </div>

          <p className="mt-3 text-sm text-foreground">
            {task.last_result ??
              task.scope_hint ??
              task.risk ??
              "No additional task detail is currently available."}
          </p>

          {(task.risk || task.scope_hint) && (
            <div className="mt-3 flex flex-wrap gap-2">
              {task.risk ? (
                <span className="rounded-full border border-warning/20 bg-warning/15 px-2.5 py-1 text-xs text-warning">
                  Risk: {task.risk}
                </span>
              ) : null}
              {task.scope_hint ? (
                <span className="rounded-full border border-border bg-muted px-2.5 py-1 text-xs text-muted-foreground">
                  {task.scope_hint}
                </span>
              ) : null}
            </div>
          )}
        </div>

        <div className="shrink-0 text-xs text-muted-foreground">
          updated {formatTimeAgo(task.updated_at)}
        </div>
      </div>
    </div>
  );
}

function TaskList({
  tasks,
  empty,
  emphasis = "default",
}: {
  tasks: DashboardTaskState[];
  empty: string;
  emphasis?: "default" | "attention" | "warning";
}) {
  if (tasks.length === 0) {
    return (
      <div className="rounded-2xl border border-border bg-card p-4 text-sm text-muted-foreground">
        {empty}
      </div>
    );
  }

  return (
    <div className="space-y-3">
      {tasks.map((task) => (
        <TaskWorkCard key={task.id} task={task} emphasis={emphasis} />
      ))}
    </div>
  );
}

function QueueColumn({
  title,
  caption,
  tasks,
}: {
  title: string;
  caption: string;
  tasks: DashboardTaskState[];
}) {
  return (
    <div className="rounded-2xl border border-border bg-card p-4">
      <div className="mb-3 flex items-center justify-between gap-3">
        <div>
          <h3 className="text-sm font-semibold text-foreground">{title}</h3>
          <p className="mt-1 text-xs text-muted-foreground">{caption}</p>
        </div>
        <span className="rounded-full border border-border bg-muted px-2.5 py-1 text-xs text-muted-foreground">
          {tasks.length}
        </span>
      </div>
      <TaskList tasks={tasks} empty={`No tasks in ${title.toLowerCase()}.`} />
    </div>
  );
}

export default async function TaskBoardPage() {
  const tasks = await getTasks();

  const readyTasks = sortNewest(tasks.filter((t) => t.status === "ready"));
  const runningTasks = sortNewest(tasks.filter((t) => t.status === "running"));
  const awaitingOperatorTasks = sortNewest(
    tasks.filter((t) => t.status === "awaiting_operator")
  );
  const blockedTasks = sortNewest(tasks.filter((t) => t.status === "blocked"));
  const escalatedTasks = sortNewest(tasks.filter((t) => t.status === "escalated"));
  const doneTasks = sortNewest(tasks.filter((t) => t.status === "done"));

  const actionQueue = [...readyTasks, ...runningTasks];
  const operatorAttention = [...awaitingOperatorTasks, ...escalatedTasks].slice(
    0,
    6
  );
  const handoffEquivalents = [
    ...awaitingOperatorTasks,
    ...doneTasks.filter((task) => Boolean(task.last_result)),
  ].slice(0, 6);
  const blockerQueue = [...escalatedTasks, ...blockedTasks].slice(0, 6);

  const nextMoves = [
    awaitingOperatorTasks.length > 0
      ? {
          title: "Review operator queue first",
          detail: `${awaitingOperatorTasks.length} task${
            awaitingOperatorTasks.length === 1 ? "" : "s"
          } are explicitly waiting for operator attention.`,
        }
      : null,
    escalatedTasks.length > 0 || blockedTasks.length > 0
      ? {
          title: "Resolve blockers and escalations",
          detail: `${escalatedTasks.length} escalated and ${blockedTasks.length} blocked item${
            escalatedTasks.length + blockedTasks.length === 1 ? "" : "s"
          } are currently slowing work.`,
        }
      : null,
    readyTasks.length > 0
      ? {
          title: "Pull the next ready task",
          detail: `${readyTasks.length} ready task${
            readyTasks.length === 1 ? "" : "s"
          } can move immediately into active work.`,
        }
      : null,
  ].filter(Boolean) as { title: string; detail: string }[];

  return (
    <div className="space-y-6 pb-6 text-foreground">
      <section className="space-y-4">
        <div>
          <div className="text-[11px] font-medium uppercase tracking-[0.24em] text-muted-foreground">
            Operator Execution Surface
          </div>
          <h1 className="mt-2 text-3xl font-semibold tracking-tight text-foreground">
            Work
          </h1>
          <p className="mt-2 max-w-3xl text-sm leading-6 text-muted-foreground">
            {tasks.length} total task{tasks.length === 1 ? "" : "s"} tracked ·{" "}
            {actionQueue.length} active or ready · {awaitingOperatorTasks.length}{" "}
            waiting for operator attention · {blockedTasks.length + escalatedTasks.length}{" "}
            blocked or escalated
          </p>
        </div>

        <div className="grid grid-cols-2 gap-3 sm:grid-cols-3 xl:grid-cols-6">
          <HudMetricCard label="Ready" value={readyTasks.length} />
          <HudMetricCard label="Running" value={runningTasks.length} />
          <HudMetricCard
            label="Awaiting operator"
            value={awaitingOperatorTasks.length}
            variant={awaitingOperatorTasks.length > 0 ? "warning" : "default"}
          />
          <HudMetricCard
            label="Blocked"
            value={blockedTasks.length}
            variant={blockedTasks.length > 0 ? "warning" : "default"}
          />
          <HudMetricCard
            label="Escalated"
            value={escalatedTasks.length}
            variant={escalatedTasks.length > 0 ? "warning" : "default"}
          />
          <HudMetricCard label="Done" value={doneTasks.length} variant="healthy" />
        </div>
      </section>

      <div className="grid gap-6 xl:grid-cols-[minmax(0,1.7fr)_minmax(320px,1fr)]">
        <div className="space-y-6">
          <SectionBlock
            kicker="Queue"
            title="Action Queue"
            summary="This is the primary work surface for tasks that can move now. Ready and running work are grouped separately for faster scanability."
          >
            <div className="grid gap-4 xl:grid-cols-2">
              <QueueColumn
                title="Ready to Start"
                caption="Tasks already in a startable state."
                tasks={readyTasks}
              />
              <QueueColumn
                title="In Progress"
                caption="Tasks currently moving through execution."
                tasks={runningTasks}
              />
            </div>
          </SectionBlock>

          <SectionBlock
            kicker="Attention"
            title="Pending Approvals / Operator Attention"
            summary="The current task model does not expose formal approval objects, so this section truthfully uses the nearest equivalents: tasks explicitly marked `awaiting_operator`, followed by escalated work."
          >
            <TaskList
              tasks={operatorAttention}
              empty="No tasks are currently waiting for operator review."
              emphasis="attention"
            />
          </SectionBlock>

          <SectionBlock
            kicker="Review"
            title="Handoff Packets / Ready-for-Review Work"
            summary="There is no packet model on this page, so this section shows the nearest truthful equivalents: operator-review tasks and recently completed work that already has a result summary."
          >
            <TaskList
              tasks={handoffEquivalents}
              empty="No clear handoff-ready equivalents are visible in the current task data."
            />
          </SectionBlock>

          <SectionBlock
            kicker="Risk"
            title="Escalation / Blockers"
            summary="Escalated and blocked tasks are separated into a high-visibility queue so bottlenecks are easier to triage."
          >
            <TaskList
              tasks={blockerQueue}
              empty="No blocked or escalated work is visible right now."
              emphasis="warning"
            />
          </SectionBlock>
        </div>

        <div className="space-y-6">
          <SectionBlock
            kicker="Moves"
            title="Quick Actions / Next Work Moves"
            summary="These are directional summaries only, based on the same visible task counts and statuses already on the page."
          >
            {nextMoves.length === 0 ? (
              <div className="rounded-2xl border border-border bg-card p-4 text-sm text-muted-foreground">
                No immediate next move stands out from the current task state.
              </div>
            ) : (
              <div className="space-y-3">
                {nextMoves.map((move) => (
                  <div
                    key={move.title}
                    className="rounded-2xl border border-border bg-card p-4"
                  >
                    <div className="text-sm font-semibold text-foreground">
                      {move.title}
                    </div>
                    <p className="mt-2 text-sm leading-6 text-muted-foreground">
                      {move.detail}
                    </p>
                  </div>
                ))}
              </div>
            )}
          </SectionBlock>

          <SectionBlock
            kicker="Status Map"
            title="Current Buckets"
            summary="All existing task status buckets are preserved; this panel keeps their counts visible without changing the underlying definitions."
          >
            <div className="space-y-3">
              {[
                { status: "ready" as TaskStatus, count: readyTasks.length },
                { status: "running" as TaskStatus, count: runningTasks.length },
                {
                  status: "awaiting_operator" as TaskStatus,
                  count: awaitingOperatorTasks.length,
                },
                { status: "blocked" as TaskStatus, count: blockedTasks.length },
                { status: "escalated" as TaskStatus, count: escalatedTasks.length },
                { status: "done" as TaskStatus, count: doneTasks.length },
              ].map(({ status, count }) => (
                <div
                  key={status}
                  className="flex items-center justify-between rounded-2xl border border-border bg-card px-4 py-3"
                >
                  <span
                    className={`inline-flex rounded-full border px-2 py-1 text-[11px] font-medium ${statusBadgeClass(
                      status
                    )}`}
                  >
                    {formatStatusLabel(status)}
                  </span>
                  <span className="text-sm font-semibold text-foreground">
                    {count}
                  </span>
                </div>
              ))}
            </div>
          </SectionBlock>
        </div>
      </div>
    </div>
  );
}
