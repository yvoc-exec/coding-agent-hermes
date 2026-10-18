---
name: coding-cap-secure-coding
description: "Security and Supply Chain Review"
---

# Security and Supply Chain Review

Trace input trust, privilege boundaries, authentication and authorization through actual consumers. Inspect parser/serializer semantics, path normalization, SQL/query construction, XSS/CSRF/SSRF as applicable, secrets logging, dependency source integrity, and generated/executed code. Do not collect sensitive data or disclose private source unnecessarily. Preserve deny-by-default behavior and test negative permission cases. Distinguish theoretical exploit conditions from confirmed impact in a safe local test. Never silently relax policy or disable security tests to get code working.

Read the owning Domain or Methodology when the concrete task triggers it. Preserve operator scope and explicit test evidence.
