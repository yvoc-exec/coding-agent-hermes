# Root-Cause Tracing: From Symptom to First Invalid Boundary

**Use when:** the reported failure is downstream of the actual defect, or data crosses a process, service, queue, file, persistence, identity or timing boundary.

1. **Anchor:** identify the first observable failure, with exact file/symbol, input/actor, expected result, actual result and command or log location. A stack trace points to the *detection site*, not necessarily the *origin*.
2. **Step upstream:** find the immediately preceding producer/caller. Check the actual argument, type, serialization, normalization and lifecycle at that boundary. Do not assume a same-named function or string match is on the active path.
3. **Mark transitions:** for each observed hop, record the input, transformation, output, owner/process, and evidence (source/test/log). Distinguish what was observed from what is only inferred.
4. **Find divergence:** identify the earliest hop where observed data, authorization, event order or persisted state violates the intended contract. Compare one working variant (or known-good baseline) with the failing variant to isolate the responsible difference.
5. **Discriminate:** choose one bounded experiment that would falsify the leading explanation without editing unrelated paths. Consider stale worker identity, configuration precedence, retry duplication, missing commit, mock-only path, and wrong environment as alternatives.
6. **Repair at owner:** apply the narrowest change at the owning boundary. Preserve safe downstream validation; don't delete a guard simply because it exposes the defect.
7. **Proof:** retain a regression that reaches the affected consumer, checks a meaningful output or side effect, and fails before / passes after where feasible. Re-check negative paths and all affected interfaces.

**Failure examples:** an invalid API response caused by a database serializer is not fixed by swallowing client errors; a worker using a different identity is not fixed by changing frontend permissions; a test that fails at import time does not validate business logic. If source access or reproduction is missing, record the first *unverified* hop and state the strongest supported hypothesis, not a fabricated root cause.
