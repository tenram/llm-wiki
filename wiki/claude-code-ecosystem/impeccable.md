# Impeccable

> Sources: Paul Bakaus / Impeccable, Unknown date
> Raw: [Impeccable README](../../raw/claude-code-ecosystem/2026-11-10-impeccable.md); [2026-11-15 source snapshot](../../raw/claude-code-ecosystem/2026-11-15-impeccable.md); [2026-11-21 source snapshot](../../raw/claude-code-ecosystem/2026-11-21-impeccable.md)

## Overview

Impeccable is a coding-agent skill and deterministic detector for improving interface design. It supplies named design commands, context files, review modes, live browser iteration, and rules intended to reduce repetitive AI-generated UI patterns.

## Command And Context Model

The installer adds the skill to supported coding tools, after which `/impeccable init` creates `PRODUCT.md` and `/impeccable document` can capture a project design system in `DESIGN.md`. Commands such as `bolder`, `quieter`, `distill`, `typeset`, `layout`, `critique`, `audit`, `polish`, `harden`, and `adapt` target a named page or component.

The workflow favors narrow targets and iterative review. `critique` scores usability heuristics, while `audit` reports accessibility, performance, theming, and responsive findings with priorities. A browser live mode lets a user select elements, compare variants, and accept changes into the local checkout.

## Deterministic Checks And Boundaries

The detector advertises 62 deterministic rules and does not require an LLM or API key. Source scans cover pattern rules; rendered-page scans add checks such as contrast and small text. The README warns that live copy application can invoke a local coding agent with permissions inherited from the environment, so unfamiliar hooks and scripts require review.

## Practical Takeaway

Impeccable is a domain-specific harness layer for UI iteration rather than a general frontend framework. Its main contribution is vocabulary plus repeatable review and detector checks that turn vague design requests into bounded agent actions.

## See Also

- [UI UX Pro Max Skill](ui-ux-pro-max-skill.md)
- [Agent Skills Engineering Workflows](agent-skills-engineering-workflows.md)
- [Agent Skills Platform](../ai-agent-harnesses/agent-skills-platform.md)
