"""End-to-end pipeline: brief -> content -> publish."""

from __future__ import annotations

from datetime import datetime
from typing import Iterable, Optional

from agents.content_creator_agent import ContentCreatorAgent, ContentPackage
from agents.social_media_agent import SocialMediaAgent
from connectors.base import PostResult
from utils import get_logger

log = get_logger(__name__)


class Orchestrator:
    def __init__(self, dry_run: bool = False) -> None:
        self.creator = ContentCreatorAgent()
        self.publisher = SocialMediaAgent(dry_run=dry_run)

    def run(
        self,
        topic: str,
        platforms: Iterable[str],
        tone: str = "engaging dan profesional",
        target_audience: str = "umum",
        language: str = "Indonesia",
        extra_context: Optional[str] = None,
        image_paths: Optional[dict[str, str]] = None,
        post_at: Optional[datetime] = None,
    ) -> tuple[ContentPackage, list[PostResult]]:
        log.info("Pipeline start: topic=%r platforms=%s", topic, list(platforms))
        package = self.creator.create(
            topic=topic,
            tone=tone,
            target_audience=target_audience,
            language=language,
            extra_context=extra_context,
        )
        results = self.publisher.publish(
            package=package,
            platforms=platforms,
            image_paths=image_paths,
            post_at=post_at,
        )
        log.info("Pipeline done. %d post results.", len(results))
        return package, results
