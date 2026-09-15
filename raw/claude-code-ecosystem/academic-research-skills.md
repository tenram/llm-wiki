# Academic Research Skills for Claude Code

> Source: https://github.com/imbad0202/academic-research-skills
> Collected: 2026-07-11
> Published: Unknown

A suite of Claude Code skills covering the full research-to-publication pipeline, built around human-in-the-loop workflows rather than full automation, informed by documented AI research failure modes.

Four core skills: Deep Research (v2.11.0), a 13-agent research team with 8 operational modes including Socratic guided research, PRISMA-based systematic reviews, fact-checking; Academic Paper (v3.2.0), a 12-agent writing pipeline supporting multiple paper structures and citation formats; Academic Paper Reviewer (v1.10.0), a 7-agent peer review system using 0-100 quality rubrics and multi-perspective assessment; Academic Pipeline (v3.15.0), a 10-stage orchestrator linking research through publication with integrity checkpoints.

Architecture features: human oversight via stage integrity gates (stages 2.5 and 4.5) that cannot be bypassed; a "concession threshold protocol" for devil's-advocate debaters to resist sycophancy; intent detection distinguishing exploratory versus goal-oriented research modes; a "Material Passport" for tracking experiment provenance and claim verification.

Output formats: Markdown, DOCX, LaTeX (APA 7.0, IEEE, Chicago), 5+ citation formats, multiple paper structures (IMRaD, literature review, policy brief, case study), bilingual English/Traditional Chinese abstracts.

Installation (v3.7.0+): `/plugin marketplace add Imbad0202/academic-research-skills` then `/plugin install academic-research-skills`. Requires Claude Code (latest) and ANTHROPIC_API_KEY; optionally Pandoc for DOCX and tectonic for typeset PDF. Stated philosophy: AI augments researcher decision-making rather than acting autonomously.
