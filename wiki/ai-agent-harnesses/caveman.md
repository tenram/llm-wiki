# Caveman

> Sources: Julius Brussee, Unknown date
> Raw: [Caveman](../../raw/ai-agent-harnesses/2026-09-30-caveman.md)

## Overview

Caveman is a token-reduction toolkit for coding agents. It includes a skill that shortens agent prose, a local proxy that compresses tool results before they reach the model, and middleware that applies the same approach inside applications built with common agent frameworks.

## Three compression layers

The skill changes conversational prose while preserving code, commands, paths, exact errors, and security warnings. It supports lite, full, ultra, and Wenyan modes and works across more than 30 agent hosts.

The proxy runs locally between an agent and its provider. It detects JSON, logs, code, diffs, search results, and text, then retains the parts most likely to answer the task. Originals remain in local SQLite storage and can be retrieved with a recovery handle. MCP tools expose compression, retrieval, statistics, TOON encoding, and decoding.

The middleware wraps provider calls in TypeScript or Python applications. It compresses large tool results while keeping originals in conversation history and giving the model a retrieval tool. Framework adapters include Vercel AI SDK, OpenAI, Anthropic, Google GenAI, LangChain, LiteLLM, CrewAI, PydanticAI, AutoGen, LlamaIndex, and MCP.

## Evidence and limits

The project reports a pinned 54-run benchmark with 33.2% fewer input tokens and 18/18 answer checks passing for its wrap-plus-skill arm. It also reports lower output-token counts from JetBrains and Adobe Research evidence for caveman-style output. These are source-reported measurements, not universal guarantees: one HTML workload increased tokens, the skill adds input tokens, and the README recommends running an A/B trial on the user's own workload.

The skill and client surfaces use MIT licensing. The engine-linked runtime, proxy, rewriter, browse, MCP server, and related Go components use BSL-1.1 with a later Apache-2.0 change date. CLI telemetry is enabled by default but can be disabled.

## See Also

- [Ponytail](ponytail.md)
- [Harness Design Principles](harness-design-principles.md)
- [Superpowers](superpowers.md)
