# Laporan Praktikum Kriptografi
Minggu ke-: 12 Topik: Aplikasi TLS & E_commers  Nama: Resty chonifatul Jannah  NIM: 230202780 Kelas: 5ikrb  

---
## 1. Tujuan
1. Menganalisis penggunaan kriptografi pada email dan SSL/TLS.
2. Menjelaskan enkripsi dalam transaksi e-commerce.
3. Mengevaluasi isu etika & privasi dalam penggunaan kriptografi di kehidupan sehari-hari.

---
## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

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
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
