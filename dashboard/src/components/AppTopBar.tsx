"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

const routeTitles = [
  { href: "/foundry-implementation-queue", label: "Foundry Implementation Queue" },
  { href: "/foundry-registry-review", label: "Foundry Registry Review" },
  { href: "/foundry-article-intake", label: "Foundry Article Intake" },
  { href: "/foundry-github-intake", label: "Foundry GitHub Intake" },
  { href: "/foundry-x-post-intake", label: "Foundry X Post Intake" },
  { href: "/research-swarm", label: "Research Swarm" },
  { href: "/stock-intake", label: "Stock Intake" },
  { href: "/stock-briefs", label: "Stock Briefs" },
  { href: "/checklists", label: "Checklists" },
  { href: "/pathfinder", label: "Pathfinder" },
  { href: "/tasks", label: "Task Board" },
  { href: "/runs", label: "Recent Runs" },
  { href: "/", label: "Overview" },
] as const;

function getRouteLabel(pathname: string): string {
  const match = routeTitles.find(({ href }) =>
    href === "/" ? pathname === "/" : pathname.startsWith(href)
  );

  return match?.label ?? "Jarvis Dashboard";
}

export function AppTopBar() {
  const pathname = usePathname();
  const currentLabel = getRouteLabel(pathname);
  const inFoundry = pathname.startsWith("/foundry-");

  return (
    <header className="sticky top-0 z-30 border-b border-border bg-card backdrop-blur-sm">
      <div className="mx-auto flex max-w-7xl flex-col gap-4 px-4 py-4 sm:px-6 lg:px-8">
        <div className="flex flex-col gap-3 md:flex-row md:items-center md:justify-between">
          <div className="min-w-0">
            <div className="text-[11px] uppercase tracking-[0.24em] text-muted-foreground">
              Jarvis Dashboard
            </div>
            <div className="mt-1 flex flex-wrap items-center gap-3">
              <h1 className="truncate text-xl font-semibold tracking-tight text-foreground">
                {currentLabel}
              </h1>
              <span className="inline-flex items-center rounded-full border border-primary/20 bg-primary/15 px-2.5 py-1 text-xs font-medium text-primary">
                {inFoundry ? "Foundry Surface" : "Primary Route"}
              </span>
            </div>
          </div>

          <div className="flex flex-wrap items-center gap-3">
            <label className="min-w-[220px] flex-1 md:flex-none">
              <span className="sr-only">Search routes</span>
              <input
                type="search"
                readOnly
                value=""
                placeholder="Search shell surfaces"
                className="w-full rounded-lg border border-border bg-muted px-3 py-2 text-sm text-muted-foreground outline-none transition-colors placeholder:text-muted-foreground focus:border-border"
              />
            </label>

            <div className="inline-flex items-center gap-2 rounded-lg border border-border bg-muted px-3 py-2 text-sm text-muted-foreground">
              <span className="h-2 w-2 rounded-full bg-success" aria-hidden="true" />
              <span>Routes preserved</span>
            </div>

            <Link
              href="/foundry-article-intake"
              className="inline-flex items-center justify-center rounded-lg border border-primary/20 bg-card px-4 py-2 text-sm font-medium text-primary transition-colors hover:bg-muted"
            >
              Foundry Intake
            </Link>
          </div>
        </div>
      </div>
    </header>
  );
}
