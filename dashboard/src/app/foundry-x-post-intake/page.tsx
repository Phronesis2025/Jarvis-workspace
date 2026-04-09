import { FoundryLaneIntakeClient } from "@/components/FoundryLaneIntakeClient";
import { getTopIdeasForLane } from "@/lib/foundry-intake";

export const dynamic = "force-dynamic";
export const fetchCache = "force-no-store";

export default async function FoundryXPostIntakePage() {
  const topIdeas = await getTopIdeasForLane("x_post");
  return (
    <FoundryLaneIntakeClient
      lane="x_post"
      pageTitle="X Post Intake"
      inputLabel="X post / briefing text"
      inputPlaceholder="Paste X post or briefing text for bounded local intake..."
      inputType="textarea"
      initialTopIdeas={topIdeas}
    />
  );
}
