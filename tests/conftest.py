"""Pytest Configuration & Fixtures"""

import pytest
from fastapi.testclient import TestClient
from geos.main import app


@pytest.fixture
def client():
    """Test client fixture"""
    return TestClient(app)


@pytest.fixture
def mock_agent():
    """Mock agent fixture"""
    return {
        "id": "test-agent",
        "name": "Test Agent",
        "center": "test",
        "role": "Testing"
    }
