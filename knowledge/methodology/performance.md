# Performance and Reliability Investigation

Define a measurable workload, resource envelope and baseline before optimization. Profile the real bottleneck rather than assuming algorithmic, IO, database or UI causes. Distinguish throughput, latency percentiles, tail behavior, memory, startup and cancellation. Evaluate concurrency races, backpressure, cache invalidation, allocation, N+1 queries, lock contention and retry storms as relevant. Test unchanged baseline vs candidate under comparable conditions; report measurements, tradeoffs and unmeasured risk.

## Comparative measurement protocol

Fix environment, workload and tool versions; record a representative baseline and resource envelope. Use warmup when caching/JIT materially changes results, then several comparable repetitions (not one cherry-picked run). Report median/range or relevant tail percentiles and observed variance; compare an unchanged control if conditions may drift. Profile the suspected hot path before a large optimization, and verify that semantic correctness and memory/resource bounds remain intact. Avoid claiming a speedup smaller than measurement noise. An unrun benchmark is a hypothesis, not a result.
