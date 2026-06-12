"""GEOS Agents API"""

from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()


class Agent(BaseModel):
    """Agent model"""
    id: str
    name: str
    center: str
    role: str
    status: str = "active"
    version: str = "1.0.0"


class AgentConfig(BaseModel):
    """Agent configuration"""
    name: str
    center: str
    role: str
    behaviors: Optional[dict] = None


# Mock data
agents_db = {
    "finserv-marketing": Agent(
        id="finserv-marketing",
        name="FinServ Marketing Agent",
        center="creator_models",
        role="Financial Services Marketing",
        status="active"
    )
}


@router.get("/agents", response_model=List[Agent])
async def list_agents():
    """List all agents"""
    return list(agents_db.values())


@router.get("/agents/{agent_id}", response_model=Agent)
async def get_agent(agent_id: str):
    """Get agent by ID"""
    if agent_id not in agents_db:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agents_db[agent_id]


@router.post("/agents", response_model=Agent, status_code=status.HTTP_201_CREATED)
async def create_agent(config: AgentConfig):
    """Create new agent"""
    agent = Agent(
        id=config.name.lower().replace(" ", "-"),
        name=config.name,
        center=config.center,
        role=config.role,
    )
    agents_db[agent.id] = agent
    return agent
