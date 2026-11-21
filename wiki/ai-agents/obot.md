# Obot

> Sources: Obot AI, Unknown date
> Raw: [Obot README](../../raw/ai-agents/2026-10-19-obot.md)

## Overview

Obot is an open-source AI governance platform for organizations that need controlled access to models, MCP servers, skills, agents, credentials, and hosted workloads. Its central design is a governed platform that connects AI clients on user devices to Obot-managed gateways, registries, sandboxes, identity controls, and correlated audit logs.

## Platform Architecture

Obot Server provides MCP and LLM gateways, sandboxed execution, identity and access management, secrets, registries, and audit services. On managed devices, Obot Sentry inventories AI clients and tools, installs hooks, and records or enforces policy on local activity. The Obot CLI lets users and clients discover and install approved MCP servers and skills.

The MCP Gateway is a single controlled entry point for permitted MCP servers. It can proxy hosted or external servers, compose selected tools, apply user or identity-provider-group access rules, manage OAuth and credentials, and inspect or modify requests and responses through MCP or webhook filters. The LLM Gateway provides provider-compatible endpoints while keeping provider credentials in Obot, restricting model access through policies, and recording requests, responses, token usage, costs, client metadata, and sessions.

## Registries, Sandboxing, And Audit

Git-backed MCP and Skills registries centralize catalog curation and distribution. Policies can apply to individual entries, repositories, or complete catalogs. Hosted `npx`, `uvx`, and containerized servers or agents run in isolated Docker or Kubernetes environments, with domain-based egress controls where configured.

Obot correlates MCP, LLM, hosted-workload, and device-side activity. The README describes filtering by user, server, tool, provider, model, client, device, and session, plus one-time or scheduled export. This makes governance and observability first-class platform functions rather than add-ons to an individual agent.

## Deployment Boundary

The documented Docker quick start mounts the host Docker socket so Obot can launch sibling containers. The README limits this setup to development, evaluation, or trusted single-tenant environments and recommends Kubernetes for production or multi-tenant deployments. That distinction is a concrete trust-boundary warning, not merely a deployment preference.

## Practical Takeaway

Obot addresses the organizational control plane around heterogeneous AI clients. It is most relevant when the requirement is to govern model and tool access across users and devices, not simply to build one agent. Its design complements, rather than replaces, client-side agent frameworks and MCP servers.

## See Also

- [Model Context Protocol (MCP)](../browser-and-mcp-tooling/model-context-protocol-overview.md)
- [Harness Design Principles](../ai-agent-harnesses/harness-design-principles.md)
