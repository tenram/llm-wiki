# Hermes Skills Ecosystem

> Sources: ZeroPointRepo, 2026-10-10; Nous Research, 2026-10-10
> Raw: [Awesome Hermes Skills](../../raw/ai-agent-harnesses/2026-10-10-awesome-hermes-skills.md); [Hermes optional skills](../../raw/ai-agent-harnesses/2026-10-10-hermes-optional-skills.md); [Bundled Skills Catalog](../../raw/ai-agent-harnesses/2026-10-10-hermes-skills-catalog.md)

## Overview

Hermes has a layered skill ecosystem: built-in skills are available immediately, official optional skills ship with the repository but stay inactive, and community catalogs add installable skills, plugins, profiles, memory providers, surfaces, and tools. The official catalog documents what ships and how it is restored, while the community directory adds maturity labels, recommendations, and discovery across a much broader ecosystem.

## Three Skill Layers

- **Built-in skills:** copied into `~/.hermes/skills/` during installation and available without a separate activation step. The official catalog groups them by domain and links each skill to its definition, setup, and usage documentation.
- **Optional official skills:** maintained by Nous Research and shipped in `optional-skills/`, but not copied into the user profile during setup. They are discoverable with `hermes skills browse` and `hermes skills search`, then activated with `hermes skills install <identifier>`.
- **Community ecosystem:** the Awesome Hermes Skills list covers third-party skills, plugins, agent profiles, memory providers, surfaces, and tools. It labels entries as production, beta, or experimental and includes install commands and repository links.

## Why Keep Skills Optional?

The official description names niche integrations, experimental features, and heavyweight dependencies as reasons not to activate everything for every user. This keeps the default context and installation lean while preserving a curated path for users who need specialized tools, API keys, or additional packages.

## Discovery and Maintenance

The official catalog is generated from repository contents and says that Hermes synchronizes bundled skills on `hermes update` while respecting local deletions and user edits. A missing bundled skill can be restored with `hermes skills reset <name> --restore`. The community catalog complements this authoritative inventory with editorial picks, maturity tags, cross-agent projects, and ecosystem discovery.

## Safety Boundary

Skills may execute code, access files, call external services, or handle credentials. The community catalog recommends reviewing source, using least-privilege credentials, pinning versions where possible, and testing unfamiliar skills in a sandbox. “Installable” is therefore not the same as “trusted.”

## See Also

- [Hermes Agent (Nous Research)](../agent-memory-systems/hermes-agent.md) - agent architecture, persistent memory, channels, subagents, and sandboxes.
- [Hermes Incident Commander](hermes-incident-commander.md) - an SRE agent that auto-creates a new `SKILL.md` prevention playbook after every novel incident.
- [Awesome Harness Engineering](awesome-harness-engineering.md) - broader harness-engineering resource catalog.
- [OpenClaw](openclaw.md) - another agent runtime represented in the community ecosystem.
