# REA: Reverse Engineer Anything

> Source: https://github.com/morluto/rea
> Collected: 2026-10-13
> Published: Unknown

# REA: Reverse Engineer Anything

### One MCP for reverse engineering across binaries, applications, and runtime behavior.

**See a feature you like. Understand how it works, down to the binary level.**

Get REA from morluto/rea, rea.tools, or the rea-agents npm package. Follow the installation and release links from these official sources. A similar repository name or copied README does not establish that a download is official.

```bash
npx rea-agents setup
```

See a feature in an app that you want in your own product? Ask your agent to investigate it with REA. It can inspect the app without its source code, explain how the feature works, show the evidence, and build a version for your project.

REA connects your agent to tools for inspecting native binaries, JavaScript and Electron apps, .NET assemblies, and websites. You can also use the same tools from your terminal. Analysis runs locally, and results include the evidence and limitations behind each conclusion.

Setup registers REA with your agent and installs matching workflow instructions. Native analysis can use an existing Hopper, Ghidra, or IDA installation; setup can optionally install Hopper with approval. Static JavaScript analysis needs no native analysis engine.

## Quick start

### Set up your agent

With Node.js and npm installed, run:

```bash
npx rea-agents setup
```

Choose your agents, review the proposed changes, and approve them. Setup adds REA's MCP server and matching workflow instructions, with backups of existing configuration. Restart your agent afterward.

Setup supports Claude Code, Codex, Cursor, Gemini CLI, Grok Build and other agents.

### Ask your agent

```
Understand how search works in the Notes app, show me the evidence, and build a similar feature for my project.
```

Replace Notes with your target app and the feature you want to understand.

### Use the terminal

Inspect an extracted JavaScript/Electron app directory or ASAR:

```bash
npx -y rea-agents@latest analyze-javascript-application /absolute/path/to/app --json
```

The result includes modules, imports, Electron boundaries and their evidence. Replace the path with your target, such as `"D:/apps/example"` on Windows.

To install the `rea` command for regular use:

```bash
npm install --global rea-agents
rea --help
```

For native analysis, configure a provider first. See the CLI and Evidence guide for native commands, provider selection, snapshots and scripting.

### Update REA

REA changes quickly, and new releases include frequent bug fixes. Keep your installation up to date.

For a CLI installed with `npm install --global` or `bun add --global`:

```bash
rea update
```

Bun global updates require Bun 1.2.17 or later. With an older Bun release, upgrade Bun manually before running `rea update`.

To refresh your agent registrations and skill, run the setup command printed by the update.

If you use `npx`, update your agent setup with:

```bash
npx rea-agents@latest setup
```

Review the setup changes and restart your agent. For one-off CLI commands, use `npx rea-agents@latest` followed by the command. With Bun, use `bunx rea-agents@latest` in place of `npx rea-agents@latest`.

## How REA works

Your agent calls REA through MCP to inspect the target and trace relevant code. REA returns findings with their evidence. The agent uses them to ask follow-up questions, explain the behavior, or write and test an implementation. CLI commands use the same workflows.

## What you can analyze

REA requires Node.js 22.x (>=22.19), 24.x (>=24.11), or 26+, plus npm. Additional tools and host support depend on the target:

| Target | What REA returns | Requirements |
| ------ | ---------------- | ------------ |
| Native binaries | Pseudocode, assembly, strings, symbols, calls and references | Hopper, Ghidra or IDA |
| Offline ELF layout | Sections, segments, original symbols/relocations and static mitigation candidates | Caller-supplied pwntools on Linux x64 |
| Go binaries | Embedded compiler version, modules, replacements and build settings | Built-in static ELF/PE/thin Mach-O inspection; no Go installation required |
| Rust binaries | Embedded cargo-auditable crate names, versions, sources and dependency edges | Built-in static ELF/PE/thin Mach-O inspection |
| WASM artifact | Validation, sections, exact import/export WAT forms and decoded WAT | Caller-supplied WABT 1.0.42 |
| EVM bytecode | Dispatch selectors, byte offsets, inferred arguments and mutability | Local raw/hex carrier on Linux x64 |
| SQLite databases | Tables, columns, indexes, views, triggers and selected ordinary-table rows | Local database/WAL snapshot; Node.js 24.x >=24.15 or 26+ with native SQLite limits |
| Recorded Linux crashes | Raw notes, every recorded thread's registers/signals and optional mapping candidates | Caller-supplied pwntools on Linux x64; optional GDB/pwndbg |
| JavaScript / Electron | Modules, imports, source maps, routes, IPC and native add-on relationships | Node.js and npm |
| Websites | Page structure, scripts, network observations and requested screenshots | A Chrome-family browser |
| Saved network captures | Requests, responses, exposed payloads and source locations | HAR or Fiddler Everywhere SAZ; mitmdump on Linux for native mitmproxy |
| .NET assemblies | Metadata, CIL instructions, declared native dependencies and build comparisons | None (static only) |
| Android APKs | Manifest declarations, classes, decompiled methods and references | Headless JADX and a full JDK on Linux/macOS/Windows x64 |
| Android devices | Devices, packages, processes, logs, dumps, screen captures, and APK/file transfers | Caller-supplied adb (emulator or hardware) |
| JEB projects | Engine-backed project units, artifact digests and type/method pseudo-code | A caller-started JEB client serving MCP, selected with REA_JEB_MCP_URL |
| Android resources | Decoded manifest, string tables, locales and version facts | Caller-supplied Apktool launcher |
| Flutter apps | Dart snapshot hash, per-ABI library digests and engine build provenance | None (static APK parsing) |
| Firmware | Regions, extraction results and native-analysis handoffs | Binwalk / Unblob on Linux |
| Recorded packets | Selected fields, repeated values, filters and decode-as rules | Linux: TShark 4.x + prlimit |
| Packet summaries | Endpoints, DNS, TLS SNI, protocol distribution and HTTP requests | Caller-supplied tshark and capinfos (Linux-verified) |
| Recorded logic signals | Decoder annotations, sample ranges and diagnostics | Linux: sigrok-cli 0.7.2 + prlimit |
| Packages and resources | File inventories, digests, plists, Apple bundle anatomy and extracted resources | - |
| Process behavior | Terminal output, interactions, exit and filesystem observations, and run comparisons | Linux/macOS with a native PTY |

Static JavaScript and .NET inspection read the supplied files without running the application. Runtime capture runs or interacts with the selected target using your user permissions; each runtime guide describes its effects.

Native formats and host support vary by provider. Ghidra also supports 16-bit DOS analysis. For large binaries, raise the provider's startup deadline with `REA_GHIDRA_STARTUP_TIMEOUT_MS` or `REA_HOPPER_STARTUP_TIMEOUT_MS`.

## Showcases

### DX-Ball: reconstruct a sound-pan calculation

Follow a sound call into its position-to-pan helper, inspect the instructions, and turn incomplete pseudocode into C. The reconstruction passes 3,205 original-x86 cases and reproduces all 63 compiled function bytes.

### Notion: trace the Electron clipboard bridge

Find the renderer's clipboard API, follow it through preload and IPC into the main process, and inspect the rich clipboard format.

### TH04: recover a DOS bullet-ring calculation

Inspect the original PC-98 game's 16-bit instructions, recover the fixed and aimed angle calculations, and compare the reconstructed C++ with the historical compiler output.

If you've used REA on something interesting, share your case in an issue or a pull request, including the target, your question, how REA helped, and what you found.

## FAQ

**Which agents can use REA?**

Any agent that supports local MCP servers. Setup configures the supported agents; other clients can use manual MCP registration.

**Do I need Hopper, Ghidra or IDA?**

Deep native analysis uses one of them. Static JavaScript and .NET inspection work without a native analysis engine. Setup can install Hopper after approval; Ghidra and IDA use your existing installations.

**Do I need to start Hopper first?**

REA starts Hopper when an operation needs it. On macOS, a first-run dialog may ask you to choose demo mode or activate your license. Complete that prompt in the same user session before your first CLI/MCP operation or unattended job. Open Hopper manually if needed.

**What does installing the skill from skills.sh do?**

The skill supplies investigation instructions for your agent. Use `npx rea-agents setup` to register REA's MCP server and install the matching instructions, then restart your agent.

**What code does REA return?**

Native analysis returns pseudocode and assembly. JavaScript/Electron analysis recovers modules and their relationships. Your agent uses these findings to write and test an implementation.

**Does REA upload my app?**

REA analyzes targets locally. Your agent receives the tool results, and its model provider has its own data policy.

**What should I do if I hit a bug?**

Update first; a recent release may already fix it. For a CLI installed with `npm install --global` or `bun add --global`, run `rea update`. For agent setup through `npx`, run `npx rea-agents@latest setup`. If the problem persists, open an issue with your REA version, target type, steps to reproduce and error output.

## Documentation

Start with the website's worked guides (https://rea.tools/guides/). For exact options, prerequisites and result contracts: installation and setup, readiness and troubleshooting, CLI and Evidence, MCP contracts and agent prompts, tool catalog, and roadmap.

Report vulnerabilities through SECURITY.md.

## Star history

180,000 GitHub stars.

## Disclaimer

See DISCLAIMER.md for responsible-use guidance. The project's position on illegal or unauthorized use covers all REA versions, distribution channels, and platforms; each copy retains its applicable licenses. REA is for lawful research, education, interoperability, software preservation, and analysis of software you own or are authorized to examine.

## Contributing

Open an issue to report a bug or suggest a feature, or send a pull request to improve the code or docs. See CONTRIBUTING.md for development setup and checks, testing for verification lanes, and the architecture map.

## License

MIT. REA-authored code is licensed under MIT. Third-party material retains its own licenses and copyright notices; see Third-party notices for the dependency inventory, preserved license texts, and external-tool terms.

**You must legally obtain and be authorized to use commercial tools**, including IDA Pro / Hex-Rays decompilers, Hopper, and JEB, under their applicable licenses. REA grants no tool license, key, or activation entitlement. Trials and demos remain subject to vendor terms, including user, feature, automation, and output sharing restrictions. Cracked copies, stolen keys, unauthorized key sharing, and bypassing license restrictions are not authorized. This guidance does not amend MIT or third-party licenses.
