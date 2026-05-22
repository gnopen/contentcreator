import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class GeminiSettings:
    api_key: str = os.getenv("GEMINI_API_KEY", "")
    model: str = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")


@dataclass
class TwitterSettings:
    api_key: str = os.getenv("TWITTER_API_KEY", "")
    api_secret: str = os.getenv("TWITTER_API_SECRET", "")
    access_token: str = os.getenv("TWITTER_ACCESS_TOKEN", "")
    access_secret: str = os.getenv("TWITTER_ACCESS_SECRET", "")
    bearer_token: str = os.getenv("TWITTER_BEARER_TOKEN", "")


@dataclass
class FacebookSettings:
    page_id: str = os.getenv("FACEBOOK_PAGE_ID", "")
    access_token: str = os.getenv("FACEBOOK_ACCESS_TOKEN", "")
    instagram_business_account_id: str = os.getenv("INSTAGRAM_BUSINESS_ACCOUNT_ID", "")


@dataclass
class LinkedInSettings:
    access_token: str = os.getenv("LINKEDIN_ACCESS_TOKEN", "")
    author_urn: str = os.getenv("LINKEDIN_AUTHOR_URN", "")


LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

gemini = GeminiSettings()
twitter = TwitterSettings()
facebook = FacebookSettings()
linkedin = LinkedInSettings()
