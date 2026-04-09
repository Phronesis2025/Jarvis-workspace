"use client";

import { useMemo, useState } from "react";
import type { FoundryRegistryIdea } from "@/lib/types";

interface Props {
  ideas: FoundryRegistryIdea[];
  sourceLanesByIdeaId: Record<string, string[]>;
}

function toSearchable(idea: FoundryRegistryIdea): string {
  return [
    idea.title,
    idea.summary,
    idea.canonical_problem,
    idea.canonical_pattern,
  ]
    .join(" ")
    .toLowerCase();
}

export function FoundryRegistryReviewClient({ ideas, sourceLanesByIdeaId }: Props) {
  const [statusFilter, setStatusFilter] = useState<string>("all");
  const [categoryFilter, setCategoryFilter] = useState<string>("all");
  const [sourceLaneFilter, setSourceLaneFilter] = useState<string>("all");
  const [search, setSearch] = useState<string>("");
  const [selectedIdeaId, setSelectedIdeaId] = useState<string>(ideas[0]?.idea_id ?? "");

  const categories = useMemo(
    () => Array.from(new Set(ideas.map((idea) => idea.category))).sort(),
    [ideas]
  );
  const sourceLanes = useMemo(() => {
    const all = ideas.flatMap((idea) => sourceLanesByIdeaId[idea.idea_id] ?? []);
    return Array.from(new Set(all)).sort();
  }, [ideas, sourceLanesByIdeaId]);

  const filtered = useMemo(() => {
    const query = search.trim().toLowerCase();
    return ideas.filter((idea) => {
      if (statusFilter !== "all" && idea.status !== statusFilter) return false;
      if (categoryFilter !== "all" && idea.category !== categoryFilter) return false;
      if (
        sourceLaneFilter !== "all" &&
        !(sourceLanesByIdeaId[idea.idea_id] ?? []).includes(sourceLaneFilter)
      ) {
        return false;
      }
      if (query && !toSearchable(idea).includes(query)) return false;
      return true;
    });
  }, [ideas, statusFilter, categoryFilter, sourceLaneFilter, search, sourceLanesByIdeaId]);

  const selected =
    filtered.find((idea) => idea.idea_id === selectedIdeaId) ??
    filtered[0] ??
    null;

  return (
    <div className="space-y-6">
      <section className="grid grid-cols-1 gap-3 sm:grid-cols-2 lg:grid-cols-4">
        <div className="hud-metric p-3">
          <div className="text-xs uppercase tracking-wider text-slate-500">Total active ideas</div>
          <div className="mt-1 text-xl font-semibold text-cyan-200">
            {ideas.filter((idea) => idea.status === "active").length}
          </div>
        </div>
        <div className="hud-metric p-3">
          <div className="text-xs uppercase tracking-wider text-slate-500">Total queued ideas</div>
          <div className="mt-1 text-xl font-semibold text-cyan-200">
            {ideas.filter((idea) => idea.status === "queued").length}
          </div>
        </div>
        <div className="hud-metric p-3">
          <div className="text-xs uppercase tracking-wider text-slate-500">Highest weighted score</div>
          <div className="mt-1 text-xl font-semibold text-cyan-200">
            {ideas.length > 0 ? ideas[0].weighted_score.toFixed(2) : "—"}
          </div>
        </div>
        <div className="hud-metric p-3">
          <div className="text-xs uppercase tracking-wider text-slate-500">Needs more research</div>
          <div className="mt-1 text-xl font-semibold text-cyan-200">
            {ideas.filter((idea) => idea.review_state === "needs_more_research").length}
          </div>
        </div>
      </section>

      <section className="hud-panel p-4">
        <div className="grid grid-cols-1 gap-3 md:grid-cols-2 lg:grid-cols-4">
          <label className="space-y-1 text-sm">
            <span className="text-slate-400">Status</span>
            <select
              value={statusFilter}
              onChange={(e) => setStatusFilter(e.target.value)}
              className="w-full rounded border border-cyan-500/20 bg-slate-950 px-2 py-2 text-slate-200"
            >
              <option value="all">all</option>
              {Array.from(new Set(ideas.map((idea) => idea.status))).sort().map((status) => (
                <option key={status} value={status}>
                  {status}
                </option>
              ))}
            </select>
          </label>
          <label className="space-y-1 text-sm">
            <span className="text-slate-400">Category</span>
            <select
              value={categoryFilter}
              onChange={(e) => setCategoryFilter(e.target.value)}
              className="w-full rounded border border-cyan-500/20 bg-slate-950 px-2 py-2 text-slate-200"
            >
              <option value="all">all</option>
              {categories.map((category) => (
                <option key={category} value={category}>
                  {category}
                </option>
              ))}
            </select>
          </label>
          <label className="space-y-1 text-sm">
            <span className="text-slate-400">Source lane</span>
            <select
              value={sourceLaneFilter}
              onChange={(e) => setSourceLaneFilter(e.target.value)}
              className="w-full rounded border border-cyan-500/20 bg-slate-950 px-2 py-2 text-slate-200"
            >
              <option value="all">all</option>
              {sourceLanes.map((lane) => (
                <option key={lane} value={lane}>
                  {lane}
                </option>
              ))}
            </select>
          </label>
          <label className="space-y-1 text-sm">
            <span className="text-slate-400">Search</span>
            <input
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              placeholder="title, summary, problem, pattern"
              className="w-full rounded border border-cyan-500/20 bg-slate-950 px-2 py-2 text-slate-200 placeholder:text-slate-500"
            />
          </label>
        </div>
      </section>

      <section className="grid grid-cols-1 gap-6 lg:grid-cols-2">
        <div className="hud-panel overflow-x-auto p-0">
          <table className="min-w-full divide-y divide-cyan-500/10">
            <thead>
              <tr>
                {[
                  "title",
                  "category",
                  "status",
                  "weighted score",
                  "supporting source count",
                  "confidence",
                  "expected upside",
                  "implementation cost",
                  "risk reduction value",
                  "last updated",
                ].map((header) => (
                  <th key={header} className="px-3 py-2 text-left text-xs font-medium uppercase text-slate-400">
                    {header}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody className="divide-y divide-cyan-500/5">
              {filtered.map((idea) => {
                const selectedRow = selected?.idea_id === idea.idea_id;
                return (
                  <tr
                    key={idea.idea_id}
                    onClick={() => setSelectedIdeaId(idea.idea_id)}
                    className={`cursor-pointer ${selectedRow ? "bg-cyan-500/10" : "hover:bg-slate-900/70"}`}
                  >
                    <td className="px-3 py-2 text-sm text-slate-200">{idea.title}</td>
                    <td className="px-3 py-2 text-sm text-slate-300">{idea.category}</td>
                    <td className="px-3 py-2 text-sm text-slate-300">{idea.status}</td>
                    <td className="px-3 py-2 text-sm text-cyan-200">{idea.weighted_score.toFixed(2)}</td>
                    <td className="px-3 py-2 text-sm text-slate-300">{idea.supporting_source_count}</td>
                    <td className="px-3 py-2 text-sm text-slate-300">{idea.confidence}</td>
                    <td className="px-3 py-2 text-sm text-slate-300">{idea.expected_upside}</td>
                    <td className="px-3 py-2 text-sm text-slate-300">{idea.implementation_cost}</td>
                    <td className="px-3 py-2 text-sm text-slate-300">{idea.risk_reduction_value}</td>
                    <td className="whitespace-nowrap px-3 py-2 text-sm text-slate-400">
                      {new Date(idea.last_updated).toLocaleString()}
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
          {filtered.length === 0 && (
            <div className="p-4 text-sm text-amber-300">
              No registry ideas match the current filters.
            </div>
          )}
        </div>

        <div className="hud-panel p-4">
          {!selected ? (
            <p className="text-sm text-slate-400">Select a registry idea to review details.</p>
          ) : (
            <div className="space-y-4 text-sm text-slate-300">
              <div>
                <h3 className="text-lg font-semibold text-cyan-100">{selected.title}</h3>
                <p className="mt-1 text-slate-300">{selected.summary}</p>
              </div>
              <div className="grid grid-cols-1 gap-2 sm:grid-cols-2">
                <div><span className="text-slate-500">Review state:</span> {selected.review_state}</div>
                <div><span className="text-slate-500">Queue eligibility:</span> {selected.queue_eligibility ? "true" : "false"}</div>
                <div><span className="text-slate-500">Status:</span> {selected.status}</div>
                <div><span className="text-slate-500">Queue reason:</span> {selected.queue_reason}</div>
              </div>
              <div>
                <div className="text-xs uppercase tracking-wider text-slate-500">Canonical problem</div>
                <div>{selected.canonical_problem}</div>
              </div>
              <div>
                <div className="text-xs uppercase tracking-wider text-slate-500">Canonical pattern</div>
                <div>{selected.canonical_pattern}</div>
              </div>
              <div>
                <div className="text-xs uppercase tracking-wider text-slate-500">Promotion reason</div>
                <div>{selected.promotion_reason || "—"}</div>
              </div>
              <div>
                <div className="text-xs uppercase tracking-wider text-slate-500">Score breakdown</div>
                <pre className="mt-1 overflow-x-auto rounded border border-cyan-500/20 bg-slate-950 p-2 text-xs text-cyan-100">
                  {JSON.stringify(selected.score_breakdown, null, 2)}
                </pre>
              </div>
              <div>
                <div className="text-xs uppercase tracking-wider text-slate-500">Review notes</div>
                <div>{selected.review_notes || "—"}</div>
              </div>
              <div>
                <div className="text-xs uppercase tracking-wider text-slate-500">Implementation notes</div>
                <div>{selected.implementation_notes || "—"}</div>
              </div>
              <div>
                <div className="text-xs uppercase tracking-wider text-slate-500">Dependencies</div>
                <div>{selected.dependencies.length > 0 ? selected.dependencies.join(", ") : "—"}</div>
              </div>
              <div>
                <div className="text-xs uppercase tracking-wider text-slate-500">Related ideas</div>
                <div>{selected.related_ideas.length > 0 ? selected.related_ideas.join(", ") : "—"}</div>
              </div>
              <div>
                <div className="text-xs uppercase tracking-wider text-slate-500">Supporting source refs</div>
                <div>{selected.source_refs.length > 0 ? selected.source_refs.join(", ") : "—"}</div>
              </div>
            </div>
          )}
        </div>
      </section>
    </div>
  );
}
