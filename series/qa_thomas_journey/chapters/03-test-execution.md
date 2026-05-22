# Chapter 03: Test Execution — Smoke, Functional, Exploratory, Regression

Selamat datang di jantung operasi Quality Assurance! Jika pada bab sebelumnya kita telah belajar cara membaca *requirement* dan merancang strategi serta *test case* yang solid, kini saatnya kita beraksi. Chapter ini akan membawa Anda melalui tahapan eksekusi tes, yaitu momen di mana Anda benar-benar menguji aplikasi, menemukan *bug*, dan memvalidasi kualitas.

Eksekusi tes bukan sekadar "klik sana-sini" atau "menjalankan daftar tugas". Ini adalah proses strategis yang membutuhkan pemikiran kritis, observasi tajam, dan kemampuan untuk bertindak cepat. Kita akan membahas urutan eksekusi yang efisien, mengapa urutan tersebut penting, bagaimana menangani setiap jenis pengujian, hingga cara melaporkan hasil dan *bug* yang ditemukan. Tujuan utama kita adalah mengadopsi prinsip *fail-fast*: menemukan masalah secepat mungkin agar tim pengembangan dapat memperbaikinya tanpa menunda proses lebih lanjut.

Mari kita selami bagaimana seorang QA Engineer yang efektif menjalankan pengujian!

## Mengapa Urutan Eksekusi Tes Itu Penting? — Konsep Fail-Fast

Bayangkan Anda sedang membangun sebuah rumah. Apakah Anda akan langsung memasang atap sebelum memastikan pondasinya kokoh? Tentu tidak. Anda akan memulai dengan pondasi, lalu dinding, kemudian rangka atap, dan seterusnya. Setiap langkah dibangun di atas keberhasilan langkah sebelumnya.

Konsep *fail-fast* dalam pengujian memiliki filosofi yang sama. Kita ingin menemukan masalah paling fundamental dan kritis secepat mungkin. Mengapa?
1.  **Menghemat Waktu dan Sumber Daya:** Jika ada masalah serius di fungsionalitas dasar aplikasi, melanjutkan pengujian fungsional yang lebih mendalam akan membuang-buang waktu. Lebih baik berhenti, melaporkan, dan menunggu perbaikan.
2.  **Meningkatkan Efisiensi:** Dengan memastikan dasar-dasar berfungsi, kita dapat lebih percaya diri saat melangkah ke pengujian yang lebih kompleks, fokus pada detail tanpa khawatir fondasinya rapuh.
3.  **Mempercepat Umpan Balik:** Semakin cepat *bug* ditemukan dan dilaporkan, semakin cepat pengembang dapat memperbaikinya, mengurangi *cycle time* pengembangan secara keseluruhan.

Untuk mencapai prinsip *fail-fast*, kita akan mengikuti urutan eksekusi tes yang telah terbukti efektif. Urutan ini dirancang untuk secara progresif meningkatkan kedalaman dan cakupan pengujian, dimulai dari pemeriksaan paling dasar hingga eksplorasi yang lebih luas dan verifikasi regresi.

Berikut adalah urutan eksekusi tes yang akan kita ikuti:

1.  **Automation Smoke Testing:** Memastikan build dasar berfungsi.
2.  **Functional Testing:** Memverifikasi setiap *user story* atau fitur.
3.  **Automation Exploratory Testing:** Mencari *edge cases* dan perilaku tak terduga secara terprogram.
4.  **Regression Testing:** Memastikan tidak ada fungsionalitas lama yang rusak akibat perubahan baru.

Mari kita bahas masing-masing tahapan ini secara detail.

## 1. Automation Smoke Testing: Penjaga Gerbang Pertama

*Smoke Testing*, kadang disebut juga *Build Verification Test (BVT)*, adalah jenis pengujian awal yang dilakukan untuk memastikan bahwa *build* perangkat lunak yang baru di-deploy stabil dan fungsionalitas utamanya bekerja. Anggap saja ini sebagai "penjaga gerbang" pertama yang menentukan apakah *build* tersebut layak untuk diuji lebih lanjut.

**Apa yang Diperiksa?**
*   Aplikasi dapat diakses (misalnya, halaman login terbuka).
*   Fungsionalitas inti (misalnya, login, registrasi, membuat item dasar) berfungsi.
*   Tidak ada *error* fatal yang menyebabkan aplikasi *crash*.

**Tujuan Utama:**
*   Mencegah tim QA membuang waktu menguji *build* yang rusak secara fundamental.
*   Memberikan umpan balik instan kepada tim *engineering* jika ada masalah kritis pada *build* terbaru.

**Kapan Dijalankan?**
*Smoke Testing* idealnya dijalankan secara otomatis setiap kali ada *deploy* baru ke lingkungan pengembangan (misalnya, *staging* atau *dev*). Ini memastikan bahwa setiap perubahan kode yang masuk tidak merusak fungsionalitas dasar.

**Contoh Otomatisasi Smoke Test**
Biasanya, *smoke test* adalah *suite* yang relatif kecil namun penting. Anda dapat menjalankannya menggunakan *framework* pengujian yang relevan dengan *stack* teknologi proyek Anda.

```bash
# Contoh untuk proyek Python dengan Pytest
pytest tests/smoke/ --maxfail=1 -q

# Contoh untuk proyek JavaScript/Node.js
npm run test:smoke

# Contoh lain jika menggunakan Playwright (akan dibahas lebih lanjut di Chapter 07)
npx playwright test --grep "@smoke"
```

Perintah `--maxfail=1` pada `pytest` berarti pengujian akan berhenti setelah kegagalan pertama, ini sangat cocok dengan prinsip *fail-fast* untuk *smoke test*.

### Apa yang Harus Dilakukan Jika Smoke Test Gagal?

Ini adalah poin krusial yang harus Anda ingat:

*   **JANGAN LANJUTKAN:** Jika *smoke test* gagal, itu berarti *build* tidak stabil untuk pengujian lebih lanjut. Semua pengujian lain yang Anda lakukan setelahnya kemungkinan besar akan menemukan lebih banyak *bug* yang disebabkan oleh masalah dasar ini, yang pada akhirnya membuang waktu Anda dan tim.
*   **Laporkan Segera:** Prioritas utama Anda adalah memberi tahu tim *engineering* secepat mungkin. Komunikasi instan sangat penting di sini.

**Langkah-langkah Pelaporan Kegagalan Smoke Test:**

1.  **Identifikasi Masalah:** Lihat log *smoke test* untuk mengetahui bagian mana yang gagal.
2.  **Berhenti Total:** Hentikan semua aktivitas pengujian lainnya pada *build* tersebut.
3.  **Kirim Pesan ke Saluran #engineering:** Gunakan Slack atau *platform* komunikasi tim Anda untuk mengirim pesan ke saluran khusus *engineering*.
4.  **Tag Tech Lead:** Pastikan Anda me-mention *Tech Lead* atau individu yang bertanggung jawab atas *deploy* agar mereka segera menyadari masalahnya.
5.  **Sertakan Detail Penting:**
    *   Sebutkan bahwa *smoke test* gagal.
    *   Tautkan ke *build* atau *commit* yang bermasalah.
    *   Sebutkan modul atau fungsionalitas yang terdampak.
    *   Berikan tautan ke log *CI/CD* atau laporan *smoke test* yang lebih detail.

**Contoh Pesan Slack untuk Kegagalan Smoke Test:**

```
Halo tim #engineering,

Mohon perhatiannya, *smoke test* untuk *deploy* terbaru ke lingkungan *staging* [Link ke Build/Commit CI/CD] GAGAL.

Modul yang terdampak:
- [Login Pengguna]
- [Registrasi Akun]

Log selengkapnya dapat dilihat di sini: [Link ke Log CI/CD atau Laporan Otomatisasi]

Saya akan menunda semua pengujian fungsional hingga masalah ini teratasi. Mohon segera dicek. @[Nama Tech Lead]
```

Dengan tindakan cepat ini, Anda telah menjaga kualitas *pipeline* pengembangan dan mencegah pemborosan waktu yang berharga bagi tim QA.

## 2. Functional Testing: Memverifikasi Setiap Cerita Pengguna

Setelah *smoke test* berhasil dan Anda yakin *build* dasar berfungsi, langkah selanjutnya adalah *Functional Testing*. Di tahap ini, Anda akan memverifikasi bahwa setiap fitur atau *user story* yang telah dikembangkan bekerja sesuai dengan spesifikasi yang telah disepakati di *Product Requirement Document (PRD)* dan *test case* yang Anda rancang di Chapter 02.

**Apa yang Diperiksa?**
*   Setiap fungsionalitas yang disebutkan dalam *user story* atau *requirement*.
*   Apakah sistem menghasilkan *output* yang benar untuk *input* yang diberikan.
*   Apakah semua skenario positif, negatif, dan *edge case* (sesuai *test case* Anda) memberikan hasil yang diharapkan.

**Kapan Dijalankan?**
*   Setelah *smoke test* berhasil.
*   Ketika fitur baru selesai dikembangkan dan di-*deploy* ke lingkungan *staging* atau *QA*.

**Proses Melakukan Functional Testing:**

1.  **Ambil Test Case:** Gunakan daftar *test case* yang sudah Anda siapkan dari Chapter 02. Idealnya, *test case* ini sudah dikelompokkan per fitur atau *user story*.
2.  **Eksekusi Step-by-Step:** Jalankan setiap langkah dalam *test case* secara berurutan.
3.  **Verifikasi Hasil:** Bandingkan *actual result* dengan *expected result*.
4.  **Catat Status:** Tandai status setiap *test case*. Status umum meliputi:
    *   **Pass:** Hasil aktual sesuai dengan yang diharapkan.
    *   **Fail:** Hasil aktual tidak sesuai dengan yang diharapkan (ada *bug*).
    *   **Blocked:** Tidak dapat menjalankan *test case* karena ada *bug* di fungsionalitas sebelumnya atau *dependency* lain.
    *   **Skipped:** *Test case* tidak relevan untuk *build* saat ini atau tidak perlu dijalankan karena alasan tertentu.
5.  **Kumpulkan Bukti (untuk Kegagalan):** Jika sebuah *test case* gagal, sangat penting untuk mengumpulkan bukti yang cukup agar pengembang dapat mereproduksi dan memperbaiki *bug* tersebut. Bukti yang harus dikumpulkan meliputi:
    *   **Screenshot/Video:** Rekam layar atau ambil tangkapan layar saat *bug* terjadi. Video seringkali lebih baik untuk *bug* yang melibatkan interaksi dinamis.
    *   **Console Logs:** Buka *developer tools* di browser (biasanya F12) dan tangkap log di tab "Console". Ini bisa menunjukkan *error* JavaScript atau masalah di sisi *frontend*.
    *   **Network Logs:** Di *developer tools*, tab "Network" dapat menunjukkan permintaan API yang gagal atau respons yang tidak terduga.
    *   **Langkah Reproduksi (Repro Steps):** Tuliskan dengan sangat jelas dan terperinci langkah-langkah yang Anda lakukan untuk menemukan *bug* tersebut. Ini adalah hal terpenting!

**Alat untuk Melacak Functional Testing:**

Untuk melacak *test case* dan status eksekusinya, Anda bisa menggunakan berbagai alat:

*   **Spreadsheet (Google Sheets/Excel):** Sederhana dan mudah digunakan untuk proyek kecil. Anda bisa membuat kolom untuk ID *Test Case*, Deskripsi, Status, Bukti, dan Catatan *Bug*.
*   **Test Management Tools (Jira, TestRail, Zephyr, qTest):** Alat khusus yang dirancang untuk manajemen *test case*, *test execution*, dan pelaporan. Mereka menawarkan fitur yang lebih canggih seperti pelacakan riwayat, integrasi dengan *bug tracking*, dan laporan yang komprehensif.
*   **Notion:** Untuk tim yang menggunakan Notion sebagai *workspace* terpusat, Anda bisa membuat *sub-table* atau *database* khusus untuk *test case* dan eksekusinya.

**Contoh Pelacakan Test Case di Notion atau Spreadsheet:**

| ID Test Case | Deskripsi Test Case                                | Status   | Bukti (Link)                | Catatan Bug (Link) |
| :----------- | :------------------------------------------------- | :------- | :-------------------------- | :----------------- |
| TC-001       | Login dengan kredensial email dan password valid   | ✅ Pass  | -                           | -                  |
| TC-002       | Login dengan email tidak terdaftar                 | ❌ Fail  | [SS/Video TC-002]           | [BUG-005]          |
| TC-003       | Login dengan password salah                        | ✅ Pass  | -                           | -                  |
| TC-004       | Registrasi akun baru dengan data lengkap           | ✅ Pass  | -                           | -                  |
| TC-005       | Registrasi akun baru dengan email sudah terdaftar  | ❌ Fail  | [SS/Video TC-005]           | [BUG-006]          |
| TC-006       | Melihat daftar produk di halaman utama             | ✅ Pass  | -                           | -                  |
| TC-007       | Menambahkan produk ke keranjang belanja            | 🚫 Blocked | -                           | [BUG-007]          |
| TC-008       | Checkout dengan metode pembayaran kartu kredit     | ⏸️ Skipped | Tidak relevan untuk build ini | -                  |

Kolom "Catatan Bug (Link)" akan mengarah ke tiket *bug* yang Anda buat di sistem pelacakan *bug* (misalnya Notion, Jira), yang akan kita bahas lebih lanjut di Chapter 04.

Dengan melakukan *functional testing* secara sistematis, Anda memastikan bahwa setiap bagian dari aplikasi bekerja sesuai tujuan, dan Anda memiliki bukti yang kuat untuk setiap masalah yang ditemukan.

## 3. Automation Exploratory Testing: Berburu Kasus Edge yang Tersembunyi

Setelah Anda memverifikasi fungsionalitas inti melalui *functional testing*, saatnya untuk berburu *bug* yang lebih sulit ditemukan: *edge cases*, perilaku tak terduga, atau masalah yang muncul dari kombinasi input yang tidak biasa. Ini adalah ranah *Exploratory Testing*.

**Apa itu Exploratory Testing?**
Berbeda dengan *functional testing* yang mengikuti *test case* yang sudah ditentukan, *exploratory testing* adalah pendekatan pengujian yang tidak terstruktur, simultan dalam desain dan eksekusi. Artinya, Anda mendesain tes saat Anda menjalankannya, berdasarkan pengetahuan, pengalaman, dan intuisi Anda.

**Penting:** *Exploratory testing* **bukan *box-ticking***. Ini adalah aktivitas "berburu". Anda tidak hanya menandai *pass/fail*, tetapi Anda menjelajahi, bereksperimen, dan mengamati perilaku sistem yang tidak terduga.

**Tujuan Utama:**
*   Menemukan *bug* yang tidak tercakup oleh *test case* formal.
*   Mengidentifikasi *edge cases* atau skenario yang tidak terpikirkan sebelumnya.
*   Memahami lebih dalam bagaimana aplikasi berperilaku di bawah kondisi yang berbeda.
*   Memberikan umpan balik tentang kegunaan (usability) dan pengalaman pengguna (UX).

**Kapan Dijalankan?**
*   Setelah *functional testing* selesai dan *build* dianggap cukup stabil.
*   Ketika Anda memiliki waktu luang setelah pengujian utama, atau ketika Anda ingin memahami area baru dari aplikasi.

**Time-Box Exploratory Testing:**
Karena sifatnya yang tidak terstruktur, *exploratory testing* dapat menjadi *black hole* waktu jika tidak dibatasi. Sangat penting untuk menetapkan *time-box* atau batas waktu yang jelas. Misalnya: **4-8 jam per fitur atau area aplikasi.**

Dalam konteks "Automation Exploratory Testing", kita tidak hanya mengandalkan eksplorasi manual, tetapi juga memanfaatkan skrip otomatisasi untuk menghasilkan *input* secara terprogram dan mencari perilaku yang tidak terduga. Ini adalah perpaduan antara kecerdasan manusia dan kekuatan otomatisasi.

**Teknik Automation Exploratory Testing:**

1.  **Property-Based Testing:**
    *   **Konsep:** Alih-alih menguji dengan *input* spesifik, Anda mendefinisikan "properti" yang harus selalu benar untuk fungsi Anda, terlepas dari *input* yang valid. *Framework* kemudian menghasilkan ribuan *input* acak (tetapi valid) untuk mencoba melanggar properti tersebut.
    *   **Contoh:** Jika Anda memiliki fungsi `tambah(a, b)`, properti bisa jadi `tambah(a, b) == tambah(b, a)` (komutatif) atau `tambah(a, 0) == a`. *Framework* akan mencoba berbagai angka `a` dan `b` untuk melihat apakah properti ini selalu berlaku.
    *   **Library:** Hypothesis (Python), QuickCheck (Haskell/Scala), js-jig (JavaScript).

2.  **Fuzzing Inputs to APIs:**
    *   **Konsep:** *Fuzzing* melibatkan pengiriman *input* yang tidak valid, tidak terduga, atau semi-acak ke suatu sistem (misalnya, API, *form* web) untuk mencoba menyebabkan *crash*, *error*, atau perilaku yang tidak diinginkan.
    *   **Contoh:** Mengirim *string* yang sangat panjang ke kolom nama pengguna, karakter khusus ke kolom angka, JSON yang tidak valid ke *endpoint* API, atau nilai negatif ke kolom yang hanya menerima positif.
    *   **Tools:** Burp Suite (untuk aplikasi web), Postman (dengan koleksi yang dimodifikasi), atau skrip kustom menggunakan bahasa pemrograman favorit Anda.

3.  **Stress Sessions:**
    *   **Konsep:** Mensimulasikan banyak pengguna bersamaan atau banyak permintaan ke sistem untuk menguji kinerja, stabilitas, dan bagaimana aplikasi menangani beban tinggi.
    *   **Tujuan:** Menemukan *bottleneck*, *memory leak*, atau *race conditions* yang hanya muncul di bawah tekanan.
    *   **Tools:** JMeter, k6, Locust, Gatling.

**Contoh Skenario Exploratory Testing (Manual atau dengan Bantuan Script):**

*   **Form Input:**
    *   Memasukkan karakter khusus (`!@#$%^&*()`) ke semua kolom teks.
    *   Memasukkan teks yang sangat panjang (ribuan karakter) ke kolom yang seharusnya singkat.
    *   Mencoba mengunggah file dengan ukuran sangat besar atau tipe yang tidak didukung.
    *   Mengubah *input* di *developer console* (misalnya, membuat *input* yang disable menjadi *enable*).
*   **Alur Pengguna:**
    *   Melakukan tindakan yang tidak biasa: misalnya, menambahkan item ke keranjang, lalu mengklik tombol *back* beberapa kali, lalu mencoba *checkout* lagi.
    *   Membuka banyak tab browser secara bersamaan dan melakukan tindakan yang berbeda di setiap tab.
    *   Menguji aplikasi di berbagai ukuran layar dan orientasi (mode *responsive*).
    *   Memutus koneksi internet di tengah-tengah transaksi penting.

**Bagaimana Mencatat Hasil Exploratory Testing?**

Karena sifatnya yang tidak terstruktur, Anda tidak akan memiliki *test case* yang *pass/fail*. Namun, Anda tetap harus mencatat apa yang Anda temukan:

*   **Bug Baru:** Jika Anda menemukan *bug*, segera laporkan dengan format yang sama seperti *bug* dari *functional testing* (bukti, langkah reproduksi).
*   **Ide Test Case Baru:** Eksplorasi sering kali mengungkapkan skenario yang belum Anda pikirkan. Catat ide-ide ini untuk dimasukkan ke dalam *test plan* Anda di masa depan.
*   **Observasi:** Catat hal-hal menarik tentang perilaku sistem, area yang terasa rapuh, atau area yang membutuhkan pengujian lebih lanjut.
*   **Sesi Jurnal:** Beberapa QA Engineer suka membuat jurnal singkat selama sesi eksplorasi, mencatat apa yang mereka lakukan, apa yang mereka amati, dan apa yang mereka pelajari.

*Exploratory testing* adalah salah satu area di mana kreativitas dan intuisi seorang QA Engineer sangat bersinar. Dengan menggabungkannya dengan otomatisasi, Anda dapat memperluas jangkauan pencarian *bug* Anda secara signifikan.

## 4. Regression Testing: Memastikan Fungsionalitas Lama Tetap Berjalan

Setelah *functional testing* dan *exploratory testing* untuk fitur baru selesai, ada satu tahap krusial lagi sebelum *build* siap rilis: *Regression Testing*.

**Apa itu Regression Testing?**
*Regression Testing* adalah proses pengujian yang dilakukan untuk memastikan bahwa perubahan baru pada kode (misalnya, penambahan fitur baru, perbaikan *bug*, atau perubahan konfigurasi) tidak merusak fungsionalitas yang sudah ada dan sebelumnya bekerja dengan baik.

**Mengapa Penting?**
Dalam pengembangan perangkat lunak, sangat mudah bagi perubahan di satu bagian kode untuk secara tidak sengaja memengaruhi bagian lain yang tampaknya tidak terkait. Ini disebut "regresi". Aplikasi modern sering kali memiliki banyak *shared code paths* (jalur kode yang digunakan oleh berbagai fitur). Fitur baru atau perbaikan *bug* dapat memperkenalkan *bug* baru di area lain, dan *regression testing* adalah jaring pengaman kita untuk menangkapnya.

**Kapan Dijalankan?**
*   Sebelum setiap rilis besar (major release).
*   Setelah implementasi fitur baru atau perbaikan *bug* yang signifikan.
*   Secara berkala, misalnya, setiap minggu atau setiap dua minggu, untuk memastikan stabilitas aplikasi secara keseluruhan.

**Pendekatan untuk Regression Testing:**

Ada dua pendekatan utama untuk *regression testing*: otomatis dan manual. Idealnya, sebagian besar *regression test* harus diotomatisasi untuk efisiensi.

### a. Automated Regression Suite

Jika Anda memiliki *suite* pengujian otomatis yang komprehensif (seperti yang akan kita bahas di Chapter 07), ini adalah aset terbesar Anda untuk *regression testing*.

**Cara Melakukan:**
Cukup jalankan *suite* otomatisasi regresi Anda.

```bash
# Contoh untuk proyek Python dengan Pytest
pytest tests/regression/ -n 4 --html=reports/regression.html

# Contoh untuk proyek JavaScript/Playwright
npx playwright test --grep "@regression" --project=chromium --output=reports/
```

*   `pytest tests/regression/`: Menjalankan semua tes di folder `tests/regression/`.
*   `-n 4`: Menjalankan tes secara paralel menggunakan 4 proses (mempercepat eksekusi).
*   `--html=reports/regression.html`: Menghasilkan laporan dalam format HTML.
*   `--grep "@regression"`: Menjalankan tes yang diberi tag `@regression`.

**Keuntungan Otomatisasi:**
*   **Cepat:** Dapat dijalankan dalam hitungan menit atau jam, bukan hari.
*   **Konsisten:** Selalu menjalankan langkah yang sama persis setiap kali.
*   **Dapat Diulang:** Dapat dijalankan berulang kali tanpa kelelahan.
*   **Skalabilitas:** Mudah untuk menambahkan lebih banyak tes tanpa peningkatan biaya linier.

### b. Manual Regression Checklist

Untuk kasus di mana otomatisasi belum sepenuhnya diterapkan, atau untuk *flow* yang sangat kompleks yang sulit diotomatisasi, Anda dapat menggunakan *checklist* regresi manual.

**Cara Membuat dan Menggunakan:**
1.  **Identifikasi Alur Kunci:** Buat daftar alur pengguna atau fungsionalitas inti yang harus selalu berfungsi. Contoh:
    *   Login dan Logout pengguna.
    *   Proses *checkout* (jika aplikasi *e-commerce*).
    *   Membuat, mengedit, dan menghapus item dasar (jika aplikasi CRUD).
    *   Pencarian dan filter.
    *   Memuat halaman *dashboard* utama.
    *   Integrasi pembayaran (jika ada).
2.  **Dokumentasikan di Notion:** Simpan *checklist* ini di Notion atau alat manajemen proyek serupa dengan label khusus (misalnya, `Labels=["regression-checklist"]`).
3.  **Jalankan Secara Periodik:** Secara manual ikuti setiap item di *checklist* dan verifikasi fungsionalitasnya.
4.  **Catat Status:** Tandai *pass/fail* dan laporkan *bug* yang ditemukan seperti biasa.

**Contoh Manual Regression Checklist di Notion:**

```markdown
# Regression Checklist: Aplikasi E-commerce Thomas

**Status:** [Dalam Proses / Selesai]
**Terakhir Dijalankan:** 2023-10-26 (v1.5.0-rc1)

---

## Fungsionalitas Akun Pengguna
- [ ] Login dengan kredensial valid
- [ ] Login dengan kredensial tidak valid (email/password salah)
- [ ] Registrasi akun baru
- [ ] Reset password melalui email
- [ ] Mengubah informasi profil (nama, alamat)
- [ ] Logout

## Fungsionalitas Produk
- [ ] Melihat daftar produk di halaman utama
- [ ] Melihat detail produk
- [ ] Menggunakan fitur pencarian produk
- [ ] Menggunakan filter dan sortir produk

## Fungsionalitas Keranjang & Checkout
- [ ] Menambahkan produk ke keranjang belanja
- [ ] Mengubah kuantitas produk di keranjang
- [ ] Menghapus produk dari keranjang
- [ ] Melakukan checkout dengan metode pembayaran kartu kredit
- [ ] Melakukan checkout dengan metode pembayaran transfer bank
- [ ] Melihat riwayat pesanan setelah checkout berhasil

## Fungsionalitas Umum
- [ ] Memuat halaman utama tanpa error
- [ ] Navigasi antar halaman (header, footer)
- [ ] Responsivitas di perangkat mobile (uji beberapa resolusi kunci)
- [ ] Tidak ada error di Console Browser

---
**Catatan:** Jika ada item yang gagal, buat tiket bug dan tautkan di sini.
```

*Regression testing*, baik otomatis maupun manual, adalah investasi waktu yang sangat penting untuk menjaga kualitas produk seiring waktu. Tanpa ini, kita berisiko memperkenalkan *bug* baru setiap kali ada perubahan, yang dapat merusak kepercayaan pengguna dan reputasi produk.

## Pelaporan Eksekusi Tes: Transparansi Hasil

Setelah Anda selesai menjalankan *smoke*, *functional*, *exploratory*, dan *regression testing*, langkah selanjutnya adalah menyusun laporan eksekusi tes. Laporan ini adalah ringkasan dari semua aktivitas pengujian yang telah Anda lakukan, status kualitas aplikasi, dan *bug* yang ditemukan. Ini adalah cara Anda mengkomunikasikan hasil kerja keras Anda kepada tim proyek (PM, *engineering*, *stakeholder* lainnya).

**Tujuan Laporan Eksekusi Tes:**

*   Memberikan gambaran yang jelas dan ringkas tentang status kualitas *build* atau fitur yang diuji.
*   Mengidentifikasi area yang stabil dan area yang memerlukan perhatian lebih lanjut.
*   Menjadi dasar untuk keputusan "Siap Rilis" atau "Tidak Siap Rilis".
*   Mencatat *bug* yang ditemukan dan prioritasnya.

**Struktur Laporan Standar:**

Berikut adalah struktur laporan eksekusi tes yang efektif dan informatif, yang dapat Anda adaptasi sesuai kebutuhan proyek Anda. Anda bisa menyusunnya dalam format Markdown, dokumen Notion, atau bahkan email/pesan Slack yang lebih ringkas.

```markdown
# Test Execution Report — [Nama Fitur/Build] — [Tanggal Eksekusi]

**Tanggal:** 2023-10-26
**Lingkungan:** Staging v1.5.0-rc1
**Reporter:** QA Thomas

## Ringkasan Eksekusi Tes
Ringkasan ini memberikan gambaran cepat tentang keseluruhan status pengujian.

-   **Total Test Cases:** 50
-   **Passed:** 42 (84%)
-   **Failed:** 5
-   **Blocked:** 2
-   **Skipped:** 1

**Catatan:** Fungsionalitas utama [Sebutkan Fungsionalitas] telah diverifikasi dan berfungsi dengan baik. Terdapat beberapa isu di [Sebutkan Area Bermasalah].

## Bug yang Ditemukan
Daftar *bug* yang ditemukan selama siklus eksekusi ini, dikelompokkan berdasarkan prioritas. Sertakan tautan ke tiket *bug* di sistem pelacakan (Notion/Jira).

-   **P0 (Critical):** 1
    *   [BUG-001] Login button tidak responsif setelah percobaan gagal pertama - [Link ke Notion Bug]
-   **P1 (High):** 1
    *   [BUG-002] Error 500 saat menambahkan item ke keranjang dari halaman produk - [Link ke Notion Bug]
-   **P2 (Medium):** 2
    *   [BUG-003] Tampilan footer pecah di resolusi mobile tertentu - [Link ke Notion Bug]
    *   [BUG-004] Validasi input email tidak mendeteksi format email yang salah - [Link ke Notion Bug]
-   **P3 (Low):** 1
    *   [BUG-005] Typo pada tooltip "Tambah ke Keranjang" - [Link ke Notion Bug]

## Rekomendasi
Berdasarkan hasil eksekusi tes dan status *bug* yang ditemukan, berikan rekomendasi mengenai kesiapan rilis.

-   [ ] Siap untuk rilis
-   [ ] Siap secara kondisional (harus memperbaiki: [BUG-001], [BUG-002] sebelum rilis)
-   [X] TIDAK siap untuk rilis

## Risiko / Observasi Tambahan
Catat risiko potensial, area yang mungkin memerlukan pengujian lebih lanjut, atau observasi penting lainnya yang tidak masuk ke kategori di atas.

-   Ditemukan penurunan kinerja ringan pada halaman daftar produk saat memuat lebih dari 100 item. Perlu pengujian performa lebih lanjut.
-   Integrasi pihak ketiga [Nama Integrasi] belum diuji secara end-to-end karena *staging environment* tidak mendukung koneksi ke sana.
-   Beberapa *edge cases* terkait input form (misalnya, karakter khusus) belum sepenuhnya diuji karena keterbatasan waktu.
```

**Kapan dan Bagaimana Mendistribusikan Laporan:**

*   **Setelah Setiap Siklus Eksekusi:** Idealnya, laporan ini dibuat setelah setiap siklus eksekusi yang signifikan (misalnya, setelah pengujian fitur utama selesai, atau di akhir hari jika pengujian berlangsung beberapa hari).
*   **Saluran Komunikasi:**
    *   **Slack #qa:** Posting ringkasan laporan ke saluran QA tim Anda. Ini menjaga semua orang tetap *aware* dan memberikan transparansi.
    *   **Centralized Report:** Simpan laporan lengkap di lokasi terpusat seperti Google Drive (untuk laporan HTML otomatisasi), Notion, atau *wiki* tim Anda. Berikan tautan ke laporan lengkap di pesan Slack Anda.
    *   **Meeting / Demo:** Siapkan ringkasan untuk dibahas dalam *daily stand-up*, *sprint review*, atau *demo* fitur.

Dengan laporan yang terstruktur dengan baik, Anda tidak hanya melaporkan angka, tetapi juga memberikan konteks, rekomendasi, dan wawasan yang berharga bagi tim proyek. Ini adalah salah satu cara utama QA Engineer menunjukkan nilai strategis mereka.

## Routing Bug: Memastikan Bug Sampai ke Tangan yang Tepat

Menemukan *bug* adalah satu hal, tetapi memastikan *bug* tersebut ditangani dengan benar dan oleh orang yang tepat adalah hal lain. Di sinilah peran "Routing Bug" menjadi sangat penting. Sistem *routing* yang efektif memastikan bahwa *bug* dengan prioritas tinggi segera mendapatkan perhatian, sementara *bug* dengan prioritas lebih rendah masuk ke *backlog* untuk ditinjau.

**Pentingnya Routing yang Benar:**

*   **Efisiensi:** Mencegah *bug* kritis terabaikan dan *bug* minor mengganggu alur kerja pengembang.
*   **Prioritas:** Memastikan sumber daya tim *engineering* dialokasikan untuk masalah yang paling mendesak.
*   **Transparansi:** Semua *stakeholder* tahu di mana mencari *bug* dan statusnya.

### Sistem Prioritas Bug (P0-P3)

Kita akan menggunakan skala prioritas umum: P0, P1, P2, P3. Definisi ini mungkin sedikit bervariasi antar tim, tetapi inti maknanya sama.

*   **P0 (Critical / Blocker):**
    *   **Definisi:** Menghentikan fungsionalitas inti aplikasi, sistem tidak dapat digunakan, atau terjadi kehilangan data yang signifikan. Tidak ada *workaround*.
    *   **Contoh:** Pengguna tidak bisa login sama sekali, aplikasi *crash* saat startup, proses pembayaran selalu gagal.
    *   **Routing:**
        1.  Buat tiket *bug* di Notion (atau Jira).
        2.  Posting peringatan ke saluran Slack **`#incidents`** (saluran untuk masalah mendesak).
        3.  **DM langsung Tech Lead** atau pengembang yang bertanggung jawab. Ini adalah *bug* yang membutuhkan perhatian instan.
    *   **Contoh DM Slack ke Tech Lead:**
        ```
        @TechLeadName, ada P0 bug baru: [BUG-001] Login button not responding. Ini sangat kritis dan memblokir pengujian. Mohon segera lihat. Link tiket: <Notion Bug Link>
        ```

*   **P1 (High):**
    *   **Definisi:** Fungsionalitas inti terpengaruh secara signifikan, tetapi mungkin ada *workaround* atau tidak sepenuhnya memblokir seluruh sistem. Degradasi serius pada pengalaman pengguna.
    *   **Contoh:** Fitur utama tidak bekerja di browser tertentu, *error* saat upload gambar tetapi pengguna masih bisa upload gambar lain, sebagian data tidak ditampilkan.
    *   **Routing:**
        1.  Buat tiket *bug* di Notion.
        2.  Posting peringatan ke saluran Slack **`#incidents`**.
        3.  **DM langsung Tech Lead** atau pengembang yang bertanggung jawab. Meskipun ada *workaround*, ini tetap prioritas tinggi.

*   **P2 (Medium):**
    *   **Definisi:** Fungsionalitas non-inti terpengaruh, *minor issue*, *UI/UX glitch*, atau masalah yang tidak menghalangi penggunaan utama aplikasi.
    *   **Contoh:** Tampilan *footer* pecah di resolusi tertentu, validasi *input* yang kurang sempurna, *error* di *console* yang tidak memengaruhi fungsionalitas utama.
    *   **Routing:**
        1.  Buat tiket *bug* di Notion.
        2.  Posting ke saluran Slack **`#qa`** atau saluran umum tim pengembangan untuk visibilitas. Tidak perlu DM langsung.

*   **P3 (Low):**
    *   **Definisi:** Masalah kosmetik, *typo*, perbaikan kecil, saran perbaikan, atau masalah yang dampaknya minimal dan tidak memengaruhi fungsionalitas.
    *   **Contoh:** Typo pada label, warna tombol sedikit melenceng dari desain, *alignment* teks yang sedikit bergeser.
    *   **Routing:**
        1.  Buat tiket *bug* di Notion **saja**. *Bug* ini akan terlihat saat *backlog review* atau *sprint planning*, dan dapat diprioritaskan jika ada waktu atau relevan dengan *sprint* mendatang. Tidak perlu notifikasi Slack.

### Flow Routing Bug Otomatis vs. Manual

Tim yang lebih maju mungkin memiliki skrip atau integrasi yang mengotomatisasi *routing* ini.

**Contoh Skrip Otomatisasi (Konseptual, dari Source Material):**

```python
# scripts/qa_report_bug.py
# Skrip ini mengimplementasikan routing berbasis severity
# P0/P1 → Notion bug + #incidents Slack + DM Tech Lead
# P2    → Notion bug + #qa Slack
# P3    → Notion bug only (visible in backlog review)

# Cara penggunaan (dari terminal):
# python scripts/qa_report_bug.py --title "[login] Login button unresponsive" --severity P1 --assignee "dev-john"
```

**Ekuivalen Manual (Menggunakan Python untuk Ilustrasi Konsep):**

Jika Anda belum memiliki skrip otomatisasi penuh, Anda akan melakukan langkah-langkah ini secara manual menggunakan *tool* yang relevan (misalnya, membuat tiket di Notion secara manual, lalu mengirim pesan di Slack secara manual).

```python
# Ini adalah ilustrasi bagaimana sebuah skrip akan bekerja,
# Anda akan melakukan langkah-langkah ini secara manual
# menggunakan Notion dan Slack secara terpisah.

# Asumsikan Anda memiliki konektor untuk Notion dan Slack
# (Ini hanya pseudocode untuk menjelaskan konsep)
from notion_connector import NotionTicketing
from slack_connector import SlackConnector

# Inisialisasi konektor (asumsikan sudah dikonfigurasi)
nt = NotionTicketing.from_env()
slack = SlackConnector.from_env()

# Data bug yang ditemukan
bug_title = "[login] Login button unresponsive after first failed attempt"
bug_reporter = "qa-thomas"
bug_severity = "P1" # Bisa P0, P1, P2, P3
bug_steps = """
1. Navigate to /login
2. Enter valid email, wrong password, click Sign in
3. Wait for error message
4. Click Sign in again (without changing inputs)
"""
bug_expected = "Login attempt re-submitted"
bug_actual = "Button does not respond; no network request fires"
bug_environment = "staging v1.4.2-rc3, Chrome 124, macOS"
bug_screenshots = ["https://drive.google.com/link_ke_screenshot_1", "https://drive.google.com/link_ke_screenshot_2"]

# 1. Buat tiket bug di Notion
bug_ticket = nt.create_bug(
    title=bug_title,
    reporter=bug_reporter,
    severity=bug_severity,
    steps_to_reproduce=bug_steps,
    expected=bug_expected,
    actual=bug_actual,
    environment=bug_environment,
    screenshots=bug_screenshots,
)

print(f"Bug created in Notion: {bug_ticket.url}")

# 2. Lakukan routing berdasarkan severity
if bug_severity == "P0" or bug_severity == "P1":
    # Post ke #incidents channel
    slack.post_message(
        channel="#incidents",
        text=f":warning: **P{bug_severity} bug filed**: {bug_title}",
        ticket_url=bug_ticket.url,
        priority=bug_severity,
    )
    print(f"Posted to #incidents Slack channel for P{bug_severity} bug.")

    # DM Tech Lead
    slack.dm_user(
        user_id="U123ABC", # ID Slack Tech Lead
        text=f":alert: **P{bug_severity} bug requires immediate attention**: {bug_title}. Link: {bug_ticket.url}"
    )
    print(f"DM'd Tech Lead for P{bug_severity} bug.")

elif bug_severity == "P2":
    # Post ke #qa channel
    slack.post_message(
        channel="#qa",
        text=f":bug: **P2 bug filed**: {bug_title}",
        ticket_url=bug_ticket.url,
        priority=bug_severity,
    )
    print("Posted to #qa Slack channel for P2 bug.")

elif bug_severity == "P3":
    print("P3 bug filed in Notion only. Will be reviewed in backlog.")

```

Melalui sistem *routing* ini, Anda tidak hanya menemukan *bug*, tetapi juga memastikan bahwa setiap *bug* mendapatkan visibilitas dan penanganan yang sesuai dengan tingkat urgensinya. Ini adalah bagian integral dari menjaga alur kerja tim pengembangan tetap efisien dan menjaga kualitas produk secara keseluruhan.

## Laporan Terpusat dan Sign-off: Akhir dari Siklus Eksekusi

Setelah semua siklus eksekusi tes (smoke, fungsional, eksplorasi, regresi) selesai, laporan eksekusi tes telah disusun, dan semua *bug* telah di-route, ada dua langkah terakhir yang penting: membuat "Laporan Terpusat" dan melakukan "Sign-off" untuk menyatakan kesiapan rilis.

### Laporan Terpusat (Centralized Report)

Laporan terpusat adalah ringkasan progres harian atau ringkasan akhir siklus pengujian yang dibagikan kepada seluruh tim proyek, terutama Product Manager (PM) dan tim *engineering*. Ini biasanya berupa pesan singkat di saluran Slack yang berisi poin-poin penting dari laporan eksekusi tes yang lebih detail.

**Tujuan Laporan Terpusat:**

*   Memberikan *update* reguler tentang status pengujian kepada semua *stakeholder*.
*   Menjaga transparansi dan memastikan semua orang memiliki pemahaman yang sama tentang kualitas *build*.
*   Membantu PM dan *Tech Lead* dalam mengambil keputusan terkait rilis.

**Konten Laporan Terpusat (Biasanya Dikirim ke Saluran #qa):**

*   **Progres Tes:** Berapa banyak *test case* yang telah dijalankan dari total yang direncanakan (misalnya, X dari Y *test case* telah dijalankan).
*   **Bug Baru yang Ditemukan:** Jumlah *bug* baru yang diajukan, dikelompokkan berdasarkan *severity*.
*   **Bloker yang Terbuka:** Jika ada *bug* P0 atau P1 yang masih terbuka dan memblokir pengujian lebih lanjut.
*   **Estimasi Kesiapan Rilis (ETA to "ready for release"):** Perkiraan kapan *build* akan siap untuk rilis, berdasarkan progres dan *bug* yang tersisa.
*   **Tautan ke Laporan Lengkap:** Selalu sertakan tautan ke laporan eksekusi tes yang lebih detail (misalnya, dokumen Notion, laporan HTML otomatisasi di Google Drive).

**Contoh Pesan Slack (Laporan Harian/Akhir Siklus):**

```
Halo Tim #qa,

Berikut adalah update QA untuk [Nama Fitur/Build] (v1.5.0-rc1) per 2023-10-26:

**Progres Tes:**
- Total 50 test case, 45 sudah dijalankan (90%).
- Status: 42 Passed, 3 Failed, 0 Blocked, 0 Skipped.

**Bug Baru Ditemukan:**
- P0: 1 ([BUG-001] Login button unresponsive)
- P1: 1 ([BUG-002] Error 500 saat tambah item ke keranjang)
- P2: 2 ([BUG-003], [BUG-004])
- P3: 1 ([BUG-005])

**Bloker Terbuka:**
- [BUG-001] masih memblokir pengujian alur login lanjutan. Tim engineering sedang menanganinya.

**ETA Ready for Release:**
- Jika [BUG-001] dan [BUG-002] diperbaiki hari ini, saya perkirakan build ini bisa "Ready for Release" besok sore.

Laporan eksekusi lengkap: [Link ke Notion Test Execution Report]
Laporan otomatisasi HTML: [Link ke Google Drive/S3 Bucket]

Mohon informasinya jika ada pertanyaan!
```

### Sign-off: Pernyataan Kesiapan Rilis

"Sign-off" adalah momen formal di mana Anda, sebagai QA Engineer, secara resmi menyatakan bahwa *build* atau fitur telah memenuhi semua kriteria keluar (exit criteria) pengujian dan siap untuk rilis atau tahap selanjutnya (misalnya, *User Acceptance Testing - UAT*).

**Kriteria Keluar (Exit Criteria) yang Umum:**

*   Semua *test case* kritis dan prioritas tinggi telah dijalankan dan *pass*.
*   Semua *bug* P0 dan P1 telah diperbaiki dan diverifikasi.
*   *Bug* P2 dan P3 yang tersisa telah ditinjau dan disepakati untuk ditunda ke *sprint* berikutnya atau diterima sebagai *known issue*.
*   *Regression suite* telah dijalankan dan tidak ada regresi kritis yang ditemukan.
*   Semua *stakeholder* yang relevan telah diberitahu dan setuju dengan status kesiapan.

**Langkah-langkah Sign-off:**

1.  **Verifikasi Semua Kriteria Keluar:** Pastikan Anda telah memeriksa setiap poin dalam daftar kriteria keluar tim Anda.
2.  **Perbarui Status Tiket Test Strategy:** Jika Anda melacak *test strategy* dalam sistem manajemen proyek (misalnya Notion), ubah status tiket tersebut menjadi `Done` atau `Ready for Release`.
3.  **Hasilkan UAT Report (Opsional, tapi Direkomendasikan):** Jika proyek Anda melibatkan *User Acceptance Testing* (UAT), ini adalah waktu yang tepat untuk mulai menyusun UAT Report yang merangkum hasil pengujian Anda dan akan menjadi dasar bagi UAT oleh *end-user* atau PM. (Ini akan dibahas lebih detail di Chapter 05).
4.  **Beritahu Product Manager (PM):** Kirim pesan eksplisit kepada PM (dan *Tech Lead*) yang menyatakan bahwa fitur atau *build* sudah "Ready for Release". Pesan ini harus jelas dan ringkas.

**Contoh Pesan Slack ke PM untuk Sign-off:**

```
Halo @PMThomas dan @TechLeadName,

Saya ingin menginformasikan bahwa fitur [Nama Fitur] (Link ke PRD/Epic) telah selesai melalui semua siklus eksekusi tes (smoke, fungsional, eksplorasi, regresi) untuk build `v1.5.0-rc1`.

**Semua test case kritis dan prioritas tinggi telah PASS.**
**Semua bug P0 dan P1 telah diperbaiki dan diverifikasi.**
Bug P2 dan P3 yang tersisa telah disepakati untuk ditunda/diterima.

Berdasarkan hasil pengujian komprehensif, saya merekomendasikan fitur ini **SIAP UNTUK RILIS.**

Detail laporan eksekusi lengkap dapat dilihat di sini: [Link ke Notion Test Execution Report]

Mohon informasinya jika ada pertanyaan lebih lanjut. Terima kasih!
```

Dengan melakukan pelaporan terpusat dan *sign-off* secara formal, Anda tidak hanya menyelesaikan tugas pengujian Anda, tetapi juga memainkan peran kunci dalam proses pengambilan keputusan rilis, memastikan bahwa produk yang diluncurkan memiliki kualitas terbaik yang mungkin.

---

## Rangkuman

Chapter ini telah membawa Anda melalui inti dari tugas seorang QA Engineer: eksekusi tes. Kita telah membahas bagaimana pendekatan yang terstruktur dan berprinsip *fail-fast* dapat menghemat waktu dan sumber daya tim.

Berikut poin-poin penting yang perlu Anda ingat:

*   **Urutan Eksekusi Itu Penting:** Selalu ikuti urutan Smoke -> Functional -> Exploratory -> Regression untuk menemukan masalah paling kritis di awal dan mengoptimalkan efisiensi.
*   **Smoke Test sebagai Penjaga Gerbang:** Jika *smoke test* gagal, segera hentikan pengujian, laporkan ke tim *engineering* (dan *Tech Lead*), dan jangan lanjutkan hingga masalah dasar teratasi.
*   **Functional Testing:** Verifikasi setiap *user story* dengan *test case* yang telah dibuat, kumpulkan bukti yang solid untuk setiap kegagalan.
*   **Exploratory Testing:** Lakukan "perburuan" *bug* yang tidak terduga dan *edge cases* dengan *time-box* yang jelas (4-8 jam), baik secara manual maupun dengan bantuan skrip otomatisasi. Ini bukan sekadar *box-ticking*.
*   **Regression Testing:** Pastikan perubahan baru tidak merusak fungsionalitas lama, dengan memanfaatkan *suite* otomatisasi atau *checklist* manual.
*   **Pelaporan yang Transparan:** Susun laporan eksekusi tes yang ringkas namun informatif, mencakup ringkasan, daftar *bug*, dan rekomendasi.
*   **Routing Bug yang Efektif:** Tentukan prioritas *bug* (P0-P3) dan *route* ke saluran komunikasi yang tepat (DM *Tech Lead*, `#incidents`, `#qa`, atau hanya Notion) agar mendapatkan perhatian sesuai urgensinya.
*   **Laporan Terpusat dan Sign-off:** Berikan *update* reguler kepada tim melalui laporan terpusat dan berikan *sign-off* formal ketika semua kriteria keluar terpenuhi, menyatakan bahwa *build* siap rilis.

Anda kini memiliki pemahaman yang kuat tentang bagaimana menjalankan pengujian secara strategis dan efisien. Di chapter berikutnya, kita akan menyelami lebih dalam tentang bagaimana melaporkan *bug* secara efektif, memastikan setiap *bug* dapat direproduksi dan ditangani.

---

## Checklist Actionable

Berikut adalah daftar tindakan yang bisa Anda lakukan dan praktikkan setelah membaca chapter ini:

*   [ ] **Pahami dan Terapkan Urutan Eksekusi:** Selalu mulai dengan *Smoke Testing*, lalu *Functional*, *Exploratory*, dan terakhir *Regression*.
*   [ ] **Siapkan Skrip Smoke Test Otomatis:** Identifikasi fungsionalitas kunci aplikasi Anda dan buat skrip *smoke test* otomatis yang berjalan cepat.
*   [ ] **Tentukan Protokol Kegagalan Smoke Test:** Buat *template* pesan Slack untuk melaporkan kegagalan *smoke test* ke `#engineering` dan pastikan Anda tahu siapa *Tech Lead* yang harus di-DM.
*   [ ] **Gunakan Alat Pelacakan Tes:** Pilih *spreadsheet* atau *test management tool* (seperti Notion) untuk melacak status setiap *test case* selama *functional testing*.
*   [ ] **Kumpulkan Bukti Komprehensif:** Saat menemukan *bug* di *functional testing*, selalu ambil *screenshot/video*, *console logs*, *network logs*, dan tulis *repro steps* yang jelas.
*   [ ] **Alokasikan Waktu untuk Exploratory Testing:** Jadwalkan sesi *exploratory testing* dengan *time-box* (misalnya, 4-8 jam) setelah *functional testing* untuk setiap fitur baru.
*   [ ] **Buat atau Perbarui Regression Checklist:** Identifikasi alur kunci di aplikasi Anda dan buat *checklist* regresi (manual atau otomatis) yang akan dijalankan secara berkala.
*   [ ] **Adaptasi Template Laporan Eksekusi Tes:** Sesuaikan *template* laporan yang diberikan di chapter ini dengan kebutuhan proyek Anda dan gunakan secara konsisten.
*   [ ] **Pahami Definisi Prioritas Bug (P0-P3):** Pastikan Anda dan tim Anda memiliki pemahaman yang sama tentang definisi setiap prioritas *bug*.
*   [ ] **Tentukan Flow Routing Bug:** Latih diri Anda untuk merouting *bug* sesuai prioritasnya: P0/P1 ke `#incidents` + DM *Tech Lead*; P2 ke `#qa`; P3 ke Notion saja.
*   [ ] **Siapkan Template Pesan Sign-off:** Buat *template* pesan Slack untuk memberitahu PM dan *Tech Lead* saat *build* atau fitur siap rilis.
