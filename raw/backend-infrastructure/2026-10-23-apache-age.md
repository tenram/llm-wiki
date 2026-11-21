# Apache AGE

> Source: https://github.com/apache/age
> Collected: 2026-10-23
> Published: Unknown

Apache AGE (A Graph Extension) is a PostgreSQL extension that adds a graph database model on top of an existing relational database. It is designed to store relational and graph data together and supports standard ANSI SQL alongside openCypher. Because it extends PostgreSQL, it retains PostgreSQL features while adding graph capabilities.

## Overview

Apache AGE is:

- **Powerful**: adds graph database support to PostgreSQL.
- **Flexible**: supports openCypher queries and querying multiple graphs.
- **Intelligent**: supports graph queries used for fraud detection, master data management, recommendations, identity and relationship management, personalization, and knowledge management.

## Features

- Cypher graph queries
- Hybrid SQL and Cypher querying
- Queries across multiple graphs
- Hierarchical graph-label organization
- Property indexes on vertices and edges
- PostgreSQL feature support

## Installation

AGE can be installed from source or run with Docker. Source builds require PostgreSQL and build dependencies such as a C compiler, readline, zlib, flex, and bison. The README says the current release supports PostgreSQL 11 through 18.

For a source installation, run `make install`, optionally passing `PG_CONFIG=/path/to/postgres/bin/pg_config`. The Docker image can be started with:

```bash
docker pull apache/age
docker run --name age -p 5455:5432 \
  -e POSTGRES_USER=postgresUser \
  -e POSTGRES_PASSWORD=postgresPW \
  -e POSTGRES_DB=postgresDB \
  -d apache/age
```

After connecting, load the extension and set the search path:

```sql
CREATE EXTENSION age;
LOAD 'age';
SET search_path = ag_catalog, "$user", public;
```

AGE stores objects in the `ag_catalog` schema. The README warns that AGE must be installed before granting database `CREATE` privileges to other roles, because a pre-created `ag_catalog` owned by another role can prevent extension installation.

## Transaction Behavior

AGE graph and label creation, deletion, data loading, and Cypher writes are transactional PostgreSQL writes. Clients that do not use autocommit must explicitly commit them before other sessions can see the changes. `LOAD` and `SET search_path` are session-local and do not need a commit. The README calls out a psycopg savepoint trap: a transaction block nested inside an already-open transaction creates a savepoint, not a top-level transaction.

## Quick Start

Create a graph with `SELECT create_graph('graph_name')`, then use `cypher()` to create vertices, edges, and queries. AGE provides built-in Go, Java, Node.js, and Python drivers. Apache AGE Viewer provides a UI for graph and table visualization and exploration.

## Source

The repository links to the Apache AGE manual, installation guidance, developer guidelines, and community mailing list. It is licensed under the Apache License.
