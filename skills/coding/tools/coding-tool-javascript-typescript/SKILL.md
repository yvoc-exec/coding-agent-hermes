---
name: coding-tool-javascript-typescript
description: "JavaScript TypeScript Tooling"
---

# JavaScript TypeScript Tooling

Read `package.json` scripts and existing lockfile before running npm/pnpm/yarn/bun commands. Use installed dependencies and the project's package manager; do not auto-install or mutate lockfiles merely to test. Check tsconfig/module mode, runtime Node target, async promise rejection, bundler/SSR boundaries and generated outputs. Execute targeted test, `tsc`/typecheck and build scripts only after understanding script effects; do not assume `npm test` is safe or complete. Preserve public types and module resolution semantics.
