# anthropics/skills

> Source: https://github.com/anthropics/skills
> Collected: 2026-07-11
> Published: Unknown

Anthropic's public repository implementing "Agent Skills" for Claude: folders of instructions, scripts, and resources Claude loads dynamically for specialized tasks (brand-guideline document creation, org-specific data workflows, task automation). Repo layout: `./skills` (examples across Creative & Design, Development & Technical, Enterprise & Communication, Document Skills for PDF/DOCX/PPTX/XLSX), `./spec` (Agent Skills specification), `./template` (skill template), `.claude-plugin` (plugin config).

Skill structure: a folder containing a required `SKILL.md` with YAML frontmatter (`name`, `description`) followed by instructions, examples, and guidelines.

Usage: in Claude Code, `/plugin marketplace add anthropics/skills` then `/plugin install document-skills@anthropic-agent-skills` or `/plugin install example-skills@anthropic-agent-skills`; also usable in Claude.ai (paid plans) and via the Claude API.

Licensing: most skills Apache 2.0 open source; document skills (docx, pdf, pptx, xlsx) are source-available (not open source), shared as reference implementations. Explicit disclaimer these are for demonstration/educational purposes.

Repo stats at fetch time: 160k stars, 18.9k forks, 287 issues, 734 PRs, 43 commits; languages Python 84.4%, HTML 12.4%, Shell 1.9%, JavaScript 1.3%.
