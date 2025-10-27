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
---

## 4. Langkah Percobaan

1.Membuat file dengan nama modular_math.py di folder praktikum/week3-modmath/src/.
2.Menyalin kode program dari panduan praktikum.
3.Menjalankan program dengan perintah sesuai nama file.
4.Mengaploud hasil screenshot program (hasil.png) di folder praktikumweek3-modmath/screenshots/
5.Mengerjakan soal diskusi

---

## 5. Source Code

*Langkah 1-Aritmetika Modular*
```
def mod_add(a, b, n): return (a + b) % n
def mod_sub(a, b, n): return (a - b) % n
def mod_mul(a, b, n): return (a * b) % n
def mod_exp(base, exp, n): return pow(base, exp, n)  # eksponensiasi modular

print("7 + 5 mod 12 =", mod_add(7, 5, 12))
print("7 * 5 mod 12 =", mod_mul(7, 5, 12))
print("7^128 mod 13 =", mod_exp(7, 128, 13))

```
*Langkah 2-GCD dan Algoritma Euclidean*
```
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("gcd(54, 24) =", gcd(54, 24))
```
*Langkah 3 — Extended Euclidean Algorithm*
```
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = egcd(b % a, a)
    return g, y1 - (b // a) * x1, x1

def modinv(a, n):
    g, x, _ = egcd(a, n)
    if g != 1:
        return None
    return x % n

print("Invers 3 mod 11 =", modinv(3, 11))  # hasil: 4
```
*Langkah 4 — Logaritma Diskrit (Discrete Log)*

```
def discrete_log(a, b, n):
    for x in range(n):
        if pow(a, x, n) == b:
            return x
    return None

print("3^x ≡ 4 (mod 7), x =", discrete_log(3, 4, 7))  # hasil: 4
``   
Hasil Penggabungan Kode:
``   
def mod_add(a, b, n): return (a + b) % n
def mod_sub(a, b, n): return (a - b) % n
def mod_mul(a, b, n): return (a * b) % n
def mod_exp(base, exp, n): return pow(base, exp, n)  # eksponensiasi modular

print("7 + 5 mod 12 =", mod_add(7, 5, 12))
print("7 * 5 mod 12 =", mod_mul(7, 5, 12))
print("7^128 mod 13 =", mod_exp(7, 128, 13))

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("gcd(54, 24) =", gcd(54, 24))

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = egcd(b % a, a)
    return g, y1 - (b // a) * x1, x1

def modinv(a, n):
    g, x, _ = egcd(a, n)
    if g != 1:
        return None
    return x % n

print("Invers 3 mod 11 =", modinv(3, 11))  # hasil: 4

def discrete_log(a, b, n):
    for x in range(n):
        if pow(a, x, n) == b:
            return x
    return None

print("3^x ≡ 4 (mod 7), x =", discrete_log(3, 4, 7))  # hasil: 4
```
Hasil :
```
7 + 5 mod 12 = 0
7 * 5 mod 12 = 11
7^128 mod 13 = 3
gcd(54, 24) = 6
Invers 3 mod 11 = 4
3^x ≡ 4 (mod 7), x = 4
```
--
## 6. Hasil dan Pembahasan
Hasil Program :
<img width="1919" height="1078" alt="hasil" src="https://github.com/user-attachments/assets/c6ab364c-bfbe-4dfd-b794-1e88103da676" />

Pembahasan : Semua percobaan berhasil tanpa eror, dan hasil keluaran sesuia dengan teori dasar kriptografi.
---

## 7. Jawaban Pertanyaan
- Pertanyaan 1: Apa peran aritmetika modular dalam kriptografi modern?
- 
  jawab : Aritmetika modular merupakan dasar utama dalam kriptografi modern karena digunakan dalam hampir seluruh operasi matematika pada proses enkripsi dan dekripsi. Prinsip ini bekerja pada sistem bilangan terbatas dengan modulus tertentu, sehingga hasil perhitungannya tetap berada dalam ruang nilai yang terkontrol.
  
- Pertanyaan 2: Mengapa invers modular penting dalam algoritma kunci publik (misalnya RSA)?
  
  jawab : Pada algoritma RSA, invers modular digunakan untuk menentukan kunci privat (d) berdasarkan kunci publik (e). Nilai 𝑑diperoleh sebagai invers dari 𝑒 terhadap fungsi totien Euler 𝜑(𝑛), sehingga memenuhi hubungan: 𝑒 × 𝑑 ≡ 1 (mod 𝜑(𝑛)).Proses ini menjamin bahwa pesan yang dienkripsi menggunakan kunci publik hanya dapat didekripsi menggunakan kunci privat yang sesuai. Dengan demikian, invers modular berperan sebagai mekanisme matematis yang menghubungkan kunci publik dan kunci privat, serta memastikan keamanan komunikasi dalam sistem kriptografi asimetris.
  
- pertanyaan 3: Apa tantangan utama dalam menyelesaikan logaritma diskrit untuk modulus besar?
  
  jawab : Tantangan utama dalam logaritma diskrit untuk modulus besar Masalah utama dalam logaritma diskrit adalah sulitnya menemukan nilai pangkat yang sesuai saat modulusnya sangat besar. Tidak ada cara cepat untuk menghitungnya, sehingga membutuhkan waktu komputasi yang sangat lama. Kesulitan inilah yang membuat algoritma seperti Diffie-Hellman dan ElGamal tetap aman digunakan.
---

## 8. Kesimpulan

Berdasarkan hasil uji coba dapat disimpulakn bahwa aritmetika modular, algoritma Euclidean, invers modular, dan logaritma diskrit memiliki keterkaitan erat serta menjadi landasan utama dalam kriptografi modern. Aritmetika modular berfungsi menjaga hasil operasi tetap dalam rentan tertentu, algoritma algoritma Euclidean berperan dalam menentukan bilangan yang saling relatif prima, invers modular digunakan pada proses dekripsi dalam sistem kunci publik, dan logaritma diskrit menjadi faktor keamanan utama karena sulit dipecahkan pada modulus besar. Secara keseluruhan, ke empat konsep tersebut merupakan elemen penting yang menopang sistemkeamanan data digital dalam algoritma kriptografi seperti RSA dan Diffie-Hellman.
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
