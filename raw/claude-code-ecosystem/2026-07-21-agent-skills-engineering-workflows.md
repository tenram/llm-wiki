# Agent Skills: Production-Grade Engineering Workflows for AI Agents

> Source: https://github.com/addyosmani/agent-skills
> Collected: 2026-07-21
> Published: Unknown

## Overview

Agent Skills is an open-source collection of structured engineering workflows designed to guide AI coding agents through professional software development practices. The project contains 24 skills organized across the complete development lifecycle, from specification through deployment.

## Core Purpose

The fundamental challenge Agent Skills addresses: AI agents naturally gravitate toward shortcuts—skipping specifications, tests, security reviews, and other practices that distinguish production-quality work from prototype-quality code. These skills encode the disciplined workflows senior engineers follow, making them repeatable and accessible to AI agents.

## Key Components

**8 Slash Commands** mapping to development phases:
- `/spec` - Define requirements before coding
- `/plan` - Decompose work into atomic tasks
- `/build` - Implement incrementally
- `/test` - Verify functionality
- `/review` - Quality gates before merging
- `/webperf` - Audit web performance
- `/code-simplify` - Reduce complexity
- `/ship` - Deploy to production

**24 Skills** organized by lifecycle stage:
- **Define**: Interview-me, idea-refine, spec-driven-development
- **Plan**: Planning-and-task-breakdown
- **Build**: Seven skills covering implementation, testing, API design, and context management
- **Verify**: Browser testing and debugging
- **Review**: Code review, simplification, security, performance
- **Ship**: Git workflow, CI/CD, deprecation, documentation, observability, launching

**4 Specialist Personas**: Code reviewer, test engineer, security auditor, web performance auditor

## Skill Anatomy

Each skill follows a consistent structure:
- Frontmatter with name and triggering conditions
- Process: step-by-step workflow agents follow
- Rationalizations table: common excuses for skipping steps plus rebuttals
- Red flags: warning signs something's wrong
- Verification requirements: measurable evidence of completion

## Installation

The fastest approach uses the open skills CLI:
```
npx skills add addyosmani/agent-skills
```

Tool-specific integrations available for Claude Code, Cursor, Antigravity CLI, Gemini CLI, Windsurf, Codex, OpenCode, and GitHub Copilot.

## Design Philosophy

Skills encode hard-won engineering judgment from sources like "Software Engineering at Google," including concepts such as:
- Hyrum's Law in API design
- The test pyramid in TDD
- Trunk-based development in git workflows
- Shift Left and feature flags in CI/CD
- Treating code as a liability in deprecation practices

Three distinguishing characteristics:
1. **Process-driven**: Actionable workflows, not reference documentation
2. **Anti-rationalization**: Embedded counter-arguments to common shortcuts
3. **Verification-focused**: Every skill ends with measurable exit criteria

## Adoption Approaches

The Adoption Guide covers two paths: greenfield projects using the full lifecycle from day one, or incremental rollout for established codebases prioritizing verification first.

## Contributing

Skills must be specific (actionable steps), verifiable (clear exit criteria), battle-tested (based on real workflows), and minimal (only necessary guidance). See `docs/skill-anatomy.md` for format specifications.

## License

MIT—skills are freely usable in projects, teams, and tools.
