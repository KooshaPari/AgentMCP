# AgentMCP

> Agentic Model Context Protocol framework — a Python harness (smartcp) plus
> 391-test compliance suite for building and validating MCP-speaking agents.

AgentMCP is the Phenotype-org reference implementation for **agent-side** MCP
tooling: it pairs a thin runtime harness (`smartcp`) with a comprehensive test
battery so you can stand up a new MCP-aware agent and prove it conforms to the
spec on day one.

> **Status:** scaffolding. The canonical implementation lives in adjacent
> Phenotype repos (see [PhenoMCP](https://github.com/KooshaPari/PhenoMCP) for
> the polyglot protocol core) and is being staged here for public release.

## What's in the box

- **`smartcp/`** — Python harness for hosting MCP servers and clients,
  with structured logging, transport selection (stdio/SSE/WebSocket), and
  automatic capability negotiation.
- **`tests/`** — 391-test compliance suite covering protocol framing,
  capability handshakes, tool invocation, resource subscriptions, and
  cancellation semantics.
- **`examples/`** — minimal end-to-end agents demonstrating common patterns
  (filesystem tools, HTTP fetch, database query).

## Install

```bash
pip install agentmcp        # once published
# or, from source:
git clone https://github.com/KooshaPari/AgentMCP.git
cd AgentMCP && pip install -e .
```

## Quick start

```python
from smartcp import Agent, tool

@tool
def echo(message: str) -> str:
    """Return the input message verbatim."""
    return message

agent = Agent(name="echo-agent", tools=[echo])
agent.run()  # speaks MCP over stdio by default
```

Run the compliance suite against your server:

```bash
pytest tests/                       # full 391-test battery
pytest tests/compliance -k handshake  # focused subset
```

## Related repositories

- **[PhenoMCP](https://github.com/KooshaPari/PhenoMCP)** — polyglot MCP core
  (Rust + bindings for Swift, Kotlin, C#).
- **[TestingKit](https://github.com/KooshaPari/TestingKit)** — shared test
  fixtures and quality tooling used by the compliance suite.

## Contributing

Issues and PRs welcome. Please open an issue describing the change first so we
can align on scope. All contributions must include tests and pass the
compliance suite.

## License

Dual-licensed under either of [Apache License 2.0](LICENSE-APACHE) or
[MIT License](LICENSE-MIT) at your option.
