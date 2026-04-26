# AgentMCP / SmartCP

> **Note:** This local checkout is a SmartCP app, not the AgentMCP repo at github.com/KooshaPari/AgentMCP. Do not push from this directory. See ../docs/security/AGENTMCP_REMOTE_REVERT_RUNBOOK.md.

**SmartCP MCP Server** - A production-grade Model Context Protocol (MCP) server with resource access enforcement, intelligent routing, and multi-backend integration.

## Overview

AgentMCP (also known as SmartCP) is a hybrid Python/Go application that serves as an MCP protocol frontend, delegating business logic to a Bifrost backend via GraphQL. It provides a secure, scalable interface for AI tool orchestration with built-in authentication, semantic search, and intelligent request routing.

## Key Features

### MCP Protocol Support
- Full Model Context Protocol 2.13+ implementation
- Tool registration, discovery, and execution
- Resource access enforcement with scoped permissions
- Semantic search capabilities via vector database

### Authentication & Security
- JWT-based authentication middleware
- OAuth 2.0 with Device Code Request (DCR) for CLI/servers
- PKCE (Proof Key for Code Exchange) for secure tokens
- Token caching with TTL and encryption

### Intelligent Routing
- Bifrost backend integration via GraphQL
- Smart request routing with confidence scoring
- Cost, performance, speed, and balanced routing strategies
- Pareto-optimized model selection

### Data Layer
- Multi-database support: PostgreSQL, Neo4j, Redis, Qdrant
- Supabase integration for real-time data
- Vector search for semantic queries
- Migration management with asyncpg

### ML & AI Integration
- MLX framework support for Apple Silicon
- OpenAI API integration
- Transformers library for model inference
- Custom classification and routing models

### Development & Operations
- FastAPI for high-performance async APIs
- Pydantic v2 for type-safe data models
- Prometheus metrics and structured logging
- Docker Compose for local development
- Comprehensive test suite with pytest

## Quick Start

### Prerequisites
- Python 3.10+
- Go 1.21+ (for CLI components)
- PostgreSQL 14+
- Redis 7+
- Neo4j 5+ (optional)
- Qdrant (optional, for vector search)

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd AgentMCP

# Install Python dependencies (using uv recommended)
uv pip install -e ".[dev]"

# Or with pip
pip install -e ".[dev]"

# Install Go dependencies
cd smartcpcli && go mod download
```

### Configuration

Create a `.env` file:

```env
# Database
DATABASE_URL=postgresql://user:pass@localhost/smartcp
REDIS_URL=redis://localhost:6379
NEO4J_URI=bolt://localhost:7687
QDRANT_URL=http://localhost:6333
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key

# Auth
JWT_SECRET=your-jwt-secret
OAUTH_CLIENT_ID=your-oauth-client-id
OAUTH_CLIENT_SECRET=your-oauth-client-secret

# Bifrost
BIFROST_URL=http://localhost:4000/graphql
BIFROST_API_KEY=your-bifrost-key

# OpenAI (optional)
OPENAI_API_KEY=sk-...

# Voyage AI for embeddings (optional)
VOYAGE_API_KEY=...
```

### Running the Server

```bash
# Start dependencies
docker-compose up -d postgres redis neo4j qdrant

# Run migrations
python -m alembic upgrade head

# Start the FastAPI server
python main.py
# Or
uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# Server will be available at http://localhost:8000
# API docs at http://localhost:8000/docs
```

### Health Check

```bash
curl http://localhost:8000/health
```

### Using the API

```bash
# List available tools
curl http://localhost:8000/tools

# Route a query
curl -X POST http://localhost:8000/route \
  -H "Content-Type: application/json" \
  -d '{
    "action": "analyze",
    "prompt": "Summarize the quarterly report",
    "context": {"user_id": "123"}
  }'

# Semantic search
curl -X POST "http://localhost:8000/search/semantic?query=machine learning&limit=5"
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=.

# Run specific test suites
pytest tests/unit/
pytest tests/integration/
pytest tests/e2e/ -c pytest.e2e.ini
```

## Project Structure

```
AgentMCP/
├── auth/               # Authentication & OAuth
├── bifrost/            # Bifrost plugin POC
├── bifrost_client.py   # Bifrost GraphQL client
├── bifrost_extensions/ # Production SDK (routing, resilience)
├── cmd/                # CLI entry points
├── config/             # Configuration management
├── docs/               # Documentation & archived code
├── internal/           # Go internal packages
├── main.py             # FastAPI application entry point
├── middleware/         # FastAPI middleware
├── migrations/         # Database migrations
├── models/             # Pydantic models
├── research/           # POCs and experimental code
├── runtime/            # Agent runtime & sandbox
├── schema/             # GraphQL schemas
├── scripts/            # Utility scripts
├── server.py           # MCP server implementation
├── services/           # Business logic services
├── smartcpcli/         # Go CLI tool
├── tests/              # Test suites
├── tools/              # MCP tool implementations
└── infrastructure/     # Infrastructure as code
```

## Architecture

SmartCP follows a layered architecture:

1. **API Layer** (FastAPI): RESTful endpoints, request validation
2. **Service Layer**: Business logic, tool orchestration
3. **Client Layer**: Bifrost GraphQL client, external service clients
4. **Data Layer**: Database models, migrations, queries

The Bifrost backend handles complex business logic, while SmartCP focuses on MCP protocol compliance and request routing.

## SDK Generation

SmartCP is designed to support multi-language SDK generation:

- Python SDK (current, built-in)
- TypeScript SDK (planned)
- Go SDK (planned)
- Rust SDK (planned)

See `docs/bifrost-extensions-sdk-generation.md` for the detailed roadmap.

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make changes with tests
4. Run quality checks: `pre-commit run --all-files`
5. Submit a pull request

## License

MIT License - See LICENSE file for details.

## Support

- Issues: GitHub Issues
- Documentation: `/docs` directory
- Architecture: See `CONSOLIDATION_SUMMARY.md`
