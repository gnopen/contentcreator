# QA Agent Pack — Start Here

A complete starter kit for QA engineers and SDETs who want to augment their work with AI agents. **Drag-drop this entire folder into Google Drive** and share the folder link with your team.

---

## What's in This Folder (8 files)

| # | File | What it is |
|---|------|------------|
| 00 | `00-START-HERE.md` | This file — read first |
| 01 | `01-agent-system-prompt.md` | The brain — paste into Claude Project / ChatGPT |
| 02 | `02-skill-test-case-generator.md` | Skill — generate test cases from user stories |
| 03 | `03-skill-bug-report-formatter.md` | Skill — turn messy notes into ticket-ready reports |
| 04 | `04-skill-edge-case-brainstormer.md` | Skill — 12-category edge case walkthrough |
| 05 | `05-skill-regression-tracker.md` | Skill — plan, track, summarize regression runs |
| 06 | `06-skill-test-plan-writer.md` | Skill — lean and detailed test plan documents |
| 07 | `07-connector-slack.md` | Send agent outputs to Slack |
| 08 | `08-connector-google-drive.md` | Archive agent outputs to Google Drive |

---

## 15-Minute Setup

### Step 1 — Choose your LLM platform

**Option A: Claude (recommended)**
- Go to [claude.ai](https://claude.ai)
- Click **Projects** in the sidebar → **Create Project**
- Name it: `QA Agent`

**Option B: ChatGPT**
- Go to [chat.openai.com](https://chat.openai.com)
- Click your profile → **My GPTs** → **Create a GPT**
- Name it: `QA Agent`

### Step 2 — Load the agent brain

1. Open `01-agent-system-prompt.md`
2. Copy the content inside the ` ``` ` code block
3. Paste into:
   - **Claude Project:** Project instructions field
   - **ChatGPT:** "Instructions" field of your custom GPT

### Step 3 — Upload the 5 skills

For each of the 5 skill files (02 through 06):
1. Download / open the `.md` file
2. Upload to your Claude Project's knowledge files (or ChatGPT custom GPT knowledge)

### Step 4 — Test it

In a new chat with your agent, try:
- *"Generate test cases for a login flow with email + password + magic link"*
- *"I noticed checkout breaks on iOS Safari sometimes. Help me format a bug report."*
- *"Brainstorm edge cases for a file upload feature accepting PDFs up to 25MB"*

The agent should route to the right skill automatically.

---

## Optional — Setup Integrations

If you want agent outputs to flow into your team's tools:

### Connect Slack
Open `07-connector-slack.md`. Follow the **Incoming Webhook** path (simplest, 5 minutes). Use cases:
- Daily regression summaries posted to `#qa-daily`
- Critical bug alerts to `#bugs-critical`
- Morning brief delivered to your DM

### Connect Google Drive
Open `08-connector-google-drive.md`. Follow the **Apps Script** path (no API setup needed). Use cases:
- Auto-archive test reports per release
- Store bug evidence (screenshots, logs)
- Daily test artifact backup

---

## Recommended Workflow

```
Daily / Weekly
├── Morning: Open agent, ask for daily plan or test case priorities
├── During: Use Bug Report Formatter for any bugs you find
├── End of day: Ask agent to summarize what you covered
└── Friday: Run regression with Regression Tracker, archive to Drive

Per Release
├── Day -7: Test Plan Writer drafts the plan
├── Days -3 to 0: Regression Tracker manages execution
├── Day 0: Summary report archived to Drive + posted to Slack
└── Day +7: Retrospective using accumulated logs
```

---

## Customization

The default agent is generic. To make it work better for your team, edit `01-agent-system-prompt.md`:

| Section to edit | What to add |
|-----------------|-------------|
| Domain context | "We're a [healthcare/fintech/e-commerce] platform. Critical paths: [list]." |
| Severity scale | Replace Critical/High/Medium/Low with your team's scale (e.g., P0-P3) |
| Tool stack | "We use Playwright + GitHub Actions + Jira" |
| Output format defaults | Replace "Gherkin" with your team's preferred format |
| Compliance flags | "Flag any test that touches PHI/PCI data" |

Save the edited version in your Project — every chat will use the customized version.

---

## Security & Privacy Notes

✅ This pack contains:
- Generic system prompts and skill definitions
- Placeholder examples (no real company data)
- Documented best practices for credential handling
- Multiple setup paths so you can choose your security comfort level

❌ This pack does NOT contain:
- Any real API keys, tokens, or secrets
- Any specific company workflows
- Any actual production agent code

### Before sharing with your team

If you customize this pack with company-specific context (domain, severity scale, tools), consider:
- Whether your customized version is OK to share publicly or should stay internal
- Strip any references to internal systems, customer names, or proprietary processes before sharing externally
- Use a separate Project / GPT for customer-confidential context that you don't share

---

## How to Use With Google Drive

### To upload this pack to Drive:
1. Download this entire folder (`qa-agent-pack/`)
2. In Drive, create a new folder (e.g., `QA AI Pack`)
3. Drag-drop all 9 files into the new folder
4. Share with your team (View access for users, Editor for the QA Lead)

### Recommended Drive structure for team:
```
Your Drive/
└── QA AI Pack/
    ├── 00-START-HERE.md
    ├── 01-agent-system-prompt.md
    ├── ... (all 9 files)
    └── _team-customizations/        ← create this subfolder for your edits
        ├── custom-system-prompt.md
        └── custom-skill-bug-format.md
```

Keep originals untouched; team edits live in `_team-customizations/`. Makes it easy to pull future updates without losing your changes.

---

## Updates

This pack will be updated periodically. To check for newer versions:
- **Source repo:** [github.com/gnopen/contentcreator/tree/main/ai-daily-routine/qa-agent-pack](https://github.com/gnopen/contentcreator/tree/main/ai-daily-routine/qa-agent-pack)
- **Follow updates:** [@aidailyroutine](https://instagram.com/aidailyroutine) on Instagram

Major version log:
- **v1.0** (2026-05-22) — Initial release. Agent + 5 skills + 2 connectors.

---

## Questions / Feedback

DM `@aidailyroutine` on Instagram with what you built. Best DMs become future case studies (with your permission).

If something here is broken or unclear, that's useful to hear too.

---

## What's Next?

Once your agent is running and useful, consider these next-level moves:

1. **Build 2-3 custom skills** for your specific workflows (using the skill files as templates)
2. **Connect to your CI/CD** so test results auto-flow into the agent for analysis
3. **Set up scheduled triggers** (e.g., n8n cron) so agent runs reports without you asking
4. **Share your customizations** with the team — let everyone start from the same agent baseline

The full course on **building agentic systems + skill libraries** covers all of this in depth — 4 weekly live sessions, cohort-based. DM `AGENT` to `@aidailyroutine` for class waitlist.

---

## License

Free to use, modify, and share for personal or team use. Attribution appreciated when shared publicly. Don't repackage and sell as a course without permission.
