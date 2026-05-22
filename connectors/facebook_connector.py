"""Facebook Page connector via Graph API."""

from typing import Optional

import requests

from connectors.base import SocialMediaConnector, PostResult
from config import facebook as fb_cfg
from utils import get_logger

log = get_logger(__name__)

GRAPH_API_VERSION = "v19.0"


class FacebookConnector(SocialMediaConnector):
    platform = "facebook"

    def __init__(self) -> None:
        if not fb_cfg.page_id or not fb_cfg.access_token:
            raise RuntimeError("Facebook credentials belum diset di .env")
        self.page_id = fb_cfg.page_id
        self.token = fb_cfg.access_token
        log.info("FacebookConnector ready (page=%s)", self.page_id)

    def post(self, text: str, image_path: Optional[str] = None) -> PostResult:
        try:
            if image_path:
                url = f"https://graph.facebook.com/{GRAPH_API_VERSION}/{self.page_id}/photos"
                with open(image_path, "rb") as fh:
                    resp = requests.post(
                        url,
                        data={"caption": text, "access_token": self.token},
                        files={"source": fh},
                        timeout=30,
                    )
            else:
                url = f"https://graph.facebook.com/{GRAPH_API_VERSION}/{self.page_id}/feed"
                resp = requests.post(
                    url,
                    data={"message": text, "access_token": self.token},
                    timeout=30,
                )

            resp.raise_for_status()
            data = resp.json()
            post_id = data.get("post_id") or data.get("id")
            return PostResult(
                platform=self.platform,
                success=True,
                post_id=post_id,
                url=f"https://facebook.com/{post_id}" if post_id else None,
            )
        except Exception as exc:
            log.exception("Facebook post failed")
            return PostResult(platform=self.platform, success=False, error=str(exc))
