import type { Metadata } from "next";
import "./globals.css";
import { NavBar } from "@/components/NavBar";

export const metadata: Metadata = {
  title: "Jarvis Dashboard",
  description: "Read-only dashboard for Jarvis system progress and workflow",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-[#0a0e17] text-slate-200 antialiased">
        <header className="border-b border-cyan-500/20 bg-[#0a0e17] shadow-[0_0_24px_rgba(34,211,238,0.06)]">
          <div className="mx-auto max-w-7xl px-4 py-3 sm:px-6">
            <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
              <h1 className="text-lg font-semibold tracking-tight text-cyan-100">
                Jarvis Dashboard
              </h1>
              <NavBar />
            </div>
          </div>
        </header>
        <main className="mx-auto max-w-7xl px-4 py-6 sm:px-6">{children}</main>
      </body>
    </html>
  );
}
