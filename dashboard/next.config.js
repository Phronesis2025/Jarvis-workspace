/** @type {import('next').NextConfig} */
/**
 * Dashboard server code reads workspace files via `join(process.cwd(), "..", ...)`.
 * File tracing (NFT) follows those paths and was pulling `.git`, `logs`, webpack
 * cache, pathfinder, repo_intake, and large docs trees into serverless bundles.
 *
 * `outputFileTracingIgnores` is wired into the webpack NFT ignore callback
 * (`TraceEntryPointsPlugin`). Next also merges this array into
 * `experimental.outputFileTracingExcludes` for the post-trace step. Globs use
 * double-star segments so they match traced paths under the dashboard root.
 */
const outputFileTracingIgnores = [
  "**/.git/**",
  "**/logs/**",
  "**/.next/cache/**",
  "**/future_modules/pathfinder/**",
  "**/future_modules/repo_intake/**",
  "**/future_modules/research_swarm/docs/**",
  "**/future_modules/research_swarm/scripts/**",
  "**/future_modules/research_swarm/examples/**",
  "**/future_modules/research_swarm/schemas/**",
  "**/future_modules/research_swarm/ops/**",
  "**/future_modules/research_swarm/scratch/**",
  "**/future_modules/research_swarm/outputs/**/*.md",
  "**/future_modules/stock_module/research/**",
  "**/future_modules/stock_module/*.md",
  "**/future_modules/the_fade/docs/**",
  // Repo-root handoff bundles (not read by dashboard data loaders)
  "../*.md",
  "../*.txt",
];

const nextConfig = {
  experimental: {
    outputFileTracingIgnores,
  },
};

module.exports = nextConfig;
