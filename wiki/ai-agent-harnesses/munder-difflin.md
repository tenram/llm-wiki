# Munder Difflin

> Sources: chaitanyagiri, 2026-08-24
> Raw: [Munder Difflin](../../raw/ai-agent-harnesses/2026-08-24-munder-difflin.md)

## Overview

A desktop (Electron) multi-agent harness that wraps real terminal-agent CLIs — Claude Code, Antigravity/agy, Codex, Grok, Kimi, Gemini CLI, Qwen, OpenCode, Crush, pi.dev, Copilot CLI, Cursor — into a self-coordinating team visualized as avatars on a 2D office floor. A GOD orchestrator agent ("Michael", your clone) routes work; you talk to Michael and escalate only what needs you. Works on subscription hourly limits with BYOK keys and local LLMs.

## Coordination model

The hive is a local git repo of plain files: per-agent memory, atomic-file mailboxes (`outbox/`/`inbox/`), a shared blackboard, an append-only event log. Agents never touch git themselves — a single-committer design avoids `index.lock` corruption. The router delivers messages; the GOD agent adjudicates, assigns, and escalates only critical items (spend, destructive ops, scope changes) into a human approvals queue.

## Notable engineering

- Real PTYs: every agent is a `node-pty` process rendered byte-for-byte in xterm.js; provider lifecycle hooks (`cth-hook`, `agy-hook`) feed the event plane.
- Memory: markdown-first layer plus a semantic recall index with condensation; an Enterprise Knowledge Graph makes your own documents queryable by any agent.
- Safety: circuit breaker ladder (steer → constrain → stop), per-agent token budgets, cost attribution read from real JSONL transcripts.
- Command Center: dependency-aware kanban, scheduled missions, fleet monitoring, Monaco IDE with git rails, Slack/webhook-spawned ephemeral workers, shareable "hires".

## See Also

- [GNHF](gnhf.md)
- [Firstmate](firstmate.md)
- [Multica](multica.md)
