"use client";

import { useEffect, useMemo, useState } from "react";
import type {
  FoundryLane,
  FoundryTopIdea,
  FoundryIntakeScoringEvaluationPayload,
  FoundryScoringMode,
} from "@/lib/foundry-intake";
import {
  computeIntakeWeightedScorePreview,
  RUBRIC_KEYS,
  type IntakeHeuristicDimensions,
} from "@/lib/foundry-scoring";

interface IntakeResult {
  status: "success";
  lane: FoundryLane;
  run_id: string;
  limitation_note: string;
  source_record: Record<string, unknown>;
  candidate_ideas: Array<Record<string, unknown>>;
  output_paths: Record<string, string>;
  top_10_lane_ideas: FoundryTopIdea[];
  scoring_evaluation: FoundryIntakeScoringEvaluationPayload;
}

interface OptionAPreviewResponse {
  status: "success";
  lane: FoundryLane;
  rubric_anchor_version: string;
  proposal_evaluation_method: string;
  heuristic_prefill_scores: Record<string, number>;
  proposed_scores: Record<string, number>;
  score_reasons: Record<string, string>;
  evidence_support: Record<string, string>;
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

const DEFAULT_MANUAL: Record<string, number> = Object.fromEntries(RUBRIC_KEYS.map((k) => [k, 2]));

function rubricBand(w: number): string {
  if (w < 35) return "discard";
  if (w <= 49) return "watchlist";
  if (w <= 64) return "research_next";
  if (w <= 79) return "implement_soon";
  return "queue_candidate";
}

/** GitHub only: trim, then add https:// for bare github.com paths so server validation accepts common pastes. */
function normalizeGithubInput(raw: string): string {
  const trimmed = raw.trim();
  if (/^https?:\/\//i.test(trimmed)) return trimmed;
  if (/^(www\.)?github\.com\/.+/i.test(trimmed)) {
    return `https://${trimmed.replace(/^\/+/, "")}`;
  }
  return trimmed;
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
  const [scoringMode, setScoringMode] = useState<FoundryScoringMode>("option_a_rubric_assisted");
  const [manualRubric, setManualRubric] = useState<Record<string, number>>({ ...DEFAULT_MANUAL });
  const [status, setStatus] = useState<"idle" | "submitting" | "success" | "error">("idle");
  const [errorMessage, setErrorMessage] = useState("");
  const [result, setResult] = useState<IntakeResult | null>(null);
  const [topIdeas, setTopIdeas] = useState<FoundryTopIdea[]>(initialTopIdeas);

  const [optionAPreview, setOptionAPreview] = useState<OptionAPreviewResponse | null>(null);
  const [optionALocked, setOptionALocked] = useState<Record<string, number> | null>(null);
  const [previewBusy, setPreviewBusy] = useState(false);
  const [previewError, setPreviewError] = useState("");

  useEffect(() => {
    setOptionAPreview(null);
    setOptionALocked(null);
    setPreviewError("");
  }, [input, scoringMode]);

  const manualPayload = useMemo(() => {
    const o: Record<string, number> = {};
    for (const k of RUBRIC_KEYS) {
      o[k] = manualRubric[k] ?? 2;
    }
    return o;
  }, [manualRubric]);

  const optionALockedDims = useMemo(() => {
    if (!optionALocked) return null;
    const o = { ...optionALocked } as Record<string, number>;
    for (const k of RUBRIC_KEYS) {
      o[k] = optionALocked[k] ?? 2;
    }
    return o as IntakeHeuristicDimensions;
  }, [optionALocked]);

  const lockedWeightedPreview = useMemo(() => {
    if (!optionALockedDims) return null;
    return computeIntakeWeightedScorePreview(optionALockedDims);
  }, [optionALockedDims]);

  async function runOptionAPreview() {
    setPreviewBusy(true);
    setPreviewError("");
    try {
      const inputForRequest = lane === "github" ? normalizeGithubInput(input) : input;
      const response = await fetch("/api/foundry/option-a-preview", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ lane, input: inputForRequest }),
      });
      const payload = (await response.json()) as OptionAPreviewResponse | { status: "error"; message: string };
      if (!response.ok || payload.status !== "success") {
        throw new Error("message" in payload ? payload.message : "Preview failed.");
      }
      setOptionAPreview(payload);
      const locked: Record<string, number> = {};
      for (const k of RUBRIC_KEYS) {
        locked[k] = payload.proposed_scores[k] ?? 2;
      }
      setOptionALocked(locked);
    } catch (e) {
      setPreviewError(e instanceof Error ? e.message : "Preview failed.");
      setOptionAPreview(null);
      setOptionALocked(null);
    } finally {
      setPreviewBusy(false);
    }
  }

  async function onSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setStatus("submitting");
    setErrorMessage("");

    try {
      // Article / X post: send the textarea value as-is (server validates with trim). GitHub: normalize URL only.
      const inputForRequest = lane === "github" ? normalizeGithubInput(input) : input;
      if (lane === "github" && inputForRequest !== input) {
        setInput(inputForRequest);
      }
      if (scoringMode === "option_a_rubric_assisted") {
        if (!optionALocked) {
          setStatus("error");
          setErrorMessage(
            'Option A: click "Preview rubric proposal" first, adjust locked 0–5 scores if needed, then submit intake.'
          );
          return;
        }
      }

      const body: Record<string, unknown> = { lane, input: inputForRequest, scoring_mode: scoringMode };
      if (scoringMode === "option_b_manual_matrix") {
        body.manual_rubric_scores = manualPayload;
      }
      if (scoringMode === "option_a_rubric_assisted" && optionALocked) {
        const lockedPayload: Record<string, number> = {};
        for (const k of RUBRIC_KEYS) {
          lockedPayload[k] = optionALocked[k] ?? 2;
        }
        body.option_a_locked_rubric_scores = lockedPayload;
      }

      const response = await fetch("/api/foundry/intake", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify(body),
      });
      const payload = (await response.json()) as IntakeResult | { status: "error"; message: string };
      if (!response.ok || payload.status !== "success") {
        const message = "message" in payload ? payload.message : "Intake request failed.";
        throw new Error(message);
      }
      setResult(payload);
      setTopIdeas(Array.isArray(payload.top_10_lane_ideas) ? payload.top_10_lane_ideas : []);
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
          Option A: explicit 0–5 rubric anchors → proposal + source-tied reasons/snippets; you preview, then lock final integers
          (edit if needed) before intake runs. Heuristic prefill is shown separately and is not the matrix. Option B: you enter all
          eight 0–5 integers manually. Engine weighted formula is unchanged. Local JSON only; bounded rules—not semantic certainty.
        </p>
      </div>

      <section className="hud-panel p-4">
        <form className="space-y-4" onSubmit={onSubmit} noValidate>
          <fieldset className="space-y-2">
            <legend className="text-xs font-medium uppercase tracking-wider text-cyan-400/80">Scoring mode</legend>
            <label className="flex cursor-pointer items-center gap-2 text-sm text-slate-300">
              <input
                type="radio"
                name="scoring_mode"
                checked={scoringMode === "option_a_rubric_assisted"}
                onChange={() => setScoringMode("option_a_rubric_assisted")}
                className="border-cyan-500/40"
              />
              Option A — rubric-assisted (explicit anchors → proposal; operator locks final)
            </label>
            <label className="flex cursor-pointer items-center gap-2 text-sm text-slate-300">
              <input
                type="radio"
                name="scoring_mode"
                checked={scoringMode === "option_b_manual_matrix"}
                onChange={() => setScoringMode("option_b_manual_matrix")}
                className="border-cyan-500/40"
              />
              Option B — manual rubric matrix (operator 0–5 per dimension)
            </label>
          </fieldset>

          {scoringMode === "option_a_rubric_assisted" && (
            <div className="space-y-3 rounded border border-cyan-500/20 bg-cyan-500/5 p-3">
              <div className="text-xs font-medium uppercase tracking-wider text-cyan-200/90">Option A — preview & lock</div>
              <button
                type="button"
                disabled={previewBusy || status === "submitting"}
                onClick={() => void runOptionAPreview()}
                className="rounded border border-cyan-500/40 bg-slate-950 px-3 py-2 text-sm text-cyan-100 hover:bg-slate-900 disabled:opacity-50"
              >
                {previewBusy ? "Building proposal…" : "Preview rubric proposal"}
              </button>
              {previewError ? <p className="text-sm text-amber-300">{previewError}</p> : null}
              {optionAPreview ? (
                <div className="space-y-2 text-xs text-slate-400">
                  <p>
                    <span className="text-slate-500">Matrix version:</span>{" "}
                    <span className="font-mono text-cyan-200/90">{optionAPreview.rubric_anchor_version}</span> ·{" "}
                    <span className="text-slate-500">proposal method:</span>{" "}
                    <span className="font-mono text-cyan-200/90">{optionAPreview.proposal_evaluation_method}</span>
                  </p>
                  <p className="text-slate-500">
                    Heuristic prefill (legacy buckets, not rubric truth): shown per dimension as “prefill” in the table below.
                  </p>
                  <div className="overflow-x-auto">
                    <table className="min-w-full border border-cyan-500/15 text-left">
                      <thead>
                        <tr className="bg-slate-950/80">
                          <th className="px-2 py-1 text-slate-500">Dimension</th>
                          <th className="px-2 py-1 text-slate-500">Prefill</th>
                          <th className="px-2 py-1 text-slate-500">Proposed</th>
                          <th className="px-2 py-1 text-slate-500">Locked (submit)</th>
                          <th className="px-2 py-1 text-slate-500">Reason</th>
                          <th className="px-2 py-1 text-slate-500">Evidence</th>
                        </tr>
                      </thead>
                      <tbody>
                        {RUBRIC_KEYS.map((key) => (
                          <tr key={key} className="border-t border-cyan-500/10">
                            <td className="px-2 py-1 font-mono text-cyan-100/90">{key}</td>
                            <td className="px-2 py-1 text-slate-500">{optionAPreview.heuristic_prefill_scores[key]}</td>
                            <td className="px-2 py-1 text-slate-300">{optionAPreview.proposed_scores[key]}</td>
                            <td className="px-2 py-1">
                              <select
                                value={optionALocked?.[key] ?? optionAPreview.proposed_scores[key]}
                                onChange={(e) =>
                                  setOptionALocked((prev) => ({
                                    ...(prev ?? {}),
                                    [key]: Number.parseInt(e.target.value, 10),
                                  }))
                                }
                                className="rounded border border-cyan-500/30 bg-slate-950 px-1 py-0.5 text-slate-200"
                              >
                                {[0, 1, 2, 3, 4, 5].map((n) => (
                                  <option key={n} value={n}>
                                    {n}
                                  </option>
                                ))}
                              </select>
                            </td>
                            <td className="max-w-[200px] px-2 py-1 text-slate-500">{optionAPreview.score_reasons[key]}</td>
                            <td className="max-w-[160px] truncate px-2 py-1 text-slate-600">
                              {optionAPreview.evidence_support[key]}
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                  {lockedWeightedPreview !== null ? (
                    <p className="text-sm text-teal-200/90">
                      Locked weighted preview (same formula as engine): {lockedWeightedPreview.toFixed(2)} · band:{" "}
                      {rubricBand(lockedWeightedPreview)}
                    </p>
                  ) : null}
                </div>
              ) : null}
            </div>
          )}

          {scoringMode === "option_b_manual_matrix" && (
            <div className="rounded border border-amber-500/20 bg-amber-500/5 p-3">
              <div className="mb-2 text-xs font-medium uppercase tracking-wider text-amber-200/90">Manual rubric (0–5)</div>
              <div className="grid grid-cols-1 gap-2 sm:grid-cols-2">
                {RUBRIC_KEYS.map((key) => (
                  <label key={key} className="flex items-center justify-between gap-2 text-sm text-slate-300">
                    <span className="font-mono text-xs text-slate-400">{key}</span>
                    <select
                      value={manualRubric[key] ?? 2}
                      onChange={(e) =>
                        setManualRubric((prev) => ({ ...prev, [key]: Number.parseInt(e.target.value, 10) }))
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
            </div>
          )}

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
                type={lane === "github" ? "text" : "url"}
                inputMode={lane === "github" ? "url" : undefined}
                autoComplete={lane === "github" ? "url" : undefined}
                spellCheck={lane === "github" ? false : undefined}
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder={inputPlaceholder}
                className="w-full rounded border border-cyan-500/20 bg-slate-950 px-3 py-2 text-slate-200 placeholder:text-slate-500"
              />
            )}
          </label>
          <button
            type="submit"
            disabled={
              status === "submitting" ||
              (scoringMode === "option_a_rubric_assisted" && !optionALocked)
            }
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
              <span className="text-slate-500">Persisted scoring mode:</span>{" "}
              <span className="font-mono text-cyan-200/90">{result.scoring_evaluation.scoring_mode_selected}</span> ·{" "}
              <span className="text-slate-500">method:</span>{" "}
              <span className="font-mono text-cyan-200/90">{result.scoring_evaluation.evaluation_method}</span>
              {result.scoring_evaluation.rubric_anchor_version ? (
                <>
                  {" "}
                  · <span className="text-slate-500">rubric matrix:</span>{" "}
                  <span className="font-mono text-cyan-200/90">{result.scoring_evaluation.rubric_anchor_version}</span>
                </>
              ) : null}
            </p>
            <p>
              <span className="text-slate-500">Weighted score (locked formula):</span>{" "}
              <span className="text-cyan-200">
                {Number.isFinite(result.scoring_evaluation.weighted_score)
                  ? result.scoring_evaluation.weighted_score.toFixed(2)
                  : "—"}
              </span>{" "}
              · band:{" "}
              {Number.isFinite(result.scoring_evaluation.weighted_score)
                ? rubricBand(result.scoring_evaluation.weighted_score)
                : "—"}
            </p>
            <p>
              <span className="text-slate-500">Review summary:</span> {asString(result.source_record.review_summary)}
            </p>
          </div>
        )}
      </section>

      {status === "success" && result && (
        <section className="hud-panel p-4">
          <h3 className="mb-2 text-xs font-medium uppercase tracking-widest text-cyan-400/80">Scoring audit (this run)</h3>
          <p className="mb-2 text-xs text-slate-500">
            Saved to <span className="font-mono text-cyan-200/80">{result.scoring_evaluation.sidecar_path}</span> — flipping the
            page toggle later does not change this record.
          </p>
          <div className="overflow-x-auto text-xs">
            <table className="min-w-full border border-cyan-500/15">
              <thead>
                <tr className="bg-slate-950/80">
                  <th className="px-2 py-1 text-left text-slate-500">Dimension</th>
                  <th className="px-2 py-1 text-left text-slate-500">Proposed</th>
                  <th className="px-2 py-1 text-left text-slate-500">Final</th>
                  <th className="px-2 py-1 text-left text-slate-500">Reason</th>
                  <th className="px-2 py-1 text-left text-slate-500">Support snippet</th>
                </tr>
              </thead>
              <tbody>
                {RUBRIC_KEYS.map((k) => (
                  <tr key={k} className="border-t border-cyan-500/10">
                    <td className="px-2 py-1 font-mono text-cyan-100/90">{k}</td>
                    <td className="px-2 py-1 text-slate-400">
                      {result.scoring_evaluation.proposed_scores?.[k] ?? "—"}
                    </td>
                    <td className="px-2 py-1 text-slate-200">{result.scoring_evaluation.final_scores[k]}</td>
                    <td className="max-w-[220px] px-2 py-1 text-slate-400">
                      {result.scoring_evaluation.score_reasons?.[k] ?? "—"}
                    </td>
                    <td className="max-w-[200px] truncate px-2 py-1 text-slate-500">
                      {result.scoring_evaluation.evidence_support?.[k] ?? "—"}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>
      )}

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
                  recommendation: {asString(idea.recommendation_state)} | weighted_score: {String(idea.weighted_score ?? "—")} (engine
                  formula on final integers)
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
        <h3 className="mb-3 text-xs font-medium uppercase tracking-widest text-cyan-400/80">Top 10 ideas for this source lane</h3>
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
                    <td className="px-3 py-2 text-sm text-cyan-200">
                      {Number.isFinite(idea.weighted_score) ? idea.weighted_score.toFixed(2) : "—"}
                    </td>
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
