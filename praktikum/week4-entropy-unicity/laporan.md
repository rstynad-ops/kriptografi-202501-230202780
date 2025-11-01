# Laporan Praktikum Kriptografi
Minggu ke-: 4  Topik: entropi & unicity distance  Nama:Resty Chonifatul Jannah  NIM: 230202780 Kelas:5 IKRB

---
## 1. Tujuan
1.Menyelesaikan perhitungan sederhana terkait entropi kunci.

2.Menggunakan teorema Euler pada contoh perhitungan modular & invers.

3.Menghitung unicity distance untuk ciphertext tertentu.

4.Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.

5.Mengevaluasi potensi serangan brute force pada kriptosistem sederhana.

---
## 2. Dasar Teori
- Entropi merupakan ukuran ketidakpasian atau jumlah informasi yang terkandung dalam suatu sistem.Konsep ini pertama kali diperkenalkan oleh Claude E.Shannon pada tahun 1948 dalam teori informasi.Dalam kriptografi, entropi menggambarkan tingkat ketidakpastian pesan atau kunci yang digunakan dalam suatu sistem kriptografi.Secara sistematis, entropi H(X) dari suatu variabel acak X dengan kemungkinan (P(Xi) yang di definisikan sebagai :
 
 <img width="419" height="46" alt="Screenshot 2025-11-01 103849" src="https://github.com/user-attachments/assets/4698c51e-0ebf-44a5-80c7-1e17c1e9f8ac" />

H(X)= entropi dari variabel acak X, menyatakan jumlah rata-rata informasi(dalam satuan bit) yang dikandung oleh X, 
X= variabel acak yang merepresentasikan sumber pesan atau kunci dalam sistem kriptografi,
p(Xi)= probabilitas kemunculan suatu simbolatau nilai Xi dari variabel X,
log2​= logaritma basis 2, karena satuan informasi yang digunakan adalah bit,
−∑= tanda negatif digunakan kerena probabilitas p(Xi) bernilai antara 0 dan 1, sehingga log2 (p(Xi)) selalu bernilai negatif.

- Unicity Distance (jarak Keunikan) merupakan konsep yang diperkenalkan oleh Claude E.Shannon, yang menggambarkan jumlah minimum ciphertext yang dibutuhkan agar kunci enkripsi dapat ditentukan secara unik.Secara matematis, Unicity Distance U dapat didefinisikan sebagai :

<img width="214" height="79" alt="image" src="https://github.com/user-attachments/assets/a5ea5de6-8784-472e-8ae0-4c72ebac1668" />

dengan:
H(K) = entropi kunci(jumlah bit informasi yang terkandung dalam kunci),
D= redundansi pesan per karakter (berapa banyak informasi berlebih dalam plaintext).

---
## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
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
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
