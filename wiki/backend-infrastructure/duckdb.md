# DuckDB

> Sources: DuckDB contributors, Unknown date
> Raw: [DuckDB README](../../raw/backend-infrastructure/2026-10-23-duckdb.md)

## Overview

DuckDB is an embedded analytical database. It runs in-process without a separate server, exposes a full SQL dialect, and is designed to query local or remote data directly from applications, scripts, and a standalone CLI.

## Data And Integrations

DuckDB can read and write CSV, Parquet, JSON, and Excel files from local storage or S3, HTTP(S), Azure, and Google Cloud Storage. Direct file queries make it useful for analytical work without a separate ingestion step. It also supports DuckLake, Apache Iceberg, and Delta Lake, including catalog, transaction, snapshot, and time-travel patterns described by the source.

DuckDB can attach to PostgreSQL, MySQL, and SQLite and query or move data across those systems without a separate ETL process. The quack protocol connects DuckDB instances over HTTP. A modular extension system adds connectors, file formats, functions, and types at runtime.

## Clients And Development

The project provides a standalone CLI and clients for Python, R, Java, Rust, Go, Wasm, and other environments, with integrations such as pandas. Building from source requires CMake, Python 3, and a C++17 compiler. The repository documents release, debug, unit-test, and benchmark make targets.

## Practical Takeaway

DuckDB is the opposite of a traditional always-on analytical service: the database travels with the application and reaches into files and other databases when needed. That makes it a strong local analytics and data-preparation component, while larger shared deployments require deliberate choices about remote access, extensions, and data ownership.

## See Also

- [Supabase](supabase.md)
- [Apache AGE](apache-age.md)
