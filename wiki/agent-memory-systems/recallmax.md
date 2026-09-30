# RecallMax

> Sources: Christopher L. Hammer, Unknown date
> Raw: [RecallMax](../../raw/agent-memory-systems/2026-09-30-recallmax.md)

## Overview

RecallMax is a TypeScript library and CLI for compressing long conversations, notes, and project histories into structured memory records that fit future agent context. It is designed for local-first continuity without requiring an LLM call during compression.

## What it preserves

The compressor parses conversation-style input, scores messages by importance, removes filler and duplicates, and retains decisions, facts, errors, open questions, and constraints. The result exposes structured fields such as `decisions` and `openQuestions`, with a configurable token budget.

## Usage and fit

The package can be built and tested with npm and used from TypeScript through `compressText`. Its CLI accepts JSON conversations or Markdown from standard input and can emit compressed Markdown. It fits the memory layer of a local-first agent stack: unlike a vector or graph retrieval system, its primary operation is deterministic context reduction before a later session.

## See Also

- [HybridRAG: Combining Knowledge Graphs and Vector Retrieval](hybridrag-system.md)
- [RightMemory](rightmemory.md)
- [Open Brain (OB1)](ob1.md)
