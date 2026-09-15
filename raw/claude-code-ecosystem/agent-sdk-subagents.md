# Agent SDK Overview (Subagents)

> Source: https://code.claude.com/docs/en/agent-sdk/overview#subagents
> Collected: 2026-07-31
> Published: Unknown

The Claude Agent SDK is a library (Python and TypeScript) that runs the same agent loop, tools, and context management that power Claude Code, but programmable in your own process — distinct from the Claude Code CLI (interactive terminal use), the Client SDK (raw API access, you implement the tool loop), and Managed Agents (hosted REST API, Anthropic runs the agent/sandbox).

## Capabilities table

| Capability | What it does |
|---|---|
| Built-in tools | Read, write, edit files, run commands, search the web |
| Hooks | Run custom code at key points in the agent lifecycle |
| Subagents | Spawn specialized agents for focused subtasks |
| MCP | Connect external tools/data sources via Model Context Protocol |
| Permissions | Control which tools run automatically vs. need approval |
| Sessions | Maintain context across exchanges; resume or fork later |
| Skills, commands, memory | Load automatically from `.claude/` and `~/.claude/`, same as Claude Code |
| Plugins | Package skills, agents, hooks, and MCP servers; load by local path |

Subagents specifically let a top-level agent spawn specialized agents for focused subtasks — the same mechanism documented in the [Subagents](https://code.claude.com/docs/en/agent-sdk/subagents) reference page.

## Branding note

Third-party products built on the Agent SDK may not claim to be "Claude Code" or "Claude Code Agent," must not offer claude.ai login or its rate limits, and must maintain their own product branding rather than appearing to be an Anthropic product.
