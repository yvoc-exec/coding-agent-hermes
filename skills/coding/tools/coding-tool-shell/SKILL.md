---
name: coding-tool-shell
description: "Shell and Local Process Safety"
---

# Shell and Local Process Safety

Use the selected repository root as working directory. Quote paths; check executable/script entry points for external side effects before execution. Prefer read-only exploration (`rg`, `find`, `sed`, `cat`) and safe local test commands. Be explicit about environment variables and stdout/stderr/exit status. Avoid `sudo`, pipe-to-shell installers, arbitrary remote scripts, system services, destructive shell globbing, and network/production modifications absent explicit authorization. Mask tokens in recorded commands/results. A successful shell exit alone is not application proof.

On native Windows, Hermes may execute terminal commands through Git Bash even when launched from PowerShell. Distinguish the shell used by the active terminal tool before choosing command syntax. Preserve Windows drive paths and paths containing spaces through appropriate quoting or verified path conversion. Do not assume PowerShell expressions are valid Bash commands or that POSIX home-directory expansion identifies HERMES_HOME. Use the active repository root and resolved Hermes profile paths rather than guessed locations.
