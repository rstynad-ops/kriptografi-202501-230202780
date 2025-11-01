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
- Google Chrome
---

## 4. Langkah Percobaan
1. Membuat file `entropy-unicity.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `entropy_unicity.py`
4. Mengupload hasil eksekusi dangan nama file hasil.png di folder praktikum/week4-entropy_unicity/screenshot/.
5. Membuat laporan pada  file laporan.md di folder praktikum/week4-entropy_unicity/laporan.md

---

## 5. Source Code
```
import math

def entropy(keyspace_size):
    return math.log2(keyspace_size)

print("Entropy ruang kunci 26 =", entropy(26), "bit")
print("Entropy ruang kunci 2^128 =", entropy(2**128), "bit")

def unicity_distance(HK, R=0.75, A=26):
    return HK / (R * math.log2(A))

HK = entropy(26)
print("Unicity Distance untuk Caesar Cipher =", unicity_distance(HK))

def brute_force_time(keyspace_size, attempts_per_second=1e6):
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600*24)
    return days

print("Waktu brute force Caesar Cipher (26 kunci) =", brute_force_time(26), "hari")
print("Waktu brute force AES-128 =", brute_force_time(2**128), "hari")
```
---
## 6. Hasil dan Pembahasan
```
Entropy ruang kunci 26 = 4.700439718141092 bit
Entropy ruang kunci 2^128 = 128.0 bit
Unicity Distance untuk Caesar Cipher = 1.3333333333333333
Waktu brute force Caesar Cipher (26 kunci) = 3.0092592592592593e-10 hari
Waktu brute force AES-128 = 3.938453320844195e+27 hari
```
Pembahasan: 
1. Entropy ruang kunci 26=4.700439718141092 bit, entropynya sangat rendah karena hanya ada 26 kemungkinan pergeseran dan keamanan kunci hanya setara dengan kurang ari 5 bit data biner.
2. Entropy ruang kunci 2^128=128.0 bit, pengguna entropy sangat tinggi karena ada 128.0 kemungkinan kunci unik.
3. Unicity Distance untuk caesar cipher=1.3333333333333333, panjang chipertext hanya sepanjang 1 sampai 2 huruf sehingga sangat mudah untuk memecahkan kode dangan menganalisis frekuensinya.
4. waktu brute force Caesar Chiper (26 kunci)= 3.0092592592592593e-10 hari, pemecahan kunci dapat dilakukan dengan mencoba semua 26 kunci secara instan dalam waktu hitungan detik.
5. Waktu brute force AES-128= 3.938453320844195e+27 hari, Jumlah waktu yang digunakan sangat lama sehingga tidak memungkinkan untuk memecahkan kode dengan brute force.

Hasil eksekusi program entropy_unicity:
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/30ee3591-22fb-43b6-b5b8-23f68c3e0f0e" />

---
## 7. Jawaban Pertanyaan 
- Pertanyaan 1: Apa arti dari nilai entropy dalam konteks kekuatan kunci?
- 
Jawab :Nilai entropy dalam konteks kekuatan kunci adalah untuk menunjukan tingkat ketidakpastian atau keacakan dari suatu ruang kunci. Semakin besar nilai entropy, semakin banyak kemungkinan kunci yang dapat di gunakan, sehingga sulit bagi penyerang untuk menebak atau mencoba seluruh kunci yang mungkin.

- Pertanyaan 2: Mengapa unicity ditence penting dalam menentukan keamanan suatu cipher?

Jawab : Unicity distence menunjukan erapa banyak potongan ciphertext yang dibutuhkan agar kunci enkripsi bisa ditebak dengan pasti oleh penyerang. Jika ciphertext yang di dapat lebih sedikit dari unicity distence, maka masih ada banyak kemungkinan kunci (cipher masih aman), tetapi jika ciphertext yang didapat lebih banyak dari nilai unicity distence, maka penyerang bisa menemukan kunci yang benar secara unik( cipher bisa dibobol). Jadi, semakin besar nilai unicity distence, maka semakin aman pula suatu cipher terhadap ananlisis kunci.

- Pertanyaan 3: Mengapa btrute force masih menjadi ancaman meskipun algoritma sudah kuat?

Jawab : brute force akan tetap menjadi ancama karena kemajuan komputasi, penggunaan kunci lemah atau pendek, kesalahan implementasi, serta potensi komputer kuantum dimasa depan.

---
## 10. Commit Log
```
week4-entropy-unicity
Author: Resty chonifatul Jannah
Date:   2025-11-1

    week4-entropy-unicity: Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force)

```
