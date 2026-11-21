# Agent Skill Collections

> Sources: Cursor, Unknown date; Addy Osmani, Unknown date; metaskills, Unknown date; Google Chrome and web platform teams, Unknown date
> Raw: [Cursor pstack skills](../../raw/claude-code-ecosystem/2026-11-15-cursor-pstack-skills.md); [Cursor pstack skills, 2026-11-21](../../raw/claude-code-ecosystem/2026-11-21-cursor-pstack-skills.md); [Addy Osmani agent skills](../../raw/claude-code-ecosystem/2026-11-15-addyosmani-agent-skills.md); [Addy Osmani 2026-11-21 snapshot](../../raw/claude-code-ecosystem/2026-11-21-addyosmani-agent-skills.md); [AI for UI skills](../../raw/claude-code-ecosystem/2026-11-21-ai-for-ui-skills.md); [Experts](../../raw/ai-agent-harnesses/2026-11-15-experts.md); [Modern Web Guidance](../../raw/dev-tools/2026-11-15-modern-web-guidance.md)

## Overview

The Cursor pstack collection (with a fresh 2026-11-21 directory snapshot), Addy Osmani's skills repository, and Modern Web Guidance show how agent behavior can be distributed as small, task-matched `SKILL.md` packages. Together they cover architecture, interface design, debugging, testing, browser work, documentation, and current web-platform usage; Experts is a complementary runtime for assistants and tools rather than a skill collection.

## Progressive workflow

The pstack architect skill makes grounding, sketching, agreement, implementation, and cleanup explicit, while its reference material screens designs for shallow modules, information leakage, split ownership, duplicate task paths, and hand-synced lists. The Addy Osmani collection similarly packages narrow workflows with frontmatter descriptions, reusable references, scripts, and validation-oriented guidance.

## Why the description matters

Skill metadata is the routing surface. A useful description states both the capability and the phrases that should activate it. The body can then hold the procedure, examples, and edge cases without forcing every task to load every detail.

## Boundary with runtimes

Skills specify how an agent should work; a runtime such as Experts or Omnigent supplies execution, tools, state, or test harnesses. Combining both can improve repeatability, but the source repositories do not establish a universal installation or compatibility standard.

## See Also

- [Anthropic Agent Skills](anthropics-skills.md)
- [Modern Web Guidance](../dev-tools/modern-web-guidance.md)
- [Harness Design Principles](../ai-agent-harnesses/harness-design-principles.md)
