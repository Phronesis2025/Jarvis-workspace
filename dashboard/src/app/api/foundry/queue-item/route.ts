import { NextResponse } from "next/server";
import {
  updateFoundryQueueItem,
  type FoundryQueueItemPatch,
  type FoundryQueueOperatorApproval,
  type FoundryQueueStatus,
} from "@/lib/foundry-queue";

const APPROVAL: FoundryQueueOperatorApproval[] = ["pending", "approved", "rejected"];
const STATUSES: FoundryQueueStatus[] = [
  "proposed",
  "ready",
  "in_design",
  "in_build",
  "blocked",
  "done",
  "dropped",
];

interface Body {
  queue_id?: string;
  operator_approval_state?: string;
  approval_notes?: string;
  status?: string;
  blockers?: unknown;
  next_action?: string;
}

export async function PATCH(request: Request) {
  let body: Body;
  try {
    body = (await request.json()) as Body;
  } catch {
    return NextResponse.json({ status: "error", message: "Invalid JSON body." }, { status: 400 });
  }

  const queueId = body.queue_id;
  if (typeof queueId !== "string" || !queueId.trim()) {
    return NextResponse.json({ status: "error", message: "queue_id is required." }, { status: 400 });
  }

  const patch: FoundryQueueItemPatch = {};

  if (body.operator_approval_state !== undefined) {
    if (typeof body.operator_approval_state !== "string" || !APPROVAL.includes(body.operator_approval_state as FoundryQueueOperatorApproval)) {
      return NextResponse.json({ status: "error", message: "Invalid operator_approval_state." }, { status: 400 });
    }
    patch.operator_approval_state = body.operator_approval_state as FoundryQueueOperatorApproval;
  }
  if (body.approval_notes !== undefined) {
    if (typeof body.approval_notes !== "string") {
      return NextResponse.json({ status: "error", message: "approval_notes must be a string." }, { status: 400 });
    }
    patch.approval_notes = body.approval_notes;
  }
  if (body.status !== undefined) {
    if (typeof body.status !== "string" || !STATUSES.includes(body.status as FoundryQueueStatus)) {
      return NextResponse.json({ status: "error", message: "Invalid status." }, { status: 400 });
    }
    patch.status = body.status as FoundryQueueStatus;
  }
  if (body.blockers !== undefined) {
    if (!Array.isArray(body.blockers) || body.blockers.some((b) => typeof b !== "string")) {
      return NextResponse.json({ status: "error", message: "blockers must be an array of strings." }, { status: 400 });
    }
    patch.blockers = body.blockers as string[];
  }
  if (body.next_action !== undefined) {
    if (typeof body.next_action !== "string") {
      return NextResponse.json({ status: "error", message: "next_action must be a string." }, { status: 400 });
    }
    patch.next_action = body.next_action;
  }

  if (Object.keys(patch).length === 0) {
    return NextResponse.json({ status: "error", message: "No valid fields to update." }, { status: 400 });
  }

  try {
    const { item } = await updateFoundryQueueItem(queueId.trim(), patch);
    return NextResponse.json({ status: "success", item }, { status: 200 });
  } catch (error) {
    const message = error instanceof Error ? error.message : "Update failed.";
    return NextResponse.json({ status: "error", message }, { status: 500 });
  }
}
