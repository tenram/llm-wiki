# codebase-memory-mcp

> Source: https://github.com/DeusData/codebase-memory-mcp
> Collected: 2026-08-24
> Published: Unknown (arXiv preprint 2603.27277)

"The fastest and most efficient code intelligence engine for AI coding agents." Full-indexes an average repository in milliseconds; Linux kernel (28M LOC, 75K files) in 3 minutes; structural queries under 1ms. Ships as a native executable (pure C, no language runtime) for macOS/Linux/Windows. MIT licensed.

## Core design

- Parsing via tree-sitter AST analysis across 158 languages (vendored grammars compiled into the binary), enhanced with Hybrid LSP semantic type resolution for Python, TS/JS/JSX/TSX, PHP, C#, Go, C, C++, Java, Kotlin, Rust, Perl — producing a persistent knowledge graph of functions, classes, call chains, HTTP routes, cross-service links.
- 15 MCP tools; no LLM inside — the connected MCP client is the intelligence/query-translator layer.
- Research: arXiv:2603.27277 "Codebase-Memory: Tree-Sitter-Based Knowledge Graphs for LLM Code Exploration via MCP" — across 31 repos: 83% answer quality, 10× fewer tokens, 2.1× fewer tool calls vs file-by-file exploration.
- RAM-first pipeline: LZ4 compression, in-memory SQLite, single dump at end; memory released after indexing.
- 100% local, no telemetry, no API keys.

## Features

- Graph & analysis: get_architecture (languages/packages/routes/hotspots/boundaries/layers/clusters), manage_adr (Architecture Decision Records), Louvain community detection, detect_changes (git diff → blast radius with risk classification), dead code detection, Cypher-like queries (read-only openCypher subset).
- Search: semantic_query (bundled Nomic nomic-embed-code embeddings compiled into binary; 11-signal scoring), BM25 via SQLite FTS5 with camelCase-aware tokenizer, structural search_graph, graph-augmented search_code.
- Cross-service linking: HTTP route↔call-site matching, gRPC/GraphQL/tRPC detection, channel detection (EMITS/LISTENS_ON) for Socket.IO/EventEmitter/pub-sub.
- Cross-repo intelligence: CROSS_* edges link nodes across repos indexed under one store; multi-galaxy 3D UI layout.
- Edge types include CALLS, CALL_REFERENCE, USAGE, IMPORTS, DEFINES, IMPLEMENTS, INHERITS, HTTP_CALLS, ASYNC_CALLS, EMITS, LISTENS_ON, DATA_FLOWS (arg-to-param mapping), SIMILAR_TO (MinHash+LSH near-clone), SEMANTICALLY_RELATED.
- Infrastructure-as-code indexing: Dockerfiles, Kubernetes manifests, Kustomize overlays as graph nodes.
- Built-in 3D graph visualization UI at localhost:9749, owned by a shared per-account coordination daemon that also coordinates watchers/indexing across Claude Code, Codex, OpenCode, and other clients (exact-build admission barriers).
- Team-shared artifact: commit `.codebase-memory/graph.db.zst` (zstd-compressed SQLite snapshot) so teammates bootstrap without full reindex; merge=ours gitattributes auto-created.
- Session coordination hooks: fail-open context-only hooks (PreToolUse on Grep/Glob injects matching graph symbols; post-Read coverage context). Installs Scout/Verify/Auditor three-tier agent profiles across 43 client surfaces.

## Performance (Apple M3 Pro)

Linux kernel full index 3 min (4.81M nodes, 7.72M edges); Django ~6s; Cypher query <1ms; name search <10ms; dead code ~150ms; trace depth-5 <10ms. Token efficiency: five structural queries ~3,400 tokens vs ~412,000 via grep exploration (99.2% reduction).

## Install

One-line curl installer or package managers (npm, PyPI, Homebrew, Scoop, Winget, Chocolatey, AUR, go install). `install` auto-detects installed coding agents and configures MCP entries plus durable instructions/skills/hooks. Updates run from the install script (idempotent re-run); binary never phones home.
