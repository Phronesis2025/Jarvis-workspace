/** Instrument-panel style metric card for HUD dashboard */
export function HudMetricCard({
  label,
  value,
  variant = "default",
}: {
  label: string;
  value: React.ReactNode;
  variant?: "default" | "healthy" | "warning";
}) {
  const valueColor =
    variant === "healthy"
      ? "text-teal-400"
      : variant === "warning"
        ? "text-amber-400"
        : "text-cyan-200";

  return (
    <div className="hud-metric p-3">
      <div className="text-xs uppercase tracking-wider text-slate-500">
        {label}
      </div>
      <div className={`mt-1 text-xl font-semibold sm:text-2xl ${valueColor}`}>
        {value}
      </div>
    </div>
  );
}
