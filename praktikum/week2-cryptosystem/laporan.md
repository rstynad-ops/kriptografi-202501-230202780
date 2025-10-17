# Laporan Praktikum Kriptografi
Minggu ke-:2 Topik:week2-cryptosystem Nama:Resty Chonifatul jannah  NIM:230202780 Kelas:5 ikrb

---

## 1. Tujuan
1. Mengidentifikasi komponen dasar kriptosistem (plaintext, ciphertext, kunci, algoritma).
2. Menggambarkan proses enkripsi dan dekripsi sederhana.
3. Mengklasifikasikan jenis kriptosistem (simetris dan asimetris).

## 2. Dasar Teori
Komponen - komponen Kriptosistem
Dalam  sebuah kriptosistem, terdapat beberapa komponen utama yang bekerja sama untuk melakukan proses enkripsi (penyandian) dan deskripsi (pembacaan kembali). Berikut komponen-komponen utamanya:
- Plaintext atau pesan asli merupakan data asli yang akan dikirim atau disimpan dengan aman.
Plaintext ini berupa teks,angka,gambar,atau informasi lain sebelum di enkripsi.
- Chipertext adalah hasil dari proses enkripsi terhadap plaintext menggunakan algoritma tertentu. Chipertext tidak bisa dibaca tanpa mengetahui kunci yang digunakan untuk mendeskripsikan pesan.
- Algoritma enkripsi merupakan proses atau aturan matematis yang digunakan untuk mengubah plaintext menjadi chipertext.
- Algoritma deskripsi yaitu kebalikan dari enkripsi, digunakan untuk mengubah pesan dari chipertext kembali menjadi plaintext menggunakan kunci tertentu,yang mana biasanya menggunakan algoritma yang sama atau serupa dengan proses enkripsi.
- Kunci atau Key merupakan nilai rahasuia yang di gunakan dalam proses enkripsi dan deskripsi. Tanpa kunci, pesan tidak dapat dikembalikan ke bentuk aslinya, kunci inilah yang membuat sistem aman.
## Kriptografi simetris & asimetris
- Kriptografi sismetris merupakan sistem enkripsi yang menggunakan kata kunci yang sama dengan untuk proses deskripsi. Cara kerja dari kriptografi sismertis yaitu, pengirim mengenkripsi pesan dengan suatu kunci, dan penerima harus memiliki kunci yang sama untuk mendeskripsikan pesan tersebut. Contoh algoritma yang sering digunakan ialah, DES,AES,RC4.
- Kriptografi asimetris merupakan kebalikan dari kriptografi simetris yang mana kriptografi asimetris menggukan dua kunci yang berbeda,yaitu kunci public(proses enkripsi pesan), dan kunci privat(untuk deskripsi pesan). cara kerja dari kriptografi asimetris yaitu, pengirim mengenkripsi pesan menggunakan kunci public penerima, dan penerima membuka pesan dengan menggunakan kunci privat miliknya. Contoh algoritma yang sering digunakan ialah, RSA,DSA,dan ECC.
  
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

def encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def decrypt(ciphertext, key):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift - key) % 26 + shift)
        else:
            result += char
    return result

if __name__ == "__main__":
    message = "<230202780><Resty Chonifatul Jannah>"
    key = 5

    enc = encrypt(message, key)
    dec = decrypt(enc, key)

    print("Plaintext :", message)
    print("Ciphertext:", enc)
    print("Decrypted :", dec)
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
