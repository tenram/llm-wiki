# Agentic Awesome Skills

> Sources: sickn33, Unknown date; benjaminasterA, 2026-11-10
> Raw: [AAS Core — Agentic Awesome Skills](../../raw/antigravity-ecosystem/2026-08-14-agentic-awesome-skills.md); [Antigravity Awesome Skills README (2026-11-10 snapshot)](../../raw/antigravity-ecosystem/2026-11-10-antigravity-awesome-skills.md)

## Overview

Agentic Awesome Skills and the similarly named `benjaminasterA/antigravity-awesome-skills` are large agent-first skills catalogs for cross-tool coding assistants. The new snapshot advertises 889+ skills, universal `SKILL.md` compatibility, bundles, workflows, validation, and installers for Claude Code, Gemini CLI, Codex CLI, Cursor, Copilot, OpenCode, Antigravity, and other tools. The two repositories are related in theme but are distinct projects.

## Core Model

The AAS Core repo separates selection from application. The agent searches the full catalog, picks exact skill IDs, and validates the resulting stack in memory. AAS Core records that choice and can preview the plan, but it does not rank skills or certify semantic fit. The Antigravity Awesome Skills repo adds role-based bundles and ordered workflows as discovery and execution aids; its README presents these as curated guidance, not separate installations.

That separation is the main design point:

1. Search the local catalog.
2. Compose the stack from exact IDs.
3. Validate structure and identity.
4. Persist an approved stack and evidence artifact.
5. Preview the plan before any write path.

## Antigravity Path

Antigravity gets explicit first-class support. The repository treats it as the default direct-install target, with a narrowed-install flow that avoids overloading the host with the full catalog.

The Antigravity path is intentionally conservative:

- Use exact skill IDs when you already know the set.
- Use metadata filters when you need a narrower catalog slice.
- Use `--all` only with explicit consent.

## Packaging Surface

The repo is not just a skill list. It also ships:

- a hosted and local web app for review,
- specialized plugins for narrower domains,
- bundles for role-based discovery,
- workflows for ordered execution,
- host-specific install targets for Claude Code, Cursor, Codex CLI, Gemini CLI, OpenCode, GitHub Copilot, Kiro, and Autohand Code.

## Why It Matters

This repo is useful when you want breadth, reproducibility, and a review step before installation. It is also a good comparison point for curated lists like [Awesome Claude Skills](../claude-code-ecosystem/awesome-claude-skills.md).

## See Also

- [Awesome Claude Skills](../claude-code-ecosystem/awesome-claude-skills.md)
- [Superpowers](../ai-agent-harnesses/superpowers.md)
- [Opencode Orchestration Layer](../opencode-ecosystem/opencode-orchestration.md)
- [Anthropic Agent Skills](../claude-code-ecosystem/anthropics-skills.md)
