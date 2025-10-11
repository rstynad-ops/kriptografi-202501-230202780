# Laporan Praktikum Kriptografi
Minggu ke-: 1  Topik: Into CIA  Nama: Resty Chonifatul Jannah NIM: 230202780  Kelas: 5 IKRB  
---

## 1. Tujuan
1.	Menjelaskan sejarah dan evolusi kriptografi dari masa klasik hingga modern.
2.	Menyebutkan prinsip Confidentiality, Integrity, Availability (CIA) dengan benar.
3.	Menyimpulkan peran kriptografi dalam sistem keamanan informasi modern.
4.	Menyiapkan repositori GitHub sebagai media kerja praktikum.
   
---

## 2. Dasar Teori
Sejarah Kriptografi & Prinsip CIA
Kriptografi erasala dari dua kata Yunani,yaitu kryptos (tersembunyi) dan graphein (menulis), yang jika digabungkan akan berarti"menulis secara tersembunyi".kriptografi  berfunngsi untuk melindungi informasi agar informasi tersebut hanya dapat dibaca  oleh pihak yang memiliki wewenang.
    pada era kriptografi klasik, metode yang digunakan masih sederhana dan berbasis pada penggantian serta pergeseran huruf. Minsalnya Caesar Cipher,yang mengganti huruf dengan posisi tertentu di alfabet, Vigenere Cipher menggunakan kunci berupa kata untuk mengenkripsi pesan.Tujuan utama dari metode ini adalah untuk menjaga kerahasiaan pesan dalam komunikasi militer dan diplomatik. Lalu memasuki era kriptografi modern,pendekatan matematika dan komputer mulai digunakan dimana kriptografi tidak hanya untuk merahasiakan pesan,tetapi juga untuk memastikan keaslian dan integritas data. Algoritma seperti AES(Advanced Encryption Standard) digunakan untuk enkripsi simetris yang cepat dan aman, sedangkan RSA(Rivest-Shamir-Adleman) menjadi algoritma asimetris yang memungkinkan penggunaan kunci publik dan privat. 
    Memasuki era kriptografi kontemporer, kriptografi berkembang pesat dengan munculnya tekologi digital dan internet.Salah satu contoh penerapannya adalah blockchain, yang menggunakan konsep hash dan tanda tangan digital untuk menjaga integritas transaksi tanpa perantara. Teknologi ini menjadi dasar bagi cryptocurrency seperti Bitcoin, yang mengandalkan kriptografi untuk menjamin keamanan dan keaslian transaksi digital.
    kriptografi telah berevolusi dari sekadar penyandian sederhana menjadi ilmu penting dalam keamanan informasi. Perkembangannya menunjukkan bahwa kebutuhan manusia terhadap keamanan, privasi, dan kepercayaan pada sistem digital semakin meningkat seiring kemajuan teknologi.
    
prinnsip CIA

CIA merupakan kependekan dari Confidentiality,Integrity, dan Availability.Dimana tiga unsur ini dikenal sebagai CIA Triad,yaitu tiga pilar utama keamanan informasi yang menjadi dasar untuk melindungi data dan sistem agar tetap aman,utuh,serta dapat diakses oleh pihak yang berhak.
Confidentiality(Kerahasiaan),menjaga agar informasi hanya dapat diakses oleh pihak yang berwenang.Tujuaannya untuk mencegah kebocoran atau akses tidak sah terhadap data penting.
Contoh:Enkripsi pada pesan whatsapp agar hanya pengirim dan penerima yang bisa membaca isinya.
Integrity(Integritas), menjaga agar data tetap utuh,asli,dan tidak boleh tanpa izin hal ini bertujuan untuk memastikan bahwa informasi yang diterima sama persis dengan apa yang dikirim, tanpa ada manipulasi.
Contoh:Penggunaan data tangan digital pada dokumen untuk memastikan dokumen tersebut belum dimodifikasi.
Availability(Ketersediaan),menjamin bahwa sistem,layanan,dan data selalu tersedia bagi pengguna yang berhak kapan pun dibutuhkan.
Contoh:Penggunaan beckup server dan sistem keamanan jaringan agar layanan tetep aktif meski terjadi gangguan teknis.

---

## 3. Alat dan Bahan
- Git dan akun GitHub  
---

## 4. Langkah Percobaan
- Melakukan fork repository kriptografi
- Melakukan clone repository ke komputer lokal.
- Membuat folder praktikum/week1-intro-cia/ berisi laporan.md dan folder screenshot.
- Menulis ringkasan materi singkat.
- Menjawab quiz.
---

## 7. Quiz singkat
- Pertanyaan 1: Cloude Shannon 
- Pertanyaan 2: - RSA(Rivest-Shamir-Adleman):Paling banyak digunakan untuk enkripsi dan tanda tangan digital
                - ECC (Elliptic Curve Cryptography) dan Diffie-Hellman yang banyak digunakan untuk enkripsi data dan pertukaran kunci secara aman.
- pertanyaan 3: Kriptografi klasik menggunakan metode sederhana berbasis penggantian huruf atau pergeseran karakter(Caesar Cipher,Vigenere Cipher)
                Kriptografi modern menggunakan algoritma matematis kompleks dan komputer, melibatkan kunci publik dan privat,serta mampu mengamankan data digital dalam skala besar(AES,RSA).
  
---

## 8. Kesimpulan
   Kriptografi merupakan ilmu yang berawal dari teknik penyandian sederhana pada masa klasik hingga berkembang menjadi sistem keamanan digital yang kompleks di era modern dan kontemporer. Perkembangannya mencerminkan kebutuhan manusia untuk menjaga keamanan, keaslian, dan kerahasiaan informasi dalam dunia digital. Prinsip dasar keamanan informasi dijelaskan melalui konsep CIA Triad (Confidentiality, Integrity, dan Availability), yang menekankan pentingnya menjaga kerahasiaan data, memastikan keaslian serta keutuhannya, dan menjamin ketersediaan informasi bagi pihak yang berhak. Dengan demikian, kriptografi dan prinsip CIA menjadi fondasi utama dalam menjaga keamanan informasi di era teknologi saat ini.

