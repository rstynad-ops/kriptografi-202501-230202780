# Laporan Praktikum Kriptografi
Minggu ke-: 10 Topik:Publik Key Infrastructure(PKI & Certificate Authority)  Nama: Resty Chonifatul Jannah NIM: 230202780 Kelas: 5 Ikrb 

---
## 1. Tujuan
1. Membuat sertifikat digital sederhana.
2. Menjelaskan peran Certificate Authority (CA) dalam sistem PKI.
3. Mengevaluasi fungsi PKI dalam komunikasi aman (contoh: HTTPS, TLS).
   
---
## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )

---
## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Google chrome

---
## 4. Langkah Percobaan
1. Membuat file `pki_cert.py` di folder `praktikum/week10-pki/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python pki_cert.py`.
4. Menjawab pertanyaan diskusi
 
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
- Pertanyaan 1: Apa fugsi utama Certificate Authority (CA)?
- Pertanyaan 2: Mengapa self-signed certificate tidak cukup untuk sistem produksi?
- Pertanyaan 3: Bagaimana PKI mencegah serangan MITM dalam komunikasi TSL/HTTPS?
Jawab :
1. Certificate Authority (CA) berfungsi sebagai pihak tepercaya yang menerbitkan dan memverifikasi sertifikat digital, CA memeastikan bahwa identitas pemilik sertifikat (seperti website atau server) benar-benar valid dan sesuai dengan kunci publik yang digunakan. Dengan adanya CA, pengguna dapat mempercayai bahwa komunikasi dilakukan dengan pihak yang sah, bukan pihak palsu.
2. self-signed certificate ditandatangai oleh pemiliknya sendiri tanpa verifikasi dari pihak ketiga tepertcaya. Akibatnya,browser atau aplikasi tidak dapat memastikan keaslian identitas server dan akan menampilkan peringatan keamanan. Dalam sistem produksi, hal ini beresiko karena sertifikat tersebut mudah dipalsukan dan tidak memberikan tingkat kepercayaan yang cukup untuk melindungi komunikasi pengguna.
3. Public Key Infrastructure (PKI) mencegah serangan Man-in-the-Middle dengan menggunakan sertifikat digital yang diverivikasi oleh CA. saat koneksi TSL atau HTTPS dibuat, klien akan memeriksa keabsahan sertifikat server, termasuk tanda tangan Ca dan masa berlakunya. Jika sertifikat valid, klien dan server melakukan pertukaran kunci secara aman untuk mengenkripsikan data, sehingga pihak ketiga tidak dapat menyadap atau memodifikasi komunikasi 
---
## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan
)

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
```
commit week10-pki
Author: Resty Chonifatul jannah <230202780>
Date:   2026-01-01

    week10-pki: Public Key Infrastructure (PKI & Certificate Authority)
```
