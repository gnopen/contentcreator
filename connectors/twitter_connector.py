"""Twitter / X connector (uses tweepy v2 API)."""

from typing import Optional

from connectors.base import SocialMediaConnector, PostResult
from config import twitter as twitter_cfg
from utils import get_logger

log = get_logger(__name__)


class TwitterConnector(SocialMediaConnector):
    platform = "twitter"

    def __init__(self) -> None:
        import tweepy  # lazy import

        if not twitter_cfg.api_key:
            raise RuntimeError("Twitter credentials belum diset di .env")

        self.client = tweepy.Client(
            bearer_token=twitter_cfg.bearer_token,
            consumer_key=twitter_cfg.api_key,
            consumer_secret=twitter_cfg.api_secret,
            access_token=twitter_cfg.access_token,
            access_token_secret=twitter_cfg.access_secret,
        )
        # v1.1 untuk media upload
        auth = tweepy.OAuth1UserHandler(
            twitter_cfg.api_key,
            twitter_cfg.api_secret,
            twitter_cfg.access_token,
            twitter_cfg.access_secret,
        )
        self.api_v1 = tweepy.API(auth)
        log.info("TwitterConnector ready")

    def post(self, text: str, image_path: Optional[str] = None) -> PostResult:
        try:
            media_ids = None
            if image_path:
                media = self.api_v1.media_upload(filename=image_path)
                media_ids = [media.media_id]

            resp = self.client.create_tweet(text=text, media_ids=media_ids)
            tweet_id = resp.data["id"]
            return PostResult(
                platform=self.platform,
                success=True,
                post_id=str(tweet_id),
                url=f"https://twitter.com/i/status/{tweet_id}",
            )
        except Exception as exc:
            log.exception("Twitter post failed")
            return PostResult(platform=self.platform, success=False, error=str(exc))
