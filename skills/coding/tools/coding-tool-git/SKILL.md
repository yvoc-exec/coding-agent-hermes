---
name: coding-tool-git
description: "Git Inspection and Patch Hygiene"
---

# Git Inspection and Patch Hygiene

Use `git status --short --branch`, `git diff --`, `git diff --check`, and read-only `git log`/`show` as needed to establish baseline. Inspect untracked and staged work before editing; do not assume a clean tree or reset someone else's changes. `git diff` omits untracked content. Treat submodules/worktrees/nested repositories and symlinked paths as separate scope boundaries. Do not run `git add`, `commit`, `push`, `pull`, `merge`, `rebase`, `reset`, `checkout`, `switch`, `branch`, `tag` or destructive clean operations unless separately authorized for the exact scope. Never force push.
