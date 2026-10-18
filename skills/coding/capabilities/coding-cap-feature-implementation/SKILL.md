---
name: coding-cap-feature-implementation
description: "Feature Engineering and API Compatibility"
---

# Feature Engineering and API Compatibility

Translate the operator's task into observable inputs, outputs, failure cases and invariants. Reuse existing patterns, components and approved dependencies. Identify public surface, schemas/types, default values, migrations, callers and versioned interfaces before editing. Favor a coherent minimal implementation with explicit error handling and rollback strategy. Add tests for happy path and at least one consequential edge case; avoid speculative feature expansion. Keep Docs and usage samples aligned with the actual implementation. Never add new dependencies, run installers or change production configuration without the project's authority and explicit safety constraints.

Read the owning Domain or Methodology when the concrete task triggers it. Preserve operator scope and explicit test evidence.

## Implementation brief for material changes

Before a multi-file implementation, capture in the existing Workspace (when useful): exact before/after examples, invariants, affected paths/functions, interface compatibility, write/persistence impact, error behavior, test oracles, and rollback boundary. Then perform small coherent edits, compare observed behavior to expected test output, and reconcile any invalid assumptions instead of layering speculative fixes. For simple scoped tasks, use the compact version mentally; do not block on ceremonies, a separate planner or mandatory subagents. Final handoff names validated outcomes and any proof not obtained. See `knowledge/methodology/implementation-validation.md`.
