# Tests That Prove Behavior, Not Test Plumbing

**Use when:** a new regression test appears green too easily, the defect spans boundaries, mocks dominate, or test discovery is uncertain.

- **Validity:** a failing baseline should report the intended violated assertion. Import/setup errors, unavailable services and incorrectly mocked paths invalidate claims that the business contract was tested.
- **Production reachability:** the tested function/route must be the code that callers actually execute. If a test only validates a stub, adapter, or mock return value, name that narrower scope.
- **Assertion strength:** verify an outcome that would be wrong under the original bug, e.g. response payload, access denial, persisted mutation, event emission and cleanup, not merely `was_called` or `status == 200` when those are insufficient.
- **Counterfactual:** ask whether a known-wrong implementation would still pass. If yes, strengthen the assertion before relying on the result.
- **Isolation:** restore state, close resources, avoid static sleeps and avoid interaction between neighboring tests. Exercise timeouts and cancellation where they define correctness.
- **Change proof:** where safe and relevant, compare pre- and post-change outcomes for the same deterministic test, and preserve both observed outputs. Explicitly distinguish tests *run*, *skipped*, *blocked* and *not run*.

A complete-looking test suite is not a full integration or production guarantee. Prefer a small reliable assertion through the real path over an elaborate test that mocks away the failure.
