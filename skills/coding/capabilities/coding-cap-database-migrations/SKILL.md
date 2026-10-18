---
name: coding-cap-database-migrations
description: "Database and Persistent State Changes"
---

# Database and Persistent State Changes

Trace schema and ORM models, live read/write call sites, transaction boundaries and migration framework. Distinguish migration file creation from execution. Inspect constraints, defaults, historic data, unique/index changes, rollback, and compatibility across rolling versions. Avoid destructive or production data operations without explicit operator authorization. Prefer additive migrations and reversible rollouts when possible; handle retries and partial application safely. Validate against disposable/local test database, including old-data fixtures, and report any migration assumptions or unverified rollback.

Read the owning Domain or Methodology when the concrete task triggers it. Preserve operator scope and explicit test evidence.
