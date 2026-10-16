# DevCDP

> Sources: Dayananda-D, Unknown date
> Raw: [DevCDP README](../../raw/browser-and-mcp-tooling/2026-10-13-devcdp.md)

## Overview

DevCDP is an MCP server giving an AI assistant real Chrome DevTools access: reading the console, watching the network, querying the DOM, resolving source maps, setting breakpoints, and inspecting live variables — so the assistant can explain why something broke instead of guessing from a pasted error. It is framework- and product-agnostic, works with any MCP-capable assistant, and runs fully locally (nothing is hosted). MIT licensed, built by a single developer, listed in the official MCP Registry. Ships 74 tools.

## Capabilities

- **Console** — logs, warnings, uncaught exceptions with file, 1-based line, and stack.
- **Network** — every request from attach onward: method, status, timing, size, initiator, response bodies on request.
- **DOM** — selector queries with real visibility/geometry, named computed styles, mutation history, iframe support, dialog detection.
- **Sources** — loaded scripts plus original pre-bundling files recovered from source maps (including external `.map` files behind auth); full-text search across both.
- **Debugger** — breakpoints on original files by original line, stepping, and scope inspection that expands nested objects.
- **Discovery** — asks the app what it is: framework, routing, working selectors, backend API surface, project docs.
- **Collaboration** — the human can take over any time; clicks/choices/typed values are recorded and readable by the assistant.

## Reliability Principles

- **Never fakes success** — unbound breakpoints say `bound: false` and why; discarded bodies are disclosed; every failure returns `{ok: false, code, message, hint}` with the next action named.
- **States its knowledge limits** — attaching later than a console history can't replay it, so it reports that rather than an empty "no errors".
- **Cannot be stranded** — calls into the page are bounded on DevCDP's side (renderer-enforced timeouts fail when the renderer is stuck); a page wedged in an infinite loop fails in seconds and DevCDP aborts the runaway script and retries.
- **Never leaves the app frozen** — breakpoints resume on their own; a deliberate pause is released after `maxPauseMs`.

## Setup

Node 18+, Chrome, and an MCP-capable assistant. Install via npm (`npx -y devcdp`) into any MCP client, or as a plugin/extension for Claude Code, Gemini CLI, Codex, VS Code/Copilot CLI, Cursor, and opencode. A setup wizard (`node initialize_MCP.js`) writes the right config per detected editor, never overwrites unparseable configs, and is covered by 23 tests. Chrome launches with a separate debug profile via `debug-chrome.bat` or `chrome --remote-debugging-port=9222 --user-data-dir=<separate profile>`.

## Sessions and Tab Ownership

Multiple agents debug safely on one machine: each session atomically claims a tab in `~/.devcdp/registry/`; dead sessions are reaped via heartbeat timeout. Each claimed tab carries a 1px edge border + identity chip (blue glow = working, green = handed to you, red = failed) and a titled Chrome tab group via the bundled extension (Chromium/Chrome-for-Testing auto-load it; branded Chrome needs a one-time manual install).

## Typical Investigation

`devtools_connect` → `source_search("save")` to find the handler by content → `debugger_set_breakpoint(file, line)` returning `bound: true` → trigger the click → `debugger_get_capture` returns scope, console, and network from the pause in one call. `debugger_set_breakpoint_at_function("app.store.save")` breaks at the first statement of a function resolved via the engine, avoiding unreliable text-name search on framework-assigned functions.

## See Also

- [Playwright MCP](playwright-mcp.md) — the other major browser-automation MCP server; Playwright MCP drives the browser, while DevCDP is a debugging-focused view into a real DevTools session.
- [JS Reverse MCP](../reverse-engineering/js-reverse-mcp.md) — CDP/DevTools-based JavaScript reverse engineering for agents.
- [Model Context Protocol Overview](model-context-protocol-overview.md)
