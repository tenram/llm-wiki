# cmux

> Sources: Manaflow, 2026-10-10
> Raw: [cmux README](../../raw/ai-agent-harnesses/2026-10-10-cmux.md)

## Overview

cmux is a native macOS terminal workspace for AI coding agents, built with Swift/AppKit on Ghostty's libghostty renderer. It adds vertical tabs, split panes, agent-aware notifications, an embedded programmable browser, SSH workspaces, session restoration, and CLI/socket control without forcing an opinionated agent-orchestration workflow.

## Agent Workflow

cmux makes parallel terminal agents visible. Workspaces and panes expose git branches, linked PR status, working directories, listening ports, and recent notification text. Notification rings and unread badges identify panes where agents need input; OSC 9/99/777 sequences, `cmux notify`, and agent hooks can trigger those notifications. Claude Code teams can be launched with `cmux claude-teams`, with teammates represented as native splits instead of hidden background processes.

## Browser and Automation Surface

The embedded browser can be split beside a terminal and controlled through the CLI or Unix socket. The README describes accessibility-tree snapshots, element references, clicks, form filling, JavaScript evaluation, console/network inspection, screenshots, and URL navigation. This lets an agent inspect and verify a local web application without leaving the terminal workspace.

## Remote and Session Behavior

`cmux ssh user@remote` creates a remote workspace, and browser traffic can route through the remote network so remote localhost services remain usable. On quit and relaunch, cmux restores app-owned layout, working directories, scrollback where possible, and browser navigation state. It does not keep arbitrary processes alive. Optional local tmux or zellij owners provide live detach/reattach, while supported agent hooks can resume native sessions.

Imported session files are treated as untrusted. Layout and ordinary browsing state can be restored, but custom commands, sensitive environment values, non-HTTP pages, and unapproved resume commands are held back. This is a stronger boundary than blindly replaying a serialized workspace.

## Design Position

cmux describes itself as a primitive rather than a prescriptive orchestrator: it provides terminal, browser, notifications, workspaces, splits, tabs, and control APIs, while leaving agent workflow design to the user. That distinguishes it from GUI products that impose a project-management model. Its current platform scope is macOS, and its open-source application is GPL-3.0-or-later; the README separately identifies BSL-licensed server components.

## See Also

- [Superset](superset.md) - broader desktop IDE for parallel CLI agents, worktrees, review, previews, and remote access.
- [Munder Difflin](munder-difflin.md) - multi-agent desktop harness that coordinates terminal CLIs as a team.
- [Playwright MCP](../browser-and-mcp-tooling/playwright-mcp.md) - browser automation exposed through MCP rather than cmux's embedded browser and socket surface.
