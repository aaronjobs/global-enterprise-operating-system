"""GEOS: Global Enterprise Operating System - Production v2"""

__version__ = "2.0.0"
__author__ = "Aaron Jobson"
__description__ = "Enterprise AI Agent Operating System"

from geos.main import app
from geos.config import Settings

__all__ = ["app", "Settings"]
