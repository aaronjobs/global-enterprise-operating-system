"""Agents API Tests"""

import pytest
from fastapi.testclient import TestClient
from geos.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_list_agents(client):
    """Test listing agents"""
    response = client.get("/api/agents")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


def test_get_agent(client):
    """Test getting specific agent"""
    response = client.get("/api/agents/finserv-marketing")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == "finserv-marketing"


def test_get_nonexistent_agent(client):
    """Test getting nonexistent agent"""
    response = client.get("/api/agents/nonexistent")
    assert response.status_code == 404


def test_create_agent(client):
    """Test creating agent"""
    response = client.post("/api/agents", json={
        "name": "Test Agent",
        "center": "test",
        "role": "Testing"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Agent"
