# Superset

> Sources: Superset project, Unknown date
> Raw: [Superset](../../raw/ai-agent-harnesses/2026-09-30-superset.md)

## Overview

Superset is a desktop agentic IDE for running Claude Code, Codex, OpenCode, and other CLI coding agents in parallel workspaces. It combines terminals, worktrees, diff review, browser previews, automation, remote access, a CLI, a TypeScript SDK, and an MCP server around the same workspace model.

## Workspace model

Each independent task can use its own Git worktree, terminals, and preview ports. The built-in diff viewer supports inspection and feedback before commits. Agents can also receive UI element context from Design mode, fix selected pull-request lines, or publish reviewable Pages for teammates.

## Automation and integrations

Superset supports scheduled agent sessions, remote access from another computer or an iPhone, workspace setup and teardown scripts, terminal presets, Slack and Linear entry points, and handoff to other IDEs. Its built-in skills cover parallel orchestration, automations, feedback, and issue diagnosis. The CLI manages workspaces, agents, terminals, and hosts; the SDK and MCP server expose the same surfaces programmatically.

## Position in the harness landscape

Superset is an operational harness and workspace manager rather than an agent model. Its key design choice is to make parallel execution, review, and environment isolation first-class. Worktrees separate files but do not sandbox processes or eliminate merge conflicts, so process isolation and review remain explicit responsibilities.

## See Also

- [Harness Design Principles](harness-design-principles.md)
- [Awesome Harness Engineering](awesome-harness-engineering.md)
- [Ponytail](ponytail.md)
