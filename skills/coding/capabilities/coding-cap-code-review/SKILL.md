---
name: coding-cap-code-review
description: "Independent Differential Review"
---

# Independent Differential Review

Review selected changed lines against original baseline and all affected consumers. Check correctness, backward compatibility, input validation, authorization, resource lifecycle, failure paths, concurrency and missing tests. For each material issue cite file, location, actor/input, proof or reproduction, and narrowly proposed fix. Differentiate confirmed defect from plausible risk and style preference. Track what files and tests were actually inspected. Never infer clean security or full compatibility from an uneventful lint/build. A review subagent is read-only unless its assigned brief expressly names exclusive writable paths.

Read the owning Domain or Methodology when the concrete task triggers it. Preserve operator scope and explicit test evidence.
