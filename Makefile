.PHONY: help install dev test lint format clean docker-build docker-run

help:
	@echo "GEOS Production v2 - Available Commands"
	@echo "======================================="
	@echo "make install      - Install dependencies"
	@echo "make dev          - Run development server"
	@echo "make test         - Run test suite"
	@echo "make test-cov     - Run tests with coverage"
	@echo "make lint         - Lint code"
	@echo "make format       - Format code"
	@echo "make clean        - Clean build artifacts"
	@echo "make docker-build - Build Docker image"
	@echo "make docker-run   - Run Docker container"

.venv:
	python3 -m venv .venv

install: .venv
	. .venv/bin/activate && pip install -r requirements.txt

dev: .venv
	. .venv/bin/activate && uvicorn geos.main:app --reload --host 0.0.0.0 --port 8000

test: .venv
	. .venv/bin/activate && pytest

test-cov: .venv
	. .venv/bin/activate && pytest --cov=geos --cov-report=html

lint: .venv
	. .venv/bin/activate && python -m py_compile geos/**/*.py

format: .venv
	. .venv/bin/activate && isort geos/ tests/ || true && black geos/ tests/ || true

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + || true
	find . -type f -name *.pyc -delete
	rm -rf .pytest_cache .coverage htmlcov dist build *.egg-info

docker-build:
	docker build -t geos:latest .

docker-run:
	docker run -p 8000:8000 --env-file .env geos:latest
