# Chapter 05: Reporting & Documentation — UAT, Release Notes, Knowledge Base

Selamat datang kembali dalam perjalanan Anda sebagai Quality Assurance Engineer! Jika di bab-bab sebelumnya kita sudah membahas bagaimana cara menganalisis *requirement*, merancang strategi pengujian, hingga melaksanakan eksekusi pengujian, kini saatnya kita berbicara tentang bagaimana semua kerja keras itu dikomunikasikan.

Sebagai seorang QA Engineer, tugas Anda tidak berhenti pada menemukan *bug* atau memastikan fitur bekerja. Bagian krusial lainnya adalah mendokumentasikan dan melaporkan temuan serta status kualitas produk kepada berbagai pihak yang berkepentingan. Bayangkan Anda telah menemukan *bug* kritis atau memastikan sebuah fitur siap dirilis, tetapi informasi ini tidak sampai ke telinga yang tepat. Tentu saja, itu akan menjadi sia-sia, bukan?

Bab ini akan memandu Anda melalui empat jenis dokumen utama yang akan Anda hasilkan sebagai QA Engineer, serta bagaimana cara mendistribusikannya secara efektif. Kita akan membahas Laporan UAT (User Acceptance Testing) yang krusial untuk persetujuan *stakeholder*, Catatan Rilis (Release Notes) yang berhadapan langsung dengan pengguna, Dokumentasi Pengujian sebagai basis pengetahuan jangka panjang, dan Laporan Eksekusi Pengujian yang menjadi catatan harian Anda. Mari kita mulai!

## Mengapa Dokumentasi Penting dalam Peran QA?

Sebelum kita menyelami jenis-jenis dokumen, mari kita pahami mengapa aspek pelaporan dan dokumentasi ini sangat vital:

1.  **Transparansi dan Akuntabilitas:** Dokumentasi memberikan gambaran jelas tentang apa yang telah diuji, bagaimana hasilnya, dan apa saja risiko yang mungkin ada. Ini membangun kepercayaan dan akuntabilitas.
2.  **Pengambilan Keputusan:** Laporan yang baik membantu *stakeholder* (Product Manager, Tech Lead, bahkan jajaran direksi) membuat keputusan yang tepat, misalnya apakah sebuah fitur sudah siap dirilis, atau apakah ada *bug* yang harus segera diperbaiki.
3.  **Basis Pengetahuan Jangka Panjang:** Dokumentasi pengujian berfungsi sebagai *knowledge base* yang dapat dirujuk di masa depan. Ini sangat berharga untuk *onboarding* anggota tim baru, *regresi*, atau untuk memahami mengapa sebuah keputusan pengujian diambil di masa lalu.
4.  **Komunikasi Efektif:** Tidak semua orang dalam tim atau perusahaan memiliki pemahaman teknis yang sama. Dokumentasi yang terstruktur membantu Anda mengkomunikasikan informasi kompleks dalam format yang mudah dicerna oleh audiens yang berbeda.
5.  **Audit dan Kepatuhan:** Dalam beberapa industri, dokumentasi pengujian adalah persyaratan wajib untuk tujuan audit dan kepatuhan regulasi.

Singkatnya, dokumentasi adalah jembatan antara aktivitas pengujian Anda dengan pengambilan keputusan bisnis. Ini adalah cara Anda memastikan bahwa kualitas tidak hanya *tercapai*, tetapi juga *terkomunikasikan* dengan baik.

## 1. Laporan UAT (User Acceptance Testing)

Laporan UAT adalah salah satu dokumen terpenting yang akan Anda hasilkan, terutama setelah fase UAT selesai. Tujuan utamanya adalah untuk memberikan gambaran komprehensif kepada *stakeholder* tentang status fitur atau produk dari sudut pandang pengguna akhir, dan yang terpenting, mendapatkan persetujuan resmi (sign-off) untuk rilis.

**Siapa yang membaca ini?**
Laporan UAT ditujukan untuk audiens tingkat tinggi: Leadership, Product Manager, Tech Lead, dan *stakeholder* bisnis lainnya yang memiliki kepentingan dalam produk.

**Struktur Laporan UAT**

Laporan UAT harus jelas, ringkas, dan fokus pada informasi yang relevan untuk pengambilan keputusan. Berikut adalah struktur yang disarankan, berdasarkan template yang sering digunakan di "Journey QA Thomas":

```markdown
# UAT Report — [Nama Fitur/Proyek] — [Tanggal]

**Doc type**: UAT Report
**Feature/Release**: [Nama Fitur atau Versi Rilis]
**Author**: qa-thomas
**Status**: Draft | Final
**Last updated**: YYYY-MM-DD
**Related**:
- PRD: [Link ke Product Requirement Document]
- Test Strategy: [Link ke Dokumen Strategi Pengujian]
- Linked Epic: [Link ke Epic di Jira/Notion]

---

## Executive Summary
<1 paragraf. Apakah kita mencapai target kualitas? Temuan penting? Rekomendasi?>

## Scope Tested
- Stories: <Daftar User Story yang diuji dengan ID/link>
- Out of scope: <Daftar hal yang tidak termasuk dalam pengujian>

## Pass/Fail by User Story

| Story ID | Story | Status | Notes |
|---|---|---|---|
| S-01 | Pengguna dapat mendaftar akun baru | ✅ Pass | |
| S-02 | Pengguna dapat masuk dengan email/password | ⚠️ Pass with notes | Ada sedikit inkonsistensi UI pada halaman login saat resolusi kecil, namun tidak menghalangi fungsi. |
| S-03 | Pengguna dapat mengubah profil | ❌ Fail | Fitur upload foto profil gagal saat ukuran file > 2MB. (Lihat Bug #BUG-005) |

## Bug Summary

| Severity | Count | Status | Tickets |
|---|---|---|---|
| P0 | 0 | — | |
| P1 | 2 | 1 fixed, 1 open | [BUG-005], [BUG-007] |
| P2 | 5 | 3 fixed, 2 deferred | [BUG-001], [BUG-002], [BUG-003], [BUG-004], [BUG-006] |
| P3 | 8 | logged for backlog | [BUG-008] - [BUG-015] |

## UAT Participants
| Name | Role | Sessions | Findings filed |
|---|---|---|---|
| Thomas | Product Manager | 3 | 2 bugs, 1 improvement |
| Sarah | Business Analyst | 2 | 1 bug |
| Budi | Marketing Lead | 1 | 0 |

## Performance Observations
- Response time: <rata-rata 300ms vs target 500ms>
- Error rate: <0.1% vs target 0.5%>
- Load test: <Tidak dilakukan untuk rilis ini>

## Accessibility Observations
- Screen reader: <Pass, semua elemen interaktif dapat diakses>
- Keyboard navigation: <Pass, semua fungsi dapat diakses via keyboard>
- Color contrast: <Ada beberapa isu pada elemen secondary, tidak blocking>

## Risks for Release
1. **Bug P1 yang masih terbuka:** [BUG-007] (Error saat mengubah email) - **Mitigasi:** Akan dirilis hotfix dalam 24 jam setelah rilis utama. Diterima oleh PM.
2. **Inkonsistensi UI kecil:** Tidak blocking, akan diperbaiki di sprint berikutnya.

## Recommendation
- [ ] Ready for release
- [x] Conditionally ready (membutuhkan perbaikan [BUG-007] sebagai *hotfix*)
- [ ] NOT ready (reason: ...)

## Sign-offs

| Role | Name | Signed | Date |
|---|---|---|---|
| QA | qa-thomas | ✅ | 2023-10-26 |
| PM | pm-thomas | ⬜ | |
| Tech Lead | tech-lead-thomas | ⬜ | |
| Business stakeholder | ... | ⬜ | |
```

**Penjelasan Bagian-bagian Penting:**

*   **Executive Summary:** Ini adalah bagian terpenting bagi *stakeholder* tingkat tinggi. Rangkum temuan kunci dan rekomendasi dalam satu paragraf yang mudah dicerna.
*   **Scope Tested:** Jelaskan dengan jelas apa saja yang diuji dan apa yang sengaja tidak diuji. Ini menghindari kesalahpahaman.
*   **Pass/Fail by User Story:** Ini memberikan detail granular tentang status setiap *user story* yang diuji selama UAT. Gunakan status visual (✅, ⚠️, ❌) untuk kejelasan.
*   **Bug Summary:** Ringkasan *bug* berdasarkan tingkat keparahan (P0-P3, seperti yang dibahas di Bab 04). Ini menunjukkan gambaran risiko yang ada.
*   **UAT Participants:** Mencatat siapa saja yang terlibat dalam UAT, berapa sesi yang mereka ikuti, dan berapa banyak temuan yang mereka laporkan. Ini menunjukkan partisipasi dan validasi.
*   **Performance & Accessibility Observations:** Meskipun bukan fokus utama UAT, observasi ini penting untuk memberikan gambaran kualitas yang lebih holistik.
*   **Risks for Release:** Identifikasi risiko yang masih ada dan bagaimana tim berencana untuk mengatasinya. Ini menunjukkan proaktivitas Anda.
*   **Recommendation:** Rekomendasi Anda sebagai QA Engineer: apakah produk siap dirilis, siap dengan syarat, atau belum siap sama sekali. Ini adalah hasil dari penilaian Anda.
*   **Sign-offs:** Bagian ini **sangat krusial**. Ini adalah tempat *stakeholder* secara resmi menyetujui atau menolak rilis berdasarkan laporan Anda. Tanda tangan (atau centang digital) dari PM, Tech Lead, dan *stakeholder* bisnis lainnya adalah bentuk komitmen. Tanpa ini, rilis bisa berisiko karena tidak ada persetujuan yang jelas.

**Penyimpanan dan Distribusi:**
Di "Journey QA Thomas", laporan ini disimpan sebagai tugas di Notion dan diekspor ke PDF untuk *stakeholder* yang mungkin lebih memilih lampiran email. Pastikan format PDF tetap rapi dan mudah dibaca.

## 2. Catatan Rilis (Release Notes)

Berbeda dengan Laporan UAT yang ditujukan untuk internal dan *stakeholder*, Catatan Rilis (Release Notes) adalah dokumen yang berhadapan langsung dengan **pengguna akhir**. Tujuannya adalah untuk menginformasikan kepada pengguna tentang perubahan, fitur baru, perbaikan, atau isu yang diketahui dalam versi produk yang baru dirilis.

**Siapa yang membaca ini?**
Pengguna akhir produk, tim Marketing (untuk kampanye), dan tim Support (untuk membantu pengguna).

**Struktur Catatan Rilis**

Catatan rilis harus ditulis dengan bahasa yang mudah dipahami oleh non-teknisi, fokus pada manfaat bagi pengguna, dan menghindari jargon teknis.

```markdown
# Release v1.2.0 — 2023-10-26

**Doc type**: Release Notes
**Feature/Release**: v1.2.0 - Peningkatan Fitur Profil
**Author**: qa-thomas
**Status**: Final
**Last updated**: 2023-10-26
**Related**:
- Linked Epic: [Link ke Epic "Peningkatan Profil Pengguna"]

---

Halo Pengguna Atmoscheck!

Kami sangat senang untuk mengumumkan pembaruan terbaru kami, v1.2.0, yang membawa peningkatan signifikan pada pengalaman profil Anda! Kami mendengarkan masukan Anda dan bekerja keras untuk membuat Atmoscheck lebih baik.

## ✨ Baru
- **Upload Foto Profil yang Lebih Mudah:** Kini Anda bisa mengunggah foto profil langsung dari perangkat Anda dengan antarmuka yang lebih intuitif. Ekspresikan diri Anda!
- **Pengaturan Notifikasi yang Lebih Detail:** Kontrol penuh ada di tangan Anda! Sesuaikan jenis notifikasi yang ingin Anda terima, mulai dari peringatan cuaca hingga pembaruan komunitas.

## 🐛 Diperbaiki
- Memperbaiki masalah di mana beberapa pengguna tidak dapat menyimpan perubahan pada nama pengguna mereka. Sekarang, semua perubahan akan tersimpan dengan benar.
- Mengatasi *bug* yang menyebabkan aplikasi *crash* saat mencoba melihat riwayat data dari tanggal tertentu. Pengalaman Anda kini lebih stabil.

## 🔧 Ditingkatkan
- Peningkatan kinerja pada halaman *dashboard*, membuat pemuatan data cuaca Anda lebih cepat dan responsif.
- Tampilan antarmuka pengguna (UI) yang lebih bersih dan modern pada bagian pengaturan, memberikan pengalaman navigasi yang lebih mulus.

## ⚠️ Isu yang Diketahui
- Saat ini, kami menemukan isu kecil di mana pratinjau foto profil mungkin terlihat sedikit terdistorsi pada beberapa perangkat Android lama. Kami sedang berupaya untuk memperbaikinya di pembaruan berikutnya. Tidak ada dampak pada kualitas foto yang diunggah.

Terima kasih atas dukungan Anda!
Tim Atmoscheck
```

**Penjelasan Bagian-bagian Penting:**

*   **Judul dan Versi:** Jelas menunjukkan versi rilis dan tanggalnya.
*   **Pengantar:** Sapa pengguna dan berikan sedikit konteks tentang pembaruan ini.
*   **✨ New (Baru):** Daftar fitur baru. Fokus pada manfaat yang akan didapatkan pengguna, bukan detail teknis implementasinya.
*   **🐛 Fixed (Diperbaiki):** Daftar *bug* yang telah diperbaiki. Lagi-lagi, jelaskan masalah dari sudut pandang pengguna, bukan ID *bug* atau *stack trace*.
*   **🔧 Improved (Ditingkatkan):** Peningkatan pada kinerja, UX, atau fitur yang sudah ada.
*   **⚠️ Known Issues (Isu yang Diketahui):** Jika ada *bug* non-kritis yang disadari tetapi belum bisa diperbaiki di rilis ini, jujur sampaikan di sini. Berikan *workaround* jika ada. Ini membangun kepercayaan dan mengurangi tiket *support*.

**Penyimpanan dan Distribusi:**
Catatan rilis disimpan di Notion (dengan label `release-notes`), di folder Drive (agar tim Marketing/Support dapat mengambilnya dengan mudah), dan diringkas kemudian diposting di saluran Slack `#announcements`. Marketing juga mungkin akan menggunakannya untuk *email blast* kepada pengguna.

## 3. Dokumentasi Pengujian Jangka Panjang (Test Documentation)

Selain laporan spesifik per rilis, ada kebutuhan untuk menjaga basis pengetahuan jangka panjang mengenai pengujian. Ini adalah *knowledge base* yang terus berkembang dan menjadi referensi utama bagi tim QA (dan kadang-kadang tim lain) untuk memahami *setup*, data, dan proses pengujian secara keseluruhan.

**Siapa yang membaca ini?**
Tim QA (utama), Developer (untuk memahami lingkungan pengujian atau *bug patterns*), dan tim *onboarding* (untuk anggota baru).

**Kategori Utama dalam Test Documentation (di Notion "QA Knowledge Base"):**

1.  **Test Environments (Lingkungan Pengujian):**
    *   **Deskripsi:** Detail tentang berbagai lingkungan pengujian yang tersedia (misalnya, `staging`, `dev`, `QA`, `pre-prod`).
    *   **Apa yang disertakan:**
        *   URL untuk setiap lingkungan.
        *   Kredensial akses (username/password atau cara mendapatkannya).
        *   Detail konfigurasi unik atau "gotchas" (misalnya, "lingkungan staging tidak memiliki integrasi pembayaran langsung, gunakan mode sandbox").
        *   Status lingkungan (misalnya, kapan terakhir di-refresh, siapa yang bertanggung jawab).
    *   **Contoh:**
        ```
        ### Lingkungan Staging
        - **URL**: `https://staging.atmoscheck.com`
        - **Akses**: Login SSO via Google. Jika tidak bisa akses, hubungi #ops-team.
        - **Data**: Refresh otomatis setiap hari Minggu pukul 03:00 WIB dari database produksi yang di-masking. Data pengguna bersifat anonim.
        - **Catatan**: Pembayaran real tidak aktif. Gunakan kartu kredit test yang disediakan Stripe.
        ```

2.  **Test Data Inventory (Inventaris Data Pengujian):**
    *   **Deskripsi:** Daftar pengguna, *fixture*, atau data spesifik yang tersedia untuk pengujian.
    *   **Apa yang disertakan:**
        *   Jenis data (misalnya, pengguna admin, pengguna premium, pengguna tanpa langganan).
        *   Kredensial atau cara mengakses data tersebut.
        *   Status data (misalnya, "pengguna admin_thomas memiliki akses ke semua fitur").
        *   Cara me-refresh atau membuat data baru.
    *   **Contoh:**
        ```
        ### Data Pengguna untuk Testing
        - **Admin User**: `admin_test@atmoscheck.com` / `password123` (akses penuh)
        - **Premium User**: `premium_test@atmoscheck.com` / `password123` (langganan aktif)
        - **Free User**: `free_test@atmoscheck.com` / `password123` (langganan dasar)
        - **Pengguna dengan Data Cuaca Spesifik**:
            - `user_jakarta@atmoscheck.com` (memiliki data historis Jakarta 5 tahun)
            - `user_bandung@atmoscheck.com` (memiliki data historis Bandung 3 tahun)
        - **Cara Membuat Data Baru**: Gunakan script `generate_test_data.sh` di repo `atmoscheck-backend/scripts`.
        ```

3.  **Automation Infrastructure (Infrastruktur Otomasi):**
    *   **Deskripsi:** Informasi tentang *framework* otomasi, cara menjalankannya, dan di mana menemukan hasilnya.
    *   **Apa yang disertakan:**
        *   *Framework* yang digunakan (misalnya, Playwright, Selenium).
        *   Perintah untuk menjalankan *test suite* (lokal atau CI/CD).
        *   Lokasi laporan pengujian (misalnya, Allure Reports, dashboard CI).
        *   Panduan tentang cara menambahkan *test case* baru.
    *   **Contoh:**
        ```
        ### Panduan Automation Testing (Playwright)
        - **Repo**: `git@github.com:atmoscheck/qa-automation.git`
        - **Setup Lokal**: `npm install && npx playwright install`
        - **Menjalankan Semua Test**: `npm test`
        - **Menjalankan Test Spesifik**: `npm test -- --project=chromium --grep "login feature"`
        - **Laporan HTML Lokal**: `npx playwright show-report` (setelah `npm test`)
        - **Laporan CI/CD**: Terintegrasi dengan Jenkins. Laporan Allure dapat diakses via [Link ke Jenkins Job].
        - **Cara Menambahkan Test Baru**: Lihat `docs/HOW_TO_ADD_TESTS.md` di repo.
        ```

4.  **Regression Checklist (Daftar Periksa Regresi):**
    *   **Deskripsi:** Daftar *test case* atau skenario kritis yang **harus selalu diuji** sebelum setiap rilis utama, terlepas dari fitur yang berubah. Ini memastikan fungsi inti tidak rusak.
    *   **Apa yang disertakan:**
        *   Daftar skenario kritis (misalnya, login, pendaftaran, melihat *dashboard* utama, melakukan pembayaran).
        *   Link ke *test case* yang relevan jika ada.
        *   Prioritas atau frekuensi pengujian.
    *   **Contoh:**
        ```
        ### Daftar Periksa Regresi Wajib (Setiap Rilis)
        1.  **Login & Logout**:
            *   [TC-001] Login sukses dengan kredensial valid.
            *   [TC-002] Logout sukses.
            *   [TC-003] Login gagal dengan kredensial tidak valid.
        2.  **Dashboard Utama**:
            *   [TC-005] Data cuaca saat ini ditampilkan dengan benar.
            *   [TC-006] Navigasi ke halaman lain berfungsi.
        3.  **Pengaturan Profil**:
            *   [TC-010] Mengubah nama pengguna berhasil.
            *   [TC-011] Mengubah foto profil berhasil.
        4.  **Pembayaran (jika ada)**:
            *   [TC-007] Proses pembayaran langganan berhasil.
        ```

5.  **Bug Patterns (Pola Bug):**
    *   **Deskripsi:** Dokumentasi tentang jenis *bug* yang sering muncul, penyebab umumnya, dan contoh tiket terkait. Ini membantu tim belajar dari kesalahan masa lalu dan mengidentifikasi *bug* lebih cepat.
    *   **Apa yang disertakan:**
        *   Kategori *bug* (misalnya, "Off-by-one errors", "Race conditions", "Cross-browser UI issues").
        *   Deskripsi singkat tentang pola tersebut.
        *   Contoh *bug report* (dengan link tiket).
        *   Saran mitigasi atau cara menguji untuk pola tersebut.
    *   **Contoh:**
        ```
        ### Pola Bug Umum Atmoscheck
        1.  **Inkonsistensi Data Historis**:
            *   **Deskripsi**: Sering terjadi ketika ada perubahan pada API data cuaca eksternal atau saat sinkronisasi data. Data yang ditampilkan tidak sesuai dengan data asli atau memiliki gap.
            *   **Contoh Tiket**: [BUG-201: Data historis Jakarta hilang untuk 2022], [BUG-205: Perbedaan suhu historis antara staging dan prod]
            *   **Tips Uji**: Selalu verifikasi data historis dari sumber yang terpercaya setelah setiap perubahan pada integrasi API data.
        2.  **UI/UX Browser-Specific**:
            *   **Deskripsi**: Tampilan atau interaksi UI yang berbeda/rusak pada browser tertentu (terutama Safari dan Firefox) dibandingkan Chrome.
            *   **Contoh Tiket**: [BUG-310: Tombol "Lihat Detail" tidak rata di Safari], [BUG-315: Modal notifikasi terpotong di Firefox]
            *   **Tips Uji**: Selalu lakukan pengujian visual cepat di setidaknya 3 browser utama.
        ```

**Pemeliharaan:**
Dokumentasi ini harus menjadi *living document*. Di "Journey QA Thomas", disarankan untuk mengalokasikan "documentation hour" setiap bulan untuk meninjau dan memperbarui *knowledge base* ini. Ini memastikan informasi tetap relevan dan akurat.

## 4. Laporan Eksekusi Pengujian (Test Execution Report)

Laporan Eksekusi Pengujian adalah dokumen yang dihasilkan setelah setiap siklus pengujian selesai. Ini adalah catatan harian atau mingguan dari aktivitas pengujian Anda. Meskipun sudah dibahas secara detail di Bab 03, penting untuk memahami perannya dalam konteks pelaporan dan dokumentasi secara keseluruhan.

**Siapa yang membaca ini?**
Product Manager dan Tech Lead, untuk mendapatkan *update* harian atau mingguan tentang progres pengujian.

**Fungsi Utama:**

*   **Progress Tracking:** Menunjukkan berapa banyak *test case* yang telah dieksekusi, berapa yang lulus, gagal, atau diblokir.
*   **Identifikasi Masalah:** Menyoroti *bug* yang ditemukan selama siklus pengujian tersebut.
*   **Input untuk Laporan UAT:** Untuk rilis besar, beberapa laporan eksekusi pengujian dapat diagregasikan menjadi ringkasan pengujian tingkat rilis yang kemudian dimasukkan ke dalam Laporan UAT.

**Penyimpanan dan Distribusi:**
Setiap laporan eksekusi pengujian biasanya diajukan sebagai tugas di Notion dan ringkasannya diposting di saluran Slack `#qa` setiap hari atau pada akhir siklus pengujian. Ini memastikan tim inti selalu mendapatkan informasi terbaru.

## Konvensi Header Dokumen QA

Untuk menjaga konsistensi dan memudahkan pencarian informasi, semua dokumen yang dihasilkan oleh tim QA Thomas menggunakan konvensi header yang seragam. Ini membantu pembaca segera memahami konteks dokumen.

```markdown
**Doc type**: <UAT Report | Release Notes | Test Doc | Test Execution Report>
**Feature/Release**: <nama fitur atau versi rilis>
**Author**: qa-thomas
**Status**: Draft | Final | Archived
**Last updated**: YYYY-MM-DD
**Related**:
- PRD: <link ke Product Requirement Document>
- Test Strategy: <link ke Dokumen Strategi Pengujian>
- Linked Epic: <link ke Epic di Jira/Notion>
```

**Penjelasan Field Header:**

*   **Doc type:** Mengidentifikasi jenis dokumen (misalnya, "UAT Report", "Release Notes"). Ini membantu dalam kategorisasi dan pencarian.
*   **Feature/Release:** Nama fitur atau nomor versi rilis yang menjadi fokus dokumen.
*   **Author:** Nama penulis dokumen (misalnya, `qa-thomas`).
*   **Status:** Status terkini dokumen (misalnya, `Draft`, `Final`, `Archived`).
*   **Last updated:** Tanggal terakhir dokumen diperbarui.
*   **Related:** Bagian ini sangat penting untuk keterlacakan (traceability). Ini menyediakan tautan ke dokumen atau entitas terkait lainnya, seperti:
    *   **PRD (Product Requirement Document):** Dokumen yang menjelaskan persyaratan produk.
    *   **Test Strategy:** Dokumen yang menjelaskan strategi pengujian secara keseluruhan.
    *   **Linked Epic:** Tautan ke *epic* di *project management tool* (misalnya, Notion, Jira) yang terkait dengan fitur atau rilis ini.

Menerapkan konvensi header ini memastikan bahwa setiap dokumen memiliki identitas yang jelas dan mudah dihubungkan dengan konteks proyek yang lebih luas.

## Distribusi Dokumen: Siapa Membaca Apa?

Membuat dokumen yang hebat tidak cukup; Anda juga harus memastikan bahwa dokumen tersebut sampai ke audiens yang tepat melalui saluran yang sesuai. Berikut adalah panduan distribusi dokumen di "Journey QA Thomas":

| Dokumen                      | Audiens                                   | Saluran                                         | Mengapa?                                                                                                                                                                                                                                                                                       |
| :--------------------------- | :---------------------------------------- | :---------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Laporan UAT**              | Leadership, PM, Tech Lead, Stakeholder Bisnis | Notion + PDF (lampiran email)                   | *Stakeholder* membutuhkan ringkasan komprehensif untuk pengambilan keputusan rilis. Notion sebagai *source of truth* internal, PDF untuk formalitas dan kemudahan distribusi ke pihak eksternal atau yang prefer email.                                                                       |
| **Catatan Rilis**            | Pengguna, Marketing, Support              | Notion + Slack `#announcements` + Email Blast (oleh Marketing) | Pengguna perlu tahu apa yang baru/berubah. Marketing menggunakannya untuk promosi. Support menggunakannya untuk menjawab pertanyaan pengguna. Slack untuk pengumuman cepat, Notion sebagai arsip, Email Blast untuk jangkauan luas.                                                          |
| **Dokumentasi Pengujian Jangka Panjang** | Tim Internal (QA, Dev)                  | Notion (QA Knowledge Base)                      | Ini adalah *knowledge base* internal yang terus diperbarui. Notion adalah platform kolaboratif yang ideal untuk dokumen hidup seperti ini. Tidak perlu distribusi luas ke seluruh perusahaan.                                                                                                |
| **Laporan Eksekusi Pengujian** | PM, Tech Lead                             | Notion + Slack `#qa` (ringkasan harian)         | PM dan Tech Lead perlu *update* harian/mingguan tentang progres pengujian. Slack untuk komunikasi cepat dan informal, Notion untuk detail dan arsip.                                                                                                                                 |

**Pentingnya Memilih Saluran yang Tepat:**

*   **Notion:** Berfungsi sebagai *source of truth* terpusat dan kolaboratif untuk sebagian besar dokumen QA. Ini memungkinkan *link* antar dokumen dan pencarian yang efisien.
*   **PDF/Email:** Digunakan untuk dokumen formal yang membutuhkan persetujuan atau distribusi ke audiens yang mungkin tidak aktif di Notion.
*   **Slack `#announcements`:** Untuk pengumuman rilis yang cepat dan menjangkau seluruh tim internal.
*   **Slack `#qa`:** Untuk *update* harian atau ringkasan yang lebih teknis khusus untuk tim pengembangan dan produk.
*   **Drive Folder:** Untuk menyimpan aset yang mungkin dibutuhkan oleh tim lain, seperti gambar untuk marketing atau versi final yang mudah diunduh.

Memahami audiens dan saluran distribusi adalah kunci untuk memastikan informasi Anda tidak hanya *ada*, tetapi juga *digunakan* dan *dipahami* oleh pihak yang tepat.

## Rangkuman

Di bab ini, Anda telah mempelajari bahwa peran QA Engineer jauh melampaui sekadar eksekusi pengujian. Kemampuan untuk mendokumentasikan dan mengkomunikasikan hasil pengujian secara efektif adalah keterampilan yang sangat berharga. Kita telah membahas empat jenis dokumen utama:

1.  **Laporan UAT:** Dokumen krusial untuk *stakeholder* yang merangkum hasil pengujian penerimaan pengguna dan mendapatkan *sign-off* resmi untuk rilis.
2.  **Catatan Rilis:** Dokumen yang berhadapan dengan pengguna akhir, menginformasikan tentang fitur baru, perbaikan, dan isu yang diketahui dalam rilis terbaru.
3.  **Dokumentasi Pengujian Jangka Panjang:** *Knowledge base* internal yang vital untuk tim QA, mencakup lingkungan, data, infrastruktur otomasi, *checklist regresi*, dan pola *bug*.
4.  **Laporan Eksekusi Pengujian:** Catatan harian/mingguan tentang progres pengujian yang juga menjadi input untuk Laporan UAT.

Anda juga telah memahami pentingnya menggunakan konvensi header yang seragam untuk semua dokumen dan bagaimana mendistribusikan setiap dokumen ke audiens yang tepat melalui saluran yang paling efektif. Dengan menguasai aspek pelaporan dan dokumentasi ini, Anda tidak hanya menjadi *tester* yang handal, tetapi juga *quality gate* yang mampu menjembatani celah antara teknis dan bisnis, memastikan bahwa kualitas produk tidak hanya tercapai, tetapi juga dipahami dan dihargai oleh semua orang.

## Checklist Actionable

Berikut adalah beberapa langkah yang dapat Anda terapkan segera setelah membaca bab ini:

*   [ ] **Identifikasi *stakeholder* utama** untuk proyek Anda saat ini dan pahami kebutuhan informasi mereka.
*   [ ] **Biasakan diri Anda dengan template Laporan UAT.** Coba isi bagian-bagiannya dengan skenario fiktif untuk melatih pemahaman Anda.
*   [ ] **Buat draf Catatan Rilis** untuk fitur yang sedang Anda kerjakan, fokus pada manfaat pengguna dan hindari jargon teknis.
*   [ ] **Mulai membangun atau mengisi "QA Knowledge Base" di Notion Anda.** Setidaknya, dokumentasikan lingkungan pengujian dan data pengujian yang Anda gunakan.
*   [ ] **Jadwalkan "documentation hour" mingguan atau bulanan** untuk meninjau dan memperbarui dokumentasi pengujian jangka panjang Anda.
*   [ ] **Pastikan setiap dokumen yang Anda hasilkan memiliki header yang konsisten** sesuai konvensi yang dibahas.
*   [ ] **Verifikasi saluran distribusi** yang Anda gunakan untuk setiap jenis dokumen, apakah sudah tepat untuk audiensnya.
*   [ ] **Berlatih menulis ringkasan eksekutif** yang ringkas dan informatif untuk laporan Anda.
*   [ ] **Diskusikan dengan tim Anda** tentang pentingnya *sign-off* pada Laporan UAT dan bagaimana prosesnya akan dilakukan.
