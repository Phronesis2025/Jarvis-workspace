"use client";

import { useState } from "react";
import type { FoundryLane, FoundryTopIdea } from "@/lib/foundry-intake";

interface IntakeResult {
  status: "success";
  lane: FoundryLane;
  run_id: string;
  limitation_note: string;
  source_record: Record<string, unknown>;
  candidate_ideas: Array<Record<string, unknown>>;
  output_paths: Record<string, string>;
  top_10_lane_ideas: FoundryTopIdea[];
}

interface Props {
  lane: FoundryLane;
  pageTitle: string;
  inputLabel: string;
  inputPlaceholder: string;
  inputType: "textarea" | "url";
  initialTopIdeas: FoundryTopIdea[];
}

function asString(value: unknown): string {
  return typeof value === "string" ? value : "—";
}

export function FoundryLaneIntakeClient({
  lane,
  pageTitle,
  inputLabel,
  inputPlaceholder,
  inputType,
  initialTopIdeas,
}: Props) {
  const [input, setInput] = useState("");
  const [status, setStatus] = useState<"idle" | "submitting" | "success" | "error">("idle");
  const [errorMessage, setErrorMessage] = useState("");
  const [result, setResult] = useState<IntakeResult | null>(null);
  const [topIdeas, setTopIdeas] = useState<FoundryTopIdea[]>(initialTopIdeas);

  async function onSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setStatus("submitting");
    setErrorMessage("");

    try {
      const response = await fetch("/api/foundry/intake", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ lane, input }),
      });
      const payload = (await response.json()) as IntakeResult | { status: "error"; message: string };
      if (!response.ok || payload.status !== "success") {
        const message = "message" in payload ? payload.message : "Intake request failed.";
        throw new Error(message);
      }
      setResult(payload);
      setTopIdeas(payload.top_10_lane_ideas);
      setStatus("success");
    } catch (error) {
      setStatus("error");
      setErrorMessage(error instanceof Error ? error.message : "Unexpected intake failure.");
    }
  }

  return (
    <div className="space-y-6">
      <div className="flex flex-col gap-1">
        <h2 className="text-xl font-semibold tracking-tight text-cyan-100">{pageTitle}</h2>
        <p className="text-sm text-slate-400">
          Local bounded intake. Scores are deterministic heuristics (length, lane, light structure, keyword hits)—not LLM
          semantic ranking. Writes Foundry local JSON.
        </p>
      </div>

      <section className="hud-panel p-4">
        <form className="space-y-3" onSubmit={onSubmit}>
          <label className="block text-sm text-slate-300">
            <span className="mb-1 block text-slate-400">{inputLabel}</span>
            {inputType === "textarea" ? (
              <textarea
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder={inputPlaceholder}
                rows={8}
                className="w-full rounded border border-cyan-500/20 bg-slate-950 px-3 py-2 text-slate-200 placeholder:text-slate-500"
              />
            ) : (
              <input
                type="url"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder={inputPlaceholder}
                className="w-full rounded border border-cyan-500/20 bg-slate-950 px-3 py-2 text-slate-200 placeholder:text-slate-500"
              />
            )}
          </label>
          <button
            type="submit"
            disabled={status === "submitting"}
            className="rounded bg-cyan-600 px-4 py-2 text-sm font-medium text-white disabled:cursor-not-allowed disabled:opacity-60"
          >
            {status === "submitting" ? "Submitting..." : "Submit Intake"}
          </button>
        </form>
      </section>

      <section className="hud-panel p-4">
        <h3 className="mb-2 text-xs font-medium uppercase tracking-widest text-cyan-400/80">Intake result status</h3>
        {status === "idle" && <p className="text-sm text-slate-500">No intake submitted yet.</p>}
        {status === "submitting" && <p className="text-sm text-cyan-300">Submitting intake and running local engine...</p>}
        {status === "error" && <p className="text-sm text-amber-300">Error: {errorMessage}</p>}
        {status === "success" && result && (
          <div className="space-y-2 text-sm text-slate-300">
            <p className="text-teal-300">Success. Run ID: {result.run_id}</p>
            <p className="text-slate-400">{result.limitation_note}</p>
            <p>
              <span className="text-slate-500">Review summary:</span>{" "}
              {asString(result.source_record.review_summary)}
            </p>
            <p>
              <span className="text-slate-500">Processed output ref:</span>{" "}
              {asString(result.source_record.processed_output_ref)}
            </p>
          </div>
        )}
      </section>

      <section className="hud-panel p-4">
        <h3 className="mb-2 text-xs font-medium uppercase tracking-widest text-cyan-400/80">Candidate ideas from this intake</h3>
        {!result || result.candidate_ideas.length === 0 ? (
          <p className="text-sm text-slate-500">No candidate ideas returned yet.</p>
        ) : (
          <div className="space-y-3">
            {result.candidate_ideas.map((idea, idx) => (
              <div key={`${asString(idea.candidate_id)}_${idx}`} className="rounded border border-cyan-500/20 bg-slate-950 p-3 text-sm">
                <div className="font-medium text-cyan-200">{asString(idea.title)}</div>
                <div className="mt-1 text-slate-300">{asString(idea.summary)}</div>
                <div className="mt-2 text-xs text-slate-500">
                  recommendation: {asString(idea.recommendation_state)} | weighted_score: {String(idea.weighted_score ?? "—")}{" "}
                  (heuristic dims → engine formula; not full meaning)
                </div>
              </div>
            ))}
          </div>
        )}
      </section>

      <section className="hud-panel p-4">
        <h3 className="mb-2 text-xs font-medium uppercase tracking-widest text-cyan-400/80">Storage/output confirmation</h3>
        {!result ? (
          <p className="text-sm text-slate-500">No output written yet for this page session.</p>
        ) : (
          <ul className="space-y-1 text-sm text-slate-300">
            {Object.entries(result.output_paths).map(([key, value]) => (
              <li key={key}>
                <span className="text-slate-500">{key}:</span> <span className="font-mono text-cyan-200">{value}</span>
              </li>
            ))}
          </ul>
        )}
      </section>

      <section className="hud-panel p-4">
        <h3 className="mb-3 text-xs font-medium uppercase tracking-widest text-cyan-400/80">
          Top 10 ideas for this source lane
        </h3>
        {topIdeas.length === 0 ? (
          <p className="text-sm text-slate-500">No registry ideas currently mapped to this lane.</p>
        ) : (
          <div className="overflow-x-auto">
            <table className="min-w-full divide-y divide-slate-700/50">
              <thead>
                <tr>
                  <th className="px-3 py-2 text-left text-xs text-slate-500">Title</th>
                  <th className="px-3 py-2 text-left text-xs text-slate-500">Status</th>
                  <th className="px-3 py-2 text-left text-xs text-slate-500">Score</th>
                  <th className="px-3 py-2 text-left text-xs text-slate-500">Category</th>
                  <th className="px-3 py-2 text-left text-xs text-slate-500">Sources</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-700/30">
                {topIdeas.map((idea) => (
                  <tr key={idea.idea_id}>
                    <td className="px-3 py-2 text-sm text-slate-200">{idea.title}</td>
                    <td className="px-3 py-2 text-sm text-slate-400">{idea.status}</td>
                    <td className="px-3 py-2 text-sm text-cyan-200">{idea.weighted_score.toFixed(2)}</td>
                    <td className="px-3 py-2 text-sm text-slate-400">{idea.category}</td>
                    <td className="px-3 py-2 text-sm text-slate-400">{idea.supporting_source_count}</td>
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
