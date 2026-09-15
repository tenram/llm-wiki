# Codebase Memory and Code Graphs

> Sources: https://github.com/DeusData/codebase-memory-mcp; https://github.com/colbymchenry/codegraph; https://github.com/ArcadeData/arcadedb; https://github.com/neo4j/neo4j
> Collected: 2026-08-18
> Published: Unknown

This cluster covers code-aware memory systems that turn repositories into persistent, queryable structure. `codebase-memory-mcp` exposes code memory over MCP, while `codegraph` turns code into graph form for later traversal and lookup.

ArcadeDB and Neo4j provide graph-backed storage choices for those relationships. The shared pattern is simple: extract symbols, links, and dependencies once, then query the resulting graph instead of rereading raw source on every question.
