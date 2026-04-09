import { NextResponse } from "next/server";
import { buildFoundryOptionAPreview, type FoundryLane } from "@/lib/foundry-intake";

interface Body {
  lane?: FoundryLane;
  input?: string;
}

export async function POST(request: Request) {
  let body: Body;
  try {
    body = (await request.json()) as Body;
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
    const preview = buildFoundryOptionAPreview(lane, input);
    return NextResponse.json(preview, { status: 200 });
  } catch (error) {
    const message = error instanceof Error ? error.message : "Preview failed.";
    return NextResponse.json({ status: "error", message }, { status: 400 });
  }
}
