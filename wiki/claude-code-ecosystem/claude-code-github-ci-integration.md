# Claude Code GitHub CI Integration

> Sources: Piotr Minkowski, 2026-07-02; Chamith Madusanka, Unknown date
> Raw: [Claude Code GitHub CI Integration](../../raw/claude-code-ecosystem/claude-code-github-ci-integration.md)

## Overview

Two independent accounts of wiring the Claude GitHub App into repository CI so Claude implements features and reviews PRs automatically in response to `@claude` mentions, converging on the same core pattern despite different codebases (a Spring Boot API vs. a Go/React/Terraform enterprise platform).

## Common Pattern

1. Install the Claude GitHub App with read access to contents, issues, and PRs.
2. Add an API credential as a repo secret (`ANTHROPIC_API_KEY` or `CLAUDE_CODE_OAUTH_TOKEN`).
3. Generate `.github/workflows/claude.yml` (responds to `@claude` mentions on issues/PR comments) and, optionally, a dedicated `claude-code-review.yml` (auto-reviews every new PR), both built on `anthropics/claude-code-action@v1`.
4. Provide repo context via `CLAUDE.md` and optional custom skills in `.claude/skills/`.
5. Keep branch protection requiring human approval before merge.

Minkowski's setup used Claude Code's `install-github-app` flow to scaffold the workflow files as a PR, with model `claude-sonnet-4-6` and an added `code-review@claude-code-plugins` plugin for the review workflow. Madusanka's enterprise setup used Claude Opus 4.5, Node.js 22/Go 1.24 tooling, and reported code review time dropping from 30-60 minutes to under 5 minutes, alongside more consistent lint/style enforcement and reduced onboarding friction.

Minkowski also noted non-trivial per-issue cost for simple tasks (no exact figures published) and recommended using cheaper/different models for generation versus review, a cost-routing pattern echoed by several harness projects in this wiki (see [oh-my-claudecode](../ai-agent-harnesses/oh-my-claudecode.md), [Statewright](../ai-agent-harnesses/statewright.md)).

## See Also

- [Claude How To](claude-howto.md)
- [oh-my-claudecode](../ai-agent-harnesses/oh-my-claudecode.md)
