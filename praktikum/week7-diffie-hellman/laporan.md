# Laporan Praktikum Kriptografi
Minggu ke-: 7 Topik: Deffie-Hellman LKey Exchange Nama: Resty Chonifatul Jannah  NIM: 230202780 Kelas: 5 Ikrb  

---
## 1. Tujuan
1. Melakukan simulasi protokol Diffie-Hellman untuk pertukaran kunci publik.
2. Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.
3. Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan Man-in-the-Middle / MITM).
---
## 2. Dasar Teori  
Diffie-Hellman Key Exchange merupakan protokol kriptografi yang memungkinkan dua pihak membangun kunci rahasia bersama melalui jaringan yang tidak aman tanpa harus mengirimkan kunci tersebut secara langsung. Mekanisme ini dimulai dengan kesepakatan dua nilai publik berupa bilangan prima dan generator, kemudian masing-masing pihak memilih kunci rahasia pribadi, menghitung kunci publik menggunakan operasi eksponensial modulo, dan saling menukarkannya. Setelah menerima kunci publik satu sama lain, kedua pihak menghitung kunci rahasia akhir yang bernilai sama , sehingga dapat digunakan untuk enkripsi simetris. Keamanan metode ini bergantung pada sulitnya memecahkan masalah logaritma diskrit, sehingga meskipun nilai publik diketahui, phak ketiga tetap sulit menebak kunci rahasia yang terbantuk.

---
## 3. Alat dan Bahan
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Google Chrome
  
---
## 4. Langkah Percobaan
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week7-diffie-hellman/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)
4. Menjawab Pertanyaan diskusi
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
- Pertanyaan 1: Mengapa Diffie-Hellman memungkinkan pertukaran kunci di saluran publik?
- Pertanyaan 2: Apa kelemahan utama protokol Diffie-Hellman murni?
- Pertanyaan 3:Bagaimana cara mencegah serangan MITM pada protokol ini?
Jawab:
1. Karena Diffie-Hellman tidak pernah mengirimkan kunci rahasia secara langsung. yang dikirim hanya angka-angka biasa yang boleh dilihat siapa pun. dari angka-angka itu, masing-masing pihak bisa menghitung sendiri kunci rahasia yang sama. orang lain yang mengintip tidak bisa menebak kuncinya karena perhitungannya sangat sulit dibalik.
2. Kelemahan utama Diffie-Hellman murni adalah tidak adanya autentikasi, sehingga pihak yang terlibat tidak bisa memastikan apakah kunci publik yang diterima bener milik lawan komunikasi. Akibatnya, protokal ini rentan terhadap Man-in-the-Middle attack(MITM), dimana penyerang dapat menyesipkan diri ditengah dan dapat membuat dua kunci berbeda dangan masing-masing pihak tanpa diketahui.
3. Serangan MITM dapat dicegah dengan menambahkan mekanisme autentikasi pada pertukaran kunci. Cara umum yang digunakan yaitu: Menggunakan tanda tangan digital(digital signature) untuk menandatangani nilai publik sehingga identitas pihak dapat diverifikasi, menggunakan sertifikat digital (CA) serpeti pada TLS/HTTPS agar kunci publik terjamin keasliannya, menggabungkan Diffie-Hellman dengan protokol autentikasi seperti password, token, listrik, atau kunci publik.

---
## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---
## 10. Commit Log
```
commit week7-diffie-hellman
Author: Resty Chonifatul Jannah <rstynad@gmail.com>
Date: 2025-12-08

    week7-diffie-hellman: Diffie-Hellman Key Exchange
```
