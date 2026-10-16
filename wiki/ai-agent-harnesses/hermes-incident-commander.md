# Hermes Incident Commander

> Sources: Lethe044, Unknown date
> Raw: [Hermes Incident Commander (Lethe044)](../../raw/ai-agent-harnesses/2026-10-16-hermes-incident-commander.md)

## Overview

Hermes Incident Commander (MIT, Python 3.10+) is an autonomous SRE agent that detects, diagnoses, and self-heals production incidents, then learns from each one. It was originally built on [Hermes Agent](../agent-memory-systems/hermes-agent.md) by Nous Research for the "Show us what Hermes Agent can do" hackathon, and it now also ships a **standalone watchdog** that runs on any Linux host with nothing but an Anthropic API key — no Hermes install required. It is a concrete demonstration of using every Hermes harness feature (memory, skill auto-creation, cron, gateway, subagents, session search, execute_code, MCP) in one coherent workflow.

## The Loop

Incident alert → DETECT (CPU/memory/disk/services) → TRIAGE (P0–P3) → DIAGNOSE (logs/processes/stack traces) → REMEDIATE (tier 1→2→3) → VERIFY → LEARN (post-incident report, new prevention `SKILL.md`, MEMORY.md update, FTS5 search). A cron scheduler triggers detection (every 5 min health check, hourly audit, daily 08:00 briefing); a gateway delivers alerts to Telegram/Discord/PagerDuty.

## Two Very Different Risk Profiles

- **Demo / RL training** gives the model full terminal access — only safe in a disposable sandbox/VM/container.
- **Standalone watchdog** never gives the model shell access. It collects real metrics with `psutil`, sends only numbers to Claude, and restricts remediation to an explicit allow-list (restart *this* service, clean *this* log directory). `--dry-run` previews exactly what would be restarted or deleted without doing it. A written SAFETY.md documents the threat model.

This split is the project's most reusable idea: the same agent capability is safe or dangerous depending entirely on whether it is given raw shell access or a narrow, human-configured allow-list.

## Standalone Watchdog Features

- Thresholds for CPU/memory/disk plus failed systemd units, with `--adaptive-thresholds` learning a per-hour baseline (can only *raise* the effective threshold above the configured value, capped at 1.5x, so a real incident can't train the watchdog into ignoring itself).
- Notification fan-out to Discord, Slack, Microsoft Teams, a generic webhook (with a configurable payload template), and/or PagerDuty (Events API v2, with auto-resolve and retry/backoff on transient failures).
- Flapping detection (3+ same-category incidents within an hour) that also proposes a concrete new threshold, and throttles repeat pages for the same ongoing flap.
- Quiet hours / maintenance windows: breaches are still detected, reported, and indexed, but outbound notifications are suppressed; a breach still active when the window closes triggers one "still ongoing" notice.
- Local incident index in SQLite with full-text search (`incident_db.py --search`, `--stats`, `--prune` with `--archive`), with CSV/JSON export.
- Offline, self-contained HTML dashboard (severity/category breakdown, 14-day trend, searchable table, CSV export) with no server or external requests.
- Prometheus `/metrics` endpoint (read-only, localhost-bound) plus a ready-to-import Grafana dashboard JSON.
- `--validate-config` for typo/threshold/allow-list validation; `scripts/install-watchdog.sh` for one-command systemd install (dry-run by default, secrets written to a root-only file) with an optional daily prune timer.

## Hermes Feature Mapping

The README's table is a useful catalogue of what a persistent-memory agent harness enables: persistent memory builds a system topology map and learns which remediations work; skill auto-creation writes a new `SKILL.md` prevention playbook after every novel incident; cron schedules health checks and briefings; the gateway delivers alerts; subagents investigate nginx/database/application layers in parallel; FTS5 session search answers "have we seen this error before?"; `execute_code` collapses multi-step diagnostics into single turns; and MCP connects cloud provider APIs for auto-scaling remediation.

## RL Training Environment

An Atropos RL environment with 10 incident scenarios (service crash, disk full, memory leak, Docker/Kubernetes/ECS crash loops, network unreachable, CPU runaway, failed systemd unit, Lambda timeout). The reward function weights Resolution 50, RCA Quality 15, Report Quality 15, Skill Created 10, Response Speed 5, Tool Efficiency 5. The project ships 220 pytest cases and CI across Python 3.10–3.12.

## See Also

- [Hermes Agent (Nous Research)](../agent-memory-systems/hermes-agent.md) — the underlying multi-platform agent with persistent memory and subagents.
- [Hermes Skills Ecosystem](hermes-skills-ecosystem.md) — how Hermes distributes built-in, optional, and community skills.
- [Beszel](../server-monitoring/beszel.md) — a monitoring tool whose alerting this project automates a response to.
