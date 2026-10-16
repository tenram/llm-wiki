# Hermes Incident Commander (Lethe044)

> Source: https://github.com/Lethe044/hermes-incident-commander
> Collected: 2026-10-16
> Published: Unknown

## About

Autonomous SRE agent that detects, diagnoses, and self-heals production incidents - with a standalone watchdog that needs no Hermes install, just an Anthropic API key. Memory + Skills + Cron + Gateway + Subagents + Atropos RL.

- Repository: Lethe044/hermes-incident-commander
- License: MIT
- Language: Python 3.10+
- Stars: 72; Forks: 4; Commits: 17
- Topics: anthropic, atropos, automation, autonomous-agents, claude-ai, devops, hermes-agent, incident-response, kubernetes, llm-agent, mttr, nous-research, observability, pagerduty, python, self-healing, site-reliability-engineering, sre
- Originally built on Hermes Agent (NousResearch) for the "Show us what Hermes Agent can do" hackathon.

## README

> An autonomous SRE agent that detects, diagnoses, and heals production infrastructure - then learns from every incident it resolves.

Originally built on Hermes Agent by NousResearch for the "Show us what Hermes Agent can do" hackathon. Now also ships a standalone watchdog that runs on any real Linux host with nothing but an Anthropic API key - no Hermes installation required.

### What's New (selected)

- Microsoft Teams notification channel (`TEAMS_WEBHOOK_URL`).
- Flapping/quiet-hours Prometheus gauges (`hermes_watchdog_flapping`, `hermes_watchdog_in_quiet_hours`) on `/metrics`.
- Scheduled `--prune` via the systemd installer (`--with-prune-timer`).
- `--prune --archive DIR` for cold storage.
- `incident_db.py --prune` removes incidents older than `--older-than-days` (dry-run by default, `--yes` to delete).
- "Still ongoing" notification after quiet hours end.
- Configurable generic-webhook payload template (`GENERIC_WEBHOOK_TEMPLATE`).
- Download CSV button in the offline dashboard; clickable category chart.
- `incident_db.py --stats --format csv`.
- Flapping incidents suggest a concrete threshold fix and throttle repeat notifications.
- `incident_db.py --stats` (totals, by severity/category, auto-remediation rate, last 7/30 days, busiest category).
- Category breakdown chart and 14-day trend chart in the offline dashboard.
- Fixed a path-isolation bug in `flapping.py`, `baseline.py`, `incident_db.py` (paths now resolved fresh on every call).
- `--validate-config` checks a `watchdog_config.yaml` for typos, out-of-range thresholds, invalid allow-list entries.
- CSV/JSON export from `incident_db.py --search`.
- Search box in the offline dashboard.
- Notifier retry/backoff.
- Flapping detection (3+ incidents of the same category within an hour).
- `scripts/install-watchdog.sh` one-command systemd install.
- Local incident search (`monitor/incident_db.py`: SQLite + FTS).
- Adaptive, time-of-day-aware thresholds (`--adaptive-thresholds`).
- 10 incident scenarios (Docker, Kubernetes, ECS, Lambda + service/disk/memory/CPU/network).
- Prometheus `/metrics` + ready-to-import Grafana dashboard JSON; `--dry-run`.
- PagerDuty integration (trigger + auto-resolve), alongside Discord/Slack.
- Standalone Watchdog (CPU/memory/disk + failed systemd units, Claude-powered triage, opt-in safe auto-remediation).
- Offline HTML dashboard, CI on every push, SAFETY.md threat model, ROADMAP.md.

### The Problem

When a production server goes down at 3 AM, an on-call engineer has to: wake up and check alerts; SSH in and run diagnostics manually; piece together root cause from logs; apply a fix; verify it worked; write a post-mortem nobody will read. "Mean time to resolve (MTTR) for P0 incidents averages 45–60 minutes. Much of that is humans doing things a sufficiently capable agent could do faster and better."

### Demo

```sh
pip install anthropic rich
export ANTHROPIC_API_KEY=sk-ant-...
python demo/demo_incident.py --scenario disk-full-logs
python demo/demo_incident.py --scenario svc-crash-nginx
python demo/demo_incident.py --scenario cpu-runaway-process
```

Hermes detects the incident and classifies severity (P0/P1/P2/P3), runs parallel diagnostics, identifies root cause with explicit reasoning, applies the safest effective fix, verifies it, writes a structured post-incident report to `~/.hermes/incidents/`, and creates a new prevention skill in `~/.hermes/skills/`. The demo and the RL training environment give the model full terminal access — only run them in a disposable sandbox/VM/container.

### Standalone Mode (No Hermes Required)

`monitor/watchdog.py` runs as an always-on process on any Linux host and needs nothing but `ANTHROPIC_API_KEY`:

```sh
pip install -e .              # or: pip install -r requirements.txt psutil
export ANTHROPIC_API_KEY=sk-ant-...
export DISCORD_WEBHOOK_URL=...
export SLACK_WEBHOOK_URL=...
export TEAMS_WEBHOOK_URL=...
export PAGERDUTY_ROUTING_KEY=...
export GENERIC_WEBHOOK_URL=...
export GENERIC_WEBHOOK_TEMPLATE='{"text": {message}}'

python -m monitor.watchdog --once
python -m monitor.watchdog --dry-run
python -m monitor.watchdog --cpu-threshold 85 --interval 30
python -m monitor.watchdog --config monitor/watchdog_config.yaml --auto-remediate
python -m monitor.watchdog --metrics-port 9877
python -m monitor.watchdog --adaptive-thresholds
python -m monitor.incident_db --search "nginx" --format json
python -m monitor.incident_db --stats
python -m monitor.incident_db --prune --older-than-days 90 --archive /backup/incidents --yes
python -m monitor.watchdog --config monitor/watchdog_config.yaml --validate-config
./scripts/install-watchdog.sh
```

Unlike the demo/training environment, the watchdog never gives the model shell access. It collects real metrics with `psutil`, sends only numbers to Claude, and any remediation is restricted to an explicit allow-list you configure. `--adaptive-thresholds` learns a running mean/stddev per hour-of-day and can only ever raise the effective threshold above what you configured (never lower), capped at 1.5x the static threshold.

`monitor/notifier.py` fans an alert out to Discord, Slack, Microsoft Teams, a generic webhook, and/or PagerDuty (Events API v2), retrying transient failures with exponential backoff.

Flapping: 3+ incidents of the same category within an hour get flagged in the report, console, and dashboard; for cpu/mem/disk the banner proposes a concrete new threshold.

Quiet hours: recurring daily UTC windows where breaches are still detected/reported/indexed but outbound notifications are suppressed. If a breach is still active once the window closes, the next poll sends one notification noting how long it's been running.

Incidents are indexed by `monitor/incident_db.py` (SQLite + FTS5 when available, falling back to `LIKE`). `--stats` prints a quick summary; `--prune` bounds disk usage. `--validate-config` flags unrecognized keys, out-of-range thresholds, negative intervals, malformed quiet-hours windows, and allow-list entries that don't match anything.

`scripts/install-watchdog.sh` installs the systemd unit in one command (dry-run by default; writes API key/secrets to a root-only file). `--with-prune-timer` adds a daily prune timer; `--uninstall --yes` removes everything.

`python -m monitor.dashboard --open` writes a single self-contained HTML file (no server, no external requests) summarizing incident counts by severity and category, a 14-day trend, auto-remediation rate, and a searchable table with CSV export.

Prometheus: `--metrics-port` starts a dependency-free `/metrics` endpoint (`monitor/prometheus_exporter.py`) exposing `hermes_watchdog_cpu_percent`, `hermes_watchdog_mem_percent`, `hermes_watchdog_disk_percent`, `hermes_watchdog_failed_services_count`, a `hermes_watchdog_breach{metric="..."}` gauge, and the flapping/quiet-hours gauges. Binds to `127.0.0.1` and is read-only. A Grafana dashboard JSON ships in `docs/assets/grafana-dashboard.json`.

### How It Uses Every Hermes Feature

- **Persistent Memory** — builds a system topology map over time; learns which services fail together, time-of-day patterns, and which remediations work on your infrastructure.
- **Skill Auto-Creation** — after every novel incident, writes a new `SKILL.md` prevention playbook.
- **Cron Scheduler** — every 5 min critical health check; hourly full audit; daily 08:00 morning briefing to Telegram.
- **Gateway (Telegram/Discord/PagerDuty)** — real-time P0 alerts, resolution notices, daily briefings.
- **Subagent Spawning** — parallel subagents to investigate nginx, database, and application layers simultaneously.
- **Session Search (FTS5)** — "Have we seen this error before?" searches past incidents.
- **execute_code** — collapses multi-step diagnostic pipelines into single inference turns.
- **MCP Integration** — connects to cloud provider APIs (AWS/GCP/Azure MCP servers) for auto-scaling and cloud-native remediation.

### Architecture

Incident alert → DETECT (CPU/memory/disk/services) → TRIAGE (P0–P3) → DIAGNOSE (logs/processes/stack traces) → REMEDIATE (tier 1→2→3) → VERIFY → LEARN (post-incident report, prevention SKILL.md, MEMORY.md update, FTS5 search). A CRON scheduler triggers DETECT; a GATEWAY delivers alerts and briefings.

### Project Structure

`skills/incident-commander/SKILL.md` (install into `~/.hermes/skills/`); `environments/incident_env.py` (Atropos RL environment, 10 scenarios) and `incident_config.yaml`; `demo/demo_incident.py`; `monitor/` (`watchdog.py`, `notifier.py`, `dashboard.py`, `prometheus_exporter.py`, `incident_db.py`, `baseline.py`, `flapping.py`); `scripts/install-watchdog.sh`; `tests/` (220 pytest cases); `docs/`; `.github/workflows/ci.yml`.

### Installation (Full Hermes Setup)

1. Install Hermes Agent: `curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash`
2. Configure Hermes: `hermes setup`, `hermes model`, `hermes gateway setup`
3. Install the Incident Commander Skill: `cp -r skills/incident-commander ~/.hermes/skills/`; verify with `/skills`
4. Set up monitoring cron jobs (in conversation: health check every 5 minutes, P0/P1 alerts to Telegram, daily 08:00 briefing).
5. Optional RL training environment: `pip install atroposlib`; `python environments/incident_env.py process --config environments/incident_config.yaml`; `python environments/incident_env.py serve --config environments/incident_config.yaml`.

### Reward Function (for RL Training)

Multi-component reward: Resolution 50, RCA Quality 15, Report Quality 15, Skill Created 10, Response Speed 5, Tool Efficiency 5.

### Incident Scenarios (Training Scenarios)

| ID | Severity | Category | Description |
|---|---|---|---|
| svc-crash-nginx | P0 | service | nginx crashed, website unreachable |
| disk-full-logs | P1 | disk | 95% disk usage from exploded log files |
| memory-leak-process | P1 | memory | Mystery process eating 150MB+ |
| docker-container-crash | P1 | docker | Container stuck in a restart/crash loop |
| k8s-pod-crashloop | P1 | kubernetes | Pod stuck in CrashLoopBackOff |
| ecs-task-crashloop | P1 | ecs | ECS task stuck in a deploy/rollback loop |
| network-unreachable | P1 | network | Upstream dependency unreachable, timeouts spiking |
| cpu-runaway-process | P2 | cpu | 95% CPU from runaway computation |
| failed-systemd-unit | P2 | service | Custom worker service in failed state |
| lambda-timeout-spike | P2 | lambda | Lambda function timing out on cold starts |

### Running Tests

`python environments/incident_env.py --smoke-test` (stdlib + pyyaml); `pytest tests/ -v` (220 tests). CI runs across Python 3.10, 3.11, 3.12 on every push/PR.

### Why This Project Is Worth Using

Real problem, real impact; uses every Hermes capability; self-improving; closes the training loop via the Atropos RL environment; works standalone on a real host with an explicit, documented safety model instead of giving an LLM raw shell access; ships with working code and CI.

### Safety

Read SAFETY.md before pointing anything in this repo at a machine you care about — demo mode and the watchdog have very different risk profiles.

### License

MIT.
