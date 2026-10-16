# WAHA — WhatsApp HTTP API

> Sources: devlikeapro (WAHA project), Unknown date
> Raw: [WAHA README](../../raw/messaging-apis/2026-10-13-waha.md)

## Overview

WAHA (**W**hats**A**pp **H**TTP **A**PI) is a self-hosted REST API for WhatsApp that installs via Docker and can be running in under five minutes. It exposes an HTTP API with Swagger documentation, letting clients start WhatsApp sessions, scan QR codes, and send messages without managing the WhatsApp Web client directly. Per the repo description, WAHA supports multiple engines: WEBJS (browser-based), NOWEB (websocket, Node.js), GOWS (websocket, Go), and WPP (browser).

## Quick Start Flow

1. `docker pull devlikeapro/waha` (or `devlikeapro/waha-plus` for the paid Plus build).
2. Run the container (`-p 3000:3000`) and open `http://localhost:3000` for the Swagger UI.
3. `POST /api/sessions` with a `{"name": "default"}` payload to start a session (the name field enables multiple WhatsApp accounts per container in Plus).
4. `GET /api/screenshot` to obtain the QR code; scan it with the WhatsApp mobile app.
5. `POST /api/sendText` with a `chatId` of the international number without `+` plus `@c.us` (e.g., `12132132131@c.us`) and a `text` field.

## Sessions and Sending

Sessions are named (e.g., `default`); chat IDs use WhatsApp's `<number>@c.us` format. Messages and other operations go through `/api/...` endpoints with JSON payloads, also usable via curl. A public dashboard and Swagger example are available at waha.devlike.pro.

## Development

Built with Node.js (>=22) and includes a `whatsapp-rust-bridge` that compiles Go WhatsApp-web proto definitions to WASM via a Rust nightly toolchain and Bun; dependencies installed with `yarn`.

## See Also

- [Evolution API](evolution-api.md) — competing self-hosted WhatsApp REST API, notable for also supporting Meta's official Cloud API and a wider event/chatbot integration surface.
