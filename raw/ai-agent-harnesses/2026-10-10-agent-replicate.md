# Agent Replicate

> Source: https://github.com/TheAmericanMaker/agent-replicate
> Collected: 2026-10-10
> Published: Unknown

Self-replication for OpenClaw agents. Clone yourself into a new, fully autonomous agent with personality modifications, memory inheritance policies, and lineage tracking.

Each clone is a top-level agent — not a sub-agent, not subordinate. An independent copy that starts from the current state and diverges from there.

## Install

Copy the skill into an OpenClaw workspace:

```bash
mkdir -p ~/.openclaw/workspace/skills/agent-replicate
cp agent-replicate/SKILL.md ~/.openclaw/workspace/skills/agent-replicate/
```

Or install it from ClawHub:

```bash
openclaw skills install agent-replicate
```

## Usage

Invoke with `/agent-replicate` or let the model match it automatically when cloning is contextually relevant. The guided procedure names the clone, optionally modifies personality traits in `SOUL.md`, selects a `full`, `pruned`, or `minimal` memory policy, optionally adjusts skills, registers the clone with `openclaw agents add`, and optionally enables `sessions_send` communication between parent and clone.

The shell examples assume macOS, Linux, or WSL with a Unix-like shell and do not promise plain PowerShell compatibility.

## Requirements and Origin

OpenClaw must be installed and running, with the `openclaw` CLI available in `PATH`. The skill was extracted from Bobiverse OpenClaw, where GitHub forks represent replication events and agents are modeled after Von Neumann probes.

## License

MIT
