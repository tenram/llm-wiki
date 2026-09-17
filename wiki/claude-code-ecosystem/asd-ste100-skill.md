# ASD-STE100 Skill

> Sources: danyuchn, Unknown date
> Raw: [ASD-STE100 Skill](../../raw/claude-code-ecosystem/2026-09-17-asd-ste100-skill.md)

## Overview

A Claude Code skill that rewrites dense, ambiguous English into ASD-STE100 Simplified Technical English (STE) — the controlled-language standard the aerospace and defense industry built so aircraft maintenance instructions cannot be misread. Repurposed for the machine-to-machine case: an AI agent parsing another agent's output, a tool description, an error message, or an inter-agent instruction, with no human in the loop to resolve ambiguity.

## Why STE for agents

The same failure mode motivates both audiences: a misread instruction can kill people (aircraft) or silently corrupt downstream behavior (agents). STE's rules — one meaning per word, active voice, simple tenses, one instruction per sentence, short sentences, no dropped words — apply directly to agent-facing text. An agent parsing another agent's output has no back-channel to ask "did you mean X or Y?"

## What it does

Two modes: **Strict** (procedures, error messages, tool descriptions) and **STE-flavored** (READMEs, PR descriptions, explanatory prose — sentence discipline without the fixed-vocabulary lockdown). The skill flags rule violations sentence-by-sentence (ambiguity, complex tenses, passive voice with unclear actor, multi-instruction sentences, oversized noun clusters, dropped words, over-length sentences, phrasal verbs, nominalizations, semicolons, hedge stacks, marketing adjectives) and rewrites each without dropping any fact, condition, or scope qualifier. A deterministic `ste-lint.py` linter checks structural patterns only; the ASD ~900-word approved dictionary is not reproduced because the standard is not free to redistribute.

## Scope

Built for agent-to-agent messages, tool/function descriptions, error messages, system prompts, inter-agent instructions. Not for creative writing or marketing copy. Fixes the form of a text, not its substance.

## See Also

- [Anthropic Agent Skills](anthropics-skills.md)
- [Agent Skills Engineering Workflows](agent-skills-engineering-workflows.md)
- [Awesome Claude Skills](awesome-claude-skills.md)