import { FoundryLaneIntakeClient } from "@/components/FoundryLaneIntakeClient";
import { getTopIdeasForLane } from "@/lib/foundry-intake";

export const dynamic = "force-dynamic";
export const fetchCache = "force-no-store";

export default async function FoundryArticleIntakePage() {
  const topIdeas = await getTopIdeasForLane("article");
  return (
    <FoundryLaneIntakeClient
      lane="article"
      pageTitle="Article Intake"
      inputLabel="Article text"
      inputPlaceholder="Paste article text for bounded local intake..."
      inputType="textarea"
      initialTopIdeas={topIdeas}
    />
  );
}
