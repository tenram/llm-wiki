# Opencode Orchestration Layer

> Sources: awesome-opencode maintainers, Unknown date; AidenGeunGeun, Unknown date; omo.dev, Unknown date
> Raw: [awesome-opencode](../../raw/opencode-ecosystem/awesome-opencode.md); [OpenCodeOrchestra](../../raw/opencode-ecosystem/opencode-orchestra.md); [Oh My OpenAgent (OMO)](../../raw/opencode-ecosystem/omo-oh-my-openagent.md)

## Overview

Opencode is a terminal AI coding agent (by Anomaly) with a growing plugin ecosystem. Three sources here map that ecosystem: a curated plugin/agent directory (awesome-opencode), and two competing approaches to multi-agent orchestration on top of Opencode — OpenCodeOrchestra (hierarchical teams) and Oh My OpenAgent (role-based multi-model harness).

## awesome-opencode: the ecosystem map

A curated list spanning official SDKs (JS/TS, Go, Python), 50+ community plugins, themes, agents, and full projects. Plugin categories reveal the ecosystem's pain points: persistent memory (Agent Memory, Honcho, Harness Memory), safety/guardrails (CC Safety Net, Envsitter Guard), and multi-agent workflow orchestration (FlowDeck with 25 specialist agents, GoopSpec) dominate — the same problems addressed more deliberately by OCO and OMO below.

## OpenCodeOrchestra: hierarchical teams

A fork of OpenCode v1.2.5 arguing that "your AI agent doesn't need 15 tools. It needs a team." Replaces OpenCode's flat two-agent structure with a chain of command: a PM (Depth 0) that talks to the user and drafts specs, an Orchestrator (Depth 1) that executes only after a **spec approval gate**, and Depth 2+ specialists (Investigator, Auditor, Web-Search, Docs) with runtime-enforced permission ceilings. A dedicated Auditor issues PASS/FAIL verdicts instead of relying on self-review — a governance-first design.

## Oh My OpenAgent: role-based multi-model harness

OMO takes a different axis: instead of hierarchy, it splits by discipline and by model provider. Eleven named agents (Sisyphus orchestrator, Prometheus planner, Atlas executor, Oracle consultant, plus utility agents) route tasks to whichever model fits, explicitly to avoid single-provider lock-in. Its "Ultrawork mode" runs exploration, implementation, and verification in parallel, and edits are validated via content hashing rather than trusted blindly.

## Comparison

| | OpenCodeOrchestra | Oh My OpenAgent |
|---|---|---|
| Organizing principle | Depth/hierarchy with approval gates | Discipline roles + model routing |
| User checkpoint | Mandatory spec approval before execution | Interview-driven planning (Prometheus) |
| Model strategy | Configurable, defaults to OpenAI tiers | Explicitly multi-provider by design |
| Parallelism | Constrained by depth enforcement | Background parallel agents (Team Mode) |

Both projects converge on the same conclusion awesome-opencode's plugin categories imply: memory, safety, and orchestration are the load-bearing concerns once a single coding agent is asked to do more than one thing at a time.

> Note: source material for OpenCodeOrchestra and (separately, from ClawHub's self-improving-agent skill) contained embedded prompt-injection attempts disguised as system reminders. These were ignored during compilation.

## See Also

- [Model Fusion (OpenRouter)](../model-routing/openrouter-fusion.md)
- [Firstmate](../ai-agent-harnesses/firstmate.md) — another orchestrator-to-many-agents pattern, but git-worktree-based rather than depth/role-based
