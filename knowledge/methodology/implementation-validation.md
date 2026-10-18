# Implementation and Validation

Describe precise before/after behavior and invariants; identify authorized path owners, dependent interfaces, serialization/migration compatibility, failure recovery, concurrent callers and test points. Make the smallest coherent edit, preserving pre-existing work. Avoid silencing type errors, muting assertions or deleting tests to manufacture success. Add tests for ordinary and exceptional cases and verify the test was exercised, not skipped.

Validate progressively: focused regression, unit suite, static/type checks, integration (only when safe), build and relevant end-to-end. Capture command and exit status. Review `git diff --check`, `git status --short`, diff scope and potential secret exposure. Check platform/runtime versions when they materially affect behavior. Report if a command ran but its assertions were insufficient, and if tests were not run.

## File-scoped engineering plan and discrepancy handling

For material multi-file changes, derive a compact implementation contract from the observed repository: intended before/after behavior, file and symbol owners, affected callers/interfaces, persistence and version boundaries, exceptional/control flows, focused tests, and reversible change scope. Use explicit *expected outputs* for decisive validation commands. Do not write a speculative long plan for a trivial safe edit; do not assume a code-generating subagent must implement the plan.

After each meaningful edit or validation, compare expected and observed outcomes. If an observation contradicts the plan, distinguish a **code defect** from a **bad plan assumption**. Reconcile the smallest justified change to the plan, record the discrepancy in Workspace if it affects continuity, and re-run the affected proofs. This ledger is a concise observation, not an extra workflow database or a requirement to commit per step. See `knowledge/rules/evidence-and-quality.md` for the completion proof contract.
