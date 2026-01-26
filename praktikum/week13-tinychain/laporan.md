# Laporan Praktikum Kriptografi
Minggu ke-: 13 Topik: Tinychain-Proof of work (PoW)  Nama: Resty Chonifatul Jannah NIM: 230202780 Kelas: 5 ikrb 

---
## 1. Tujuan
1. Menjelaskan peran hash function dalam blockchain.
2. Melakukan simulasi sederhana Proof of Work (PoW).
3. Menganalisis keamanan cryptocurrency berbasis kriptografi.
   
---
## 2. Dasar Teori
Hasd funcation adalah fungsi kriptogarfi yang mengubah data dengan panjang berapa pun menjadi nilai hash yang berdimensi tetap dan bersifat satu arah, sehingga hasil hash tidak dapat dikembalikan ke dalam bentuk data aslinya. Hash memilki sifat derterministrik, dimana input yang sama akan menghasilkan otput yang sama, dan akan sangat sensitif terhadap perubahan kecil pda input sehingga mampu mendeteksi perubahan data. Oleh karena itu, hash funcation banyak digunakan untuuk menjaga integritas data, autentikasi, ttanda tanga  digital, penyimpanan password, dan berbagai keamanan informasi lainya.

Sementara itu, Proof of Work (PoW) merupakan mekanisme konsensus dalam teknologi blockhain yang mengharuskan komputer untuk melakukan proses perhitungan hash secara berulang untuk menemukan nilai tertentu yang memenuhi tingkat kesulitan jaringan sebagai bukti krtja.Proses ini membutuhkan daya komputasi dan juga energi yang besar, sehingga mempersulit pihak tidak bertanggung jawab untuk melakuakan pemalsuan transaksi atau mengubah data. Dengan kombinasi hash funcation dan PoW, sistem digital dapat menjamin keamanan, keabshan transaksi, serta kepercayaan antar pengguna dalam lingkungan terdistribusi.

---
## 3. Alat dan Bahan
- Python 3.11 
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---
## 4. Langkah Percobaan
1. Membuat file tinychain.py di folder praktikum/week13-tinychain/src/.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah python tinychain.py.
4. Mengerjakan laporan.md
5. Membuat file hasil.png di folder praktikum/week13-tinychain/sreenshoots/

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
