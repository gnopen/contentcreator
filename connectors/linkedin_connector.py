"""LinkedIn UGC Post connector."""

from typing import Optional

import requests

from connectors.base import SocialMediaConnector, PostResult
from config import linkedin as li_cfg
from utils import get_logger

log = get_logger(__name__)


class LinkedInConnector(SocialMediaConnector):
    platform = "linkedin"

    def __init__(self) -> None:
        if not li_cfg.access_token or not li_cfg.author_urn:
            raise RuntimeError("LinkedIn credentials belum diset di .env")
        self.token = li_cfg.access_token
        self.author = li_cfg.author_urn  # mis. urn:li:person:xxx atau urn:li:organization:xxx
        log.info("LinkedInConnector ready (author=%s)", self.author)

    def post(self, text: str, image_path: Optional[str] = None) -> PostResult:
        # Catatan: text-only post; image upload LinkedIn butuh 2-step
        # (register upload -> upload binary -> create post). Disederhanakan
        # ke text-only — extend bila diperlukan.
        try:
            url = "https://api.linkedin.com/v2/ugcPosts"
            headers = {
                "Authorization": f"Bearer {self.token}",
                "X-Restli-Protocol-Version": "2.0.0",
                "Content-Type": "application/json",
            }
            payload = {
                "author": self.author,
                "lifecycleState": "PUBLISHED",
                "specificContent": {
                    "com.linkedin.ugc.ShareContent": {
                        "shareCommentary": {"text": text},
                        "shareMediaCategory": "NONE",
                    }
                },
                "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"},
            }
            resp = requests.post(url, headers=headers, json=payload, timeout=30)
            resp.raise_for_status()
            post_id = resp.headers.get("x-restli-id") or resp.json().get("id")
            return PostResult(
                platform=self.platform,
                success=True,
                post_id=post_id,
            )
        except Exception as exc:
            log.exception("LinkedIn post failed")
            return PostResult(platform=self.platform, success=False, error=str(exc))
