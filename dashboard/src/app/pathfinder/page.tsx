import { getPathfinderCases } from "@/lib/data";

export default async function PathfinderPage() {
  const cases = await getPathfinderCases(50);

  return (
    <div className="space-y-6">
      <h2 className="text-xl font-semibold text-slate-800">Pathfinder</h2>

      {cases.length === 0 ? (
        <p className="text-slate-500">No Pathfinder cases.</p>
      ) : (
        <div className="overflow-x-auto rounded-lg border border-slate-200 bg-white">
          <table className="min-w-full divide-y divide-slate-200">
            <thead>
              <tr>
                <th className="px-4 py-3 text-left text-xs font-medium text-slate-500">
                  run_id
                </th>
                <th className="px-4 py-3 text-left text-xs font-medium text-slate-500">
                  intake_summary
                </th>
                <th className="px-4 py-3 text-left text-xs font-medium text-slate-500">
                  route
                </th>
                <th className="px-4 py-3 text-left text-xs font-medium text-slate-500">
                  synthesis_source
                </th>
                <th className="px-4 py-3 text-left text-xs font-medium text-slate-500">
                  confidence
                </th>
                <th className="px-4 py-3 text-left text-xs font-medium text-slate-500">
                  likely_next_action
                </th>
                <th className="px-4 py-3 text-left text-xs font-medium text-slate-500">
                  backlog_candidate_title
                </th>
                <th className="px-4 py-3 text-left text-xs font-medium text-slate-500">
                  omitted_reason
                </th>
                <th className="px-4 py-3 text-left text-xs font-medium text-slate-500">
                  created_at
                </th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              {cases.map((c) => (
                <tr key={c.id} className="hover:bg-slate-50">
                  <td className="whitespace-nowrap px-4 py-3 text-sm font-mono text-slate-700">
                    {c.run_id}
                  </td>
                  <td className="max-w-[240px] truncate px-4 py-3 text-sm text-slate-600">
                    {c.intake_summary ?? "—"}
                  </td>
                  <td className="px-4 py-3 text-sm text-slate-600">
                    {c.route ?? "—"}
                  </td>
                  <td className="px-4 py-3 text-sm">
                    {c.synthesis_source === "llm" ? (
                      <span className="text-emerald-600">llm</span>
                    ) : c.synthesis_source === "rule_based" ? (
                      <span className="text-slate-600">rule_based</span>
                    ) : (
                      "—"
                    )}
                  </td>
                  <td className="px-4 py-3 text-sm text-slate-600">
                    {c.confidence ?? "—"}
                  </td>
                  <td className="max-w-[200px] truncate px-4 py-3 text-sm text-slate-600">
                    {c.likely_next_action ?? "—"}
                  </td>
                  <td className="max-w-[200px] truncate px-4 py-3 text-sm text-slate-600">
                    {c.backlog_candidate_title ?? "—"}
                  </td>
                  <td className="max-w-[200px] truncate px-4 py-3 text-sm text-amber-600">
                    {c.omitted_reason ?? "—"}
                  </td>
                  <td className="whitespace-nowrap px-4 py-3 text-sm text-slate-500">
                    {new Date(c.created_at).toLocaleString()}
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
