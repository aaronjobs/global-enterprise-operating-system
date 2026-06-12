"""GEOS Plugins API"""

from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()


class PluginMetadata(BaseModel):
    """Plugin metadata"""
    name: str
    version: str
    author: str
    description: str


class Plugin(BaseModel):
    """Plugin model"""
    id: str
    metadata: PluginMetadata
    status: str = "installed"
    capabilities: List[str] = []


@router.get("/plugins", response_model=List[Plugin])
async def list_plugins():
    """List installed plugins"""
    return []


@router.get("/plugins/{plugin_id}", response_model=Plugin)
async def get_plugin(plugin_id: str):
    """Get plugin by ID"""
    raise HTTPException(status_code=404, detail="Plugin not found")


@router.post("/plugins", response_model=Plugin, status_code=status.HTTP_201_CREATED)
async def register_plugin(plugin: Plugin):
    """Register new plugin"""
    return plugin
