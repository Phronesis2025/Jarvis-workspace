"use client";

import { useMemo, useState } from "react";
import type { FoundryRegistryIdea, FoundryScoringEvaluation } from "@/lib/types";
import { RUBRIC_KEYS } from "@/lib/foundry-scoring";

interface Props {
  ideas: FoundryRegistryIdea[];
  sourceLanesByIdeaId: Record<string, string[]>;
  scoringEvaluationsByIdeaId: Record<string, FoundryScoringEvaluation | null>;
}

function rubricBand(w: number): string {
  if (w < 35) return "discard";
  if (w <= 49) return "watchlist";
  if (w <= 64) return "research_next";
  if (w <= 79) return "implement_soon";
  return "queue_candidate";
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

const SANDBOX_DEFAULT: Record<string, number> = Object.fromEntries(RUBRIC_KEYS.map((k) => [k, 2]));

export function FoundryRegistryReviewClient({ ideas, sourceLanesByIdeaId, scoringEvaluationsByIdeaId }: Props) {
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

  const persistedEval = selected ? scoringEvaluationsByIdeaId[selected.idea_id] : null;

  const [sandboxRubric, setSandboxRubric] = useState<Record<string, number>>({ ...SANDBOX_DEFAULT });
  const [sandboxPreview, setSandboxPreview] = useState<{ weighted_score: number; note?: string } | null>(null);
  const [sandboxBusy, setSandboxBusy] = useState(false);
  const [sandboxErr, setSandboxErr] = useState("");

  async function runSandboxPreview() {
    setSandboxBusy(true);
    setSandboxErr("");
    try {
      const manual_rubric_scores: Record<string, number> = {};
      for (const k of RUBRIC_KEYS) {
        manual_rubric_scores[k] = sandboxRubric[k] ?? 2;
      }
      const res = await fetch("/api/foundry/score-preview", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ manual_rubric_scores }),
      });
      const data = (await res.json()) as { status: string; weighted_score?: number; note?: string; message?: string };
      if (!res.ok || data.status !== "success" || data.weighted_score === undefined) {
        throw new Error(data.message ?? "Preview failed.");
      }
      setSandboxPreview({ weighted_score: data.weighted_score, note: data.note });
    } catch (e) {
      setSandboxErr(e instanceof Error ? e.message : "Preview failed.");
      setSandboxPreview(null);
    } finally {
      setSandboxBusy(false);
    }
  }

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
              <div className="rounded border border-cyan-500/20 bg-slate-950/60 p-3">
                <div className="text-xs font-medium uppercase tracking-wider text-cyan-400/80">
                  Persisted intake scoring audit (sidecar)
                </div>
                <p className="mt-1 text-xs text-slate-500">
                  Registry JSON below is unchanged when you change filters. This panel shows what was saved at dashboard intake
                  time (if any). No silent re-score on toggle.
                </p>
                {!persistedEval ? (
                  <p className="mt-2 text-sm text-slate-500">
                    No <span className="font-mono">scoring_evaluations/</span> file for this idea (pre-A/B intake or non-dashboard
                    origin).
                  </p>
                ) : (
                  <div className="mt-2 space-y-2 text-xs">
                    <div>
                      <span className="text-slate-500">Mode:</span>{" "}
                      <span className="font-mono text-cyan-200/90">{persistedEval.scoring_mode_selected}</span> ·{" "}
                      <span className="text-slate-500">method:</span>{" "}
                      <span className="font-mono text-cyan-200/90">{persistedEval.evaluation_method}</span>
                    </div>
                    <div>
                      <span className="text-slate-500">Sidecar weighted_score:</span>{" "}
                      <span className="text-cyan-200">{persistedEval.weighted_score.toFixed(2)}</span> · band:{" "}
                      {rubricBand(persistedEval.weighted_score)} ·{" "}
                      <span className="text-slate-500">engine_run_id:</span> {persistedEval.engine_run_id}
                    </div>
                    <div className="overflow-x-auto">
                      <table className="min-w-full border border-cyan-500/15 text-left">
                        <thead>
                          <tr className="bg-slate-950">
                            <th className="px-2 py-1 text-slate-500">Dim</th>
                            <th className="px-2 py-1 text-slate-500">Final</th>
                            <th className="px-2 py-1 text-slate-500">Reason</th>
                          </tr>
                        </thead>
                        <tbody>
                          {RUBRIC_KEYS.map((k) => (
                            <tr key={k} className="border-t border-cyan-500/10">
                              <td className="px-2 py-1 font-mono text-cyan-100/80">{k}</td>
                              <td className="px-2 py-1">{persistedEval.final_scores[k]}</td>
                              <td className="max-w-[200px] px-2 py-1 text-slate-400">
                                {persistedEval.score_reasons?.[k] ?? "—"}
                              </td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  </div>
                )}
              </div>
              <div className="rounded border border-amber-500/25 bg-amber-500/5 p-3">
                <div className="text-xs font-medium uppercase tracking-wider text-amber-200/90">
                  Manual rubric sandbox (Option B preview only)
                </div>
                <p className="mt-1 text-xs text-slate-500">
                  Try different 0–5 integers; preview uses the locked formula only. Does not write registry or sidecar files.
                </p>
                <div className="mt-2 grid grid-cols-1 gap-2 sm:grid-cols-2">
                  {RUBRIC_KEYS.map((key) => (
                    <label key={key} className="flex items-center justify-between gap-2 text-xs text-slate-300">
                      <span className="font-mono text-slate-400">{key}</span>
                      <select
                        value={sandboxRubric[key] ?? 2}
                        onChange={(e) =>
                          setSandboxRubric((prev) => ({ ...prev, [key]: Number.parseInt(e.target.value, 10) }))
                        }
                        className="rounded border border-cyan-500/20 bg-slate-950 px-2 py-1 text-slate-200"
                      >
                        {[0, 1, 2, 3, 4, 5].map((n) => (
                          <option key={n} value={n}>
                            {n}
                          </option>
                        ))}
                      </select>
                    </label>
                  ))}
                </div>
                <button
                  type="button"
                  onClick={() => void runSandboxPreview()}
                  disabled={sandboxBusy}
                  className="mt-3 rounded bg-amber-700/90 px-3 py-1.5 text-xs font-medium text-white disabled:opacity-50"
                >
                  {sandboxBusy ? "Computing…" : "Preview weighted score"}
                </button>
                {sandboxErr && <p className="mt-2 text-xs text-amber-300">{sandboxErr}</p>}
                {sandboxPreview && (
                  <p className="mt-2 text-sm text-cyan-200">
                    Preview weighted_score: {sandboxPreview.weighted_score.toFixed(2)} · band:{" "}
                    {rubricBand(sandboxPreview.weighted_score)}
                    {sandboxPreview.note ? <span className="block text-xs text-slate-500">{sandboxPreview.note}</span> : null}
                  </p>
                )}
              </div>
              <div>
                <div className="text-xs uppercase tracking-wider text-slate-500">Eight dimensions (registry record)</div>
                <div className="mt-1 grid grid-cols-2 gap-1 text-xs sm:grid-cols-4">
                  <span className="text-slate-500">evidence_strength</span>
                  <span>{selected.evidence_strength}</span>
                  <span className="text-slate-500">transferability</span>
                  <span>{selected.transferability}</span>
                  <span className="text-slate-500">expected_upside</span>
                  <span>{selected.expected_upside}</span>
                  <span className="text-slate-500">risk_reduction_value</span>
                  <span>{selected.risk_reduction_value}</span>
                  <span className="text-slate-500">implementation_cost</span>
                  <span>{selected.implementation_cost}</span>
                  <span className="text-slate-500">novelty</span>
                  <span>{selected.novelty}</span>
                  <span className="text-slate-500">dependency_burden</span>
                  <span>{selected.dependency_burden}</span>
                  <span className="text-slate-500">confidence</span>
                  <span>{selected.confidence}</span>
                </div>
                <div className="mt-1 text-xs text-slate-500">
                  weighted_score: <span className="text-cyan-200">{selected.weighted_score.toFixed(2)}</span> · band:{" "}
                  {rubricBand(selected.weighted_score)}
                </div>
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
