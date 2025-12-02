# Laporan Praktikum Kriptografi
Minggu ke-: 6  Topik: Cipher Modern Nama: Resty Chonifatul Jannah NIM: 230202780  Kelas: 5 Ikrb  

---
## 1. Tujuan
1. Mengimplementasikan algoritma DES untuk blok data sederhana.
2. Menerapkan algoritma AES dengan panjang kunci 128 bit.
3. Menjelaskan proses pembangkitan kunci publik dan privat pada algoritma RSA.
---
## 2. Dasar Teori
Cipher Modern merupakan teknik penyandian data dalam kriptogaarafi yang digunakan pada era komputer dan jaringan digital. berbeda dengan cipher klasik yang hanya mengandalkan subtitusi dan transposisi sederhana,cipher modern menggunakan algoritma matematis kompleks, operasi bit, transformasi blok, serta kunci yang panjang dan acak. tujuan utamanya adalah untuk memastikan kerahasiaan, integritas, serta keamanan data dalam proses komunikasi digital.

Karakteristik Cipher Modern
1. Menggunakan kunci yang panjang dan acak sehingga sulit ditebak.
2. Bekerja dengan data digital, yaitu bit atau blok data.
3. Tahan terhadap serangan kriptanalisis modern, seperti brute-force, differential cryptanalysis, dan linear cryptanalysis.
4. Cepat dan efisien, karena dioptimalkan untuk perangkat keras maupun perangkat lunak.
5. Memiliki fungsi enkripsi dan dekripsi yang terstruktur, dengan operasi seperti XOR, rotasi bit, substitusi, dan permutasi.

1.DES (Data Encryption Standard)
DES adalah algoritma kriptografi modern awal yang menggunakan kunci simetrik, artinya kunci yang sama dipakai untuk proses enkripsi dan dekripsi. DES bekerja dengan membagi data menjadi blok 64 bit dan melakukan proses substitusi serta permutasi dalam 16 putaran menggunakan kunci sepanjang 56 bit. Walaupun DES dulu sangat populer dan digunakan secara luas, kini dianggap tidak lagi aman karena kuncinya terlalu pendek sehingga dapat diretas menggunakan brute force. Karena itu, DES sudah digantikan oleh algoritma yang lebih kuat seperti AES.
2.AES (Advanced Encryption Standard)
AES adalah algoritma enkripsi simetrik yang menjadi standar modern dan sangat aman digunakan saat ini. AES bekerja pada blok data 128 bit dengan panjang kunci 128, 192, atau 256 bit, membuatnya lebih tahan terhadap serangan brute force. Algoritma ini menggunakan beberapa langkah seperti SubBytes, ShiftRows, MixColumns, dan AddRoundKey, yang dilakukan secara berulang dalam 10–14 putaran tergantung panjang kunci. AES banyak dipakai pada sistem keamanan modern seperti WiFi, VPN, aplikasi pesan instan, dan penyimpanan data karena cepat, efisien, dan sangat kuat.
3. RSA (Rivest-Shamir-Adleman)
RSA merupakan algoritma kriptografi asimetrik yang menggunakan dua kunci berbeda: kunci publik untuk enkripsi dan kunci privat untuk dekripsi. Keamanan RSA bergantung pada kesulitan memfaktorkan bilangan besar yang merupakan hasil perkalian dua angka prima yang sangat besar. RSA tidak cocok untuk mengenkripsi data dalam jumlah besar karena prosesnya lebih lambat, tetapi sangat ideal untuk pertukaran kunci, tanda tangan digital, dan autentikasi. RSA menjadi dasar keamanan komunikasi internet seperti HTTPS dan protokol email aman.

---
## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Google Chrome
- pip install pycryptodome

---
## 4. Langkah Percobaan
1. Membuat file `aes.py` ,`des.py`, `rsa.py` di folder `praktikum/week6-cipher-modern/src/`.
2. Menyalin kode program dari panduan praktikum.
3. membuat folder screenshots dan mengupload file `hasil.png`
4. mengerjakan soal
---

## 5. Source Code
1. Langka 1-DES
2. Langkah 2-AES
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
- Pertanyaan 1: …  
- Pertanyaan 2: …  
)
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
commit week6-cipher-,modern
Author: Resty Chonifatul Jannah <rstynad@gmail.com>
Date:   2025-12-02

    week6-cipher-modern: Cipher Modern (DES, AES, RSA)
```
