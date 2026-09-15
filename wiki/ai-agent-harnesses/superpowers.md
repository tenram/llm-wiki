# Superpowers

> Sources: Jesse Vincent / Prime Radiant, Unknown date
> Raw: [Superpowers](../../raw/ai-agent-harnesses/superpowers.md)

## Overview

A skills framework and development methodology for coding agents that front-loads clarification and planning before any code is written, structured around TDD, YAGNI, and DRY.

## Workflow

Brainstorming (Socratic dialogue to validate specs) → Git Worktree Management (isolated workspace, clean baseline) → Planning (2-5 minute tasks with exact file paths and verification steps) → Development Execution (subagents per task, two-stage review: spec compliance then code quality) → Test-Driven Development (RED-GREEN-REFACTOR, deleting pre-test code) → Code Review (severity-based, critical issues block progress) → Branch Finalization (merge, PR, or discard).

## Skills Library

Grouped into Testing, Debugging (systematic-debugging's 4-phase root cause analysis; verification-before-completion), Collaboration (brainstorming, writing-plans, executing-plans, dispatching-parallel-agents, requesting/receiving-code-review, using-git-worktrees, finishing-a-development-branch, subagent-driven-development), and Meta (writing-skills, using-superpowers).

Cross-harness: supports Claude Code, Antigravity, Codex, Cursor, Factory Droid, GitHub Copilot CLI, Kimi Code, OpenCode, and Pi. MIT licensed.

## See Also

- [Harness Design Principles](harness-design-principles.md)
- [Self-Improving AI Skills](../claude-code-ecosystem/self-improving-ai-skills.md)
