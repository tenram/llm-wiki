# Fact Check Skill

> Sources: petar-nauka, 2026-10-05
> Raw: [Fact Check Skill](../../raw/fact-checking/fact-check-skill.md)

## Overview

Fact Check Skill is a Claude and Codex skill for evidence-led fact checking, source-credibility evaluation, misinformation-risk scoring, prebunking briefings, and HTML Fact-Check Cards.

## Structure

The repository keeps trigger metadata and the core workflow in `SKILL.md`. Detailed evaluation guidance lives in `references/`, result contracts live in `schema/`, and scripts validate results, render cards, and package archives. Regression fixtures are stored in `tests/`.

## Validation

The documented checks are `python .\\scripts\\validate_skill.py .` and `python -m unittest discover -s tests`. The skill therefore treats output validation and regression fixtures as part of the fact-checking workflow, rather than relying only on prompt instructions.

## See Also

- [Fake News Detection Multi-Agent System](fake-news-detector-agent.md)
- [Fact Checker Skill Listing](fact-checker-app-pattern.md)
