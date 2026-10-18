# Software Engineering Framework

Treat requested behavior as a contract across callers, dependencies, persistence, errors, deployment and tests. Preserve the existing architecture unless evidence requires modification. Identify the affected users, entry points, state and invariants; map source through observable side effects. Separate requirements, assumptions, existing guarantees and unknowns. Prefer incremental improvements that can be checked in isolation.

A patch is complete when it addresses the proven cause, does not break supported interfaces or important side effects, includes regression coverage where feasible and has honestly reported validation. Maintainability includes naming, testability, debuggability, ownership, clear failure behavior and small reviewable diffs. Do not chase superficial complexity without a measured reason.
