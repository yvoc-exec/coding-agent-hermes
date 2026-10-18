---
name: coding-cap-unit-integration-testing
description: "Test Engineering and Verification"
---

# Test Engineering and Verification

Select the smallest test that proves the changed contract, then boundary/integration checks when authorized. Inspect actual test framework/config and isolation boundaries. Build deterministic fixtures, cover error handling, time, concurrency and cleanup where relevant; avoid environment-dependent sleeps and brittle snapshot-only assertions. Confirm tests are discovered and assertions run, not skipped. Separate local client failure, missing service, flaky behavior and product regression. Report exact command, exit code, assertions relevant to the change and unrun suites. Do not quietly delete tests, rewrite expected results to hide defects, or claim E2E without executing a real representative path.

Read the owning Domain or Methodology when the concrete task triggers it. Preserve operator scope and explicit test evidence.
