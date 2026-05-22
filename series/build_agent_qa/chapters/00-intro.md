# Chapter 0: Membangun Agent QA — Apa yang Anda Butuhkan

Pada satu titik di pekerjaan QA, Anda akan menyadari hal berikut: 80% dari waktu Anda habis untuk hal yang **berulang dan terstruktur** — baca PRD dan cari ambiguity, susun test case dari user story, audit hasil regression, copy-paste data ke template UAT report, kejar status bug ticket di Slack. Sisanya 20% untuk hal yang benar-benar butuh judgment manusia — verifikasi acceptance criteria yang kompleks, demo ke stakeholder, triage incident.

Series ini tentang **menggeser 80% itu ke AI Agent yang Anda bangun sendiri**, supaya energi Anda bisa fokus ke 20% sisanya. Bukan AI yang ngobrol di tab browser, tapi AI yang **punya akses ke Notion Bugs DB Anda, ke Slack workspace Anda, ke Google Drive UAT report Anda** — dan tahu konvensi tim Anda karena Anda yang mengajarkannya.

Sebelum kita masuk ke kode, mari pastikan tiga hal: kenapa **Claude** (bukan ChatGPT atau Gemini), apa saja **tools** yang wajib Anda siapkan, dan apa **requirement** yang harus Anda penuhi sebelum hari pertama coding.

## Kenapa AI Agent, Bukan Sekadar Chatbot?

Mari mulai dengan membedakan dua hal yang sering dianggap sama.

**ChatGPT, Claude.ai, Gemini di web** — semuanya **chatbot**. Anda mengetik, AI menjawab. Selesai. AI tidak ingat percakapan dari sesi lain (kecuali Anda paste ulang konteks), tidak bisa buka Notion Anda, tidak tahu nama project Anda, dan tidak bisa mengeksekusi perintah di mesin Anda.

**Agent** adalah AI yang sama, tapi **dilengkapi tiga hal tambahan**:

1. **Tools** — kemampuan menjalankan aksi nyata: baca/tulis file, panggil API, query database, navigasi web, eksekusi shell command.
2. **Memory / Context** — pengetahuan persisten tentang Anda, project, konvensi tim, dan keputusan sebelumnya.
3. **Goal-oriented loop** — kemampuan memecah satu instruksi besar jadi langkah-langkah, lalu mengeksekusinya satu per satu sambil verifikasi.

Untuk QA, perbedaan ini bukan teknis — ini **operasional**. ChatGPT bisa membantu Anda menulis 1 test case kalau Anda jelaskan konteksnya panjang lebar. Agent QA bisa **membaca PRD baru di Notion, mengeluarkan 30 scenarios, menulis test cases di kategori positive/negative/edge/data, dan file ticket draftnya ke Notion** — semua dalam satu instruksi.

## Bagian 1: Kenapa Claude (Bukan ChatGPT atau Gemini)

Saya bukan fans-boy. Tiga model frontier (Claude, GPT, Gemini) bagus dalam pekerjaan teks. Tetapi untuk **membangun agent yang akan kerja berhari-hari, multi-step, dan butuh akses ke sistem Anda**, Claude punya tiga keunggulan yang nyata:

### 1. Skills system (modular knowledge)

Claude punya konsep **"Skills"** — bundle pengetahuan yang bisa di-load on demand berdasarkan trigger phrase. Anda bisa menulis sebuah `SKILL.md` yang isinya:

```
---
name: agent-qa
description: 'Specialist agent QA. INVOKE saat user sebut "test case",
"regression", "UAT", "bug report"...'
---

# Agent: QA Thomas

You are QA Thomas — the quality gate...
[isi skill: 5 sub-flow, severity rubric, templates]
```

Saat user mengetik `"buatkan test case untuk fitur login"`, Claude otomatis me-load skill `agent-qa` dan sekarang punya konteks lengkap soal cara tim Anda kerja — tanpa Anda perlu paste ulang konvensi tiap percakapan. Ini berbeda dengan sekadar "system prompt panjang" — skills bisa berlapis (global skills + per-role skills) dan load hanya saat relevan, jadi context window tidak boros.

### 2. MCP (Model Context Protocol) — protokol terbuka untuk extend tools

MCP adalah **standar terbuka** yang dibuat Anthropic untuk menyambungkan AI ke tools eksternal. Bukan proprietary. Anda bisa:

- Pakai **MCP server bawaan** (filesystem, web fetch, git, dll)
- Bangun **MCP server custom** dengan TypeScript/Python (mis. Cloudflare Workers) yang expose Notion, Slack, internal API, atau workbook Google Sheets ke Claude
- Plug-and-play di Claude Code dengan satu command:
  ```
  claude mcp add --transport http my-server "https://your-mcp.workers.dev/mcp"
  ```

Untuk QA, Anda bisa bangun MCP server yang expose tools spesifik: `eligibility_check`, `read_workbook`, `fetch_jarvis_result` — Claude akan otomatis tahu kapan memakainya berdasarkan deskripsi tool.

### 3. Claude Code — interactive CLI dan IDE-aware agent

**Claude Code** adalah aplikasi CLI/IDE extension resmi Anthropic untuk agentic engineering. Ini bukan sekadar editor dengan AI completion — ini agent yang bisa:

- Baca seluruh workspace project Anda
- Menjalankan terminal command (dengan permission)
- Edit file di banyak tempat sekaligus dalam satu task
- Pakai MCP tools yang Anda daftarkan
- Load skills yang Anda tulis

Gemini punya CLI mereka (Gemini CLI), GPT punya Cursor/Aider ecosystem. Tapi untuk QA agent yang harus pegang **5 sub-flow + connector ke banyak sistem + automation Playwright**, Claude Code punya integration paling mature per awal 2026.

> **Catatan jujur**: Anda boleh saja pakai Gemini atau GPT dengan adaptasi. Konsep di series ini (Skills, MCP, connectors) bisa diterjemahkan. Tapi semua contoh dan command yang saya tunjukkan akan pakai Claude — biar konkret, bukan teoretis.

## Bagian 2: Tools yang Wajib

Sebelum hari pertama membangun Agent QA, lima tools ini harus terpasang dan teruji bisa Anda jalankan:

### 1. Claude Code (atau Claude API SDK)

**Untuk kebanyakan orang**: install Claude Code via terminal. Ini akan jadi interface utama Anda dengan agent.

```bash
# Install (cek panduan resmi terbaru di docs Anthropic untuk command tepat)
npm install -g @anthropic-ai/claude-code

# Konfigurasi API key
claude auth login
```

**Untuk yang membangun integrasi sendiri**: pakai SDK Anthropic langsung dari Python/Node — relevan kalau Anda mau embed agent di pipeline CI/CD.

### 2. MCP Server Setup

Minimal Anda butuh satu MCP server custom untuk QA Anda — yang menghubungkan ke sistem internal tim:

- **Notion** (untuk Bugs DB, Tasks DB, PRD)
- **Slack** (untuk channel `#incidents`, `#qa`, escalation)
- **Google Drive / Google Sheets** (UAT reports, test artifacts, workbook)

Cara mudah: pakai **Cloudflare Workers** — gratis untuk traffic kecil, deploy dalam 5 menit, MCP SDK TypeScript sudah jadi.

```bash
# Skeleton minimal
npm create cloudflare@latest my-qa-mcp
cd my-qa-mcp
# Tambah @modelcontextprotocol/sdk
# Implement satu tool, contoh: notion_create_bug(title, severity, ...)
wrangler deploy
```

Setelah deploy, register ke Claude Code:

```bash
claude mcp add --transport http my-qa "https://my-qa-mcp.workers.dev/mcp"
```

### 3. Connectors Layer (Python / TypeScript)

Connector adalah **wrapper code** untuk API eksternal yang dipanggil oleh tools MCP Anda. Untuk QA, minimum yang akan Anda butuhkan:

| Connector | Fungsi | API yang dipanggil |
|---|---|---|
| Notion | Create bug, create task, add comment | `api.notion.com/v1/pages` |
| Slack | Post message, DM Tech Lead, thread reply | `slack.com/api/chat.postMessage` |
| Google Drive | Upload screenshot/video evidence, baca UAT template | Drive API v3 |
| API/DB internal | Setup/teardown test data, verifikasi state | Aplikasi spesifik tim |

Susun ini di folder `shared/connectors/` — agent role lain (PM, Marketing) juga bisa reuse.

### 4. Skills Bundle

Folder berisi instruksi spesifik agent QA dalam format Anthropic Skills:

```
QA/skill/
├── SKILL.md                              ← entry point, system prompt
├── references/
│   ├── sub-requirement-analysis.md
│   ├── sub-test-design.md
│   ├── sub-test-execution.md
│   ├── sub-reporting-documentation.md
│   ├── sub-stakeholder-engagement.md
│   ├── test-case-template.md
│   ├── bug-template.md
│   └── uat-report-template.md
└── scripts/
    └── qa_report_bug.py                  ← bug routing helper
```

Inilah "otak" agent QA Anda. Akan kita bedah pembuatannya di chapter berikutnya.

### 5. IDE / Editor

Claude Code bisa berjalan standalone di terminal, tapi sebagian besar workflow lebih nyaman dengan integrasi IDE:

- **VS Code** dengan ekstensi Claude Code (paling matang per awal 2026)
- **JetBrains IDE** (PyCharm, IntelliJ, WebStorm) — ekstensi tersedia
- **Terminal-only** (Vim/Neovim, plain terminal) — pakai CLI Claude Code

Pilih yang paling Anda kenal. Yang penting Anda bisa cepat scroll workspace, lihat diff, dan run shell command.

## Bagian 3: Requirement Sebelum Mulai Membangun

Ini bagian yang sering dilupakan orang yang excited "ayo bikin AI agent". Tanpa requirement berikut, agent Anda akan jadi mainan demo yang tidak dipakai serius oleh siapapun di tim.

### Requirement #1: Knowledge yang Sudah Tertulis

Agent QA Anda hanya akan sebagus **dokumentasi sub-flow QA yang Anda tulis untuknya**. Sebelum koding apapun, pastikan Anda sudah punya jawaban tulisan untuk lima pertanyaan:

1. **Requirement Analysis** — checklist apa yang dipakai tim Anda saat review PRD?
2. **Test Design** — template test case Anda seperti apa? Apa 4 kategori (positive/negative/edge/data) sudah punya contoh konkret?
3. **Test Execution** — urutan eksekusi (smoke → functional → exploratory → regression)? Tools-nya apa?
4. **Reporting & Documentation** — format UAT report, release notes, test execution report tim Anda?
5. **Stakeholder Engagement** — siapa yang harus di-tag kapan? Channel Slack mana untuk apa?

Kalau ada satu yang masih kabur, **tulis dulu** sebelum bikin agent. Agent tidak bisa "menebak" konvensi tim Anda — Anda harus tulis eksplisit. Saya bahas detail kelima sub-flow ini di series _Journey QA Thomas_ — bisa Anda jadikan template.

### Requirement #2: Source Material & Templates

Punya, dalam format file `.md` atau `.csv`:

- ✅ Severity rubric (P0/P1/P2/P3) dengan contoh kasus tim Anda
- ✅ Bug ticket template (field wajib: title, repro, expected, actual, environment, severity)
- ✅ Test case template (TC ID, kategori, pre-condition, steps, expected, linked story)
- ✅ UAT report template (executive summary, pass/fail by story, sign-off section)
- ✅ Test strategy template (scope, approach, environment, entry/exit, **estimasi waktu**)
- ✅ Release notes template

Kalau template-nya selama ini ada di kepala lead QA, **tulis dulu**. Agent akan refer ke file ini, bukan ke ingatan Anda.

### Requirement #3: External Access (Credentials & Permissions)

Agent Anda akan kerja atas nama Anda di sistem eksternal. Siapkan:

| Akses | Untuk | Cara dapat |
|---|---|---|
| **Notion API token** | Create/update bugs & tasks | Settings → Connections → Develop or manage integrations |
| **Notion DB IDs** | Pointer ke Bugs DB, Tasks DB, PRD page | Klik kanan database → Copy link → ekstrak ID dari URL |
| **Slack Bot token** | Post ke channel & DM | api.slack.com/apps → Create app → OAuth scopes |
| **Slack channel IDs** | Pointer ke `#incidents`, `#qa`, dst | Channel name → Right-click → Copy link |
| **Google Service Account** | Drive upload + Sheets read | console.cloud.google.com → IAM → Service Account → JSON key |
| **Sheet/Drive sharing** | Service account email perlu di-share ke Drive folder & sheets | "Share" tombol di Drive |
| **Anthropic API key** | Untuk Claude API/Claude Code | console.anthropic.com → API Keys |

⚠️ **Simpan semua credentials di `.env` yang `.gitignore`-d**. Jangan commit. Jangan paste di chat dengan AI yang bukan local.

### Requirement #4: Workspace yang Terstruktur

Buat folder workspace dengan layout yang predictable — agent perlu tahu di mana melihat apa:

```
your-workspace/
├── QA/
│   ├── skill/                  ← skills bundle (otak agent)
│   ├── automation-playwright/  ← automation framework
│   └── README.md               ← entry point khusus QA
├── shared/
│   ├── connectors/             ← Notion, Slack, Drive wrapper
│   └── .secrets/               ← .gitignored credentials
├── .claude/                    ← konfigurasi Claude Code per project
└── README.md                   ← entry point workspace
```

Setup ini juga membuat **kolaborasi dengan tim lebih mudah** — onboarding QA baru cukup `git clone`, install dependencies, isi `.env`, dan agent siap dipakai.

### Requirement #5: Waktu & Iterasi

Jujur saja: **bukan 1 hari kerjaan**. Realistic timeline untuk agent QA yang berguna:

- **Day 1-2**: Setup tools (Claude Code + IDE + Cloudflare Worker MCP skeleton)
- **Day 3-5**: Tulis skills bundle (SKILL.md + 5 sub-flow references + templates)
- **Day 6-7**: Implement connectors (Notion + Slack minimum)
- **Week 2**: Test dengan 1-2 user story nyata, iterate
- **Week 3+**: Tambah tools sesuai pain point (workbook reader, dashboard fetcher, dll)

Jangan harap perfect dari awal. **Build minimum useful agent dulu** (bisa create bug ticket dari instruksi natural language), pakai 2 minggu, baru tambah feature berikutnya berdasarkan apa yang ternyata Anda butuhkan tiap hari.

## Apa yang Akan Series Ini Bahas

Sembilan chapter berikutnya membongkar setiap tahapan:

| Chapter | Topik |
|---|---|
| 1 | Setup Claude Code + IDE — workspace pertama Anda |
| 2 | Menulis SKILL.md — anatomi system prompt yang dapat di-trigger |
| 3 | Membangun references — bedah 5 sub-flow ke file-file Markdown |
| 4 | MCP server custom — Cloudflare Workers + first tool |
| 5 | Connector layer — Notion + Slack + Drive |
| 6 | Handoff antar role — convention untuk multi-agent workspace |
| 7 | Testing agent Anda — bagaimana memastikan agent tidak halusinasi |
| 8 | Deployment & sharing — agent tim, bukan agent pribadi |
| 9 | Maintenance & iterasi — workflow update agent saat tim berkembang |

Tiap chapter akan punya **kode konkret** (TypeScript / Python / Markdown skill files), bukan hanya teori.

## Rangkuman

- **Agent QA bukan chatbot di tab browser.** Agent punya tools, memory, dan goal-oriented loop yang membuatnya bisa kerja multi-step di sistem nyata Anda.
- **Claude dipilih** karena Skills system (modular knowledge), MCP (open protocol untuk extend tools), dan Claude Code (agent CLI/IDE matang). Konsep bisa diterjemahkan ke Gemini/GPT, tapi contoh di series ini pakai Claude.
- **5 tools wajib**: Claude Code, MCP server custom (Cloudflare Workers paling cepat), connectors layer, skills bundle, IDE pilihan.
- **5 requirement sebelum mulai**: knowledge tertulis, source material/templates, external access credentials, workspace terstruktur, waktu realistis 2-3 minggu untuk versi pertama yang berguna.

## Checklist Actionable

Sebelum lanjut ke Chapter 1, pastikan Anda sudah:

- [ ] Punya akun Anthropic dengan API key (atau Claude Code terinstall + login)
- [ ] Pilih IDE/editor (VS Code paling direkomendasikan)
- [ ] Punya akses admin/owner ke Notion workspace tim Anda
- [ ] Punya akses Slack workspace (minimum bisa create bot app)
- [ ] Punya Google account untuk Cloud Console + Service Account
- [ ] Sudah menulis (atau punya akses ke) dokumen 5 sub-flow QA tim Anda
- [ ] Sudah punya draft severity rubric P0-P3 yang disepakati tim
- [ ] Bisa menjelaskan dalam 2 menit ke teman: "kenapa agent QA, kenapa Claude, apa bedanya dengan ChatGPT"

Kalau semua ☑, masuk Chapter 1 — kita setup Claude Code + workspace pertama Anda.
