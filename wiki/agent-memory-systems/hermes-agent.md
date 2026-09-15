# Hermes Agent (Nous Research)

> Sources: Nous Research, Unknown date
> Raw: [Hermes Agent: Overview](../../raw/agent-memory-systems/2026-07-21-hermes-agent-nousresearch.md)

## Overview

Hermes Agent is an open-source (MIT), self-hosted desktop AI agent from Nous Research, available on macOS, Windows, and Linux. It is built around a single design goal: an agent that grows with the user over time, learning from projects and interactions while staying reachable across whichever surface the user happens to be on.

## Capabilities

- **Multi-platform, unified memory**: runs across Telegram, Discord, Slack, WhatsApp, Signal, email, and CLI (a growing list), sharing one memory across all of them rather than siloing state per channel.
- **Persistent memory with auto-generated skills**: learns user projects and "never forgets how it solved a problem," accumulating reusable skills from past sessions.
- **Natural-language automation**: scheduled reports, backups, and briefings run unattended through the gateway.
- **Subagent delegation**: isolated subagents get their own conversations, terminals, and Python RPC scripts for parallel task execution.
- **Web and multimodal tools**: web search, browser automation, vision, image generation, text-to-speech, multi-model reasoning.
- **Sandboxed execution**: five backends (local, Docker, SSH, Singularity, Modal) with container hardening and namespace isolation.

## Nous Research Connection

Maintained by Nous Research and integrated with their Nous Portal subscription, which provides access to 300+ AI models and monthly usage credits for running the agent.

## See Also

- [OpenClaw](../ai-agent-harnesses/openclaw.md) — a comparable open-source, multi-platform, persistent-memory agent framework; Hermes Agent's subagent/sandbox model is more elaborate, OpenClaw's Markdown-workspace configuration is more transparent/editable.
