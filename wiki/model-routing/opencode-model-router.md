# opencode-model-router

> Sources: Marco Jardim, Unknown date
> Raw: [opencode-model-router](../../raw/model-routing/opencode-model-router.md)

## Overview

An OpenCode plugin that routes coding tasks to the cheapest adequate model tier, claiming 80-92% cost reduction versus using one high-end model for everything. Unlike [Model Fusion (OpenRouter)](openrouter-fusion.md), which runs multiple models on the same prompt and fuses answers, this router picks exactly one tier per task and never pays for redundant inference.

## Mechanism

A compressed ~210-token "delegation protocol" is injected into the orchestrator's system prompt, teaching it to: match tasks to a configurable fast/medium/heavy taxonomy; split composite tasks (explore cheaply, then execute at a higher tier, ~36% savings); skip delegation entirely for trivial 1-2 tool-call tasks; and fall back across providers (Anthropic, OpenAI, Google, GitHub Copilot) on failure. The orchestrator itself runs on a mid-tier model rather than the most expensive one available.

## Configurability

Everything — task patterns, cost ratios, tier assignments, routing rules — lives in `tiers.json`. Four built-in modes (normal, budget, quality, deep) bias the router toward savings or capability. Plans can be annotated per-step with `[tier:fast/medium/heavy]` to remove routing ambiguity entirely, and budget-mode state persists across sessions.

## See Also

- [Model Fusion (OpenRouter)](openrouter-fusion.md)
