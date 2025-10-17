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
1. Membuat ringkasan perbedaan antara kriptosistem simetris dan asimetris.
2. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
3. Menyalin kode program dari panduan praktikum.
4. Menjalankan program dengan perintah `python caesar_cipher.py`.
5. Mengaploud hasil eksekusi di folder praktikum/week2-cryptosistem/screenshots/
6. Menjawab pertanyaan diskusi.

---

## 5. Source Code
Simulasi enkripsi & dekripsi menggunakan substitusi sederhana (misalnya Caesar Cipher).
```
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
```
Ekspetasi Keluaran
```
Plaintext : <230202780><Resty Chonifatul Jannah>
Ciphertext: <230202780><Wjxyd Hmtsnkfyzq Ofssfm>
Decrypted : <230202780><Resty Chonifatul Jannah>
```
---

## 6. Hasil dan Pembahasan

Diagram Kriptosistem : 

<img width="481" height="221" alt="diagram_kriptosistem" src="https://github.com/user-attachments/assets/292134e8-2f67-46a9-9ca1-412bd80210c0" />


Hasil eksekusi program Caesar Cipher:
<img width="1919" height="1079" alt="Screenshot 2025-10-17 215128" src="https://github.com/user-attachments/assets/dff8d9dd-bbf6-4a49-84dd-5d24b3a60a19" />
<img width="1919" height="1069" alt="Screenshot 2025-10-17 215334" src="https://github.com/user-attachments/assets/bf1c6b3a-65fc-416b-aa29-6467b8f31002" />

---

## 7. Pertanyaan
1. Sebutkan komponen utama dalam sebuah kriptosistem.
2. Apa kelebihan dan kelemahan sistem simetris dibandingkan asimetris?
3. Mengapa distribusi kunci menjadi masalah utama dalam kriptografi simetris?
## Jawaban :  
- Pertanyaan 1:
- Plaintext :Pesan asli yang ingin dikirim atau disembunyikan
- Kunci :Hasil dari proses enkripsi yang tidak dapat dibaca tanpa kunci dekripsi.
- Key (Kunci), Informasi rahasia yang digunakan dalam proses enkripsi dan dekripsi.
- Algoritma Enkripsi/Dekripsi, Metode atau aturan yang digunakan untuk menyandikan dan membuka pesan.
- Pertanyaan 2:
## Sistem Kriptogafi Simetris
- Kelebihan :
  1.Proses lebih cepat, enkripsi dan deskripsi tidak membutuhkan komputasi rumit
  2.Efisien untuk data besar, cocok digunakan untuk mengenkripsi file besar
  3.Algoritma sederhana, mudah diimplementasikan dan tidak membutuhkan perangkat keras mahal
-  Kelemahan :
  1.Masalah distribusi kunci, kunci rahasia harus dibagikan ke pihak lain secara aman
  2.Tidak cocok untuk banyak pengguna, karena setiap pasangan pengguna butuh kunci berbeda,   sehingga sulit dikelola
  3.Tidak ada otentifikasi identitas, penerima tidak bisa memastikan siapa pengirim sebenarnya,karena semua pihak memakai kunci yang sama.
## Sistem Kriptografi Asimetris
- Kelebihan
  1.Keamanan tinggi, karena menggunakan dua kunci yang berbeda
  2.Distribusi kunci lebih aman, tidak perlu mengirimkan kunci rahasia ke penerima
  3.Mendukung otentifikasi dan tandatangan digital
  4.Cocok untuk komunikasi banyak pihak
- Kelemahan
  1.Proses lebih lambat, enkripsi dan deskripsi memerlukan perhitungan matematika kompleks
  2.Membutuhkan sumber daya besar, memerlukan daya komputasi tinggi dan waktu yang lebih lama
  3.Implementasi lebih rumit, pengelolaan duakunci perlu sistem keamanan tambahan agar tdk bocor
- Pertanyaan 3 :
Karena kriptografi simetris hanya menggunakan kunci tunggal untuk enkripsi dan dekripsi sehingga dalam proses distribusi sangat berisiko terhadap penyadapan atau pencurian.
---

## 8. Kesimpulan
Dari praktikum ini,dapat disimpulkan bahwa kriptosistem terdiri dari beberapa komponen utama, yaitu plaintext, ciphertext, algoritma enkripsi dan dekripsi, serta kunci.Pada kriptografi simetris, prosesnya cepat karena menggunakan satu kunci yang sama, tapi memiliki kelemahan pada distribusi kunci yang berisiko disadap.Sedangkan pada kriptografi asimetris, digunakan dua kunci berbeda yaitu publik dan privat, sehingga lebih aman, namun prosesnya lebih lambat.
Jadi, bisa disimpulkan bahwa pemilihan jenis kriptografi tergantung pada kebutuhan, jika ingin cepat gunakan sistem simetris, dan jika ingin lebih aman gunakan sistem asimetris.

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
