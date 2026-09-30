# i-have-adhd

> Sources: ayghri, Unknown date
> Raw: [i-have-adhd](../../raw/claude-code-ecosystem/2026-09-30-i-have-adhd.md)

## Overview

i-have-adhd is a cross-agent skill and plugin that makes coding-agent responses easier to scan. Its governing style is action first, numbered steps for multi-step work, visible state, short lists, matter-of-fact errors, and one concrete next step instead of a preamble, recap, or closing.

## Rules and example

The ten rules lead with the next action, number tasks, end with a concrete next step, suppress tangents, restate state, use specific minute estimates, make wins visible, report errors plainly, cap lists at five items, and remove preambles and closers. The repository shows the transformation from a long conversational explanation into a short command followed by three numbered steps and a next action.

## Distribution

The skill is installable as a Claude plugin and is also exposed through plugin and skill formats for several coding-agent hosts. Users can install it from the repository or fork it and edit `skills/i-have-adhd/SKILL.md`. It is MIT licensed and is intended to shape agent output, not to diagnose ADHD or organize a person's life.

## See Also

- [ASD-STE100 Skill](asd-ste100-skill.md)
- [Anthropic Agent Skills](anthropics-skills.md)
- [Ponytail](../ai-agent-harnesses/ponytail.md)
