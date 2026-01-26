# Laporan Praktikum Kriptografi
Minggu ke-: 14 Topik: Analisis Serangan Kriptografi Nama:Resty Chonifatul Jannah  NIM: 230202780 Kelas: 5 Ikrb 

---
## 1. Tujuan
1. Mengidentifikasi jenis serangan pada sistem informasi nyata.
2. Mengevaluasi kelemahan algoritma kriptografi yang digunakan.
3. Memberikan rekomendasi algoritma kriptografi yang sesuai untuk perbaikan keamanan.

---
## 2. Dasar Teori
Analisis serangan kripptografi merupakan proses mempelajari bagaimana suatu sistem keamanan dapat diserang atau ditebus, dengan tujuan mengetahui kelemahanya dan meningkatkan tingkat keamanannya. Dalam kriptografi, keamanan data harus menjaga kerahasian informasi, keutuhan data, dan keaslian pengirim agar tidak mudah dimanipulasi oleh pihak yang tidak berwenang.

Ada beberapa jenis serangan yang sering terjadi adalah brute force attack, yaitu mencoba semua kemungkinan password atau kunci sampai berhasil, serta dictionary attack, yaitu menebak password menggunakan daftar kata yang sering dipakai pengguna. Serangan ini biasanya berhasil jika pengguna memakai password yang lemah atau sistem tidak membatasi jumlah percobaan login. Selain itu, ada juga serangan Man-in-the-Middle, yaitu penyerang menyadap komunikasi antara dua pihak dan bisa mencuri atau mengubah data jika koneksi tidak dienkripsi dengan baik.

Dalam analisis kriptografi, penting untuk membedakan kelemahan algoritma dan kelemahan implementasi. Algoritma bisa saja aman secara teori, tetapi menjadi tidak aman karena kesalahan dalam penerapan, seperti penggunaan kunci yang terlalu pendek, penyimpanan password yang tidak terenkripsi, atau kesalahan konfigurasi sistem. Oleh karena itu, analisis serangan kriptografi membantu memahami potensi risiko dan cara memperkuat keamanan sistem.

---
## 3. Alat dan Bahan
- Python 3.11 
- Visual Studio Code / editor lain  
- Git dan akun GitHub
- Google Chrome
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---
## 4. Langkah Percobaan
1. Membuat file `dictionary_atteck_demo.py` di folder `praktikum/week14-analisis-serangan/src/`.
2. Menulis kode Python untuk mensimulasikan penyimpanan password MySpace menggunakan algoritma hash MD5 tanpa salt.
3. Membuat file teks dictionary.txt yang berisi kumpulan password umum seperti 123456, password, qwerty, dan 12345678.
4. Mengimplementasikan fungsi dictionary attack untuk mencocokkan hash MD5 hasil kebocoran dengan daftar password pada file dictionary.txt.Menyalin kode program dari panduan praktikum.
5. Mencatat hasil keluaran (output) ketika password berhasil ditemukan melalui proses dictionary attack.
4. Menjalankan program dengan perintah `python dictionary_atteck_damo..py`.

---
## 5. Source Code
```import hashlib

# Password asli (simulasi korban)
password_asli = "password"

# Hash MD5 dari password
target_hash = hashlib.md5(password_asli.encode()).hexdigest()

print("Hash yang bocor:", target_hash)
print("-" * 40)

# Baca dictionary dan tebak password
with open("dictionary.txt", "r") as file:
    for kata in file:
        kata = kata.strip()
        hash_kata = hashlib.md5(kata.encode()).hexdigest()
        print("Mencoba:", kata)

        if hash_kata == target_hash:
            print("\n✅ Password ditemukan:", kata)
            break
```
Hasilnya :
```
c3b5aa765d61d8327deb882cf99
----------------------------------------
Mencoba: 123456
Mencoba: password

✅ Password ditemukan: password
```

---

## 6. Hasil dan Pembahasan
Hasil eksekusi program dictionary_atteck_demo.py :
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/a25b3920-4201-48c1-a1c2-73ccce210d21" />
Berdasarkan hasil eksekusi program dictionary_attack_demo.py, sistem berhasil menemukan password asli dengan mencocokkan nilai hash MD5 dari daftar kata (dictionary). Program membaca setiap kata dalam file dictionary.txt, kemudian mengubahnya menjadi hash MD5 dan membandingkannya dengan hash target. Ketika hash yang dihasilkan sama dengan hash target, program menampilkan bahwa password berhasil ditemukan. Hal ini menunjukkan bahwa password yang sederhana dan umum dapat dengan mudah ditebak menggunakan metode dictionary attack.

Percobaan ini membuktikan bahwa penggunaan algoritma MD5 tanpa salt sangat rentan terhadap serangan. Karena MD5 memiliki kecepatan komputasi yang tinggi, proses pencocokan hash dapat dilakukan dengan cepat sehingga peluang keberhasilan serangan menjadi besar. Selain itu, jika daftar kata yang digunakan semakin lengkap, maka kemungkinan password ditemukan juga semakin tinggi. Oleh sebab itu, sistem yang masih menggunakan MD5 untuk penyimpanan password tidak lagi aman dan perlu diganti dengan algoritma yang lebih kuat seperti bcrypt, scrypt, atau Argon2 untuk meningkatkan keamanan data pengguna.

---
## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1:Mengapa banyak sistem lama masih rentan terhadap brute force atau dictionary attack?
- Pertanyaan 2:Apa bedanya kelemahan algoritma dengan kelemahan implementasi?
- Pertanyaan 3:Bagaimana organisasi dapat memastikan sistem kriptografi mereka tetap aman di masa depan?
Jawab:
1. Banyak sistem lama masih rentan karena menggunakan algoritma kriptografi yang sudah usang, panjang kunci yang pendek, serta metode penyimpanan password yang tidak aman seperti tanpa hashing atau salting. Selain itu, keterbatasan teknologi pada saat sistem tersebut dibuat membuatnya tidak dirancang untuk menghadapi kemampuan komputasi modern yang jauh lebih cepat.
2. Kelemahan algoritma terjadi ketika metode kriptografi itu sendiri memiliki celah matematis atau desain yang dapat dieksploitasi. Sementara itu, kelemahan implementasi terjadi akibat kesalahan dalam penerapan algoritma, seperti penggunaan kunci yang lemah, pengelolaan kunci yang buruk, atau kesalahan pemrograman, meskipun algoritmanya sebenarnya aman.
3. Organisasi dapat menjaga keamanan sistem kriptografi dengan selalu memperbarui algoritma dan standar keamanan, menerapkan panjang kunci yang kuat, melakukan audit keamanan secara berkala, serta mengikuti perkembangan ancaman siber. Selain itu, pelatihan sumber daya manusia dan penerapan kebijakan keamanan yang baik juga penting untuk mengurangi risiko kesalahan manusia.
   
---
## 8. Kesimpulan
Berdasarkan percobaan, password yang disimpan menggunakan hash MD5 tanpa salt dapat dengan mudah ditebak menggunakan metode dictionary attack. Hal ini menunjukkan bahwa algoritma MD5 sudah tidak aman untuk melindungi data sensitif. Oleh karena itu, diperlukan penggunaan algoritma hash yang lebih kuat agar keamanan sistem dapat ditingkatkan.

---
## 10. Commit Log:
```
commit week14-analisis-serangan
Author: Resty Chonifatu Jannah <rstynad@gmail.com>
Date:   2026-01-26

    week14-analisis-serangan: Analisis Serangan Kriptografi )
```
