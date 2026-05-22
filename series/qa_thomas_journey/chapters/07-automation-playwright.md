# Chapter 07: Automation Testing dengan Playwright

Selamat, Anda telah melangkah lebih jauh dalam perjalanan menjadi Quality Assurance Engineer yang andal! Setelah memahami pentingnya analisis *requirement* yang kritis, merancang *test case* yang komprehensif, melaksanakan *testing* secara strategis, melaporkan *bug* dengan efektif, hingga mendokumentasikan dan berinteraksi dengan *stakeholder*, kini saatnya kita membahas pilar berikutnya yang krusial: *Automation Testing*.

Di dunia pengembangan perangkat lunak yang serba cepat, mengandalkan *manual testing* sepenuhnya bisa menjadi hambatan. Proses *testing* yang berulang, terutama untuk *regression testing*, memakan waktu dan rentan terhadap *human error*. Di sinilah *automation testing* berperan. Dengan mengotomatiskan *test case* tertentu, Anda dapat menjalankan *test* lebih cepat, lebih sering, dan dengan konsistensi yang lebih tinggi, membebaskan waktu Anda untuk *exploratory testing* atau fokus pada skenario yang lebih kompleks.

Dalam bab ini, kita akan menyelami Playwright, sebuah *framework automation testing* modern yang kuat dan fleksibel. Kita akan belajar cara menyiapkan proyek Playwright, memahami struktur yang rapi menggunakan *Page Object Model*, mengeksplorasi *data-driven testing*, dan bagaimana menjalankan *test* serta menganalisis laporannya. Bersiaplah untuk meningkatkan kemampuan QA Anda ke level berikutnya!

---

## Mengapa Playwright? Pilihan di Antara Para Raksasa

Ketika berbicara tentang *automation testing* untuk aplikasi web, ada banyak pilihan *tool* di luar sana. Mungkin Anda pernah mendengar tentang Selenium, Cypress, atau Katalon. Di Fairatmos, kami telah beralih sepenuhnya ke Playwright. Mengapa demikian? Mari kita bedah keunggulan Playwright dibandingkan kompetitornya.

### Playwright vs. Selenium
Selenium adalah pelopor di dunia *web automation* dan merupakan *framework* yang sangat matang dengan dukungan komunitas yang besar. Selenium WebDriver memungkinkan Anda mengontrol *browser* dari berbagai bahasa pemrograman (Java, Python, C#, Ruby, JavaScript).

Namun, Selenium memiliki beberapa tantangan:
*   **Setup yang Kompleks**: Membutuhkan konfigurasi WebDriver terpisah untuk setiap *browser*, yang seringkali memakan waktu dan rentan terhadap masalah kompatibilitas versi.
*   **Flakiness**: Tes Selenium seringkali *flaky* (tidak konsisten) karena masalah *timing* atau *race condition*. Anda harus menambahkan *explicit waits* atau *sleep* manual, yang memperlambat eksekusi dan membuat *script* kurang stabil.
*   **Debugging yang Sulit**: Laporan *error* terkadang kurang informatif, dan *debugging* bisa menjadi proses yang rumit.

Playwright hadir untuk mengatasi banyak masalah ini. Playwright dibangun dengan arsitektur yang lebih modern, memungkinkan interaksi langsung dengan *browser* tanpa perantara WebDriver.

### Playwright vs. Cypress
Cypress adalah *framework* yang relatif baru dan sangat populer di kalangan *developer* karena kemudahan penggunaannya dan pengalaman *developer* yang luar biasa. Cypress berjalan di dalam *browser*, yang membuatnya sangat cepat dalam eksekusi dan *debugging*.

Meskipun demikian, Cypress memiliki beberapa batasan:
*   **Dukungan Browser Terbatas**: Secara historis, Cypress hanya mendukung *browser* berbasis Chromium dan Firefox. Dukungan WebKit (Safari) baru ditambahkan belakangan dan masih dalam pengembangan.
*   **Single-Origin Policy**: Cypress terikat pada *single-origin policy* *browser*, yang menyulitkan pengujian skenario yang melibatkan interaksi dengan *domain* atau *tab* yang berbeda.
*   **Tidak Ada Akses API Langsung**: Meskipun bisa melakukan *network requests*, Cypress tidak dirancang untuk *API testing* *first-class* seperti Playwright.

Playwright, di sisi lain, menawarkan dukungan penuh untuk Chromium, Firefox, dan WebKit (Safari) secara *out-of-the-box*. Playwright juga dapat menguji skenario multi-*tab* dan multi-*domain* dengan mudah, serta memiliki dukungan *API testing* yang sangat baik.

### Playwright vs. Katalon
Katalon Studio adalah *tool automation testing* yang *low-code/no-code*, yang sangat cocok untuk pemula atau tim yang ingin memulai *automation* dengan cepat tanpa harus menulis banyak kode. Katalon menyediakan *recorder* untuk merekam interaksi pengguna dan menghasilkan *script* secara otomatis.

Kelemahan Katalon muncul ketika Anda membutuhkan fleksibilitas tinggi atau skenario *testing* yang sangat kompleks:
*   **Keterbatasan Kustomisasi**: Meskipun memungkinkan penulisan *script* Groovy, Katalon bisa menjadi kurang fleksibel dibandingkan *framework* berbasis kode murni seperti Playwright saat menghadapi logika yang rumit atau integrasi khusus.
*   **Performa**: Eksekusi *test* di Katalon bisa lebih lambat dibandingkan *framework* modern yang dioptimalkan untuk kecepatan.
*   **Vendor Lock-in**: Ketergantungan pada ekosistem Katalon bisa menjadi masalah jika Anda ingin beralih ke *tool* lain di masa mendatang.

Di Fairatmos, kami juga pernah menggunakan Katalon, tetapi seiring dengan kebutuhan *testing* yang semakin kompleks dan cepat, kami memutuskan untuk beralih ke Playwright. Migrasi ini memungkinkan kami untuk memiliki kontrol penuh atas *script*, mengoptimalkan performa, dan memanfaatkan kekuatan TypeScript untuk *type safety*.

### Keunggulan Playwright

Jadi, mengapa Playwright menjadi pilihan kami? Berikut adalah beberapa karakteristik utama yang membuatnya menonjol:

1.  **Cross-Browser Penuh**: Playwright mendukung Chromium (Chrome, Edge), Firefox, dan WebKit (Safari) secara *native* hanya dengan satu API. Anda dapat menguji aplikasi Anda di ketiga mesin *browser* utama, memastikan kompatibilitas yang luas.
2.  **Auto-Waiting**: Playwright secara cerdas menunggu elemen siap sebelum berinterinteraksi dengannya. Ini secara signifikan mengurangi *flakiness* *test* dan menghilangkan kebutuhan akan *explicit waits* manual, membuat *script* Anda lebih stabil dan mudah ditulis.
3.  **API Testing First-Class**: Playwright memiliki API bawaan untuk melakukan *network requests* (HTTP/HTTPS). Ini berarti Anda dapat melakukan *API testing* di samping *UI testing* dalam *framework* yang sama, bahkan menggunakannya untuk menyiapkan *test data* tanpa harus membuka *browser*.
4.  **Trace Viewer, Screenshots, dan Video Otomatis**: Untuk setiap eksekusi *test* yang gagal, Playwright dapat secara otomatis merekam *trace* (langkah-langkah interaksi), mengambil *screenshot*, dan merekam video. Fitur ini sangat membantu dalam *debugging* dan memahami mengapa suatu *test* gagal.
5.  **Parallelization**: Playwright dirancang untuk menjalankan *test* secara paralel secara *default*, baik di *browser* yang berbeda maupun di *worker* yang berbeda dalam *browser* yang sama. Ini mempercepat waktu eksekusi *test suite* secara drastis.
6.  **TypeScript Support**: Playwright memiliki dukungan TypeScript yang sangat baik, memungkinkan Anda menulis *test* dengan *type safety*, *autocompletion*, dan *refactoring* yang lebih mudah.

Dengan kombinasi fitur-fitur ini, Playwright memberikan pengalaman *automation testing* yang modern, efisien, dan andal.

---

## Struktur Proyek Automation Playwright

Proyek *automation testing* yang baik harus memiliki struktur folder yang terorganisir dengan rapi. Ini meningkatkan keterbacaan, kemudahan pemeliharaan, dan skalabilitas. Di Fairatmos, proyek Playwright kami diatur sebagai berikut:

```
automation-playwright/
├─ playwright.config.ts        # Konfigurasi runner & browser Playwright
├─ tsconfig.json               # Konfigurasi TypeScript
├─ package.json                # Metadata proyek & daftar dependensi
├─ .env.example                # Template variabel lingkungan (environment variables)
├─ api/                        # Modul untuk interaksi API
│  └─ auth.api.ts              # Contoh: wrapper untuk POST /api/v1/user/sign-in
├─ helpers/                    # Fungsi-fungsi utilitas umum
│  └─ customize.ts             # Contoh: waitForText, fill by testId
├─ pages/                      # Implementasi Page Object Model (POM)
│  ├─ login.page.ts            # Objek halaman untuk alur login
│  ├─ register.page.ts         # Objek halaman untuk registrasi user baru
│  ├─ forgot-password.page.ts  # Objek halaman untuk alur forgot password
│  ├─ profile.page.ts          # Objek halaman untuk profil user, logout
│  ├─ dashboard.page.ts        # Objek halaman untuk dashboard
│  ├─ forestry.page.ts         # Objek halaman untuk pertanyaan Forestry
│  ├─ shapefile.page.ts        # Objek halaman untuk upload shapefile
│  ├─ review.page.ts           # Objek halaman untuk halaman review proyek
│  └─ result.page.ts           # Objek halaman untuk halaman hasil proyek
├─ data/                       # Data uji (test data) untuk skenario data-driven
│  └─ shapefile.data.ts        # Contoh: data untuk upload shapefile
├─ test-data/                  # File data biner yang dibutuhkan test
│  └─ Shapefile/atmostalk/     # Contoh: file .shp/.shx/.dbf/.prj
├─ qa-docs/                    # Dokumentasi QA terkait (test design, UAT, bug list)
├─ scripts/                    # Script utilitas (misal: integrasi Slack)
│  ├─ slack-connector.ts
│  ├─ bug-parser.ts
│  └─ report-bugs.ts
└─ tests/                      # File test spec (skenario pengujian)
   ├─ smoke.spec.ts            # Test smoke untuk sanity check
   ├─ login/                   # Kumpulan test untuk alur login
   │  ├─ login-valid.spec.ts
   │  ├─ login-incorrect-email.spec.ts
   │  ├─ login-incorrect-password.spec.ts
   │  └─ login-api.spec.ts
   ├─ forgot-password/         # Kumpulan test untuk alur forgot password
   │  ├─ forgot-password.spec.ts
   │  └─ forgot-password-email-not-exist.spec.ts
   ├─ homepage/                # Kumpulan test untuk halaman utama
   │  ├─ register.spec.ts
   │  ├─ logout.spec.ts
   │  └─ new-dashboard.spec.ts
   └─ forestry/                # Kumpulan test untuk modul forestry
      └─ upload-shapefile.spec.ts
```

Mari kita jelaskan setiap bagian penting dari struktur ini:

*   **`playwright.config.ts`**: Ini adalah jantung konfigurasi Playwright Anda. Di sini Anda menentukan *browser* apa yang akan digunakan, berapa banyak *worker* yang akan dijalankan secara paralel, *timeout*, *base URL*, dan opsi *reporting* seperti perekaman video atau *screenshot*.
*   **`tsconfig.json`**: File konfigurasi untuk TypeScript. Mengatur bagaimana kode TypeScript Anda akan dikompilasi menjadi JavaScript.
*   **`package.json`**: File standar Node.js yang berisi metadata proyek, seperti nama, versi, *script* yang dapat dijalankan (`npm test`, `npm run report`), dan daftar semua dependensi (paket *library* pihak ketiga) yang dibutuhkan proyek.
*   **`.env.example`**: Contoh file untuk variabel lingkungan. Anda akan menyalinnya menjadi `.env` dan mengisi kredensial sensitif seperti `TEST_EMAIL` dan `TEST_PASSWORD` yang tidak boleh di-*commit* ke *repository* kode.
*   **`api/`**: Folder ini berisi fungsi-fungsi *wrapper* untuk interaksi dengan *API backend* aplikasi Anda. Mengapa penting? Anda dapat menggunakannya untuk menyiapkan data uji (misalnya, membuat pengguna baru via API) atau bahkan menguji *endpoint* API secara langsung tanpa perlu membuka *browser*, yang jauh lebih cepat.
*   **`helpers/`**: Berisi fungsi-fungsi utilitas atau *custom commands* yang dapat digunakan kembali di berbagai *test case* atau *Page Object*. Contohnya bisa berupa fungsi untuk menunggu teks tertentu muncul, mengisi *field* berdasarkan `testId`, atau *assertion* yang sering digunakan.
*   **`pages/`**: Ini adalah implementasi dari pola desain *Page Object Model* (POM). Setiap file di sini mewakili sebuah halaman atau komponen utama dalam aplikasi Anda. Kita akan membahas ini lebih detail di bagian selanjutnya.
*   **`data/`**: Folder ini dikhususkan untuk menyimpan data uji. Daripada menanamkan data langsung ke dalam *test script*, memisahkannya ke dalam file terpisah memungkinkan Anda mengelola data dengan lebih baik, terutama untuk skenario *data-driven testing*.
*   **`test-data/`**: Untuk menyimpan file data biner yang dibutuhkan oleh *test*, seperti *shapefile* (`.shp`, `.shx`, `.dbf`, `.prj`) yang digunakan dalam *test* Forestry. Memisahkannya dari kode memastikan *repository* tetap rapi.
*   **`qa-docs/`**: Meskipun bukan bagian dari *automation script* itu sendiri, folder ini menunjukkan integrasi dengan dokumentasi QA. Ini bisa berisi *test design*, *execution reports*, *bug list*, dan *UAT reports*.
*   **`scripts/`**: Folder untuk *script* utilitas yang tidak langsung terkait dengan *testing*, seperti *script* untuk integrasi Slack atau *parsing bug report*.
*   **`tests/`**: Ini adalah tempat semua *test spec* (file yang berisi skenario pengujian) Anda berada. Biasanya diatur dalam sub-folder berdasarkan fitur atau modul aplikasi, seperti `login/`, `forgot-password/`, atau `forestry/`.

Struktur ini memastikan bahwa kode *automation* Anda modular, mudah dinavigasi, dan siap untuk dikembangkan seiring bertambahnya kompleksitas aplikasi Anda.

---

## Page Object Model (POM): Membangun Abstraksi Halaman

*Page Object Model* (POM) adalah pola desain yang sangat populer dalam *automation testing* untuk aplikasi web. Tujuannya adalah untuk membuat abstraksi dari halaman-halaman antarmuka pengguna (UI) aplikasi Anda menjadi objek-objek kode.

### Mengapa Menggunakan POM?

1.  **Keterbacaan (Readability)**: *Test case* menjadi lebih mudah dibaca karena tidak lagi berisi detail implementasi UI. Sebagai gantinya, *test case* akan memanggil metode pada *Page Object* yang merepresentasikan tindakan pengguna.
2.  **Pemeliharaan (Maintainability)**: Jika UI aplikasi berubah (misalnya, *locator* elemen berubah), Anda hanya perlu memperbarui *Page Object* yang relevan, bukan setiap *test case* yang menggunakan elemen tersebut. Ini mengurangi upaya pemeliharaan secara drastis.
3.  **Penggunaan Kembali (Reusability)**: Logika interaksi dengan halaman dapat digunakan kembali di berbagai *test case*. Misalnya, *flow* login dapat digunakan sebagai prasyarat untuk banyak *test case* lainnya.

### Cara Kerja POM di Playwright

Di Playwright, Anda akan membuat sebuah kelas (class) untuk setiap halaman atau komponen utama aplikasi Anda. Kelas ini akan berisi:

*   **Locators**: Properti yang mendefinisikan cara menemukan elemen UI di halaman (misalnya, tombol, *input field*, *dropdown*). Playwright memiliki *locator* yang sangat kuat, seperti `getByRole`, `getByText`, `getByLabel`, `getByPlaceholder`, `getByTestId`, dan `locator` umum.
*   **Methods**: Fungsi-fungsi yang merepresentasikan tindakan pengguna atau interaksi dengan elemen di halaman tersebut. Misalnya, `fillEmail`, `clickLoginButton`, `verifyErrorMessage`.

Mari kita lihat contoh implementasi POM untuk alur login di Fairatmos.

### Contoh Nyata: Login Flow

Anggap kita memiliki halaman login dengan *field* email, *password*, dan tombol login.

#### 1. Membuat `LoginPage` Page Object (`pages/login.page.ts`)

```typescript
// automation-playwright/pages/login.page.ts

import { expect, Locator, Page } from '@playwright/test';
import { CustomHelper } from '../helpers/customize'; // Asumsi ada helper

export class LoginPage {
  readonly page: Page;
  readonly emailInput: Locator;
  readonly passwordInput: Locator;
  readonly loginButton: Locator;
  readonly errorMessageToast: Locator;
  readonly helper: CustomHelper;

  constructor(page: Page) {
    this.page = page;
    this.helper = new CustomHelper(page); // Inisialisasi helper
    this.emailInput = page.getByPlaceholder('Masukkan email Anda');
    this.passwordInput = page.getByPlaceholder('Masukkan password Anda');
    // Menggunakan getByRole untuk tombol Login
    this.loginButton = page.getByRole('button', { name: 'Login' });
    // Menggunakan locator yang lebih spesifik jika ada toast message
    this.errorMessageToast = page.locator('.Toastify__toast--error');
  }

  async navigateToLogin() {
    await this.page.goto('/login'); // Asumsi base URL sudah dikonfigurasi
  }

  async login(email: string, password_input: string) {
    await this.emailInput.fill(email);
    await this.passwordInput.fill(password_input);
    await this.loginButton.click();
  }

  async verifyLoginSuccess() {
    // Asumsi setelah login berhasil akan diarahkan ke dashboard
    await expect(this.page).toHaveURL(/dashboard/);
    // Atau bisa juga menunggu elemen tertentu di dashboard muncul
    await expect(this.page.getByText('Selamat Datang di Fairatmos')).toBeVisible();
  }

  async verifyLoginFailedMessage(message: string) {
    await expect(this.errorMessageToast).toBeVisible();
    await expect(this.errorMessageToast).toContainText(message);
  }

  // Contoh metode lain menggunakan helper (jika ada)
  async fillEmailByTestId(email: string) {
      await this.helper.fillByTestId('email-field', email);
  }
}
```

**Penjelasan:**

*   `constructor(page: Page)`: Mengambil objek `page` dari Playwright, yang merupakan representasi halaman *browser*. Semua interaksi akan melalui objek `page` ini.
*   `readonly emailInput: Locator;`: Mendefinisikan *locator* untuk *field* email. Kita menggunakan `page.getByPlaceholder()` yang merupakan salah satu *smart locator* Playwright.
*   `async navigateToLogin()`: Metode untuk menavigasi ke halaman login.
*   `async login(email: string, password_input: string)`: Metode utama untuk melakukan alur login. Ini mengabstraksi detail pengisian *field* dan klik tombol.
*   `async verifyLoginSuccess()`: Metode untuk melakukan *assertion* setelah login berhasil.
*   `async verifyLoginFailedMessage(message: string)`: Metode untuk memverifikasi pesan *error* jika login gagal.

#### 2. Menggunakan `LoginPage` di Test Spec (`tests/login/login-valid.spec.ts`)

Sekarang, mari kita lihat bagaimana *Page Object* ini digunakan dalam *test spec* untuk skenario login yang valid.

```typescript
// automation-playwright/tests/login/login-valid.spec.ts

import { test, expect } from '@playwright/test';
import { LoginPage } from '../../pages/login.page'; // Import Page Object
import * as dotenv from 'dotenv';

dotenv.config(); // Memuat variabel lingkungan dari file .env

test.describe('Login Flow', () => {
  let loginPage: LoginPage; // Deklarasikan variabel LoginPage

  test.beforeEach(async ({ page }) => {
    loginPage = new LoginPage(page); // Inisialisasi LoginPage sebelum setiap test
    await loginPage.navigateToLogin(); // Navigasi ke halaman login
  });

  test('should allow a user to log in with valid credentials', async () => {
    // Mengambil kredensial dari environment variables
    const email = process.env.TEST_EMAIL || 'default@example.com';
    const password = process.env.TEST_PASSWORD || 'password123';

    // Panggil metode login dari Page Object
    await loginPage.login(email, password);

    // Panggil metode verifikasi dari Page Object
    await loginPage.verifyLoginSuccess();

    console.log(`Login berhasil untuk user: ${email}`);
  });

  test('should show error message for incorrect password', async () => {
    const email = process.env.TEST_EMAIL || 'default@example.com';
    const incorrectPassword = 'wrongpassword';

    await loginPage.login(email, incorrectPassword);
    await loginPage.verifyLoginFailedMessage('Email atau password salah');
  });

  test('should show error message for non-existent email', async () => {
    const nonExistentEmail = 'nonexistent@example.com';
    const anyPassword = 'anypassword';

    await loginPage.login(nonExistentEmail, anyPassword);
    await loginPage.verifyLoginFailedMessage('Email atau password salah');
  });
});
```

**Penjelasan:**

*   `import { LoginPage } from '../../pages/login.page';`: Mengimpor *Page Object* yang telah kita buat.
*   `test.beforeEach`: Sebelum setiap *test* dijalankan, kita membuat instance `LoginPage` baru dan menavigasi ke halaman login. Ini memastikan setiap *test* dimulai dari kondisi yang bersih.
*   `await loginPage.login(email, password);`: *Test case* menjadi sangat ringkas dan mudah dibaca. Ia hanya memanggil metode `login` pada objek `loginPage`, tanpa perlu tahu *locator* atau langkah-langkah detail di baliknya.
*   `await loginPage.verifyLoginSuccess();`: Demikian pula, verifikasi juga dilakukan melalui metode pada *Page Object*.

Dengan POM, jika *locator* untuk *field* email berubah dari `getByPlaceholder('Masukkan email Anda')` menjadi `getByLabel('Email Address')`, Anda hanya perlu mengubahnya di satu tempat: yaitu di file `login.page.ts`. Semua *test case* yang menggunakan `loginPage.emailInput` akan otomatis terbarui tanpa perubahan pada *test spec* itu sendiri. Ini adalah kekuatan utama dari *Page Object Model*.

---

## Data-Driven Testing: Menguji dengan Berbagai Data

Dalam *automation testing*, seringkali Anda perlu menjalankan *test case* yang sama berulang kali dengan *input data* yang berbeda. Misalnya, menguji formulir dengan berbagai kombinasi data valid/invalid, atau mengunggah berbagai jenis file. Ini disebut *Data-Driven Testing*.

*Data-driven testing* membantu Anda:
*   **Meningkatkan Cakupan (Coverage)**: Menguji lebih banyak skenario dengan data yang bervariasi.
*   **Mengurangi Duplikasi Kode**: Logika *test* tetap sama, hanya datanya yang berubah.
*   **Memudahkan Pemeliharaan Data**: Data uji disimpan secara terpisah dari logika *test*.

Di Playwright dengan TypeScript, kita dapat mengimplementasikan *data-driven testing* dengan menyimpan data dalam file TypeScript terpisah dan mengulanginya dalam *test spec*.

### Contoh Nyata: Upload Shapefile

Di Fairatmos, salah satu fitur penting adalah kemampuan untuk mengunggah *shapefile* untuk proyek kehutanan. Proses ini melibatkan pengunggahan empat jenis file (`.shp`, `.shx`, `.dbf`, `.prj`) secara bersamaan. Kita perlu menguji ini dengan berbagai set *shapefile* yang berbeda (misalnya, dari lokasi yang berbeda, atau yang mungkin memiliki karakteristik khusus).

#### 1. Menyimpan Data Uji (`data/shapefile.data.ts`)

Kita akan membuat sebuah *array* objek yang setiap objeknya merepresentasikan satu set data *shapefile* yang akan diunggah.

```typescript
// automation-playwright/data/shapefile.data.ts

export interface ShapefileData {
  id: string; // ID unik untuk setiap set data
  name: string; // Nama untuk identifikasi dalam laporan
  folder: string; // Nama folder tempat file shapefile berada
  projectName: string; // Nama proyek yang akan diinput
  expectedCarbonCredit?: string; // Opsional: nilai kredit karbon yang diharapkan
  expectedScore?: string; // Opsional: skor yang diharapkan
}

export const shapefileDatasets: ShapefileData[] = [
  {
    id: 'cilacap_srn',
    name: 'Cilacap SRN',
    folder: 'cilacap',
    projectName: 'Proyek Cilacap SRN Otomatis',
    expectedCarbonCredit: '1000', // Contoh nilai yang diharapkan
    expectedScore: '85',
  },
  {
    id: 'bug1_verra',
    name: 'Bug Fix Test Verra',
    folder: 'bug1',
    projectName: 'Proyek Bug Fix 1 Verra Otomatis',
    expectedCarbonCredit: '500',
    expectedScore: '70',
  },
  {
    id: 'bug2_srn',
    name: 'Bug Fix Test SRN',
    folder: 'bug2',
    projectName: 'Proyek Bug Fix 2 SRN Otomatis',
    expectedCarbonCredit: '1200',
    expectedScore: '90',
  },
  // Anda bisa menambahkan lebih banyak set data di sini
];
```

**Penjelasan:**

*   `export interface ShapefileData`: Mendefinisikan *interface* TypeScript untuk struktur data setiap *dataset*. Ini memberikan *type safety* dan *autocompletion*.
*   `export const shapefileDatasets: ShapefileData[]`: Sebuah *array* dari objek `ShapefileData`. Setiap objek adalah satu set data yang akan digunakan untuk satu eksekusi *test*.
*   `folder`: Ini akan digunakan untuk menemukan file *shapefile* yang sebenarnya di `test-data/Shapefile/atmostalk/`. Misalnya, `test-data/Shapefile/atmostalk/cilacap/` akan berisi `.shp`, `.shx`, `.dbf`, `.prj` untuk *dataset* 'cilacap_srn'.

#### 2. Menggunakan Data di Test Spec (`tests/forestry/upload-shapefile.spec.ts`)

Sekarang, kita akan membuat *test spec* yang akan mengulang melalui `shapefileDatasets` dan menjalankan logika *upload shapefile* untuk setiap *dataset*.

```typescript
// automation-playwright/tests/forestry/upload-shapefile.spec.ts

import { test, expect } from '@playwright/test';
import { LoginPage } from '../../pages/login.page';
import { DashboardPage } from '../../pages/dashboard.page';
import { ForestryPage } from '../../pages/forestry.page';
import { ShapefilePage } from '../../pages/shapefile.page';
import { ReviewPage } from '../../pages/review.page';
import { ResultPage } from '../../pages/result.page';
import { shapefileDatasets, ShapefileData } from '../../data/shapefile.data'; // Import data
import * as path from 'path';
import * as dotenv from 'dotenv';

dotenv.config();

// Definisikan path dasar ke folder shapefile
const SHAPEFILE_BASE_DIR = process.env.SHAPEFILE_DIR || path.resolve(__dirname, '../../test-data/Shapefile/atmostalk');

test.describe('Forestry Project - Upload Shapefile (Data-Driven)', () => {
  let loginPage: LoginPage;
  let dashboardPage: DashboardPage;
  let forestryPage: ForestryPage;
  let shapefilePage: ShapefilePage;
  let reviewPage: ReviewPage;
  let resultPage: ResultPage;

  test.beforeEach(async ({ page }) => {
    loginPage = new LoginPage(page);
    dashboardPage = new DashboardPage(page);
    forestryPage = new ForestryPage(page);
    shapefilePage = new ShapefilePage(page);
    reviewPage = new ReviewPage(page);
    resultPage = new ResultPage(page);

    // Prasyarat: Login sebagai user test
    await loginPage.navigateToLogin();
    await loginPage.login(process.env.TEST_EMAIL!, process.env.TEST_PASSWORD!);
    await loginPage.verifyLoginSuccess();
    await dashboardPage.closeWelcomeModalIfVisible(); // Tutup modal selamat datang jika ada
  });

  // Iterasi melalui setiap dataset shapefile
  for (const dataset of shapefileDatasets) {
    test(`should successfully upload shapefile for ${dataset.name}`, async () => {
      await test.step('Mulai proyek Forestry baru', async () => {
        await dashboardPage.clickNewProjectButton();
        await dashboardPage.selectForestryProject();
      });

      await test.step('Jawab pertanyaan Forestry', async () => {
        // Asumsi ada metode untuk menjawab pertanyaan di ForestryPage
        await forestryPage.answerAllQuestions();
        await forestryPage.clickNextButton();
      });

      await test.step(`Upload shapefile dari folder ${dataset.folder}`, async () => {
        const folderPath = path.join(SHAPEFILE_BASE_DIR, dataset.folder);
        const shpPath = path.join(folderPath, `${dataset.folder}.shp`);
        const shxPath = path.join(folderPath, `${dataset.folder}.shx`);
        const dbfPath = path.join(folderPath, `${dataset.folder}.dbf`);
        const prjPath = path.join(folderPath, `${dataset.folder}.prj`);

        await shapefilePage.uploadShapefiles([shpPath, shxPath, dbfPath, prjPath]);
        await shapefilePage.waitForUploadProgressToComplete();
        await shapefilePage.clickNextButton();
      });

      await test.step(`Review dan beri nama proyek: ${dataset.projectName}`, async () => {
        await reviewPage.inputProjectName(dataset.projectName);
        await reviewPage.clickContinueButton();
      });

      await test.step('Verifikasi halaman hasil', async () => {
        await resultPage.waitForResultPageLoad();
        await resultPage.verifyProjectName(dataset.projectName);
        // Lakukan assertion berdasarkan data yang diharapkan dari dataset
        if (dataset.expectedCarbonCredit) {
          await resultPage.verifyCarbonCredit(dataset.expectedCarbonCredit);
        }
        if (dataset.expectedScore) {
          await resultPage.verifyProjectScore(dataset.expectedScore);
        }
        // Tambahkan assertion lain sesuai kebutuhan
      });
    });
  }
});
```

**Penjelasan:**

*   `import { shapefileDatasets, ShapefileData } from '../../data/shapefile.data';`: Mengimpor data uji yang telah kita definisikan.
*   `for (const dataset of shapefileDatasets)`: Ini adalah inti dari *data-driven testing*. Kita menggunakan perulangan `for...of` untuk mengiterasi setiap objek `dataset` dalam *array* `shapefileDatasets`.
*   `test(`should successfully upload shapefile for ${dataset.name}`, async () => { ... });`: Untuk setiap `dataset`, kita mendefinisikan sebuah *test case* baru. Nama *test case* dibuat dinamis menggunakan `dataset.name` agar mudah diidentifikasi dalam laporan.
*   `const folderPath = path.join(SHAPEFILE_BASE_DIR, dataset.folder);`: Kita menggunakan modul `path` dari Node.js untuk menggabungkan jalur file. `SHAPEFILE_BASE_DIR` diambil dari variabel lingkungan atau *path* default.
*   `await shapefilePage.uploadShapefiles([...]);`: Metode ini (yang akan ada di `pages/shapefile.page.ts`) akan bertanggung jawab untuk memilih dan mengunggah file-file tersebut.

Dengan pendekatan ini, Anda dapat dengan mudah menambahkan *dataset* baru ke `shapefile.data.ts` tanpa perlu mengubah logika *test* di `upload-shapefile.spec.ts`. Setiap penambahan *dataset* akan otomatis membuat *test case* baru yang akan dieksekusi, memastikan cakupan yang luas dengan kode yang efisien.

---

## Menjalankan Test Otomatis & Melihat Laporan

Setelah Anda menulis *test case*, langkah selanjutnya adalah menjalankannya dan menganalisis hasilnya. Playwright menyediakan berbagai perintah untuk menjalankan *test* Anda, dari eksekusi *headless* cepat hingga mode UI interaktif untuk *debugging*.

### Setup Pertama Kali

Sebelum menjalankan *test*, pastikan Anda sudah melakukan *setup* proyek:

```bash
cd automation-playwright
npm install                          # Menginstal semua dependensi
npx playwright install --with-deps chromium # Menginstal browser Chromium Playwright
copy .env.example .env               # Salin template env
# Lalu isi file .env dengan kredensial TEST_EMAIL, TEST_PASSWORD, dll.
```

### Perintah Penting untuk Menjalankan Test

| Perintah                        | Fungsi                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
| `npm test`                      | Menjalankan semua tes secara *headless* (tanpa membuka GUI *browser*). Ini adalah mode default untuk eksekusi cepat di CI/CD. |
| `npm run test:headed`           | Sama seperti `npm test`, tetapi *browser* akan terlihat saat *test* berjalan. Berguna untuk melihat interaksi secara visual saat *debugging*. |
| `npm run test:ui`               | Membuka Playwright UI. Ini adalah mode interaktif yang sangat direkomendasikan saat Anda mengembangkan atau *debugging test*. Anda bisa melihat *trace*, *screenshot*, menjalankan *test* satu per satu, dan bahkan melakukan *step-by-step debugging*. |
| `npm run test:debug`            | Memulai *debugger* Playwright, memungkinkan Anda untuk mengatur *breakpoint* dan melangkah melalui kode *test* Anda. Berguna untuk menganalisis perilaku *test* secara mendalam. |
| `npm run codegen`               | Perintah yang sangat ampuh! Ini membuka *browser* dan merekam interaksi Anda, lalu secara otomatis menghasilkan kode *test* Playwright. Sangat berguna untuk membuat *boilerplate* awal untuk *test* baru atau untuk mengidentifikasi *locator*. |
| `npm run report`                | Membuka laporan HTML interaktif dari hasil eksekusi *test* terakhir. Ini adalah *tool* penting untuk menganalisis kegagalan dan mendapatkan *insight* tentang performa *test*. |

### Memfilter Test Tertentu

Anda tidak selalu ingin menjalankan seluruh *test suite*. Playwright memungkinkan Anda untuk memfilter *test* berdasarkan *path* file, *nama test*, atau *tag*.

*   **Menjalankan semua *test* dalam folder tertentu:**
    ```bash
    npx playwright test tests/login
    ```
    Perintah ini akan menjalankan semua file `.spec.ts` yang ada di dalam folder `tests/login/`.

*   **Menjalankan *test* dengan nama tertentu (menggunakan *substring* atau *regex*):**
    ```bash
    npx playwright test -g "incorrect_email"
    ```
    Ini akan menjalankan semua *test case* yang namanya mengandung string "incorrect_email". Anda bisa menggunakan `-g` (atau `--grep`) untuk mencocokkan sebagian nama *test* atau deskripsi *suite*.

*   **Menjalankan *test* API saja (tanpa membuka *browser*):**
    ```bash
    npx playwright test tests/login/login-api.spec.ts
    ```
    Jika Anda memiliki *test* yang hanya berinteraksi dengan API (`request.post()`, `request.get()`, dll.), Anda bisa menjalankannya secara terpisah. Ini jauh lebih cepat karena tidak perlu meluncurkan *browser* UI.

*   **Menjalankan *smoke test* cepat sebelum *deploy*:**
    ```bash
    npx playwright test tests/smoke.spec.ts tests/login/login-valid.spec.ts tests/login/login-api.spec.ts
    ```
    Anda bisa menentukan beberapa file *spec* untuk dijalankan bersamaan. Ini ideal untuk *smoke test* yang cepat dan penting.

### Parallelization (Eksekusi Paralel)

Salah satu keunggulan Playwright adalah kemampuannya untuk menjalankan *test* secara paralel secara *default*. Ini berarti jika Anda memiliki banyak *test case*, Playwright akan membaginya ke beberapa *worker* (proses) dan menjalankannya secara bersamaan, mempercepat total waktu eksekusi. Anda dapat mengkonfigurasi jumlah *worker* di `playwright.config.ts`.

### Laporan HTML dan Fitur Debugging

Setelah *test* selesai dijalankan (terutama jika ada kegagalan), Anda dapat membuka laporan HTML interaktif dengan `npm run report`. Laporan ini adalah *tool* yang sangat berharga:

*   **Ringkasan Hasil**: Menunjukkan berapa banyak *test* yang lulus, gagal, atau di-*skip*.
*   **Detail Setiap Test**: Untuk setiap *test*, Anda bisa melihat langkah-langkah yang dieksekusi, *assertion* yang dilakukan, dan *error message* jika gagal.
*   **Trace Viewer**: Ini adalah fitur unggulan Playwright. Untuk setiap *test* yang terekam *trace*, Anda bisa melihat *timeline* eksekusi, *screenshot* di setiap langkah, status jaringan, dan bahkan video singkat dari interaksi *browser*. Ini seperti memiliki kamera pengawas yang merekam setiap detail saat *test* dijalankan.
*   **Screenshots dan Video**: Playwright dapat dikonfigurasi untuk mengambil *screenshot* saat *test* gagal atau merekam video penuh dari setiap eksekusi *test*. Ini sangat membantu dalam mereproduksi *bug* atau memahami konteks kegagalan.

Dengan fitur-fitur ini, menganalisis kegagalan *test* menjadi jauh lebih mudah dan cepat, memungkinkan Anda mengidentifikasi akar masalah dengan efisien.

---

## Rangkuman

Selamat! Anda telah menyelesaikan bab penting tentang *automation testing* dengan Playwright. Kita telah belajar bahwa *automation testing* bukan lagi pilihan, melainkan keharusan untuk memastikan kualitas perangkat lunak di tengah siklus pengembangan yang cepat. Playwright menonjol sebagai *tool* modern yang kuat, mengatasi banyak keterbatasan *framework* lama dengan fitur-fitur seperti *auto-waiting*, dukungan *cross-browser* yang luas, *API testing* *first-class*, dan kemampuan *debugging* yang luar biasa.

Anda kini memahami pentingnya struktur proyek yang rapi, yang memastikan kode *automation* Anda mudah dikelola dan diskalakan. Kita juga telah mendalami *Page Object Model* (POM) sebagai pola desain fundamental untuk membuat *test case* yang mudah dibaca dan dipelihara, serta bagaimana menerapkan *data-driven testing* untuk menguji berbagai skenario dengan data yang bervariasi secara efisien. Terakhir, Anda telah mempelajari berbagai cara untuk menjalankan *test* dan memanfaatkan laporan HTML serta fitur *trace viewer* Playwright untuk *debugging* yang efektif.

Menguasai *automation testing* dengan Playwright akan secara signifikan meningkatkan efisiensi dan cakupan *testing* Anda, membebaskan Anda untuk fokus pada aspek kualitas yang lebih kompleks. Ini adalah langkah maju yang besar dalam perjalanan Anda menjadi Quality Assurance Engineer yang kompeten dan berharga.

---

## Checklist Actionable

Berikut adalah langkah-langkah yang dapat Anda lakukan untuk mulai menerapkan *automation testing* dengan Playwright:

*   [ ] **Inisialisasi Proyek Playwright**: Buat proyek baru atau navigasi ke folder `automation-playwright/` jika Anda menggunakan *template* yang ada. Jalankan `npm install` dan `npx playwright install --with-deps chromium`.
*   [ ] **Konfigurasi Lingkungan**: Salin `.env.example` menjadi `.env` dan isi variabel lingkungan yang dibutuhkan (misalnya, `TEST_EMAIL`, `TEST_PASSWORD`).
*   [ ] **Buat Page Object Sederhana**: Pilih salah satu halaman di aplikasi Anda (misalnya, halaman login atau halaman beranda). Buat file `.page.ts` baru di folder `pages/` dan definisikan *locator* serta metode dasar untuk berinteraksi dengan halaman tersebut.
*   [ ] **Tulis Test Case Pertama Anda**: Buat file `.spec.ts` baru di folder `tests/` yang menggunakan *Page Object* yang baru Anda buat. Tulis *test case* sederhana untuk menguji fungsionalitas dasar halaman tersebut.
*   [ ] **Jalankan Test Anda**: Gunakan `npm run test:headed` untuk melihat *test* Anda berjalan di *browser*.
*   [ ] **Eksplorasi Playwright UI**: Gunakan `npm run test:ui` untuk membuka mode UI interaktif. Coba jalankan *test* satu per satu, gunakan fitur *step-by-step debugging*, dan lihat *trace viewer* untuk *test* yang gagal.
*   [ ] **Buat Laporan HTML**: Setelah menjalankan *test*, buka laporan HTML dengan `npm run report` dan analisis hasilnya, terutama untuk *test* yang gagal.
*   [ ] **Pertimbangkan Data-Driven Testing**: Identifikasi *test case* yang perlu diulang dengan data berbeda. Pindahkan data tersebut ke file di folder `data/` dan modifikasi *test spec* Anda untuk mengiterasi data tersebut.
*   [ ] **Integrasikan API Testing**: Jika ada kebutuhan untuk menyiapkan *test data* atau menguji *endpoint* API, mulai buat *wrapper* di folder `api/` dan gunakan di *test* Anda.
*   [ ] **Terus Berlatih**: Semakin banyak Anda menulis dan menjalankan *test* otomatis, semakin mahir Anda akan menjadi. Jangan ragu untuk bereksperimen dengan berbagai fitur Playwright!
