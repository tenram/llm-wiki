# ezBookkeeping

> Source: https://github.com/mayswind/ezbookkeeping
> Collected: 2026-10-10
> Published: Unknown

## Introduction

ezBookkeeping is an open source, powerful, self-hosted personal finance app that is easy to use. It helps you record daily transactions, import data from various sources, and quickly search and filter your bills. You can analyze historical data using built-in charts or perform custom queries with your own chart dimensions to better understand spending patterns and financial trends. ezBookkeeping is easy to deploy, and you can start it with just one single Docker command. Designed to be resource-efficient, it runs smoothly on devices such as home servers, NAS and Raspberry Pi.

ezBookkeeping offers tailored interfaces for mobile and desktop devices. With PWA (Progressive Web Apps) support, you can add it to your mobile home screen and use it like a native app.

## Features

- **Open Source & Self-Hosted**: Built for privacy and control.
- **Lightweight & Fast**: Minimal resource usage, suitable for home servers, NAS and Raspberry Pi.
- **Easy Installation**: Docker, SQLite, MySQL, PostgreSQL, cross-platform Windows/macOS/Linux support, and x86, amd64, and ARM architectures.
- **User-Friendly Interface**: Mobile and desktop UI, PWA support, customizable overview layouts, and dark mode.
- **AI-Powered Features**: Text and receipt image recognition, AI custom chart generation, MCP integration, and Agent Skill/API command-line tools.
- **Powerful Bookkeeping**: Two-level accounts and categories, transaction image attachments, location tracking, scheduled transactions, filtering, search, visualization, and analysis.
- **Localization & Internationalization**: Multi-language and multi-currency support, exchange-rate sources, time zones, and custom formats.
- **Security**: Two-factor authentication, OIDC, login rate limiting, and PIN/WebAuthn application lock.
- **Data Import & Export**: CSV, Excel, OFX, QFX, QIF, IIF, Camt.052, Camt.053, MT940, GnuCash, Firefly III, Beancount, and more, with custom mappings, rules, and scripts.

## Installation

### Run with Docker

    $ docker run -p8080:8080 mayswind/ezbookkeeping

For production use, mount a persistent volume to prevent data loss.

### Install from Binary

    $ ./ezbookkeeping server run

By default, ezBookkeeping listens on port 8080.

### Build from Source

    $ ./build.sh package -o ezbookkeeping.tar.gz

You can also build a Docker image with `./build.sh docker`.

## Documentation

Documentation is available in English and Simplified Chinese.

## License

[MIT](https://github.com/mayswind/ezbookkeeping/blob/master/LICENSE)
