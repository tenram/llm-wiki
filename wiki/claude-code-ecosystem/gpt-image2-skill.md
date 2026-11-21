# GPT Image 2 Skill

> Sources: wuyoscar, Unknown date
> Raw: [GPT-Image2-Skill](../../raw/claude-code-ecosystem/2026-11-15-gpt-image2-skill.md)

## Overview

GPT-Image2-Skill is a gallery-first, CLI-first agent skill for generating and editing images with GPT Image models. It pairs a large reference gallery with a packaged command-line tool, bilingual documentation, installation guidance, and optional animation workflows.

## Gallery and attribution

The repository organizes examples by visual task and asks contributors to keep English and Chinese galleries aligned. New entries must preserve numbering, local image paths, category structure, prompt text, and attribution for prompts sourced outside the repository.

## Operational safeguards

The documented workflow checks existing installation state before changing it, treats global installs as opt-in, and keeps API keys out of files unless explicitly requested. The CLI includes generation, editing, model selection, and GIF-related workflows; offline tests and smoke checks are part of the repository's verification story.

## Practical takeaway

The skill treats examples as a searchable prompt interface, not as decoration. The useful unit is the combination of intent analysis, gallery lookup, prompt construction, and a reproducible CLI invocation.

## See Also

- [Impeccable](impeccable.md)
- [Agent Skill Collections](agent-skill-collections.md)
