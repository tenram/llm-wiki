# Playwright MCP (official docs)

> Source: https://playwright.dev/mcp/introduction
> Collected: 2026-10-13
> Published: Unknown

# Playwright MCP

A Model Context Protocol server that provides browser automation capabilities using Playwright. Enables LLMs to interact with web pages through structured accessibility snapshots — no vision models required.

## Example

```
You: Navigate to https://demo.playwright.dev/todomvc and add "Buy groceries".
→ browser_navigate { url: "https://demo.playwright.dev/todomvc" }
  - heading "todos" [level=1] [ref=e3]
  - textbox "What needs to be done?" [ref=e5]
→ browser_type { target: "e5", text: "Buy groceries", submit: true }
  - heading "todos" [level=1] [ref=e3]
  - textbox "What needs to be done?" [ref=e5]
  - list [ref=e8]:
    - listitem [ref=e9]:
      - checkbox "Toggle Todo" [ref=e10]
      - text: Buy groceries
  - contentinfo [ref=e12]:
    - text: 1 item left
```

The LLM reads the accessibility snapshot, finds element refs like `e5`, and passes them as the `target` of the next tool call — clicking buttons, filling forms, checking checkboxes. No screenshots or coordinate guessing needed.

## Key Features

- **Snapshot-based** — operates on the accessibility tree, not pixels. Each element gets a unique ref for deterministic interaction
- **LLM-friendly** — structured text output that LLMs parse naturally, far cheaper than DOM dumps or screenshots
- **Cross-browser** — Chrome, Firefox, WebKit, and Edge support
- **Full automation** — 70+ tools covering navigation, forms, network mocking, storage, tracing, video, and more
- **Persistent sessions** — login state and cookies preserved between sessions by default
- **Works everywhere** — VS Code, Cursor, Windsurf, Claude Code, Claude Desktop, and any MCP client

## Quick Start

Add the server to your MCP client:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    }
  }
}
```

The browser opens in **headed mode** by default so you can see what's happening.

## Playwright MCP vs Playwright CLI

| | MCP | Playwright CLI |
|---|---|---|
| Best for | Specialized agentic loops, exploratory automation | Coding agents (Claude Code, Copilot) working with large codebases |
| How it works | LLM calls MCP tools with structured parameters | Agent runs shell commands |
| Token cost | Higher — tool schemas + snapshots in context | Lower — concise CLI output, skills loaded on demand |
| Default mode | Headed | Headless |
| Setup | JSON config in MCP client | `npm install -g @playwright/cli` |

## Available Tools

### Core (always enabled)

`browser_navigate`, `browser_navigate_back`, `browser_snapshot`, `browser_find`, `browser_click`, `browser_hover`, `browser_drag`, `browser_drop`, `browser_type`, `browser_fill_form`, `browser_select_option`, `browser_press_key`, `browser_take_screenshot`, `browser_tabs`, `browser_handle_dialog`, `browser_file_upload`, `browser_console_messages`, `browser_network_requests`, `browser_network_request`, `browser_evaluate`, `browser_run_code_unsafe`, `browser_wait_for`, `browser_close`, `browser_resize`

### Network (`--caps=network`)

`browser_route` (mock network requests), `browser_route_list`, `browser_unroute`, `browser_network_state_set` (go online/offline)

### Storage (`--caps=storage`)

`browser_cookie_list/get/set/delete/clear`, `browser_localstorage_*`, `browser_sessionstorage_*`, `browser_storage_state` (save cookies + local storage to a file), `browser_set_storage_state` (restore saved state)

### Testing (`--caps=testing`)

`browser_generate_locator`, `browser_verify_element_visible`, `browser_verify_text_visible`, `browser_verify_list_visible`, `browser_verify_value`

### Developer tools (`--caps=devtools`)

`browser_start_tracing` / `browser_stop_tracing`, `browser_start_video` / `browser_stop_video`, `browser_video_chapter`, `browser_video_show_actions` / `browser_video_hide_actions`, `browser_start_recording` / `browser_stop_recording`, `browser_highlight` / `browser_hide_highlight`, `browser_annotate`, `browser_resume`

### PDF (`--caps=pdf`)

`browser_pdf_save` — export page as PDF

### Vision (`--caps=vision`)

`browser_mouse_move_xy`, `browser_mouse_click_xy`, `browser_mouse_drag_xy`, `browser_mouse_down` / `browser_mouse_up`, `browser_mouse_wheel`

### Config (`--caps=config`)

`browser_get_config` — get the resolved config
