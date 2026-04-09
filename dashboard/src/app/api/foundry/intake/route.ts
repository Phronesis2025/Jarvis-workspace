import { NextResponse } from "next/server";
import { runFoundryLaneIntake, type FoundryLane, type FoundryScoringMode } from "@/lib/foundry-intake";

interface IntakeBody {
  lane?: FoundryLane;
  input?: string;
  scoring_mode?: FoundryScoringMode;
  manual_rubric_scores?: unknown;
  option_a_locked_rubric_scores?: unknown;
}

export async function POST(request: Request) {
  let body: IntakeBody;
  try {
    body = (await request.json()) as IntakeBody;
  } catch {
    return NextResponse.json({ status: "error", message: "Invalid JSON body." }, { status: 400 });
  }

  const lane = body.lane;
  const input = body.input;
  if (lane !== "article" && lane !== "github" && lane !== "x_post") {
    return NextResponse.json({ status: "error", message: "Invalid lane." }, { status: 400 });
  }
  if (typeof input !== "string") {
    return NextResponse.json({ status: "error", message: "Input must be a string." }, { status: 400 });
  }

  const scoring_mode: FoundryScoringMode =
    body.scoring_mode === "option_b_manual_matrix" ? "option_b_manual_matrix" : "option_a_rubric_assisted";

  try {
    const result = await runFoundryLaneIntake(lane, input, {
      scoring_mode,
      manual_rubric_scores: body.manual_rubric_scores,
      option_a_locked_rubric_scores: body.option_a_locked_rubric_scores,
    });
    return NextResponse.json(result, { status: 200 });
  } catch (error) {
    const message = error instanceof Error ? error.message : "Unexpected intake failure.";
    return NextResponse.json({ status: "error", message }, { status: 500 });
  }
}
