# Omnigent

> Sources: omnigent-ai, Unknown date
> Raw: [omnigent repository](../../raw/ai-agent-harnesses/2026-11-15-omnigent.md)

## Overview

Omnigent is an agent harness and testing repository whose supplied documentation focuses on running local servers and exercising real agent backends through reproducible end-to-end scenarios. The snapshot includes harnesses for Antigravity, Copilot, and CLI setup flows.

## Harness testing model

The documented workflow starts a local server and runner, launches the target CLI or SDK harness, drives a real turn, and checks observable behavior. Separate skills cover native Antigravity RPC and tmux delivery, the Antigravity SDK path, Copilot SDK flows, and a PTY-based CLI onboarding loop.

## Safety and repeatability

The tests isolate configuration, data directories, OAuth copies, bridge state, and MCP relay credentials. The documentation requires targeted scenarios, smoke tests, bug-bash passes, and explicit teardown. It also calls out sharp edges such as session state, launch arguments, and differences between native and SDK harnesses.

## Practical takeaway

Omnigent treats a coding-agent harness as a system boundary that must be tested through its real server, runner, terminal, authentication, and tool bridge. Its main contribution is a repeatable verification loop rather than a model or prompt recipe.

## See Also

- [Harness Design Principles](harness-design-principles.md)
- [Ruvnet Agent Ecosystem](ruvnet-agent-ecosystem.md)
