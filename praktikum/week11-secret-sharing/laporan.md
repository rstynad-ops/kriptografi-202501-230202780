# Laporan Praktikum Kriptografi
Minggu ke-: 11 Topik: Secret Sharing  Nama:Resty Chonifatul jannah  NIM: 230202780  Kelas: 5 Ikrb  

---
## 1. Tujuan
1. Menjelaskan konsep Shamir Secret Sharing (SSS).
2. Melakukan simulasi pembagian rahasia ke beberapa pihak menggunakan skema SSS.
3. Menganalisis keamanan skema distribusi rahasia.

---
## 2. Dasar Teori
Shamir secret sharing (SSS) merupakan sebuah skema kriptografi yang diperkenalkan oleh Adi Shamir pada tahun 1979 untuk membagi sebuah rahasia (secret) menjadi beberapa bagian (sheres), sehingga rahasia hanya dapat direkontruksi jika minimal k atau bagian digabungkan, kurang dari k bagian tidak memberikan informasi apapun tentang rahasia.

Shamir secret shering bekerja berdasarkan prinsip interpolasi polinominal pada bidang hingga, yakni sebuah polinomial berderajat K - 1 dapat ditenteukan secara unik minimal K titik. Pada proses pembangkitan share, sebuah rahasia S ditempatkan sebagai konstanta dalam polinomial acak 

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
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: …  
- Pertanyaan 2: …  
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---
## 10. Commit Log
```

Author: Resty Chonifatul Jannah <rstynad@gmail.com>
Date:   2026-01-14

    week11-secret-sharing: implementasi Caesar Cipher dan laporan )
```
