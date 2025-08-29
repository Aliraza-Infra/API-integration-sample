import requests
import logging
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

class APIClient:
    def __init__(self, base_url: str, headers: Optional[Dict[str, str]] = None, timeout: int = 15):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update(headers or {})
        self.timeout = timeout

    def _url(self, path: str) -> str:
        if path.startswith('http'):
            return path
        return f"{self.base_url}/{path.lstrip('/')}"

    def request(self, method: str, path: str, **kwargs) -> requests.Response:
        url = self._url(path)
        logger.debug("Request %s %s", method, url)
        try:
            resp = self.session.request(method, url, timeout=self.timeout, **kwargs)
            resp.raise_for_status()
            return resp
        except requests.HTTPError as e:
            logger.error("HTTP error %s %s: %s", method, url, e)
            raise
        except Exception as e:
            logger.error("Request error %s %s: %s", method, url, e)
            raise

    def get(self, path: str, params: Dict[str, Any] = None, **kwargs):
        return self.request('GET', path, params=params, **kwargs)

    def post(self, path: str, data: Any = None, json: Any = None, **kwargs):
        return self.request('POST', path, data=data, json=json, **kwargs)
