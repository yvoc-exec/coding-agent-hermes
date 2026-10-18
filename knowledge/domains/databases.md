# Databases, Schemas and Persistence

Trace reads, writes, transactions, migrations, constraints, isolation, indexes, connection lifecycle and retry semantics. Treat schema change as a compatibility contract across old/new app versions and stored records. Prefer additive reversible migrations with explicit data safety strategy; do not run against production without approval. Validate migration ordering, rollback assumptions, seed data, uniqueness and concurrent access. A successful schema CLI exit is not proof that historic data survived.
