# ThinkRail

> Sources: JetBrains, Unknown date
> Raw: [ThinkRail README](../../raw/ai-agent-harnesses/2026-11-10-thinkrail.md)

## Overview

ThinkRail is a JetBrains incubator agentic IDE built around the `pi` coding agent. It combines isolated Git worktree workspaces, a GUI, durable project specifications, reusable skills, multiple chat sessions, and extension support.

## Workspace And Specification Model

Projects can create separate Git worktree workspaces so agents work in parallel without modifying the original checkout. ThinkRail shows branches, pull requests, CI checks, diffs, terminals, and review state. Chats can share plans, delegate to subagents, and continue work from project-free scratch chats.

The project keeps a connected graph of `SPEC.md` files beside the code. Dedicated tools let the agent read, search, and maintain specifications, so product intent and module boundaries persist across sessions. The README describes spec-first development: contract or boundary changes should update the relevant specification in the same change.

## Agent Host And Controls

ThinkRail runs `pi` in-process and owns the workspace manager, GUI, and typed engine/UI contracts. It loads existing `pi` configuration, skills, MCP servers, providers, and custom OpenAI-compatible model servers. Repository-defined MCP servers remain disabled until approved, and ThinkRail asks before calling servers that do not declare themselves read-only.

## Practical Takeaway

ThinkRail is an IDE-level harness that makes isolation, durable specifications, and reviewable Git changes first-class. Its distinctive combination is a rich desktop/browser surface around an existing coding agent rather than a replacement model runtime.

## See Also

- [OpenHands Agent Canvas](openhands-agent-canvas.md)
- [Superset](superset.md)
- [Statewright](statewright.md)
- [Codebase Memory and Code Graphs](../agent-memory-systems/codebase-memory-and-code-graphs.md)
