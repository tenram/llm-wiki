# Claude Code GitHub CI Integration (two accounts)

> Source: https://piotrminkowski.com/2026/07/02/continuous-development-with-claude-code-on-github/ ; https://chamith.medium.com/how-we-integrated-claude-code-into-our-github-workflow-97a5db8bcb8e
> Collected: 2026-07-11
> Published: 2026-07-02 (Piotr Minkowski article); Unknown (Chamith Madusanka article)

## Piotr Minkowski: "Continuous Development with Claude Code on GitHub" (2026-07-02)

Explains setting up continuous, AI-driven development using the Claude GitHub App with Claude Code, so Claude acts as a permanent contributor implementing features and reviewing PRs automatically in response to GitHub issues. Sample project: a Spring Boot REST API bootstrapped from a Backstage template with JPA persistence, CRUD endpoints, two layers of tests, CI pipelines, OpenAPI docs.

Steps: install the Claude GitHub App (github.com/apps/claude) with read access to contents/issues/PRs; in the repo, run Claude Code and choose `install-github-app`, which creates GitHub workflows responding to `@claude` mentions and reviewing new PRs; Claude Code generates `claude.yml` and `claude-code-review.yml` in `.github/workflows` plus an Anthropic API key secret, submitted as a PR to merge. `claude.yml` triggers on issue/PR comments and issue open/assign events containing `@claude`, running `anthropics/claude-code-action@v1` (author's version uses model `claude-sonnet-4-6`, `allowed_bots: 'renovate'`, `additional_permissions: actions: read`). `claude-code-review.yml` triggers on PR open/synchronize/ready_for_review/reopened, also using `claude-code-action@v1` with model `claude-sonnet-4-6`, configuring `plugin_marketplaces` and the `code-review@claude-code-plugins` plugin.

Usage: create an issue starting with `@claude`; the agent implements the change on a temporary branch and summarizes work for a PR; every new PR is auto-reviewed. Notes a cost chart for test issues showing non-trivial cost for simple tasks (no exact figures given); highlights using different models for generation versus review.

## Chamith Madusanka: "How We Integrated Claude Code Into Our GitHub Workflow"

Describes integrating Claude Code into an enterprise platform built on Go, React, TypeScript, and Terraform. Developers mention `@claude` in issues/PRs to trigger AI-assisted implementation, testing, and review without a local checkout. Setup: install the Claude GitHub App, add a `CLAUDE_CODE_OAUTH_TOKEN` secret, create `.github/workflows/claude.yml`, establish context via `CLAUDE.md`, define custom skills in `.claude/skills/`, enforce branch protection requiring human approval before merge. Tooling: GitHub Actions, Claude Opus 4.5, Node.js 22, Go 1.24, golangci-lint, Nx caching, pnpm, Git commit signing.

Reported results: code review time dropped from 30-60 minutes to under 5 minutes; more consistent coding-pattern enforcement; reduced onboarding friction and context-switching; automated linting/formatting/boilerplate.
