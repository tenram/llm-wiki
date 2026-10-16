# JS Reverse MCP

> Sources: zhizhuodemao, Unknown date
> Raw: [JS Reverse MCP README (Chinese)](../../raw/reverse-engineering/2026-10-13-js-reverse-mcp.md)

## Overview

JS Reverse MCP is an AI-native JavaScript reverse-engineering MCP server that lets coding assistants (Claude, Cursor, Copilot) continuously debug, locate, save, and replay JavaScript behavior in web pages. Rather than mapping Chrome DevTools API calls directly to tools, it reorganizes scripts, breakpoints, network, WebSocket, browser state, and local-file I/O into primitives suited to an agent's sequential reasoning. Apache 2.0. The original README is in Chinese.

## Design Philosophy

- **Tools are agent primitives, not DevTools menu mappings** — e.g., `list_network_requests` lists indexes, looks up details by `reqid`, and exports exact material to an `outputFile`; `evaluate_script` runs on the page, in a paused call frame, and can read a `localFilePath` input.
- **Output must guide the next step** — list output stays short and scannable; detail output is bounded; large results prompt export; pending requests explicitly advise resuming execution rather than waiting forever.
- **Local files are the analysis workbench** — `save_script_source`, network `outputFile`, and `evaluate_script` with `localFilePath` let the agent shuttle between browser, network, and local files instead of stuffing large code into context.
- **State can be cleaned and flows replayed** — default profile keeps login state; `--isolated` gives a one-shot clean environment; `clear_site_data` clears only current-site state to reproduce cookie-generation, anti-bot-initiation, and request chains.

## Anti-Detection (Supporting Capability)

The wrapper itself does zero JS injection and no `Object.defineProperty` hacks (itself a detectable signal). Anti-detection sits in two non-overlapping layers:

- **Protocol layer (CDP)** — default: a dedicated, independently-maintained [Patchright fork](https://github.com/zhizhuodemao/patchright-mcp) that avoids `Runtime.enable`/`Console.enable`, evaluates in an isolated world, removes the automation launch flag, and keeps fixing known shared implementation traits. No page-level JS injection.
- **Source layer (C++ binary patch)** — only with `--cloak`: CloakBrowser binary covering `navigator.webdriver`, canvas, WebGL, audio, GPU, fonts, screen, WebRTC, and TLS fingerprint patches (custom Chromium build, separate profile directory).

Navigation-level measures in both modes: CDP-silent navigation (Network/Debugger domains not activated on page load until a tool explicitly needs them), default Google referer on `new_page`, and a real viewport instead of Playwright's fake 1280×720.

## Tools (24)

- **Page & navigation**: `select_page`, `new_page`, `navigate_page`, `select_frame`, `click_element`, `take_screenshot`
- **Script analysis**: `list_scripts`, `get_script_source`, `save_script_source` (large/minified/WASM), `search_in_sources` (string or regex)
- **Breakpoints & execution**: `set_breakpoint_on_text` (auto by code-text search, for minified code), `break_on_xhr` (by URL pattern), `remove_breakpoint`, `list_breakpoints`, `get_paused_info`, `pause_or_resume`, `step` (over/into/out)
- **Network & WebSocket**: `list_network_requests`, `clear_network_requests`, `get_request_initiator` (JS call stack), `get_websocket_messages`
- **Browser state**: `clear_site_data`
- **Inspection**: `evaluate_script`, `list_console_messages`

## Configuration

CLI flags are all optional; defaults suit 99% of cases. Key options: `--cloak` (CloakBrowser stealth binary, ~200MB auto-download), `--isolated` (temporary profile), `--browserUrl/-u` (connect to a running Chrome via CDP endpoint, e.g., AdsPower/BitBrowser fingerprint browsers), `--logFile` (mode-0600 log; only `DEBUG=mcp:*`, never `DEBUG=*`), and `--allowedRoots` (restrict agent-accessible directories; disables `file:`/`view-source:file:`/`filesystem:file:` pages when set).

## See Also

- [REA: Reverse Engineer Anything](rea.md) — broader agent reverse-engineering MCP spanning binaries, apps, and runtime; JS Reverse MCP is the web/JavaScript-focused sibling.
- [Stealth Browser Automation](../browser-and-mcp-tooling/stealth-browser-automation.md) — fingerprint-reduction layers for Playwright/Puppeteer; JS Reverse MCP's Patchright fork and CloakBrowser extend this to protocol and source layers.
