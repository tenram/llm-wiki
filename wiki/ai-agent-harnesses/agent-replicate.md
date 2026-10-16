# Agent Replicate

> Sources: TheAmericanMaker, 2026-10-10
> Raw: [Agent Replicate](../../raw/ai-agent-harnesses/2026-10-10-agent-replicate.md)

## Overview

Agent Replicate is an OpenClaw skill for cloning an existing agent into a new top-level autonomous agent. It treats the clone as an independent copy rather than a subordinate sub-agent, and exposes explicit choices for personality changes, memory inheritance, skill specialization, registration, and parent-clone communication.

## Replication Flow

The guided flow names the clone, optionally modifies `SOUL.md` personality traits, selects a memory policy, adjusts the clone's skills, registers it with `openclaw agents add`, and optionally enables `sessions_send` communication. Memory policies are `full` for complete inheritance, `pruned` for retaining knowledge while clearing observations, and `minimal` for a clean start.

## Operational Boundary

The skill requires OpenClaw and its CLI. Its examples assume macOS, Linux, or WSL with a Unix-like shell. The source explicitly does not promise plain PowerShell compatibility. The project identifies itself as MIT licensed and traces its origin to Bobiverse OpenClaw, where forks represent replication events and agents follow a Von Neumann-probe metaphor.

## See Also

- [Hermes Skills Ecosystem](hermes-skills-ecosystem.md) - layered skill distribution and safety guidance for Hermes.
- [OpenClaw](openclaw.md) - the runtime targeted by Agent Replicate.
