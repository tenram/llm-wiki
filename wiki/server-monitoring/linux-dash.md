# Linux Dash

> Sources: tariqbuilds, 2026-08-24
> Raw: [linux-dash](../../raw/server-monitoring/2026-08-24-linux-dash.md)

## Overview

A simple, low-overhead (~400KB) web dashboard for Linux systems. Four included server stacks: Node.js (recommended), Go, Python, PHP. The metrics engine is a bash script shelling out to coreutils and procfs — CPU, RAM/swap, disks, bandwidth, processes, Docker containers, users, cron, network connections.

## Status

Effectively unmaintained: last upstream push April 2024, issue creation restricted, and an open shell-injection-class issue (#498) never fixed. No built-in authentication whatsoever — upstream states plainly that installations must be protected by an external measure (firewall or reverse proxy). Known modern-platform issues: PHP-mode JSON escaping bugs, Node JSON serialization errors, missing net-tools silently disabling several network modules.

## When it still fits

Single-host, trusted-network-only, real-time glance value where deploying a hub+agent system is overkill. For anything multi-host, historical, or alert-driven, [Beszel](beszel.md) supersedes it on every axis.

## See Also

- [Beszel](beszel.md)
