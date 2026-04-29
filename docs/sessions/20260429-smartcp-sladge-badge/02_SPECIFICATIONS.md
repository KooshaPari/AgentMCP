# Specifications

## Scope

- Add the sladge badge to `README.md`.
- Do not change code, dependencies, workflows, runtime configuration, or remote
  settings.
- Do not push or otherwise treat this local SmartCP checkout as the canonical
  AgentMCP remote.

## Acceptance Criteria

- README includes `[![AI Slop Inside](https://sladge.net/badge.svg)](https://sladge.net)`.
- Badge appears directly under the top-level heading.
- Session docs note the detached checkout and remote caution.

## Assumptions, Risks, Uncertainties

- Assumption: SmartCP is in scope because it is an MCP/AI tool orchestration
  surface.
- Risk: The repo name can be confused with the AgentMCP remote.
- Mitigation: Record the prepared worktree state and do not push.
