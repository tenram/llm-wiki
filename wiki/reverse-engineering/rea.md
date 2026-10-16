# REA: Reverse Engineer Anything

> Sources: morluto / REA project, Unknown date
> Raw: [REA README](../../raw/reverse-engineering/2026-10-13-rea-reverse-engineer-anything.md)

## Overview

REA (Reverse Engineer Anything) is an MCP server — with a matching CLI (`rea-agents` npm package) — that connects AI agents to reverse-engineering tools for inspecting native binaries, JavaScript/Electron apps, .NET assemblies, websites, and more. Its core use case: a user asks an agent to understand how a feature in an existing app works (down to the binary level) so the agent can explain it with evidence or reimplement it, all without the target's source code. Analysis runs locally, and results carry the evidence and limitations behind each conclusion.

## How It Works

The agent calls REA through MCP to inspect a local target and trace relevant code; REA returns findings with supporting evidence. The agent uses those findings to ask follow-up questions, explain behavior, or write and test an implementation. The same workflows are available from the terminal. Static JavaScript and .NET inspection read files without executing the application; runtime capture runs or interacts with targets using the user's permissions.

## Analysis Targets

REA requires Node.js 22.x (>=22.19), 24.x (>=24.11), or 26+, plus npm. Target coverage:

- **Native binaries** — pseudocode, assembly, strings, symbols, calls and references via a Hopper, Ghidra, or IDA provider (setup can optionally install Hopper; Ghidra also supports 16-bit DOS analysis).
- **Go / Rust binaries** — embedded compiler version and module/crate metadata via built-in static ELF/PE/thin Mach-O inspection (no toolchain install needed).
- **JavaScript / Electron** — modules, imports, source maps, routes, IPC, and native add-on relationships.
- **.NET assemblies** — metadata, CIL instructions, declared native dependencies, build comparisons (static only).
- **Websites** — page structure, scripts, network observations, requested screenshots (Chrome-family browser).
- **Android** — APK manifest/classes/decompiled methods via JADX; device analysis via adb; resources via Apktool; Flutter apps via static APK parsing.
- **Network and hardware artifacts** — saved network captures (HAR/SAZ), recorded packets (TShark), pcap summaries, recorded logic signals (sigrok-cli), firmware (Binwalk/Unblob).
- **Other** — WASM artifacts (WABT), EVM bytecode, SQLite databases, recorded Linux crashes (pwntools/GDB), packages/resources (Apple bundles), and process behavior via native PTY.

## Setup and Agent Integration

`npx rea-agents setup` registers the MCP server and installs matching workflow instructions for Claude Code, Codex, Cursor, Gemini CLI, Grok Build, and other MCP-capable agents, backing up existing configuration. Native deep analysis needs Hopper, Ghidra, or IDA; static JavaScript/.NET analysis needs no native engine. The CLI supports one-off analysis (e.g., `analyze-javascript-application`) and `rea update` for self-updates.

## Showcases

- **DX-Ball**: reconstructed a sound-pan calculation from a 16-bit-era binary into C, passing 3,205 original-x86 cases and reproducing all 63 compiled function bytes.
- **Notion**: traced the Electron clipboard bridge from renderer API through preload and IPC into the main process.
- **TH04**: recovered a PC-98 DOS bullet-ring calculation and compared reconstructed C++ against historical compiler output.

## Licensing and Responsible Use

MIT-licensed for REA-authored code. Commercial tools (IDA Pro/Hex-Rays, Hopper, JEB) must be legally obtained; REA grants no license or activation entitlement. Usage is scoped to lawful research, education, interoperability, software preservation, and analysis of software the user owns or is authorized to examine.

## See Also

- [JS Reverse MCP](js-reverse-mcp.md) — web/JavaScript-focused agent reverse-engineering MCP with anti-detection layers.
- [Model Context Protocol (MCP)](../browser-and-mcp-tooling/model-context-protocol-overview.md) — the open standard over which REA exposes its tools to agents.
