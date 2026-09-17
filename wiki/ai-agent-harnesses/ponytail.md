# Ponytail

> Sources: DietrichGebert, 2026-06-18
> Raw: [Ponytail](../../raw/ai-agent-harnesses/2026-09-17-ponytail.md)

## Overview

A cross-harness skill that makes your AI agent think like "the laziest senior dev in the room": before writing code, stop at the first ladder rung that holds, so the smallest working solution wins. "The best code is the code you never wrote." Sells on measured agentic-benchmark reductions — ~54% less code, ~20% cheaper, ~27% faster — while keeping every safety guard.

## The ladder

1. Does this need to exist at all? → no: skip it (YAGNI)
2. Already in this codebase? → reuse, don't rewrite
3. Stdlib does it? → use it
4. Native platform feature? → use it
5. Already-installed dependency? → use it
6. Can it be one line? → one line
7. Only then: the minimum code that works

The ladder runs *after* understanding the problem, not instead of it. Lazy, not negligent: trust-boundary validation, data-loss handling, security, and accessibility are never on the chopping block.

## Intensity levels

`full` (default) enforces the ladder; `lite` is a lighter touch; `ultra` is for "when the codebase has wronged you personally"; `off` disables. Persistent via `PONYTAIL_DEFAULT_MODE` or `~/.config/ponytail/config.json`.

## Distribution

Ships as plugin/skill for ~20 agent hosts (Claude Code, Codex, Copilot CLI, Pi, OpenCode, Gemini CLI, Cursor, Hermes, OpenClaw, Grok, and more) plus an AGENTS.md rule-only fallback that works from a checkout on most agents. Adds `/ponytail`, `/ponytail-review`, `/ponytail-audit`, `/ponytail-debt`, `/ponytail-gain`, `/ponytail-help` commands. Ruleset is injected into subagents spawned via the Agent tool.

## Measurement

Agentic benchmark: headless Claude Code on a real FastAPI + React repo, 12 feature tickets, n=4, Haiku 4.5, scored on the git diff. ponytail was the only arm cutting every metric (LOC -54%, tokens -22%, cost -20%, time -27%) while staying 100% safe — the earlier 80-94% single-shot figure was partly a conversational-baseline artifact.

## See Also

- [Superpowers](superpowers.md)
- [oh-my-claudecode](oh-my-claudecode.md)
- [Harness Design Principles](harness-design-principles.md)