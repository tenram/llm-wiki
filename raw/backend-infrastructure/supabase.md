# Supabase

> Source: https://github.com/supabase/supabase
> Collected: 2026-07-31
> Published: Unknown

Supabase describes itself as "the Postgres development platform," offering Firebase-like developer ergonomics built on open-source tools.

## Features

- **Database**: hosted, fully managed PostgreSQL
- **Authentication**: JWT-based user management via GoTrue
- **APIs**: auto-generated REST and GraphQL, plus real-time subscriptions
- **Serverless functions**: database functions and edge functions
- **File storage**: S3-based, with permissions enforced through PostgreSQL
- **Vector/AI tools**: embeddings toolkit for AI applications
- **Dashboard**: web-based management UI

## Architecture

Combines PostgreSQL (core database), PostgREST (API generation), Realtime (an Elixir server for WebSocket subscriptions), and Kong (API gateway). Official client libraries for JavaScript, Python, Flutter, and Swift; community SDKs for Go, Rust, C#, and others. 107,000+ GitHub stars, 37,000+ commits, Apache 2.0 licensed.
