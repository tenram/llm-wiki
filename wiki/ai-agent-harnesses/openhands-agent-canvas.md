# OpenHands Agent Canvas

> Sources: OpenHands, Unknown date
> Raw: [OpenHands README](../../raw/ai-agent-harnesses/2026-11-10-openhands-agent-canvas.md)

## Overview

OpenHands Agent Canvas is a self-hosted developer control center for running coding agents and automations across local, remote, and cloud backends. It can run OpenHands, Claude Code, Codex, Gemini, Pi, OpenCode, or other Agent-Client Protocol-compatible agents.

## Control-Center Model

Canvas provides a frontend for conversations, backend selection, workspace access, and scheduled or event-triggered automations. Integrations include services such as Slack, GitHub, Notion, and other automation targets. The OpenHands Agent Server supplies the REST execution API; the Canvas frontend can connect to multiple agent servers.

The project supports local execution, Docker sandboxes, multiple per-conversation Docker sandboxes, and source development. It exposes a local web interface and can connect to agent servers running on laptops, dedicated machines, virtual machines, or OpenHands infrastructure.

## Security And Deployment Boundary

The README explicitly distinguishes unsandboxed local execution, which gives the agent full filesystem access, from Docker-based isolation. It recommends loopback binding for local launchers and warns about session-key exposure when publishing Docker on a LAN or public interface. Production self-hosting requires following the project’s security-hardening guidance.

## Practical Takeaway

Agent Canvas is a multi-agent control surface and automation host, not merely a coding-agent model or SDK. Its main architectural choice is to separate the UI/control center from replaceable agent backends and execution environments.

## See Also

- [Paperclip](paperclip.md)
- [ThinkRail](thinkrail.md)
- [Superset](superset.md)
- [Statewright](statewright.md)
