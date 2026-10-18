---
name: coding-cap-bugfix-debugging
description: "Bug Reproduction and Root-Cause Repair"
---

# Bug Reproduction and Root-Cause Repair

Capture the exact failure, versions, env, command and input. Classify tool/environment/test/product. Reproduce safely and, if feasible, write a failing regression test before changing production code. Trace values and event order from entry through failing consumer, including async callbacks, identity, retries and persistence when implicated. Compare at least two causal explanations for significant ambiguity. Repair the actual cause, not only the symptom. Prove before/after with targeted test output, then run affected suite and inspect diff. If reproduction is not possible, state why and demonstrate the strongest available substitute without claiming a reproduced failure.

Read the owning Domain or Methodology when the concrete task triggers it. Preserve operator scope and explicit test evidence.
