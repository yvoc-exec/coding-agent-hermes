# Repository Mapping and System Tracing

Start from entry points, package/build manifests and authoritative tests; map callers/callees, interface types, transport, configurations, storage, workers, queues, security identities and expected lifecycle. Establish whether generated code is derived, tracked or authoritative. Resolve imports and dynamic dispatch using actual definitions, not matching names alone. For bugs, follow the concrete input/identity/state through each transformation to the failing consumer. Mark unobserved branches as hypotheses; never infer all paths from one happy-path trace.

Record affected files, critical symbols, relevant tests, external integration boundaries and state writes in Workspace when they materially affect follow-up. File discovery is proportional to the question, not a forced exhaustive tree listing.
