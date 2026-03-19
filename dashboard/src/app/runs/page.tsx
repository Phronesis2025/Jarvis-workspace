import { getRuns } from "@/lib/data";
import type { DashboardRun, OperatorCheckpoints } from "@/lib/types";

function RunTrustCell({ run }: { run: DashboardRun }) {
  if (run.module !== "wcs") return <td className="px-4 py-3 text-sm text-slate-400">—</td>;
  const cp = (run.operator_checkpoints ?? {}) as OperatorCheckpoints;
  const b = cp.build?.status ?? "?";
  const s = cp.smoke?.status ?? "?";
  const p = cp.page_smoke?.status ?? "?";
  const route = cp.page_smoke?.route;
  const color = (v: string) =>
    v === "pass" ? "text-emerald-600" : v === "fail" ? "text-amber-600" : "text-slate-500";
  return (
    <td className="px-4 py-3 text-sm">
      <span className="font-mono">
        <span className={color(b)}>B:{b}</span>{" "}
        <span className={color(s)}>S:{s}</span>{" "}
        <span className={color(p)}>P:{p}</span>
        {route && <span className="ml-1 text-slate-500">({route})</span>}
      </span>
    </td>
  );
}

export default async function RecentRunsPage() {
  const runs = await getRuns(50);

  return (
    <div className="space-y-6">
      <h2 className="text-xl font-semibold text-slate-800">Recent Runs</h2>

      {runs.length === 0 ? (
        <p className="text-slate-500">No runs data.</p>
      ) : (
        <div className="overflow-x-auto rounded-lg border border-slate-200 bg-white">
          <table className="min-w-full divide-y divide-slate-200">
            <thead>
              <tr>
                <th className="px-4 py-3 text-left text-xs font-medium text-slate-500">
                  run_id
                </th>
                <th className="px-4 py-3 text-left text-xs font-medium text-slate-500">
                  module
                </th>
                <th className="px-4 py-3 text-left text-xs font-medium text-slate-500">
                  script_name
                </th>
                <th className="px-4 py-3 text-left text-xs font-medium text-slate-500">
                  task_ids
                </th>
                <th className="px-4 py-3 text-left text-xs font-medium text-slate-500">
                  started_at
                </th>
                <th className="px-4 py-3 text-left text-xs font-medium text-slate-500">
                  ended_at
                </th>
                <th className="px-4 py-3 text-left text-xs font-medium text-slate-500">
                  outcome
                </th>
                <th className="px-4 py-3 text-left text-xs font-medium text-slate-500">
                  trust
                </th>
                <th className="px-4 py-3 text-left text-xs font-medium text-slate-500">
                  stop_reason
                </th>
                <th className="px-4 py-3 text-left text-xs font-medium text-slate-500">
                  llm_used
                </th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              {runs.map((r) => (
                <tr key={r.id} className="hover:bg-slate-50">
                  <td className="whitespace-nowrap px-4 py-3 text-sm font-mono text-slate-700">
                    {r.run_id}
                  </td>
                  <td className="px-4 py-3 text-sm text-slate-600">
                    {r.module}
                  </td>
                  <td className="px-4 py-3 text-sm text-slate-600">
                    {r.script_name}
                  </td>
                  <td className="px-4 py-3 text-sm text-slate-600">
                    {r.task_ids?.length
                      ? r.task_ids.join(", ")
                      : "—"}
                  </td>
                  <td className="whitespace-nowrap px-4 py-3 text-sm text-slate-500">
                    {new Date(r.started_at).toLocaleString()}
                  </td>
                  <td className="whitespace-nowrap px-4 py-3 text-sm text-slate-500">
                    {r.ended_at
                      ? new Date(r.ended_at).toLocaleString()
                      : "—"}
                  </td>
                  <td className="px-4 py-3 text-sm text-slate-600">
                    {r.outcome ?? "—"}
                  </td>
                  <RunTrustCell run={r} />
                  <td className="max-w-[200px] truncate px-4 py-3 text-sm text-slate-500">
                    {r.stop_reason ?? "—"}
                  </td>
                  <td className="px-4 py-3 text-sm">
                    {r.llm_used ? (
                      <span className="text-amber-600">yes</span>
                    ) : (
                      <span className="text-slate-400">no</span>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
