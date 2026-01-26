# Laporan Praktikum Kriptografi
Minggu ke-: 12 Topik: Aplikasi TLS & E_commers  Nama: Resty chonifatul Jannah  NIM: 230202780 Kelas: 5ikrb  

---
## 1. Tujuan
1. Menganalisis penggunaan kriptografi pada email dan SSL/TLS.
2. Menjelaskan enkripsi dalam transaksi e-commerce.
3. Mengevaluasi isu etika & privasi dalam penggunaan kriptografi di kehidupan sehari-hari.

---
## 2. Dasar Teori
Kriptografi pada layanan email dan protokol SSL/TLS berfungsi untuk menjaga kerahasian, integritas, dan keaslian data dalam pertukaran informasi. Teknologi seperti PGP dan S/MIME menggunakan enkripsi kunci publik agar hanya penerima yang berhak untuk dapat membaca pesan, dan tanda tangan digital untuk menverifikasi identitas pengirim. Sementara itu , SSL/TSL mengamankankomunikasi antara klien dan server dengan mengenkripsi data sehingga mencegah penyadapan serta serangan man-in-the-middle.

Dalam transaksi e-commerce, penggunaan HTTPS berbasis SSl/TLS melindungi data sensitif seperti informasi pembayaran dan identitas pengguna dari akses tidak sah. Selain meningkatkan keamanan, kriptografi juga mendukung proses autentikasi dan non-repudiation sehingga menumbuhkan kepercayaan antara pihak yang bertransaksi. Dari sisi etika dan privasi, krptografi melindugi data pribadi, namun dapat menimbulkan keraguan ketika digunakan untuk menyembunyikan aktivitas ilegal atau sat terjadi upaya pengaasan oleh pihak tertentu, sehingga diperlukan kebijakan yang seimbang dan bertanggung jawab.

---
## 3. Alat dan Bahan
- Python 3.11 
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Google Chrome
  
---
## 4. Langkah Percobaan
1. Langkah 1 — Analisis SSL/TLS pada Email & Web
   - Issuer CA (Certificate Authority),Sertifikat digital website shoppe diterbitkan oleh GlobalSign GCC AlphaSSL CA 2023 dengan organisasi GlobalSign nv-sa. GlobalSign merupakan lembaga otiritas sertifikat internasional yang terpercaya.
   -Sertifikat Shoppe ini mulai berlaku pada 24 maret 2025 dan akan berarhit pada 25 april 2026 .
   - Sertifikat menggunakan fingerprint SHA-256 untuk menjaga keaslian data. Dalam komunikasi HTTPS,menggunakan algoritma RSA untuk pertukaran kunci dan AES untuk mengenkripsi data, sehingga informasi pengguna terlindungi dari penyadapan.
   - Website menggunakan protokol HTTPS yang ditandai dengan ikon gembok pada browser, menandakan bahwa seluruh data yang dikirim dan diterima telah terenkripsi. hal ini membiat komunikasi lebih   aman, menjaga kerahasian data, serta meniningkatkan kepercayaan pengguna. Sebaliknya, website yang tidak menggunakan HTTPS (HTTP) tidak memiliki sertifikat digital dan tidak menerapkan enkripsi, sehingga data mudah disadap, dimanipulasi, serta beresiko terhadap serangan keaman seperti pencurian data atau penyisipan malawe

2. Langkah 2 — Studi Kasus E-commerce
   Pada website e-commerce seperti shoppe, enkripsi digunkan untuk melindungi data pengguna saat proses login, transaksi, dan pembayaran dengan cara mengenkripsi informasi menggunakan protokol TSL sebelum dikirim ke server. Hal ini memastikan bahwa data seperti username,password, dan informasi pembayaran tidak dapat dibaca oleh pihak yang tidak berwenang. sertifikat digital juga berperan dalam memverifikasi keaslian website sehingga pengguna terhindar dari situs palsu. Jika TLS tidak digunakan, data akan dikirim dalam bentuk teks biasa dan rentan terhadap serangan seperti Man-in-the-Middle, di mana penyerang dapat menyadap, mengubah, atau mencuri informasi pengguna. Oleh karena itu, penggunaan TLS sangat penting untuk menjaga keamanan dan kepercayaan dalam transaksi online.
3. Langkah 3- Analisis Etika & Privasi
   Pengguna email terenkripsi seperti PGP dan S/MIME bertujuan untuk menjaga kerahasian komunikasi agar hanya pihak yang berwenang dapat mengakses isi pesan. Namun, penggunaan enkripsi juga menimbulkan isu privasi, terutama terkait pengelolaan kunci dan potensi penyalahgunaan teknologi tersebut. Secara etika, terdapat dilema mengenai kewenangan perusahan dalam mendeskripsi email karyawan untuk keperluan audit, karena hal ini harus mempertimbangkan keeimbangan antara keamanan organisasi dan privasi individu.

---
## 5. Source Code
---

## 6. Hasil dan Pembahasan
Hasil CA pada website Shopee:
<img width="1920" height="1080" alt="Screenshot 2026-01-26 131436" src="https://github.com/user-attachments/assets/3bbce7e5-54ca-4df3-9b65-bb008a75bd68" />

Berdasarkan hasil pemeriksaan sertifikat digital pada website  shopee.co.id, diketahui bahwa sertifikat tersebut diterbitkan oleh GlobalSign GCC R6 AlphaSSL CA 2023 dengan organisasi GlobalSign nv-sa. GlobalSign merupakan salah satu Certificate Authority (CA) internasional yang terpercaya dan berfungsi untuk menverifikasi keaslian identitas suatu website sebelum sertifikat diterbitkan. Dengan adanya sertifikat tersebut, browser dapat memastikan bahwa pengguna benar- benar terhubung ke server resmi Shopee dan bukan situs palsu ataupun tiruan. Sertifikat tersebut juga mendukung proses enkripsi data menggunakan protokol HTTPS, Sehingga informasi pengguna seperti akun, transaksi, dan juga data pribadi terlindungi selama proses komunikasi pada internet.

---
## 7. Jawaban Pertanyaan  
- Pertanyaan 1:apakah perbedana utama antara HTTP dan HTTPS?  
- Pertanyaan 2: Mengapa sertifikat digital menjadi penting dalam komunikasi TLS? 
- Pertanyaan 3:Bagaimana Kriptografi mendukung privasi dalam komunikasi digital, tetapi sekaligus menimbulka tentang hukuman dan etika?

Jawab:
1. HTTP (HyperText Transfer Protocol) mengirimkan data dalam bentuk teks biasa sehingga mudah disadap atau dimodifikasi oleh pihak lain. Sementara itu, HTTPS (HyperText Transfer Protocol Secure) menggunakan protokol keamanan TLS/SSL untuk mengenkripsi data yang dikirim, sehingga informasi seperti password, data pribadi, dan transaksi menjadi lebih aman. HTTPS juga menjamin keaslian server dan integritas data selama proses komunikasi.
2. Sertifikat digital berfungsi untuk memverifikasi identitas suatu server atau pihak yang berkomunikasi agar pengguna yakin bahwa mereka terhubung ke pihak yang benar, bukan ke penyerang. Sertifikat ini dikeluarkan oleh lembaga terpercaya yang disebut Certificate Authority (CA). Selain itu, sertifikat digital juga digunakan untuk mendistribusikan kunci publik secara aman sehingga proses enkripsi dan pertukaran data dalam TLS dapat berlangsung dengan aman dan terpercaya.
3. Kriptografi melindungi privasi dengan mengenkripsi data sehingga hanya pihak yang berwenang yang dapat membaca informasi tersebut, misalnya pada komunikasi pesan, transaksi online, dan penyimpanan data. Namun, penggunaan kriptografi juga menimbulkan tantangan hukum dan etika karena dapat dimanfaatkan untuk menyembunyikan aktivitas ilegal, menyulitkan penegakan hukum dalam proses penyelidikan. Oleh karena itu, diperlukan keseimbangan antara perlindungan privasi individu dan kepentingan keamanan publik.
   
---
## 8. Kesimpulan
Berdasarkan  kajian teori dan percobaan, dapat disimpulkan bahwa kriptografi memiliki peran penting dalam menjaga keamanan komunikasi digital, khususnya pada layanan email dan transaksi e-commerce. Penggunaan SSL/TLS melalui HTTPS terbukti mampu melindungi data dari penyadapan, manipulasi, dan serangan man-in-the-middle, serta memastikan keaslian identitas server melalui sertifikat digital. Sementara itu, teknologi enkripsi pada email seperti PGP dan S/MIME menjamin kerahasiaan dan keutuhan pesan. Meskipun memberikan perlindungan privasi yang kuat, penerapan kriptografi juga menimbulkan tantangan etika dan hukum, sehingga diperlukan kebijakan yang seimbang antara keamanan, privasi, dan kepentingan publik.

---
## 10. Commit Log
```
commit week12-aplikasi TLS
Author: Resty Chonifatul Jannah
Date:   2026/01/26

    week12-aplikasi tsl: Aplikasi tsl & E-commerce
```
