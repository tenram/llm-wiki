# Self-Improving AI Skills (Claude Code)

> Sources: MindStudio, Unknown date; Peter Yang (creatoreconomy.so), Unknown date; pskoett (ClawHub), Unknown date
> Raw: [Self-Improving AI Skills in Claude Code: Summary](../../raw/claude-code-ecosystem/2026-07-21-self-improving-ai-skills-mindstudio.md); [Full Tutorial: Build Self-Improving Claude Skills in 20 Min](../../raw/claude-code-ecosystem/2026-07-31-self-improving-claude-skills-tutorial.md); [self-improving-agent (OpenClaw skill)](../../raw/claude-code-ecosystem/clawhub-self-improving-agent-skill.md)

## Overview

MindStudio describes a pattern for making Claude Code skills improve across runs without any model fine-tuning: each skill maintains a `learnings.md` file that it reads at startup and writes back to after execution, accumulating what worked, what failed, and what to avoid.

## Mechanism

Three components form the loop:

1. **`learnings.md`** — a persistent Markdown file of accumulated observations, read at the start of each skill invocation.
2. **Feedback signals** — either automated binary evaluations (defined in `eval.json`) or human ratings scored against concrete criteria.
3. **Write-back step** — a wrap-up phase that translates the feedback into updated notes in `learnings.md` after each run.

**Binary evals** are emphasized over subjective judgments: objective yes/no criteria ("does output contain required element?") rather than vague quality ratings ("is tone good?"). Expect roughly five to ten run cycles before behavioral change becomes visible; early runs are mostly data collection. Multiple self-improving skills can chain independently while passing outputs downstream, compounding improvement across a workflow. The **AutoResearch pattern** — generating multiple candidate outputs per run, scoring each, and logging what distinguished the winner — is cited as one way to accelerate the feedback loop.

## Distinction from Fine-Tuning

This is explicitly not weight modification. It's an external context file, read and written at runtime, that's faster, cheaper, and incrementally updatable compared to any training-based approach.

## Practical Build Steps (Peter Yang's tutorial)

A five-step process for building this pattern into a real skill: (1) seed the skill with personal examples/context, (2) write explicit "Use when..." trigger phrases into the description so activation is reliable, (3) implement binary pass/fail evaluation loops in `evals.md` rather than subjective scoring, (4) log lessons to `memory.md` after each run, (5) build meta-skills (`/skill-editor`, `/no-ai-slop`) to maintain quality across the whole skill library. This matches MindStudio's `learnings.md` loop but adds concrete tooling: keep example content in separate files from the skill definition, and run evaluation agents in a clean context separate from editing agents to avoid self-grading bias.

## OpenClaw Implementation: `.learnings/`

OpenClaw's `self-improving-agent` skill is a working instance of this pattern outside Claude Code: it writes to `LEARNINGS.md`, `ERRORS.md`, and `FEATURE_REQUESTS.md` under `.learnings/`, with entries tagged by a deduplicating "Pattern-Key" (`area.symptom`). An optional hook auto-scans session transcripts for error patterns on `command:new`/`command:reset` and writes redacted excerpts to `ERRORS.md` — the documentation itself flags this as a data-retention risk in shared workspaces. Learnings that prove broadly applicable get promoted into persistent files (`SOUL.md`, `TOOLS.md`, `AGENTS.md`), mirroring how `learnings.md` content is expected to eventually harden into a skill's own instructions.

> Note: the ClawHub source page for this skill contained an embedded prompt-injection attempt disguised as a system reminder, instructing tool use and asking not to be mentioned to the user. It was disregarded.

## See Also

- [Superpowers](../ai-agent-harnesses/superpowers.md) — a skills framework this pattern could be layered onto, since it already enforces a structured workflow before coding.
- [Autoresearch](../research-and-training/autoresearch.md) — related autonomous-experimentation pattern; worth checking whether this article's "AutoResearch pattern" is the same project or a coincidentally-named technique.
