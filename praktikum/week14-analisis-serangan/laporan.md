# Laporan Praktikum Kriptografi
Minggu ke-: 14 Topik: Analisis Serangan Kriptografi Nama:Resty Chonifatul Jannah  NIM: 230202780 Kelas: 5 Ikrb 

---
## 1. Tujuan
1. Mengidentifikasi jenis serangan pada sistem informasi nyata.
2. Mengevaluasi kelemahan algoritma kriptografi yang digunakan.
3. Memberikan rekomendasi algoritma kriptografi yang sesuai untuk perbaikan keamanan.

---
## 2. Dasar Teori
Analisis serangan kripptografi merupakan proses mempelajari bagaimana suatu sistem keamanan dapat diserang atau ditebus, dengan tujuan mengetahui kelemahanya dan meningkatkan tingkat keamanannya. Dalam kriptografi, keamanan data harus menjaga kerahasian informasi, keutuhan data, dan keaslian pengirim agar tidak mudah dimanipulasi oleh pihak yang tidak berwenang.

Ada beberapa jenis serangan yang sering terjadi adalah brute force attack, yaitu mencoba semua kemungkinan password atau kunci sampai berhasil, serta dictionary attack, yaitu menebak password menggunakan daftar kata yang sering dipakai pengguna. Serangan ini biasanya berhasil jika pengguna memakai password yang lemah atau sistem tidak membatasi jumlah percobaan login. Selain itu, ada juga serangan Man-in-the-Middle, yaitu penyerang menyadap komunikasi antara dua pihak dan bisa mencuri atau mengubah data jika koneksi tidak dienkripsi dengan baik.

Dalam analisis kriptografi, penting untuk membedakan kelemahan algoritma dan kelemahan implementasi. Algoritma bisa saja aman secara teori, tetapi menjadi tidak aman karena kesalahan dalam penerapan, seperti penggunaan kunci yang terlalu pendek, penyimpanan password yang tidak terenkripsi, atau kesalahan konfigurasi sistem. Oleh karena itu, analisis serangan kriptografi membantu memahami potensi risiko dan cara memperkuat keamanan sistem.

---
## 3. Alat dan Bahan
- Python 3.11 
- Visual Studio Code / editor lain  
- Git dan akun GitHub
- Google Chrome
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---
## 4. Langkah Percobaan
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
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1:Mengapa banyak sistem lama masih rentan terhadap brute force atau dictionary attack?
- Pertanyaan 2:Apa bedanya kelemahan algoritma dengan kelemahan implementasi?
- Pertanyaan 3:Bagaimana organisasi dapat memastikan sistem kriptografi mereka tetap aman di masa depan?
Jawab:
1. Banyak sistem lama masih rentan karena menggunakan algoritma kriptografi yang sudah usang, panjang kunci yang pendek, serta metode penyimpanan password yang tidak aman seperti tanpa hashing atau salting. Selain itu, keterbatasan teknologi pada saat sistem tersebut dibuat membuatnya tidak dirancang untuk menghadapi kemampuan komputasi modern yang jauh lebih cepat.
2. Kelemahan algoritma terjadi ketika metode kriptografi itu sendiri memiliki celah matematis atau desain yang dapat dieksploitasi. Sementara itu, kelemahan implementasi terjadi akibat kesalahan dalam penerapan algoritma, seperti penggunaan kunci yang lemah, pengelolaan kunci yang buruk, atau kesalahan pemrograman, meskipun algoritmanya sebenarnya aman.
3. Organisasi dapat menjaga keamanan sistem kriptografi dengan selalu memperbarui algoritma dan standar keamanan, menerapkan panjang kunci yang kuat, melakukan audit keamanan secara berkala, serta mengikuti perkembangan ancaman siber. Selain itu, pelatihan sumber daya manusia dan penerapan kebijakan keamanan yang baik juga penting untuk mengurangi risiko kesalahan manusia.
   
---
## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 10. Commit Log:
```
commit week14
Author: Resty Chonifatu Jannah <rstynad@gmail.com>
Date:   2026-01-26

    week14-cryptosystem: Analisis Serangan Kriptografi )
```
