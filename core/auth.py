import os
import time
import logging

logger = logging.getLogger(__name__)

class TokenStore:
    """Simple token holder; extend with refresh logic if needed."""
    def __init__(self, token: str = None, expires_at: float = None):
        self.token = token
        self.expires_at = expires_at or 0

    def is_valid(self) -> bool:
        return bool(self.token) and time.time() < self.expires_at - 30

    def set(self, token: str, ttl: int = 3600):
        self.token = token
        self.expires_at = time.time() + ttl
        logger.debug("Token set; expires in %s secs", ttl)

    def get(self):
        return self.token
