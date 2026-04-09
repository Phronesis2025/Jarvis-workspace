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
        <header className="sticky top-0 z-40 border-b border-slate-800 bg-[#0a0e17]/95 backdrop-blur">
          <div className="mx-auto max-w-7xl px-4 py-3 sm:px-6">
            <div className="flex flex-col gap-3">
              <h1 className="text-lg font-semibold tracking-tight text-white">
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
