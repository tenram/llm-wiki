# Dokploy

> Sources: Dokploy, 2026-11-03
> Raw: [Dokploy README](../../raw/self-hosted/2026-11-03-dokploy.md)

## Overview

Dokploy is a free, self-hostable Platform as a Service (PaaS) for deploying and managing applications and databases on a VPS. Its README positions it as an open-source alternative to Vercel, Netlify, and Heroku, combining application deployment, database operations, Docker management, routing, monitoring, backups, and notifications in one control plane.

## Deployment Surface

Dokploy supports applications written in Node.js, PHP, Python, Go, Ruby, and other application types. It provides native Docker Compose support, one-click deployment templates, Docker container management, and a CLI/API for managing applications and databases. The documented quick start installs it on a VPS through the project's shell installer; Dokploy Cloud is offered as an alternative to self-hosting.

## Infrastructure Features

- **Databases:** MySQL, PostgreSQL, MongoDB, MariaDB, libsql, and Redis.
- **Networking:** Traefik integration for routing and load balancing.
- **Scaling:** Multi-node deployments managed through Docker Swarm, plus deployment to external servers.
- **Operations:** Automated database backups, resource monitoring, and deployment-success or failure notifications through Slack, Discord, Telegram, email, and other channels.
- **Observability:** Container and host logs and metrics can be shipped to services including Grafana's Loki and Prometheus/Mimir, Datadog, New Relic, InfluxDB, VictoriaMetrics, Better Stack, Elasticsearch/OpenSearch, Splunk, and AWS CloudWatch.

## Positioning

Dokploy is a broad self-hosted deployment platform rather than a single-purpose service. It is aimed at operators who want a VPS-based application platform with a web-oriented control surface and integrated infrastructure features, while retaining the option of a hosted cloud offering. The README does not by itself establish licensing terms, production limits, security properties, or the behavior of every listed integration; those require checking the repository's current documentation and configuration.

## See Also

- [Compass](compass.md) — self-hosted service catalog and infrastructure discovery dashboard.
