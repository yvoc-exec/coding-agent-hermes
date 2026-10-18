---
name: coding-cap-secure-coding
description: "Security and Supply Chain Review"
---

# Security and Supply Chain Review

Trace input trust, privilege boundaries, authentication and authorization through actual consumers. Inspect parser/serializer semantics, path normalization, SQL/query construction, XSS/CSRF/SSRF as applicable, secrets logging, dependency source integrity, and generated/executed code. Do not collect sensitive data or disclose private source unnecessarily. Preserve deny-by-default behavior and test negative permission cases. Distinguish theoretical exploit conditions from confirmed impact in a safe local test. Never silently relax policy or disable security tests to get code working.

Read the owning Domain or Methodology when the concrete task triggers it. Preserve operator scope and explicit test evidence.

## Evidence and dependency-delta review

For each apparent security issue, trace attacker-controlled input to the exact sensitive operation and identify required prerequisites, encoding and authorization boundaries. Try to *refute* a suspected finding using the actual guard/consumer before labeling it confirmed; record what is verified versus hypothetical. Test missing/unauthorized identities and malformed inputs where safe.

When package manifests, generated clients, SBOMs or lockfiles change, identify direct **and transitive** version changes, provenance, API/security impact and reproducibility. Prefer already-installed dependency metadata and authoritative advisories. Do not execute dependency installers, generic scanners that run untrusted scripts, or unreviewed upgrade commands without permission. A clean scan cannot establish 'secure', and a scanner finding alone cannot establish exploitability.
