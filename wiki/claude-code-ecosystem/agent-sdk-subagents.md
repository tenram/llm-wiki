# Claude Agent SDK: Subagents

> Sources: Anthropic, Unknown date
> Raw: [Agent SDK Overview (Subagents)](../../raw/claude-code-ecosystem/agent-sdk-subagents.md)

## Overview

The Claude Agent SDK is a Python/TypeScript library exposing the same agent loop, tools, and context management that power Claude Code, but embeddable in your own process. It sits alongside three other Anthropic entry points: the Claude Code CLI (interactive terminal use), the Client SDK (raw API access where you implement the tool loop yourself), and Managed Agents (a hosted REST API where Anthropic runs the agent and sandbox).

## Capabilities

Built-in tools, hooks (custom code at lifecycle points), MCP connectivity, fine-grained permissions, resumable/forkable sessions, and auto-loaded skills/commands/memory from `.claude/` — all available to SDK-built agents, not just the CLI. Plugins package skills, agents, hooks, and MCP servers for distribution by local path.

**Subagents** are the SDK's mechanism for spawning specialized agents to handle focused subtasks from within a top-level agent — the same subagent pattern Claude Code itself uses for parallel or context-isolated work, now exposed as a first-class SDK capability rather than a CLI-only behavior.

## Branding Constraint

Third-party products built on the SDK cannot call themselves "Claude Code" or "Claude Code Agent," cannot offer claude.ai login or its rate limits, and must keep their own distinct branding rather than appearing to be an Anthropic product.

## See Also

- [Anthropic Agent Skills](anthropics-skills.md)
