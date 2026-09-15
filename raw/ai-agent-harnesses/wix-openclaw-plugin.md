# @lacneu/wix-openclaw

> Source: https://libraries.io/npm/@lacneu%2Fwix-openclaw
> Collected: 2026-07-31
> Published: 2026-05-03

An OpenClaw plugin (npm package `@lacneu/wix-openclaw`, v0.2.2, MIT licensed) enabling AI agents to manage Wix websites programmatically. Registers roughly 50 tools across a dozen Wix products: blog, CMS, forms, bookings, contacts, events, reviews.

## Features

- Authenticated HTTP client with automatic header injection (Wix's non-standard pattern: raw API key in the Authorization header, no "Bearer" prefix)
- Site UUID whitelist enforcement to prevent cross-site accidents
- Approval gating for destructive operations (publish, delete, cancel)
- Exponential backoff retry logic for rate limits and server errors

Requires OpenClaw ≥ v2026.4.0 and a Wix API key with minimal permissions plus an allow-list of site IDs. Wraps the official Wix REST API.
