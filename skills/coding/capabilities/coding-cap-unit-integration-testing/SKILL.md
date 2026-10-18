---
name: coding-cap-unit-integration-testing
description: "Test Engineering and Verification"
---

# Test Engineering and Verification

Select the smallest test that proves the changed contract, then boundary/integration checks when authorized. Inspect actual test framework/config and isolation boundaries. Build deterministic fixtures, cover error handling, time, concurrency and cleanup where relevant; avoid environment-dependent sleeps and brittle snapshot-only assertions. Confirm tests are discovered and assertions run, not skipped. Separate local client failure, missing service, flaky behavior and product regression. Report exact command, exit code, assertions relevant to the change and unrun suites. Do not quietly delete tests, rewrite expected results to hide defects, or claim E2E without executing a real representative path.

Read the owning Domain or Methodology when the concrete task triggers it. Preserve operator scope and explicit test evidence.

## Evidence-bearing tests (trigger: changed observable behavior or repaired defect)

Use **RED → GREEN → REFACTOR** where a pre-change run is feasible and safe. RED must demonstrate the *specific* missing behavior against the baseline, not a syntax, import, network or fixture failure; record the failing assertion/exit. GREEN must exercise the production route and confirm the failure becomes a pass. REFACTOR retains the same demonstrated contract while simplifying only what was justified. If a baseline run is unavailable, mark RED **not observed** and use the strongest permitted substitute; never invent a prior failure.

Prefer assertions on external results, persisted state, emitted events and denial cases, not only mock calls or snapshot existence. Check one consequential negative/edge path and ensure the test really ran (discovered test count, absence of skip markers, clear assertion). For affected integrations, test schema/serialization compatibility, retry, cleanup and error propagation. Use [test-quality](references/test-quality.md) to review mocking boundaries and misleading passes. For flaky tests or eventual consistency, use the bugfix Skill's [async-reliability](../coding-cap-bugfix-debugging/references/async-reliability.md).

Do not require artificial TDD for documentation-only changes, unsafe migrations, or environments that cannot reproduce baseline; say what was instead verified. Do not modify existing test expectations to conceal an unwanted behavior change.
