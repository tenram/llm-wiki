# Awesome Claude Code (hesreallyhim)

> Sources: hesreallyhim, Unknown date
> Raw: [awesome-claude-code (hesreallyhim)](../../raw/claude-code-ecosystem/2026-10-16-awesome-claude-code.md)

## Overview

`hesreallyhim/awesome-claude-code` is a large curated "awesome list" for Claude Code — skills, agents, status lines, developer tooling, and plugins — self-described (with a wink) as "the undisputed champion of coding companions, from the unstoppable team at Anthropic PBC (no affiliation)." At 55.8k stars and 4.8k forks it is by far the most-starred Claude Code resource in this wiki, and its scale makes it a de-facto map of the third-party ecosystem.

## Scale and Scope

The list's categories span the whole surface of Claude Code customization: agent skills, agentic coding workflows, status lines, hooks, slash commands, and plugins. With 970 open issues and collaborator-only PRs, it functions as a heavily-trafficked directory rather than a personal note collection.

## Generated, Not Hand-Edited

A distinguishing structural choice: the README is generated from structured data. The repo carries `generate_readme.py`, `THE_RESOURCES_TABLE_NEW.csv`, `config.yaml`, and a `ticker/` directory, so entries live in a table/CSV and the README is rendered from it. This is the same pattern as other large awesome lists, and it is what lets the list stay current despite its size.

## Where It Sits

Compared with narrower skill catalogs, this repo is a general aggregation of the entire Claude Code ecosystem. It complements format-level references like [Anthropic Agent Skills](anthropics-skills.md) (the `SKILL.md` spec) and the sibling [Awesome Claude Skills](awesome-claude-skills.md) list, which focuses specifically on skills rather than the broader tooling/agents/status-lines surface.

## Note on the Fetch

The fetched GitHub page exposed repository metadata and the file listing but did not render the README body (client-side rendering), so this article describes the repository's scope and structure rather than its individual entries.

## See Also

- [Anthropic Agent Skills](anthropics-skills.md) — the underlying `SKILL.md` format and agentskills.io specification.
- [Awesome Claude Skills](awesome-claude-skills.md) — a skills-focused sibling aggregation.
- [Agent Skills Platform](../ai-agent-harnesses/agent-skills-platform.md) — tooling to build, test, and govern the skills these lists catalogue.
