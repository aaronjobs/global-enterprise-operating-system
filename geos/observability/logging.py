"""Observability - Logging Configuration"""

import logging
import json
from pythonjsonlogger import jsonlogger
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
import time


def setup_logging(log_format: str = "json", log_level: str = "info"):
    """Configure application logging"""
    logger = logging.getLogger()
    logger.setLevel(log_level.upper())
    
    handler = logging.StreamHandler()
    
    if log_format == "json":
        formatter = jsonlogger.JsonFormatter()
    else:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    
    handler.setFormatter(formatter)
    logger.addHandler(handler)


class RequestLogger(BaseHTTPMiddleware):
    """Middleware for logging HTTP requests"""
    
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time
        
        logger = logging.getLogger(__name__)
        logger.info({
            "method": request.method,
            "path": request.url.path,
            "status_code": response.status_code,
            "duration_ms": round(duration * 1000, 2)
        })
        
        return response
