import { FoundryLaneIntakeClient } from "@/components/FoundryLaneIntakeClient";
import { getTopIdeasForLane } from "@/lib/foundry-intake";

export const dynamic = "force-dynamic";
export const fetchCache = "force-no-store";

export default async function FoundryGithubIntakePage() {
  const topIdeas = await getTopIdeasForLane("github");
  return (
    <FoundryLaneIntakeClient
      lane="github"
      pageTitle="GitHub Intake"
      inputLabel="GitHub repository URL"
      inputPlaceholder="https://github.com/owner/repo"
      inputType="url"
      initialTopIdeas={topIdeas}
    />
  );
}
