# Multica

> Source: https://github.com/multica-ai/multica
> Collected: 2026-07-11
> Published: Unknown

Described as "the open-source managed agents platform," tagline "Your next 10 hires won't be human." Lets teams assign tasks to AI coding agents the way they'd assign work to human colleagues: agents appear on boards, participate in conversations, and accumulate reusable skills over time, instead of requiring users to repeatedly copy-paste prompts.

Key features: Agents as Teammates (receive assignments, post comments, create issues, proactively report blockers); Squads (groups of agents and humans led by a leader agent for stable task routing at scale); Autonomous Execution (full lifecycle management with real-time progress streaming over WebSocket); Autopilots (scheduled recurring work via cron, webhooks, or manual runs); Reusable Skills (solutions become team-wide, compounding capabilities); Unified Runtimes (centralized dashboard for local daemons and cloud runtimes with CLI auto-detection); Multi-Workspace support.

Compatible runtimes: Claude Code, Codex, CodeBuddy, GitHub Copilot CLI, OpenCode, OpenClaw, Hermes, Pi, Cursor Agent, Kimi, Kiro CLI, Antigravity, Qoder CLI, Trae CLI.

Architecture: Next.js 16 (App Router) frontend; Go backend (Chi router, sqlc, WebSocket); PostgreSQL 17 with pgvector; local daemon runtime executing supported agent CLIs.

Install: Homebrew, curl script, PowerShell (Windows), or self-hosted Docker (`--with-server`). Getting started: `multica setup`, verify runtime connectivity, create agents via Settings→Agents, assign issues. Named after Multics (1960s time-sharing OS), reframed as multiplexing compute between humans and agents.
