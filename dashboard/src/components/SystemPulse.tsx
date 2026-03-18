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
    ? "text-slate-400"
    : lastUpdateStale
      ? "text-amber-400"
      : "text-cyan-300";
  const statusColor = isHealthy ? "text-teal-400" : "text-amber-400";

  return (
    <div className="hud-panel hud-panel-glow relative overflow-hidden p-6">
      {/* Subtle radial gradient overlay */}
      <div
        className="pointer-events-none absolute inset-0 opacity-40"
        style={{
          background: "radial-gradient(ellipse 80% 80% at 50% 0%, rgba(34, 211, 238, 0.08) 0%, transparent 70%)",
        }}
      />
      <div className="relative flex flex-col items-center gap-4 sm:flex-row sm:justify-around sm:gap-6">
        {/* Central status */}
        <div className="flex flex-col items-center">
          <div className="text-xs uppercase tracking-widest text-cyan-400/80">
            System status
          </div>
          <div
            className={`mt-1 text-2xl font-bold tracking-tight sm:text-3xl ${statusColor}`}
          >
            {overallStatus}
          </div>
          <div
            className={`mt-1 h-1 w-16 rounded-full ${
              isHealthy ? "bg-teal-400/60" : "bg-amber-400/60"
            }`}
          />
        </div>

        {/* Supporting metrics */}
        <div className="flex flex-wrap justify-center gap-6 sm:gap-10">
          <div className="flex flex-col items-center">
            <div className="text-xs text-slate-500">Tasks completed</div>
            <div className="text-xl font-semibold text-cyan-200 sm:text-2xl">
              {tasksCompletedToday}
            </div>
          </div>
          <div className="flex flex-col items-center">
            <div className="text-xs text-slate-500">Work sessions</div>
            <div className="text-xl font-semibold text-cyan-200 sm:text-2xl">
              {workSessionsToday}
            </div>
          </div>
          <div className="flex flex-col items-center">
            <div className="text-xs text-slate-500">Last sync</div>
            <div className={`text-xl font-semibold sm:text-2xl ${accentColor}`}>
              {lastUpdateText}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
