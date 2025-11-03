# Laporan Praktikum Kriptografi
Minggu ke-: 5  Topik: Cipher Klasik (Caesar,Vigenere, Transposisi)  Nama: Resty Chonifatul Jannah NIM: 230202780 Kelas: 5 Ikrb  

---
## 1. Tujuan
1. Menerapkan algoritma Caesar Cipher untuk enkripsi dan dekripsi teks.
2. Menerapkan algoritma Vigenère Cipher dengan variasi kunci.
3. Mengimplementasikan algoritma transposisi sederhana.
4. Menjelaskan kelemahan algoritma kriptografi klasik.
---
## 2. Dasar Teori
1. Caesar Cipher

Caesar Cipher merupakan salah satu bentuk cipher subtitusi monoalfabetik, dimana setiap karakter dalam plaintext digantikan oleh karakter lain yang berjarak tetap pada urutan alfabet.
Secara matematis, proses enkripsi dapat dinyatakan dengan persamaan :
<img width="262" height="45" alt="image" src="https://github.com/user-attachments/assets/deff2a71-5a33-4533-a57d-56d68f2d780a" />

dan deskripsi dengan :

<img width="245" height="35" alt="image" src="https://github.com/user-attachments/assets/8844701a-ab7f-4220-8ca6-f1c8fa90e423" />

di mana :

P= huruf plaintext,

C= huruf cipertext,

K= nilai pergeseran(kunci)
   
2. Vigenere Cipher

Vigenere Cipher merupakan perkembangan dari sistem subtitusi yang bersifat polialfabetik,diperkenalkan oleh Blaise de Vigenere pada abad ke-16. Cipher ini menggunakan serangkaian alfabet subtitusi berdasarkan kata kunci (keyword), sehinngga setiap huruf pada plaintext dapat disandikan dengan pergeseran berbeda tergantung kata kunci yang bersesuaian. Secara matematis, rumus enkripsi dinyatakan sebagai :
<img width="281" height="44" alt="image" src="https://github.com/user-attachments/assets/732aa7f6-c563-4e8d-ba4c-14223274c550" />

dengan deskripsi sebagai :

<img width="309" height="50" alt="image" src="https://github.com/user-attachments/assets/11b3be12-fdcd-4914-a743-0397307e993a" />

di mana:

Pi= huruf plaintext ke-i,

Ci= huruf Ciphertext ke-i,

Ki= huruf dari kunci yang diulang sepanjang pesan
        
3. Transposisi Cipher

Transposisi Cipher merupakan proses enkripsi yang dilakukan dengan menuliskan plaintext ke dalam matriks atau pola tertentu, kemudian membacanya kembali menurut urutan kolom atau baris yang ditentukan oleh kunci. Salah satu bentuk umum dari metode ini adalah Columnar Transposition Cipher.

Contoh sederhana: plaintext “DATAAMAN” disusun dalam tabel 4 kolom, kemudian dibaca kolom demi kolom menghasilkan ciphertext “DAAAMTAN”.

---
## 3. Alat dan Bahan

- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Google Chrome
---

## 4. Langkah Percobaan

1. Membuat file `caesar.py` ,`vigenere.py`,dan `transpose.py` di folder `praktikum/week5-cipher-klasik/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar.py`,`vigenere.py`, dan `transpose.py`.
4. Membuat folder screenshots lalu mengupload `hasil.png`.
5. Mengerjakan tugas pertanyaan.

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
