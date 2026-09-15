# GNHF (Good Night, Have Fun)

> Sources: kunchenguid, 2026-08-24
> Raw: [gnhf](../../raw/ai-agent-harnesses/2026-08-24-gnhf.md)

## Overview

gnhf is a ralph/autoresearch-style orchestrator that keeps coding agents working autonomously overnight: each iteration makes one small, committed, documented change toward an objective, and you wake up to a branch of clean work plus a full log. One command starts the loop; runtime caps and stop conditions bound it.

## Design

The loop is deliberately simple: validate a clean git tree, branch, then iterate — build prompt (injecting shared `notes.md` memory), invoke the agent non-interactively, commit on success or roll back on failure. Three consecutive failures abort. The interesting engineering is in failure semantics:

- Commit failures preserve uncommitted work for the next iteration to repair; other failures `git reset --hard`.
- Usage-limit exhaustion is not a failure: gnhf reads rate-limit reset times and resumes automatically after the window (`--max-rate-limit-wait` caps total waiting).
- No-op iterations count as failures toward the abort limit.
- `--stop-when <natural-language condition>` ends the loop when the agent reports the condition met.

## Modes

Default creates a `gnhf/<slug>` branch. Live Branch Mode (`--current-branch --push`) commits to the current branch and pushes per iteration. Worktree Mode runs each agent in an isolated git worktree, enabling multiple concurrent agents on one repo; completed worktrees are preserved for review.

## Agent support

Seven native agents (Claude Code, Codex, Copilot CLI, Pi, Cursor, Rovo Dev, OpenCode) plus any ACP target via bundled acpx. Config covers default agent, binary path overrides, per-agent arg overrides, and commit-message conventions (plain or conventional-commits preset).

## See Also

- [Autoresearch](../research-and-training/autoresearch.md)
- [Firstmate](firstmate.md)
- [Munder Difflin](munder-difflin.md)
