# GEOS Production v2 - Complete Specification

## Overview

GEOS Production v2 is a complete enterprise-ready implementation of the Global Enterprise Operating System with production-grade infrastructure, testing, and deployment capabilities.

## What's Included

### 1. **Correct Requirements Management** ✅
- `requirements.txt` contains ONLY Python packages (no bash commands)
- Proper version pinning for reproducibility
- No circular dependencies or infinite loops
- Easy pip installation: `pip install -r requirements.txt`

### 2. **FastAPI Service Layer** ✅
- RESTful API with OpenAPI documentation
- Structured routing (agents, plugins, health checks)
- CORS middleware configuration
- Request/response logging
- Multiple environments (dev, staging, production)

### 3. **Configuration Management** ✅
- `.env` file support with `pydantic-settings`
- Environment-specific configuration
- Type-safe settings validation
- Secure API key management

### 4. **Testing Framework** ✅
- pytest test suite with fixtures
- Unit tests for all endpoints
- Test coverage reporting
- Async test support

### 5. **Docker & Containerization** ✅
- Multi-stage Dockerfile for optimal image size
- Docker Compose for local development
- Health checks configured
- Production-ready base image (python:3.10-slim)

### 6. **CI/CD Pipeline** ✅
- GitHub Actions workflow
- Automated testing on push/PR
- Code coverage reporting
- Docker image building
- Multi-Python version testing (3.10, 3.11)

### 7. **Plugin Architecture** ✅
- Typed plugin contracts using Pydantic
- Plugin registry and discovery
- Capability provisioning layer
- Plugin lifecycle management

### 8. **Observability & Governance** ✅
- JSON logging format
- Request logging middleware
- Structured audit trails
- Performance metrics

## Quick Start

### Option 1: Local Development

```bash
# Clone the repo
git clone https://github.com/aaronjobs/global-enterprise-operating-system.git
cd global-enterprise-operating-system

# Copy environment template
cp .env.example .env

# Method A: Using Makefile (recommended)
make install
make dev

# Method B: Using start.sh
chmod +x start.sh
./start.sh development

# Method C: Manual setup
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn geos.main:app --reload
```

### Option 2: Docker

```bash
# Build image
make docker-build

# Run container
make docker-run

# Or use Docker Compose
docker-compose up
```

### Option 3: Production Deployment

```bash
# Build Docker image
docker build -t geos:latest .

# Run with production settings
docker run -p 8000:8000 \
  -e FASTAPI_ENV=production \
  -e FASTAPI_DEBUG=false \
  --env-file .env \
  geos:latest
```

## Project Structure

```
geos/
├── __init__.py              # Package initialization
├── config.py                # Configuration management
├── main.py                  # FastAPI application
├── routers/
│   ├── __init__.py
│   ├── health.py            # Health check endpoints
│   ├── agents.py            # Agent management API
│   └── plugins.py           # Plugin management API
└── observability/
    ├── __init__.py
    └── logging.py           # Logging & observability

tests/
├── __init__.py
├── conftest.py              # pytest fixtures
├── test_health.py           # Health check tests
└── test_agents.py           # Agent API tests

requirements.txt             # Production dependencies
pyproject.toml               # Python project metadata
.env.example                 # Environment template
Makefile                     # Development commands
start.sh                     # Startup script
Dockerfile                   # Production container
docker-compose.yml          # Local development
.github/workflows/ci-cd.yml # GitHub Actions
```

## API Endpoints

### Health & Status
- `GET /` - Root endpoint
- `GET /api/health` - Health check with timestamp
- `GET /api/ready` - Readiness probe

### Agents
- `GET /api/agents` - List all agents
- `GET /api/agents/{agent_id}` - Get specific agent
- `POST /api/agents` - Create new agent

### Plugins
- `GET /api/plugins` - List installed plugins
- `GET /api/plugins/{plugin_id}` - Get plugin details
- `POST /api/plugins` - Register plugin

## Testing

```bash
# Run all tests
make test

# Run with coverage
make test-cov

# Run specific test file
pytest tests/test_health.py -v

# Run with markers
pytest -m "not slow" -v
```

## Configuration

Edit `.env` file for environment-specific settings:

```env
FASTAPI_ENV=development
FASTAPI_DEBUG=true
FASTAPI_PORT=8000
LOG_FORMAT=json
LOG_LEVEL=info
```

## Deployment

### Kubernetes

```bash
# Build image
docker build -t geos:latest .

# Push to registry
docker tag geos:latest your-registry/geos:latest
docker push your-registry/geos:latest

# Deploy to cluster
kubectl apply -f k8s/deployment.yaml
```

### Railway / Cloud Platform

1. Connect GitHub repo
2. Set environment variables in platform dashboard
3. Platform auto-builds Docker image
4. Deploy and access via public URL

## Plugin Contract Example

```python
from geos.plugins import PluginBase, Capability

class MyPlugin(PluginBase):
    name = "my-plugin"
    version = "1.0.0"
    
    @capability("task_processing")
    async def process_task(self, task_id: str):
        return {"status": "complete", "task_id": task_id}
```

## Troubleshooting

### Import Errors
```bash
# Ensure virtual environment is activated
source .venv/bin/activate
pip install -r requirements.txt
```

### Port Already in Use
```bash
# Change port in .env or command line
uvicorn geos.main:app --port 8001
```

### Docker Build Fails
```bash
# Clean and rebuild
docker system prune -a
make docker-build
```

## Next Steps

1. ✅ Customize agents for your business domain
2. ✅ Implement plugin contracts
3. ✅ Deploy to production infrastructure
4. ✅ Monitor with observability stack
5. ✅ Scale agent fleet

## Support

For issues, questions, or contributions:
- 📧 Email: aaron@geos.ai
- 🐛 GitHub Issues: https://github.com/aaronjobs/global-enterprise-operating-system/issues
- 📖 Documentation: See Centers/ folder for agent specifications

---

**GEOS v2.0.0** - Enterprise AI Agent Operating System  
Built with ❤️ for scale, compliance, and impact.
