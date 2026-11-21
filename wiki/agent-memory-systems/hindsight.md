# Hindsight: Agent Memory That Learns

> Sources: Vectorize.io, Unknown date; Vectorize.io, 2026-11-02
> Raw: [Hindsight README](../../raw/agent-memory-systems/2026-10-19-hindsight.md); [Hindsight README, 2026-11-02](../../raw/agent-memory-systems/2026-11-02-hindsight.md)

## Overview

Hindsight is an agent memory system designed to help agents learn over time, not only recall conversation history. It stores facts and experiences in isolated memory banks, consolidates them into evidence-backed observations, and exposes three operations: `retain` for ingestion, `recall` for retrieval, and `reflect` for deeper synthesis.

## Memory Model

Hindsight distinguishes world facts, agent experiences, observations, and mental models. Retain uses an LLM to extract facts, entities, relationships, and temporal data, then normalizes those representations into searchable indexes. Observations consolidate related facts while retaining supporting evidence and proof counts, so later information can strengthen, weaken, or extend a belief instead of silently replacing it.

Recall combines semantic vector search, BM25 keyword search, entity and temporal graph links, and time-range filtering. Results are merged with reciprocal-rank fusion and optionally reranked with a cross-encoder. Reflect performs a more extensive analysis to form connections and answer questions that need interpretation rather than lookup.

Mental models are persistent answers to defined questions about a bank. Knowledge pages use the same mechanism as living, searchable documents that can be projected onto disk as Markdown. A bank isolates the memories for one user, agent, or project and can carry background context and disposition traits that affect reflective reasoning. The README also describes multilingual preservation and opt-in memory defense for secrets and PII.

## Integration And Operations

Hindsight offers a Docker server, external PostgreSQL, pip installation, Helm deployment, embedded Python and Node.js packages, REST, CLI, and Python, Node.js, and Go clients. It has a built-in MCP endpoint per bank and wrappers that automatically recall before an LLM call and retain the conversation afterward. The README lists integrations for coding agents, agent frameworks, low-code tools, and applications, plus a coding-agent package that creates per-repository banks and project knowledge pages.

The current README also documents an embedded Python distribution, a two-line LiteLLM wrapper, more than 60 integrations, and a coding-agent installer that creates per-repository banks without a separate ingestion command. It presents Hindsight Cloud as a usage-based managed option alongside self-hosted and air-gapped deployments.

Production storage is PostgreSQL with pgvector or Oracle AI Database 23ai. The project documents hierarchical configuration, Prometheus monitoring, an administrative CLI, lifecycle webhooks, extension points, and a managed cloud offering. Its benchmark and production-use statements are vendor claims; the README says some benchmark results were independently reproduced, but the figures remain source-attributed rather than independently verified here.

## Practical Takeaway

Hindsight is a richer alternative to a flat conversation log or a single vector index. Its distinctive commitment is a layered memory model combining structured entities, temporal data, evidence-backed consolidation, and reflective synthesis. That power adds an LLM-backed ingestion and maintenance path, so it is better suited to agents that need durable evolving knowledge than to simple one-shot RAG.

## See Also

- [HybridRAG: Combining Knowledge Graphs and Vector Retrieval](hybridrag-system.md)
- [Open Brain (OB1)](ob1.md)
- [RecallMax](recallmax.md)
- [Mem0](mem0.md) — a more direct application memory layer with hybrid retrieval and entity/temporal features.
- [Hex Knowledge Engine](hex-knowledge-engine.md) — a workspace context graph with nightly curation and contested-knowledge status.
- [Model Context Protocol (MCP)](../browser-and-mcp-tooling/model-context-protocol-overview.md)
