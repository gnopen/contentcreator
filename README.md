# Content Creator Agent System

Multi-agent system untuk membuat konten otomatis dengan Gemini Pro dan posting ke berbagai platform social media.

## Arsitektur

```
                     ┌─────────────────────┐
                     │   Orchestrator      │
                     │  (main pipeline)    │
                     └──────────┬──────────┘
                                │
              ┌─────────────────┼─────────────────┐
              ▼                 ▼                 ▼
    ┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐
    │ Content Creator  │ │  Gemini Pro      │ │  Social Media    │
    │     Agent        │◄┤   Connector      │ │  Posting Agent   │
    └──────────────────┘ └──────────────────┘ └────────┬─────────┘
                                                       │
                                  ┌────────────────────┼──────────────────┐
                                  ▼                    ▼                  ▼
                            ┌──────────┐         ┌──────────┐      ┌──────────┐
                            │ Twitter  │         │Instagram │      │ LinkedIn │
                            │    /X    │         │ Facebook │      │          │
                            └──────────┘         └──────────┘      └──────────┘
```

## Komponen

1. **Content Creator Agent** (`agents/content_creator_agent.py`)
   - Menerima topik / brief dari user
   - Menghasilkan ide, caption, hashtag, dan variasi konten via Gemini Pro
   - Output berformat siap-posting per platform

2. **Gemini Pro Connector** (`connectors/gemini_connector.py`)
   - Wrapper untuk Google Generative AI SDK
   - Mendukung text generation, multimodal, dan structured output (JSON)
   - Retry & error handling

3. **Social Media Posting Agent** (`agents/social_media_agent.py`)
   - Mendistribusikan konten ke platform yang dipilih
   - Per-platform connector (Twitter/X, Instagram, Facebook, LinkedIn)
   - Schedule & immediate post

4. **Orchestrator** (`agents/orchestrator.py`)
   - Pipeline end-to-end: brief → konten → posting

## Cara Pakai

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Copy & isi credentials
cp .env.example .env
# edit .env: GEMINI_API_KEY, TWITTER_*, FACEBOOK_*, LINKEDIN_*, dst.

# 3. Jalankan
python main.py --topic "Tips produktivitas remote working" --platforms twitter,linkedin
```

## Mendapatkan API Keys

- **Gemini Pro**: https://aistudio.google.com/app/apikey
- **Twitter/X**: https://developer.twitter.com/en/portal/dashboard
- **Facebook / Instagram**: https://developers.facebook.com/apps/
- **LinkedIn**: https://www.linkedin.com/developers/apps
