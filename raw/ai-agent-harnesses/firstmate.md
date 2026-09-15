# Firstmate

> Source: https://github.com/kunchenguid/firstmate
> Collected: 2026-07-11
> Published: Unknown

A project orchestration system letting one coding agent coordinate and supervise multiple autonomous agents working in parallel on separate tasks. Tagline: "Talk to one agent. Ship with a crew." Users interact only with the primary "firstmate" agent, which dispatches work to "crewmate" agents running independently in isolated environments; the firstmate handles coordination, supervision, and result aggregation.

Architecture: single point of contact with automatic crew delegation; each crewmate runs in isolated git worktrees (via "treehouse" or Orca); a visible session backend for observing parallel work; two task types, "ship" (delivers changes) and "scout" (produces investigation reports); event-driven supervision with zero-token overhead; optional persistent domain supervisors called "secondmates"; guarded read-only project operations; restart-resistant state management.

Setup requires a supported agent harness (Claude Code, Grok, Pi, Codex, or OpenCode), Git, an authenticated GitHub CLI, and tmux as the default session backend; auto-detects missing dependencies.

Built-in skills/commands: `/afk` (away-mode supervision), `/bearings` (status reports), `/updatefirstmate` (self-updates), `/stow` (knowledge sweep). Tech stack: primarily Shell (97.6%), minor JavaScript/TypeScript. MIT licensed, macOS/Linux support. Separates internal agent-loaded skills from public, standalone skills installable into any project.
