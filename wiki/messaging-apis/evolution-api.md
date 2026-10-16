# Evolution API

> Sources: Evolution Foundation, Unknown date
> Raw: [Evolution API README](../../raw/messaging-apis/2026-10-13-evolution-api.md)

## Overview

Evolution API is a production-ready, open-source REST API for WhatsApp and multi-channel messaging, maintained by Evolution Foundation. Originally a WhatsApp controller API built on the Baileys WhatsApp-Web library (via CodeChat), it has grown into a multi-provider platform supporting both unofficial (Baileys-based WhatsApp Web) and official (Meta WhatsApp Cloud API) connections, plus integrations with chatbots, CRMs, event streams, and storage. Apache 2.0 licensed with brand-protection conditions.

## Connection Types

- **WhatsApp API (Baileys)** — free, based on WhatsApp Web via the Baileys library; suited to multi-service chats, service bots, and WhatsApp-integrated systems, but limited by reliance on the web version.
- **WhatsApp Cloud API (official)** — Meta's official API for higher volumes and stronger integration (end-to-end encryption, analytics, customer-service tooling); requires Meta policy compliance and may incur per-message costs.

## Integrations and Architecture

Event-driven, multi-provider architecture with channel, chatbot, event, and storage layers:

- **Chatbot**: Typebot, Chatwoot, OpenAI (incl. audio-to-text transcription), Dify, Flowise, N8N.
- **Events**: WebSocket, Socket.io, RabbitMQ (AMQP), Apache Kafka, Amazon SQS, NATS, Pusher — configurable per instance.
- **Storage**: local, Amazon S3, or MinIO; automatic media download from WhatsApp.
- Built on Node.js 20+, TypeScript 5+, Express.js; PostgreSQL or MySQL via Prisma ORM; Redis recommended for caching.

## Authentication

API-key auth via the `apikey` header, instance-specific tokens for WhatsApp connection authentication, and webhook signature validation for external integrations.

## Deployment

Runs from source (Node.js + Postgres/MySQL + Redis) or via Docker image `evoapicloud/evolution-api` (port 8080). A HostGator-partnered VPS hosting option exists. Collects anonymous, non-personal telemetry (routes used, API version).

## See Also

- [WAHA](waha.md) — the main competing self-hosted WhatsApp HTTP API, Docker-first with a swagger UI.
