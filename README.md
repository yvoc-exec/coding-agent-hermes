# NOVA CODE: Coding Agent for Native Hermes

A portable **autonomous coding agent** built as a Hermes profile distribution. The agent directly reads, edits, debugs, tests, and reviews authorized codebases. It may optionally use **up to four concurrent native leaf subagents** (depth 1) for independent work. No Brain-and-Hands protocol, separate Advisor, custom model router, Kanban, scheduled learning daemon, or proprietary fork of Hermes.

## Runtime and isolation

- Distribution profile: coding-agent. The installed profile lives beneath the effective Hermes profile home. Standard native Windows installations use %LOCALAPPDATA%\hermes\profiles\coding-agent unless HERMES_HOME is customized. Resolve the actual location instead of assuming a POSIX home directory.
- The active operator-selected Hermes model is the main coding agent. The packaged auxiliary delegation default is `ollama-cloud / deepseek-v4.1-flash`, high reasoning; change via Hermes native configuration and your own credentials. A configured model is not proof of working inference.
- Project-specific memory: `<project-root>/.coding-agent/WORKSPACE.md`, artifacts, and validated Derived Skills. Profile `knowledge/` and native `skills/coding/` are permanent read-only references during ordinary coding tasks.
- Launch from the **target source repository's root**. Do not launch from this distribution checkout when intending to edit a different project.
- Git publication, profile updates, production deployments, destructive operations, and changing authentication are never automatic.

## Requirements

Hermes >= 0.21.6, Git, and a configured native Hermes inference provider. Hermes TUI may require Node.js 20+. Python 3.10+ is needed only for the shipped standalone offline structure tests. Never install prerequisites as a side effect of this distribution.

## Clean TUI and dedicated Forge skin

NOVA CODE uses the same low-noise Hermes TUI visibility policy as
the Pentest Agent, but a distinct graphite-and-muted-jade visual theme.

The distribution's `config.yaml` selects `display.skin: forge`.
The theme is defined entirely in `skins/forge.yaml` and does not
change inference, delegation, terminal execution, or tool permissions.

The display defaults hide reasoning and background activity, keep
tools expanded, collapse subagent details, and retain the Unicode
status indicator.

The `forge` filename is retained for compatibility with existing
coding-agent profiles. It is independent from the Pentest Agent's
`nova` skin.

For an already installed profile, normal profile updates may preserve
operator-customized configuration. Avoid `--force-config` unless
intentionally replacing those settings.

Check the effective setting with:

```powershell
hermes -p coding-agent config get display
```

After a distribution refresh, the selected skin should be `forge`.
If the operator has explicitly customized the selected skin, preserve
that preference rather than silently overriding it.

## Native Windows 11 deployment

NOVA CODE's primary deployment target is native Windows 11, independent of WSL2 Kali.

Verify the existing Windows Hermes CLI from PowerShell:

```powershell
Get-Command hermes
hermes --version
python --version
```

Python 3.10+ is needed for the standalone offline tests. Run them from the distribution checkout:

```powershell
Set-Location "E:\My Projects\AI\coding-agent-hermes"
python -m unittest discover -s tests -v
```

After explicit operator approval, install the named profile:

```powershell
hermes profile install .
hermes profile info coding-agent
hermes -p coding-agent config get delegation
```

Determine the standard expected native profile location, accounting for a customized Hermes home:

```powershell
$base = if ($env:HERMES_HOME) {
    $env:HERMES_HOME
} else {
    Join-Path $env:LOCALAPPDATA "hermes"
}

$profilePath = Join-Path $base "profiles\coding-agent"
Write-Output $profilePath
Test-Path (Join-Path $profilePath "SOUL.md")
Test-Path (Join-Path $profilePath "knowledge\methodology\operating-loop.md")
```

Both path checks must be true for this expected layout. If they are false, locate the effective profile through native Hermes profile information before proceeding; do not move, recreate, or overwrite profile files to make a guessed path work.

Launch the agent from the root of the coding project being worked on, not from the distribution repository:

```powershell
hermes -p coding-agent chat
```

The Windows Coding Agent and WSL2 Kali Pentest Agent are independent Hermes environments. No additional gateway, dashboard, or WSL installation is required by this distribution.

## Install from the public repository after operator-controlled publication

```sh
hermes profile install https://github.com/yvoc-exec/coding-agent-hermes.git
hermes profile info coding-agent
```

Use native Hermes model setup/auth before a live session. From an unrelated **actual coding project root**:

```sh
hermes -p coding-agent chat
```

`hermes profile update coding-agent` is explicitly operator-initiated. Avoid `--force-config`, which can overwrite the operator's model settings. Bare `hermes` remains your general agent, and `pentest-agent` remains independent.

## Verify delegated model route and runtime

```sh
hermes -p coding-agent config get delegation
hermes -p coding-agent config get model
```

The second command may show an unset/default model because main-agent selection is controlled by the active Hermes session. Local config inspection cannot prove successful model inference or live delegation; exercise the acceptance scenarios in `tests/ACCEPTANCE.md` with a scratch codebase to prove runtime behavior.

## Permanent source ownership

- `SOUL.md`: one canonical coding contract.
- `skills/coding/coding-agent/SKILL.md`: startup, source-selection, and self-contained child briefs.
- `skills/coding/capabilities/*/SKILL.md`: focused task-specific expertise.
- `skills/coding/tools/*/SKILL.md`: tool reliability and safety semantics.
- `knowledge/frameworks/`, `methodology/`, `domains/`, `rules/`: decision guidance, progressively loaded.
- `skins/forge.yaml`: presentation only; no model or execution authority.
- `tests/`: offline distribution invariants and manual live acceptance scenarios.

Each working project can maintain `.coding-agent/`; add it to that project's `.gitignore` only with operator approval. The root `.gitignore` in this distribution does not modify other projects.

## Scope of v1

Strong general-purpose software engineering: codebase archaeology, control/data-flow tracing, bug reproduction/root-cause work, implementation, API/client compatibility, tests, code review, refactors, databases/migrations, concurrency, security, performance, frontend/backend, containers/CI, and AI-agent boundaries. Knowledge is selected for actual triggers; not all documents are loaded on every task. Final correctness depends on the chosen model, tools, repository context, permissions, and real test evidence, not documentation count.
