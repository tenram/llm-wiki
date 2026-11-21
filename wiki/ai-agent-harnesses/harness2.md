# Harness²

> Sources: Google Research, Unknown date
> Raw: [Harness² repository](../../raw/ai-agent-harnesses/2026-11-15-google-research-harness2.md); [2026-11-21 source snapshot](../../raw/ai-agent-harnesses/2026-11-21-harness2.md)

## Overview

Harness² is a framework for recursively improving the system around an agent while keeping model weights fixed. It targets open-world tasks that were not known when the original harness was designed, using task-level experimentation and a persistent improvement harness.

## Two recursion levels

At the task level, an agent executor runs an initial harness, a harness editor proposes invariant or domain-specific edits, probes execute candidate variants, and a composer combines behavioral contrasts into a refined harness. At the harnessing level, an experience reflector records adopted harnesses and evidence-supported lessons for future tasks.

## Editable components and execution

The framework exposes system prompts, guardrails, memory, tool guidance, subagents, skills, scripts, and plugins. It supports sequential and parallel recursion, OpenCode and Codex executors, and benchmark workflows for JobBench, LAB, and WorkBuddy-Bench. The repository documents Linux, Python 3.12, `uv`, optional model credentials, reproducible seeds, matching evaluation parameters, and cost controls.

## Reported evidence and limits

The README reports gains across three professional benchmarks and four model–harness configurations, including improvements of up to 11.5 points on WorkBuddy-Bench, 4.5 points on JobBench, and 11.8 percentage points on LAB's partial pass rate. These are project-reported benchmark results; they are not an independent replication or a guarantee for other models, tasks, or harnesses.

## See Also

- [Harness Design Principles](harness-design-principles.md)
- [Agent Skill Collections](../claude-code-ecosystem/agent-skill-collections.md)
- [Omnigent](omnigent.md)
