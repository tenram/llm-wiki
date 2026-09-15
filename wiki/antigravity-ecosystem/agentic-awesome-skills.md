# Agentic Awesome Skills

> Sources: sickn33, Unknown date
> Raw: [AAS Core — Agentic Awesome Skills](../../raw/antigravity-ecosystem/2026-08-14-agentic-awesome-skills.md)

## Overview

`sickn33/agentic-awesome-skills` is a large agent-first skills catalog centered on AAS Core, a local control plane for discovering skills, validating exact stacks, previewing immutable plans, and keeping evidence reviewable before any target change.

## Core Model

The repo separates selection from application. The agent searches the full catalog, picks exact skill IDs, and validates the resulting stack in memory. AAS Core records that choice and can preview the plan, but it does not rank skills or certify semantic fit.

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
