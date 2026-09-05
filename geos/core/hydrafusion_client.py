from typing import Optional, Dict, Any
import os
import time
import json
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from geos.core.hydrafusion_logging import HydraFusionLogger

HYDRAFUSION_URL = os.getenv(
    "HYDRAFUSION_URL",
    "https://hydrafusion.example/api/v1/complete"
)
DEFAULT_TIMEOUT = 20  # seconds


class HydraFusionError(RuntimeError):
    """Base error for HydraFusion HTTP client."""
    pass


class HydraFusionClient:
    """
    HTTP-backed HydraFusion orchestration client for GEOS.

    - Uses HYDRAFUSION_URL + HYDRAFUSION_API_KEY from environment.
    - Provides retries, timeouts, and structured error handling.
    - Returns unified text responses for GEOS agents.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        timeout: int = DEFAULT_TIMEOUT,
    ):
        self.api_key = api_key or os.getenv("HYDRAFUSION_API_KEY")
        self.base_url = base_url or HYDRAFUSION_URL
        self.timeout = timeout

        session = requests.Session()
        retries = Retry(
            total=3,
            backoff_factor=0.5,
            status_forcelist=(502, 503, 504),
            allowed_methods=["POST"],
        )
        adapter = HTTPAdapter(max_retries=retries)
        session.mount("https://", adapter)
        session.mount("http://", adapter)
        self._session = session

        self.logger = HydraFusionLogger()

    def _headers(self) -> Dict[str, str]:
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        return headers

    def _build_payload(self, prompt: str, mode: str, extra: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        payload: Dict[str, Any] = {
            "prompt": prompt,
            "mode": mode,
            # Add HydraFusion-specific fields here as needed:
            # "max_tokens": 2048,
            # "temperature": 0.2,
        }
        if extra:
            payload.update(extra)
        return payload

    def complete(
        self,
        prompt: str,
        mode: str = "reasoning",
        domain: str = "unknown",
        intent: str = "unknown",
        extra: Optional[Dict[str, Any]] = None,
    ) -> str:
        payload = self._build_payload(prompt, mode, extra)
        start = time.time()

        try:
            resp = self._session.post(
                self.base_url,
                json=payload,
                headers=self._headers(),
                timeout=self.timeout,
            )

            # Log raw response before any parsing
            self.logger.log_raw_cli(resp.text, "")

            # Raise for status BEFORE JSON parsing
            resp.raise_for_status()

            try:
                data = resp.json()
            except json.JSONDecodeError as e:
                self.logger.log_error(domain, intent, prompt, e)
                raise HydraFusionError("hydrafusion returned malformed JSON") from e

            text = (
                data.get("text")
                or data.get("result")
                or data.get("output")
                or ""
            ).strip()

            duration = time.time() - start
            self.logger.log_success(
                domain,
                intent,
                prompt,
                text,
                duration,
                status_code=resp.status_code,
            )
            return text

        except requests.RequestException as e:
            duration = time.time() - start
            self.logger.log_error(domain, intent, prompt, e)
            raise HydraFusionError(f"hydrafusion request failed: {e}") from e
