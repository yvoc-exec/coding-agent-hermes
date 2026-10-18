---
name: coding-cap-architecture-tracing
description: "Repository Architecture and Impact Tracing"
---

# Repository Architecture and Impact Tracing

Resolve the true project root, entry points, top-level build/runtime manifests, selected target symbols, dependency injection, callers, state owners, and real side-effect consumers. Follow concrete runtime calls instead of guessing from file names. Map queue/background workers, client/server boundaries, database writes and configuration overlays when applicable. Record the shortest relevant path and independent test entry points. Differentiate existing behavior from desired behavior and any assumptions. Stop exploring broad unrelated folders when the causal path is adequately proven. Deliver affected-file map, critical interfaces, compatibility risks and evidence anchors.

Read the owning Domain or Methodology when the concrete task triggers it. Preserve operator scope and explicit test evidence.

## Ranked, bounded context retrieval

Build a compact semantic map ordered by expected relevance: (1) observed entry point or failing test, (2) actual symbol definitions and signatures, (3) callers plus concrete consumers, (4) config/runtime overlays, process or persistence boundary, and (5) owning tests. Read precise ranges around declarations and branches first, then widen only when needed. Prefer filename-only search results before opening a large number of matches; verify dynamic dispatch and generated-code ownership instead of trusting string matches.

A repository map is a navigational index, **not** proof of runtime dispatch. If a symbol index is available, use it within the authorized tools; otherwise rely on existing search/read and local diagnostics. Do not install Tree-sitter, language servers or indexing services just to follow this procedure. Stop once the relevant contract and causal chain are sufficiently evidenced, and record one-line file/symbol links for continuation after compaction.
