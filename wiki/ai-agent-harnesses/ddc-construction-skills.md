# DDC Skills for AI Agents in Construction

> Sources: DataDrivenConstruction, 2026-10-08
> Raw: [DDC Skills Collection README](../../raw/ai-agent-harnesses/2026-10-08-ddc-skills-for-ai-agents-in-construction.md)

## Overview

The DataDrivenConstruction DDC Skills Collection is a cross-agent catalog of 238 `SKILL.md` packages for construction-company automation. It covers BIM and CAD extraction, estimating, scheduling, document processing, reporting, analytics, field workflows, AI/ML, and OpenConstructionERP. The repository explicitly targets Claude Code, Google Antigravity, OpenCode, ClawdBot, and similar AI coding assistants rather than a single host.

## Organization

The six top-level groups separate production tools, book-based learning, practical workflows, curated document skills, experimental or advanced capabilities, and OpenConstructionERP integrations. The largest groups are the production toolkit with 85 skills and the book-aligned collection with 67. The remaining groups cover insights and workflows (20), curated document generation and quality assurance (20), innovative AI/ML and construction technology (34), and OpenConstructionERP (12).

The source is internally inconsistent about the total: its title and category table state 238 skills, while a later README sentence says the full collection contains 221. This article uses 238 as the primary count and preserves the discrepancy rather than resolving it without repository-level verification.

## Operating Model

The repository treats a skill as an executable instruction package: a `SKILL.md` tells an AI coding assistant what problem to solve, what code to generate, and which tools are needed. Users select a skill directory, let the assistant generate an implementation, then review, adapt, and run it against local data. This makes the collection a domain-specific capability layer that can sit above multiple agent harnesses.

## Construction Automation Path

The recommended sequence is audit, classify, connect, automate, and analyze. First inventory data silos such as spreadsheets, databases, BIM models, PDFs, and email. Then classify inputs as structured, semi-structured, or unstructured. Next extract and normalize them with ETL and specialist parsers. After that, automate recurring reports, alerts, and dashboards. Finally apply analytics and machine learning to estimate costs, forecast schedules, and assess risk.

The sequence is guidance rather than a hard gate: teams can start at the stage that matches their current maturity or most urgent problem.

## Domain Coverage

The catalog connects common construction problems to concrete skills. Examples include work-item rate search, estimate generation, Revit and IFC quantity extraction, daily reports, site-photo classification, data-silo discovery, KPI dashboards, budget tracking, PDF specification extraction, and schedule-delay analysis.

Its data model distinguishes structured data such as Excel, CSV, and SQL; semi-structured data such as IFC/BIM, JSON, and XML; and unstructured data such as PDFs, photos, and scans. The intended pipeline uses direct transformations, specialized parsers, or AI/OCR respectively, followed by centralized automation and analytics.

## Constraints and Caveats

The stated baseline is Python 3.9+, an AI coding assistant, basic Python knowledge, and project data. Advanced skills may require Docker, PostgreSQL or SQLite, or an OpenAI API key. The README presents time savings as potential outcomes, not measured guarantees, and says results depend on data quality, preparation, company size, and workflow complexity.

Licensing is mixed: the CWICR database is listed as CC BY-NC 4.0 with separate commercial licensing, while DDC tools and skills are listed as MIT. Users should check the repository and individual skill before commercial deployment.

## Relationship to Agent Harnesses

DDC is best understood as a domain catalog rather than a complete agent runtime. It supplies task-specific instructions and implementation recipes; the host assistant supplies the execution loop, tools, permissions, memory, and review controls. This separation lets the same construction capability be reused across several agent products, while leaving deployment safety and quality verification to the adopting team.

## See Also

- [Harness Design Principles](harness-design-principles.md)
- [Awesome Harness Engineering](awesome-harness-engineering.md)
- [Anthropic Agent Skills](../claude-code-ecosystem/anthropics-skills.md)
- [Awesome Claude Skills](../claude-code-ecosystem/awesome-claude-skills.md)
