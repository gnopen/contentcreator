from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass
class PostResult:
    platform: str
    success: bool
    post_id: Optional[str] = None
    url: Optional[str] = None
    error: Optional[str] = None


class SocialMediaConnector(ABC):
    """Interface umum semua social media connector."""

    platform: str = "base"

    @abstractmethod
    def post(self, text: str, image_path: Optional[str] = None) -> PostResult:
        """Publish ke platform. Return PostResult."""
