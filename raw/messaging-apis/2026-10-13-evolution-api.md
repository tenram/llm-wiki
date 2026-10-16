# Evolution API

> Source: https://github.com/evolution-foundation/evolution-api
> Collected: 2026-10-13
> Published: Unknown

# Evolution API

Open-source REST API for WhatsApp and multi-channel messaging — part of the Evolution Foundation ecosystem.

## About

**Evolution API** is a powerful, production-ready REST API for WhatsApp and multi-channel messaging. Originally focused on WhatsApp, it has grown into a comprehensive platform supporting multiple messaging providers and integrations.

Today, Evolution API supports both the Baileys-based WhatsApp Web API and the official WhatsApp Cloud API, plus integrations with Typebot, Chatwoot, Dify, OpenAI, RabbitMQ, Apache Kafka, Amazon SQS, Socket.io, Amazon S3 / MinIO, and more.

Evolution API began as a WhatsApp controller API based on CodeChat, which in turn implemented the Baileys library. We continue to acknowledge CodeChat for laying the groundwork.

## Part of the Evolution Foundation ecosystem

Evolution API is one of the messaging engines maintained by Evolution Foundation. It is used as a WhatsApp provider by the Evo CRM Community and other projects in the ecosystem.

## Connection Types

Evolution API supports multiple connection types to WhatsApp:

### WhatsApp API — Baileys
A free API based on WhatsApp Web, leveraging the Baileys library. Suitable for multi-service chats, service bots, and WhatsApp-integrated systems. Note: this method relies on the web version of WhatsApp and may have limitations compared to official APIs.

### WhatsApp Cloud API
The official API provided by Meta. Designed for businesses with higher messaging volumes and stronger integration support, including end-to-end encryption, advanced analytics, and customer service tools. Requires compliance with Meta's policies and may incur per-message costs.

## Integrations

Evolution API integrates natively with many platforms:

- **Typebot** — conversational bots with trigger management
- **Chatwoot** — customer service platform
- **RabbitMQ** — event streaming via AMQP
- **Apache Kafka** — real-time event streaming and processing
- **Amazon SQS** — cloud-based message queuing
- **Socket.io** — real-time WebSocket events
- **Dify** — AI agent workflows
- **OpenAI** — AI capabilities including audio-to-text conversion
- **Amazon S3 / MinIO** — media file storage

## Quick Start

### Prerequisites

- **Node.js** 20+
- **PostgreSQL** or **MySQL**
- **Redis** (recommended for caching)

### Installation

```bash
git clone git@github.com:evolution-foundation/evolution-api.git
cd evolution-api

# Install dependencies
npm install

# Configure environment
cp .env.example .env
# Edit .env with your database, Redis, and API key
```

### Database setup

```bash
# Set the database provider
export DATABASE_PROVIDER=postgresql  # or mysql

# Generate Prisma client
npm run db:generate

# Deploy migrations
npm run db:deploy
```

### Running

```bash
# Development with hot reload
npm run dev:server

# Production build and run
npm run build
npm run start:prod
```

### Docker

```bash
docker pull evoapicloud/evolution-api:latest
docker run -p 8080:8080 --env-file .env evoapicloud/evolution-api:latest
```

## Architecture

Evolution API is built with a multi-provider, event-driven architecture:

```
Client / CRM
     ↓
Evolution API
  ├── Channel Integrations (Baileys / Cloud API)
  ├── Chatbot Integrations (Typebot, Chatwoot, OpenAI, Dify, Flowise, N8N)
  ├── Event Integrations (WebSocket, RabbitMQ, SQS, NATS, Pusher)
  └── Storage Integrations (S3, MinIO)
```

Built with **Node.js 20+**, **TypeScript 5+**, and **Express.js**, it provides extensive integrations with chatbots, CRM systems, and messaging platforms.

### Multi-database support
PostgreSQL and MySQL via Prisma ORM with provider-specific schemas and migrations.

### Authentication
- API key-based authentication via `apikey` header
- Instance-specific tokens for WhatsApp connection authentication
- Webhook signature validation for external integrations

### Message queue support
RabbitMQ, Amazon SQS, NATS, Pusher and WebSocket for events. Configurable per instance.

### Media handling
Local storage or S3/MinIO. Automatic media download from WhatsApp. Optional audio transcription via OpenAI.

## Hosting

Deploy Evolution API with optimized infrastructure through the HostGator partnership: Evolution API VPS — HostGator (https://evolution-api.com/vps-evolution-api).

## Telemetry

Evolution API collects anonymous telemetry data (routes used, most accessed routes, API version) to help improve the service. **No sensitive or personal data is collected.**

## Security

For security issues, do not open a public issue. Email suporte@evofoundation.com.br or use GitHub's private vulnerability reporting.

## Acknowledgments

- CodeChat — original WhatsApp API foundation
- Baileys — WhatsApp Web library

## License

Evolution API is licensed under the Apache License 2.0, with additional brand-protection conditions (LOGO/copyright preservation and Usage Notification requirement).

"Evolution Foundation", "Evolution" and "Evolution API" are trademarks of Evolution Foundation.
