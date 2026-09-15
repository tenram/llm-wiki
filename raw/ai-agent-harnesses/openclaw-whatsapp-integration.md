# Adding WhatsApp Integration to OpenClaw

> Source: https://blog.gopenai.com/openclaw-add-whatsapp-27d9237d3872
> Collected: 2026-07-31
> Published: Unknown

Walkthrough of wiring WhatsApp into OpenClaw so users can message the bot through WhatsApp.

## Steps

1. Run `openclaw onboard` on the server, launching an interactive (keyboard-navigated) configuration wizard
2. Progress through disclaimers, QuickStart mode selection, model authentication, and channel selection
3. Select the WhatsApp channel and scan the generated QR code from WhatsApp to link
4. Choose between a personal account or a dedicated phone number for the bot
5. For a dedicated account, WhatsApp issues a pairing code; approve it server-side with `openclaw pairing approve whatsapp <code>`
6. Message the bot on WhatsApp to confirm AI responses are working

## Caveat

The guide warns against enabling certain optional command-completion features, since they can trigger excessive CPU usage on the server.
