---
name: coding-cap-bugfix-debugging
description: "Bug Reproduction and Root-Cause Repair"
---

# Bug Reproduction and Root-Cause Repair

Capture the exact failure, versions, env, command and input. Classify tool/environment/test/product. Reproduce safely and, if feasible, write a failing regression test before changing production code. Trace values and event order from entry through failing consumer, including async callbacks, identity, retries and persistence when implicated. Compare at least two causal explanations for significant ambiguity. Repair the actual cause, not only the symptom. Prove before/after with targeted test output, then run affected suite and inspect diff. If reproduction is not possible, state why and demonstrate the strongest available substitute without claiming a reproduced failure.

Read the owning Domain or Methodology when the concrete task triggers it. Preserve operator scope and explicit test evidence.

## Investigation protocol (trigger: unexpected behavior, reproducible defect, failing test, integration mismatch)

1. **Establish the observation.** Capture the failing command/request, relevant version and configuration, actual error and exit status. Classify syntax/import/setup failure separately from product failure; record whether reproduction is deterministic, intermittent or unavailable.
2. **Locate the first incorrect transition.** Start at the failing consumer and trace the *actual* value, actor, timestamp and caller backward until an input, transformation, authorization or persistence boundary first differs from the intended contract. Read [root-cause-tracing](references/root-cause-tracing.md) when the cause is upstream or crosses services/processes.
3. **Distinguish hypotheses.** Contrast a known-good path, prior state or baseline commit against the failure. For meaningful ambiguity, list at least two plausible explanations and choose the cheapest observation that differentiates them. Test one causal claim at a time; if evidence contradicts it, discard it rather than stacking patches.
4. **Test the bug, not the harness.** Where feasible, add a regression that fails against the unmodified production behavior *for the intended reason*. A missing dependency, import error or bad fixture is not a valid RED. If baseline cannot run, record why and retain alternate evidence.
5. **Repair and re-check.** Fix at the first incorrect transition rather than hiding the downstream symptom, then verify the narrow test, relevant consumers and changed error paths. Do not silence a failing assertion or add retries without a causal explanation.

For intermittent work, read [async-reliability](references/async-reliability.md). Do not impose this full protocol on obvious documentation-only changes. After repeated failed fixes without new evidence, stop retrying variants, examine the architectural assumption, and report the blocker before risky redesign.
