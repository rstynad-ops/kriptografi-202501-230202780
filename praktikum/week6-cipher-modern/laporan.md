# Laporan Praktikum Kriptografi
Minggu ke-: 6  Topik: Cipher Modern Nama: Resty Chonifatul Jannah NIM: 230202780  Kelas: 5 Ikrb  

---
## 1. Tujuan
1. Mengimplementasikan algoritma DES untuk blok data sederhana.
2. Menerapkan algoritma AES dengan panjang kunci 128 bit.
3. Menjelaskan proses pembangkitan kunci publik dan privat pada algoritma RSA.
---
## 2. Dasar Teori
Cipher Modern merupakan teknik penyandian data dalam kriptogaarafi yang digunakan pada era komputer dan jaringan digital. berbeda dengan cipher klasik yang hanya mengandalkan subtitusi dan transposisi sederhana,cipher modern menggunakan algoritma matematis kompleks, operasi bit, transformasi blok, serta kunci yang panjang dan acak. tujuan utamanya adalah untuk memastikan kerahasiaan, integritas, serta keamanan data dalam proses komunikasi digital.

Karakteristik Cipher Modern
1. Menggunakan kunci yang panjang dan acak sehingga sulit ditebak.
2. Bekerja dengan data digital, yaitu bit atau blok data.
3. Tahan terhadap serangan kriptanalisis modern, seperti brute-force, differential cryptanalysis, dan linear cryptanalysis.
4. Cepat dan efisien, karena dioptimalkan untuk perangkat keras maupun perangkat lunak.
5. Memiliki fungsi enkripsi dan dekripsi yang terstruktur, dengan operasi seperti XOR, rotasi bit, substitusi, dan permutasi.

1.DES (Data Encryption Standard)
DES adalah algoritma kriptografi modern awal yang menggunakan kunci simetrik, artinya kunci yang sama dipakai untuk proses enkripsi dan dekripsi. DES bekerja dengan membagi data menjadi blok 64 bit dan melakukan proses substitusi serta permutasi dalam 16 putaran menggunakan kunci sepanjang 56 bit. Walaupun DES dulu sangat populer dan digunakan secara luas, kini dianggap tidak lagi aman karena kuncinya terlalu pendek sehingga dapat diretas menggunakan brute force. Karena itu, DES sudah digantikan oleh algoritma yang lebih kuat seperti AES.

2.AES (Advanced Encryption Standard)
AES adalah algoritma enkripsi simetrik yang menjadi standar modern dan sangat aman digunakan saat ini. AES bekerja pada blok data 128 bit dengan panjang kunci 128, 192, atau 256 bit, membuatnya lebih tahan terhadap serangan brute force. Algoritma ini menggunakan beberapa langkah seperti SubBytes, ShiftRows, MixColumns, dan AddRoundKey, yang dilakukan secara berulang dalam 10–14 putaran tergantung panjang kunci. AES banyak dipakai pada sistem keamanan modern seperti WiFi, VPN, aplikasi pesan instan, dan penyimpanan data karena cepat, efisien, dan sangat kuat.

3. RSA (Rivest-Shamir-Adleman)
RSA merupakan algoritma kriptografi asimetrik yang menggunakan dua kunci berbeda: kunci publik untuk enkripsi dan kunci privat untuk dekripsi. Keamanan RSA bergantung pada kesulitan memfaktorkan bilangan besar yang merupakan hasil perkalian dua angka prima yang sangat besar. RSA tidak cocok untuk mengenkripsi data dalam jumlah besar karena prosesnya lebih lambat, tetapi sangat ideal untuk pertukaran kunci, tanda tangan digital, dan autentikasi. RSA menjadi dasar keamanan komunikasi internet seperti HTTPS dan protokol email aman.

---
## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Google Chrome
- pip install pycryptodome

---
## 4. Langkah Percobaan
1. Membuat file `aes.py` ,`des.py`, `rsa.py` di folder `praktikum/week6-cipher-modern/src/`.
2. Menyalin kode program dari panduan praktikum.
3. membuat folder screenshots dan mengupload file `hasil.png`
4. mengerjakan soal
---

## 5. Source Code
1. Langka 1-DES
```
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

key = get_random_bytes(8)  # kunci 64 bit (8 byte)
cipher = DES.new(key, DES.MODE_ECB)

plaintext = b"ABCDEFGH"
ciphertext = cipher.encrypt(plaintext)
print("Ciphertext:", ciphertext)

decipher = DES.new(key, DES.MODE_ECB)
decrypted = decipher.decrypt(ciphertext)
print("Decrypted:", decrypted)
```
Hasilnya: 
```
Ciphertext: b'\xc1E\xbe#\x98\xafne'
Decrypted: b'ABCDEFGH'
```
2. Langkah 2-AES 128
```
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)  # 128 bit key
cipher = AES.new(key, AES.MODE_EAX)

plaintext = b"Modern Cipher AES Example"
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

print("Ciphertext:", ciphertext)

# Dekripsi
cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted = cipher_dec.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())
```
Hasilnya:
```
Ciphertext: b'\xff\x00,\xc6i\xcf\xb0\xc0\xe7\xe7\\\xd5\x06u!Q\xd0Ki\xa4\n>E\xa7:'
Decrypted: Modern Cipher AES Example
```
5. Langkah 3-RSA
```
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate key pair
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Enkripsi dengan public key
cipher_rsa = PKCS1_OAEP.new(public_key)
plaintext = b"RSA Example"
ciphertext = cipher_rsa.encrypt(plaintext)
print("Ciphertext:", ciphertext)

# Dekripsi dengan private key
decipher_rsa = PKCS1_OAEP.new(private_key)
decrypted = decipher_rsa.decrypt(ciphertext)
print("Decrypted:", decrypted.decode())
```
Hasilnya:
```
Ciphertext: b'Y\xe9j\x06Us\xf1v\x9d\xb7-\x10F/*E\xd8\xc0B\x94h\x88~\xb1Q9p\xee/\'\xb8F$\x01\xb3\xad\n6\x8e\x18^\n\xce)\xaa\xb8h\xab64\xf3\x1fW\xd6\xc3i3\x98\xfc\xa1~qi\xde\xbav\xab\']\xe8\xee\x1f\x17\xab\x0e\xb4\xce\x8f\x84\x8c\x9eg\xb9\xf9B:\xda8\xb3vZ\xd0\xe6\xf5\x9f\xca\xfb\x08\t\xd6\xf9\xbd\xaa\xb9\xa6~81|\xba3\xb7\x13\x12<X7\x19\x81\x0e/\xf4\xbfm\xae\xbb\xa1\x88\x90\x91H\xa8\x82\xe1\xa6\xce\xfb\xaf\x93L\x10\xbf\xd7\xb7\x8bC\x08iVB\x11\xa3\x7fn}n\xc2/\x8d\xa4\xe4\xda\xb7\xc9\xe3\xee&SD\x00\x08g\x0f\x86pu\xce\x9a\x99\x8dM\xbbm\x8b\xe5\xcdE\x1e\x97 \xaa#Js\x9a<\xe8\xce\xf2\xed/&\x85\x91\xe0N\xc1$\xa6\x1c0\xee\xad\xfa\x94\x93\xfa\x97sP\xf1"\'\x99\xe2\xfb\x8aQ&\xa8\xd5\x84\xf80\xact\xe3\xaeG0\xc2I`\x10E\xd89 u\xa3\xcb\xa4\x02\nN\xb8'
Decrypted: RSA Example
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
commit week6-cipher-,modern
Author: Resty Chonifatul Jannah <rstynad@gmail.com>
Date:   2025-12-02

    week6-cipher-modern: Cipher Modern (DES, AES, RSA)
```
