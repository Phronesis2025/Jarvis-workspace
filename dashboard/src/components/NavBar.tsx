"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useMemo, useState } from "react";

const navItems = [
  { href: "/", label: "Overview" },
  { href: "/tasks", label: "Task Board" },
  { href: "/runs", label: "Recent Runs" },
  { href: "/pathfinder", label: "Pathfinder" },
  { href: "/research-swarm", label: "Research Swarm" },
  { href: "/stock-intake", label: "Stock Intake" },
  { href: "/stock-briefs", label: "Stock Briefs" },
  { href: "/checklists", label: "Checklists" },
] as const;

const foundryItems = [
  { href: "/foundry-registry-review", label: "Registry Review" },
  { href: "/foundry-article-intake", label: "Article Intake" },
  { href: "/foundry-github-intake", label: "GitHub Intake" },
  { href: "/foundry-x-post-intake", label: "X Post Intake" },
  { href: "/foundry-implementation-queue", label: "Implementation Queue" },
] as const;

export function NavBar() {
  const pathname = usePathname();
  const [foundryOpen, setFoundryOpen] = useState(true);
  const foundryActive = useMemo(
    () => foundryItems.some(({ href }) => pathname.startsWith(href)),
    [pathname]
  );

  function isActive(href: string): boolean {
    return href === "/" ? pathname === "/" : pathname.startsWith(href);
  }

  return (
    <nav className="flex h-full flex-col">
      <div className="border-b border-border px-4 py-4">
        <div className="flex items-center gap-3">
          <div className="flex h-10 w-10 items-center justify-center rounded-lg border border-border bg-card text-sm font-semibold text-foreground">
            J
          </div>
          <div>
            <div className="text-sm font-semibold tracking-[0.18em] text-foreground">
              JARVIS
            </div>
            <div className="mt-1 text-xs uppercase tracking-[0.24em] text-muted-foreground">
              Operator Console
            </div>
          </div>
        </div>
      </div>

      <div className="flex-1 space-y-5 overflow-y-auto px-3 py-4">
        <section className="space-y-2">
          <div className="px-3 text-[11px] font-medium uppercase tracking-[0.22em] text-muted-foreground">
            Primary Views
          </div>
          <div className="space-y-1">
            {navItems.map(({ href, label }) => {
              const active = isActive(href);
              return (
                <Link
                  key={href}
                  href={href}
                  className={`shell-nav-link ${active ? "shell-nav-link-active" : ""}`}
                  aria-current={active ? "page" : undefined}
                >
                  <span className="shell-nav-dot" aria-hidden="true" />
                  <span className="truncate">{label}</span>
                </Link>
              );
            })}
          </div>
        </section>

        <section className="space-y-2">
          <button
            type="button"
            onClick={() => setFoundryOpen((value) => !value)}
            className={`flex w-full items-center justify-between rounded-lg px-3 py-2 text-left text-[11px] font-medium uppercase tracking-[0.22em] transition-colors ${
              foundryActive
                ? "bg-sidebar-accent text-sidebar-accent-foreground"
                : "text-muted-foreground hover:bg-sidebar-accent hover:text-sidebar-accent-foreground"
            }`}
            aria-expanded={foundryOpen}
          >
            <span>Foundry</span>
            <span className={`text-sm transition-transform ${foundryOpen ? "rotate-180" : ""}`}>
              ^
            </span>
          </button>

          {foundryOpen ? (
            <div className="space-y-1">
              {foundryItems.map(({ href, label }) => {
                const active = isActive(href);
                return (
                  <Link
                    key={href}
                    href={href}
                    className={`shell-nav-link shell-nav-link-subtle ${active ? "shell-nav-link-active" : ""}`}
                    aria-current={active ? "page" : undefined}
                  >
                    <span className="shell-nav-dot" aria-hidden="true" />
                    <span className="truncate">{label}</span>
                  </Link>
                );
              })}
            </div>
          ) : null}
        </section>
      </div>

      <div className="border-t border-border p-3">
        <div className="rounded-lg border border-border bg-card p-3">
          <div className="text-[11px] uppercase tracking-[0.22em] text-muted-foreground">
            Quick Access
          </div>
          <p className="mt-2 text-sm text-muted-foreground">
            Foundry intake remains available without changing any route behavior.
          </p>
          <Link
            href="/foundry-article-intake"
            className="mt-3 inline-flex w-full items-center justify-center rounded-lg border border-primary/20 bg-primary/15 px-4 py-2.5 text-sm font-semibold text-primary transition-colors hover:bg-primary/20"
          >
            Request Intake
          </Link>
        </div>
      </div>
    </nav>
  );
}
