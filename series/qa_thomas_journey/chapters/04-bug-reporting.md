Tentu, mari kita mulai menulis Chapter 04 dari buku "Journey QA Thomas".

---

# Chapter 04: Bug Reporting — Severity, Template, dan Eskalasi

Selamat datang kembali dalam perjalanan Anda menjadi seorang Quality Assurance Engineer! Jika di bab sebelumnya kita sudah belajar bagaimana merancang strategi dan *test case* yang solid, maka di bab ini kita akan membahas salah satu momen paling krusial dan sering disalahpahami dalam siklus pengembangan: pelaporan *bug*.

Bagi sebagian orang, menemukan *bug* mungkin terasa seperti memenangkan lotre, tetapi bagi seorang QA Engineer profesional, menemukan *bug* hanyalah setengah dari pertempuran. Pertempuran sesungguhnya adalah bagaimana Anda mengomunikasikan *bug* tersebut secara efektif agar dapat dipahami, direproduksi, dan diperbaiki oleh tim *engineer*. Laporan *bug* yang baik bukan sekadar daftar masalah, melainkan peta jalan yang jelas bagi *developer* untuk menemukan akar masalah dan menyelesaikannya dengan efisien. Ingatlah *prime directive* QA Thomas: memverifikasi bahwa setiap alur yang diimplementasikan sesuai dengan *acceptance criteria* *user story*. Setiap penyimpangan dari kriteria tersebut, bahkan jika kodenya tidak *crash*, adalah sebuah *defect* yang harus dilaporkan.

Di bab ini, Anda akan belajar cara membuat laporan *bug* yang *actionable*, memahami skala prioritas *severity* (P0-P3), hingga alur eskalasi yang tepat agar *bug* Anda mendapatkan perhatian yang sesuai. Mari kita mulai!

## Anatomi Laporan Bug yang Efektif: Lebih dari Sekadar "Ini Rusak"

Sebuah laporan *bug* yang baik adalah jembatan komunikasi antara QA dan *developer*. Ia harus ringkas, jelas, dan memberikan semua informasi yang dibutuhkan agar *developer* dapat mereproduksi masalah dan memperbaikinya tanpa harus bolak-balik bertanya. Di Thomas, kami memiliki standar *template* laporan *bug* yang memandu Anda untuk mengisi setiap detail penting.

Mari kita bedah setiap komponen dari *template* laporan *bug* standar:

```markdown
# [<area>] <one-line summary>

**Severity**: P0 | P1 | P2 | P3
**Reporter**: qa-thomas
**Environment**: <build version, browser, OS, device>
**Reproducible**: Always | Intermittent | Once | Cannot reproduce
**Linked story**: <Notion task ID>

## Steps to Reproduce
1. ...
2. ...
3. ...

## Expected
<what should happen>

## Actual
<what actually happens>

## Evidence
- Screenshot: <Drive link>
- Video: <Drive link>
- Console log: <paste or link>
- Network log: <paste or link>

## Impact
- Users affected: <all | specific cohort | edge case>
- Workaround: <if any>
- Frequency: <X per Y users/sessions>

## Notes / hypothesis
<any pointers for the engineer who'll pick this up>
```

Mari kita lihat mengapa setiap bagian ini penting:

### 1. Judul (`Title`)
`[<area>] <one-line summary>`

Judul adalah kesan pertama. Ia harus singkat, deskriptif, dan langsung menunjukkan inti masalah serta area fungsional yang terpengaruh.
*   **`<area>`**: Bagian mana dari aplikasi yang terpengaruh (misalnya: `[Login]`, `[Search Page]`, `[Checkout]`, `[User Profile]`). Ini membantu *developer* dengan cepat mengetahui tim atau bagian kode mana yang kemungkinan besar bertanggung jawab.
*   **`<one-line summary>`**: Ringkasan masalah dalam satu baris. Hindari kalimat yang terlalu umum seperti "Bug di halaman X". Lebih spesifik seperti "Validasi email tidak berfungsi" atau "Tombol 'Tambah ke Keranjang' tidak responsif".

**Contoh Judul yang Baik:**
*   `[Login] Pengguna tidak bisa masuk dengan kredensial yang benar`
*   `[Search Page] Filter harga tidak mengembalikan hasil yang relevan`
*   `[Checkout] Total harga tidak terupdate setelah menghapus item`
*   `[User Profile] Avatar pengguna tidak tampil di profil`

**Contoh Judul yang Buruk:**
*   `[Bug] Halaman error` (Terlalu umum)
*   `Login rusak` (Tidak ada area spesifik, terlalu informal)
*   `Masalah di fitur baru` (Tidak deskriptif sama sekali)

### 2. Severity
`P0 | P1 | P2 | P3`

Ini adalah indikator seberapa parah dampak *bug* terhadap pengguna atau sistem. Kita akan membahas rubrik *severity* ini secara mendalam di bagian selanjutnya, tetapi penting untuk menentukannya sejak awal.

### 3. Reporter
`qa-thomas`

Siapa yang melaporkan *bug* ini? Ini penting untuk komunikasi jika *developer* membutuhkan klarifikasi lebih lanjut. Di Thomas, kami menggunakan `qa-thomas` sebagai identitas standar.

### 4. Environment
`<build version, browser, OS, device>`

Informasi ini krusial untuk mereplikasi *bug*. Sebuah *bug* bisa saja muncul di satu *environment* (misalnya Chrome di Windows 10) tetapi tidak di *environment* lain (misalnya Firefox di macOS).
*   **`build version`**: Versi *build* aplikasi yang Anda uji. Ini penting karena *bug* mungkin sudah diperbaiki di *build* yang lebih baru, atau baru muncul di *build* tertentu.
*   **`browser`**: Peramban web yang digunakan (Chrome, Firefox, Safari, Edge).
*   **`OS`**: Sistem Operasi (Windows 10, macOS Ventura, Android 13, iOS 16).
*   **`device`**: Perangkat yang digunakan (Desktop, iPhone 14, Samsung Galaxy S23, iPad Pro).

**Contoh:** `Staging v1.2.3, Chrome 115, macOS Ventura, Desktop` atau `Dev v2.0.0, Safari, iOS 16, iPhone 14 Pro`

### 5. Reproducible
`Always | Intermittent | Once | Cannot reproduce`

Seberapa sering *bug* ini muncul?
*   **`Always`**: *Bug* selalu terjadi setiap kali Anda mengikuti langkah-langkah reproduksi. Ini adalah skenario terbaik bagi *developer*.
*   **`Intermittent`**: *Bug* terjadi kadang-kadang, tidak setiap saat, meskipun langkah-langkahnya sama. Ini lebih sulit untuk di-debug, jadi berikan detail sebanyak mungkin.
*   **`Once`**: *Bug* hanya terjadi sekali dan Anda tidak dapat mereproduksinya lagi. Laporkan ini dengan hati-hati dan berikan konteks penuh.
*   **`Cannot reproduce`**: Anda mencoba mereproduksi *bug* yang dilaporkan oleh orang lain atau yang Anda lihat sekilas, tetapi tidak berhasil. Ini penting untuk dicatat agar tidak membuang waktu.

### 6. Linked Story
`<Notion task ID>`

Setiap *test case* harus dapat dilacak kembali ke *user story* yang diujinya. Demikian pula, setiap *bug* idealnya harus dapat dilacak kembali ke *user story* yang gagal dipenuhi *acceptance criteria*-nya. Ini menunjukkan bahwa *bug* tersebut adalah penyimpangan dari perilaku yang diharapkan berdasarkan spesifikasi.

### 7. Steps to Reproduce (Langkah-langkah Reproduksi)
Ini adalah bagian paling vital dari laporan *bug*. Jelaskan langkah-langkah secara berurutan, jelas, dan sespesifik mungkin agar siapa pun dapat mengikuti dan melihat *bug* yang sama.
*   Gunakan daftar bernomor.
*   Setiap langkah harus *actionable* (misalnya: "Klik tombol X", "Masukkan teks Y", "Navigasi ke halaman Z").
*   Sertakan data *test* yang digunakan jika relevan (misalnya: "Login dengan `user: thomas@example.com`, `password: thomas123`").

**Contoh Langkah-langkah Reproduksi yang Baik:**
1.  Buka aplikasi di browser Chrome (v115).
2.  Navigasi ke halaman Login (`https://app.thomas.com/login`).
3.  Masukkan email: `invalid@example.com`.
4.  Masukkan password: `password123`.
5.  Klik tombol "Masuk".

### 8. Expected (Yang Diharapkan)
Jelaskan apa yang seharusnya terjadi jika aplikasi berfungsi dengan benar, sesuai dengan *acceptance criteria* *user story*.

**Contoh:**
*   *Expected*: Sistem menampilkan pesan error "Email atau password salah." di bawah kolom email.
*   *Expected*: Halaman *search result* menampilkan produk yang harganya antara Rp 50.000 - Rp 100.000, diurutkan dari harga terendah.

### 9. Actual (Yang Terjadi)
Jelaskan apa yang sebenarnya terjadi, yang merupakan penyimpangan dari perilaku yang diharapkan. Ini adalah deskripsi *bug* itu sendiri.

**Contoh:**
*   *Actual*: Sistem menampilkan pesan error "Terjadi kesalahan. Silakan coba lagi." di bagian atas halaman, dan tidak ada pesan spesifik di bawah kolom email.
*   *Actual*: Halaman *search result* menampilkan produk dengan harga di atas Rp 100.000, dan urutan harga tidak konsisten.

### 10. Evidence (Bukti)
Sertakan bukti visual atau log teknis yang mendukung laporan *bug* Anda. Ini sangat membantu *developer* untuk memahami konteks dan mempercepat proses *debugging*.
*   **Screenshot**: Untuk *bug* visual (UI/UX).
*   **Video**: Sangat berguna untuk *bug* yang melibatkan interaksi kompleks, animasi, atau yang *intermittent*.
*   **Console log**: Pesan error atau peringatan dari *browser console* atau log aplikasi.
*   **Network log**: Permintaan dan respons API yang gagal atau tidak sesuai (dari tab Network di *developer tools*).

**Tips:** Selalu simpan bukti di lokasi yang mudah diakses dan dibagikan, seperti Google Drive, dan pastikan tautannya dapat diakses oleh tim.

### 11. Impact (Dampak)
Bagian ini membantu tim memahami urgensi dan prioritas *bug* dari perspektif bisnis atau pengguna.
*   **`Users affected`**: Siapa yang terpengaruh (semua pengguna, kohort spesifik, *edge case*).
*   **`Workaround`**: Jika ada cara bagi pengguna untuk menghindari *bug* tersebut (misalnya, "pengguna bisa menggunakan fitur X sebagai gantinya").
*   **`Frequency`**: Seberapa sering *bug* ini terjadi pada pengguna (misalnya, "terjadi pada 1 dari 100 sesi pengguna").

### 12. Notes / Hypothesis (Catatan / Hipotesis)
Ruang untuk menambahkan konteks tambahan, pengamatan, atau dugaan awal Anda tentang penyebab *bug*. Ini bisa menjadi petunjuk berharga bagi *developer*.

---

**Contoh Laporan Bug Lengkap:**

```markdown
# [Login] Pengguna tidak bisa masuk dengan kredensial yang benar

**Severity**: P1
**Reporter**: qa-thomas
**Environment**: Staging v1.2.3, Chrome 115.0.5790.170, macOS Ventura 13.5, Desktop
**Reproducible**: Always
**Linked story**: TSK-1234 (Sebagai pengguna, saya bisa login ke akun saya)

## Steps to Reproduce
1. Buka browser Chrome (v115).
2. Navigasi ke halaman Login (`https://staging.thomas.com/login`).
3. Masukkan email: `user@example.com` (kredensial yang valid).
4. Masukkan password: `password123` (kredensial yang valid).
5. Klik tombol "Masuk".

## Expected
Pengguna berhasil masuk ke aplikasi dan diarahkan ke halaman Dashboard.

## Actual
Setelah mengklik tombol "Masuk", halaman tidak merespons. Tidak ada pesan error yang muncul di UI.
Di console browser, terlihat error 500 dari endpoint `/api/auth/login`.

## Evidence
- Screenshot: [https://drive.google.com/link-ke-screenshot-error.png](https://drive.google.com/link-ke-screenshot-error.png)
- Video: [https://drive.google.com/link-ke-video-repro.mp4](https://drive.google.com/link-ke-video-repro.mp4)
- Console log:
  ```
  POST https://staging.thomas.com/api/auth/login 500 (Internal Server Error)
  Error: Request failed with status code 500
      at createError (createError.js:16:1)
      at settle (settle.js:17:1)
      at XMLHttpRequest.onloadend (xhr.js:66:1)
  ```
- Network log: [https://drive.google.com/link-ke-network-log.har](https://drive.google.com/link-ke-network-log.har)

## Impact
- Users affected: Semua pengguna yang mencoba login di lingkungan Staging.
- Workaround: Tidak ada. Pengguna tidak bisa mengakses aplikasi.
- Frequency: Terjadi pada setiap percobaan login dengan kredensial valid.

## Notes / hypothesis
Diduga ada masalah di sisi backend saat memproses permintaan login atau koneksi ke database autentikasi.
```

Dengan laporan seperti ini, *developer* dapat dengan cepat memahami masalah, mereproduksinya, dan mulai mencari solusinya tanpa banyak pertanyaan.

## Rubrik Severity: Mengukur Dampak Bug dan Menentukan Prioritas

Menentukan *severity* (tingkat keparahan) *bug* adalah salah satu tugas terpenting seorang QA. Ini bukan hanya tentang seberapa "rusak" sesuatu, tetapi lebih kepada seberapa besar *dampak* kerusakan tersebut terhadap pengguna, bisnis, dan keseluruhan sistem. Thomas menggunakan rubrik *severity* P0 hingga P3 untuk mengklasifikasikan *bug*:

| Level | Kriteria | Contoh Nyata | Alur Eskalasi Slack |
|---|---|---|---|
| **P0** | **Kritis / Blocker**: Produksi *down* (tidak bisa diakses), kehilangan data, pelanggaran keamanan, memblokir semua pengguna dari penggunaan fitur inti atau keseluruhan aplikasi. | Login tidak berfungsi sama sekali, pembayaran gagal total, data pengguna terhapus, aplikasi *crash* terus-menerus. | `#incidents` + DM Tech Lead |
| **P1** | **Tinggi**: Fitur inti rusak untuk banyak pengguna, tidak ada *workaround* yang mudah. Meskipun aplikasi bisa diakses, fungsionalitas utama tidak berjalan. | Fitur pencarian mengembalikan error 500, proses pendaftaran pengguna *intermittent* (kadang berhasil, kadang tidak), fitur *upload* gambar rusak. | `#incidents` + DM Tech Lead |
| **P2** | **Sedang**: Fitur terganggu tetapi ada *workaround* atau hanya mempengaruhi sebagian kecil fungsionalitas/pengguna. Pengguna masih bisa menyelesaikan tugasnya meskipun dengan sedikit kesulitan. | Urutan *sort* hasil pencarian salah, *typo* besar di UI yang penting, notifikasi tidak muncul tepat waktu, *bug* di fitur non-inti. | `#qa` |
| **P3** | **Rendah / Kosmetik**: Masalah visual minor, ketidaknyamanan kecil, *bug* di *edge case* yang jarang terjadi. Tidak menghalangi fungsionalitas inti. | Piksel tidak sejajar, warna teks sedikit berbeda, *placeholder* yang tidak tepat, *bug* di *tooltip* yang jarang diakses. | Notion saja |

**Penting:**
*   **P0 dan P1** biasanya memerlukan perhatian segera karena berdampak langsung pada pengalaman pengguna dan potensi kerugian bisnis.
*   **P2** masih penting untuk diperbaiki, tetapi tidak mendesak seperti P0/P1.
*   **P3** seringkali dapat ditempatkan di *backlog* dan diperbaiki di siklus pengembangan berikutnya atau saat ada waktu luang.

Pemahaman yang jelas tentang *severity* ini akan membantu Anda membuat keputusan yang tepat tentang seberapa cepat dan seberapa luas Anda perlu mengeskalasikan *bug* yang ditemukan.

## Alur Eskalasi Bug: Dari Penemuan hingga Perbaikan

Menemukan *bug* dan menuliskannya dalam *ticket* hanyalah langkah pertama. Langkah berikutnya adalah memastikan *bug* tersebut sampai ke tangan yang tepat dengan urgensi yang sesuai. Di Thomas, kami memiliki alur eskalasi yang jelas berdasarkan tingkat *severity* *bug*:

1.  **Semua Bug**: Setiap *bug* yang dilaporkan, tidak peduli *severity*-nya, akan dibuatkan *ticket* di Notion (database *bug* kami).
2.  **Visibilitas Terpusat**: Selain di Notion, semua *bug* juga akan diposting ke *channel* Slack `#qa-reports` untuk visibilitas terpusat bagi seluruh tim. Ini memastikan semua *stakeholder* dapat melihat *bug* yang ditemukan.

Berikut adalah alur eskalasi spesifik berdasarkan *severity*:

*   **P0 / P1 (Kritis & Tinggi)**:
    *   Buat *ticket* *bug* di Notion.
    *   Segera posting ke *channel* Slack `#incidents`. *Channel* ini khusus untuk masalah-masalah mendesak yang membutuhkan perhatian tim secepatnya.
    *   DM (Direct Message) Tech Lead tim terkait. Ini memastikan pemimpin teknis segera menyadari masalah dan dapat mengalokasikan sumber daya untuk perbaikan.

*   **P2 (Sedang)**:
    *   Buat *ticket* *bug* di Notion.
    *   Posting ke *channel* Slack `#qa`. Ini adalah *channel* umum untuk diskusi QA dan laporan *bug* yang tidak terlalu mendesak.

*   **P3 (Rendah / Kosmetik)**:
    *   Cukup buat *ticket* *bug* di Notion saja.
    *   *Bug* ini akan muncul dalam tinjauan *backlog* berikutnya dan akan dipertimbangkan untuk perbaikan di masa mendatang. Tidak perlu notifikasi Slack langsung.

**Mengapa Alur Eskalasi Berbeda?**
Tujuan dari alur eskalasi yang berbeda ini adalah untuk:
*   **Meningkatkan Efisiensi**: Hanya masalah yang paling mendesak yang mengganggu *workflow* tim dengan notifikasi langsung.
*   **Memastikan Prioritas**: *Bug* P0/P1 mendapatkan perhatian instan karena dampaknya yang besar.
*   **Mengurangi Kebisingan**: Tim *developer* tidak terbebani oleh notifikasi untuk *bug* minor, memungkinkan mereka fokus pada pekerjaan yang lebih penting.

### Otomatisasi Routing dengan `qa_report_bug.py`

Untuk menyederhanakan proses pelaporan dan memastikan alur eskalasi diikuti dengan benar, Thomas menggunakan *script* otomatis `qa_report_bug.py`. *Script* ini terintegrasi dengan Notion dan Slack, sehingga Anda tidak perlu melakukan langkah-langkah manual untuk setiap *bug*.

**Bagaimana Cara Kerjanya (Konseptual):**

Ketika Anda menemukan *bug* dan ingin melaporkannya, alih-alih membuka Notion dan Slack secara manual, Anda akan menjalankan *script* ini dan memberikan informasi *bug* yang diperlukan.

```bash
# Contoh penggunaan script (konseptual)
python scripts/qa_report_bug.py \
    --title "[Login] Pengguna tidak bisa masuk" \
    --severity P1 \
    --environment "Staging v1.2.3, Chrome, macOS" \
    --reproducible Always \
    --steps "1. Buka login; 2. Masukkan kredensial; 3. Klik masuk" \
    --expected "Masuk dashboard" \
    --actual "Halaman tidak merespons, error 500" \
    --evidence "link-ke-bukti.png" \
    --linked_story TSK-1234
```

*Script* ini kemudian akan:
1.  Membuat *ticket* *bug* baru di database Notion dengan semua detail yang Anda berikan.
2.  Berdasarkan `severity` yang Anda tentukan, *script* akan secara otomatis:
    *   Jika P0/P1: Memposting notifikasi ke `#incidents` Slack dan mengirim DM ke Tech Lead.
    *   Jika P2: Memposting notifikasi ke `#qa` Slack.
    *   Jika P3: Tidak melakukan notifikasi Slack tambahan (hanya Notion).
3.  Memposting ringkasan *bug* ke *channel* Slack `#qa-reports` untuk visibilitas umum.

Dengan otomatisasi ini, proses pelaporan menjadi lebih cepat, konsisten, dan meminimalkan kesalahan manusia dalam mengikuti alur eskalasi. Ini adalah contoh bagaimana seorang QA Engineer modern memanfaatkan *tool* untuk meningkatkan efisiensi.

## Kapan TIDAK Perlu Melaporkan Bug?

Tidak semua masalah atau pengamatan yang Anda temukan harus dilaporkan sebagai *bug*. Terkadang, apa yang terlihat seperti *bug* sebenarnya adalah sesuatu yang lain. Melaporkan hal-hal yang bukan *bug* hanya akan menambah *noise* di *backlog* dan membuang waktu *developer*. Berikut adalah beberapa skenario kapan Anda sebaiknya tidak membuat *ticket* *bug*:

1.  **Itu adalah Permintaan Fitur Baru (Feature Request)**
    *   **Skenario**: Anda melihat bahwa aplikasi tidak memiliki fitur "ekspor data ke Excel" dan Anda berpikir itu akan sangat berguna.
    *   **Mengapa Bukan Bug**: Aplikasi tidak memiliki fitur tersebut bukan berarti ada yang rusak. Itu adalah fitur yang belum ada.
    *   **Tindakan**: Komunikasikan ide ini kepada Product Manager (PM). PM akan mengevaluasinya sebagai potensi fitur baru untuk dipertimbangkan dalam *roadmap* produk. Jangan membuat *bug ticket*.

2.  **Kesalahpahaman Perilaku yang Diharapkan (Misunderstanding of Expected Behavior)**
    *   **Skenario**: Anda berpikir bahwa mengklik tombol "Simpan" harusnya mengarahkan Anda ke halaman lain, tetapi ternyata hanya menyimpan data di halaman yang sama. Setelah bertanya ke PM atau *developer*, ternyata memang begitulah desainnya.
    *   **Mengapa Bukan Bug**: Perilaku yang Anda harapkan berbeda dengan desain yang sebenarnya. Tidak ada yang rusak, hanya ada perbedaan pemahaman.
    *   **Tindakan**: Klarifikasi dan selesaikan kesalahpahaman ini di Slack atau dalam rapat tim. Update pemahaman Anda tentang *acceptance criteria*. Jika perlu, update *test case* Anda.

3.  **Tidak Dapat Direproduksi Setelah 2 Kali Percobaan (Can't Reproduce 2x)**
    *   **Skenario**: Anda melihat sekilas sebuah anomali (misalnya, teks berkedip sebentar atau halaman *loading* sangat lama), tetapi setelah mencoba mereproduksinya dua kali dengan langkah yang sama, *bug* tersebut tidak muncul lagi.
    *   **Mengapa Bukan Bug (untuk dilaporkan sebagai P0/P1)**: *Bug* yang tidak dapat direproduksi sangat sulit, bahkan mustahil, untuk di-debug. Melaporkannya sebagai *bug* prioritas tinggi akan membuang waktu *developer*.
    *   **Tindakan**: Jika Anda yakin ada sesuatu yang terjadi tetapi tidak dapat mereproduksinya, Anda bisa membuat *ticket* *bug* dengan `Reproducible = Cannot reproduce` atau `Once`. Namun, pastikan untuk memberi catatan di judul atau deskripsi bahwa ini mungkin *noise* atau *edge case* yang sangat langka. Jangan mengeskalasikannya sebagai *bug* P0/P1 yang mendesak.

Dengan memahami kapan tidak perlu melaporkan *bug*, Anda membantu menjaga *backlog* tetap bersih dan relevan, sehingga tim dapat fokus pada masalah nyata yang membutuhkan perhatian.

## Anti-Pattern: Batch Filing di Akhir Siklus vs. File as You Find

Salah satu kesalahan umum yang sering dilakukan oleh QA yang kurang berpengalaman adalah menunda pelaporan *bug*. Mereka mungkin menunggu hingga akhir siklus *testing* atau hingga mereka menemukan "cukup banyak" *bug* sebelum mulai membuat *ticket*. Ini dikenal sebagai **Batch Filing di Akhir Siklus** dan merupakan *anti-pattern* yang merugikan.

### Anti-Pattern: Batch Filing di Akhir Siklus

*   **Apa itu**: Menemukan *bug* sepanjang hari/minggu, mencatatnya secara pribadi (misalnya di notepad), dan baru membuat *ticket* *bug* untuk semuanya sekaligus di akhir hari atau akhir siklus.
*   **Dampak Negatif**:
    *   **Feedback Loop Lambat**: *Developer* tidak mendapatkan *feedback* segera. *Bug* yang ditemukan pagi hari baru diketahui *developer* sore hari atau keesokan harinya, menunda perbaikan.
    *   **Context Switching Tinggi**: *Developer* mungkin sudah beralih ke tugas lain. Ketika mereka mendapatkan laporan *bug* dari fitur yang mereka kerjakan kemarin, mereka harus mengalihkan konteks kembali ke pekerjaan sebelumnya.
    *   **Informasi Hilang**: Semakin lama Anda menunda pelaporan, semakin besar kemungkinan Anda melupakan detail penting, konteks, atau langkah-langkah reproduksi yang spesifik.
    *   **Crunch di Akhir**: Anda akan terburu-buru membuat banyak *ticket* *bug* di akhir, meningkatkan risiko kesalahan ketik, detail yang kurang, atau *bug* yang tidak lengkap.
    *   **Kelelahan Developer**: Menerima "banjir" *bug* sekaligus bisa membuat *developer* kewalahan dan frustrasi.

### Best Practice: File as You Find

*   **Apa itu**: Segera setelah Anda menemukan *bug* yang dapat direproduksi, buat *ticket* *bug* sesegera mungkin.
*   **Manfaat**:
    *   **Feedback Loop Cepat**: *Developer* mendapatkan notifikasi *bug* hampir secara *real-time*. Mereka dapat memperbaiki *bug* saat konteks fitur masih segar di pikiran mereka.
    *   **Efisiensi Developer**: Mengurangi *context switching*. *Developer* bisa memperbaiki *bug* kecil dengan cepat sebelum beralih ke tugas berikutnya.
    *   **Akurasi Tinggi**: Anda melaporkan *bug* saat detail dan konteksnya masih sangat jelas di kepala Anda, memastikan laporan yang lengkap dan akurat.
    *   **Distribusi Beban Merata**: *Bug* masuk secara bertahap, bukan membanjiri tim sekaligus.
    *   **Mencegah Regresi**: Perbaikan *bug* lebih awal dapat mencegah *bug* tersebut menyebabkan masalah lebih lanjut di bagian lain aplikasi.

Sebagai QA Thomas, Anda harus menganut prinsip **"File as You Find"**. Gunakan *template* standar dan otomatisasi `qa_report_bug.py` untuk membuat proses ini secepat dan semudah mungkin. Ingat, tujuan Anda adalah menjadi *quality gate* yang efisien, bukan *bottleneck*.

---

## Rangkuman

Di bab ini, Anda telah mempelajari seluk-beluk pelaporan *bug* yang efektif, sebuah keterampilan fundamental bagi setiap QA Engineer. Kita telah membahas bahwa laporan *bug* yang baik adalah alat komunikasi yang jelas, ringkas, dan lengkap, yang memandu *developer* menuju perbaikan.

Anda kini memahami setiap komponen dari *template* laporan *bug* standar Thomas, mulai dari judul yang deskriptif, detail *environment*, langkah-langkah reproduksi yang presisi, hingga pentingnya bukti visual dan log teknis. Kita juga telah mendalami rubrik *severity* P0-P3, yang membantu Anda menilai dampak *bug* dan menentukan urgensinya.

Selain itu, Anda telah melihat bagaimana alur eskalasi Thomas bekerja, memastikan *bug* mendapatkan perhatian yang sesuai berdasarkan *severity*-nya, dan bagaimana *script* otomatis `qa_report_bug.py` menyederhanakan proses ini. Terakhir, kita membahas kapan tidak perlu melaporkan *bug* (misalnya, untuk *feature request* atau kesalahpahaman) dan mengapa praktik "File as You Find" jauh lebih unggul daripada "Batch Filing" dalam menjaga efisiensi tim.

Dengan menguasai seni pelaporan *bug*, Anda tidak hanya menemukan masalah, tetapi juga menjadi fasilitator solusi yang efektif, memastikan *software* yang dirilis memenuhi standar kualitas tertinggi.

## Checklist Actionable

Berikut adalah daftar tindakan yang bisa Anda terapkan segera setelah membaca bab ini:

*   **Pahami Template Bug**: Hafalkan atau simpan *template* laporan *bug* standar. Pastikan Anda tahu setiap bagiannya dan mengapa itu penting.
*   **Latih Penulisan Judul**: Latih diri Anda untuk menulis judul *bug* yang ringkas, informatif, dan spesifik (`[Area] Ringkasan Masalah`).
*   **Detailkan Langkah Reproduksi**: Saat menemukan *bug*, tulis langkah-langkah reproduksi secara berurutan, bernomor, dan se-eksplisit mungkin.
*   **Sertakan Bukti Kuat**: Selalu sertakan *screenshot*, video, atau log (console/network) untuk mendukung laporan *bug* Anda, terutama untuk *bug* visual atau *intermittent*.
*   **Tentukan Severity dengan Tepat**: Gunakan rubrik P0-P3 secara konsisten. Pertimbangkan dampak *bug* terhadap pengguna dan bisnis, bukan hanya kesulitan teknisnya.
*   **Ikuti Alur Eskalasi**: Pastikan Anda mengikuti alur eskalasi Slack yang benar berdasarkan *severity* *bug* (P0/P1 ke `#incidents` + DM Tech Lead, P2 ke `#qa`, P3 hanya Notion).
*   **Manfaatkan Otomatisasi**: Jika tersedia, gunakan *script* `qa_report_bug.py` untuk mengotomatisasi proses pelaporan dan eskalasi.
*   **Terapkan "File as You Find"**: Laporkan *bug* segera setelah Anda menemukannya dan berhasil mereproduksinya. Hindari menumpuk *bug* untuk dilaporkan nanti.
*   **Hindari "Noise"**: Sebelum melaporkan *bug*, pertimbangkan apakah itu benar-benar *bug*, *feature request*, atau kesalahpahaman. Jika tidak dapat direproduksi, tandai dengan jelas.
*   **Verifikasi Perbaikan**: Setelah *bug* diperbaiki, pastikan Anda memverifikasi perbaikan tersebut di *build* yang baru. Ini akan dibahas lebih lanjut di bab *Test Execution*.
