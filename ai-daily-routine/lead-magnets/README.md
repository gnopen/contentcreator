# Lead Magnets — Free Resources

Open-source resources shared with anyone who comments on `@aidailyroutine` content. Designed to be **immediately useful** without exposing internal/proprietary workflows.

---

## Folder Index

```
lead-magnets/
├── README.md                          — this file
├── higgsfield-prompts/
│   └── qa-warroom-cinematic.md        — Cinematic video prompt for QA war room (Higgsfield, Runway, Sora)
├── qa-pack/
│   ├── 00-qa-agent-system-prompt.md   — General-purpose QA agent system prompt
│   ├── 01-skill-test-case-generator.md
│   ├── 02-skill-bug-report-formatter.md
│   ├── 03-skill-edge-case-brainstormer.md
│   ├── 04-skill-regression-tracker.md
│   └── 05-skill-test-plan-writer.md
└── connectors/
    ├── slack-connector.md             — Generic Slack integration guide
    └── google-drive-connector.md      — Generic Google Drive integration guide
```

---

## DM Routing Table (for `@aidailyroutine`)

When a follower comments with a keyword on Instagram or TikTok, auto-DM them the appropriate resource link:

| Comment keyword | Send DM with link to |
|------------------|----------------------|
| `QA` | `qa-pack/` folder |
| `AGENT` | `qa-pack/00-qa-agent-system-prompt.md` + 1 sample skill |
| `SLACK` | `connectors/slack-connector.md` |
| `DRIVE` | `connectors/google-drive-connector.md` |
| `VIDEO` or `HIGGSFIELD` | `higgsfield-prompts/` folder |
| `RUTIN` (general) | This README + 3 starter skills |

---

## What's Inside Each Pack

### `qa-pack/` — Free QA Agent + 5 Skills

Setup time: **15 minutes**. Outcome: a working AI assistant tuned for QA work.

A complete starter pack for QA engineers and SDETs who want to augment their work with AI. Includes:

- **System prompt** that turns any LLM (Claude, ChatGPT) into a QA-aware assistant
- **5 skills** the agent can route to automatically:
  1. Test Case Generator (Gherkin / plain / TestRail)
  2. Bug Report Formatter (messy notes → ticket-ready report)
  3. Edge Case Brainstormer (12-category systematic walkthrough)
  4. Regression Tracker (plan, live status, summary)
  5. Test Plan Writer (lean and detailed formats)

**How to use:**
1. Open [claude.ai](https://claude.ai) → Create new Project
2. Paste system prompt from `00-qa-agent-system-prompt.md` into project instructions
3. Upload all 5 skill `.md` files as project knowledge
4. Start chatting

**What it won't do:**
- Won't replace human QA judgment
- Won't run tests for you (it generates test cases, doesn't execute)
- Won't access your internal systems without you setting up connectors

---

### `connectors/` — Integration Guides

Setup time: **20-30 minutes per connector**. Outcome: agent outputs flow to your team's tools.

Generic, security-conscious setup guides for the two most common integration points:

- **Slack** — Send agent outputs to channels or DMs
- **Google Drive** — Archive generated reports and artifacts

Both guides include multiple setup paths (simple webhook / robust API / no-code platforms), security best practices, and troubleshooting tables.

**What's NOT included:**
- No actual API keys or credentials
- No pre-built code that requires your private setup
- No assumptions about your team structure

These are **patterns**, not turnkey integrations. You connect them to your own context.

---

### `higgsfield-prompts/` — Cinematic Video Prompts

A growing collection of paste-ready prompts for AI cinematic video generators (Higgsfield, Runway, Sora, Kling).

Currently includes:
- **QA War Room** — Enterprise-grade SDET operations video (great for landing pages, conference reels, course intros)

More prompts coming as the series develops.

---

## Security & Privacy Promise

Everything in this folder is:
- ✅ **Generic** — no company-specific workflows leak through
- ✅ **Credential-free** — never includes real API keys, tokens, or secrets
- ✅ **Privacy-aware** — instructs you on safe practices for any sensitive data
- ✅ **Open** — MIT-style usage; remix freely

Everything in this folder is NOT:
- ❌ The full content of the paid Agentic + Skills class
- ❌ The actual production agents running `@aidailyroutine`'s operations
- ❌ Personalized to one operator's specific stack

The free pack is a **starter kit**. The paid class is where you go deeper, integrate into your own workflow, and build a personal skill library across 4 weeks.

---

## Where the Free Pack Ends, the Class Begins

| Topic | Free Pack | Paid Class |
|-------|-----------|------------|
| Generic system prompt | ✓ Included | ✓ + 12 more, customized to your work |
| 5 skill templates | ✓ Included | ✓ + 9 more skills you design from scratch |
| Slack / Drive setup guide | ✓ Included | ✓ + live debugging when yours breaks |
| Agent anatomy | ❌ | ✓ Built end-to-end across 4 weeks |
| Multi-agent orchestration | ❌ | ✓ Connect agents that talk to each other |
| Triggers + scheduling | ❌ | ✓ Time-based, event-based, voice |
| Personalized for your role | ❌ | ✓ Live mentor review on every project |
| Cohort + alumni network | ❌ | ✓ Discord access + 6 mo. office hours |

Class details: see `ai-daily-routine/03-content-strategy.md` or DM `@aidailyroutine`.

---

## License & Attribution

These materials are free to use, modify, and share for personal or team use.

- ✅ Use in your own work
- ✅ Adapt and remix for your team's needs
- ✅ Share with colleagues
- ⚠️ Attribution appreciated when sharing publicly: link back to `@aidailyroutine`
- ❌ Don't repackage and sell as a course without permission

---

## Feedback

If something here helped, send a DM at `@aidailyroutine` — preferably with what you built. Best DMs become future case studies (with your permission).

If something is broken, missing, or could be clearer, that's also useful to hear.

---

## Versioning

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-05-22 | Initial release — QA pack + 2 connectors + 1 video prompt |
