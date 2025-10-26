# Laporan Praktikum Kriptografi
Minggu ke-:3 Topik: moodmath Nama: Resty Chonifatul Jannah NIM: 230202780 Kelas: 5 ikrb

---

## 1. Tujuan
1. Menyelesaikan operasi aritmetika modular.
2. Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).
3. Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.
## 2. Dasar Teori
1. Modular Arithmetic (Aritmetika Modular)
   
Aritmetika modular merupakan konsep dasar dalam matematika diskrit yang berperan penting dalam bidang kriptografi. Aritmetika ini bekerja berdasarkan operasi sisa hasil bagi suatu bilangan terhadap bilangan lain yang disebut modulus. Secara umum ditulis dengan notasi:
a mod m=r (ketika bilangan 𝑎 dibagi dengan 𝑚, menghasilkan sisa 𝑟. Misalnya, 17 mod 5 = 2 karena 17 dibagi 5 menyisakan 2)

Dalam aritmetika modular dikenal konsep kongruensi, yaitu ketika dua bilangan memiliki sisa pembagian yang sama terhadap suatu modulus. Hal ini ditulis sebagai:
a ≡ b (mod m),ketika a−b habis dibagi 𝑚.Sebagai contoh, 23 ≡ 3(mod 10) karena 23 dan 3 memiliki sisa yang sama yaitu 3 saat dibagi 10.
                                                                                
Aritmetika modular memiliki beberapa sifat penting, antara lain:

-Penjumlahan: (𝑎+𝑐)≡(𝑏+𝑑)(mod 𝑚) 
-Pengurangan: (𝑎−𝑐)≡(𝑏−𝑑)(mod 𝑚)
-Perkalian: (𝑎×𝑐)≡(b×d)(mod 𝑚)

aritmetika modular digunakan secara luas untuk mengamankan data melalui proses enkripsi dan dekripsi. Beberapa algoritma kriptografi yang menggunakan operasi modular antara lain RSA (Rivest–Shamir–Adleman), Diffie–Hellman Key Exchange, dan ElGamal Encryption. Misalnya pada RSA, proses enkripsi dilakukan dengan rumus. 

2. Greatest Common Divisor (GCD)
   
Greatest Common Divisor (GCD) atau Faktor Persekutuan Terbesar (FPB) adalah bilangan bulat positif terbesar yang dapat membagi dua bilangan tanpa meninggalkan sisa. Sebagai contoh, GCD (18,24)=6 karena 6 adalah bilangan terbesar yang membagi kedua bilangan tersebut secara tepat. Untuk menghitung GCD, digunakan metode Algoritma Euclidean (Euclidean Algorithm) yang lebih efisien dibandingkan mencari faktor satu per satu. Prinsip algoritma ini adalah:
GCD (a,b) = GCD (b,a mod b),Langkah perhitungan dilakukan secara berulang hingga sisa pembagian bernilai nol.
Misalnya, untuk mencari GCD(48,18): 48 mod 18 = 12,18 mod 12 = 6,12 mod 6 = 0, Maka diperoleh hasil GCD = 6.

GCD memiliki peranan penting untuk menentukan apakah dua bilangan relatif prima (coprime), yaitu jika GCD (a,m) = 1. Jika dua bilangan bersifat relatif prima, maka bilangan 𝑎 memiliki invers modular terhadap modulus 𝑚. Invers modular digunakan dalam proses dekripsi, terutama pada algoritma RSA, untuk menemukan kunci privat 𝑑 yang memenuhi persamaan: a×d ≡ 1(mod m), dalam algoritma RSA, nilai eksponen publik 𝑒 harus memenuhi syarat GCD(𝑒,𝜑(𝑛))= 1 agar dapat memiliki invers modular sebagai kunci privat 𝑑. Dengan demikian, GCD tidak hanya digunakan untuk perhitungan matematis, tetapi juga menjadi bagian penting dalam keamanan kriptografi berbasis kunci publik.

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
