---
name: coding-cap-code-review
description: "Independent Differential Review"
---

# Independent Differential Review

Review selected changed lines against original baseline and all affected consumers. Check correctness, backward compatibility, input validation, authorization, resource lifecycle, failure paths, concurrency and missing tests. For each material issue cite file, location, actor/input, proof or reproduction, and narrowly proposed fix. Differentiate confirmed defect from plausible risk and style preference. Track what files and tests were actually inspected. Never infer clean security or full compatibility from an uneventful lint/build. A review subagent is read-only unless its assigned brief expressly names exclusive writable paths.

Read the owning Domain or Methodology when the concrete task triggers it. Preserve operator scope and explicit test evidence.

## Two-pass differential review

**Pass A, specification:** Compare the actual diff with the operator's requested observable behavior, tests and explicit exclusions. Identify missing acceptance criteria and changes outside scope. **Pass B, engineering:** trace every modified public contract to callers, stored data, consumers, permissions, error paths, build/runtime targets and tests. Review the negative/denial path as carefully as the happy path.

For each finding distinguish **confirmed** (reproduced or backed by an exact code path), **plausible** (missing proof), and **suggestion** (non-blocking design/style). Record priority, path+symbol, triggering input/state, consequence, evidence and minimal correction. Do not inflate severity from an unverified scanner hit or claim a comprehensive review from a narrow diff skim.

Reviewer feedback is a *hypothesis*, not an instruction hierarchy. Reopen source and tests before adopting a suggested fix, especially if it deletes compatibility branches, relaxes authorization, alters data shapes or overrides the operator's constraints. If review advice is wrong, explain the conflict and preserve the existing guarantee. Independent review via a child is optional and read-only by default; the main agent verifies every finding and final patch itself.
