---
name: coding-tool-containers-ci
description: "Containers and CI Commands"
---

# Containers and CI Commands

Inspect Dockerfiles, compose configuration, volumes, entrypoints, network and runtime UID/GID before execution. Avoid host-mounted secrets, privileged containers, broad bind mounts, image publication and cloud deployments unless authorized. Validate with read-only syntax checks and isolated local builds where safe; distinguish a container build from successful runtime connectivity. Never use default `docker compose up` blindly against live external dependencies. CI run status may require external credentials and cannot be invented.
