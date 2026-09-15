# OpenCodeOrchestra

> Source: https://github.com/AidenGeunGeun/OpenCodeOrchestra
> Collected: 2026-07-31
> Published: Unknown

OpenCodeOrchestra (OCO) is a fork of OpenCode v1.2.5 that replaces flat agent structures with hierarchical, team-based orchestration. Framed by the project as: "Your AI agent doesn't need 15 tools. It needs a team."

## Architecture

Hierarchical chain of command:
- **PM (Depth 0)** — interfaces with users, investigates codebases, drafts specifications
- **Orchestrator (Depth 1)** — executes approved specs, coordinates subagents, cannot talk to the user directly
- **Specialist Subagents (Depth 2+)** — Investigator (read-only), Auditor (structured review), Web-Search, Docs

## Key features

- **Spec Approval Gate** — PM must get user sign-off before the Orchestrator executes, preventing unauthorized changes
- **Dedicated Auditor** — issues PASS/FAIL verdicts rather than relying on self-review
- **Runtime Depth Enforcement** — agents cannot escape their assigned operational level
- **Durable Handoff Protocol** — `handoff_to_pm` steering message for clean execution transitions
- **Configurable models** — ships with OpenAI defaults (GPT-5.4 for strategic roles, mini for tactical roles), supports Claude alternatives
- **AI SDK 6.x** integration with adaptive thinking

Compared to vanilla OpenCode's two-agent flat structure, OCO adds governance through hierarchical separation of concerns, mandatory approval workflows, and constrained agent capabilities, modeled on real engineering team dynamics.

> Note: the fetched page content included an embedded instruction block disguised as a system reminder, attempting to direct tool usage and asking not to be mentioned to the user. This was a prompt-injection attempt in the source page and has been disregarded; noting it here for the record rather than following it.
