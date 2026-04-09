/**
 * Server-only: scoring_evaluations sidecar JSON via FoundryStorage (fs or Vercel Blob).
 */

import { readdir, readFile } from "fs/promises";
import { join } from "path";
import {
  computeIntakeWeightedScorePreview,
  type FoundryScoringEvaluation,
  type FoundryScoringMode,
  type IntakeHeuristicDimensions,
  type RubricDimensionKey,
} from "./foundry-scoring";
import {
  createFoundryStorage,
  foundryBlobPrefixes,
  foundryStateRoot,
  type FoundryStorage,
} from "./foundry-storage";

export async function writeScoringEvaluationSidecar(
  payload: {
    candidateId: string;
    sourceId: string;
    engineRunId: string;
    mode: FoundryScoringMode;
    heuristicPrefill: IntakeHeuristicDimensions | null;
    proposed: IntakeHeuristicDimensions | null;
    finalScores: IntakeHeuristicDimensions;
    scoreReasons: Record<RubricDimensionKey, string> | null;
    evidenceSupport: Record<RubricDimensionKey, string> | null;
    evaluationMethod: string;
    rubricAnchorVersion?: string;
  },
  store?: FoundryStorage
): Promise<{ relativePath: string; evaluation: FoundryScoringEvaluation }> {
  const s = store ?? (await createFoundryStorage());
  const ideaId = `idea_${payload.candidateId}`;
  const weighted_score = computeIntakeWeightedScorePreview(payload.finalScores);
  const created_at = new Date().toISOString();
  const evaluation_id = `eval_${payload.candidateId}`;

  const doc: FoundryScoringEvaluation = {
    evaluation_id,
    idea_id: ideaId,
    candidate_id: payload.candidateId,
    source_id: payload.sourceId,
    engine_run_id: payload.engineRunId,
    scoring_mode_selected: payload.mode,
    evaluation_method: payload.evaluationMethod,
    heuristic_prefill_scores: payload.heuristicPrefill,
    proposed_scores: payload.proposed,
    final_scores: payload.finalScores,
    score_reasons: payload.scoreReasons,
    evidence_support: payload.evidenceSupport,
    weighted_score,
    created_at,
    ...(payload.rubricAnchorVersion ? { rubric_anchor_version: payload.rubricAnchorVersion } : {}),
  };

  const fileName = `${evaluation_id}.json`;
  await s.putJson(`${foundryBlobPrefixes.scoringEvaluations}${fileName}`, doc);
  const relativePath = `future_modules/the_foundry/state/scoring_evaluations/${fileName}`;
  return { relativePath, evaluation: doc };
}

export async function loadAllScoringEvaluationsByIdeaId(
  store?: FoundryStorage
): Promise<Record<string, FoundryScoringEvaluation>> {
  const s = store ?? (await createFoundryStorage());
  const map: Record<string, FoundryScoringEvaluation> = {};

  if (s.driver === "blob") {
    const dir = join(foundryStateRoot(), "scoring_evaluations");
    try {
      const names = await readdir(dir);
      for (const name of names.filter((n) => n.endsWith(".json"))) {
        try {
          const raw = JSON.parse(await readFile(join(dir, name), "utf-8")) as FoundryScoringEvaluation;
          if (typeof raw.idea_id === "string") map[raw.idea_id] = raw;
        } catch {
          /* skip */
        }
      }
    } catch {
      /* missing dir */
    }
  }

  try {
    const keys = await s.listJsonKeys(foundryBlobPrefixes.scoringEvaluations);
    for (const key of keys) {
      try {
        const raw = await s.getJson<FoundryScoringEvaluation>(key);
        if (raw && typeof raw.idea_id === "string") map[raw.idea_id] = raw;
      } catch {
        /* skip */
      }
    }
  } catch {
    /* */
  }

  return map;
}
