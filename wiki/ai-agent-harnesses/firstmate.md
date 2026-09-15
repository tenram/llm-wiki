# Firstmate

> Sources: kunchenguid, Unknown date
> Raw: [Firstmate](../../raw/ai-agent-harnesses/firstmate.md)

## Overview

An orchestration layer where a user talks to a single "firstmate" agent, which delegates work to isolated "crewmate" agents running in parallel, aggregating and supervising their output. Tagline: "Talk to one agent. Ship with a crew."

## Architecture

Each crewmate runs in an isolated git worktree (via "treehouse" or Orca); a visible session backend (tmux by default) lets the user observe parallel work. Two task types: "ship" (delivers changes) and "scout" (investigation reports). Supervision is event-driven with zero-token overhead when idle; optional persistent "secondmate" supervisors handle recurring domains. State is restart-resistant.

Requires Claude Code, Grok, Pi, Codex, or OpenCode as the underlying harness, plus Git, GitHub CLI, and tmux. Built-in commands: `/afk`, `/bearings`, `/updatefirstmate`, `/stow`. MIT licensed, mostly Shell.

## See Also

- [Multica](multica.md)
- [oh-my-claudecode](oh-my-claudecode.md)
