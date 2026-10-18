---
name: coding-tool-databases
description: "Database, ORM and Migration Tool Safety"
---

# Database, ORM and Migration Tool Safety

Inspect DSN/environment and migration scripts before invocation. Never execute against an unknown, staging or production database by default. Prefer ephemeral local databases and test fixtures; distinguish migration generation, migration apply and rollback. Verify transactional behavior, locks, data preservation and schema compatibility. Capture exact environment and test scope without copying secrets. If no safe local database exists, use static migration review and report validation pending.
