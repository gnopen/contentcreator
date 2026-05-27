# Connector — Google Drive

A general-purpose guide for connecting your AI agent / automation workflow to Google Drive. Use cases: archive test artifacts, store generated reports, share files with stakeholders, organize evidence.

---

## What This Enables

- Agent automatically uploads daily test summary PDFs to a shared folder
- Generated bug reports archived per release into a structured tree
- Test screenshots and videos pushed to organized subfolders by date
- AI-generated test plans saved to project folders, shareable with engineers
- Morning brief archived as a daily log for retrospectives

---

## Prerequisites

- A Google account
- An automation platform that supports HTTP or has a Drive integration (n8n, Zapier, Make, Apps Script, Python, etc.)
- 20 minutes for first-time setup

---

## Setup Options

### Option A: Google Apps Script (simplest, no API setup)

Best for: small teams, simple uploads, no separate auth infrastructure.

#### Step 1 — Create a Google Doc / Sheet for your agent
1. Create a new Google Sheet that will host your script
2. Tools → Apps Script

#### Step 2 — Write a Drive upload function
Paste this script:

```javascript
function uploadToDrive(filename, content, folderId) {
  const folder = DriveApp.getFolderById(folderId);
  const blob = Utilities.newBlob(content, 'text/plain', filename);
  folder.createFile(blob);
}

function doPost(e) {
  const data = JSON.parse(e.postData.contents);
  uploadToDrive(data.filename, data.content, data.folderId);
  return ContentService.createTextOutput('OK');
}
```

#### Step 3 — Deploy as web app
1. Deploy → New deployment → Type: Web app
2. Execute as: Me
3. Access: Anyone with the link (or restrict to your domain)
4. Deploy → copy the web app URL

⚠️ **This URL allows uploads to your Drive folder.** Treat as a secret.

#### Step 4 — Use from your agent
```bash
curl -X POST YOUR_WEB_APP_URL \
  -H 'Content-Type: application/json' \
  -d '{
    "filename": "test-report-2026-05-22.md",
    "content": "Test results...",
    "folderId": "YOUR_FOLDER_ID"
  }'
```

Get the `folderId` from the folder's URL: `https://drive.google.com/drive/folders/<THIS_PART>`

---

### Option B: Google Drive API (programmatic, robust)

Best for: production use, granular permissions, large-scale automation.

#### Step 1 — Enable the Drive API
1. Go to https://console.cloud.google.com
2. Create a new project (or use existing)
3. APIs & Services → Library → search "Google Drive API" → Enable

#### Step 2 — Create credentials

**For server-side / agent use: Service Account**
1. APIs & Services → Credentials → Create Credentials → Service Account
2. Name: e.g., `ai-agent-drive`
3. Skip optional grants
4. Done → click the new service account → Keys → Add Key → JSON
5. Download the JSON file (this is your credential)

⚠️ **The JSON file contains a private key.** Never commit to git. Store as a secret.

**For per-user use: OAuth 2.0**
1. Credentials → Create → OAuth client ID → Web application (or Desktop)
2. Add redirect URIs as needed
3. Note the client ID and client secret

#### Step 3 — Share a folder with the service account
1. Note the service account email from the JSON file (e.g., `ai-agent-drive@yourproject.iam.gserviceaccount.com`)
2. In Drive, right-click the folder → Share → add that email with "Editor" permission

#### Step 4 — Use from your agent

**Python example:**
```python
import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Load credentials from environment variable (path to JSON file)
credentials = service_account.Credentials.from_service_account_file(
    os.environ["GOOGLE_SERVICE_ACCOUNT_KEY"],
    scopes=["https://www.googleapis.com/auth/drive.file"]
)

drive = build('drive', 'v3', credentials=credentials)

def upload_file(file_path, filename, folder_id):
    file_metadata = {
        'name': filename,
        'parents': [folder_id]
    }
    media = MediaFileUpload(file_path, resumable=True)
    file = drive.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()
    return file.get('id')

# Usage
file_id = upload_file(
    file_path='./report.md',
    filename='regression-report-2026-05-22.md',
    folder_id=os.environ["DRIVE_FOLDER_ID"]
)
print(f"Uploaded: https://drive.google.com/file/d/{file_id}/view")
```

---

### Option C: n8n / Zapier / Make (no-code)

Best for: non-developers, quick connections.

#### n8n
1. Add Google Drive node
2. Connect via OAuth (one-click)
3. Operation: Upload File
4. Set folder and content from previous nodes

#### Zapier
1. Trigger: any (webhook, schedule, app event)
2. Action: Google Drive → Upload File
3. Connect Drive account, choose folder, map content

#### Make (Integromat)
1. Add Google Drive module → Upload a File
2. Authenticate, choose target folder, map content

---

## Common Patterns

### Daily test artifact archive

Folder structure:
```
/QA Daily/
  /2026-W21/
    /2026-05-20/
      regression-summary.md
      screenshots/
      failed-tests.json
    /2026-05-21/
    /2026-05-22/
```

Agent script:
1. Generate report
2. Create subfolder for today's date (or use Drive's folder ID lookup)
3. Upload report
4. Upload screenshots
5. Post link to Slack (chain with `07-connector-slack.md`)

### Per-release evidence package
Folder structure:
```
/Releases/
  /Q3-2026/
    test-plan.md
    regression-summary.md
    bug-reports/
    performance-baseline.html
    sign-off.pdf
```

### Morning brief archive
```
/Daily Briefs/
  /2026/
    /05/
      2026-05-22.md
      2026-05-23.md
      ...
```

Agent script: append today's brief as `YYYY-MM-DD.md` in the appropriate month folder. Easy retrospective: read the last 30 briefs and ask "what patterns?"

---

## Permissions Strategy

| Use case | Recommended permission |
|----------|------------------------|
| Agent uploads to shared team folder | Service account with Editor on that folder only |
| Agent uploads to your personal Drive | OAuth, limited scope `drive.file` (only files agent creates) |
| Agent reads existing files | OAuth or service account with Viewer |
| Agent organizes files (move, rename) | Editor permission on parent folders |

⚠️ **Avoid using broad `drive` scope.** Use `drive.file` (only files the app creates) when possible. Smaller scope = smaller blast radius if credentials leak.

---

## Security Best Practices

1. **Service account JSON file is a secret.** Treat like a private key. Store in env var path or secret manager (Google Secret Manager, AWS Secrets Manager, 1Password CLI).

2. **Never share service account credentials.** Each agent / environment should have its own service account.

3. **Limit folder scope.** Share only specific folders with the service account, not the entire Drive.

4. **Rotate credentials every 90 days** or immediately on suspected leak.

5. **Audit Drive activity logs** for unexpected uploads or access. (Drive → Settings → Activity)

6. **Use Drive shared drives** instead of personal Drive when working with sensitive team data — easier auditing, better permission control.

7. **Consider data retention.** Set up auto-deletion for test artifacts older than X days if data is sensitive.

---

## File Naming Conventions

Choose a convention and stick to it:

| Pattern | Example | Pros |
|---------|---------|------|
| `YYYY-MM-DD_type_description.ext` | `2026-05-22_regression_q3-release.md` | Sortable, searchable |
| `type_YYYY-MM-DD_NNN.ext` | `bug_2026-05-22_014.md` | Groups by type first |
| `release-vX_type.ext` | `release-v1.2.3_test-plan.md` | Groups by release |

Avoid spaces, special chars, and timezone-ambiguous timestamps (always use ISO 8601 + UTC or explicit timezone).

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| `403 Forbidden` | Service account lacks folder permission | Share folder with service account email |
| `404 Not Found` | Folder ID wrong or folder trashed | Verify folder ID; check Drive trash |
| `quota exceeded` | Daily upload limit hit | Drive default = 750 GB/day uploads; consolidate or wait 24h |
| File uploaded but invisible | Service account uploaded to its own implicit Drive, not your shared folder | Always specify `parents` field with target folder ID |
| Auth fails after working before | Token expired (OAuth) or key rotated | Re-authenticate or rotate service account key |

---

## What This Connector Doesn't Do

This is a **setup guide** — not a turnkey integration. You still need to:
- Define the file format and content your agent generates
- Decide folder structure that makes sense for your team
- Handle errors, retries, and rate limits in your agent code
- Test in a non-prod folder before automating to shared folders

---

## Combining With Other Connectors

A common 3-step pattern:

1. **Generate** — Claude/agent produces a test report (using `05-skill-regression-tracker.md`)
2. **Archive** — Upload to Drive (this connector)
3. **Announce** — Post link to Slack (using `07-connector-slack.md`)

Stitch with any automation platform — n8n, Zapier, Apps Script, custom Python.

---

## Related

- `07-connector-slack.md` — Pair Drive uploads with Slack notifications
- `01-agent-system-prompt.md` — The agent that generates the content you'll be archiving
