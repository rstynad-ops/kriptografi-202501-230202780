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
1. Membuat file `diffie_hellman.py` di folder `praktikum/week7-diffie-hellman/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python diffie_helllman.py`.
4. Membuat folder screenshots dan mengupload file hasil.jpg pada folder`praktikum/week7-diffie-hellman/screenshot/.
5. Mengerjakan soal yang ada pada folder praktikum/week7-diffie-helman/laporan.md/
---
## 5. Source Code
Langkah 1- Diffie-helman
```import random
# parameter umum (disepakati publik)
p = 23  # bilangan prima
g = 5   # generator

# private key masing-masing pihak
a = random.randint(1, p-1)  # secret Alice
b = random.randint(1, p-1)  # secret Bob

# public key
A = pow(g, a, p)
B = pow(g, b, p)

# exchange public key
shared_secret_A = pow(B, a, p)
shared_secret_B = pow(A, b, p)

print("Kunci bersama Alice :", shared_secret_A)
print("Kunci bersama Bob   :", shared_secret_B)
```
Hasilnya:
```
Kunci bersama Alice : 8
Kunci bersama Bob   : 8
```
Langkah 2- Analisis serangan MITM (Men-In-The_Middle)
```
import random

# parameter publik
p = 23  # bilangan prima
g = 5   # generator

# private key Alice, Bob, dan Eve
a = random.randint(1, p-1)  # secret Alice
b = random.randint(1, p-1)  # secret Bob
e = random.randint(1, p-1)  # secret Eve

# public key asli
A = pow(g, a, p)  # public Alice
B = pow(g, b, p)  # public Bob

# public key Eve
E = pow(g, e, p)

# =========================
# SERANGAN MITM OLEH EVE
# =========================
# Eve mencegat dan mengganti public key
# - Alice menerima public key Eve (bukan Bob)
# - Bob menerima public key Eve (bukan Alice)

# Alice menghitung kunci bersama (dengan Eve)
shared_Alice = pow(E, a, p)

# Bob menghitung kunci bersama (dengan Eve)
shared_Bob = pow(E, b, p)

# Eve menghitung kedua kunci
shared_Eve_with_Alice = pow(A, e, p)
shared_Eve_with_Bob   = pow(B, e, p)

# =========================
# OUTPUT
# =========================
print("Kunci Alice (mengira dengan Bob) :", shared_Alice)
print("Kunci Bob   (mengira dengan Alice):", shared_Bob)

print("\nKunci Eve dengan Alice :", shared_Eve_with_Alice)
print("Kunci Eve dengan Bob   :", shared_Eve_with_Bob)
```
Hasilnya:
```
Kunci Alice (mengira dengan Bob) : 3
Kunci Bob   (mengira dengan Alice): 12

Kunci Eve dengan Alice : 3
Kunci Eve dengan Bob   : 12
```
Penjelasan simulasi:
pada simulasi ini, algoritma Difffie-hellman digunakan untuk membentuk kunci rahasia bersama antara Alice dan Bob menggunakan parameter publik p dan g, namun proses pertukaran publik key diserang oleh pihak ke tiga (Eve) deng metode Men-In-The-Middle. Eve mencegat public key yang dikirimkan Alice dan Bob lalu menggantinya dengan public key milinya sendiri, sehingga Alice dan Bob masing-masing menghitung kuci rahasia yang dimiliki Alice dan Bob menjadi berbeda, sementara Eve mengetahui kedua kunci tersebut dan dapat menyadap atau memodifikasi komunikasi tanpa disadari yang menunjukan bahwa diffie-Hellman tanpa autentikasirentan terhadap serangan Man-In-The-Middle.

---
## 6. Hasil dan Pembahasan
Hasil eksekusi program Diffie-Hellman:

<img width="1920" height="1080" alt="hasil diffiehelman" src="https://github.com/user-attachments/assets/3b0b597c-2ca6-416c-9482-0da53cd135d5" />

Pembahasan:
Algoritma Diffie-Hellman berhasil menghasilkan kunci shared bersama tanpa mengirimkan kunci rahasia secara langsung. Setiap kali dijalankan, hasilnya akan selalu berbeda dikarenakan privat key dihasilkan secara acak melalui kode a = random.randint(1, p-1) b = random.randint(1, p-1) , meskipun begitu selama hasil eksekusi nilai Alice dan Bob sama maka algoritma bekerja dengan benar. Jadi setiap kali Alice dan Bob memulai pertukaran kunci baru maka mereka akan selalu membuat kunci privat baru. Hal ini lah yang membuat Diffie-Hellman sangat sulit diretas karena kuncinya selalu berbeda dan akan sangat aman jika digabungkan dengan autentikasi tambahan untuk mencegah serangan Man-In-The-Middle.

Hasil Analisis Serangan MITM (Man-In-The_Middle):

<img width="1920" height="1080" alt="hasil mitm" src="https://github.com/user-attachments/assets/c56244e4-55d7-4c99-9b36-656fd436e158" />

Pembahsan:
Simulasi diatas menunjukan terjadinya serangan Man-in-the-Middle pada proses pertukaran kunci Diffie–Hellman. Alice, Bob, dan Eve masing-masing memiliki private key, lalu menghasilkan public key berdasarkan parameter publik p dan g. Namun, saat pertukaran public key berlangsung, Eve mencegat komunikasi dan menggantikan public key Alice dan Bob dengan public key miliknya sendiri. Akibatnya, Alice menghitung kunci rahasia menggunakan public key Eve dan mengira kunci tersebut milik Bob, begitu pula Bob yang menghitung kunci rahasia menggunakan public key Eve dan mengira berasal dari Alice. Hasil eksekusi program memperlihatkan bahwa kunci Alice dan Bob berbeda, sementara kunci Alice sama dengan kunci Eve–Alice dan kunci Bob sama dengan kunci Eve–Bob, sehingga Eve mengetahui kedua kunci rahasia tersebut. Hal ini membuktikan bahwa Diffie–Hellman tanpa mekanisme autentikasi rentan terhadap serangan Man-in-the-Middle, karena tidak dapat menjamin keaslian public key yang dipertukarkan.

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
Berdasarkan simulasi yang dilakukan, algoritma Diffie–Hellman terbukti mampu menghasilkan kunci rahasia bersama antara dua pihak, namun tanpa mekanisme autentikasi algoritma ini rentan terhadap serangan Man-in-the-Middle. Pada serangan tersebut, pihak ketiga dapat mencegat dan mengganti public key sehingga Alice dan Bob tidak benar-benar berbagi kunci satu sama lain, sementara penyerang justru mengetahui kedua kunci rahasia yang terbentuk. Oleh karena itu, penggunaan Diffie–Hellman harus dikombinasikan dengan metode keamanan tambahan seperti tanda tangan digital, sertifikat, atau protokol TLS agar pertukaran kunci dapat berlangsung secara aman.

---
## 10. Commit Log
```
commit week7-diffie-hellman
Author: Resty Chonifatul Jannah <rstynad@gmail.com>
Date: 2025-12-08

    week7-diffie-hellman: Diffie-Hellman Key Exchange
```
