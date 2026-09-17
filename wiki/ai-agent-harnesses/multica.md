# Multica

> Sources: multica-ai, Unknown date; multica-ai (amhed fork), 2026-09-17
> Raw: [Multica](../../raw/ai-agent-harnesses/multica.md); [Multica fork snapshot](../../raw/ai-agent-harnesses/2026-09-17-multica-fork-snapshot.md)

## Overview

An "open-source managed agents platform" that treats AI coding agents as team members with assignments, comments, and accumulating skills, rather than one-off prompt sessions. Tagline: "Your next 10 hires won't be human." Agents show up on the board like anyone else — they pick up issues, report progress, raise blockers, and hand work back for review.

## Features

Agents as Teammates (assignments, comments, issue creation, proactive blocker reporting); Squads (agent+human groups led by a leader agent for stable task routing); Autonomous Execution with WebSocket progress streaming; Autopilots (cron/webhook-triggered recurring work); Reusable Skills that compound across the team; a Unified Runtimes dashboard for local daemons and cloud runtimes; execution logs replaying every tool call; review gates so work lands in review, not main; Multi-Workspace isolation; role-based access (owner/admin/member).

## Runtimes

Works with **26 agent CLIs** including Claude Code, Codex, Cursor Agent, Copilot, OpenCode, OpenClaw, Hermes, Pi, Antigravity, Kimi, Qwen, and more. Multica does not ship a model — it drives the agent CLIs you already have installed and authenticated; switching providers is a dropdown, not a migration.

## Architecture

Next.js 16 (App Router) frontend; Electron desktop sharing web UI packages; Expo/React Native iOS; Go/Chi backend with sqlc and WebSocket; PostgreSQL 17; a local agent daemon (executing any of the 26 agent CLIs) that runs next to your code. Installable via multica.ai cloud, Multica Desktop, or self-hosted Docker Compose/Helm. Named after Multics (1960s time-sharing OS), reframed as multiplexing compute between humans and agents.

## See Also

- [Firstmate](firstmate.md)
- [oh-my-claudecode](oh-my-claudecode.md)
- [GNHF](gnhf.md)