import { NextResponse } from "next/server";
import { computeIntakeWeightedScorePreview, validateManualRubricScores } from "@/lib/foundry-scoring";

/**
 * Sandbox preview: locked formula only. Does not read or write registry/sidecar JSON.
 */
export async function POST(request: Request) {
  let body: { manual_rubric_scores?: unknown };
  try {
    body = (await request.json()) as { manual_rubric_scores?: unknown };
  } catch {
    return NextResponse.json({ status: "error", message: "Invalid JSON body." }, { status: 400 });
  }

  try {
    const dims = validateManualRubricScores(body.manual_rubric_scores);
    const weighted_score = computeIntakeWeightedScorePreview(dims);
    const rawSum =
      dims.evidence_strength * 0.22 +
      dims.transferability * 0.18 +
      dims.expected_upside * 0.16 +
      dims.risk_reduction_value * 0.14 +
      (5 - dims.implementation_cost) * 0.1 +
      dims.novelty * 0.08 +
      (5 - dims.dependency_burden) * 0.07 +
      dims.confidence * 0.05;
    return NextResponse.json({
      status: "success",
      weighted_score,
      score_breakdown: {
        evidence_strength: dims.evidence_strength * 0.22,
        transferability: dims.transferability * 0.18,
        expected_upside: dims.expected_upside * 0.16,
        risk_reduction_value: dims.risk_reduction_value * 0.14,
        implementation_cost_inverted: (5 - dims.implementation_cost) * 0.1,
        novelty: dims.novelty * 0.08,
        dependency_burden_inverted: (5 - dims.dependency_burden) * 0.07,
        confidence: dims.confidence * 0.05,
        raw_sum: Math.round(rawSum * 10000) / 10000,
      },
      note: "Preview only — does not change registry ideas or scoring_evaluations files.",
    });
  } catch (error) {
    const message = error instanceof Error ? error.message : "Validation failed.";
    return NextResponse.json({ status: "error", message }, { status: 400 });
  }
}
