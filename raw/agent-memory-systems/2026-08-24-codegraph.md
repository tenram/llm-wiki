# CodeGraph

> Source: https://github.com/colbymchenry/codegraph
> Collected: 2026-08-24
> Published: Unknown

CodeGraph supercharges Claude Code, Cursor, Codex, OpenCode, Hermes Agent, Gemini, Antigravity, Kiro, and GitHub Copilot with semantic code intelligence. "The fastest complete code graph · surgical context · built for how agents actually work · 100% local." Parsing kernel written in Rust. MIT licensed, npm-distributed (@colbymchenry/codegraph), self-contained bundled Node runtime.

## Get started

1. Install CLI: `curl -fsSL .../install.sh | sh` or `npm i -g @colbymchenry/codegraph`.
2. `codegraph install` — detects and auto-configures agents' MCP configs plus marker-fenced instruction sections (CLAUDE.md / AGENTS.md / GEMINI.md) so subagents learn the CLI equivalent.
3. `codegraph init` per project — creates `.codegraph/` and builds the graph.
4. Auto-sync enabled by default: native OS file watchers (FSEvents/inotify/ReadDirectoryChangesW), debounced (~2s), incremental sync. Per-file staleness banners warn agents during the debounce window; connect-time catch-up reconciles edits made while no MCP server ran.

## Why CodeGraph

Agents discover structure the slow way (grep/glob/read). CodeGraph hands the agent exact code in one call: a pre-built knowledge graph of every symbol, call edge, and dependency, including dynamic-dispatch hops grep cannot follow.

Benchmark (2026-08 re-measurement, Claude Opus 4.8, median of 4 runs per arm, CLI blocked in both arms to avoid contamination): universal win across 7 repos — 88% fewer tool calls, 53% faster, 62% fewer tokens, 44% cheaper, file reads cut to zero. Examples: VS Code 2 vs 28 tool calls (2.2× faster); Excalidraw 2 vs 43 (3.6× faster).

Context caveat: CodeGraph responses leave ~80% more retrieval context resident at session end than file-reading agents (one dense verbatim payload stays in window vs many evicted small results). Fewer tokens processed AND larger persistent footprint are both real.

## Rust kernel

20 languages parse in compiled code with one boundary crossing per file (TypeScript, JavaScript, Java, Python, Go, C, C++, Rust, C#, Ruby, PHP, Swift, Kotlin, Scala, Dart, R, Lua, Luau; Metal/CUDA ride the C++ path). Graphs verified byte-for-byte identical to the reference engine; per-file fallback keeps identical graphs when prebuilt binaries or valid syntax are unavailable.

Self-sizing: worker pools and caches sized from real core counts (container/cgroup-aware) and measured RAM. Swift compiler repo (27k files) fresh-indexes in ~100s; one-file edit re-syncs in ~4s; watcher fires 300ms after a save. On a 2-core/6GB VPS the Linux kernel indexes to completion in under 12 minutes where RAM-first designs OOM.

## Features

- Single MCP tool by default: `codegraph_explore` — one call returns relevant symbols' verbatim source grouped by file, call paths between them, blast-radius summary. Other tools (node/search/callers/callees/impact/files/status) stay functional but unlisted; re-enable via CODEGRAPH_MCP_TOOLS. Rationale: one strong tool steers agents better than a menu of narrower ones.
- Framework-aware routes: URL patterns linked to handlers across 17 frameworks (Django, Flask, FastAPI, Express, NestJS, Laravel, Drupal, Rails, Spring, Play, Gin/chi, Axum/actix/Rocket, ASP.NET, Vapor, React Router/SvelteKit, Vue Router/Nuxt, Astro).
- Mixed iOS / React Native / Expo bridging: Swift ↔ ObjC auto-bridging, RN legacy bridge + TurboModules + Fabric view components, native→JS event emitters, Expo Modules. Bridge edges tagged provenance:'heuristic' with stable synthesizedBy channel names.
- 34+ languages total including ArkTS, Svelte, Vue, Astro, Liquid, Delphi, Lua, R, Luau, CFML, COBOL, VB.NET, Erlang, Solidity, Terraform/OpenTofu, Nix.
- Storage: local SQLite (`.codegraph/codegraph.db`) with FTS5 full-text search. 100% local, no API keys.
- Library usage: embeddable CodeGraph class (needs Node 22.5+ for node:sqlite); CLI/MCP run on bundled runtime.
- Configuration: zero-config default; optional `codegraph.json` for custom extensions, exclude/include/deprioritize path lists.
- Telemetry: anonymous usage stats only, opt-out via `codegraph telemetry off`.

## CLI reference (selected)

install, uninstall (--keep-cli), init/uninit, index, sync, status, query, explore, node, files, callers, callees, impact, affected (traces import deps to find affected test files; CI-hook friendly), daemon, telemetry, upgrade.
