# Mem0

> Sources: Mem0 team, Unknown date; Mem0 team, 2026-11-02
> Raw: [Mem0 README](../../raw/agent-memory-systems/2026-11-02-mem0.md)

## Overview

Mem0 is a memory layer for AI assistants and agents. It stores durable user, session, and agent state so applications can personalize later interactions without replaying full conversation histories. The project offers Python and JavaScript libraries, a self-hosted server, a hosted platform, a CLI, and integrations with agent frameworks and coding-agent skill systems.

## Memory And Retrieval

The README describes a newer managed-platform algorithm as single-pass, ADD-only memory extraction: memories accumulate rather than being overwritten by update/delete decisions. It adds agent-generated facts, entity linking, semantic retrieval, BM25 keyword matching, entity matching, and temporal reasoning. The listed benchmark scores and latency figures are vendor claims for the managed platform; the README explicitly says open-source results may differ.

Mem0 can maintain memories at user, session, and agent levels. A typical integration searches relevant memories before generating a response, adds the assistant response to the conversation, and then stores the resulting messages for future retrieval. The library requires an LLM and supports configurable embedding and language-model providers.

## Delivery Options

The Python package is installed with `pip install mem0ai`, with optional NLP support for hybrid search and entity extraction. JavaScript applications use the `mem0ai` package. Teams can run the authenticated self-hosted server with Docker Compose, or use the managed cloud platform for a zero-operations deployment. A CLI supports initialization, adding memories, and searching them from a terminal.

Mem0 also publishes reference and pipeline skills for coding assistants. These cover SDK knowledge, CLI usage, integration, testing, and migration from open source to the hosted platform. Framework examples include LangGraph, CrewAI, and Vercel AI SDK integrations.

## Practical Takeaway

Mem0 is a comparatively direct memory service: retrieve relevant records, place them in the model context, and write new conversation-derived memories. Its hybrid retrieval and entity/temporal features extend beyond a plain vector store, but the design remains more application- and record-oriented than Hindsight's retain/recall/reflect model with observations and mental models.

## See Also

- [Hindsight: Agent Memory That Learns](hindsight.md)
- [HybridRAG: Combining Knowledge Graphs and Vector Retrieval](hybridrag-system.md)
- [Open Brain (OB1)](ob1.md)
- [Harness Design Principles](../ai-agent-harnesses/harness-design-principles.md)
