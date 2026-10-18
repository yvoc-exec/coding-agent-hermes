# Engineering Evidence and Quality

Make claims traceable to actual source, test output or observed behavior. Distinguish a proposed fix from a written fix, a successful tool exit from adequate assertion coverage, a unit test pass from an integrated pass, and passing static checks from operational correctness. Track before/after reproduction conditions and the actual command/exit status. Preserve failure logs only where useful, sanitized of secrets.

Compatibility includes versioned protocols, APIs, database schemas, configurations, files and default behavior. Check negative cases, error handling, retry/idempotency, concurrency, resource closure, test determinism and security boundaries proportionate to the change. Never invent test runs, benchmarks, environment state, issue closure or deployment results.
