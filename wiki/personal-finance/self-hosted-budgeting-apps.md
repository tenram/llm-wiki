# Self-Hosted Budgeting and Personal Finance Apps

> Sources: teelur, 2026-10-10; mayswind, 2026-10-10; Actual Budget contributors, 2026-10-10; Awesome Selfhosted maintainers, 2026-10-10
> Raw: [Budget Board](../../raw/personal-finance/2026-10-10-budget-board.md); [ezBookkeeping](../../raw/personal-finance/2026-10-10-ezbookkeeping.md); [Actual Budget](../../raw/personal-finance/2026-10-10-actual-budget.md); [Awesome Selfhosted money catalog](../../raw/personal-finance/2026-10-10-awesome-selfhosted-money-budgeting.md)

## Overview

Self-hosted personal-finance tools span focused monthly budgeting, transaction bookkeeping, and local-first envelope budgeting. Budget Board emphasizes accounts, assets, goals, CSV import, bank-sync providers, and learned categorization. ezBookkeeping emphasizes broad import/export support, lightweight deployment, mobile/PWA use, multi-currency bookkeeping, and optional AI/MCP integrations. Actual centers local-first data with synchronization and envelope budgeting. The Awesome Selfhosted catalog places all three in a wider field that also includes accounting, shared-expense, investment, invoicing, and subscription tools.

## Product Profiles

### Budget Board

Budget Board is presented as a self-hosted alternative to Mint. Its scope combines account and asset tracking, categorized transactions, monthly category budgets, financial goals, and trend charts. It also lists CSV import, SimpleFIN and Lunchflow synchronization, automatic rules, and a machine-learning categorization model. Local two-factor authentication and OIDC are listed as authentication options. The Awesome Selfhosted catalog identifies a GPL-3.0 license and Docker-oriented deployment metadata.

### ezBookkeeping

ezBookkeeping is positioned as a resource-efficient application for home servers, NAS devices, and Raspberry Pi. The README lists Docker installation, SQLite/MySQL/PostgreSQL support, cross-platform binaries, responsive mobile and desktop interfaces, PWA support, and dark mode. Its bookkeeping model includes two-level accounts and categories, scheduled transactions, attachments, location tracking, charts, search, and analysis. It claims unusually broad financial-data import support, including CSV, Excel, OFX, QFX, QIF, IIF, several bank formats, GnuCash, Firefly III, and Beancount. It also lists multi-currency support, 2FA, OIDC, WebAuthn or PIN locking, receipt recognition, MCP, and agent/API command-line tools.

### Actual Budget

Actual describes itself as a free, open-source, local-first personal finance tool written in NodeJS. Its distinguishing workflow is envelope budgeting, with synchronization so changes can move between devices. Deployment options include PikaPods, Fly.io, Docker, and local Windows, macOS, and Linux applications. The repository separates the cross-platform `loot-core`, desktop client, and Electron desktop packages, while community documentation covers budgeting, account management, migration, and contributions.

## Comparison Dimensions

- **Budgeting model:** Actual explicitly teaches envelope budgeting; Budget Board focuses on monthly category budgets; ezBookkeeping presents broader bookkeeping and analysis features without naming one budgeting method.
- **Data ingestion:** Budget Board lists CSV import and provider synchronization. Actual's catalog entry adds QIF, OFX, QFX, and optional bank synchronization. ezBookkeeping lists the broadest set of file formats and custom import mappings, rules, and scripts.
- **Deployment:** All are self-hosting candidates. Budget Board and ezBookkeeping expose Docker-oriented paths; ezBookkeeping also documents database and architecture portability; Actual adds managed hosting and local desktop distribution.
- **Automation and intelligence:** Budget Board names learned transaction categorization and rules. ezBookkeeping lists receipt recognition, AI-generated charts, MCP, and agent tools. Actual's supplied README emphasizes synchronization and budgeting rather than AI features.
- **Scope:** The three repositories are product profiles. The Awesome Selfhosted section is a catalog and should be used for discovery, not as a substitute for checking each project's current documentation, license, deployment model, or maintenance status.

## Catalog Context

The Awesome Selfhosted section shows that “personal finance” is not one product category. Adjacent options cover double-entry accounting (Fava), financial forecasting and rules (Firefly III), shared expenses (IHateMoney), investments (Ghostfolio), bucket budgeting (OpenBudgeteer), and subscription tracking (Wallos). The catalog records licenses and implementation/deployment tags, which are useful first-pass filters but not a complete evaluation.

## Selection Heuristics

Choose Actual when local-first synchronization and envelope budgeting are the primary requirements. Choose Budget Board when a Mint-like dashboard with assets, goals, bank-sync providers, and learned categorization is the closer fit. Choose ezBookkeeping when import-format breadth, lightweight self-hosting, multi-currency support, mobile/PWA access, or AI/MCP integration matters most. Use the broader catalog when the need is accounting, shared expenses, investments, invoices, or subscriptions rather than household budgeting alone.

## See Also

- [Supabase](../backend-infrastructure/supabase.md) - hosted/self-hosted infrastructure context for applications that need PostgreSQL-backed services.
- [Mattermost](../collaboration-platforms/mattermost.md) - another self-hosted application evaluated through deployment and data-control concerns.
