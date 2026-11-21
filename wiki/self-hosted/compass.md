# Compass

> Sources: adinhodovic, Unknown date
> Raw: [Compass (adinhodovic/compass)](../../raw/self-hosted/2026-10-16-compass.md)

## Overview

Compass is an open-source (Apache-2.0), self-hosted landing page for services, dashboards, and documents. Instead of hand-maintaining a pile of cards, you add one or more discovery sources and Compass renders whatever is exposed in a server-driven UI with source status, tags, metadata, and operator context. It is a Go application, distributed as a container image and a Helm chart, with docs at adinhodovic.github.io/compass.

## Discovery Sources

Compass pulls service information from:

- **Docker** (via the Docker socket, or a socket proxy such as `tecnativa/docker-socket-proxy`)
- **Kubernetes** (in-cluster discovery with RBAC granted by the Helm chart)
- **Tailscale** and **Headscale**
- **Static config** and a **JSON API**

Each source reports health and refresh status, and contributes services with metadata, panels, and tags.

## UI and Stack

The interface is server-rendered HTML built with HTMX, Alpine.js, Tailwind, and daisyUI, so it works without a heavy client-side framework. It provides search, filter, debug views, and jump-into-service navigation.

## Deployment

A minimal config declares an organization and a list of sources:

```yaml
organization:
  name: Homelab

services:
  sources:
    - type: docker
      name: local
```

Docker runs the image with the host's docker GID added and the socket mounted read-only; Kubernetes installs the chart `oci://ghcr.io/adinhodovic/charts/compass` and grants in-cluster RBAC for discovery.

## Positioning

Compass sits alongside other self-hosted dashboards (e.g. [Beszel](../server-monitoring/beszel.md) for monitoring, [Linux Dash](../server-monitoring/linux-dash.md) for live stats) but its focus is service catalog and navigation rather than metrics: it answers "what is running and where do I go," and keeps itself current by discovering from infrastructure rather than requiring manual entries.

## See Also

- [Beszel](../server-monitoring/beszel.md) — lightweight hub+agent monitoring (metrics, not service catalog).
- [copyparty](copyparty.md) — another self-hosted service in this topic.
- [Dokploy](dokploy.md) — self-hosted VPS application and database deployment platform.
