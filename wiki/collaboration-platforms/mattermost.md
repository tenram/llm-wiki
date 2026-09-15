# Mattermost

> Sources: Mattermost README, 2026-08-28
> Raw: [mattermost.md](../../raw/collaboration-platforms/mattermost.md)

## Overview

Mattermost is an open core, self-hosted collaboration platform for secure teamwork across the software development lifecycle. The repo is the main source for the platform and combines chat, automation, calling, and AI features with on-prem and cloud deployment options.

## Platform Profile

- chat and group collaboration
- workflow automation
- voice calling and screen sharing
- AI integration
- open core distribution with regular releases

## Architecture

The repository is built around a Go backend and React frontend, runs as a single Linux binary, and uses PostgreSQL. That makes it both an application repo and the authoritative source for the platform’s core implementation.

## Deployment and Ecosystem

The README points to:

- on-prem deployment
- cloud trial
- desktop and mobile clients
- documentation for admins and developers
- webhooks, slash commands, drivers, and plugins

## License and Release Model

Mattermost ships a compiled MIT-licensed version each month while the upstream platform repo remains the primary development source.
