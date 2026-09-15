# Statewright

> Sources: statewright, Unknown date
> Raw: [Statewright](../../raw/ai-agent-harnesses/statewright.md)

## Overview

A state-machine framework that restricts which tools an agent can access per workflow phase, rather than giving it unrestricted access to 40+ tools. Tagline: "Agents are suggestions, states are laws."

## Architecture

Three layers: a pure Rust state machine Engine (no LLM dependency); an Agent Binary (`sw-agent`) that executes directly against Ollama with per-state model routing; and a Plugin Layer (MCP gateway) integrating Claude Code, Codex, Pi, opencode, and Cursor.

Enforcement mechanisms: per-state tool restriction, "bash discernment" blocking destructive commands even when Bash is otherwise allowed, edit guards capping diff size/file count per state, guard-based conditional transitions, per-state model routing (cheap models for recon, frontier models for hard reasoning), human approval gates, and environment scoping to hide or substitute credentials. Enforcement is "hard" (intercepted) for Claude Code, Codex, Pi, and opencode, but only "advisory" (context injection) for Cursor.

## Reported Results

On a 5-task SWE-bench subset, constrained execution raised pass rate from 2/10 to 10/10; the authors note a rough capability floor around 13GB models below which surgical edits become unreliable.

Licensing is split: engine/agent layers Apache 2.0, MCP gateway FSL-1.1-ALv2 (converts to Apache 2.0 in 2029), with a patent pledge. Commercial hosted tiers exist alongside self-hosting via Docker Compose.

## See Also

- [Life-Harness](life-harness.md)
- [Harness Design Principles](harness-design-principles.md)
- [OpenClaw](openclaw.md)
