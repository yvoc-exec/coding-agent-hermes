---
name: coding-cap-architecture-tracing
description: "Repository Architecture and Impact Tracing"
---

# Repository Architecture and Impact Tracing

Resolve the true project root, entry points, top-level build/runtime manifests, selected target symbols, dependency injection, callers, state owners, and real side-effect consumers. Follow concrete runtime calls instead of guessing from file names. Map queue/background workers, client/server boundaries, database writes and configuration overlays when applicable. Record the shortest relevant path and independent test entry points. Differentiate existing behavior from desired behavior and any assumptions. Stop exploring broad unrelated folders when the causal path is adequately proven. Deliver affected-file map, critical interfaces, compatibility risks and evidence anchors.

Read the owning Domain or Methodology when the concrete task triggers it. Preserve operator scope and explicit test evidence.
