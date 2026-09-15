# OpenClaw

> Sources: OpenClaw project, Unknown date; blog.gopenai.com, Unknown date; @lacneu (npm), 2026-05-03
> Raw: [OpenClaw: Complete Overview](../../raw/ai-agent-harnesses/2026-07-21-openclaw-guide.md); [Adding WhatsApp Integration to OpenClaw](../../raw/ai-agent-harnesses/openclaw-whatsapp-integration.md); [@lacneu/wix-openclaw](../../raw/ai-agent-harnesses/wix-openclaw-plugin.md)

## Overview

OpenClaw is an open-source, self-hosted agent framework that wraps an LLM (Claude, GPT, or a local model via Ollama) with real system access — file read/write, shell execution, web fetch, browser automation — plus durable memory and proactive scheduling, turning a stateless chatbot into a persistent assistant.

## Architecture

Three layers: **Tools** (the capabilities: read, write, edit, exec, web_fetch, browser automation), **Config** (which tools are permitted), and **Skills** (Markdown instruction files teaching specific workflows). All agent behavior is defined by editable, version-controllable workspace files rather than opaque databases:

- `SOUL.md` — personality and values
- `AGENTS.md` — operating instructions and priorities
- `USER.md` — user preferences and context
- `MEMORY.md` + `memory/` — persistent, searchable knowledge base
- `HEARTBEAT.md` — proactive monitoring tasks, checked on a default 30-minute interval

## Setup

Requires Node.js 22+ and an LLM API key. Install with `npm install -g openclaw@latest` then `openclaw onboard --install-daemon`. A local Gateway (port 18789) manages agent lifecycle, sessions, and routes messages across supported channels: Telegram, Discord, Slack, WhatsApp, and others.

## Use Cases

Autonomous system monitoring with proactive alerting, personalized daily briefings and email summarization, git-based standup generation, server health monitoring, and cross-platform assistant duty via a single local Gateway.

## Security Considerations

Because the agent has real shell access, the project recommends running it on a dedicated VPS rather than a personal machine in production, binding the Gateway to localhost, enabling token authentication, requiring explicit consent for destructive commands, and vetting third-party skills before installing them.

## WhatsApp Channel Setup

Wiring up the WhatsApp channel runs through `openclaw onboard`'s interactive wizard: accept disclaimers, pick QuickStart mode, configure model auth, then select WhatsApp and scan a QR code to link. Dedicated (non-personal) accounts require approving a pairing code server-side via `openclaw pairing approve whatsapp <code>`. The guide warns that enabling certain optional command-completion features can spike server CPU usage.

## Third-Party Plugin Example: Wix Management

`@lacneu/wix-openclaw` (npm, MIT) is a third-party OpenClaw plugin registering ~50 tools across a dozen Wix products (blog, CMS, forms, bookings, contacts, events, reviews), wrapping the official Wix REST API. It illustrates the guardrails a real third-party OpenClaw plugin needs beyond the core project's own recommendations: a site-UUID whitelist to prevent cross-site accidents, explicit approval gating for destructive operations (publish, delete, cancel), and exponential backoff on rate limits — concrete implementations of "vet third-party skills" and "require explicit consent for destructive commands" above.

## See Also

- [Hermes Agent](../agent-memory-systems/hermes-agent.md) — a similarly-structured open-source, multi-platform, persistent-memory desktop agent from Nous Research; compare architectures.
- [Statewright](statewright.md) — a different approach to constraining agent behavior via state-machine tool restriction rather than Markdown-file configuration.
