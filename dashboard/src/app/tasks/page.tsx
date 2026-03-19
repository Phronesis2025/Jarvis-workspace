import { getTasks } from "@/lib/data";

export const dynamic = "force-dynamic";
import type { TaskStatus } from "@/lib/types";

const COLUMNS: { status: TaskStatus; label: string }[] = [
  { status: "ready", label: "Ready" },
  { status: "running", label: "Running" },
  { status: "awaiting_operator", label: "Awaiting operator" },
  { status: "blocked", label: "Blocked" },
  { status: "escalated", label: "Escalated" },
  { status: "done", label: "Done" },
];

function TaskCard({
  task_id,
  title,
  project,
  risk,
  scope_hint,
  updated_at,
  last_result,
}: {
  task_id: string;
  title: string;
  project: string;
  risk: string | null;
  scope_hint: string | null;
  updated_at: string;
  last_result: string | null;
}) {
  return (
    <div className="rounded border border-slate-200 bg-white p-3 shadow-sm">
      <div className="font-mono text-xs text-slate-500">{task_id}</div>
      <div className="mt-1 font-medium text-slate-800">{title}</div>
      <div className="mt-1 flex flex-wrap gap-2 text-xs text-slate-600">
        <span>{project}</span>
        {risk && <span>• risk: {risk}</span>}
        {scope_hint && <span>• {scope_hint}</span>}
      </div>
      <div className="mt-2 text-xs text-slate-400">
        updated: {new Date(updated_at).toLocaleString()}
      </div>
      {last_result && (
        <div className="mt-1 text-xs text-slate-500">
          last: {last_result}
        </div>
      )}
    </div>
  );
}

export default async function TaskBoardPage() {
  const tasks = await getTasks();

  return (
    <div className="space-y-6">
      <h2 className="text-xl font-semibold text-slate-800">Task Board</h2>

      <div className="grid gap-4 lg:grid-cols-2 xl:grid-cols-3">
        {COLUMNS.map(({ status, label }) => {
          const columnTasks = tasks.filter((t) => t.status === status);
          return (
            <div
              key={status}
              className="rounded-lg border border-slate-200 bg-slate-50/50 p-4"
            >
              <h3 className="mb-3 flex items-center justify-between text-sm font-medium text-slate-700">
                {label}
                <span className="rounded bg-slate-200 px-2 py-0.5 text-xs text-slate-600">
                  {columnTasks.length}
                </span>
              </h3>
              <div className="space-y-2">
                {columnTasks.length === 0 ? (
                  <p className="text-sm text-slate-400">No tasks</p>
                ) : (
                  columnTasks.map((t) => (
                    <TaskCard
                      key={t.id}
                      task_id={t.task_id}
                      title={t.title}
                      project={t.project}
                      risk={t.risk}
                      scope_hint={t.scope_hint}
                      updated_at={t.updated_at}
                      last_result={t.last_result}
                    />
                  ))
                )}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
