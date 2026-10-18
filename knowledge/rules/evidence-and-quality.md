# Engineering Evidence and Quality

Make claims traceable to actual source, test output or observed behavior. Distinguish a proposed fix from a written fix, a successful tool exit from adequate assertion coverage, a unit test pass from an integrated pass, and passing static checks from operational correctness. Track before/after reproduction conditions and the actual command/exit status. Preserve failure logs only where useful, sanitized of secrets.

Compatibility includes versioned protocols, APIs, database schemas, configurations, files and default behavior. Check negative cases, error handling, retry/idempotency, concurrency, resource closure, test determinism and security boundaries proportionate to the change. Never invent test runs, benchmarks, environment state, issue closure or deployment results.

## Claims must have matching, fresh proof

Before declaring **PASS**, **fixed**, **E2E verified**, **secure**, or **compatible**, map each material acceptance criterion to the actual observation that supports it. Record a compact evidence row: `criterion | command/observation | environment and baseline | exit/assertion | observed result | verified / partial / blocked / not run`. Freshly inspect the final state after the last relevant edit. A previously passing run does not validate a subsequent change; an exit code of zero proves execution succeeded only to the extent of its assertions.

Use **PASS WITH RISKS** when implemented behavior is checked but meaningful integration/platform coverage remains missing; **NEEDS FIXES** when a required test fails or a defect persists; **BLOCKED** when prerequisites prevent meaningful evaluation. No 'E2E' claim from unit-only/static tests, no security guarantee from grep, no Windows/Linux equivalence from a single OS, and no assertion that a child was executed because a brief was authored. Preserve contradictory or partial evidence rather than rounding it up to success.
