# Root-Cause Debugging

Capture exact failure symptoms, command, environment, version, inputs, reproducibility and last known good evidence. Separate stack trace location from causal origin. First classify tooling/environment/configuration/test/product failure. Reproduce with the smallest representative case, instrument narrowly when necessary and compare successful and failing control-flow/state paths. Use hypotheses with distinguishing observations; a patch that merely swallows the error is not root-cause repair.

Cover process boundaries, identity, timing, retries, cache invalidation, database transactions, network failure, cancellation, shutdown and resource cleanup as triggered. Add a regression test that fails before and passes after where feasible; if baseline cannot be reproduced, clearly state the substitute validation and remaining uncertainty.
