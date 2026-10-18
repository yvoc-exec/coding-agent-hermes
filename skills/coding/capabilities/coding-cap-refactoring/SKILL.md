---
name: coding-cap-refactoring
description: "Safe Refactor and Technical Debt"
---

# Safe Refactor and Technical Debt

Establish invariant behavior and contract tests before restructuring. Identify call sites, side effects, configuration, serializations, generated boundaries and public interfaces. Change one cohesive concern at a time, keep the diff reviewable, and avoid opportunistic formatting or unrelated architecture swaps. Use tests, static checks and targeted runtime observations to substantiate equivalence. Explicitly record intentional API or migration changes and their compatibility demands. If safe preservation cannot be demonstrated, narrow or postpone the refactor rather than inventing compatibility.

Read the owning Domain or Methodology when the concrete task triggers it. Preserve operator scope and explicit test evidence.
