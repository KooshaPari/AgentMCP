# AgentMCP / SmartCP

**SmartCP MCP Server** — A production-grade Model Context Protocol server with resource access enforcement, intelligent routing, and multi-backend integration. Delegating to a Bifrost backend via GraphQL.

## Stack
| Layer | Technology |
|-------|------------|
| Backend | Python (FastAPI, Pydantic, SQLAlchemy) + Go |
| MCP Protocol | MCP 2.13+ implementation |
| Databases | PostgreSQL (asyncpg), Neo4j, Redis, Qdrant, Supabase |
| Auth | JWT-based authentication middleware |
| Config | YAML + environment variables |
| Testing | pytest (unit + e2e) |

## Key Commands
```bash
# Install dependencies
pip install -e .  # or: pip install smartcp

# Run the MCP server
python -m smartcp
python server.py

# Run tests
pytest
pytest tests/

# Lint
ruff check .
ruff format .

# Type check
ty check src/

# Docker
docker compose up
docker compose -f docker-compose.local.example.yml up
```

## Key Files
- `smartcp/` — Main package source
- `server.py` / `main.py` — Entry points
- `auth/` — Authentication middleware
- `middleware/` — Request/response middleware
- `models/` — Data models
- `runtime/` — Runtime services
- `tools/` — MCP tool definitions
- `migrations/` — Database migrations
- `tests/` — Test suite (47 subdirs)
- `docs/` — Documentation
- `pyproject.toml` — Package config (name: smartcp)

## Reference
Global Phenotype rules: see `~/.claude/CLAUDE.md` or `/Users/kooshapari/CodeProjects/Phenotype/repos/CLAUDE.md`
