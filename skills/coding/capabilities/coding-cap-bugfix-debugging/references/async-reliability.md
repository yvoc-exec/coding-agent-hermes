# Asynchronous Reliability: Event/State Readiness

**Use when:** flaky tests, workers, UI transitions or shutdown logic rely on fixed sleeps, races, stale polls, retries or eventual consistency.

- Define the *observable ready state* (committed row, emitted event, process healthy, request completed), not an arbitrary delay. Establish who publishes that state and how consumers observe a fresh value.
- Prefer event subscriptions or framework-native waits. Otherwise poll a fresh state with a monotonic deadline, bounded interval and explicit timeout error. Never reuse a cached object inside a polling loop.
- On timeout include last observed state, elapsed time and the awaiting operation; stop waiting. On cancellation propagate/clean up resources and unsubscribe listeners.
- Use fake clocks only when they control the actual production timing source. Do not replace a real queue/network boundary with mocked readiness and call it end-to-end.
- Avoid fixed sleeps as a correctness condition. A small backoff may reduce load between *state checks*, but the observed predicate determines completion. Test both success and timeout/cancellation paths.
- Watch for duplicate delivery, out-of-order updates, resettable state, handler registration after the event, shared test isolation, leaked tasks and shutdown races.

**Evidence:** record the predicate, source, deadline, observed transitions and real assertions. If the environment has no reliable readiness signal, explain that gap and use a bounded diagnostic approach instead of claiming a flake is solved by increasing a timeout.
