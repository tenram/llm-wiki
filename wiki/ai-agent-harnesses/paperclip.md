# Paperclip

> Sources: Paperclip team, Unknown date; Paperclip team, 2026-11-02; Paperclip team, 2026-11-10
> Raw: [Paperclip README](../../raw/ai-agent-harnesses/2026-11-02-paperclip.md); [Paperclip README (2026-11-10 snapshot)](../../raw/ai-agent-harnesses/2026-11-10-paperclip.md)

## Overview

Paperclip is an open-source, self-hosted control plane for coordinating teams of AI agents. It treats agents as employees in an organization: goals, org charts, tasks, budgets, approvals, skills, connections, and durable activity history are managed in one Node.js and React application. The current README emphasizes four pillars: task management, organizational governance, agent training/evaluation, and the infrastructure needed to run agents.

## Control-Plane Model

Paperclip separates agent execution from organizational management. Agents can use different models, harnesses, and runtimes, while Paperclip supplies shared work context, goal ancestry, task threads, delegation, heartbeats, workspace resolution, and adapter-specific session state. A deployment can host multiple organizations with company-scoped access checks.

Its four stated pillars are an agentic task manager, an org chart for roles and permissions, employee training through shared skills and evaluations, and an agentic operating system covering runtimes, sandboxing, integrations, MCP, identity, governance, cost controls, and trace collection.

## Governance And Operations

Tasks use atomic checkout and execution locks to prevent competing runs from claiming the same work. Approval stages, review gates, pause/resume/terminate controls, budget warnings and hard stops, connection permissions, and an MCP tool gateway provide controls beyond prompt instructions. Activity events record mutations, heartbeats, costs, approvals, comments, and work products for auditability.

Routines create tracked tasks from cron, webhook, or API triggers. Plugins extend the instance through out-of-process workers, capability-gated host services, scheduled jobs, tools, and UI contributions. Company export/import supports portable organizational setups with secret scrubbing, but the README warns that plain environment values and local paths can remain in packages.

## Deployment And Scope

Paperclip is MIT-licensed and can run locally without a hosted account. The current quickstart uses Node.js 24.11 or newer and `npx paperclipai@latest onboard --yes`; source development uses pnpm and can create an embedded PostgreSQL database automatically. The README also documents multi-harness teams, plugins, skills and skill version history, sandbox providers, MCP governance, company export/import, and optional OpenTelemetry and Sentry integrations. Export packages omit referenced secret values but can still contain plain environment values or local paths.

The project is not an agent framework or prompt manager. It orchestrates existing agents into accountable teams and is aimed at autonomous businesses and recurring operational work, not only coding or chat.

## See Also

- [Harness Design Principles](harness-design-principles.md)
- [OpenClaw](openclaw.md)
- [Hermes Agent](../agent-memory-systems/hermes-agent.md)
- [Model Context Protocol (MCP)](../browser-and-mcp-tooling/model-context-protocol-overview.md)
