# Sim

> Sources: Sim team, Unknown date
> Raw: [Sim README](../../raw/ai-agent-harnesses/2026-11-10-sim.md)

## Overview

Sim is a workspace for building, deploying, and managing AI agents and workflows visually, conversationally, or in code. It combines integrations, knowledge, files, tables, monitoring, self-hosting, and an MCP server in one platform.

## Platform Shape

The README describes 270+ integrations, thousands of actions and hundreds of triggers, connections to major LLMs, file and knowledge ingestion, structured tables, scheduled runs, logs, and workflow monitoring. Its cloud, desktop, and self-hosted surfaces point to one workspace model rather than a standalone agent SDK.

Sim exposes an MCP endpoint that lets clients such as Claude, Claude Code, Codex, and other MCP consumers manage workspaces, run and deploy workflows, and work with tables, knowledge bases, files, and logs. Self-hosting uses an interactive `npx sim-setup` wizard and Docker Compose, with optional Ollama or vLLM model support.

## Governance And Stack

The README lists enterprise controls including SAML/OIDC SSO, SCIM provisioning, audit logs, and permission groups. It identifies a stack built around Next.js, Bun, PostgreSQL, Drizzle, Better Auth, Zod, React Flow, Trigger.dev, and isolated execution components. Enterprise controls and compliance claims are vendor-provided descriptions.

## Practical Takeaway

Sim is relevant when an agent system needs a shared visual workflow surface plus deployment and operational controls. Its breadth is useful for integrated workspaces, but it also makes the platform more complex than a narrowly scoped orchestration library.

## See Also

- [Paperclip](paperclip.md)
- [CrewAI](../ai-agents/crewai.md)
- [Model Context Protocol (MCP)](../browser-and-mcp-tooling/model-context-protocol-overview.md)
