import { getTasks, getRuns, getModuleStatus } from "@/lib/data";

export default async function OverviewPage() {
  const [tasks, runs, modules] = await Promise.all([
    getTasks(),
    getRuns(10),
    getModuleStatus(),
  ]);

  const ready = tasks.filter((t) => t.status === "ready").length;
  const blocked = tasks.filter((t) => t.status === "blocked").length;
  const done = tasks.filter((t) => t.status === "done").length;
  const running = tasks.filter((t) => t.status === "running").length;
  const escalated = tasks.filter((t) => t.status === "escalated").length;

  const currentPhase =
    modules.find((m) => m.module_id === "wcs")?.phase ?? "—";
  const milestoneSummary =
    modules.find((m) => m.module_id === "wcs")?.milestone_summary ?? "—";

  return (
    <div className="space-y-6">
      <h2 className="text-xl font-semibold text-slate-800">Overview</h2>

      <section className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        <div className="rounded-lg border border-slate-200 bg-white p-4 shadow-sm">
          <div className="text-sm text-slate-500">Ready</div>
          <div className="text-2xl font-semibold text-emerald-600">{ready}</div>
        </div>
        <div className="rounded-lg border border-slate-200 bg-white p-4 shadow-sm">
          <div className="text-sm text-slate-500">Running</div>
          <div className="text-2xl font-semibold text-amber-600">{running}</div>
        </div>
        <div className="rounded-lg border border-slate-200 bg-white p-4 shadow-sm">
          <div className="text-sm text-slate-500">Blocked / Escalated</div>
          <div className="text-2xl font-semibold text-red-600">
            {blocked + escalated}
          </div>
        </div>
        <div className="rounded-lg border border-slate-200 bg-white p-4 shadow-sm">
          <div className="text-sm text-slate-500">Done</div>
          <div className="text-2xl font-semibold text-slate-700">{done}</div>
        </div>
      </section>

      <section>
        <h3 className="mb-2 text-sm font-medium text-slate-600">
          Current phase / milestone
        </h3>
        <div className="rounded-lg border border-slate-200 bg-white p-4">
          <p className="text-slate-800">
            <span className="font-medium">Phase:</span> {currentPhase}
          </p>
          <p className="mt-1 text-slate-600">{milestoneSummary}</p>
        </div>
      </section>

      <section>
        <h3 className="mb-2 text-sm font-medium text-slate-600">
          Module status
        </h3>
        <div className="grid gap-3 sm:grid-cols-2">
          {modules.length === 0 ? (
            <p className="text-slate-500">No module status data.</p>
          ) : (
            modules.map((m) => (
              <div
                key={m.id}
                className="rounded-lg border border-slate-200 bg-white p-4"
              >
                <div className="flex items-center justify-between">
                  <span className="font-medium text-slate-800">{m.name}</span>
                  <span
                    className={`rounded px-2 py-0.5 text-xs ${
                      m.status === "active"
                        ? "bg-emerald-100 text-emerald-800"
                        : "bg-slate-100 text-slate-600"
                    }`}
                  >
                    {m.status}
                  </span>
                </div>
                <p className="mt-1 text-sm text-slate-600">{m.milestone_summary}</p>
              </div>
            ))
          )}
        </div>
      </section>

      <section>
        <h3 className="mb-2 text-sm font-medium text-slate-600">
          Recent runs summary
        </h3>
        {runs.length === 0 ? (
          <p className="text-slate-500">No runs data.</p>
        ) : (
          <div className="overflow-hidden rounded-lg border border-slate-200 bg-white">
            <table className="min-w-full divide-y divide-slate-200">
              <thead>
                <tr>
                  <th className="px-4 py-2 text-left text-xs font-medium text-slate-500">
                    run_id
                  </th>
                  <th className="px-4 py-2 text-left text-xs font-medium text-slate-500">
                    module
                  </th>
                  <th className="px-4 py-2 text-left text-xs font-medium text-slate-500">
                    outcome
                  </th>
                  <th className="px-4 py-2 text-left text-xs font-medium text-slate-500">
                    started
                  </th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-100">
                {runs.slice(0, 5).map((r) => (
                  <tr key={r.id}>
                    <td className="px-4 py-2 text-sm font-mono text-slate-700">
                      {r.run_id}
                    </td>
                    <td className="px-4 py-2 text-sm text-slate-600">
                      {r.module}
                    </td>
                    <td className="px-4 py-2 text-sm text-slate-600">
                      {r.outcome ?? "—"}
                    </td>
                    <td className="px-4 py-2 text-sm text-slate-500">
                      {new Date(r.started_at).toLocaleString()}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </section>
    </div>
  );
}
