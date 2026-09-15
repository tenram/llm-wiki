# Playwright

> Sources: https://playwright.dev/; https://github.com/AtuboDad/playwright_stealth
> Collected: 2026-08-18
> Published: Unknown (Copyright 2026 Microsoft)

Playwright (Microsoft) enables "reliable web automation for testing, scripting, and AI agents," providing one API to drive Chromium, Firefox, and WebKit across tests, scripts, and agent workflows. Supports TypeScript, Python, .NET, and Java; runs on Linux, macOS, Windows, headless or headed.

Key features: auto-waiting and web-first assertions with automatic retry logic; test isolation via fresh browser contexts per test; resilient locators (`getByRole`, `getByLabel`, `getByPlaceholder`, `getByTestId`); parallel and cross-browser sharding; accessibility snapshots for agent interaction; an MCP server integration; a CLI aimed at coding agents; a test generator with recording capability; a Trace Viewer; and a VS Code extension.

The `playwright_stealth` source adds a fingerprint-reduction layer for cases where automation has to survive bot checks.

Notable claims: large adoption across Microsoft and front-end tooling ecosystems; marketed with "full isolation with near-zero overhead."
