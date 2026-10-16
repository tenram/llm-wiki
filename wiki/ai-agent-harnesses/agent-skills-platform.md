# Agent Skills Platform

> Sources: Francy J G Lisboa (Charuto), Unknown date
> Raw: [Agent Skills Platform (FrancyJGLisboa)](../../raw/ai-agent-harnesses/2026-10-16-agent-skills-platform.md)

## Overview

Agent Skills Platform (MIT, v6.1.0, ~2.4k stars) turns a real workflow into a tested, installable agent skill and then governs its lifecycle through a user-defined marketplace: evidence, discovery, updates, rollback, quarantine, and distribution to 17 platforms. It is built on the open Agent Skills standard (agentskills.io). Where most skill tooling stops at authoring, this project treats a skill as a governed, versioned, organization-owned artifact.

## From Workflow to Skill

The user gives a prompt plus the evidence behind the work (spreadsheets, reports, emails, screenshots, transcripts, links, or scripts). The creator asks only for the business decisions a human must authorize, then builds and tests the skill and shows a representative result. The output is not just a prompt: an installable skill package with instructions, functional scripts when needed, evals, security checks, a representative-run record, and a correction path.

## Governance Model

Two paths: a private "just for you" install, or a governed team marketplace (GitHub/GitLab) that inherits real ownership and approval rules. Work moves through four roles — the SME supplies examples and approves business meaning; the creator builds and verifies; the marketplace operator governs and publishes; colleagues install an approved version. The SME owns meaning; the operator owns distribution and policy.

The marketplace provides ownership, approvals, versioned releases, discovery, rollback, quarantine, and compatibility evidence. For Claude Code and Codex the marketplace can certify a skill from real agent runs (`reliability`), running the skill inside each installed runtime k times and certifying only what an agent actually discovered and followed (the "Caliper" pilot).

## Verification as a Connected System

Every skill is checked as one connected system: the skill graph links instructions, scripts, evaluations, and expected outputs. Two structural requirements enforce that every expected result is reachable (`every_expected_is_reachable`) and every predictable multi-step workflow has one reliable entry point (`deterministic_multistep_has_orchestrator`). Four checks run in parallel — specification, pipeline, security, and evaluation schema — and a representative run proves the skill produces a useful result.

## Governed Maintenance, Not Self-Modification

After release, classified run evidence is captured in `raw/`, recurring findings become evidence-linked draft patterns in `wiki/`, and only a separately validated change may update the executable skill. The project is explicit that this is a governed maintenance record, not autonomous self-modification.

## Conceptual Framing

The README draws a clean division of labor: "RAG supplies knowledge. MCP supplies capabilities. The harness supplies execution. A skill organizes them into a governed path toward a verified outcome." A skill is not itself a RAG system, MCP server, or agent runtime — it can use all three. Reason where interpretation is necessary; execute and verify with deterministic controls where reproducibility matters; external models and changing data may vary rather than promising identical outputs.

## Distribution Surfaces

Plugins ship for `.claude-plugin`, `.codex-plugin`, and `.cursor-plugin`, plus `gemini-extension.json`, `install.sh`, and `install.ps1`; a desktop app lets non-technical teammates browse and install skills with no terminal, Python, or Git. Semantic Recon runs automatically when a workflow touches an API, database, MCP, codebase, or structured file, producing a pinned data contract (skippable with `--without-semantic-recon` for local, source-free installs).

## See Also

- [Anthropic Agent Skills](../claude-code-ecosystem/anthropics-skills.md) — the `SKILL.md` format spec and agentskills.io standard this platform builds on.
- [Hermes Skills Ecosystem](hermes-skills-ecosystem.md) — another layered skill distribution model (built-in / optional / community).
- [Awesome Claude Code](../claude-code-ecosystem/awesome-claude-code.md) — discovery resource for the broader Claude Code skill/plugin ecosystem.
