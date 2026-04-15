import { getPathfinderCases } from "@/lib/data";

export const dynamic = "force-dynamic";

export default async function PathfinderPage() {
  const cases = await getPathfinderCases(50);

  return (
    <div className="space-y-6">
      <h2 className="text-xl font-semibold text-foreground">Pathfinder</h2>

      {cases.length === 0 ? (
        <p className="text-muted-foreground">No Pathfinder cases.</p>
      ) : (
        <div className="overflow-x-auto rounded-lg border border-border bg-card">
          <table className="min-w-full divide-y divide-border">
            <thead>
              <tr>
                <th className="px-4 py-3 text-left text-xs font-medium text-muted-foreground">
                  run_id
                </th>
                <th className="px-4 py-3 text-left text-xs font-medium text-muted-foreground">
                  intake_summary
                </th>
                <th className="px-4 py-3 text-left text-xs font-medium text-muted-foreground">
                  route
                </th>
                <th className="px-4 py-3 text-left text-xs font-medium text-muted-foreground">
                  synthesis_source
                </th>
                <th className="px-4 py-3 text-left text-xs font-medium text-muted-foreground">
                  confidence
                </th>
                <th className="px-4 py-3 text-left text-xs font-medium text-muted-foreground">
                  likely_next_action
                </th>
                <th className="px-4 py-3 text-left text-xs font-medium text-muted-foreground">
                  backlog_candidate_title
                </th>
                <th className="px-4 py-3 text-left text-xs font-medium text-muted-foreground">
                  omitted_reason
                </th>
                <th className="px-4 py-3 text-left text-xs font-medium text-muted-foreground">
                  created_at
                </th>
              </tr>
            </thead>
            <tbody className="divide-y divide-border">
              {cases.map((c) => (
                <tr key={c.id} className="hover:bg-muted/50">
                  <td className="whitespace-nowrap px-4 py-3 text-sm font-mono text-foreground">
                    {c.run_id}
                  </td>
                  <td className="max-w-[240px] truncate px-4 py-3 text-sm text-muted-foreground">
                    {c.intake_summary ?? "—"}
                  </td>
                  <td className="px-4 py-3 text-sm text-muted-foreground">
                    {c.route ?? "—"}
                  </td>
                  <td className="px-4 py-3 text-sm">
                    {c.synthesis_source === "llm" ? (
                      <span className="text-success">llm</span>
                    ) : c.synthesis_source === "rule_based" ? (
                      <span className="text-muted-foreground">rule_based</span>
                    ) : (
                      "—"
                    )}
                  </td>
                  <td className="px-4 py-3 text-sm text-muted-foreground">
                    {c.confidence ?? "—"}
                  </td>
                  <td className="max-w-[200px] truncate px-4 py-3 text-sm text-muted-foreground">
                    {c.likely_next_action ?? "—"}
                  </td>
                  <td className="max-w-[200px] truncate px-4 py-3 text-sm text-muted-foreground">
                    {c.backlog_candidate_title ?? "—"}
                  </td>
                  <td className="max-w-[200px] truncate px-4 py-3 text-sm text-warning">
                    {c.omitted_reason ?? "—"}
                  </td>
                  <td className="whitespace-nowrap px-4 py-3 text-sm text-muted-foreground">
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
