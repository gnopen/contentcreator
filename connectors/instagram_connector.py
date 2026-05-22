"""
Instagram Business connector via Graph API.

Instagram WAJIB pakai gambar (atau video). Image harus accessible
via public URL — Graph API tidak menerima upload langsung untuk IG.
Untuk lokal-file, host dulu (S3 / CDN / ngrok) atau gunakan parameter
`image_url`.
"""

from typing import Optional

import requests

from connectors.base import SocialMediaConnector, PostResult
from config import facebook as fb_cfg
from utils import get_logger

log = get_logger(__name__)

GRAPH_API_VERSION = "v19.0"


class InstagramConnector(SocialMediaConnector):
    platform = "instagram"

    def __init__(self) -> None:
        if not fb_cfg.instagram_business_account_id or not fb_cfg.access_token:
            raise RuntimeError("Instagram credentials belum diset di .env")
        self.ig_id = fb_cfg.instagram_business_account_id
        self.token = fb_cfg.access_token
        log.info("InstagramConnector ready (ig=%s)", self.ig_id)

    def post(self, text: str, image_path: Optional[str] = None) -> PostResult:
        """`image_path` di sini dipakai sebagai PUBLIC URL gambar."""
        try:
            if not image_path:
                return PostResult(
                    platform=self.platform,
                    success=False,
                    error="Instagram membutuhkan image_url (public URL).",
                )

            create_url = f"https://graph.facebook.com/{GRAPH_API_VERSION}/{self.ig_id}/media"
            create_resp = requests.post(
                create_url,
                data={
                    "image_url": image_path,
                    "caption": text,
                    "access_token": self.token,
                },
                timeout=30,
            )
            create_resp.raise_for_status()
            creation_id = create_resp.json()["id"]

            publish_url = f"https://graph.facebook.com/{GRAPH_API_VERSION}/{self.ig_id}/media_publish"
            pub_resp = requests.post(
                publish_url,
                data={"creation_id": creation_id, "access_token": self.token},
                timeout=30,
            )
            pub_resp.raise_for_status()
            post_id = pub_resp.json().get("id")
            return PostResult(
                platform=self.platform,
                success=True,
                post_id=post_id,
            )
        except Exception as exc:
            log.exception("Instagram post failed")
            return PostResult(platform=self.platform, success=False, error=str(exc))
