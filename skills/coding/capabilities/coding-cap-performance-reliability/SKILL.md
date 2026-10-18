---
name: coding-cap-performance-reliability
description: "Measured Performance and Concurrency"
---

# Measured Performance and Concurrency

Define metric, workload, measurement environment and baseline; identify the actual bottleneck first. Trace locks, pools, backpressure, N+1 queries, allocations, caches, rate-limits, retries, cancellation and shutdown as implicated. Propose the smallest benchmarkable change. Compare results with stable conditions and repeated samples where warranted. Include race/reliability regression cases. Report actual numbers and their measurement limits. Never claim a speedup from intuition or change consistency semantics for a synthetic benchmark.

Read the owning Domain or Methodology when the concrete task triggers it. Preserve operator scope and explicit test evidence.
