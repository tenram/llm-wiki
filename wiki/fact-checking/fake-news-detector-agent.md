# Fake News Detection Multi-Agent System

> Sources: IAmUnbounded, 2026-10-05
> Raw: [Fake News Detection Multi-Agent System](../../raw/fact-checking/fake-news-detector-agent.md)

## Overview

This project uses three cooperating agents to assess news claims: an orchestrator, a search agent, and a scoring agent. It returns an authenticity score with supporting evidence.

## Workflow

The orchestrator manages communication and the overall process. The search agent looks through historical news using a Google Search MCP Server. The scorer analyzes the supplied content with Google's Gemini API and estimates authenticity. The repository requires a Google API key and a running MCP search service.

## Caveats

An authenticity score is not proof of truth. Search coverage, source quality, retrieval errors, model bias, and the lack of an explicit human-review policy can affect results. The repository description does not provide a benchmark, calibration study, or evidence-quality rubric.

## See Also

- [Fact Check Skill](fact-check-skill.md)
- [Fact Checker Skill Listing](fact-checker-app-pattern.md)
