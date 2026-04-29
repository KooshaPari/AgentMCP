# Implementation Strategy

## Approach

Keep the update documentation-only:

- Add a single badge line under the README heading.
- Add session docs under `docs/sessions/`.
- Avoid touching source, package, runtime, or remote configuration.

## Git Strategy

Prepare in:

`AgentMCP-wtrees/sladge-badge`

This avoids mutating the detached canonical checkout.
