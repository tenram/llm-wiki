# Codebase Memory and Code Graphs

> Sources: DeusData, 2026-08-24; Colby McHenry (CodeGraph), 2026-08-24; ArcadeDB; Neo4j
> Raw: [Codebase Memory and Code Graphs](../../raw/agent-memory-systems/codebase-memory-and-code-graphs.md); [codebase-memory-mcp](../../raw/agent-memory-systems/2026-08-24-codebase-memory-mcp.md); [CodeGraph](../../raw/agent-memory-systems/2026-08-24-codegraph.md)

## Overview

This cluster covers code-aware memory systems that turn repositories into persistent, queryable structure.

## Pattern

The shared pattern is simple: extract symbols, links, and dependencies once, then query the resulting graph instead of rereading raw source on every question. `codebase-memory-mcp` and `codegraph` are both local-first MCP servers implementing it; ArcadeDB and Neo4j supply graph-backed storage choices for the same relationship model.

## codebase-memory-mcp

Pure-C native executable; tree-sitter parsing across 158 languages plus Hybrid LSP type resolution for 13 major languages. Builds a persistent knowledge graph (functions, classes, call chains, HTTP routes, cross-service links) queryable via 15 MCP tools including a read-only openCypher subset, blast-radius mapping (`detect_changes`), dead-code detection, and ADR management. Bundled Nomic embeddings power semantic search with no API key. Benchmarks: Linux kernel indexed in 3 minutes; ~99% token reduction vs grep exploration (arXiv:2603.27277). Distinguishing features: a per-account coordination daemon sharing watchers/indexing across agent clients, a built-in 3D graph UI on localhost:9749, cross-repo `CROSS_*` edges, and a team-shareable zstd-compressed graph artifact (`.codebase-memory/graph.db.zst`). Installs Scout/Verify/Auditor three-tier agent profiles across 43 client surfaces.

## CodeGraph

Rust-kernel MCP server (npm `@colbymchenry/codegraph`) with a deliberately minimal surface: one default tool, `codegraph_explore`, returning verbatim source + call paths + blast radius in a single call ("one strong tool steers agents better than a menu of narrower ones"). 20 languages parse natively in Rust with byte-for-byte identical fallback graphs; 34+ total via the portable engine. Framework-aware route extraction across 17 web frameworks and heuristic bridges for iOS/React Native/Expo cross-language flows (edges tagged with provenance). Auto-sync via native file watchers with staleness banners and connect-time catch-up. Benchmarked at 88% fewer tool calls and 44% lower cost vs file-by-file agents — but leaves ~80% more retrieval context resident in the window, a real trade-off for long sessions in small contexts.

## Comparison notes

Both tools are 100% local, SQLite-backed, zero-API-key, and target the same agent-integration surface (Claude Code, Codex, OpenCode, Cursor, Gemini, Antigravity, etc.). codebase-memory-mcp differentiates on breadth (158 grammars, Cypher queries, cross-repo edges, team artifacts, daemon coordination); CodeGraph differentiates on surgical single-call ergonomics, framework/iOS bridging, and honest measurement of residual-context cost. They overlap heavily; choosing is a workflow preference more than a capability gap.

## See Also

- [HybridRAG System](hybridrag-system.md)
- [Open Brain (OB1)](ob1.md)
