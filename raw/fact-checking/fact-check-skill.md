# Fact Check Skill

> Source: https://github.com/petar-nauka/fact-check-skill
> Collected: 2026-10-05
> Published: Unknown

Fact-checking and disinformation detection skill for Claude and Codex. It covers evidence-led fact-checking, source credibility evaluation, misinformation-risk scoring, prebunking briefings, and HTML Fact-Check Cards.

The repository separates trigger metadata and core workflow in `SKILL.md`; detailed source evaluation and output guidance in `references/`; JSON contracts in `schema/`; validation, card rendering, and packaging in `scripts/`; and regression fixtures in `tests/`.

The documented validation commands are:

```text
python .\scripts\validate_skill.py .
python -m unittest discover -s tests
```
