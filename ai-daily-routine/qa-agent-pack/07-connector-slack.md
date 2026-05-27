# Connector — Slack

A general-purpose guide for connecting your AI agent / automation workflow to Slack. Use cases: post test results, send morning briefs, alert on failures, deliver agent outputs to a channel.

---

## What This Enables

- Agent posts a daily summary to `#qa-daily`
- Test pipeline pings `#alerts` when a regression breaks
- Morning brief delivered to your DM at 06:30
- Bug detection agent escalates Critical issues to `#bugs-critical`
- Class instructor sends cohort updates to private student channels

---

## Prerequisites

- A Slack workspace where you have permission to install apps (your own or workspace admin approval)
- An LLM/automation tool that supports HTTP calls or has a Slack integration (Claude, n8n, Zapier, Make, GitHub Actions, custom Python, etc.)
- 15 minutes for first-time setup

---

## Setup — Generic Steps

### Option A: Slack Incoming Webhook (simplest, one-way)

Best for: post-only flows (alerts, summaries, briefs).

#### Step 1 — Create a Slack app
1. Go to https://api.slack.com/apps → **Create New App** → "From scratch"
2. Name: e.g., `AI Daily Assistant`
3. Pick your workspace

#### Step 2 — Enable Incoming Webhooks
1. In the app settings, click **Incoming Webhooks** → toggle "Activate Incoming Webhooks" ON
2. Click **Add New Webhook to Workspace**
3. Choose the channel where messages will post
4. Authorize → copy the webhook URL

⚠️ **The webhook URL is a secret.** Treat it like a password. Anyone with the URL can post to that channel.

#### Step 3 — Test the webhook
From your terminal, paste the URL into a curl command:

```bash
curl -X POST -H 'Content-type: application/json' \
  --data '{"text":"Hello from my AI agent"}' \
  YOUR_WEBHOOK_URL_HERE
```

You should see the message appear in your chosen Slack channel.

#### Step 4 — Use from your agent

**From Claude / GPT with tool use:**
Add a tool that calls the webhook URL with a `text` field.

**From n8n:**
1. Add HTTP Request node
2. Method: POST
3. URL: your webhook URL
4. Body type: JSON
5. Body: `{ "text": "{{ $json.message }}" }`

**From Zapier / Make:**
Pre-built Slack integration — connect with OAuth, no webhook needed for this path.

**From Python:**
```python
import requests
import os

webhook = os.environ["SLACK_WEBHOOK_URL"]
requests.post(webhook, json={"text": "Your message here"})
```

---

### Option B: Slack Bot User (read + write, multi-channel)

Best for: bidirectional flows (agent responds to mentions, reads channel context, posts to multiple channels).

#### Step 1 — Add Bot Token Scopes
In your Slack app settings → **OAuth & Permissions** → **Scopes** → **Bot Token Scopes**, add:

| Scope | Purpose |
|-------|---------|
| `chat:write` | Post messages |
| `channels:read` | List public channels |
| `channels:history` | Read public channel messages |
| `groups:read` | List private channels (if needed) |
| `im:write` | Send DMs |
| `users:read` | Look up user info |

⚠️ **Minimize scopes.** Only request what you actually need. Slack reviews high-scope apps more strictly.

#### Step 2 — Install to workspace
1. Click **Install to Workspace** → authorize
2. Copy the **Bot User OAuth Token** (starts with `xoxb-`)

⚠️ **The bot token is highly sensitive.** Store as environment variable, never in code.

#### Step 3 — Use from your agent

**Python example:**
```python
import os
from slack_sdk import WebClient

client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])

# Post a message
client.chat_postMessage(
    channel="#qa-daily",
    text="Morning brief is ready"
)
```

---

## Message Formatting

### Plain text
```json
{ "text": "Test run completed: 237 of 240 passed." }
```

### Rich formatting with blocks
```json
{
  "blocks": [
    {
      "type": "header",
      "text": { "type": "plain_text", "text": "Morning Brief" }
    },
    {
      "type": "section",
      "fields": [
        { "type": "mrkdwn", "text": "*Cash position*\n$184k operating" },
        { "type": "mrkdwn", "text": "*Pipeline*\nNorthwind $42k" }
      ]
    },
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "*Today's top 3:*\n• Reply Bright Harbor by 2pm\n• Approve Northwind redlines\n• Confirm Thu demo"
      }
    }
  ]
}
```

Test your block layouts with Slack's official **Block Kit Builder**: https://app.slack.com/block-kit-builder

---

## Common Patterns

### Daily summary at 06:30
Schedule via cron / n8n / GitHub Actions / Apple Shortcuts. Build the summary text in your agent, then POST to the webhook.

### Test failure alert
On CI/CD failure, build a summary and POST. Include:
- Pipeline name
- Failure point
- Last successful run timestamp
- Direct link to the failed build

### Bug detection escalation
If your agent detects a Critical severity issue:
1. Post to `#bugs-critical`
2. @-mention the on-call engineer (use their Slack user ID like `<@U12345>`)
3. Include direct ticket link

### DM the morning brief
Use bot token, send DM to specific user:
```python
client.chat_postMessage(
    channel="USER_SLACK_ID",
    text=morning_brief_content
)
```

---

## Security Best Practices

1. **Never commit tokens to git.** Use environment variables.
2. **Rotate tokens every 90 days** or immediately if leaked.
3. **Restrict bot to specific channels** when possible — don't give workspace-wide access if a single channel suffices.
4. **Use signing secret verification** if your agent receives events from Slack (not just sending).
5. **Audit installed apps quarterly** — workspace admins can review who installed what.
6. **Disable webhooks you no longer use** — orphaned webhooks are common security gaps.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| 404 from webhook | URL typo or webhook deleted | Re-create webhook |
| Message not appearing | Channel doesn't exist or bot not invited | Check channel name; `/invite @yourbotname` |
| Rate limit error (429) | Sending too fast | Slack allows ~1 msg/sec to a channel — batch or throttle |
| Blocks render as raw JSON | `text` field missing as fallback | Always include `text` even when using `blocks` |
| Token invalid | Token rotated / expired | Re-issue from Slack app settings |

---

## What This Connector Doesn't Do

This is a **template for setting up a connector** — not a turnkey integration. You still need to:
- Decide WHAT your agent will send (the content logic is up to you)
- Build the prompt or workflow that generates the message
- Handle retries and errors in your code
- Test in a non-prod channel before promoting

---

## Related

- `08-connector-google-drive.md` — Sync test artifacts to Drive (often used alongside Slack alerts)
- `05-skill-regression-tracker.md` — Generates the regression summaries that you'd post to Slack
- `03-skill-bug-report-formatter.md` — Generates the bug reports that you'd escalate to `#bugs-critical`
