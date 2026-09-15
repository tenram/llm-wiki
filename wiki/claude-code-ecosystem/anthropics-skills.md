# Anthropic Agent Skills

> Sources: Anthropic, Unknown date; agentskills.io, Unknown date; Bibek Poudel, Unknown date
> Raw: [anthropics/skills](../../raw/claude-code-ecosystem/anthropics-skills.md); [Specification](../../raw/claude-code-ecosystem/2026-07-13-agent-skills-specification.md); [The SKILL.md Pattern](../../raw/claude-code-ecosystem/skill-md-pattern.md)

## Overview

Anthropic's own reference repository for "Agent Skills": folders containing a `SKILL.md` (YAML frontmatter with `name`/`description`, plus instructions, examples, guidelines) that Claude loads dynamically for specialized tasks, rather than keeping all capability in the base system prompt. The format has since been documented as an open specification at agentskills.io, independent of Anthropic's own repo, describing the same `SKILL.md` structure in formal terms.

## Structure

`./skills` holds example skills grouped by Creative & Design, Development & Technical, Enterprise & Communication, and Document Skills (PDF/DOCX/PPTX/XLSX). `./spec` defines the Agent Skills specification itself; `./template` provides a starter skill. Installable in Claude Code via `/plugin marketplace add anthropics/skills`, and usable in Claude.ai (paid plans) or the Claude API.

Licensing is split: most example skills are Apache 2.0; the document skills are source-available rather than open source, shared as reference implementations only, with an explicit disclaimer that Claude's actual behavior may differ from the reference code.

This is the canonical spec that third-party skill projects (academic-research-skills, ui-ux-pro-max-skill, article-writing-skills) build on top of.

## Format specification

A skill directory requires at minimum a `SKILL.md` file, and may optionally include `scripts/` (executable code), `references/` (documentation loaded on demand), and `assets/` (templates, images, data files).

`SKILL.md` is YAML frontmatter followed by an unrestricted Markdown body. Frontmatter fields:

| Field | Required | Constraints |
|---|---|---|
| `name` | Yes | Max 64 chars; lowercase alphanumeric + hyphens; no leading/trailing/consecutive hyphens; must match parent directory name |
| `description` | Yes | Max 1024 chars, non-empty; should state what the skill does and when to use it, with keywords that help agents match tasks |
| `license` | No | License name or reference to a bundled license file |
| `compatibility` | No | Max 500 chars; environment requirements (product, system packages, network access) |
| `metadata` | No | Arbitrary string-to-string key-value map for client-specific properties |
| `allowed-tools` | No, experimental | Space-separated list of pre-approved tools, e.g. `Bash(git:*) Bash(jq:*) Read` |

The body has no format restrictions but recommended sections are step-by-step instructions, input/output examples, and edge cases. Because the whole `SKILL.md` body loads once a skill activates, longer content should be split into `references/` files, keeping `SKILL.md` itself under roughly 500 lines and file references one level deep (avoid nested reference chains).

### Progressive disclosure

Skills load in three tiers of increasing cost:

1. **Metadata** (~100 tokens): `name` + `description` loaded at startup for every skill, used for activation matching
2. **Instructions** (<5000 tokens recommended): full `SKILL.md` body loaded only once the skill activates
3. **Resources**: `scripts/`, `references/`, `assets/` files loaded only when the task actually needs them

This tiering is the mechanism that lets a large skill library exist without bloating the base context window.

### Validation

The `skills-ref` reference library (github.com/agentskills/agentskills) validates a skill directory's frontmatter and naming conventions via `skills-ref validate ./my-skill`.

## Practitioner Framing: The Description Is the Trigger

Bibek Poudel's summary of the pattern restates the spec in blunter, activation-focused terms: "if your skill does not trigger, it is almost never the instructions. It is the description." The `description` field has to carry both a plain statement of what the skill does and the specific phrases users are likely to type, not just abstract capability language — because it's the only field loaded for every skill at every turn (the metadata tier of progressive disclosure). This reframes progressive disclosure less as a context-budget optimization and more as a trigger-reliability requirement: an under-specified description doesn't just cost tokens, it silently fails to activate.

## See Also

- [Academic Research Skills](academic-research-skills.md)
- [UI UX Pro Max Skill](ui-ux-pro-max-skill.md)
- [article-writing-skills](article-writing-skills.md)
- [Agent Skills Engineering Workflows](agent-skills-engineering-workflows.md)
- [Awesome Claude Skills](awesome-claude-skills.md)
