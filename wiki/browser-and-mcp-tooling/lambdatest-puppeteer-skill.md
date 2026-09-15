# LambdaTest Puppeteer Skill

> Sources: LambdaTest, Unknown date
> Raw: [puppeteer-skill (LambdaTest Agent Skills)](../../raw/browser-and-mcp-tooling/lambdatest-puppeteer-skill.md)

## Overview

`puppeteer-skill` is a `SKILL.md`-format agent skill published by LambdaTest (part of their [LambdaTest/agent-skills](https://github.com/LambdaTest/agent-skills) repo) that teaches an agent reusable patterns for driving Puppeteer against headless Chrome/Chromium. It triggers on keywords like "Puppeteer," "headless Chrome," "page.goto," "scrape," and "PDF generation."

## Capabilities

Launching headless browsers with viewport control, navigation and form interaction, wait strategies (`waitForSelector`, `waitForNavigation`, `waitForFunction`, `waitForResponse`), screenshot and PDF generation, and request interception with response mocking or resource blocking.

## Use Cases

Web scraping and data extraction, automated login/form submission, CI-friendly end-to-end tests, visual reporting via screenshots or PDFs, and resilient automation via mocking unstable third-party APIs.

## Distribution

Listed on the LobeHub Skills Marketplace, a marketplace claiming over 100,000 skills, installable via the `@lobehub/market-cli` npm package. MIT-licensed, version 1.0.2 at time of collection.

## See Also

- [Playwright](playwright.md) / [Playwright MCP](playwright-mcp.md) — the competing/complementary browser-automation stack; Playwright MCP exposes automation via accessibility snapshots rather than the wait-strategy/selector approach this skill teaches for raw Puppeteer.
