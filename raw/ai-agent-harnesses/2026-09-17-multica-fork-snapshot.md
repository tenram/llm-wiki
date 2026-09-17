# Multica (fork snapshot, Sep 2026)

> Source: https://github.com/amhed/multica
> Collected: 2026-09-17
> Published: Unknown

A fork of multica-ai/multica (5,347 commits), adding a staging deploy card. Core README (Sep 2026) reflects the upstream project's current state:

## Positioning

"Agents that show up on the board." An open-source workspace where you assign work to AI coding agents the way you'd assign it to a teammate — they pick up the issue, report progress, raise blockers, and hand it back for review. Self-hostable, works with **26 agent CLIs**, no lock-in. "Your next 10 hires won't be human."

## Feature areas

- **Build the team** — 26 agent CLIs (Claude Code, Codex, Cursor, Copilot, Kimi, OpenCode, and more); agents as teammates (name, provider, runtime); Squads (agent+human teams, leader routes work); Skills (solved problems become reusable playbooks); your own runtime (daemon on laptop or cloud box, code never leaves it).
- **Hand off the work** — Assign an issue (agent takes it from there); Autopilots (standups, audits, reports on cron); Chat; Projects (group work, attach repos/docs as context).
- **Stay in the loop** — Execution log (replay every tool call, timestamped); token usage per agent/issue; review gates (work lands in review, not main); Inbox (pinged when an agent needs a call); retries and timeouts.
- **Make it yours** — Self-host everything (Docker Compose or Helm); any Git host (GitHub, GitLab, Gitea, Forgejo); workspaces; roles (owner/admin/member) and access scopes; security model; Slack, Lark, DingTalk, WeCom, Telegram channels; web/desktop/mobile; CLI and API.

## Runtimes (26)

claude, codex, cursor-agent, copilot, opencode, openclaw, hermes, pi, agy (Antigravity), codebuddy, deveco, grok, kimi, kiro-cli, qodercli, qoderclicn, qwen, qwenpaw, reasonix, traecli, dsh, omp, mcode, dim, codearts, and more. Multica does not ship a model — it drives the agent CLIs you already have installed and authenticated.

## Architecture

Web: Next.js 16 (App Router). Desktop: Electron sharing web UI packages. Mobile: Expo/React Native (iOS). Backend: Go (Chi router, sqlc, gorilla/websocket). Database: PostgreSQL 17 (pgcrypto + pg_trgm). Agent runtime: local daemon executing any of the 26 agent CLIs, tasks over WebSocket.

## Getting started

Sign up at multica.ai or download Multica Desktop (auto-registers the computer as a runtime). Self-host: `curl -fsSL https://raw.githubusercontent.com/multica-ai/multica/main/scripts/install.sh | bash -s -- --with-server` then `multica setup self-host`.

## Fork addition: staging deploy card

Shows the latest GitHub Actions staging deploy of each tracked repo in the sidebar footer, fed by a cron script writing a JSON snapshot (`GET /api/deploy`). Configured via `MULTICA_DEPLOY_FILE` env var, `DEPLOY_TARGETS="owner/repo:workflow-file[:workspace-slug]"`. Resolves each run's head commit to the PR that introduced it, taking the last `KEY-123` token in the PR title as the Multica issue identifier.

## Why "Multica"

**Mul**tiplexed **I**nformation and **C**omputing **A**gent — a nod to Multics, the 1960s time-sharing OS. Software teams have been single-threaded ever since; agents make time-sharing relevant again, with both humans and machines multiplexing the system.

## License

Multica License — Apache 2.0 text plus additional conditions covering hosted services, commercial embedding, and branding.