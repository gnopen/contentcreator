"""
Social Media Posting Agent
==========================
Mendistribusikan ContentPackage ke beberapa platform sekaligus.

Mendukung:
- Immediate posting
- Scheduled posting (via `post_at` datetime — sleeps sampai waktu tiba)
- Dry-run mode (preview tanpa memanggil API beneran)
"""

from __future__ import annotations

import time
from datetime import datetime
from typing import Iterable, Optional

from agents.content_creator_agent import ContentPackage, PlatformContent
from connectors.base import PostResult, SocialMediaConnector
from utils import get_logger

log = get_logger(__name__)


PLATFORM_REGISTRY: dict[str, type[SocialMediaConnector]] = {}


def _load_registry() -> None:
    """Lazy-register agar import error per-platform tidak crash semuanya."""
    global PLATFORM_REGISTRY
    if PLATFORM_REGISTRY:
        return
    try:
        from connectors.twitter_connector import TwitterConnector
        PLATFORM_REGISTRY["twitter"] = TwitterConnector
    except Exception as e:
        log.debug("Twitter connector unavailable: %s", e)
    try:
        from connectors.facebook_connector import FacebookConnector
        PLATFORM_REGISTRY["facebook"] = FacebookConnector
    except Exception as e:
        log.debug("Facebook connector unavailable: %s", e)
    try:
        from connectors.instagram_connector import InstagramConnector
        PLATFORM_REGISTRY["instagram"] = InstagramConnector
    except Exception as e:
        log.debug("Instagram connector unavailable: %s", e)
    try:
        from connectors.linkedin_connector import LinkedInConnector
        PLATFORM_REGISTRY["linkedin"] = LinkedInConnector
    except Exception as e:
        log.debug("LinkedIn connector unavailable: %s", e)


class SocialMediaAgent:
    def __init__(self, dry_run: bool = False) -> None:
        self.dry_run = dry_run
        _load_registry()
        log.info("SocialMediaAgent ready (dry_run=%s)", dry_run)

    def publish(
        self,
        package: ContentPackage,
        platforms: Iterable[str],
        image_paths: Optional[dict[str, str]] = None,
        post_at: Optional[datetime] = None,
    ) -> list[PostResult]:
        """
        Publish konten ke daftar platform.

        image_paths: dict {platform: path_or_url}
        post_at:     bila diisi, agent akan sleep sampai waktu tersebut.
        """
        if post_at:
            self._wait_until(post_at)

        image_paths = image_paths or {}
        results: list[PostResult] = []

        for plat in platforms:
            plat = plat.lower().strip()
            try:
                content = package.for_platform(plat)
            except ValueError as e:
                results.append(PostResult(platform=plat, success=False, error=str(e)))
                continue

            text = self._compose_text(content)
            image = image_paths.get(plat)

            if self.dry_run:
                log.info("[DRY-RUN] %s -> %s", plat, text[:80])
                results.append(
                    PostResult(platform=plat, success=True, post_id="dry-run", url=None)
                )
                continue

            connector_cls = PLATFORM_REGISTRY.get(plat)
            if not connector_cls:
                results.append(
                    PostResult(
                        platform=plat,
                        success=False,
                        error=f"Connector untuk {plat} tidak tersedia (credentials hilang?)",
                    )
                )
                continue

            try:
                connector = connector_cls()
                result = connector.post(text=text, image_path=image)
                results.append(result)
                log.info(
                    "Posted to %s: success=%s id=%s",
                    plat, result.success, result.post_id,
                )
            except Exception as exc:
                log.exception("Failed to post to %s", plat)
                results.append(
                    PostResult(platform=plat, success=False, error=str(exc))
                )

        return results

    @staticmethod
    def _compose_text(content: PlatformContent) -> str:
        text = content.text or ""
        if content.hashtags:
            tags = " ".join(
                h if h.startswith("#") else f"#{h.lstrip('#')}" for h in content.hashtags
            )
            # Hindari duplikasi bila hashtag sudah ada di text
            if not any(h.lstrip("#").lower() in text.lower() for h in content.hashtags):
                text = f"{text}\n\n{tags}"
        return text.strip()

    @staticmethod
    def _wait_until(when: datetime) -> None:
        delta = (when - datetime.now()).total_seconds()
        if delta <= 0:
            return
        log.info("Scheduled post: sleeping %.0fs until %s", delta, when)
        time.sleep(delta)
