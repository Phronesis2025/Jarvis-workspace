"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useEffect, useRef, useState } from "react";

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
  const foundryActive = foundryItems.some(({ href }) => pathname.startsWith(href));
  const [open, setOpen] = useState(false);
  const dropdownRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    function onPointerDown(event: MouseEvent) {
      const target = event.target as Node;
      if (dropdownRef.current && !dropdownRef.current.contains(target)) {
        setOpen(false);
      }
    }
    function onEscape(event: KeyboardEvent) {
      if (event.key === "Escape") setOpen(false);
    }
    document.addEventListener("mousedown", onPointerDown);
    document.addEventListener("keydown", onEscape);
    return () => {
      document.removeEventListener("mousedown", onPointerDown);
      document.removeEventListener("keydown", onEscape);
    };
  }, []);

  return (
    <nav className="w-full">
      <div className="flex w-full flex-wrap items-center gap-2">
        <div className="flex flex-wrap items-center gap-2">
        {navItems.map(({ href, label }) => {
          const isActive =
            href === "/"
              ? pathname === "/"
              : pathname.startsWith(href);
          return (
            <Link
              key={href}
              href={href}
              className={`whitespace-nowrap rounded-full px-3 py-2 text-sm font-medium transition-colors ${
                isActive
                  ? "bg-cyan-600 text-white shadow-sm"
                  : "text-slate-300 hover:bg-slate-800/70 hover:text-white"
              }`}
              aria-current={isActive ? "page" : undefined}
            >
              {label}
            </Link>
          );
        })}

        <div className="relative shrink-0" ref={dropdownRef}>
          <button
            type="button"
            aria-haspopup="menu"
            aria-expanded={open}
            onClick={() => setOpen((v) => !v)}
            className={`inline-flex items-center gap-1 whitespace-nowrap rounded-full px-3 py-2 text-sm font-medium transition-colors ${
              foundryActive
                ? "bg-cyan-600 text-white shadow-sm"
                : "text-slate-300 hover:bg-slate-800/70 hover:text-white"
            }`}
          >
            Foundry
            <span className={`text-xs transition-transform ${open ? "rotate-180" : ""}`}>▼</span>
          </button>
          {open ? (
            <div
              role="menu"
              className="absolute right-0 z-50 mt-2 min-w-[220px] rounded-xl border border-slate-700 bg-[#0f172a] p-1 shadow-lg"
            >
            {foundryItems.map(({ href, label }) => {
              const isActive = pathname.startsWith(href);
              return (
                <Link
                  key={href}
                  href={href}
                  role="menuitem"
                  onClick={() => setOpen(false)}
                  className={`block rounded px-3 py-2 text-sm transition-colors ${
                    isActive
                      ? "bg-cyan-600 text-white"
                      : "text-slate-300 hover:bg-slate-800/70 hover:text-white"
                  }`}
                >
                  {label}
                </Link>
              );
            })}
            </div>
          ) : null}
        </div>
        </div>
        <Link
          href="/foundry-article-intake"
          className="ml-auto shrink-0 rounded-full bg-cyan-600 px-4 py-2 text-sm font-semibold text-white shadow-sm hover:bg-cyan-500"
        >
          Request Intake
        </Link>
      </div>
    </nav>
  );
}
