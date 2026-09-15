# RightMemory

> Sources: RightL, Unknown date
> Raw: [RightMemory](../../raw/agent-memory-systems/rightmemory.md)

## Overview

A "tree + graph" memory system for teams of AI coding agents: a markdown heading tree for local context, cross-linked by typed edges (dep, cfg, ver, doc, todo) for facts spanning sections, git-synced across devices and clients.

## Design

Separates memory operations into distinct agent roles: retrieve, update, consolidation ("dreamer"), and reflection ("insight"), keeping bookkeeping isolated from the main agent's task work. Shared views use mirrored files and provider questions for controlled collaboration. Runs standalone (its own Pydantic AI agents) or delegated to Codex/Claude Code CLI, sharing one memory schema either way.

Explicit design stance: memory should be file-based, inspectable, and deterministic rather than opaque embeddings, a direct contrast with vector-based memory systems like [OB1](ob1.md).

## See Also

- [OB1](ob1.md)
- [Harness Design Principles](../ai-agent-harnesses/harness-design-principles.md)
