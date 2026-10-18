---
name: coding-agent
description: "Autonomous coding task startup, project memory, and optional native delegation"
---

# NOVA CODE Native Hermes Operations

This companion applies at a new coding task, resume, handoff or delegation. Permanent policy lives **only** in `~/.hermes/profiles/coding-agent/SOUL.md`; do not rewrite it during a project task.

## Start or resume

1. Determine the **operator-selected project root** from the session working directory or explicit task; do not treat this distribution repository as the default target.
2. Inspect current local Git branch/status and targeted source files without changing Git. Read `<project>/.coding-agent/WORKSPACE.md` if it exists; reconcile with current source and operator intent.
3. Actually read `~/.hermes/profiles/coding-agent/knowledge/methodology/operating-loop.md`. On new Workspace or resume read `knowledge/rules/workspace.md`; before mutation/material test read `knowledge/rules/execution.md`.
4. Trigger only relevant Domain, Capability, Tool, and specialized Methodology sources. Known absolute roots: `~/.hermes/profiles/coding-agent/knowledge/` and `~/.hermes/profiles/coding-agent/skills/coding/`. Do not flood context with the whole tree.
5. Work autonomously and directly by default. Optional delegation never substitutes for your own review and integration.

## Self-contained `delegate_task` brief

For every child provide a complete task description in this exact field layout, filling the content from verified current state:

```
NOVA CODE BOUNDED SUBAGENT
Parent: main autonomous coding agent; no nested delegation; main agent owns final integration.
Project root: <actual absolute project root>
Operator goal: <exact relevant user request>
Subtask: <one independent question or scoped implementation>
Known evidence: <observations, relevant symbols/files, failing tests, without secrets>
Allowed paths: <exact list of file paths or subtree>
Write authority: <read-only OR explicit exclusive paths>; all other paths read-only.
Required reads: <exact applicable knowledge/rules and native SKILL.md paths>; open actual files.
Execution constraints: non-destructive local tests only; no remote publication, deploy, secrets, package installation, production access or system changes.
Workspace ownership: do not edit .coding-agent/WORKSPACE.md or derived-skills/; do not mutate installed Hermes profile or this distribution.
Git: no commit/push/merge/rebase/reset/tag/branch actions; preserve existing user changes.
Artifacts: <unique project-local .coding-agent/artifacts/child-N/ path>; don't touch another child's artifacts.
Return: inspected files and symbols; tested hypothesis; exact changes if any; commands and observed outcomes; risks/unknowns; evidence paths.
```

Default children to read-only investigation, independent review and focused testing. Allow disjoint writes only with explicit non-overlapping file scopes. Main agent personally verifies child files and reruns impacted checks. Native `delegation.max_concurrent_children=4`, `max_spawn_depth=1`. Do not create a custom orchestrator, specialized Brain/Hands split, Advisor, or Kanban bridge. A child inference failure never prevents the main agent from directly coding within the operator's permissions.
