"""Health Check Tests"""

import pytest
from fastapi.testclient import TestClient
from geos.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_root_endpoint(client):
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "GEOS"
    assert "version" in data


def test_health_check(client):
    """Test health check endpoint"""
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data


def test_readiness_check(client):
    """Test readiness check endpoint"""
    response = client.get("/api/ready")
    assert response.status_code == 200
    data = response.json()
    assert data["ready"] is True
