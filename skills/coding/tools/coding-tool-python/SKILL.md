---
name: coding-tool-python
description: "Python Toolchain and Tests"
---

# Python Toolchain and Tests

Inspect `pyproject.toml`, lockfiles, Python version and package layout before commands. Prefer existing venv/environment and `python -m` invocation. Run focused `python -m unittest` or the repository's actual pytest command, type/lint/build checks only if available. Ensure imports, async/task cleanup, typing, packaging and OS path behavior are compatible with declared supported versions. Do not silently create a global venv or pip-install dependencies without approval. Distinguish import/setup failures from failing tests.
