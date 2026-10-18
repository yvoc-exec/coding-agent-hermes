# Implementation and Validation

Describe precise before/after behavior and invariants; identify authorized path owners, dependent interfaces, serialization/migration compatibility, failure recovery, concurrent callers and test points. Make the smallest coherent edit, preserving pre-existing work. Avoid silencing type errors, muting assertions or deleting tests to manufacture success. Add tests for ordinary and exceptional cases and verify the test was exercised, not skipped.

Validate progressively: focused regression, unit suite, static/type checks, integration (only when safe), build and relevant end-to-end. Capture command and exit status. Review `git diff --check`, `git status --short`, diff scope and potential secret exposure. Check platform/runtime versions when they materially affect behavior. Report if a command ran but its assertions were insufficient, and if tests were not run.
