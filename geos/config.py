"""GEOS Configuration Management"""

from typing import List
from pydantic_settings import BaseSettings
from pydantic import Field
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    """GEOS Application Settings"""
    
    # FastAPI
    app_name: str = "GEOS"
    app_version: str = "2.0.0"
    app_env: str = Field(default="development", alias="FASTAPI_ENV")
    debug: bool = Field(default=False, alias="FASTAPI_DEBUG")
    host: str = Field(default="0.0.0.0", alias="FASTAPI_HOST")
    port: int = Field(default=8000, alias="FASTAPI_PORT")
    log_level: str = Field(default="info", alias="FASTAPI_LOG_LEVEL")
    
    # Database
    database_url: str = Field(default="sqlite:///./geos.db", alias="DATABASE_URL")
    
    # Plugin Registry
    plugin_registry_path: str = Field(default="/etc/geos/plugins", alias="PLUGIN_REGISTRY_PATH")
    plugin_cache_ttl: int = Field(default=300, alias="PLUGIN_CACHE_TTL")
    
    # Observability
    observability_enabled: bool = Field(default=True, alias="OBSERVABILITY_ENABLED")
    log_format: str = Field(default="json", alias="LOG_FORMAT")
    
    # Security
    api_key_secret: str = Field(default="secret-key", alias="API_KEY_SECRET")
    cors_origins: List[str] = Field(
        default=["http://localhost:3000", "http://localhost:8000"],
        alias="CORS_ORIGINS"
    )
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


# Load settings
settings = Settings()
