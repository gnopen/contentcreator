# Chapter 06: Stakeholder Engagement — Demo, Meeting, UAT Coordination

Selamat datang kembali, petualang QA! Hingga chapter ini, kita telah menyelami berbagai aspek teknis peran Quality Assurance: dari menganalisis *requirement* yang kompleks, merancang *test case* yang komprehensif, mengeksekusi pengujian dengan berbagai metode, hingga melaporkan *bug* yang *actionable* dan mendokumentasikan hasil pengujian. Semua itu adalah fondasi yang sangat kuat untuk seorang QA Engineer.

Namun, pekerjaan QA tidak berhenti di meja Anda sendiri. Mungkin Anda sudah mulai menyadari bahwa *output* dari pekerjaan Anda — seperti laporan *bug*, hasil eksekusi *test case*, atau laporan UAT — tidak hanya dikonsumsi oleh Anda atau tim teknis semata. Sebaliknya, informasi tersebut menjadi jembatan komunikasi yang menghubungkan berbagai tim dan pemangku kepentingan.

Inilah inti dari *stakeholder engagement*: kemampuan seorang QA untuk berinteraksi, berkomunikasi, dan berkolaborasi secara efektif dengan berbagai pihak yang terlibat dalam siklus pengembangan produk. Dari Product Manager (PM), Developer, Tech Lead, hingga tim Marketing, bahkan *end-user* atau *business stakeholder* yang akan menggunakan fitur yang Anda uji. QA bukan sekadar 'tukang tes' yang bekerja di balik layar, melainkan seorang *quality gate* dan *communicator* yang memastikan semua orang memiliki pemahaman yang sama tentang kualitas produk.

Di chapter ini, kita akan membahas bagaimana Anda dapat menjadi QA Engineer yang tidak hanya andal secara teknis, tetapi juga mahir dalam berinteraksi dengan *stakeholder*. Kita akan melihat cara mendemonstrasikan fitur dengan percaya diri dan aman, bagaimana berkontribusi secara berbobot dalam berbagai jenis *meeting*, dan bagaimana mengoordinasikan *User Acceptance Testing* (UAT) yang efektif. Mari kita mulai perjalanan ini!

---

## 1. Demo Fitur: Strategi Aman untuk Memamerkan Kualitas

Mendemonstrasikan fitur yang baru dikembangkan kepada para pemangku kepentingan adalah momen krusial bagi tim produk dan engineering. Ini adalah kesempatan untuk menunjukkan kerja keras yang telah dilakukan, mengumpulkan *feedback*, dan mendapatkan persetujuan untuk langkah selanjutnya. Bagi seorang QA, momen demo juga merupakan validasi akhir bahwa fitur tersebut telah memenuhi standar kualitas dan siap untuk dipertontonkan.

Namun, ada satu fakta pahit tentang demo: **demo langsung (live demo) itu berbahaya.** Betul, Anda tidak salah dengar. Seringkali, saat demo langsung, hal-hal yang tidak terduga bisa terjadi. Koneksi internet tiba-tiba putus, data demo tidak sengaja terhapus, *environment* demo mendadak *down*, atau bahkan *bug* yang luput dari perhatian muncul di detik-detik terakhir. Ini bisa sangat memalukan dan merusak reputasi tim, apalagi jika terjadi di depan *stakeholder* penting.

Sebagai Quality Assurance, Anda memiliki peran penting untuk memastikan demo berjalan lancar dan tanpa drama. Bagaimana strateginya?

### Strategi Demo: Pra-Rekaman + Skrip Live + Rekaman Cadangan

Strategi terbaik untuk demo yang aman dan efektif adalah kombinasi dari persiapan matang dan rencana cadangan yang kuat:

1.  **Rekaman Otomatis (Pre-recorded Automation Run)**:
    *   Buatlah rekaman video dari skrip otomatisasi Anda yang berjalan, yang secara naratif menjelaskan alur fitur dari awal hingga akhir.
    *   Rekaman ini tidak hanya menunjukkan bahwa fitur berfungsi, tetapi juga memamerkan kemampuan otomatisasi Anda.
    *   Narasi dalam video harus jelas, ringkas, dan fokus pada *value* yang diberikan fitur.

2.  **Demo Langsung Berbasis Skrip (Scripted Live Demo)**:
    *   Idealnya, Anda tetap akan melakukan demo secara langsung. Namun, demo langsung ini harus **berbasis skrip** dan menggunakan **skrip otomatisasi yang sama** dengan yang Anda rekam.
    *   Pastikan Anda menjalankan skrip otomatisasi ini dalam kondisi *environment* demo yang stabil dan data yang terkontrol.
    *   Dengan skrip otomatisasi, Anda meminimalkan interaksi manual yang bisa memicu kesalahan dan memastikan setiap langkah demo konsisten.

3.  **Rekaman Cadangan Siap Akses (Backup Recording)**:
    *   Ini adalah jaring pengaman Anda. Rekaman otomatis yang Anda buat sebelumnya harus **diunggah ke Drive** atau *platform cloud* lain yang mudah diakses.
    *   Siapkan tautan *Slack-ready* ke rekaman ini. Jika terjadi kegagalan tak terduga saat demo langsung (misalnya, *environment* tiba-tiba *down*), Anda bisa langsung beralih ke rekaman cadangan dengan cepat dan mulus.

Dengan strategi ini, Anda tidak hanya memastikan kelancaran demo, tetapi juga menunjukkan profesionalisme dan kesiapan tim.

### Checklist Persiapan Demo

Sebelum demo, pastikan Anda telah melewati *checklist* ini:

*   **[ ] Data Demo dalam Kondisi Baik di *Environment* Demo:**
    *   Pastikan *environment* demo menggunakan data yang relevan, realistis, dan bersih. Hindari data yang aneh atau tidak lengkap yang bisa membingungkan *stakeholder*.
    *   Jika perlu, siapkan data khusus untuk demo yang menyoroti kasus penggunaan kunci.
    *   Contoh: Untuk demo fitur *checkout*, pastikan ada produk di keranjang, alamat pengiriman yang valid, dan metode pembayaran yang aktif.
*   **[ ] Skrip Otomatisasi Diuji 24 Jam Sebelum Demo:**
    *   Jangan pernah berasumsi skrip otomatisasi Anda akan selalu berfungsi. Jalankan skrip setidaknya sehari sebelum demo untuk memastikan tidak ada perubahan mendadak di *environment* atau kode yang memecah skrip Anda.
    *   Ini memberi Anda waktu untuk memperbaiki masalah kecil jika ada.
*   **[ ] Rekaman Cadangan Diunggah ke Drive:**
    *   Setelah rekaman otomatisasi selesai, segera unggah ke *platform cloud* seperti Google Drive, OneDrive, atau Dropbox.
    *   Pastikan izin aksesnya sudah diatur dengan benar agar *stakeholder* bisa melihatnya jika diperlukan.
*   **[ ] Tautan Rekaman Siap di Slack untuk Cadangan Instan:**
    *   Siapkan tautan langsung ke rekaman cadangan Anda. Simpan di *notes* pribadi atau di saluran Slack yang relevan.
    *   Jika terjadi masalah saat demo langsung, Anda bisa segera membagikan tautan ini dan melanjutkan presentasi tanpa banyak jeda.

**Contoh Skenario Demo: Thomas Menyelamatkan Hari**

Thomas, seorang QA Engineer di Atmoscheck, akan mendemonstrasikan fitur "Integrasi Laporan Cuaca Kustom" kepada tim manajemen. Dia telah menyiapkan skrip otomatisasi Playwright untuk melewati alur fitur tersebut.

*   **Persiapan Thomas:**
    *   Thomas memastikan *environment staging* memiliki akun pengguna dengan langganan premium yang memungkinkan integrasi kustom.
    *   Dia menjalankan skrip otomatisasi sehari sebelumnya dan merekamnya, lalu mengunggah video ke Google Drive dengan tautan yang dapat dibagikan. Tautan ini disimpan di *notes* dan juga di *draft* pesan Slack.
*   **Saat Demo:**
    *   Thomas memulai demo langsung, menjalankan skrip otomatisasi Playwright. Semua berjalan lancar, dan *stakeholder* terkesan dengan fluiditas demonya.
    *   Namun, di tengah-tengah demo, koneksi internet di ruang rapat tiba-tiba terputus. Panik mulai menyelimuti.
    *   **Tindakan Thomas:** Dengan tenang, Thomas berkata, "Mohon maaf atas gangguan koneksi ini. Sebagai rencana cadangan, saya telah menyiapkan rekaman demo lengkap. Saya akan membagikan tautannya di chat sekarang, dan kita bisa melanjutkan presentasi dengan video tersebut." Dia langsung menempelkan tautan Drive yang sudah disiapkan di *meeting chat*.
    *   Demo dapat dilanjutkan tanpa hambatan berarti, dan *stakeholder* menghargai kesiapan Thomas.

Ini menunjukkan bahwa persiapan yang matang dan strategi cadangan adalah kunci untuk demo yang sukses dan bebas stres.

---

## 2. Berpartisipasi dalam Meeting: Kontribusi Berbobot dari QA

Sebagai QA Engineer, Anda akan menghabiskan sebagian waktu Anda di berbagai jenis *meeting*. Ini bukan hanya tentang 'hadir', tetapi tentang 'berkontribusi'. Peran QA dalam *meeting* sangat vital karena Anda membawa perspektif kualitas, potensi risiko, dan *estimasi* pengujian yang tidak dimiliki oleh peran lain.

Berikut adalah beberapa jenis *meeting* umum yang akan Anda hadiri, beserta peran dan kontribusi Anda di dalamnya:

### Jenis-jenis Meeting dan Peran QA

| Meeting | Frekuensi | Peran QA |
|---|---|---|
| **Sprint Planning** | Mingguan/Dua Mingguan | Menyuarakan estimasi pengujian, mengidentifikasi risiko |
| **Daily Standup** | Harian | Berbagi status pengujian, mengidentifikasi *blocker* |
| **Backlog Grooming** | Mingguan | Mengidentifikasi isu *testability* pada pekerjaan yang akan datang |
| **Sprint Review** | Akhir Sprint | Demo fitur bersama PM, berbagi laporan QA |
| **Sprint Retrospective** | Akhir Sprint | Mengemukakan peningkatan proses QA |
| **Bug Triage** | Sesuai Kebutuhan | Memimpin prioritisasi *bug* dengan rubrik *severity* |
| **Pre-release Sync** | Per Rilis | Pemilik tanda tangan persetujuan rilis (*sign-off owner*) |

Mari kita bahas lebih detail peran dan kontribusi Anda di setiap *meeting*:

#### a. Sprint Planning
*   **Tujuan:** Merencanakan pekerjaan yang akan dilakukan dalam *sprint* berikutnya.
*   **Kontribusi QA:**
    *   **Memberikan Estimasi Pengujian:** Berikan estimasi waktu yang realistis untuk pengujian setiap *user story* atau tugas. Ini mencakup waktu untuk analisis, desain *test case*, eksekusi, dan pelaporan.
    *   **Mengidentifikasi Risiko Kualitas:** Soroti potensi risiko yang mungkin muncul selama pengujian, seperti ketergantungan pada sistem lain, kompleksitas fitur, atau kurangnya data uji.
    *   **Memastikan *Definition of Done* (DoD) Mencakup Pengujian:** Pastikan bahwa "selesai" untuk setiap tugas berarti juga telah melewati pengujian QA yang memadai.
    *   **Menanyakan Klarifikasi:** Jika ada *user story* yang kurang jelas atau memiliki *acceptance criteria* yang ambigu, inilah saatnya untuk menanyakan klarifikasi kepada PM atau Developer.

    *Contoh:* "Untuk *user story* 'Integrasi Pembayaran Baru', saya estimasi butuh 2 hari penuh untuk pengujian fungsional dan *negative testing*, mengingat ada banyak skenario *error* dari pihak ketiga. Kita juga perlu memastikan ada *test account* yang valid untuk setiap metode pembayaran."

#### b. Daily Standup
*   **Tujuan:** Sinkronisasi harian tentang kemajuan, *blocker*, dan rencana kerja.
*   **Kontribusi QA:**
    *   **Bagikan Status Pengujian:** Beri tahu tim apa yang sedang Anda uji, apa yang sudah selesai, dan apa yang akan Anda lakukan selanjutnya.
    *   **Laporkan *Blocker*:** Segera sampaikan jika ada masalah yang menghambat pekerjaan Anda (misalnya, *bug* kritis, *environment* tidak stabil, ketergantungan yang belum terpenuhi).
    *   **Sebutkan Potensi Risiko:** Jika Anda melihat *bug* yang berpotensi memengaruhi *user story* lain, sampaikan di sini.

    *Contoh:* "Kemarin saya selesai menguji modul *login* baru, dan semua *test case* positif lolos. Hari ini saya akan mulai *negative testing* dan *edge case*. Saya menemukan *bug* di mana *password* yang terlalu panjang tidak divalidasi dengan benar, sudah saya laporkan."

#### c. Backlog Grooming (atau Refinement)
*   **Tujuan:** Memastikan *item backlog* jelas, terdefinisi dengan baik, dan siap untuk *sprint planning* berikutnya.
*   **Kontribusi QA:**
    *   **Identifikasi Isu *Testability*:** Tinjau *user story* yang akan datang dan identifikasi apakah ada aspek yang sulit atau tidak mungkin diuji, atau membutuhkan persiapan khusus.
    *   **Sarankan *Acceptance Criteria* Tambahan:** Bantu PM untuk menyempurnakan *acceptance criteria* agar lebih spesifik dan terukur dari perspektif pengujian.
    *   **Estimasi Awal:** Berikan perkiraan kasar tentang upaya pengujian yang diperlukan untuk setiap *item*.

    *Contoh:* "Untuk fitur 'Notifikasi Push Personalisasi', *acceptance criteria* saat ini hanya menyebut 'notifikasi terkirim'. Kita perlu spesifikasi lebih lanjut tentang *trigger*, konten notifikasi untuk berbagai skenario pengguna, dan bagaimana kita akan memverifikasi pengiriman notifikasi di berbagai perangkat."

#### d. Sprint Review
*   **Tujuan:** Mendemonstrasikan pekerjaan yang telah selesai kepada *stakeholder* dan mengumpulkan *feedback*.
*   **Kontribusi QA:**
    *   **Demo Bersama PM:** Anda dapat membantu PM dalam mendemonstrasikan fitur, atau bahkan memimpin bagian demo yang menyoroti kualitas atau skenario *edge case* tertentu.
    *   **Berbagi Laporan QA:** Sajikan ringkasan singkat tentang status kualitas *sprint* tersebut, termasuk jumlah *test case* yang dieksekusi, *bug* yang ditemukan dan diperbaiki, serta hasil UAT jika sudah dilakukan.
    *   **Menjawab Pertanyaan Teknis:** Siap menjawab pertanyaan *stakeholder* terkait stabilitas, performa, atau masalah kualitas yang mungkin mereka miliki.

    *Contoh:* "Selain demo fitur yang sudah ditampilkan PM, saya ingin menambahkan bahwa kami telah menjalankan 150 *test case* untuk *sprint* ini, dengan tingkat keberhasilan 98%. Dua *bug* kritis yang ditemukan telah diperbaiki dan diverifikasi. Kita juga sudah mendapatkan *sign-off* dari UAT untuk modul *dashboard* baru."

#### e. Sprint Retrospective
*   **Tujuan:** Merefleksikan *sprint* yang baru saja berakhir dan mengidentifikasi area untuk perbaikan proses.
*   **Kontribusi QA:**
    *   **Mengemukakan Peningkatan Proses QA:** Bagikan observasi tentang apa yang berjalan baik dan apa yang bisa ditingkatkan dari perspektif QA (misalnya, *bug* yang terlambat ditemukan, kesulitan dalam setup *environment*, komunikasi yang kurang efektif).
    *   **Mencari Solusi Bersama:** Berpartisipasi aktif dalam diskusi untuk menemukan solusi atas masalah yang diangkat.
    *   **Fokus pada Proses, Bukan Individu:** Pastikan *feedback* konstruktif dan berfokus pada perbaikan sistem atau proses, bukan menyalahkan individu.

    *Contoh:* "Saya perhatikan ada beberapa *bug* yang baru muncul di akhir *sprint* karena integrasi antar modul belum dilakukan lebih awal. Mungkin kita bisa mencoba strategi *integration testing* yang lebih agresif di tengah *sprint* agar *bug* ini bisa terdeteksi lebih cepat."

#### f. Bug Triage
*   **Tujuan:** Meninjau *bug* yang dilaporkan, menentukan *severity*, *priority*, dan rencana tindakan.
*   **Kontribusi QA:**
    *   **Memimpin Prioritisasi dengan Rubrik *Severity*:** Sebagai pelapor *bug* dan penilai dampak, Anda adalah orang terbaik untuk memimpin diskusi tentang *severity* dan *priority* *bug*. Gunakan rubrik P0-P3 yang telah disepakati (lihat Chapter 04).
    *   **Memberikan Konteks Mendalam:** Jelaskan dampak *bug* dari perspektif pengguna dan bisnis.
    *   **Verifikasi Reproduksi:** Pastikan *bug* masih dapat direproduksi dan berikan langkah-langkah yang jelas.

    *Contoh:* "Berdasarkan rubrik kita, *bug* 'Pembayaran Gagal Tanpa Pesan Error' adalah P0 karena menghentikan pengguna menyelesaikan transaksi inti dan tidak ada *workaround*. Ini harus segera diperbaiki."

#### g. Pre-release Sync
*   **Tujuan:** Sinkronisasi terakhir sebelum rilis produk, memastikan semua siap.
*   **Kontribusi QA:**
    *   **Pemilik Tanda Tangan Persetujuan Rilis (*Sign-off Owner*):** Ini adalah salah satu peran paling krusial Anda. Anda adalah *gatekeeper* terakhir. Anda harus memberikan persetujuan (atau menolak) rilis berdasarkan status kualitas saat ini.
    *   **Sajikan Laporan Kualitas Final:** Siapkan ringkasan tentang status *bug* yang diketahui, hasil pengujian regresi, dan persetujuan UAT.
    *   **Identifikasi Risiko Rilis:** Sampaikan risiko yang tersisa (jika ada) dan dampak potensialnya.

    *Contoh:* "Berdasarkan semua pengujian yang telah kami lakukan, termasuk regresi otomatis dan UAT yang telah disetujui, saya memberikan *sign-off* untuk rilis versi 2.3. Semua *bug* kritis telah diperbaiki dan diverifikasi. Ada dua *bug* minor yang diketahui, namun dampaknya minimal dan tidak memblokir fungsionalitas utama."

Dengan berpartisipasi secara aktif dan berbobot dalam *meeting-meeting* ini, Anda tidak hanya meningkatkan visibilitas peran QA, tetapi juga berkontribusi secara signifikan terhadap keberhasilan tim dan kualitas produk secara keseluruhan.

---

## 3. Koordinasi UAT (User Acceptance Testing): Menjembatani Bisnis dan Teknis

*User Acceptance Testing* (UAT) adalah tahap pengujian di mana *business stakeholder* atau pengguna aktual memvalidasi bahwa fitur atau produk yang dikembangkan telah memenuhi kebutuhan bisnis mereka dan siap untuk digunakan. Ini adalah "jembatan" antara tim teknis dan pengguna akhir.

Peran Anda sebagai QA dalam UAT adalah sebagai **koordinator, dokumentator, dan fasilitator**. Anda memastikan proses UAT berjalan lancar, *feedback* terkumpul dengan baik, dan keputusan dapat diambil berdasarkan hasil UAT.

### Tahapan Koordinasi UAT

#### a. Pra-UAT (Pre-UAT)
Tahap ini adalah tentang persiapan agar UAT berjalan terstruktur.

*   **[ ] Buat Rencana UAT:**
    *   **Siapa yang Menguji Apa?** Identifikasi partisipan UAT (misalnya, PM, *Business Analyst*, *Key Users*). Tetapkan modul atau fitur spesifik yang akan diuji oleh masing-masing partisipan.
    *   **Kapan?** Tentukan jadwal UAT, durasi, dan *deadline* untuk pengumpulan *feedback*.
    *   **Kriteria Keberhasilan (Success Criteria):** Apa yang dianggap sebagai "lulus" UAT? Misalnya, "Semua alur utama dapat diselesaikan tanpa *bug* kritis," atau "80% dari skenario UAT berhasil diselesaikan."
    *   **Lingkungan UAT:** Pastikan ada *environment* khusus untuk UAT yang stabil dan terpisah dari *staging* atau *production*.

*   **[ ] Siapkan Skrip UAT:**
    *   Skrip UAT lebih sederhana daripada *test case* QA. Ditulis untuk orang non-QA, dengan bahasa yang mudah dipahami.
    *   Fokus pada alur bisnis utama dan skenario pengguna yang realistis.
    *   Sertakan langkah-langkah jelas, data yang harus digunakan, dan hasil yang diharapkan.
    *   Contoh: "Langkah 1: Buka halaman produk X. Langkah 2: Tambahkan produk ke keranjang. Hasil yang diharapkan: Produk X muncul di keranjang dengan harga yang benar."

*   **[ ] Isi *Environment* UAT dengan Data Realistis:**
    *   Data uji yang realistis sangat penting. Hindari menggunakan data *dummy* yang tidak masuk akal.
    *   Jika memungkinkan, gunakan salinan data *production* yang sudah di-*anonymize* atau buat data yang merepresentasikan skenario bisnis nyata.
    *   Pastikan data tersebut mencakup berbagai kasus (misalnya, pengguna dengan langganan berbeda, produk dengan stok kosong, dll.).

*   **[ ] Latih Partisipan (Sesi Orientasi 10 Menit):**
    *   Jangan berasumsi partisipan UAT akan langsung mengerti cara menggunakan *environment* atau mengisi *feedback*.
    *   Adakan sesi singkat (sekitar 10-15 menit) untuk:
        *   Menjelaskan tujuan UAT.
        *   Menunjukkan cara mengakses *environment* UAT.
        *   Menjelaskan cara menggunakan skrip UAT.
        *   Menjelaskan bagaimana dan di mana mereka harus melaporkan *feedback* atau *bug*.
        *   Menjawab pertanyaan awal.

    *Contoh Dialog Pelatihan UAT:*
    "Selamat pagi Bapak/Ibu, terima kasih sudah meluangkan waktu untuk UAT fitur 'Manajemen Pesanan Baru'. Dalam sesi singkat ini, saya akan menunjukkan cara mengakses *environment* UAT kita di `uat.atmoscheck.com`, bagaimana menjalankan skrip UAT yang sudah saya siapkan, dan yang paling penting, bagaimana melaporkan temuan Anda di Notion. Fokus kita adalah memastikan fitur ini memenuhi kebutuhan bisnis kita. Jika ada *bug* atau *feedback* terkait pengalaman pengguna, mohon dicatat dengan detail."

#### b. Selama UAT (During UAT)
Selama UAT berlangsung, Anda adalah titik kontak utama dan fasilitator.

*   **[ ] Siap Menjawab Pertanyaan:**
    *   Dedikasikan saluran Slack (misalnya, `#uat-manajemen-pesanan`) atau *channel* komunikasi lain di mana partisipan dapat mengajukan pertanyaan secara *real-time*.
    *   Respon dengan cepat dan bantu memecahkan masalah kecil (misalnya, "Saya tidak bisa *login*," "Data ini kenapa kosong?").
    *   Ini membantu menjaga momentum UAT dan mengurangi frustrasi partisipan.

*   **[ ] Tangkap *Feedback* Secara *Real-time*:**
    *   Gunakan *tool* seperti Notion, Jira, atau Google Sheets untuk mencatat semua temuan.
    *   Buat satu tugas/item per temuan (*finding*). Pastikan setiap entri mencakup:
        *   Deskripsi jelas tentang masalah.
        *   Langkah-langkah untuk mereproduksi (jika *bug*).
        *   *Screenshot* atau video (jika relevan).
        *   Nama pelapor.
        *   *Severity* awal (jika *bug*).
        *   Jenis temuan (bug, misunderstanding, new request).

*   **[ ] Triage Temuan:**
    *   Saat *feedback* masuk, segera *triage* (pilah) temuan tersebut ke dalam kategori:
        *   **Bug Aktual:** Masalah yang memang merupakan *defect* dalam kode atau implementasi. Laporkan ini ke tim Developer.
        *   **Kesalahpahaman (Misunderstanding):** Partisipan UAT mungkin salah memahami fungsionalitas atau cara penggunaan. Berikan klarifikasi.
        *   **Permintaan Baru (New Request):** Partisipan mungkin menyarankan fitur baru atau peningkatan yang tidak termasuk dalam *scope* awal. Catat ini sebagai *feedback* untuk *backlog* di masa mendatang, bukan *bug*.

#### c. Pasca-UAT (Post-UAT)
Setelah UAT selesai, ada beberapa langkah penting untuk merangkum dan menindaklanjuti.

*   **[ ] Buat Laporan UAT (UAT Report):**
    *   Rangkum semua temuan, statusnya (diperbaiki, ditunda, bukan *bug*), dan keputusan yang diambil.
    *   Sertakan daftar partisipan, tanggal UAT, dan kriteria keberhasilan yang tercapai/tidak tercapai.
    *   (Lihat Chapter 05 untuk detail lebih lanjut tentang pembuatan laporan).

*   **[ ] Kumpulkan *Sign-off*:**
    *   Dapatkan persetujuan resmi dari PM, Tech Lead, dan *Business Stakeholder* bahwa fitur telah memenuhi harapan mereka dan siap untuk rilis.
    *   *Sign-off* ini adalah dokumen penting yang menunjukkan bahwa semua pihak telah menyetujui kualitas dan fungsionalitas fitur.

*   **[ ] Jika *Sign-off* Terhambat:**
    *   Jika ada *bug* kritis yang ditemukan selama UAT dan belum diperbaiki, atau jika *stakeholder* merasa fitur belum memenuhi kebutuhan, *sign-off* mungkin tidak diberikan.
    *   Dalam kasus ini, Anda perlu:
        *   Melaporkan *bug* yang menghambat *sign-off*.
        *   Bekerja sama dengan tim *engineering* untuk memperbaikinya.
        *   Mengulang sebagian atau seluruh proses UAT setelah perbaikan.

*   **[ ] Jika *Sign-off* Diterima:**
    *   Segera beri tahu PM dan tim *engineering* bahwa fitur "Siap untuk Rilis". Ini adalah sinyal bahwa semua pintu kualitas telah dibuka.

Koordinasi UAT yang baik memastikan bahwa produk yang dirilis tidak hanya berfungsi dengan benar secara teknis, tetapi juga memenuhi ekspektasi dan kebutuhan bisnis pengguna.

---

## 4. Handoff: Notifikasi PM saat Siklus QA Selesai

Setelah semua pengujian selesai, *bug* kritis diperbaiki, dan UAT telah disetujui, tiba saatnya untuk secara resmi memberi tahu Product Manager bahwa siklus QA untuk fitur tersebut telah selesai. Ini adalah **handoff** yang penting, menandakan bahwa tanggung jawab selanjutnya ada di tangan PM untuk merencanakan rilis.

Handoff ini harus jelas, ringkas, dan berisi semua informasi yang relevan. Ini bukan sekadar "sudah selesai ya", tetapi sebuah notifikasi formal yang berisi rangkuman status dan artefak penting.

```python
from handoff import handoff_to_pm

handoff_to_pm(
    from_agent="qa-thomas",
    title=f"QA complete: {feature_name}",
    priority="P1",
    epic_id=epic_id,
    summary="UAT signed off. Test report attached. Ready for release.",
    body_markdown=f"""
## Status
Siklus QA selesai. Semua kriteria *exit* telah terpenuhi.

## Artefak
- Strategi Pengujian: {strategy_url}
- Test Case: {test_cases_url}
- Laporan Eksekusi: {report_url}
- Laporan UAT: {uat_url}
- Draf Release Notes: {notes_url}

## Langkah Selanjutnya yang Direkomendasikan
- PM: Konfirmasi jendela rilis
- Marketing: Handoff peluncuran (sesuai arahan Pimpinan Thomas tentang koordinasi Marketing)
- Tech Lead: Rencana *deployment*
""",
)
```

Mari kita bedah template `handoff_to_pm` ini:

*   **`from_agent="qa-thomas"`**: Menunjukkan siapa yang melakukan *handoff*. Ini penting untuk akuntabilitas.
*   **`title=f"QA complete: {feature_name}"`**: Judul yang jelas dan langsung menunjukkan fitur mana yang telah selesai diuji.
*   **`priority="P1"`**: Menunjukkan bahwa ini adalah notifikasi penting yang membutuhkan perhatian segera dari PM.
*   **`epic_id=epic_id`**: Mengaitkan *handoff* ini dengan *epic* atau proyek yang lebih besar.
*   **`summary="UAT signed off. Test report attached. Ready for release."`**: Ringkasan singkat yang memberikan gambaran cepat tentang status.
*   **`body_markdown`**: Ini adalah bagian paling detail, berisi informasi penting dalam format Markdown.

    *   **`## Status`**: Konfirmasi bahwa siklus QA telah selesai dan semua kriteria *exit* (seperti semua *test case* kritis lolos, *bug* P0/P1 ditutup, UAT selesai) telah terpenuhi.
    *   **`## Artefak`**: Daftar tautan ke semua dokumen penting yang dihasilkan selama siklus QA. Ini memudahkan PM untuk mengakses bukti pengujian dan laporan.
        *   `strategy_url`: Tautan ke dokumen strategi pengujian.
        *   `test_cases_url`: Tautan ke kumpulan *test case*.
        *   `report_url`: Tautan ke laporan eksekusi pengujian.
        *   `uat_url`: Tautan ke laporan UAT.
        *   `notes_url`: Tautan ke draf *release notes* (yang mungkin sudah Anda bantu siapkan, seperti dibahas di Chapter 05).
    *   **`## Langkah Selanjutnya yang Direkomendasikan`**: Ini adalah bagian proaktif. Anda tidak hanya melaporkan status, tetapi juga menyarankan tindakan selanjutnya untuk PM dan tim lain. Ini menunjukkan bahwa Anda berpikir ke depan dan membantu melancarkan proses rilis.
        *   Untuk PM: Konfirmasi jadwal rilis.
        *   Untuk Marketing: Koordinasi peluncuran (jika ada).
        *   Untuk Tech Lead: Rencana *deployment*.

Melakukan *handoff* seperti ini menunjukkan profesionalisme, efisiensi, dan memastikan tidak ada miskomunikasi tentang status kualitas fitur. Ini adalah momen Anda untuk menyerahkan tongkat estafet ke PM dengan percaya diri.

---

## 5. Perilaku Buruk yang Harus Dihindari oleh QA

Dalam perjalanan Anda sebagai QA Engineer, akan ada godaan atau kebiasaan buruk yang bisa merusak kredibilitas Anda dan kualitas produk. Mengenali dan menghindari perilaku ini sangat penting untuk menjadi QA yang efektif dan dihormati.

Berikut adalah beberapa perilaku buruk yang harus Anda hindari:

### a. Menyetujui Rilis di Bawah Tekanan padahal Kriteria Belum Terpenuhi
*   **Perilaku Buruk:** Anda tahu ada *bug* kritis yang belum diperbaiki, atau UAT belum selesai, tetapi tim ingin segera rilis. Anda merasa tertekan untuk memberikan *sign-off* agar tidak menghambat jadwal.
*   **Mengapa Buruk:** Anda adalah *gatekeeper* kualitas. Jika Anda menyetujui rilis di bawah tekanan, Anda mengorbankan kualitas produk dan berpotensi menyebabkan masalah serius bagi pengguna dan reputasi perusahaan. Ini juga merusak kredibilitas Anda sebagai QA.
*   **Yang Seharusnya:** Tegaslah pada kriteria *exit* yang telah disepakati. Jelaskan risiko yang ada dan dampak potensialnya jika rilis dilakukan tanpa memenuhi kriteria. Tawarkan solusi alternatif, seperti menunda rilis, melakukan *patch* cepat, atau merilis sebagian fitur.

    *Contoh Dialog:*
    *PM:* "Thomas, kita harus rilis besok pagi. Bisnis sudah menunggu. Tolong *sign-off* ya."
    *Thomas:* "Maaf, [Nama PM]. Saya belum bisa memberikan *sign-off*. *Bug* P0 'Pembayaran Gagal' masih terbuka, dan itu akan memblokir pengguna utama kita. Jika kita rilis dengan *bug* ini, kita berisiko kehilangan banyak transaksi dan merusak pengalaman pengguna."
    *PM:* "Tapi kita sudah janji!"
    *Thomas:* "Saya mengerti urgensinya. Alternatifnya, kita bisa menunda rilis sehari untuk memperbaiki *bug* ini, atau kita bisa melakukan *rollback* fitur pembayaran ini dan merilis sisanya terlebih dahulu. Mana yang lebih baik menurut Anda?"

### b. Melaporkan *Bug* Sekaligus di Akhir Siklus Pengujian
*   **Perilaku Buruk:** Anda menemukan *bug* saat pengujian, tetapi Anda menunda pelaporannya dan mengumpulkannya untuk dilaporkan sekaligus di akhir siklus.
*   **Mengapa Buruk:** Ini melanggar prinsip "fail fast". *Bug* yang dilaporkan terlambat memberikan waktu yang lebih sedikit bagi *developer* untuk memperbaikinya, meningkatkan *pressure*, dan berpotensi menyebabkan *rework* yang lebih besar karena *developer* mungkin sudah membangun fitur lain di atas *bug* tersebut.
*   **Yang Seharusnya:** Laporkan *bug* segera setelah Anda menemukannya. Berikan detail yang jelas agar *developer* dapat mereproduksinya dan memperbaikinya sesegera mungkin. Ini menghemat waktu, mengurangi biaya perbaikan, dan menjaga kualitas tetap tinggi sepanjang siklus pengembangan.

### c. Melewatkan UAT untuk Fitur "Sederhana"
*   **Perilaku Buruk:** Anda berpikir fitur tertentu terlalu sederhana dan tidak perlu UAT, atau PM mengatakan tidak ada waktu untuk UAT.
*   **Mengapa Buruk:** Jika seorang pengguna akan menyentuh fitur tersebut, UAT diperlukan. Fitur yang terlihat sederhana di mata teknis bisa jadi memiliki implikasi bisnis yang kompleks atau alur pengguna yang tidak intuitif. Melewatkan UAT berisiko merilis fitur yang secara teknis berfungsi tetapi tidak memenuhi harapan atau kebutuhan bisnis pengguna.
*   **Yang Seharusnya:** Tekankan pentingnya UAT untuk setiap fitur yang akan digunakan oleh *end-user* atau *business stakeholder*. Jika ada batasan waktu, usulkan UAT yang lebih ringkas atau fokus pada skenario kritis saja, daripada melewatkannya sama sekali.

### d. Melakukan Demo Tanpa Latihan
*   **Perilaku Buruk:** Anda langsung melakukan demo tanpa persiapan, tanpa latihan, atau tanpa rencana cadangan.
*   **Mengapa Buruk:** Demo yang tidak siap bisa menjadi bencana. Masalah teknis, kebingungan dalam navigasi, atau lupa alur bisa membuat Anda terlihat tidak profesional dan merusak kepercayaan *stakeholder* terhadap kualitas produk.
*   **Yang Seharusnya:** Ikuti strategi demo yang telah kita bahas di awal chapter ini: pra-rekaman, demo langsung berbasis skrip, dan siapkan rekaman cadangan. Selalu latihan setidaknya sekali sebelum demo sebenarnya. Pastikan *environment* dan data demo dalam kondisi prima.

Menghindari perilaku buruk ini akan membantu Anda membangun reputasi sebagai QA Engineer yang profesional, dapat diandalkan, dan menjadi aset berharga bagi tim dan perusahaan.

---

## Rangkuman

Chapter ini telah membawa kita melampaui aspek teknis QA dan masuk ke ranah yang sama pentingnya: interaksi dengan pemangku kepentingan (*stakeholder engagement*). Kita telah melihat bahwa seorang QA Engineer yang efektif tidak bekerja dalam isolasi, melainkan sebagai pusat komunikasi yang menghubungkan berbagai tim dan memastikan semua orang selaras dalam tujuan kualitas.

Berikut adalah poin-poin penting yang telah kita bahas:

*   **Strategi Demo yang Aman:** Demo langsung bisa berbahaya, oleh karena itu, kombinasi rekaman otomatis, demo langsung berbasis skrip, dan rekaman cadangan adalah pendekatan terbaik untuk memastikan demo berjalan lancar dan profesional.
*   **Kontribusi Berbobot dalam Meeting:** QA memiliki peran krusial dalam berbagai *meeting* tim, dari *Sprint Planning* hingga *Pre-release Sync*. Kontribusi Anda berupa estimasi pengujian, identifikasi risiko, laporan status, hingga *sign-off* rilis, sangat menentukan arah dan kualitas produk.
*   **Koordinasi UAT yang Efektif:** Sebagai koordinator, Anda memfasilitasi *User Acceptance Testing* dari tahap persiapan (Pra-UAT), pelaksanaan (Selama UAT), hingga tindak lanjut (Pasca-UAT), memastikan produk memenuhi kebutuhan bisnis dan mendapatkan persetujuan dari *stakeholder*.
*   **Handoff Formal ke PM:** Setelah siklus QA selesai, penting untuk melakukan *handoff* yang jelas dan terstruktur kepada Product Manager, berisi status, artefak, dan rekomendasi langkah selanjutnya, menggunakan template yang konsisten.
*   **Menghindari Perilaku Buruk:** Seorang QA yang kredibel akan menghindari menyetujui rilis di bawah tekanan, menunda pelaporan *bug*, melewatkan UAT untuk fitur "sederhana", atau melakukan demo tanpa persiapan.

Dengan menguasai aspek *stakeholder engagement* ini, Anda tidak hanya akan menjadi seorang QA Engineer yang ahli dalam pengujian, tetapi juga pemimpin yang efektif, komunikator yang ulung, dan jembatan yang vital antara tim teknis dan tujuan bisnis.

---

## Checklist Actionable

Berikut adalah daftar tindakan yang bisa Anda terapkan segera untuk meningkatkan *stakeholder engagement* Anda:

*   **[ ] Siapkan Strategi Demo Lengkap:** Untuk demo fitur berikutnya, buat rekaman otomatis, siapkan skrip untuk demo langsung, dan unggah rekaman cadangan ke Drive dengan tautan yang siap dibagikan.
*   **[ ] Tinjau Daftar Meeting Mingguan Anda:** Identifikasi jenis *meeting* yang Anda hadiri dan siapkan 3-5 poin kontribusi berbobot dari perspektif QA untuk setiap *meeting* tersebut.
*   **[ ] Latih Diri Anda untuk Sprint Planning:** Saat *sprint planning* berikutnya, aktiflah dalam memberikan estimasi pengujian dan mengidentifikasi potensi risiko kualitas untuk setiap *user story*.
*   **[ ] Buat Rencana UAT untuk Fitur Mendatang:** Identifikasi fitur yang akan datang dan mulailah menyusun draf rencana UAT (siapa, apa, kapan, kriteria sukses) serta draf skrip UAT yang sederhana.
*   **[ ] Siapkan Saluran Komunikasi UAT:** Jika Anda akan mengoordinasikan UAT, buat saluran Slack atau *platform* komunikasi khusus untuk pertanyaan *real-time* dari partisipan UAT.
*   **[ ] Gunakan Template Handoff ke PM:** Setelah menyelesaikan siklus QA untuk fitur berikutnya, gunakan template `handoff_to_pm` untuk memberi tahu PM secara formal.
*   **[ ] Evaluasi Perilaku Anda:** Refleksikan apakah Anda pernah melakukan salah satu "perilaku buruk" yang dibahas. Jika ya, rencanakan bagaimana Anda akan menghindarinya di masa depan dan berkomitmen untuk menjadi *gatekeeper* kualitas yang tegas.
*   **[ ] Proaktif dalam Bug Triage:** Saat *bug triage*, siaplah untuk memimpin diskusi prioritisasi menggunakan rubrik *severity* yang telah disepakati dan berikan konteks dampak *bug* dari sisi bisnis.
*   **[ ] Selalu Latihan Demo:** Sebelum setiap demo, luangkan waktu 15-30 menit untuk berlatih alur, bahkan jika itu hanya demo singkat untuk tim internal.

Selamat mempraktikkan keterampilan *stakeholder engagement* Anda!
