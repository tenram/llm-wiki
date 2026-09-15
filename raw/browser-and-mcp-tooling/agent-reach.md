# Agent Reach

> Source: https://github.com/Panniantong/agent-reach
> Collected: 2026-08-28
> Published: Unknown

<h1 align="center">👁️ Agent Reach</h1>

**给你的 AI Agent 一键装上互联网能力**

当下最稳的接入方式，替你选好、装好、体检好——接入方式会换代，你不用操心。

## Why Agent Reach?

It fills the gap where agents can write and reason, but struggle to read the web:

- YouTube transcripts
- Twitter/X search and timelines
- Reddit posts and comments
- Bilibili search and video details
- GitHub repo reading and search
- RSS/Atom feeds
- LinkedIn, Facebook, Instagram, Xiaohongshu with login-aware routes

## Design

Agent Reach is a capability layer, not a single tool.

It handles:

- selection
- installation
- diagnostics
- routing across fallback backends

Examples of backend routing:

```text
web.py → Jina Reader
twitter.py → twitter-cli ▸ OpenCLI ▸ bird
youtube.py → yt-dlp
github.py → gh CLI
reddit.py → OpenCLI ▸ rdt-cli
rss.py → feedparser
exa_search.py → Exa via mcporter
```

## Safety

- Credentials stay local
- Default install is read-only
- `--dry-run` previews actions
- Login-heavy channels are opt-in

## Usage

Tell the agent to install or update Agent Reach with the repo-hosted docs links. After installation, `agent-reach doctor` reports which channels are working and which backend is active.
