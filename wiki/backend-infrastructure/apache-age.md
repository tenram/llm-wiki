# Apache AGE

> Sources: Apache Software Foundation, Unknown date
> Raw: [Apache AGE README](../../raw/backend-infrastructure/2026-10-23-apache-age.md)

## Overview

Apache AGE is a PostgreSQL extension that adds a graph database model without abandoning PostgreSQL's relational storage and SQL interface. It combines ANSI SQL with openCypher, allowing one database to handle relational and graph data for workloads such as relationship analysis, fraud detection, recommendations, and knowledge management.

## Model And Querying

AGE supports multiple graphs, hierarchical labels, property indexes on vertices and edges, and hybrid SQL/Cypher queries. A typical setup loads the extension, sets `ag_catalog` in the search path, creates a graph, and sends graph operations through the `cypher()` function. Built-in Go, Java, Node.js, and Python drivers support application integration.

The important boundary is transactional behavior. Graph creation, label changes, data loading, and Cypher writes are PostgreSQL writes. Non-autocommit clients must explicitly commit them before other sessions can see the result. The README specifically warns that a nested psycopg transaction block may create only a savepoint when an outer transaction is already open.

## Deployment

AGE can be compiled against PostgreSQL or run from the Apache Docker image. The README states support for PostgreSQL 11 through 18. Apache AGE Viewer adds graph and table visualization. Installation places objects in `ag_catalog`; the source warns that AGE should be installed before granting broad `CREATE` privileges, because another role could pre-create that schema and block extension installation.

## Practical Takeaway

AGE is a useful fit when graph relationships must live beside existing PostgreSQL data and application teams want SQL and Cypher in one system. It differs from a standalone graph database by making PostgreSQL compatibility, transactions, extensions, and operational conventions the primary integration surface.

## See Also

- [Supabase](supabase.md)
- [Codebase Memory and Code Graphs](../agent-memory-systems/codebase-memory-and-code-graphs.md)
- [HybridRAG System](../agent-memory-systems/hybridrag-system.md)
