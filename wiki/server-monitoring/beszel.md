# Beszel

> Sources: henrygd, 2026-08-24
> Raw: [Beszel](../../raw/server-monitoring/2026-08-24-beszel.md)

## Overview

Lightweight, actively maintained server monitoring platform (Go + PocketBase hub, Svelte UI): Docker stats, historical data, alerts, multi-user with OAuth2/OIDC, automatic backups to disk or S3. MIT licensed. Two components: a **hub** (web app, SQLite-backed) and an **agent** per monitored machine communicating over SSH or WebSocket; unix socket supported for same-host agents.

## Metrics

CPU, memory (incl. swap/ZFS ARC), disk usage and I/O, network, load average, temperatures, fan speeds (hwmon), GPU usage/power draw (Nvidia/AMD/Intel), battery, per-container stats (Docker/Podman), and S.M.A.R.T. disk health including eMMC wear and mdraid.

## Deployment notes

Docker images or native static Go binaries with official hardened systemd installers. Practical gotchas from real deployment: SMART collection needs smartctl privileges — under `NoNewPrivileges=yes` units file capabilities are ignored, so grant `AmbientCapabilities=CAP_SYS_RAWIO CAP_SYS_ADMIN` in the unit instead; agents need docker-group membership for container stats; `SERVICE_PATTERNS` scopes systemd service monitoring.

## See Also

- [Linux Dash](linux-dash.md)
