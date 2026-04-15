"use client";

/** Central HUD-style system status anchor. Uses real metrics only. */
export function SystemPulse({
  overallStatus,
  tasksCompletedToday,
  workSessionsToday,
  lastUpdateText,
  lastUpdateStale,
  lastUpdateUnavailable,
}: {
  overallStatus: string;
  tasksCompletedToday: number;
  workSessionsToday: number;
  lastUpdateText: string;
  lastUpdateStale?: boolean;
  lastUpdateUnavailable?: boolean;
}) {
  const isHealthy = overallStatus === "Operational";
  const accentColor = lastUpdateUnavailable
    ? "text-muted-foreground"
    : lastUpdateStale
      ? "text-warning"
      : "text-primary";
  const statusColor = isHealthy ? "text-success" : "text-warning";

  return (
    <div className="hud-panel relative overflow-hidden p-6">
      <div className="relative flex flex-col items-center gap-4 sm:flex-row sm:justify-around sm:gap-6">
        <div className="flex flex-col items-center">
          <div className="text-xs uppercase tracking-widest text-muted-foreground">
            System status
          </div>
          <div
            className={`mt-1 text-2xl font-bold tracking-tight sm:text-3xl ${statusColor}`}
          >
            {overallStatus}
          </div>
          <div
            className={`mt-1 h-1 w-16 rounded-full ${
              isHealthy ? "bg-success/70" : "bg-warning/70"
            }`}
          />
        </div>

        <div className="flex flex-wrap justify-center gap-6 sm:gap-10">
          <div className="flex flex-col items-center">
            <div className="text-xs text-muted-foreground">Tasks completed</div>
            <div className="text-xl font-semibold text-foreground sm:text-2xl">
              {tasksCompletedToday}
            </div>
          </div>
          <div className="flex flex-col items-center">
            <div className="text-xs text-muted-foreground">Work sessions</div>
            <div className="text-xl font-semibold text-foreground sm:text-2xl">
              {workSessionsToday}
            </div>
          </div>
          <div className="flex flex-col items-center">
            <div className="text-xs text-muted-foreground">Last sync</div>
            <div className={`text-xl font-semibold sm:text-2xl ${accentColor}`}>
              {lastUpdateText}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
