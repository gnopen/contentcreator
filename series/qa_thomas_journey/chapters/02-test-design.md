# Chapter 02: Test Design — Strategi, Estimasi, dan Test Case

Setelah Anda berhasil menyelami dunia *Requirement Analysis* di bab sebelumnya, kini saatnya kita melangkah lebih jauh. Memahami kebutuhan produk adalah fondasi, namun bagaimana kita memastikan bahwa kebutuhan tersebut benar-benar terpenuhi oleh produk yang akan dibangun? Jawabannya ada di *Test Design*.

Banyak yang mengira peran QA baru dimulai setelah *developer* selesai menulis kode. Namun, di *Journey QA Thomas*, kami percaya bahwa peran QA adalah penjaga kualitas sejak dini. *Test Design* adalah momen krusial di mana Anda, sebagai QA Engineer, mulai merancang cetak biru pengujian Anda, bahkan sebelum satu baris kode pun ditulis oleh tim *engineering*. Ini adalah kesempatan emas untuk mengidentifikasi potensi masalah, menyelaraskan ekspektasi, dan membangun fondasi yang kokoh untuk pengujian yang efektif.

Pada bab ini, kita akan membahas secara mendalam bagaimana membangun *Test Strategy* yang komprehensif, melakukan estimasi waktu yang realistis, dan menulis *Test Case* dalam empat kategori penting. Anda akan melihat bagaimana setiap langkah ini berkontribusi pada kualitas produk secara keseluruhan, dan bagaimana Anda dapat menjadi Quality Gate yang proaktif, bukan hanya reaktif. Mari kita mulai merancang!

---

## 1. Merancang Strategi Pengujian (Test Strategy)

*Test Strategy* adalah dokumen hidup yang menjadi panduan utama Anda dalam melakukan pengujian untuk sebuah fitur atau proyek. Ini bukan sekadar daftar tugas, melainkan sebuah peta jalan yang menjawab pertanyaan-pertanyaan fundamental: **APA** yang akan kita uji, **BAGAIMANA** cara mengujinya, **DENGAN APA** pengujian itu dilakukan, dan **KAPAN** pengujian itu harus selesai.

Menyusun *Test Strategy* secara dini memiliki beberapa keuntungan:
1.  **Klarifikasi Scope**: Memastikan semua pihak (PM, Developer, QA) memiliki pemahaman yang sama tentang batasan pengujian.
2.  **Identifikasi Risiko**: Mengidentifikasi potensi masalah lebih awal dan merencanakan mitigasinya.
3.  **Estimasi Akurat**: Memberikan dasar yang kuat untuk estimasi waktu dan sumber daya.
4.  **Standarisasi**: Menjaga konsistensi dalam pendekatan pengujian di seluruh proyek.

Di Thomas, kami menggunakan *template* standar yang disimpan sebagai tugas di Notion, dengan label `test-strategy`. Ini memastikan konsistensi dan kemudahan pelacakan. Mari kita bedah setiap bagian dari *template* ini.

### Template Test Strategy

Berikut adalah *template* yang kami gunakan. Anda bisa mengadaptasinya sesuai kebutuhan tim Anda.

```markdown
# Test Strategy: <Nama Fitur>

## Scope
- In scope: <Daftar user story, fungsionalitas, atau modul yang akan diuji secara eksplisit>
- Out of scope: <Daftar fungsionalitas atau modul yang secara eksplisit TIDAK akan diuji dalam iterasi ini, beserta alasannya jika perlu>

## Test Approach
- Automation Smoke: <Ya/Tidak, skenario mana yang akan diotomatisasi untuk smoke test>
- Functional Testing: <Pendekatan pengujian fungsional, misal: berdasarkan user story, end-to-end, integrasi>
- Regression: <Rencana untuk pengujian regresi; apakah akan menjalankan seluruh suite yang ada, atau menambahkan kasus baru>
- Exploratory: <Alokasi waktu (time-box), area fokus untuk pengujian eksplorasi>
- Performance: <Jika berlaku, target performa yang akan diuji (misal: response time, throughput)>
- Accessibility: <Jika berlaku, standar aksesibilitas yang akan dipatuhi (misal: WCAG)>

## Environments
- Test data: <Bagaimana data uji akan disiapkan (misal: seeded, manual, via API)>
- Devices: <Daftar perangkat yang akan digunakan untuk pengujian (misal: Desktop, Mobile Android, Mobile iOS)>
- Browsers: <Daftar browser yang akan didukung dan diuji (misal: Chrome, Firefox, Safari, Edge)>
- Versions / builds tested: <Rencana versi/build yang akan diuji (misal: versi staging terbaru, build PR spesifik)>

## Entry Criteria
- [ ] PRD (Product Requirement Document) final dan disetujui
- [ ] Test scenarios (dari Chapter 01) disetujui oleh PM/Tech Lead
- [ ] Build aplikasi tersedia di environment staging
- [ ] Data uji awal telah disiapkan (seeded)

## Exit Criteria
- [ ] Semua test case P0/P1 berhasil (passing)
- [ ] Tidak ada bug P0/P1 yang masih terbuka
- [ ] Suite regresi berhasil dijalankan tanpa blokir (passing)
- [ ] UAT (User Acceptance Testing) telah ditandatangani oleh pemangku kepentingan

## Estimasi Waktu (WAJIB)
- Penyusunan Test Case: <h> jam
- Persiapan data uji: <h> jam
- Eksekusi (pass pertama): <h> jam
- Verifikasi bug & pengerjaan ulang: <h> jam
- Regresi: <h> jam
- Pelaporan: <h> jam
- Buffer (20%): <h> jam
**TOTAL: <h> jam / <d> hari**

## Risks
- <Risiko yang diidentifikasi> → <Rencana mitigasi>
```

Mari kita bahas lebih lanjut setiap bagiannya:

### a. Scope: Batasan Pengujian
Bagian ini adalah tentang mendefinisikan apa yang akan Anda uji dan apa yang tidak. Penting untuk sangat eksplisit di sini.

*   **In scope**: Cantumkan semua *user story*, fungsionalitas, atau area modul yang akan menjadi fokus pengujian Anda. Ini membantu memastikan tidak ada yang terlewat dan semua ekspektasi terpenuhi. Misalnya, jika Anda menguji fitur "Pembayaran Online", yang termasuk dalam *scope* bisa jadi "Pengguna dapat membayar dengan kartu kredit", "Pengguna dapat melihat riwayat transaksi", dll.
*   **Out of scope**: Ini sama pentingnya. Secara eksplisit nyatakan fungsionalitas yang *tidak* akan diuji dalam iterasi ini. Mengapa? Untuk menghindari kesalahpahaman dan mengelola ekspektasi. Mungkin fitur tertentu akan diuji di fase berikutnya, atau mungkin itu adalah fungsionalitas lama yang tidak terpengaruh oleh perubahan saat ini.

### b. Test Approach: Bagaimana Kita Akan Menguji?
Bagian ini menjelaskan metodologi dan jenis pengujian yang akan Anda terapkan.

*   **Automation Smoke**: Apakah ada *smoke test* yang akan diotomatisasi? *Smoke test* adalah pengujian cepat untuk memastikan fungsionalitas inti aplikasi berjalan. Jika ya, skenario mana saja yang akan di-otomatisasi?
*   **Functional Testing**: Ini adalah pengujian utama untuk memastikan fungsionalitas bekerja sesuai PRD. Anda bisa menjelaskan pendekatan Anda, apakah itu *end-to-end*, *integrasi*, atau berbasis *user story*.
*   **Regression**: Bagaimana Anda akan menangani *regression testing*? Apakah Anda akan menjalankan seluruh *suite* regresi yang ada, atau hanya subset yang relevan dengan perubahan saat ini?
*   **Exploratory**: Alokasikan waktu untuk *exploratory testing*. Ini adalah pengujian tanpa skenario yang terstruktur, di mana Anda bebas menjelajahi aplikasi untuk menemukan bug yang tidak terduga. Tentukan *time-box* (misalnya, 2 jam) dan area fokusnya.
*   **Performance & Accessibility**: Jika fitur memiliki persyaratan performa atau aksesibilitas, sebutkan target dan standar yang akan diuji.

### c. Environments: Dengan Apa Kita Menguji?
Detail teknis tentang lingkungan pengujian Anda.

*   **Test data**: Jelaskan bagaimana Anda akan mendapatkan data yang dibutuhkan untuk pengujian. Apakah Anda akan menggunakan data yang sudah ada, membuat data baru secara manual, atau menggunakan *script* otomatis (*seeded data*)?
*   **Devices & Browsers**: Daftar perangkat (misalnya, iPhone 13, Samsung Galaxy S22, Desktop) dan *browser* (misalnya, Chrome, Firefox, Safari) yang akan Anda gunakan untuk pengujian. Ini penting untuk memastikan kompatibilitas.
*   **Versions / builds tested**: Tentukan versi aplikasi atau nomor *build* yang akan Anda uji. Pastikan Anda memiliki mekanisme untuk melacak versi yang sedang diuji.

### d. Entry Criteria: Kapan Kita Boleh Mulai Menguji?
Ini adalah daftar prasyarat yang harus terpenuhi sebelum Anda dapat *memulai* eksekusi pengujian. Tanpa ini, Anda berisiko membuang waktu menguji *build* yang tidak stabil atau persyaratan yang belum final.

*   **PRD final**: Dokumen persyaratan produk harus sudah disetujui dan tidak ada lagi perubahan signifikan.
*   **Test scenarios approved**: Skenario pengujian yang Anda buat (dari Chapter 01) telah ditinjau dan disetujui oleh tim.
*   **Build available in staging**: Versi aplikasi yang akan diuji sudah ter-deploy di lingkungan *staging* dan siap diakses.
*   **Test data seeded**: Data yang diperlukan untuk pengujian sudah tersedia dan siap digunakan.

### e. Exit Criteria: Kapan Kita Boleh Menyatakan Pengujian Selesai?
Ini adalah kondisi yang harus terpenuhi agar pengujian dapat dianggap selesai dan fitur siap untuk dirilis.

*   **All P0/P1 test cases passing**: Semua *test case* dengan prioritas tertinggi (P0 dan P1) harus berhasil.
*   **No open P0/P1 bugs**: Tidak ada bug dengan prioritas P0 atau P1 yang masih terbuka. Bug P2 dan P3 mungkin bisa diterima dengan persetujuan tim, tergantung risikonya.
*   **Regression suite passing**: *Suite* regresi telah dijalankan dan semua *test case* di dalamnya berhasil.
*   **UAT signed off**: *User Acceptance Testing* (UAT) telah diselesaikan dan disetujui oleh *stakeholder* terkait.

### f. Estimasi Waktu (WAJIB)
Ini adalah bagian yang seringkali dianggap remeh, namun sangat krusial. Estimasi waktu yang akurat membantu tim perencanaan proyek (PM, Tech Lead) dalam menentukan jadwal rilis dan kapasitas tim. **Setiap Test Strategy harus memiliki bagian estimasi waktu ini.**

Berikut adalah komponen-komponen yang perlu Anda estimasi:
*   **Penyusunan Test Case**: Berapa jam yang Anda butuhkan untuk menulis semua *test case* untuk fitur ini?
*   **Persiapan data uji**: Berapa jam untuk menyiapkan semua data yang dibutuhkan? Ini bisa termasuk membuat akun, mengimpor data, atau memanipulasi basis data.
*   **Eksekusi (pass pertama)**: Berapa jam untuk menjalankan semua *test case* untuk pertama kalinya?
*   **Verifikasi bug & pengerjaan ulang**: Alokasikan waktu untuk memverifikasi perbaikan bug dan melakukan *re-testing* jika ada bagian aplikasi yang diubah.
*   **Regresi**: Berapa jam untuk menjalankan *regression test* yang relevan?
*   **Pelaporan**: Waktu untuk menyusun laporan pengujian, *release notes*, dll.
*   **Buffer (20%)**: Selalu tambahkan *buffer*! Proyek jarang berjalan persis sesuai rencana. *Buffer* 20% adalah praktik yang baik untuk mengakomodasi hal-hal tak terduga.

Jumlahkan semua komponen ini untuk mendapatkan total estimasi waktu dalam jam, lalu konversikan ke hari kerja.

**Contoh Pengisian Estimasi Waktu:**
Misalkan Anda mengestimasi fitur "Pembayaran Online" sebagai berikut:
*   Penyusunan Test Case: 8 jam
*   Persiapan data uji: 4 jam
*   Eksekusi (pass pertama): 12 jam
*   Verifikasi bug & pengerjaan ulang: 6 jam
*   Regresi: 4 jam
*   Pelaporan: 2 jam
*   Buffer (20% dari 36 jam): 7.2 jam (bulatkan menjadi 8 jam)
**TOTAL: 44 jam / 5.5 hari kerja** (dengan asumsi 8 jam kerja per hari)

### g. Risks: Identifikasi dan Mitigasi
Bagian terakhir dari *Test Strategy* adalah mengidentifikasi potensi risiko yang dapat menghambat proses pengujian atau kualitas produk, serta rencana mitigasinya.

*   **Contoh Risiko**: Keterlambatan *build*, perubahan persyaratan mendadak, lingkungan pengujian tidak stabil, keterbatasan sumber daya, dll.
*   **Mitigasi**: Apa yang akan Anda lakukan untuk mengurangi dampak risiko tersebut? Misalnya, jika risikonya adalah "keterlambatan *build*", mitigasinya bisa berupa "komunikasi proaktif dengan tim *development* dan PM untuk mendapatkan *update* status *build* secara berkala".

Dengan *Test Strategy* yang solid, Anda telah meletakkan dasar yang kuat untuk pengujian yang terstruktur dan efisien. Selanjutnya, kita akan membahas cara membuat *Test Case* yang spesifik dan komprehensif.

---

## 2. Membangun Test Case: Empat Kategori Krusial

Setelah *Test Strategy* Anda terbentuk, langkah berikutnya adalah menerjemahkan *test scenarios* yang telah Anda buat di Chapter 01 menjadi *Test Case* yang spesifik dan dapat dieksekusi. Di Thomas, kami menekankan bahwa setiap set *test case* harus mencakup empat kategori berikut untuk memastikan cakupan pengujian yang menyeluruh:

1.  **Positive Cases (Skenario Sukses)**
2.  **Negative Cases (Skenario Gagal)**
3.  **Edge Cases (Skenario Batasan/Tak Biasa)**
4.  **Data Preparation (Persiapan Data Uji)**

Jangan pernah melewatkan salah satu kategori ini. Masing-masing memiliki peran penting dalam memastikan kualitas produk. Untuk memberikan contoh konkret, kita akan menggunakan fitur "Login Pengguna" sebagai studi kasus.

### Format Test Case Standar

Sebelum masuk ke kategorinya, mari kita lihat format standar *Test Case* yang kami gunakan. Format ini memastikan semua informasi penting tercatat dan *test case* mudah dipahami serta dieksekusi.

```markdown
### TC-[ID]: [Judul singkat deskriptif]

**Tipe:** Positive | Negative | Edge | Data Preparation
**Linked Story:** [ID User Story atau tautan PRD yang terkait]
**Linked AC:** [Nomor Acceptance Criteria dari user story yang divalidasi]
**Prioritas:** P0 | P1 | P2 | P3
**Estimasi waktu:** [menit]

**Preconditions (Prasyarat):**
- [kondisi #1 yang harus terpenuhi sebelum memulai]
- [kondisi #2 yang harus terpenuhi sebelum memulai]

**Test data (Data Uji):**
- [input atau referensi fixture yang digunakan]

**Steps (Langkah-langkah):**
1. [aksi yang tepat]
2. [aksi yang tepat]
3. [aksi yang tepat]

**Expected result (Hasil yang diharapkan):**
- [hasil yang dapat diamati — harus jelas dan tidak ambigu]

**Tear-down (Jika diperlukan):**
- [mengembalikan kondisi semula, membersihkan data]
```

**Pentingnya Estimasi Waktu per Test Case:**
Seperti yang telah dibahas di *Test Strategy*, setiap *test case* **wajib** memiliki estimasi waktu. Mengapa ini begitu penting?
*   **Agregasi ke Test Strategy**: Estimasi ini akan diakumulasikan untuk membentuk estimasi total dalam *Test Strategy* Anda, yang dibutuhkan oleh PM dan Tech Lead untuk perencanaan *sprint*.
*   **Identifikasi Utang Pengujian**: *Test case* manual yang memakan waktu lama (misalnya, 30 menit) adalah kandidat kuat untuk diotomatisasi. Ini membantu Anda mengidentifikasi "utang pengujian" Anda.
*   **Ekspektasi SLA QA**: Menetapkan ekspektasi waktu untuk eksekusi pengujian.

Berikut adalah panduan kasar untuk estimasi waktu:
*   **< 5 menit**: Sangat cepat, kandidat kuat untuk otomatisasi.
*   **5-15 menit**: Manual tapi cepat, bisa diotomatisasi jika sering diulang.
*   **15-30 menit**: Membutuhkan *setup* yang kompleks, ROI otomatisasi tinggi.
*   **30+ menit**: Segera eskalasi! Hampir selalu layak untuk diotomatisasi.

Sekarang, mari kita lihat contoh *Test Case* untuk fitur Login berdasarkan empat kategori.

### a. Positive Cases ("Happy Path")

*Positive Cases* memvalidasi bahwa *user story* berfungsi seperti yang diharapkan ketika pengguna melakukan tindakan yang benar dan sistem merespons sesuai spesifikasi. Ini adalah skenario "jalan bahagia" di mana semuanya berjalan lancar. **Setiap *Acceptance Criteria* (AC) setidaknya membutuhkan satu *positive case*.**

**Contoh:**

```markdown
### TC-P-001: Pengguna terverifikasi berhasil login dan melihat dashboard
**Tipe:** Positive
**Linked Story:** US-001: Sebagai pengguna, saya ingin login ke aplikasi
**Linked AC:** AC1: Pengguna dapat login dengan email dan password yang valid.
**Prioritas:** P0
**Estimasi waktu:** 5 menit

**Preconditions:**
- Pengguna uji `tc001@thomas.local` sudah terdaftar, terverifikasi, dan memiliki password yang valid.
- Pengguna memiliki data dashboard 7 hari terakhir.

**Test data:**
- Email: `tc001@thomas.local`
- Password: `Password123!`

**Steps:**
1. Navigasi ke halaman `/login`.
2. Masukkan email `tc001@thomas.local` dan password `Password123!`.
3. Klik tombol "Sign In".

**Expected result:**
- Pengguna diarahkan ke halaman `/dashboard` dalam waktu 2 detik.
- Dashboard menampilkan 3 kartu data (Penggunaan, Tren, Anomali) yang terisi.
- Tidak ada *error* di konsol *browser*.
- *Auth cookie* terpasang dengan benar.
```

### b. Negative Cases (Input atau Alur yang Sengaja Salah)

*Negative Cases* memvalidasi bahwa sistem dapat menangani input yang salah, tidak valid, atau alur yang tidak diharapkan dengan aman dan anggun. Tujuannya adalah memastikan sistem tidak *crash*, tidak merusak data, dan memberikan pesan kesalahan yang jelas dan informatif.

**Contoh:**

```markdown
### TC-N-001: Login gagal dengan password yang salah
**Tipe:** Negative
**Linked Story:** US-001: Sebagai pengguna, saya ingin login ke aplikasi
**Linked AC:** AC1 (implisit: kebutuhan autentikasi yang aman)
**Prioritas:** P1
**Estimasi waktu:** 3 menit

**Preconditions:**
- Pengguna uji `tc001@thomas.local` sudah terdaftar dan terverifikasi.

**Test data:**
- Email: `tc001@thomas.local`
- Password: `salahpassword` (password yang salah)

**Steps:**
1. Navigasi ke halaman `/login`.
2. Masukkan email `tc001@thomas.local` (email benar) dan password `salahpassword` (password salah).
3. Klik tombol "Sign In".

**Expected result:**
- Pesan kesalahan generik "Email atau password tidak valid" ditampilkan di bawah form login.
- Pengguna TIDAK diarahkan ke halaman lain; tetap berada di halaman `/login`.
- Form tetap terisi dengan email (bukan password).
- Tidak ada *auth cookie* yang terpasang.
- Percobaan login dicatat untuk *rate limiting* (misalnya, setelah 5 kali percobaan gagal, akun dikunci 5 menit).
```

### c. Edge Cases (Kondisi Batasan atau Input Tak Biasa)

*Edge Cases* adalah skenario yang menguji kondisi batas, input yang tidak biasa tetapi valid, atau situasi yang jarang terjadi. Ini membantu menemukan *bug* yang mungkin terlewat oleh *positive* atau *negative cases* standar.

**Pola Umum Edge Cases:**
*   **Nilai Batas**: 0, 1, nilai maksimum - 1, nilai maksimum, nilai maksimum + 1.
*   **Input Kosong/Null/Sangat Panjang**: Apa yang terjadi jika *field* kosong, atau diisi dengan ribuan karakter?
*   **Karakter Khusus**: Unicode, emoji, bahasa RTL (Right-to-Left).
*   **Kondisi Jaringan**: Jaringan lambat (3G *throttling*).
*   **Aksi Bersamaan**: Membuka aplikasi di dua *tab browser* secara bersamaan.
*   **Waktu**: Tengah malam, pergantian waktu musim panas (DST), tahun kabisat.
*   **Batasan Izin**: Pengguna yang baru saja dicabut/diberikan izin.

**Contoh untuk Fitur Login:**

```markdown
### TC-E-001: Login dengan email yang mengandung tanda plus (alias email)
**Tipe:** Edge
**Linked Story:** US-001: Sebagai pengguna, saya ingin login ke aplikasi
**Linked AC:** AC1 (implisit: penanganan format email yang fleksibel)
**Prioritas:** P2
**Estimasi waktu:** 4 menit

**Preconditions:**
- Pengguna uji `tc001+alias@thomas.local` sudah terdaftar dan terverifikasi (alias email yang valid).

**Test data:**
- Email: `tc001+alias@thomas.local`
- Password: `Password123!`

**Steps:**
1. Navigasi ke halaman `/login`.
2. Masukkan email `tc001+alias@thomas.local` dan password `Password123!`.
3. Klik tombol "Sign In".

**Expected result:**
- Pengguna berhasil login dan diarahkan ke halaman `/dashboard`.
- Alias email ditangani dengan benar oleh sistem.

---

### TC-E-002: Login dengan password yang sangat panjang (256 karakter)
**Tipe:** Edge
**Linked Story:** US-001: Sebagai pengguna, saya ingin login ke aplikasi
**Linked AC:** AC1 (implisit: batasan input password)
**Prioritas:** P2
**Estimasi waktu:** 5 menit

**Preconditions:**
- Pengguna uji `tc002@thomas.local` sudah terdaftar dengan password 256 karakter yang valid.

**Test data:**
- Email: `tc002@thomas.local`
- Password: [password 256 karakter yang valid]

**Steps:**
1. Navigasi ke halaman `/login`.
2. Masukkan email `tc002@thomas.local` dan password yang sangat panjang.
3. Klik tombol "Sign In".

**Expected result:**
- Pengguna berhasil login dan diarahkan ke halaman `/dashboard`.
- Sistem menangani panjang password dengan benar tanpa *error* atau *truncation*.

---

### TC-E-003: Login dengan spasi di awal/akhir email
**Tipe:** Edge
**Linked Story:** US-001: Sebagai pengguna, saya ingin login ke aplikasi
**Linked AC:** AC1 (implisit: *trimming* spasi input)
**Prioritas:** P2
**Estimasi waktu:** 3 menit

**Preconditions:**
- Pengguna uji `tc003@thomas.local` sudah terdaftar.

**Test data:**
- Email: ` tc003@thomas.local ` (dengan spasi di awal dan akhir)
- Password: `Password123!`

**Steps:**
1. Navigasi ke halaman `/login`.
2. Masukkan email dengan spasi di awal/akhir dan password.
3. Klik tombol "Sign In".

**Expected result:**
- Sistem secara otomatis *trim* spasi di awal/akhir email.
- Pengguna berhasil login dan diarahkan ke halaman `/dashboard`.

---

### TC-E-004: Login dari negara baru (memicu geofencing)
**Tipe:** Edge
**Linked Story:** US-001: Sebagai pengguna, saya ingin login ke aplikasi
**Linked AC:** AC1 (implisit: keamanan akun)
**Prioritas:** P1
**Estimasi waktu:** 7 menit

**Preconditions:**
- Pengguna uji `tc004@thomas.local` belum pernah login dari lokasi geografis "Jerman".
- Sistem memiliki fitur deteksi login dari lokasi baru (geofencing) yang memerlukan verifikasi tambahan.

**Test data:**
- Email: `tc004@thomas.local`
- Password: `Password123!`
- IP Address: [IP Address dari Jerman, dapat disimulasikan dengan VPN/proxy]

**Steps:**
1. Navigasi ke halaman `/login` menggunakan VPN/proxy ke Jerman.
2. Masukkan email dan password.
3. Klik tombol "Sign In".

**Expected result:**
- Sistem mendeteksi login dari lokasi baru.
- Pengguna diminta untuk melakukan verifikasi tambahan (misal: kode OTP ke email/telepon).
- Email notifikasi "Login dari lokasi baru" terkirim ke email pengguna.
```

### d. Data Preparation (Persiapan Data Uji)

*Data Preparation* adalah *test case* itu sendiri, bukan hanya catatan di *precondition*. Ini adalah langkah-langkah yang diperlukan untuk membangun kondisi data yang spesifik untuk *test case* lain. Mengapa ini penting? Karena *setup* data bisa gagal, dan kegagalan ini perlu dilacak dan diperbaiki.

**Contoh:**

```markdown
### TC-DP-001: Seed pengguna uji standar dengan data dashboard 7 hari
**Tipe:** Data Preparation
**Linked Stories:** US-001, US-002, dst. (Beberapa kasus dashboard)
**Prioritas:** P0 (memblokir semua pengujian dashboard)
**Estimasi waktu:** 10 menit (satu kali)

**Preconditions:**
- Akses ke lingkungan development/staging.
- Script seeding data `scripts/seed_test_data.py` tersedia dan berfungsi.

**Steps:**
1. Jalankan *script* `scripts/seed_test_data.py --user tc001@thomas.local --days 7` di terminal.
2. Verifikasi di database PostgreSQL: `SELECT count(*) FROM events WHERE user_email='tc001@thomas.local';`

**Expected result:**
- Script keluar dengan kode 0 (berhasil).
- Jumlah *event* di PostgreSQL sesuai dengan yang diharapkan (biasanya 100-200 *event* tergantung konfigurasi *seed*).

---

### TC-DP-002: Siapkan pengguna dengan 2FA (Two-Factor Authentication) diaktifkan
**Tipe:** Data Preparation
**Linked Stories:** US-003: Sebagai pengguna, saya ingin mengaktifkan 2FA
**Prioritas:** P1
**Estimasi waktu:** 5 menit

**Preconditions:**
- Pengguna `tc002fa@thomas.local` sudah terdaftar.

**Steps:**
1. Login sebagai `tc002fa@thomas.local`.
2. Navigasi ke halaman Pengaturan Akun.
3. Aktifkan 2FA melalui aplikasi Authenticator.
4. Verifikasi dengan kode OTP.

**Expected result:**
- 2FA berhasil diaktifkan untuk akun `tc002fa@thomas.local`.
- Pengguna tidak dapat login tanpa kode 2FA.

---

### TC-DP-003: Siapkan pengguna yang terkunci (locked-out user)
**Tipe:** Data Preparation
**Linked Stories:** US-001 (implisit: keamanan login)
**Prioritas:** P1
**Estimasi waktu:** 3 menit

**Preconditions:**
- Pengguna `tc003locked@thomas.local` sudah terdaftar.

**Steps:**
1. Navigasi ke halaman `/login`.
2. Masukkan email `tc003locked@thomas.local` dan password yang salah sebanyak 5 kali berturut-turut.
3. Amati pesan kesalahan dan status akun.

**Expected result:**
- Setelah 5 percobaan gagal, akun `tc003locked@thomas.local` terkunci selama 5 menit.
- Pesan kesalahan yang sesuai ditampilkan ("Akun Anda sementara terkunci. Coba lagi dalam 5 menit.").
```

### Anti-Pola dalam Penulisan Test Case

Ada beberapa kebiasaan buruk yang harus Anda hindari saat menulis *test case*:

*   **"Uji bahwa login berfungsi"**: Terlalu samar. Selalu sebutkan AC yang tepat, langkah-langkah yang presisi, dan hasil yang diharapkan.
*   **Menggabungkan *positive* dan *negative case* dalam satu TC**: Pisahkan. Setiap *test case* harus fokus pada satu tujuan pengujian.
*   **Melewatkan *data preparation TC* dengan alasan "itu hanya *setup*"**: Jangan. *Setup* data bisa gagal, dan kegagalan itu perlu dilacak dan dipelihara.
*   **Tidak menyertakan estimasi waktu**: Diagram alur kerja Thomas secara eksplisit mewajibkan ini. PM membutuhkan ini untuk perencanaan.
*   **Tidak ada tautan ke AC**: *Test case* tanpa tautan ke *user story* atau AC adalah "tes yatim piatu". Ini mengalahkan tujuan utama QA untuk memverifikasi bahwa *Acceptance Criteria* terpenuhi.

---

## 3. Menyimpan dan Mengelola Test Case

Setelah Anda selesai menulis semua *test case* Anda, langkah berikutnya adalah menyimpannya di lokasi yang terorganisir dan mudah diakses. Di Thomas, kami menggunakan Notion sebagai sistem manajemen tugas dan dokumentasi utama kami.

### Penyimpanan di Notion

Setiap set *test case* untuk sebuah fitur disimpan sebagai sub-tugas di bawah PRD induk di Notion. Ini memungkinkan keterkaitan yang jelas antara persyaratan dan pengujian.

Anda bisa membuat tugas secara manual, atau jika Anda memiliki alat bantu, Anda bisa membuatnya secara programatik:

```python
from notion_connector import NotionTicketing # Asumsi ada modul ini
nt = NotionTicketing.from_env()

# Contoh membuat tugas untuk Test Case
nt.create_task(
    title=f"Test Cases: Fitur Login Pengguna",
    owner="qa-thomas",
    reporter="qa-thomas",
    priority="P1",
    source="QA",
    epic_id="<ID-Epic-Fitur-Login>", # ID Epic dari fitur Login
    labels=["test-cases"],
    body_markdown="<markdown-dari-semua-test-case-di-atas>", # Semua test case dalam satu dokumen markdown
)
```
**Catatan**: Dalam praktik, untuk *test case* yang sangat banyak, mungkin lebih praktis untuk membuat setiap *test case* sebagai tugas terpisah di Notion, dengan judul `TC-XXX: [Judul Test Case]`. Ini memungkinkan pelacakan status (Pass/Fail) per *test case* secara individual. Setiap tugas *test case* ini kemudian akan dilabeli `test-case` dan kategori spesifiknya (`positive`, `negative`, `edge`, `data-prep`), serta ditautkan ke *epic* fitur induk.

### Untuk Suite yang Lebih Besar: CSV di Google Drive

Untuk *suite* pengujian yang sangat besar (ratusan atau ribuan *test case*), menyimpan semuanya sebagai *body markdown* di satu tugas Notion mungkin kurang efisien untuk pelacakan individual. Dalam kasus ini, kami akan melampirkan file CSV di Google Drive (satu baris per *test case*) dan menautkan file tersebut dari tugas Notion.

### Format Kolom CSV Test Case Standar

Saat menggunakan CSV, pastikan Anda memiliki kolom standar ini untuk konsistensi dan kemudahan analisis:

| Kolom         | Deskripsi                                                                 | Contoh                                                    |
| :------------ | :------------------------------------------------------------------------ | :-------------------------------------------------------- |
| **TC ID**     | ID unik untuk *test case*.                                                | `TC-P-001`                                                |
| **Category**  | Kategori *test case* (Positive, Negative, Edge, Data Preparation).        | `Positive`                                                |
| **Title**     | Judul singkat dan deskriptif.                                             | `Login dengan kredensial valid`                           |
| **Pre-condition** | Kondisi yang harus terpenuhi sebelum *test case* dieksekusi.              | `Pengguna terdaftar`                                      |
| **Steps**     | Langkah-langkah detail untuk mengeksekusi *test case*.                    | `1. Navigasi ke /login; 2. Masukkan email & password; ...` |
| **Expected**  | Hasil yang diharapkan setelah langkah-langkah dieksekusi.                 | `Pengguna diarahkan ke /dashboard`                        |
| **Linked Story** | ID atau tautan ke *user story* yang terkait.                               | `US-001`                                                  |
| **Automatable** | Indikasi apakah *test case* ini kandidat untuk otomatisasi (Ya/Tidak).     | `Ya`                                                      |
| **Priority**  | Prioritas *test case* (P0, P1, P2, P3).                                   | `P0`                                                      |
| **Estimasi Waktu** | Estimasi waktu eksekusi *test case* dalam menit.                          | `5`                                                       |

Menggunakan format yang konsisten, baik di Notion maupun CSV, sangat penting untuk menjaga keteraturan dan mempermudah kolaborasi dalam tim QA.

---

## 4. Mengidentifikasi Kandidat Otomatisasi

Salah satu praktik terbaik dalam *Test Design* adalah mengidentifikasi *test case* mana yang menjadi kandidat kuat untuk otomatisasi **sejak awal**. Ini membantu Anda dan tim *engineering* merencanakan pengembangan *automation script* secara paralel dengan pengembangan fitur. Mengotomatisasi *test case* yang tepat dapat menghemat waktu dan sumber daya dalam jangka panjang, terutama untuk pengujian regresi.

Di Thomas, kami memiliki aturan standar untuk menentukan kandidat otomatisasi:

*   **Semua *test case* P0/P1 → Otomatisasi Wajib**
    *   *Test case* dengan prioritas P0 (Critical) dan P1 (High) adalah yang paling penting untuk memastikan fungsionalitas inti aplikasi. Kegagalan pada *test case* ini dapat menyebabkan dampak serius pada pengguna atau bisnis. Oleh karena itu, otomatisasi mereka adalah prioritas utama untuk memastikan stabilitas dan kualitas secara berkelanjutan.
    *   Contoh: Login, registrasi, pembayaran, membuat pesanan.

*   **P2 → Otomatisasi Bersyarat (jika *effort* rendah)**
    *   *Test case* P2 (Medium) memiliki tingkat kepentingan sedang. Otomatisasi mereka dipertimbangkan jika upaya yang dibutuhkan untuk menulis *automation script* relatif rendah. Ini bisa berarti *test case* tersebut sederhana, tidak memerlukan banyak *setup* data, atau menggunakan komponen yang sudah memiliki *helper function* otomatisasi.
    *   Contoh: Memperbarui profil pengguna, filter pencarian sederhana.

*   **P3 → Manual Saja (kecuali sangat trivial)**
    *   *Test case* P3 (Low) biasanya melibatkan fungsionalitas minor, *edge cases* yang sangat jarang, atau skenario yang membutuhkan interaksi manusia yang kompleks (misalnya, verifikasi visual yang sulit diotomatisasi). Umumnya, *test case* ini akan tetap diuji secara manual. Pengecualian adalah jika *test case* tersebut sangat trivial dan dapat diotomatisasi dengan sedikit atau tanpa *effort* tambahan.
    *   Contoh: Mengubah tema aplikasi, memeriksa *tooltip* kecil.

### Proses Penyerahan Kandidat Otomatisasi

Setelah Anda mengidentifikasi *test case* mana yang akan diotomatisasi, Anda perlu menyerahkan daftar ini kepada tim *engineering*. Di Thomas, ini dilakukan dalam sebuah *ticket* terpisah di Notion dengan label `automation-pending`. *Ticket* ini akan berisi daftar ID *test case* yang ditargetkan untuk otomatisasi, serta tautan ke *test case* aslinya.

**Contoh *Ticket* Notion untuk Otomatisasi:**

```markdown
# Otomatisasi Test Case: Fitur Login Pengguna

**Owner:** <Nama Developer Otomatisasi>
**Reporter:** qa-thomas
**Labels:** `automation-pending`, `feature-login`
**Linked Epic:** <ID-Epic-Fitur-Login>

**Deskripsi:**
Berikut adalah daftar test case untuk fitur Login Pengguna yang diidentifikasi sebagai kandidat otomatisasi. Mohon untuk dipertimbangkan dalam sprint automation berikutnya.

**Daftar Test Case untuk Otomatisasi:**
- TC-P-001: Pengguna terverifikasi berhasil login dan melihat dashboard
  - Prioritas: P0
  - Tautan TC: [Link ke Notion TC-P-001]
- TC-N-001: Login gagal dengan password yang salah
  - Prioritas: P1
  - Tautan TC: [Link ke Notion TC-N-001]
- TC-E-004: Login dari negara baru (memicu geofencing)
  - Prioritas: P1
  - Tautan TC: [Link ke Notion TC-E-004]
- TC-DP-001: Seed pengguna uji standar dengan data dashboard 7 hari
  - Prioritas: P0
  - Tautan TC: [Link ke Notion TC-DP-001]

**Catatan:**
Prioritas P0/P1 wajib diotomatisasi. TC P2/P3 akan diuji manual kecuali ada waktu dan effort minimal.

Terima kasih.
```

Dengan mengidentifikasi kandidat otomatisasi di tahap *Test Design*, Anda tidak hanya membantu memastikan cakupan pengujian yang efisien, tetapi juga mendorong mentalitas "otomatisasi terlebih dahulu" dalam tim, yang pada akhirnya akan mempercepat siklus rilis dan meningkatkan kualitas produk secara keseluruhan.

---

## 5. Gerbang Menuju Eksekusi (Gate to Test Execution)

Selamat! Anda telah melalui proses *Test Design* yang komprehensif. Sebelum kita melangkah ke bab berikutnya, yaitu *Test Execution*, penting untuk diingat bahwa *Test Design* adalah sebuah gerbang. Ada beberapa kriteria yang harus dipenuhi sebelum Anda dapat secara resmi memulai fase eksekusi pengujian. Ini memastikan bahwa Anda memulai pengujian dengan fondasi yang kokoh dan mengurangi risiko pemborosan waktu.

Berikut adalah *checklist* yang harus Anda pastikan terpenuhi:

*   **[ ] Dokumen *Test Strategy* telah disetujui:**
    *   Ini berarti *scope*, pendekatan, lingkungan, serta *entry* dan *exit criteria* telah disepakati oleh semua *stakeholder* terkait (PM, Tech Lead, dll.).
    *   Pastikan tidak ada pertanyaan atau keberatan yang belum terselesaikan mengenai rencana pengujian Anda.

*   **[ ] Keempat kategori *test case* telah lengkap:**
    *   Pastikan Anda telah menulis *test case* untuk *Positive Cases*, *Negative Cases*, *Edge Cases*, dan *Data Preparation*.
    *   Jangan ada kategori yang terlewat, karena setiap kategori memiliki perannya masing-masing dalam memastikan cakupan pengujian yang menyeluruh.

*   **[ ] Estimasi waktu telah ditinjau dan disetujui oleh PM/Tech Lead:**
    *   Estimasi waktu yang Anda buat dalam *Test Strategy* dan per *test case* harus sudah ditinjau dan disetujui oleh Project Manager dan/atau Tech Lead.
    *   Ini penting untuk perencanaan *sprint* dan alokasi sumber daya. Jika ada perbedaan, diskusikan hingga mencapai kesepakatan.

*   **[ ] Rencana persiapan data uji sudah siap:**
    *   Anda harus memiliki pemahaman yang jelas tentang bagaimana data yang dibutuhkan untuk setiap *test case* akan disiapkan.
    *   Apakah itu melalui *script seeding*, pembuatan manual, atau melalui API? Pastikan semua metode sudah jelas dan siap dieksekusi.

*   **[ ] Kandidat otomatisasi telah diidentifikasi dan dikomunikasikan:**
    *   Daftar *test case* yang menjadi kandidat untuk otomatisasi telah Anda tentukan dan diserahkan kepada tim *engineering* (misalnya, melalui *ticket* Notion).
    *   Ini memastikan bahwa tim *development* dapat mulai merencanakan atau bahkan memulai pengembangan *automation script* secara paralel.

Memenuhi semua kriteria ini adalah tanda bahwa Anda siap untuk beralih ke fase *Test Execution* dengan kepercayaan diri dan efisiensi. Anda telah melakukan pekerjaan rumah Anda, dan sekarang saatnya untuk melihat bagaimana aplikasi benar-benar bekerja!

---

## Rangkuman

Bab ini telah membawa Anda melampaui analisis persyaratan dan masuk ke jantungnya peran QA: *Test Design*. Kita telah mempelajari bahwa menjadi QA Engineer bukan sekadar "klik-klik tombol", melainkan merancang sebuah strategi yang kokoh untuk memastikan kualitas.

Berikut poin-poin penting yang Anda pelajari:

*   **Test Strategy**: Anda kini memahami pentingnya *Test Strategy* sebagai peta jalan pengujian, yang mencakup *scope*, pendekatan, lingkungan, *entry/exit criteria*, estimasi waktu, dan manajemen risiko. Dokumen ini adalah jembatan komunikasi antara QA dan *stakeholder* lainnya.
*   **Estimasi Waktu**: Anda belajar cara menyusun estimasi waktu yang realistis untuk setiap fase pengujian, termasuk *buffer*, dan mengapa ini krusial untuk perencanaan proyek. Estimasi ini harus ada di *Test Strategy* dan juga per *test case*.
*   **Empat Kategori Test Case**: Anda telah menguasai empat pilar *Test Case* – *Positive*, *Negative*, *Edge*, dan *Data Preparation* – lengkap dengan contoh konkret untuk fitur login. Memastikan cakupan di keempat kategori ini akan memberikan Anda kepercayaan diri yang lebih besar terhadap kualitas produk.
*   **Format dan Penyimpanan Test Case**: Anda kini tahu bagaimana menyimpan *test case* secara terorganisir di Notion atau CSV, menggunakan format standar yang memudahkan pelacakan dan kolaborasi.
*   **Kandidat Otomatisasi**: Anda telah belajar cara mengidentifikasi *test case* mana yang menjadi kandidat utama untuk otomatisasi (P0/P1 wajib, P2 kondisional, P3 manual), sebuah langkah proaktif yang menghemat waktu dan sumber daya di masa depan.
*   **Quality Gate**: Anda memahami bahwa *Test Design* adalah *Quality Gate* yang krusial. Memastikan semua kriteria *Test Design* terpenuhi sebelum masuk ke *Test Execution* akan menghemat banyak masalah di kemudian hari.

Dengan bekal *Test Design* ini, Anda tidak hanya siap untuk menguji, tetapi juga untuk memimpin inisiatif kualitas dalam tim Anda. Anda telah mengubah persyaratan abstrak menjadi rencana pengujian yang konkret dan dapat dieksekusi.

---

## Checklist Actionable

Berikut adalah daftar langkah-langkah yang dapat Anda terapkan segera setelah membaca bab ini:

*   [ ] **Buat *template Test Strategy*** di Notion atau alat manajemen proyek pilihan Anda, berdasarkan *template* yang telah diberikan.
*   [ ] **Pilih satu fitur yang sedang atau akan dikembangkan** di proyek Anda.
*   [ ] **Susun *Test Strategy* lengkap** untuk fitur tersebut, isi setiap bagian: *Scope*, *Approach*, *Environments*, *Entry/Exit Criteria*, *Estimasi Waktu*, dan *Risks*.
*   [ ] **Lakukan estimasi waktu secara detail** untuk setiap komponen dalam *Test Strategy* Anda (penyusunan TC, eksekusi, regresi, dll.), dan pastikan ada *buffer* 20%.
*   [ ] **Mulai tulis *Test Case* untuk fitur tersebut**, pastikan Anda mencakup keempat kategori: *Positive*, *Negative*, *Edge*, dan *Data Preparation*. Gunakan fitur Login sebagai inspirasi.
*   [ ] **Sertakan estimasi waktu (dalam menit) untuk setiap *test case*** yang Anda buat.
*   [ ] **Pastikan setiap *test case* tertaut ke *User Story* dan *Acceptance Criteria*** yang relevan.
*   [ ] **Identifikasi kandidat otomatisasi** untuk *test case* yang baru Anda buat, tandai P0/P1 sebagai wajib otomatisasi.
*   [ ] **Simpan *test case* Anda di Notion** (sebagai tugas terpisah atau *body markdown* di tugas induk) atau dalam format CSV standar.
*   [ ] **Presentasikan *Test Strategy* dan *Test Case* Anda** kepada PM dan Tech Lead untuk mendapatkan *feedback* dan persetujuan, pastikan semua *Entry Criteria* terpenuhi sebelum melangkah ke *Test Execution*.
