# Chapter 0: Selamat Datang — Apa Itu QA?

Saya pernah ketemu seorang programmer yang bilang, _"QA itu yang klik-klik tombol kan? Kerjanya nyari tombol mana yang error?"_

Kalau Anda mengangguk membaca kalimat itu, selamat — Anda baru saja menemukan alasan kenapa buku ini dibuat. Karena selama Anda masih menganggap QA sebagai _"tester yang klik-klik tombol"_, Anda akan terus melepas bug ke production, terus tertekan tiap mau release, dan terus merasa tim engineering Anda lambat padahal masalahnya bukan di sana.

QA bukan pekerjaan klik-klik. QA adalah **quality gate** — gerbang yang menentukan apakah sebuah fitur layak sampai ke tangan user atau tidak. Buku ini menulis ulang pekerjaan itu dari nol, dengan satu prinsip pegangan yang sederhana tapi sering dilupakan.

## Kenapa Bug yang Lolos ke Production Itu Mahal

Sebelum kita bicara teknis, mari sepakati dulu kenapa peran ini penting. Industri sudah lama punya angka klasik soal biaya bug:

| Bug ditemukan di tahap | Biaya relatif untuk diperbaiki |
|---|---|
| Requirement / desain | 1x |
| Coding | 5x |
| Testing | 10x |
| **Production** | **30-100x** |

Angkanya bisa diperdebatkan, tapi intinya: **semakin telat sebuah bug ditemukan, semakin mahal biaya memperbaikinya**. Bukan cuma biaya engineering — termasuk juga reputasi, churn user, dan jam tidur tim oncall jam 3 pagi.

Pekerjaan QA pada dasarnya adalah **menggeser deteksi bug sejauh mungkin ke kiri** (shift-left). Jangan ketemu bug di production, ketemu di staging. Jangan ketemu di staging, ketemu di code review. Jangan ketemu di code review, ketemu di PRD. Buku ini akan mengajari Anda satu-satu cara melakukan itu.

## Prime Directive — Mantra yang Harus Anda Hafal

Sebelum lanjut, hafalkan kalimat ini:

> **"Komunikasi untuk mengecek apakah flow sudah sesuai dengan criteria user story."**

Itu prime directive seorang QA. Sederhana, tapi konsekuensinya besar:

- Kalau code berjalan tapi **menyimpang dari acceptance criteria** → tetap bug. File bug-nya.
- Kalau implementasi "secara teknis benar" tapi **user story bilang lain** → tetap bug. File bug-nya.
- Kalau "tidak ada error di console" tapi **expected behavior tidak terjadi** → tetap bug. File bug-nya.

QA bukan menilai apakah code-nya benar. **QA menilai apakah code-nya menjawab kebutuhan yang ditulis di user story.** Dua hal yang berbeda. Pegang ini erat-erat.

## Anatomi Pekerjaan: 5 Sub-Flow QA

Pekerjaan QA bukan satu aktivitas, tapi lima aktivitas yang saling berurutan. Kita akan bedah satu per satu di chapter berikutnya.

```
┌─────────────────────────┐
│ 1. Requirement Analysis │  Baca PRD, pecah user story jadi scenarios
└─────────────┬───────────┘
              ▼
┌─────────────────────────┐
│ 2. Test Design          │  Strategi + estimasi + 4 kategori test case
└─────────────┬───────────┘
              ▼
┌─────────────────────────┐
│ 3. Test Execution       │  Smoke → Functional → Exploratory → Regression
└─────────────┬───────────┘
              ▼
┌─────────────────────────┐
│ 4. Reporting & Docs     │  UAT Report + Release Notes + Test Documentation
└─────────────┬───────────┘
              ▼
┌─────────────────────────┐
│ 5. Stakeholder Engage   │  Demo, meeting, UAT coordination
└─────────────────────────┘
```

Sub-flow ini bukan teori. Ini urutan kerja harian seorang QA Engineer di tim modern. Kalau Anda melompati salah satu, hampir pasti akan ada bug yang lolos atau release yang macet.

### 1. Requirement Analysis (Chapter 1)

Pintu masuk pertama. Sebelum engineering nulis satu baris kode, QA harus sudah membaca PRD dan menemukan _ambiguity_ — kalimat-kalimat seperti _"sistem menangani input invalid secara baik"_ yang tidak bisa dites. Setelah itu memecah tiap user story jadi daftar skenario (happy path, edge case, failure mode) yang akan jadi bahan test case.

### 2. Test Design (Chapter 2)

Setelah skenario disepakati, QA menulis **test strategy** (apa yang dites, bagaimana, dengan apa, kapan) dan **test case** dalam empat kategori wajib: positive, negative, edge, dan data preparation. Plus — yang sering dilupakan — **estimasi waktu**. Tanpa estimasi waktu, Anda akan terus dipaksa selesai dalam "secepatnya" yang berarti tidak akan pernah selesai.

### 3. Test Execution (Chapter 3)

Eksekusi mengikuti urutan fail-fast: smoke testing dulu (5 menit, kalau gagal langsung stop), baru functional testing per user story, lalu exploratory untuk hunting edge case, dan terakhir regression untuk memastikan tidak ada feature lain yang rusak. Tiap cycle menghasilkan **Test Execution Report**.

### 4. Reporting & Documentation (Chapter 5)

Empat jenis dokumen yang jadi tanggung jawab QA: **UAT Report** untuk stakeholder, **Release Notes** untuk user, **Test Documentation** untuk knowledge base internal, dan **Test Execution Report** per cycle. Dokumen-dokumen ini yang membuat pekerjaan QA bisa diaudit dan diwariskan ke tim berikutnya.

### 5. Stakeholder Engagement (Chapter 6)

QA tidak kerja sendirian. Ada demo ke stakeholder, ada meeting standup-sprint planning-retro, ada koordinasi UAT dengan user beneran. Bagian ini sering disepelekan — padahal QA yang tidak hadir di sprint planning akan terus dapat scope yang tidak realistis.

## Severity Rubric — Bahasa Bersama Tim

Salah satu kontribusi paling berharga seorang QA adalah _bahasa bersama_ untuk membicarakan tingkat keparahan bug. Kita pakai 4 level:

| Level | Definisi | Contoh |
|---|---|---|
| **P0** | Production down, data loss, security breach | Login total tidak bisa, payment gagal semua user |
| **P1** | Core feature rusak, tidak ada workaround | Search return 500, signup intermittent |
| **P2** | Feature impaired tapi ada workaround | Urutan sort salah, typo di UI |
| **P3** | Cosmetic, minor inconvenience | Pixel misalign, edge timing |

Severity ini menentukan **routing eskalasi**:
- P0/P1 → file di Notion Bugs DB + post ke channel `#incidents` Slack + DM ke Tech Lead langsung.
- P2 → file di Notion + post ke `#qa`.
- P3 → file di Notion saja, akan muncul di backlog review berikutnya.

Detail dan template lengkap dibahas di Chapter 4.

## Mindset yang Membedakan QA Biasa dengan QA Hebat

Sebelum kita masuk ke teknis, saya mau Anda menyerap empat mindset ini lebih dulu. Tanpa ini, semua teknik di chapter berikutnya hanya akan jadi checklist mati.

**1. Adversarial, bukan defensive.** QA yang baik berpikir _"bagaimana saya membuat fitur ini gagal?"_ bukan _"bagaimana saya membuktikan fitur ini jalan?"_. Anggap diri Anda lawan dari fitur tersebut.

**2. Trace ke user story, selalu.** Setiap test case yang Anda tulis harus bisa Anda kaitkan ke user story tertentu. Kalau tidak bisa, Anda sedang tes hal yang salah.

**3. File bug sambil jalan, jangan di-batch.** Anti-pattern paling umum: QA menumpuk semua bug di akhir cycle lalu dump 30 ticket sekaligus. Itu menyebalkan untuk semua orang. File begitu Anda menemukan, satu per satu.

**4. Anda adalah gerbang, bukan tukang stempel.** Kalau acceptance criteria tidak terpenuhi, jangan approve walaupun ditekan _"sudah deadline"_. Tugas Anda menjaga gerbang. Stempel kosong tidak punya nilai.

## Apa yang Akan Anda Pelajari di Buku Ini

Sembilan chapter berikutnya akan mengisi tiap sub-flow di atas dengan detail praktis:

- **Chapter 1**: Review PRD step-by-step + decomposing user story jadi scenarios.
- **Chapter 2**: Template Test Strategy, estimasi waktu, 4 kategori test case dengan contoh kode.
- **Chapter 3**: Urutan eksekusi yang benar + format Test Execution Report.
- **Chapter 4**: Bug Reporting — anatomi bug ticket yang baik + flow eskalasi.
- **Chapter 5**: Empat dokumen QA + konvensi distribusinya.
- **Chapter 6**: Demo yang tidak meledak, meeting yang efektif, UAT yang terkoordinasi.
- **Chapter 7**: Automation Testing dengan Playwright — setup, Page Object Model, contoh nyata.
- **Chapter 8**: Tooling lengkap — Notion, Slack, Drive, dan workflow handoff antar role.
- **Chapter 9**: Penutup + 10-pertanyaan self-assessment + next step untuk 7 hari pertama.

Tiap chapter punya **rangkuman** dan **checklist actionable** di akhir. Jangan dilewati.

## Rangkuman

- **QA bukan klik-klik tombol.** QA adalah quality gate yang memastikan flow sesuai dengan acceptance criteria user story.
- **Prime directive**: _"Komunikasi untuk mengecek apakah flow sudah sesuai dengan criteria user story."_ Kalau menyimpang dari criteria, walaupun code-nya jalan, itu bug.
- **Bug ditemukan lebih awal jauh lebih murah.** Tugas QA adalah men-shift-left deteksi bug — idealnya sampai ke tahap review PRD.
- **5 sub-flow** yang berurutan: Requirement Analysis → Test Design → Test Execution → Reporting & Documentation → Stakeholder Engagement.
- **Severity P0-P3** menentukan urgensi dan routing eskalasi bug.
- Empat mindset penentu: adversarial, trace-to-story, file-as-you-find, gate-not-stamp.

## Checklist Actionable

Sebelum lanjut ke Chapter 1, pastikan Anda:

- [ ] Menghafal prime directive di luar kepala.
- [ ] Bisa menyebut 5 sub-flow QA tanpa lihat catatan.
- [ ] Bisa membedakan P0, P1, P2, P3 dengan contoh kasus.
- [ ] Setuju bahwa "code jalan tapi menyimpang dari acceptance criteria" = bug.
- [ ] Mengidentifikasi minimal 1 fitur di project Anda saat ini yang akan Anda jadikan "studi kasus" sambil membaca buku ini.
- [ ] Punya akses ke PRD, Notion (atau task tracker lain), Slack workspace tim Anda.
- [ ] Siap "shift-left" — datang ke meeting PRD review berikutnya, bukan menunggu fitur jadi.

Kalau semua check terisi, kita siap masuk ke quality gate pertama: **membaca PRD dengan mata QA**. Lanjut ke Chapter 1.
