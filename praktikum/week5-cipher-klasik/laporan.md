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

**Langkah 1 - Implementasi Caesar Ciper**

```
def caesar_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, key):
    return caesar_encrypt(ciphertext, -key)

# Contoh uji
msg = "CLASSIC CIPHER"
key = 3
enc = caesar_encrypt(msg, key)
dec = caesar_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```
Hasilnya:
```
Plaintext : CLASSIC CIPHER
Ciphertext: FODVVLF FLSKHU
Decrypted : CLASSIC CIPHER
```

**Langkah 2 - Implementasi Vigenere Ciper**

```
def vigenere_encrypt(plaintext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

def vigenere_decrypt(ciphertext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base - shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

# Contoh uji
msg = "KRIPTOGRAFI"
key = "KEY"
enc = vigenere_encrypt(msg, key)
dec = vigenere_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```
Hasilnya: 
```
Plaintext : KRIPTOGRAFI
Ciphertext: UVGZXMQVYPM
Decrypted : KRIPTOGRAFI
```

**Langkah 3 - Implementasi Transposisi Sederhana**

```
def transpose_encrypt(plaintext, key=5):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key
    return ''.join(ciphertext)

def transpose_decrypt(ciphertext, key=5):
    num_of_cols = int(len(ciphertext) / key + 0.9999)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(ciphertext)
    plaintext = [''] * num_of_cols
    col = 0
    row = 0
    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1
        if (col == num_of_cols) or (col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1
    return ''.join(plaintext)

# Contoh uji
msg = "TRANSPOSITIONCIPHER"
enc = transpose_encrypt(msg, key=5)
dec = transpose_decrypt(enc, key=5)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```
Hasilnya:
```
Plaintext : TRANSPOSITIONCIPHER
Ciphertext: TPIPROOHASNENICRSTI
Decrypted : TRANSPOSITIONCIPHER
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
