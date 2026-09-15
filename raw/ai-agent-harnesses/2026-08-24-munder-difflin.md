# Munder Difflin

> Source: https://github.com/chaitanyagiri/munder-difflin
> Collected: 2026-08-24
> Published: Unknown (v0.4.5, working prototype)

Agent harness to run an office of your clones. Free, open-source, performant multi-agent harness that works with subscriptions you already pay for, on their hourly limits. Wraps terminal coding CLIs — Claude Code, Antigravity/agy (Gemini), OpenAI Codex, xAI Grok, Kimi Code, Gemini CLI, Qwen, OpenCode, Crush, pi.dev, GitHub Copilot CLI, Cursor — with bring-your-own keys and local LLMs. Electron · React · TypeScript · Pixi.js · xterm.js · node-pty. MIT (code); bundled pixel art licensed separately from LimeZu.

## Concept

Each terminal CLI session becomes a real agent process in a pseudo-terminal (node-pty), rendered byte-for-byte with xterm.js. Each agent is an avatar on a Pixi.js 2D office floor (Animal Crossing × Earthbound × SNES aesthetic; The Office cast). A GOD orchestrator agent ("Michael", your clone) routes work between agents; you talk to Michael and remain his boss.

## How it works

1. You spawn agents — each a normal terminal process with its own working directory, identity, provider lifecycle.
2. Agents collaborate through the hive — a local git repo of plain files: per-agent `outbox/`/`inbox/` mailboxes, shared blackboard, append-only event log. Single-committer design (no agent touches git) avoids index.lock corruption.
3. GOD agent reads every request, resolves routine ones itself, escalates only critical items (spend, destructive ops, scope changes) into an approvals queue.
4. Everything visible: avatars move, envelopes fly desk-to-desk, live terminal streams; you can type back into any session.

## Features

- Per-agent git worktrees for parallel isolation.
- Memory: markdown-first memory layer + semantic recall index ("fastest memory layer in the world" claim), condensation so it doesn't grow forever; Enterprise Knowledge Graph for your own documents/policies.
- Control & safety: human gates, circuit breaker (steer → constrain → stop ladder), per-agent token budgets, real cost from transcripts, durable ledger, OTel spans, tool waterfall.
- Command Center: kanban tasks with dependencies, scheduled missions + heartbeat, fleet monitoring, memory search, activity log, CI watcher; Skills catalog (227 skills) across Claude Code/OpenCode/Codex; built-in Monaco IDE with git rails.
- Integrations: Slack & webhooks (Michael spawns ephemeral workers), shareable hires via munderdifflin:// links + Agent Gallery, BYOK secret broker, Ollama/LM Studio/vLLM local LLMs, one-click updates, Prerequisites page that self-heals missing CLIs.

## Architecture

Two data planes feed one Electron renderer:
- Terminal plane: main-process PtyManager spawns node-pty processes, streams over per-id IPC; renderer talks through typed window.cth bridge with sandboxed fs/git helpers.
- Hive/event plane: hive.ts (on-disk multi-agent layer), hooks.ts (hook server receiving provider lifecycle payloads — cth-hook for Claude Code, agy-hook for Antigravity), memory.ts (semantic memory CLI wrapper), router + GOD adjudication, inbox wake watchdogs.

Cost telemetry reads ~/.claude/projects/ JSONL transcripts for real token/cost attribution. v0.4.5 fixed cost-counter resets, Apple Silicon NaN embeddings (pinned to CPU), and undelivered-mail stalls.
