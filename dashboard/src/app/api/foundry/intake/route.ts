import { NextResponse } from "next/server";
import { runFoundryLaneIntake, type FoundryLane } from "@/lib/foundry-intake";

interface IntakeBody {
  lane?: FoundryLane;
  input?: string;
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

  try {
    const result = await runFoundryLaneIntake(lane, input);
    return NextResponse.json(result, { status: 200 });
  } catch (error) {
    const message = error instanceof Error ? error.message : "Unexpected intake failure.";
    return NextResponse.json({ status: "error", message }, { status: 500 });
  }
}
