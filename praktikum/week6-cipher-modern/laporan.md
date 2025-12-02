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

1. DES (Data Encryption Standard)
DES adalah algoritma kriptografi modern awal yang menggunakan kunci simetrik, artinya kunci yang sama dipakai untuk proses enkripsi dan dekripsi. DES bekerja dengan membagi data menjadi blok 64 bit dan melakukan proses substitusi serta permutasi dalam 16 putaran menggunakan kunci sepanjang 56 bit. Walaupun DES dulu sangat populer dan digunakan secara luas, kini dianggap tidak lagi aman karena kuncinya terlalu pendek sehingga dapat diretas menggunakan brute force. Karena itu, DES sudah digantikan oleh algoritma yang lebih kuat seperti AES.
2. AES (Advanced Encryption Standard)
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
Hasil eksekusi implementasi DES:

<img width="1919" height="1079" alt="Screenshot 2025-12-02 233014" src="https://github.com/user-attachments/assets/88a3dbbc-bc99-41d5-a0aa-845d4e5c2759" />

Hasil eksekusi implementasi AES:

<img width="1920" height="1080" alt="Screenshot 2025-12-02 233543" src="https://github.com/user-attachments/assets/0a71cb3a-e181-4a1e-bd6e-8d436ed3ac4f" />

Hasil eksekusi implementasi RSA:

<img width="1920" height="1080" alt="Screenshot 2025-12-02 233729" src="https://github.com/user-attachments/assets/99ac8be0-e8ac-4e41-9bb3-400602537962" />

Pembahasan: 

Hasil eksekusi menunjukkan bahwa ketiga algoritma bekerja sesuai konsepnya:
1. DES berhasil mengenkripsi dan mendekripsi teks dengan benar, namun keamanannya lemah karena panjang kuncinya pendek.
2. AES menghasilkan ciphertext acak dan mampu mengembalikan plaintext dengan tepat, menunjukkan keamanan dan efisiensi yang tinggi.
3. RSA juga berjalan baik, menggunakan kunci publik untuk enkripsi dan kunci privat untuk dekripsi, membuktikan konsep asimetrisnya.
---
## 7. Jawaban Pertanyaan
- Pertanyaan 1: Apa perbedaan mendasar antara DES, AES, dan RSA dalam hal kunci dan keamanan?
- Pertanyaan 2: Mengapa AES lebih banyak digunakan dibanding DES di era modern?
- Pertanyaan 3: Mengapa RSA dikategorikan sebagai algoritma asimetris, dan bagaimana proses pembangkitan kuncinya?
 Jawab:
1. DES dan AES adalah algoritma enkripsi simetris, artinya menggunakan satu kunci yang sama untuk proses enkripsi dan dekripsi. DES menggunakan kunci yang relatif pendek (56 bit), sehingga sekarang dianggap tidak aman karena mudah diretas menggunakan brute force. Sementara itu, AES menggunakan kunci jauh lebih panjang (128/192/256 bit) sehingga sangat kuat dan tahan terhadap serangan modern. RSA adalah algoritma enkripsi asimetris, yang berarti menggunakan dua kunci berbeda: kunci publik untuk enkripsi dan kunci privat untuk dekripsi. Keamanannya tidak bergantung pada panjang kunci simetris, tetapi pada kesulitan matematis memfaktorkan bilangan prima besar, yang membuatnya aman untuk komunikasi dan autentikasi.
2. AES lebih banyak digunakan karena jauh lebih aman dan efisien dibanding DES. Kunci DES hanya 56 bit, yang dapat diretas dengan brute force dalam waktu singkat menggunakan komputer modern. Sebaliknya, AES menawarkan kunci hingga 256 bit yang sangat sulit ditembus bahkan oleh superkomputer. Selain itu, AES dirancang agar lebih cepat, lebih fleksibel, dan lebih optimal digunakan pada perangkat modern seperti smartphone, komputer, maupun perangkat IoT. Karena faktor keamanan dan performa inilah AES menjadi standar enkripsi global yang menggantikan DES.
3. RSA disebut algoritma asimetris karena menggunakan dua kunci berbeda namun saling terkait:
   - Kunci publik → digunakan untuk enkripsi atau verifikasi tanda tangan
   - Kunci privat → digunakan untuk dekripsi atau membuat tanda tangan

Kedua kunci tersebut tidak dapat saling menggantikan, sehingga bersifat asimetris.

Proses pembangkitan kuncinya secara sederhana adalah:

1. Pilih dua bilangan prima besar, misalnya 𝑝 dan 𝑞.
2. Hitung 𝑛 = 𝑝×𝑞, yang akan menjadi bagian dari kunci publik.
3. Hitung nilai totien: 𝜙(𝑛) = (𝑝−1)(𝑞−1).
4. Pilih bilangan 𝑒 yang relatif prima terhadap 𝜙(𝑛) → ini menjadi eksponen publik.
5. Hitung nilai 𝑑 sebagai invers modular dari 𝑒 terhadap 𝜙(𝑛) → ini menjadi eksponen privat.
6. Hasilnya:
   . Kunci publik = (e, n)
   . Kunci privat = (d, n)

Keamanan RSA berasal dari fakta bahwa meskipun n diketahui publik, sangat sulit memfaktorkan n kembali menjadi p dan q, selama nilai p dan q sangat besar (biasanya 2048 bit atau lebih).

---
## 8. Kesimpulan
DES, AES, dan RSA berbeda dalam jenis algoritma dan keamanan. DES sudah tidak digunakan karena kunci 56 bit mudah diretas sehingga AES menjadi standar keamanan baru karena lebih aman dan efisien dengan ukuran kunci hingga 256 bit. Sedangkan RSA termasuk algoritma asimetris karena menggunakan dua kunci berbeda untuk menjaga keamanan datanya dan biasanya digunakan untuk tanda tangan digital.

---
## 10. Commit Log
```
commit week6-cipher-,modern
Author: Resty Chonifatul Jannah <rstynad@gmail.com>
Date:   2025-12-02

    week6-cipher-modern: Cipher Modern (DES, AES, RSA)
```
