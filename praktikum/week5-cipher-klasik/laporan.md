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
**1.Caesar Ciper**
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/67d0949d-d20e-497f-8b38-54cf08073468" />

**2.Vigenere Ciper**
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/371810c0-5b8a-4c49-bf32-89a85fa8ebe7" />

**3.Transposisi Sederhana**
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/feb3d40a-57ea-4c05-a3eb-5f0b93144511" />

**Pembahasan :**
Berdasarkan hasil program yang telah dilakukan, ketiga algoritma clasik ciper,yaitu Caesar Ciper, Vigenere Ciper, dan Tranposisi Sederhana berhasil melakukan proses enkripsi dan deskripsi dengan tepat. Caesar Ciper menggeser huruf berdasarkan nilai kunci  tertentu, Vigenere Ciper mengunakan kata kunci untuk menghasilkan pola enkripsi yang lebih kompleks, sedangkan Transposisi Sederhana mengacak urutan huruf tanpa mengubah karakter aslinya. Dari hasil yang proses enkripsi deskripsi yang telah dilakukan menunjukan bahwa algoritma dapat mengubah teks  asli menjadi ciphertext kemudian di mengembalikannya sesuasi teks aslinya, hal  ini  juga yang menandakan bahwa implementasi program berjalan sesuai teori kriptografi klasik.

---

## 7. Jawaban Pertanyaan
- Pertanyaan 1:Apa kelemahan utama algoritma Caesar Cipher dan Vigenère Cipher?
- Jawab:
Kelemahan Caesar Ciper terletak pada mekanismenya yang sangat sederhana ya sederhana dimana hanya dengan menggeser huruf dengan jumlah tertentu. Ruang kuncinya terbatas, sehingga mudah ditebak hanya dengan mencoba beberapa kali kemungkinan pergeseran. Selain itu, Pola kemunculan huruf dalam teks masih tampak jelas, sehingga metode analisis frekuensi dapat dengan mudah digunakan untuk menebak isi pesan.

Vigenère Cipher memiliki kelemahan ketika kunci yang digunakan terlalu pendek atau pola kuncinya berulang. Pengulangan ini menimbulkan pola tertentu pada hasil enkripsi, sehingga seseorang dapat memperkirakan panjang kuncinya. Setelah panjang kunci diketahui, ciphertext bisa dipecah berdasarkan posisi huruf terhadap kunci, dan setiap bagian dapat dianalisis frekuensinya sampai pesan asli berhasil diungkap.

- Pertanyaan 2:Mengapa cipher klasik mudah diserang dengan analisis frekuensi?
- Jawab: Ciper Klasik mudah diserang dengan analisis frekuensi karena proses enkripsinya tidak benar-benar "mengacak" pola bahasa. Huruf-huruf yang sering muncul pada teks alsi tetap muncul dengan frekuensi yang hampir sama pada ciphertext,tetapi dalam bentuk huruf lain. Bahasa memiliki pola khas , misalnya huruf tertentu sering muncul, ada kombinasi huruf yang umum, dan ada huruf yang jarang dipakai. Pola-pola ini masih terbawa dalam ciphertext, sehingga penyerang cukup memetakan frekuensi kemunculan huruf untuk menebak huruf aslinya satu per satu.
  
- Pertanyaan 3:Bandingkan kelebihan dan kelemahan cipher substitusi vs transposisi.
- Jawab:Cipher substitusi mengganti setiap huruf dengan huruf lain berdasarkan aturan tertentu, sedangkan cipher transposisi hanya menukar posisi huruf tanpa mengganti karakter itu sendiri. Kelebihan cipher substitusi adalah sederhana dan cepat diterapkan, tetapi mudah diretas melalui analisis frekuensi. Sementara itu, cipher transposisi lebih sulit dipecahkan dengan analisis frekuensi karena huruf tidak berubah, namun tetap dapat diserang jika pola penukarannya terdeteksi.

---

## 8. Kesimpulan
Ketiga algoritma berhasil melakukan proses enkripsi dan dekripsi dengan benar sehingga setiap ciphertext yang dihasilkan dapat dikembalikan menjadi plaintext asli menggunakan kunci yang sama. Penggunaan caesar cipher terbukti paling sederhana namun mudah dipecahkan, Vigenère cipher memberikan keamanan lebih baik dengan penggunaan kunci sedangkan transposisi mengacak urutan huruf untuk menambah tingkat keamanan pesan.

---

## 10. Commit Log
```
commit week5-cipher-klasik
Author: Resty Chonifatul Jannah
Date:   2025-11-10

    week5: Cipher Klasik ( Caesar, Vigenere, Transposisi)
```
