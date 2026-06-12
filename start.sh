#!/bin/bash

# GEOS Production v2 - Startup Script
# Usage: ./start.sh [environment]
#   environment: development, staging, production (default: development)

set -e

ENV=${1:-development}

echo "[GEOS] Starting GEOS v2 in $ENV environment..."

# Load environment variables
if [ -f .env ]; then
    export $(cat .env | grep -v '#' | xargs)
else
    echo "[GEOS] WARNING: .env file not found. Using defaults."
fi

# Create virtual environment if it doesn't exist
if [ ! -d .venv ]; then
    echo "[GEOS] Creating Python virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
echo "[GEOS] Installing dependencies..."
pip install -q -r requirements.txt

# Run migrations (if applicable)
echo "[GEOS] Running pre-flight checks..."
python -m geos.cli verify --environment=$ENV

# Start the FastAPI server
echo "[GEOS] Starting FastAPI server..."
uvicorn geos.main:app \
    --host ${FASTAPI_HOST:-0.0.0.0} \
    --port ${FASTAPI_PORT:-8000} \
    --reload
