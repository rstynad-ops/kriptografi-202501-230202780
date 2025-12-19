# Laporan Praktikum Kriptografi
Minggu ke-: 9 Topik: Digital Signature (RSA/DSA)  Nama: Resty Chonifatul Jannah NIM: 230202780 Kelas: 5 ikrb

---
## 1. Tujuan
1. Mengimplementasikan tanda tangan digital menggunakan algoritma RSA/DSA.
2. Memverifikasi keaslian tanda tangan digital.
3. Menjelaskan manfaat tanda tangan digital dalam otentikasi pesan dan integritas data.

---
## 2. Dasar Teori
Digital signature merupakan mekanisme kriptografi yang mulai berkembang sejak akhir 1970-an setelah diperkenalkannya konsep kriptografi kunci publik oleh Diffie dan Hellman, dengan tujuan memberikan jaminan keamanan pada dokumen dan pesan digital agar memiliki kekuatan kepercayaan yang setara dengan tanda tangan konvensional. Digital signature berfungsi untuk menjamin keasilan pengirim, keutuhan data, dan nirpenyangkalan, sehinggga pesan yang dikirim tidak dapat disangkal oleh pengirimnya.

Salah satu algoritma yang paling banyak digunakan adalah RSA, yang diperkenalkan pada tahun 1997 oleh Rivest, Shamir, dan Adleman, dan memiliki keunggulan karena dapat digunakan baik untuk proses enkripsi maupun tanda tangan digital, dimana penandatanganan dilakukan menggunakan kunci privat dan proses verifikasi menggunakan kunci publik.

Selain itu, terdapat DSA (digital Signature Algorithm) yang dikembangkan oleh National Institute of Standards and Tachnology (NIST) pada tahun 1991 sebagai standar resmi tanda tangan digital, yang secara khusus dirancang hanya untuk digital signature serta menghasilkan tanda tangan berdasarkan kunci privat, nilai hash pesan, dan bilangan acak. Hingga saat ini, RSA dan DSA menjadai komponen penting dalam sistem keamanan informasi modern karena banyak diterapkan pada sertifikat digital, transaksi elektronik, dan berbagi layanan komunikasi daring yang membutuhkan tingkat keamanan dan kepercayaan yang tinggi.

---
## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Google Chrome

---
## 4. Langkah Percobaan
1. Membuat file `signature.py` di folder `praktikum/week9-digital-signature/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python signature.py`.
4. Mencoba memodifikasi program
5. Menjawab soal diskusi
6. Membuat folder `Screenshots` di folder `praktikum/wekk9-digital` lalu mengupload hasil praktikum di dalam folder tersebut.

---
## 5. Source Code
Langkah 1-Generate Key dan Buat Tanda Tangan
```from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate pasangan kunci RSA
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Pesan yang akan ditandatangani
message = b"Hello, ini pesan penting."
h = SHA256.new(message)

# Buat tanda tangan dengan private key
signature = pkcs1_15.new(private_key).sign(h)
print("Signature:", signature.hex())
```
Langkah 2-Verifikasi Tanda Tangan
```
try:
    pkcs1_15.new(public_key).verify(h, signature)
    print("Verifikasi berhasil: tanda tangan valid.")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak valid.")
```
Langkah 3-Uji Modifikasi Pesan 
```
# Modifikasi pesan
fake_message = b"Hello, ini pesan palsu."
h_fake = SHA256.new(fake_message)

try:
    pkcs1_15.new(public_key).verify(h_fake, signature)
    print("Verifikasi berhasil (seharusnya gagal).")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak cocok dengan pesan.")
```

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
commit Week9-digital-signature
Author: Resty Chonifatul Jannah
Date:   2025-12-20

    week9-digital-signature: implementasi Caesar Cipher dan laporan )
```
