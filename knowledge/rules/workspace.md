# Project Workspace Contract

Use `<project-root>/.coding-agent/WORKSPACE.md` as concise project-local engineering memory, never as a replacement for source inspection or current operator authorization. Create it only for actual coding work when durable state is useful. Include project root and goal; baseline Git/dirty state and protected pre-existing work; concise architecture and control/data-flow anchors; proven observations vs hypotheses; changes and verified effects; commands/test outcomes; blockers/risks; exact next step and source/evidence pointers.

Update only at material transitions, before a consequential context handoff, and upon completion. Keep logs under `.coding-agent/artifacts/` when necessary; never dump massive transcripts or secrets into Workspace. The main agent is the only Workspace writer. On resume re-check current source/Git and reconcile newer outputs against the checkpoint. Neither stale Workspace nor child claims override actual code.
