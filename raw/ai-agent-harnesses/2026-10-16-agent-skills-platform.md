# Agent Skills Platform (FrancyJGLisboa)

> Source: https://github.com/FrancyJGLisboa/agent-skills-platform
> Collected: 2026-10-16
> Published: Unknown

## About

Build tested agent skills and govern their lifecycle through a user-defined marketplace: evidence, discovery, updates, rollback, quarantine, and 17-platform distribution.

- Repository: FrancyJGLisboa/agent-skills-platform
- License: MIT (Copyright © 2026 Francy J G Lisboa, also known as Charuto)
- Stars: 2.4k; Forks: 272; Watching: 12; Commits: 214; Version: 6.1.0
- Topics: agent-skills, ai-agents, claude-code, codex, cursor, developer-tools, evals, github-copilot, governance, skill-marketplace
- Site: https://francyjglisboa.github.io/agent-skills-platform/
- Built on the Agent Skills Open Standard (agentskills.io specification)

## README

**Turn a real workflow into a tested, installable agent skill—then publish it safely to your team.**

Agent Skills Platform turns the way people already work into tested, installable agent skills. Give it a prompt plus the evidence behind the work—spreadsheets, reports, emails, screenshots, transcripts, links, or scripts—and it builds a reusable workflow that a person can inspect, an organization can review, and a team can safely reuse.

Example prompt:

```
/agent-skills-platform

Turn my monthly revenue-variance review into a reusable internal skill.
I attached past reports and the source spreadsheets. The decision is whether to
escalate a material variance. It must not modify source data.
```

The result is not just a prompt: it is an installable skill package with instructions, functional scripts when needed, evals, security checks, a representative-run record, and a correction path for real-world learning.

After release, a skill can retain maintenance evidence without turning every log into runtime prompt context: classified run evidence is captured in `raw/`, recurring findings become evidence-linked draft patterns in `wiki/`, and only a separately validated change may update the executable skill. This is a governed maintenance record, not autonomous self-modification.

### Create your first skill

First question: is this skill just for you, or will teammates install or reuse the skill itself?

- **Just for you** — create, verify, and install it privately. No marketplace setup.
- **My team** — create or select a governed GitHub/GitLab marketplace first, so the skill inherits real ownership and approval rules.

Teammates receiving a report or queue does not require a marketplace. Use the team path only when teammates will install or reuse the skill.

**I have a workflow — no code required.** Open the AI agent you already use, attach examples of the work, and paste the prompt. The creator asks for the business decisions only you can authorize, builds and tests the skill, and shows a representative result. When it is correct: "Publish this to the Finance marketplace." When the workflow uses an API, database, MCP, codebase, or structured file, Semantic Recon runs automatically before implementation and creates a pinned data contract. Use `./install.sh --without-semantic-recon` only for a deliberately local, source-free installation.

**My teammates just need to install skills.** Give them the desktop app: download, paste the team-library link, click Install. Skills land in GitHub Copilot (or the tool they pick) with no terminal, Python, or Git involved.

**I run the marketplace.** Use the governed team marketplace guide to admit, approve, release, distribute, update, quarantine, and roll back tested skills.

**I am evaluating the platform.** Read the product scope, organizational acceptance protocol, and technical implementation guide.

### Why teams use it

- **Preserve expert judgment.** A skill captures the question, evidence, decision, and success measure behind recurring work.
- **Trust what is shared.** Skills carry validation, security checks, evals, and a representative run before they are published; for Claude Code and Codex the marketplace can also certify a skill from real agent runs (`reliability`).
- **Learn without runtime bloat.** Maintenance keeps evidence, draft patterns, and rejected changes separate from the concise instructions an agent executes.
- **Govern team use.** The marketplace provides ownership, approvals, versioned releases, discovery, rollback, quarantine, and compatibility evidence.

### How work moves through the organization

```
SME supplies examples and approves the result
        ↓
Creator builds and verifies a skill
        ↓
Marketplace operator governs and publishes it
        ↓
Colleagues install an approved version and use it
```

The SME owns business meaning. The marketplace operator owns distribution and policy.

### What happens behind the scenes

An Agent Skill is a reusable workflow package that guides an agent from a recognized situation to a verified outcome. It can use retrieved knowledge, MCP tools, APIs, deterministic scripts, and agent judgment, but it is not itself a RAG system, MCP server, or agent runtime.

"RAG supplies knowledge. MCP supplies capabilities. The harness supplies execution. A skill organizes them into a governed path toward a verified outcome."

Reason where interpretation is necessary. Execute and verify with deterministic controls where reproducibility matters. External models, APIs, and changing data may vary rather than promising identical outputs.

Humans establish meaning. The flow is: messy problem → agent inspects evidence → proposed/conflicting meanings → human authority decision → interview READY → build, prove, publish.

Every skill is checked as one connected system. The skill graph links its instructions, scripts, evaluations, and expected outputs. Two structural requirements confirm that every expected result is tested and every predictable multi-step workflow has one reliable entry point. Four checks—specification, pipeline, security, and evaluation schema—run in parallel. Finally, a representative run proves that the skill produces a useful result. The graph also enforces `every_expected_is_reachable` and `deterministic_multistep_has_orchestrator`. After intake, `team_marketplace.py reliability` can run the skill inside each installed agent runtime k times and certify only what an agent actually discovered and followed (Caliper).

## Repository layout (top-level)

`.agents`, `.claude-plugin`, `.codex-plugin`, `.cursor-plugin`, `.github`, `.hallmark`, `assets`, `desktop`, `docs`, `exports`, `gates`, `references`, `registry`, `scripts`, plus `AGENTS.md`, `CHANGELOG.md`, `CITATION.cff`, `GATES.md`, `LAUNCH.md`, `LEARNINGS.md`, `PLAN.md`, `README.md`, `SKILL.md`, `discovery.json`, `gemini-extension.json`, `install.sh`, `install.ps1`, `pytest.ini`, `ruff.toml`.

## Related docs referenced

Website; Installation (docs/INSTALL.md); Worker runbook (docs/WORKER_RUNBOOK.md); Team marketplace (docs/TEAM_MARKETPLACE.md); Product scope (docs/PRODUCT_SCOPE.md); Desktop app (docs/DESKTOP_APP.md); Caliper pilot (docs/CALIPER.md); Technical overview (docs/TECHNICAL_OVERVIEW.md); Organizational acceptance (docs/ORGANIZATIONAL_ACCEPTANCE.md).
