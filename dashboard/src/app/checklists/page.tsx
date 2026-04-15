import { getModuleChecklists } from "@/lib/data";
import type {
  ModuleChecklist,
  ModuleChecklistPhase,
  ModuleChecklistItem,
  ChecklistItemStatus,
} from "@/lib/types";

export const dynamic = "force-dynamic";

function statusColor(s: ChecklistItemStatus): string {
  switch (s) {
    case "done":
      return "text-success";
    case "in_progress":
      return "text-primary";
    case "not_started":
      return "text-muted-foreground";
    case "blocked":
      return "text-warning";
    case "deferred":
      return "text-muted-foreground italic";
    default:
      return "text-muted-foreground";
  }
}

function statusBadge(s: ChecklistItemStatus): string {
  switch (s) {
    case "done":
      return "border-success/20 bg-success/15 text-success";
    case "in_progress":
      return "border-primary/20 bg-primary/15 text-primary";
    case "not_started":
      return "border-border bg-muted text-muted-foreground";
    case "blocked":
      return "border-warning/20 bg-warning/15 text-warning";
    case "deferred":
      return "border-border bg-muted text-muted-foreground";
    default:
      return "border-border bg-muted text-muted-foreground";
  }
}

function ChecklistItemRow({ item }: { item: ModuleChecklistItem }) {
  return (
    <div className="flex items-start gap-3 py-1.5">
      <span
        className={`mt-1.5 h-2 w-2 shrink-0 rounded-full ${
          item.status === "done"
              ? "bg-success"
            : item.status === "in_progress" || item.status === "blocked"
                ? "bg-warning"
                : "bg-muted-foreground"
        }`}
      />
      <div className="min-w-0 flex-1">
        <span className={`text-sm ${statusColor(item.status)}`}>
          {item.label}
        </span>
        {item.notes && (
          <p className="mt-0.5 text-xs text-muted-foreground">{item.notes}</p>
        )}
      </div>
      <span
        className={`shrink-0 rounded border px-2 py-0.5 text-xs font-medium ${statusBadge(item.status)}`}
      >
        {item.status.replace("_", " ")}
      </span>
    </div>
  );
}

function PhaseBlock({
  phase,
  isCurrentPhase,
}: {
  phase: ModuleChecklistPhase;
  isCurrentPhase: boolean;
}) {
  const doneCount = phase.items.filter((i) => i.status === "done").length;
  const remaining =
    phase.items.length -
    phase.items.filter((i) => i.status === "done").length;

  return (
    <div
      className={`hud-panel p-4 ${isCurrentPhase ? "ring-1 ring-primary/20" : ""}`}
    >
      <div className="mb-2 flex flex-wrap items-center justify-between gap-2">
        <div>
          <h4 className="text-sm font-medium text-foreground">
            {phase.phase_name}
            {isCurrentPhase && (
              <span className="ml-2 text-xs text-primary">
                (current phase)
              </span>
            )}
          </h4>
          <p className="mt-0.5 text-xs text-muted-foreground">{phase.goal}</p>
        </div>
        <div className="flex items-center gap-2">
          <span
            className={`rounded border px-2 py-0.5 text-xs ${statusBadge(phase.status)}`}
          >
            {phase.status.replace("_", " ")}
          </span>
          <span className="text-xs text-muted-foreground">
            {doneCount}/{phase.items.length}
          </span>
        </div>
      </div>
      <div className="space-y-0 divide-y divide-border">
        {phase.items.map((item) => (
          <ChecklistItemRow key={item.id} item={item} />
        ))}
      </div>
      {remaining > 0 && (
        <p className="mt-2 text-xs text-muted-foreground">
          {remaining} item{remaining === 1 ? "" : "s"} remaining
        </p>
      )}
    </div>
  );
}

function ModuleSection({ module: m }: { module: ModuleChecklist }) {
  const totalItems = m.phases.reduce((sum, p) => sum + p.items.length, 0);
  const doneItems = m.phases.reduce(
    (sum, p) => sum + p.items.filter((i) => i.status === "done").length,
    0
  );
  const remainingItems = totalItems - doneItems;
  const currentPhase = m.phases.find((p) => p.phase_id === m.current_phase);

  return (
    <section className="space-y-4">
      <div className="hud-panel p-4">
        <div className="mb-3 flex flex-wrap items-start justify-between gap-3">
          <div>
            <h2 className="text-lg font-semibold text-foreground">
              {m.module_name}
            </h2>
            <p className="mt-1 text-sm text-muted-foreground">{m.purpose}</p>
          </div>
          <span
            className={`shrink-0 rounded border px-3 py-1.5 text-sm font-medium ${statusBadge(m.status)}`}
          >
            {m.status.replace("_", " ")}
          </span>
        </div>

        <div className="mb-4 grid grid-cols-1 gap-3 sm:grid-cols-2">
          <div className="rounded-lg border border-border bg-muted p-3">
            <div className="text-xs uppercase tracking-wider text-muted-foreground">
              Current phase
            </div>
            <div className="mt-1 text-sm font-medium text-foreground">
              {currentPhase?.phase_name ?? m.current_phase}
            </div>
          </div>
          <div className="rounded-lg border border-border bg-muted p-3">
            <div className="text-xs uppercase tracking-wider text-muted-foreground">
              Current step
            </div>
            <div className="mt-1 text-sm font-medium text-foreground">
              {m.current_step.replace(/_/g, " ")}
            </div>
          </div>
        </div>

        <div className="mb-4 rounded-lg border border-border bg-muted p-3">
          <div className="text-xs uppercase tracking-wider text-muted-foreground">
            Final version
          </div>
          <p className="mt-1 text-sm text-foreground">
            {m.final_version_definition}
          </p>
        </div>

        <div className="mb-2 flex items-center gap-2 text-sm">
          <span className="text-success">{doneItems} done</span>
          <span className="text-muted-foreground">•</span>
          <span className="text-warning">{remainingItems} remaining</span>
          <span className="text-muted-foreground">•</span>
          <span className="text-muted-foreground">{totalItems} total</span>
        </div>
      </div>

      <div className="space-y-4">
        {m.phases.map((phase) => (
          <PhaseBlock
            key={phase.phase_id}
            phase={phase}
            isCurrentPhase={phase.phase_id === m.current_phase}
          />
        ))}
      </div>
    </section>
  );
}

export default async function ChecklistsPage() {
  const data = await getModuleChecklists();

  return (
    <div className="space-y-8">
      <div>
        <h1 className="text-2xl font-semibold tracking-tight text-foreground">
          Module Checklists
        </h1>
        <p className="mt-1 text-sm text-muted-foreground">
          Build-path view for each module. Rendered from{" "}
          <code className="rounded bg-muted px-1.5 py-0.5 font-mono text-xs text-primary">
            state/module_checklists.json
          </code>
          .
        </p>
      </div>

      {!data ? (
        <div className="hud-panel p-6">
          <p className="text-warning">
            Checklist data unavailable. Run the dashboard locally with the
            Jarvis workspace so{" "}
            <code className="rounded bg-muted px-1 py-0.5 font-mono text-xs text-foreground">
              state/module_checklists.json
            </code>{" "}
            can be read.
          </p>
        </div>
      ) : (
        <>
          {data.generated_at && (
            <p className="text-xs text-muted-foreground">
              Generated: {new Date(data.generated_at).toISOString()}
            </p>
          )}
          <div className="space-y-10">
            {data.modules.map((m) => (
              <ModuleSection key={m.module_id} module={m} />
            ))}
          </div>
        </>
      )}
    </div>
  );
}
