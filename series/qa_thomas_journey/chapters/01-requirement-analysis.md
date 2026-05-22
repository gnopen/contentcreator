# Chapter 01: Requirement Analysis — Quality Gate Pertama

Selamat datang di babak pertama perjalanan Anda sebagai Quality Assurance Engineer! Jika Anda membayangkan pekerjaan QA hanya tentang menemukan *bug* di akhir siklus pengembangan, siapkan diri untuk sebuah kejutan. Peran QA modern jauh lebih strategis dan proaktif. Gerbang kualitas (Quality Gate) pertama, dan arguably yang paling krusial, dimulai jauh sebelum baris kode pertama ditulis: yaitu pada tahap *Requirement Analysis*.

Bayangkan ini: sebuah tim *engineering* menghabiskan satu minggu penuh untuk mengembangkan sebuah fitur berdasarkan dokumen yang ambigu. Saat fitur tersebut selesai, Anda sebagai QA menemukan bahwa ada bagian yang tidak jelas, atau bahkan bertentangan dengan ekspektasi pengguna. Apa yang terjadi? Fitur harus dirombak, waktu terbuang, *deadline* terancam, dan semangat tim menurun. Ini adalah skenario mimpi buruk yang bisa dihindari jika QA terlibat sejak awal.

Dalam bab ini, kita akan menyelami bagaimana Anda, sebagai QA Engineer, dapat menjadi penjaga kualitas yang proaktif. Kita akan belajar cara membaca Product Requirement Document (PRD) secara kritis, mengidentifikasi celah dan ambiguitas, serta memecah *user story* menjadi skenario-skenario yang siap diuji. Ini adalah fondasi penting yang akan menghemat banyak waktu, tenaga, dan frustrasi di kemudian hari. Mari kita mulai menjadi Quality Gate pertama yang tangguh!

---

## Memahami Peran QA dalam Requirement Analysis

Sebagai Quality Assurance Engineer, tugas Anda bukan hanya memastikan produk berfungsi sesuai spesifikasi, tetapi juga memastikan spesifikasi itu sendiri sudah benar, lengkap, dan jelas. Keterlibatan di tahap analisis kebutuhan adalah investasi waktu yang sangat berharga. Semakin dini Anda menemukan potensi masalah atau ambiguitas, semakin murah biaya perbaikannya.

Mengapa ini disebut "Quality Gate Pertama"? Karena di sinilah Anda memiliki kesempatan emas untuk:
1.  **Mencegah *bug* sejak awal:** Dengan mengidentifikasi persyaratan yang tidak jelas atau hilang, Anda mencegah *developer* membangun sesuatu yang salah atau tidak lengkap.
2.  **Membangun pemahaman bersama:** Memastikan semua pihak (Product Manager, Designer, Developer, QA) memiliki pemahaman yang sama tentang apa yang akan dibangun.
3.  **Mempercepat siklus pengembangan:** Mengurangi kebutuhan untuk pengerjaan ulang (*rework*) di tahap akhir, yang pada akhirnya mempercepat waktu peluncuran produk.
4.  **Meningkatkan kualitas secara keseluruhan:** Dengan fondasi persyaratan yang kuat, proses *development* dan *testing* selanjutnya akan jauh lebih efisien dan efektif.

Mari kita lihat bagaimana Anda bisa menjalankan peran krusial ini.

---

## Langkah 1: Mereview PRD — Gerbang Kualitas yang Tidak Boleh Terlewat

Product Requirement Document (PRD) adalah dokumen kunci yang menjelaskan apa yang akan dibangun, mengapa dibangun, dan bagaimana fitur tersebut akan berfungsi dari perspektif pengguna. Bagi QA, PRD adalah peta jalan pertama Anda. Mereview PRD bukan sekadar membaca, tetapi menganalisis secara kritis untuk mencari celah, ambiguitas, dan potensi masalah.

**Kapan Anda harus mereview PRD?**
Jawabannya jelas: **SEBELUM tim *engineering* mulai menulis kode.** Ini adalah mantra yang harus selalu Anda ingat.

### Checklist Review PRD

Berikut adalah daftar periksa yang bisa Anda gunakan untuk setiap PRD yang Anda review. Ini adalah 8 item penting yang akan membantu Anda mengidentifikasi masalah potensial sedini mungkin:

*   **[ ] Setiap *user story* memiliki kriteria penerimaan (Acceptance Criteria) dalam format Given/When/Then.**
    *   **Mengapa penting:** Format Given/When/Then (sering disebut Gherkin Syntax) adalah standar dalam Behavior-Driven Development (BDD). Ini membantu mendefinisikan perilaku sistem yang diharapkan dengan sangat jelas.
    *   **Yang dicari QA:** Pastikan setiap *user story* memiliki kriteria yang spesifik, terukur, dan dapat diuji. Jika hanya ada deskripsi naratif, mintalah PM untuk memecahnya menjadi Given/When/Then.
    *   **Contoh:**
        *   **Buruk:** "Pengguna bisa login." (Terlalu umum)
        *   **Baik:**
            *   `Given` pengguna berada di halaman login
            *   `When` pengguna memasukkan email dan password yang benar
            *   `And` pengguna menekan tombol "Login"
            *   `Then` pengguna diarahkan ke halaman *dashboard*

*   **[ ] Persyaratan fungsional (*Functional Requirements*) bersifat dapat diuji (setiap FR dapat dipetakan ke setidaknya satu *test case*).**
    *   **Mengapa penting:** Persyaratan yang tidak dapat diuji berarti Anda tidak tahu kapan fitur itu "selesai" atau "bekerja dengan benar."
    *   **Yang dicari QA:** Baca setiap FR dan tanyakan pada diri sendiri: "Bagaimana cara saya menguji ini?" Jika Anda kesulitan membayangkan *test case* untuk suatu FR, itu adalah pertanda ada ambiguitas atau kurangnya detail.

*   **[ ] Persyaratan non-fungsional (*Non-functional Requirements*) memiliki target yang terukur.**
    *   **Mengapa penting:** NFR seperti kecepatan, keamanan, dan skalabilitas sangat penting bagi pengalaman pengguna, tetapi seringkali ditulis secara samar. Kata-kata seperti "cepat," "aman," atau "mudah digunakan" tidak cukup.
    *   **Yang dicari QA:** Pastikan ada angka atau metrik yang jelas.
    *   **Contoh:**
        *   **Buruk:** "Aplikasi harus cepat."
        *   **Baik:** "Waktu pemuatan halaman *dashboard* harus kurang dari 2 detik untuk 90% pengguna di koneksi 4G."
        *   **Buruk:** "Data pengguna harus aman."
        *   **Baik:** "Semua data pengguna harus dienkripsi saat transit (TLS 1.2+) dan saat disimpan (AES-256)."

*   **[ ] *Edge cases* (kasus-kasus batas/ekstrem) eksplisit dan mencakup skenario seperti kegagalan jaringan, status parsial, pengguna bersamaan, *input* kosong/null, *input* yang salah format.**
    *   **Mengapa penting:** Aplikasi yang stabil tidak hanya berfungsi di "jalan lurus" (*happy path*), tetapi juga menangani situasi yang tidak terduga. *Edge cases* adalah sumber *bug* yang paling umum.
    *   **Yang dicari QA:** Apakah PRD membahas apa yang terjadi jika:
        *   Koneksi internet terputus di tengah proses?
        *   Server mengembalikan error 500?
        *   Pengguna mencoba mengirim data kosong?
        *   Dua pengguna mencoba memperbarui data yang sama secara bersamaan?
        *   Format *input* tidak sesuai (misalnya, email tanpa '@' atau domain)?
        *   Data yang diharapkan tidak ada (*null state*)?

*   **[ ] Diagram alur (*Flow Diagram*) ada dan cocok dengan narasi.**
    *   **Mengapa penting:** Diagram visual seringkali lebih mudah dipahami daripada teks panjang. Ini membantu memvisualisasikan perjalanan pengguna dan interaksi sistem.
    *   **Yang dicari QA:** Bandingkan diagram alur dengan deskripsi tekstual. Apakah ada perbedaan? Apakah ada langkah yang hilang di salah satu sisi? Diagram juga bisa membantu mengidentifikasi *edge cases* yang mungkin terlewat.

*   **[ ] Bagian "Di luar cakupan" (*Out-of-scope*) jelas.**
    *   **Mengapa penting:** Menentukan apa yang *tidak* akan dibangun sama pentingnya dengan apa yang akan dibangun. Ini mencegah perdebatan lingkup (*scope arguments*) di tengah *sprint*.
    *   **Yang dicari QA:** Apakah ada fitur terkait yang mungkin diasumsikan oleh *stakeholder* atau pengguna tetapi tidak akan disertakan dalam rilis ini? Memiliki bagian *out-of-scope* yang jelas membantu mengelola ekspektasi.

*   **[ ] Daftar *event* analitik ada (Anda akan memverifikasi *event* ini terpicu).**
    *   **Mengapa penting:** Banyak fitur modern membutuhkan pelacakan penggunaan untuk analisis data dan pengambilan keputusan bisnis.
    *   **Yang dicari QA:** Apakah PRD menyebutkan *event* apa saja yang perlu dikirim ke sistem analitik (misalnya, Google Analytics, Mixpanel, Amplitude) saat pengguna melakukan tindakan tertentu? Anda perlu tahu ini untuk menguji apakah *event* tersebut terpicu dengan benar.
    *   **Contoh:** "Ketika pengguna mengklik tombol 'Beli Sekarang', *event* `purchase_initiated` harus terpicu dengan parameter `product_id` dan `quantity`."

*   **[ ] Bagian pemeriksaan pra-*sprint* (*Pre-sprint check*) sudah tersedia.**
    *   **Mengapa penting:** Ini adalah daftar item yang harus disiapkan atau diverifikasi sebelum *sprint* dimulai.
    *   **Yang dicari QA:** Apakah ada dependensi eksternal, konfigurasi *environment*, atau data uji yang perlu disiapkan? Misalnya, "API pembayaran pihak ketiga sudah terintegrasi di *staging*."

### Cara Memberikan Feedback Konstruktif di PRD

Menemukan celah atau ambiguitas adalah satu hal, mengomunikasikannya secara efektif adalah hal lain. Tujuan Anda bukan hanya menunjukkan kesalahan, tetapi membantu meningkatkan kualitas dokumen dan, pada akhirnya, produk.

**Langkah-langkah saat menemukan celah:**
1.  **Berikan komentar spesifik pada tiket PRD (misalnya di Notion, Jira, Confluence) dengan pertanyaan yang jelas.** Hindari komentar umum seperti "Ini tidak jelas."
2.  **Tag Product Manager (PM) yang bersangkutan.** Ini memastikan PM segera melihat dan menindaklanjuti komentar Anda.
3.  **Blokir serah terima (*handoff*) ke *Tech Lead* atau tim *engineering* hingga masalah terselesaikan.** Ini adalah langkah krusial untuk menegaskan bahwa PRD belum siap untuk pengembangan.

**Contoh Kasus: 'Handle Invalid Input Gracefully'**

Misalkan Anda menemukan *functional requirement* seperti ini di PRD: "Sistem harus menangani *input* yang tidak valid dengan anggun (*gracefully*)."

Ini adalah contoh klasik dari persyaratan yang ambigu. Apa arti "dengan anggun" bagi Anda, bagi PM, dan bagi *developer*? Bisa jadi sangat berbeda.

Berikut adalah contoh dialog dan cara Anda memberikan komentar yang konstruktif:

**Dialog Internal (Pikiran QA Thomas):**
*   "Dengan anggun? Apa maksudnya? Menampilkan pesan error? Menolak *input* secara diam-diam? Mengarahkan ke halaman lain? Ini bisa diinterpretasikan banyak cara, dan *developer* bisa saja memilih implementasi yang tidak sesuai harapan PM atau pengguna."
*   "Saya perlu meminta PM untuk mendefinisikan perilaku spesifiknya."

**Komentar di PRD (Notion/Jira):**

```markdown
**Komentar QA (Thomas):**

**Ref:** FR-3: "Sistem harus menangani *input* yang tidak valid dengan anggun."

**Pertanyaan:** Mohon diperjelas definisi "menangani dengan anggun" untuk *input* yang tidak valid.

Apakah yang dimaksud adalah:
1.  Menampilkan pesan error yang jelas dan informatif kepada pengguna (misal: "Format email tidak valid")?
2.  Menolak *input* secara diam-diam tanpa *feedback* kepada pengguna?
3.  Mengarahkan pengguna ke halaman *error* umum?
4.  Melakukan koreksi otomatis pada *input* jika memungkinkan?

Mohon diberikan contoh spesifik untuk beberapa skenario *input* tidak valid (misalnya, email tanpa '@', tanggal yang salah format, angka di luar rentang yang diizinkan) dan bagaimana sistem seharusnya bereaksi pada setiap skenario tersebut.

Tanpa klarifikasi ini, ada risiko implementasi yang berbeda dari ekspektasi dan memerlukan *rework* di kemudian hari.

**@PM_Thomas** - Mohon bantuannya untuk klarifikasi ini sebelum *handoff* ke tim *engineering*.

---
```

**Penjelasan Komentar:**
*   **Spesifik:** Merujuk langsung ke FR yang bermasalah.
*   **Bertanya, bukan menuduh:** Menggunakan pertanyaan terbuka untuk mendorong PM memberikan detail.
*   **Memberikan opsi:** Memberikan beberapa kemungkinan interpretasi membantu PM memikirkan skenario dan memilih yang paling tepat.
*   **Menjelaskan dampak:** Mengingatkan tentang risiko jika tidak diklarifikasi (implementasi salah, *rework*).
*   **Panggilan tindakan:** Men-tag PM secara langsung.
*   **Menegaskan pentingnya waktu:** "sebelum *handoff* ke tim *engineering*."

Dengan pendekatan ini, Anda tidak hanya menemukan masalah tetapi juga memfasilitasi solusi, menjadikan diri Anda sebagai mitra strategis bagi tim produk.

---

## Langkah 2: Menganalisis User Story dan Memecahnya menjadi Skenario

Setelah PRD Anda melewati tahap review dan semua pertanyaan telah terjawab, langkah selanjutnya adalah menganalisis setiap *user story* dan memecahnya menjadi daftar skenario yang dapat diuji. Ini adalah jembatan antara persyaratan tingkat tinggi dan *test case* yang akan Anda tulis nanti.

**Apa itu *User Story*?**
*User story* adalah deskripsi singkat dan sederhana tentang sebuah fitur dari perspektif pengguna akhir. Format umumnya adalah:
"Sebagai [Tipe Pengguna], saya ingin [Tindakan], sehingga [Manfaat]."
Contoh: "Sebagai pengguna baru, saya ingin melihat *guided tour* pada saat login pertama, sehingga saya bisa memahami fitur-fitur utama aplikasi."

Tujuan dari memecah *user story* menjadi skenario adalah untuk memastikan Anda telah memikirkan semua kemungkinan cara pengguna berinteraksi dengan fitur tersebut, termasuk *happy path*, variasi, dan mode kegagalan.

### Decomposing User Story menjadi Skenario

Untuk setiap *user story*, Anda harus menghasilkan **daftar skenario** yang komprehensif. Skenario ini dapat dikategorikan menjadi beberapa jenis:

1.  **Happy Path (Jalur Sukses Utama):**
    *   Ini adalah skenario ideal di mana pengguna mengikuti alur yang diharapkan dan semuanya berjalan lancar. Ini adalah jalur paling dasar yang harus selalu berfungsi.
    *   **Contoh:** Pengguna memasukkan data yang valid dan berhasil menyelesaikan transaksi.

2.  **Variasi / Jalur Alternatif (*Alternative Paths*):**
    *   Skenario ini mencakup interaksi pengguna yang valid tetapi sedikit berbeda dari *happy path*. Ini mungkin melibatkan pilihan yang berbeda, data yang berbeda, atau kondisi sistem yang berbeda.
    *   **Contoh:** Pengguna memilih opsi "Lewati" di *guided tour*. Pengguna login dengan akun yang sudah ada.

3.  **Mode Kegagalan / Skenario Negatif (*Failure Modes / Negative Scenarios*):**
    *   Skenario ini menguji bagaimana sistem bereaksi terhadap *input* yang tidak valid, kondisi error, atau tindakan yang tidak diharapkan dari pengguna. Ini adalah bagian krusial untuk memastikan ketahanan dan stabilitas aplikasi.
    *   **Contoh:** Kegagalan jaringan saat memuat data, *input* yang salah format, API mengembalikan error, pengguna mencoba mengakses fitur tanpa izin.

### Contoh Nyata: Daftar Skenario untuk Fitur 'Guided Tour First Login'

Mari kita ambil *user story* yang disebutkan sebelumnya:
**Story:** Sebagai pengguna baru, saya melihat *guided tour* pada login pertama.

Berikut adalah daftar skenario yang bisa Anda buat, lengkap dengan penjelasan mengapa setiap skenario penting untuk diuji:

```
Story: As a new user, I see a guided tour on first login.

Scenarios:
```

1.  **Happy Path: Pengguna baru mendarat di halaman utama → modal *tour* muncul dalam 1 detik.**
    *   **Penjelasan:** Ini adalah skenario dasar. Memastikan *tour* muncul secara otomatis dan cepat untuk pengguna yang baru pertama kali login. Aspek "dalam 1 detik" adalah persyaratan non-fungsional (kinerja) yang penting untuk pengalaman pengguna.
    *   **Apa yang diuji:** Logika identifikasi pengguna baru, kecepatan pemuatan UI, tampilan *tour* default.

2.  **Pengguna Kembali (*Returning User*): Pengguna yang sudah ada login → *tour* TIDAK muncul.**
    *   **Penjelasan:** Penting untuk memastikan *tour* tidak mengganggu pengguna yang sudah familiar dengan aplikasi. Ini menguji logika identifikasi pengguna lama.
    *   **Apa yang diuji:** Logika kondisi untuk menampilkan/menyembunyikan *tour* berdasarkan status pengguna.

3.  **Penolakan (*Dismissal*): Pengguna mengklik "Lewati" → *tour* menghilang, *event* "tour_skipped" terpicu.**
    *   **Penjelasan:** Menguji fungsionalitas tombol "Lewati" dan memastikan *event* analitik yang relevan terpicu. *Event* ini penting untuk PM dalam memahami perilaku pengguna.
    *   **Apa yang diuji:** Interaksi tombol, penutupan *modal*, pelacakan *event* analitik.

4.  **Penyelesaian (*Completion*): Pengguna menyelesaikan semua 4 langkah → *event* "tour_completed" terpicu.**
    *   **Penjelasan:** Menguji seluruh alur *tour* hingga selesai dan memastikan *event* analitik "tour_completed" terpicu.
    *   **Apa yang diuji:** Navigasi langkah *tour*, transisi antar langkah, pelacakan *event* analitik akhir.

5.  **Parsial (*Partial*): Pengguna menutup *browser* di langkah 2 → membuka kembali → *tour* melanjutkan di langkah 2.**
    *   **Penjelasan:** Menguji persistensi status *tour*. Jika pengguna meninggalkan *tour* di tengah jalan, apakah progresnya disimpan dan dilanjutkan saat mereka kembali? Ini adalah contoh *state management*.
    *   **Apa yang diuji:** Penyimpanan progres *tour* (misalnya di *local storage* atau *backend*), resume *tour* dari langkah terakhir yang dilihat.

6.  **Jaringan Lambat (*Slow Network*): Aset *tour* membutuhkan waktu >3 detik untuk dimuat → *fallback* ke *skeleton UI*, tidak ada *error* JS.**
    *   **Penjelasan:** Menguji perilaku aplikasi dalam kondisi jaringan yang kurang ideal. Apakah ada indikator pemuatan yang baik? Apakah aplikasi tetap stabil?
    *   **Apa yang diuji:** Penanganan *timeout* pemuatan aset, tampilan *placeholder* (skeleton), stabilitas aplikasi tanpa *error* JavaScript.

7.  **Kegagalan API (*API Failure*): *Endpoint* metadata *tour* mengembalikan 500 → *tour* dilewati, *error* dicatat (*logged*).**
    *   **Penjelasan:** Menguji penanganan error dari *backend*. Jika API yang menyediakan konten *tour* gagal, apakah aplikasi crash atau dapat menanganinya dengan anggun (misalnya, melewatkan *tour* dan mencatat *error* untuk investigasi)?
    *   **Apa yang diuji:** Penanganan *error* HTTP (misalnya 500 Internal Server Error), *fallback* behavior, pencatatan *error* di *console* atau sistem *logging*.

8.  **Tampilan Seluler Potret (*Mobile Portrait*): *Tour* muat di *viewport*, semua teks terbaca jelas.**
    *   **Penjelasan:** Menguji responsivitas UI *tour* pada orientasi potret di perangkat seluler.
    *   **Apa yang diuji:** Responsivitas CSS, ukuran font, *layout* elemen, tidak ada *clipping* teks atau elemen tersembunyi.

9.  **Tampilan Seluler Lanskap (*Mobile Landscape*): *Tour* reposisi, tidak ada *clipping*.**
    *   **Penjelasan:** Menguji responsivitas UI *tour* pada orientasi lanskap di perangkat seluler.
    *   **Apa yang diuji:** Adaptasi *layout* untuk orientasi lanskap, elemen tidak tumpang tindih atau terpotong.

10. **Pembaca Layar (*Screen Reader*): Konten *tour* dapat dibaca, urutan fokus benar.**
    *   **Penjelasan:** Menguji aksesibilitas *tour* untuk pengguna dengan kebutuhan khusus yang menggunakan pembaca layar.
    *   **Apa yang diuji:** Atribut ARIA, *semantic HTML*, urutan tabulasi yang logis, semua teks dan kontrol dapat diakses dan dibaca oleh *screen reader*.

Daftar skenario ini akan menjadi *input* utama Anda untuk tahap selanjutnya: `Test Design` (merancang *test case*). Semakin detail dan komprehensif daftar skenario Anda, semakin mudah dan efektif proses pembuatan *test case*.

---

## Output dari Analisis Kebutuhan

Setelah Anda selesai mereview PRD dan membuat daftar skenario untuk setiap *user story*, Anda perlu mendokumentasikan hasil analisis Anda. Output ini biasanya berupa tugas atau dokumen "Analisis Pengujian" yang terhubung dengan PRD asli. Ini adalah cara Anda mengomunikasikan temuan Anda kepada tim dan memastikan semua orang berada di halaman yang sama.

Berikut adalah contoh struktur dan konten yang bisa Anda masukkan dalam tugas "Analisis Pengujian" di sistem manajemen proyek Anda (misalnya Notion, Jira):

```markdown
### Judul: Analisis Pengujian: Fitur Guided Tour Login

**Pemilik:** QA Thomas
**Reporter:** QA Thomas
**Prioritas:** P1 (Jika ada pertanyaan yang memblokir, atau P2 jika hanya klarifikasi)
**Sumber:** QA
**Label:** test-analysis, requirement-analysis

---

## Ringkasan Review PRD
**Link PRD:** [URL ke dokumen PRD di Notion/Jira/Confluence]

### Pertanyaan Terbuka untuk Product Manager
*   [ ] FR-3: Mohon definisikan "menangani *invalid input* dengan anggun" secara spesifik. (Lihat komentar saya di PRD untuk detail lebih lanjut).
*   [ ] NFR-1: Target waktu pemuatan untuk *dashboard* disebutkan "<2 detik". Apakah ini untuk 90% atau 100% pengguna? Di jaringan apa?
*   [ ] Edge Case: Apakah ada persyaratan untuk penanganan *race condition* jika dua pengguna mencoba mendaftar dengan email yang sama secara bersamaan?

### Klarifikasi yang Didapat (setelah diskusi dengan PM)
*   [x] FR-3: "Menangani dengan anggun" berarti menampilkan pesan error validasi di bawah *field* input yang relevan dan tidak mengizinkan *submit* form.
*   [x] NFR-1: Target <2 detik adalah untuk 90% pengguna di koneksi 4G.
*   [x] Edge Case: Untuk *race condition* pendaftaran email, sistem akan mengembalikan error "Email sudah terdaftar" ke salah satu pengguna.

---

## Skenario yang Diidentifikasi

### Story: Sebagai pengguna baru, saya melihat *guided tour* pada login pertama.
*   **Happy path:** Pengguna baru login → *tour* muncul dalam 1 detik.
*   **Pengguna Kembali:** Pengguna lama login → *tour* TIDAK muncul.
*   **Penolakan:** Pengguna klik "Lewati" → *tour* hilang, *event* "tour_skipped" terpicu.
*   **Penyelesaian:** Pengguna menyelesaikan semua langkah → *event* "tour_completed" terpicu.
*   **Parsial:** Pengguna menutup *browser* di langkah 2 → membuka kembali → *tour* melanjutkan di langkah 2.
*   **Jaringan Lambat:** Aset *tour* butuh >3 detik → *skeleton UI*, tanpa *error* JS.
*   **Kegagalan API:** *Endpoint* metadata *tour* 500 → *tour* dilewati, *error* dicatat.
*   **Seluler Potret:** *Tour* muat di *viewport*, semua teks terbaca jelas.
*   **Seluler Lanskap:** *Tour* reposisi, tidak ada *clipping*.
*   **Pembaca Layar:** Konten *tour* dapat dibaca, urutan fokus benar.

---

## Estimasi Usaha Desain Pengujian
~ 8 jam (untuk fitur 'Guided Tour Login' ini, termasuk menulis *test cases* manual dan merencanakan tes otomatisasi dasar).

---
```

Dokumen ini menjadi *single source of truth* untuk pemahaman QA tentang fitur tersebut. Ini juga menunjukkan kepada tim bahwa Anda telah melakukan analisis mendalam.

---

## Kriteria Gerbang (Gate Criteria): Kapan Analisis Dianggap Selesai?

Penting untuk memiliki titik henti yang jelas sebelum Anda melanjutkan ke fase berikutnya (Desain Pengujian). Ini adalah "gerbang" yang harus Anda lewati untuk memastikan kualitas fondasi sudah kokoh.

Anda **jangan mulai menulis *test case*** sampai semua kriteria berikut terpenuhi:

*   **[ ] Semua pertanyaan review PRD telah dijawab dan diselesaikan oleh Product Manager.**
    *   Tidak boleh ada ambiguitas atau celah yang tidak terjawab. Semua orang harus memiliki pemahaman yang sama.

*   **[ ] Semua skenario pengujian telah didaftarkan dan dikategorikan (happy path, variasi, failure modes) untuk setiap *user story*.**
    *   Daftar skenario Anda harus komprehensif dan mencakup semua aspek yang dapat diuji dari fitur tersebut.

*   **[ ] Product Manager telah menyetujui cakupan skenario yang Anda identifikasi.**
    *   Ini adalah langkah validasi yang sangat penting. PM perlu mengonfirmasi bahwa daftar skenario Anda sudah sesuai dengan ekspektasi mereka terhadap apa yang akan diuji. Jika ada skenario yang terlewat atau prioritas yang berbeda, ini adalah kesempatan terakhir untuk menyelaraskannya.

Setelah Anda mendapatkan "lampu hijau" dari PM dan semua poin di atas terpenuhi, barulah Anda bisa dengan percaya diri melangkah ke fase berikutnya: Desain Pengujian, di mana Anda akan mengubah skenario-skenario ini menjadi *test case* yang konkret.

---

## Rangkuman

Bab ini telah membawa kita pada Quality Gate pertama dan terpenting dalam perjalanan QA Anda: Analisis Kebutuhan. Kita telah belajar bahwa peran QA bukan hanya menemukan *bug* di akhir, tetapi menjadi penjaga kualitas proaktif yang memastikan fondasi produk dibangun di atas persyaratan yang jelas, lengkap, dan dapat diuji.

Anda kini memiliki alat untuk:
*   Menganalisis Product Requirement Document (PRD) secara kritis menggunakan daftar periksa 8 poin yang komprehensif.
*   Memberikan *feedback* yang konstruktif dan spesifik kepada Product Manager, mengubah ambiguitas menjadi klarifikasi yang dapat diuji.
*   Memecah *user story* menjadi daftar skenario pengujian yang detail, mencakup *happy path*, variasi, dan mode kegagalan, seperti yang kita lihat pada contoh *guided tour first login*.
*   Mendokumentasikan hasil analisis Anda dalam format yang jelas dan actionable.
*   Mengetahui kapan analisis Anda dianggap selesai, dengan persetujuan dari Product Manager, sebelum melangkah ke tahap selanjutnya.

Dengan menguasai tahap ini, Anda tidak hanya mencegah *bug* sebelum mereka lahir, tetapi juga membangun hubungan yang kuat dengan tim produk dan *engineering*, menunjukkan nilai strategis Anda sebagai Quality Assurance Engineer.

---

## Checklist Actionable

Berikut adalah daftar tindakan yang dapat Anda lakukan segera setelah membaca bab ini:

*   **[ ] Pahami Alur Kerja PRD:** Ketahui di mana PRD disimpan di perusahaan Anda (Notion, Jira, Confluence, dll.) dan siapa Product Manager yang bertanggung jawab.
*   **[ ] Jadwalkan Keterlibatan Dini:** Bicarakan dengan PM Anda untuk memastikan Anda dilibatkan dalam review PRD *sebelum* *engineering* mulai koding.
*   **[ ] Terapkan Checklist Review PRD:** Gunakan 8 poin checklist yang dibahas dalam bab ini setiap kali Anda mereview PRD. Buat template pribadi Anda jika perlu.
*   **[ ] Latih Komunikasi Konstruktif:** Saat menemukan celah, tulis komentar di PRD yang spesifik, mengajukan pertanyaan, dan menawarkan opsi solusi, bukan hanya menunjuk masalah.
*   **[ ] Pecah User Story menjadi Skenario:** Untuk setiap *user story* dalam PRD, buat daftar skenario yang mencakup *happy path*, variasi, dan *failure modes*. Gunakan contoh 'guided tour' sebagai referensi.
*   **[ ] Dokumentasikan Output Analisis:** Buat tugas "Analisis Pengujian" di sistem manajemen proyek Anda yang merangkum temuan PRD dan daftar skenario.
*   **[ ] Pastikan Kriteria Gerbang Terpenuhi:** Jangan mulai menulis *test case* sampai semua pertanyaan terjawab, semua skenario terdaftar, dan PM telah menyetujui cakupan skenario Anda.
*   **[ ] Ajukan Pertanyaan:** Jika Anda tidak yakin tentang suatu persyaratan, jangan ragu untuk bertanya. Lebih baik bertanya sekarang daripada menemukan *bug* nanti.
