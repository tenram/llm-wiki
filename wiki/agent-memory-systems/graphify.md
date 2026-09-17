# Graphify

> Sources: Graphify-Labs, Unknown date
> Raw: [Graphify](../../raw/agent-memory-systems/2026-09-17-graphify.md)

## Overview

A `/graphify` skill for Claude Code, Cursor, Codex, Gemini CLI, and 15+ coding assistants that maps an entire project — code, docs, PDFs, images, videos — into a queryable knowledge graph you can query instead of grepping through files. Code is parsed locally with tree-sitter (deterministic, no LLM); only the semantic pass over docs/media calls a model.

## Key design points

- **Not a vector index.** No embeddings, no vector store — a real graph you traverse. Three query verbs: `graphify query` (plain-language question → scoped subgraph), `graphify path A B` (how two things connect), `graphify explain X` (one concept).
- **Every edge is explained.** Each connection is tagged `EXTRACTED` (explicit in source) or `INFERRED` (resolved by graphify), so you know what was read vs. guessed.
- **Three outputs:** `graph.html` (clickable force-directed graph with Leiden communities), `GRAPH_REPORT.md` (god nodes, surprising connections, suggested questions), `graph.json` (the full graph, queryable without re-reading files).
- **Rationale as first-class nodes.** `# NOTE:` / `# WHY:` comments and ADR/RFC citations become nodes linked to the code they explain.

## Capabilities

Cross-file `calls`/`imports`/`inherits`/`mixes_in` edges across ~40 languages via tree-sitter AST; docs, PDFs, images, video/audio all map into the same graph; git hooks auto-rebuild on commit/branch switch (AST-only, no API cost); `graphify-out/` is committed so teams share one map; a merge driver keeps `graph.json` conflict-free.

## Benchmarks

On LOCOMO (n=300): recall@10 0.497 (vs mem0 0.048, supermemory 0.149), QA accuracy 45.3%. On LongMemEval-S: 76% QA accuracy, tied with dense RAG. Graph build costs zero LLM credits.

## MCP serving

`python -m graphify.serve graphify-out/graph.json` exposes `query_graph`, `get_node`, `get_neighbors`, `shortest_path`, `list_prs`, `get_pr_impact`, `triage_prs` over MCP — stdio for local use, or a shared HTTP transport so a whole team points at one URL.

## Comparison with codebase-memory systems

Graphify overlaps with codebase-memory-mcp and CodeGraph (graph-over-grep for agent code understanding) but targets a broader corpus — code plus docs, PDFs, images, and media in one graph — and ships as a skill/CLI rather than an MCP server. Its `EXTRACTED`/`INFERRED` edge confidence tags and cost-free local AST pass are the distinguishing features.

## See Also

- [Codebase Memory and Code Graphs](codebase-memory-and-code-graphs.md)
- [HybridRAG System](hybridrag-system.md)