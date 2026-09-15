# Agent Skills Engineering Workflows

> Sources: addyosmani, Unknown date
> Raw: [Agent Skills: Production-Grade Engineering Workflows](../../raw/claude-code-ecosystem/2026-07-21-agent-skills-engineering-workflows.md)

## Overview

`addyosmani/agent-skills` is a curated collection of 24 skills built on the Agent Skills format, aimed at a specific problem: AI coding agents default to shortcuts, skipping specs, tests, and security review in favor of fast prototype-quality output. The collection encodes senior-engineer workflow discipline (drawn in part from "Software Engineering at Google") as skills an agent can load, covering the entire software development lifecycle from specification through deployment.

## Structure

Two layers sit on top of the skills themselves:

- **8 slash commands**, one per lifecycle phase: `/spec` (define requirements), `/plan` (break work into atomic tasks), `/build` (implement incrementally), `/test` (verify functionality), `/review` (quality gate before merge), `/webperf` (performance audit), `/code-simplify` (reduce complexity), `/ship` (deploy).
- **24 skills** grouped by stage: Define (interview-me, idea-refine, spec-driven-development), Plan (planning-and-task-breakdown), Build (seven skills spanning implementation, testing, API design, context management), Verify (browser testing and debugging), Review (code review, simplification, security, performance), Ship (git workflow, CI/CD, deprecation, documentation, observability, launching).
- **4 specialist personas**: code reviewer, test engineer, security auditor, web performance auditor.

## Skill Anatomy

Every skill in the collection shares a fixed shape: YAML frontmatter with triggering conditions, a step-by-step process, a rationalizations table (common excuses for skipping the step, paired with rebuttals), red flags to watch for, and measurable verification requirements the agent must satisfy before calling the step done.

## Design Philosophy

Three properties distinguish this collection from generic documentation:

1. **Process-driven** — actionable workflows rather than reference material.
2. **Anti-rationalization** — each skill anticipates and pre-empts the excuse an agent would use to skip it.
3. **Verification-focused** — every skill ends in a measurable exit criterion rather than a vague "done."

Specific engineering concepts are baked into individual skills: Hyrum's Law informs API design guidance, the test pyramid shapes the TDD skill, trunk-based development underlies the git workflow skill, Shift Left and feature flags inform CI/CD, and "code as a liability" frames the deprecation skill.

## Installation and Adoption

Installed via the open skills CLI (`npx skills add addyosmani/agent-skills`), with tool-specific integrations for Claude Code, Cursor, Antigravity CLI, Gemini CLI, Windsurf, Codex, OpenCode, and GitHub Copilot. The adoption guide offers two paths: adopt the full lifecycle from day one on a greenfield project, or roll out incrementally on an existing codebase by prioritizing verification-stage skills first.

Licensed MIT.

## See Also

- [Anthropic Agent Skills](anthropics-skills.md) — the underlying `SKILL.md` format and specification this collection builds on.
