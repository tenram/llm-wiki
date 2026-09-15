# opencode-model-router

> Source: https://github.com/marco-jardim/opencode-model-router
> Collected: 2026-07-31
> Published: Unknown

An OpenCode plugin that automatically routes coding tasks to the most cost-effective model tier, claiming 80-92% cost reduction versus using one high-end model for all work.

## Mechanism

Injects a compressed ~210-token "delegation protocol" into each message's system prompt, teaching the orchestrator to:

1. Match tasks to tiers using a configurable taxonomy (fast for searching/reading, medium for implementation, heavy for architecture)
2. Split composite tasks — explore cheaply with @fast, then execute with @medium (~36% savings on multi-phase work)
3. Skip unnecessary delegation for trivial tasks (1-2 tool calls)
4. Select the cheapest adequate tier, using injected cost ratios so the model understands price tradeoffs
5. Fall back across providers if one fails

The orchestrator itself runs on a mid-tier model (Sonnet), not Opus, reserving premium models for genuinely complex work.

## Features

- Four routing modes: normal (balanced), budget (aggressive savings), quality (liberal), deep (architecture-focused)
- Multi-provider support: Anthropic, OpenAI, Google, GitHub Copilot, with automatic fallback
- Fully configurable task patterns, cost ratios, rules, and tier assignments via `tiers.json`
- Plan annotation: tag markdown steps with `[tier:fast/medium/heavy]` to remove routing ambiguity
- Cross-session persistence — budget mode survives restarts
