# UI UX Pro Max Skill

> Sources: nextlevelbuilder, Unknown date
> Raw: [UI UX Pro Max Skill](../../raw/claude-code-ecosystem/ui-ux-pro-max-skill.md)

## Overview

A design-intelligence skill for Claude Code and other AI coding tools, providing structured design knowledge (styles, palettes, typography, charts, accessibility rules, industry-specific reasoning) rather than leaving design decisions to model improvisation.

## Content and Mechanism

Ships 67 UI styles, 161 color palettes, 57 font pairings, 25 chart-type recommendations, 99 UX/accessibility guidelines, and 161 industry-specific reasoning rules across 22+ tech stacks (React, Vue, SwiftUI, Flutter, etc.). Retrieval uses BM25 ranking (Python) across style/palette/pattern/typography domains rather than embeddings. Version 2.0 adds full "design system generation": given requirements, it outputs a complete design system tailored to a vertical (SaaS, finance, healthcare, e-commerce, etc.).

Install via Claude Code marketplace or `npm install -g ui-ux-pro-max-cli`; auto-activates on UI/UX requests. Open-source version covers design intelligence; a premium tier adds brand identity and asset generation.

## See Also

- [Anthropic Agent Skills](anthropics-skills.md)
- [Claude Design](claude-design.md)
