# Laporan Praktikum Kriptografi
Minggu ke-: 15 Topik: TinyCoin ERC20  Nama: Resty Chonifatul Jannah NIM: 230202780 Kelas: 5 Ikrb

---
## 1. Tujuan
1. Mengembangkan proyek sederhana berbasis algoritma kriptografi.
2. Mendokumentasikan proses implementasi proyek ke dalam repository Git.
3. Menyusun laporan teknis hasil proyek akhir.

---
## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )

---

## 3. Alat dan Bahan
- Remix IDE   
- Git dan akun GitHub  
- Google Chrome
  
---
## 4. Langkah Percobaan
1. Membuat file TinyCoin.sol di Remix.IDE
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan klik menu compile.
4. Lalu masuk ke bagian deploy pilih vm pada bagian environment dan masukan nilai
5. initialsupply lalu klik deploy dan contract berhasil dibuat.
6. Menu balanceof untuk mengecek nilai initial supply dengan memasukan alamat account.
7. Menu transfer untuk melakukan transfer dengan cara memasukan alamat account lain dan masukan nilai kemudian klik transact dan akan berhasil jika pada bagian terminal ada centang hijau.

---
## 5. Source Code

```// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract TinyCoin is ERC20 {
    constructor(uint256 initialSupply) ERC20("TinyCoin", "TNC") {
        _mint(msg.sender, initialSupply);
    }
}
```
---
## 6. Hasil dan Pembahasan
<img width="1920" height="1080" alt="AKUNPERTAMA" src="https://github.com/user-attachments/assets/f5e8af78-74a2-4154-bf08-032edcdb415a" />

Akun pertama (Account 1) berperan sebagai deployer smart contract TinyCoin pada lingkungan Remix VM (London). Akun ini secara otomatis menerima seluruh initial supply token saat kontrak di-deploy melalui fungsi constructor. Akun ini memiliki alamat 0x5B38Da6a701c568545dCfcB03FcB875f56beddC4 yang bertindak sebagai pengirim token pada proses pengujian fungsi transfer untuk mendistribusikan token ke akun lain.pada gambar tersebut akun pertam memiliki saldo sebesar 99900., yang nantinya akan dikirim ke akun ke dua.

<img width="1920" height="1080" alt="AKUNKEDUA" src="https://github.com/user-attachments/assets/fdb30877-db41-4985-bf81-c0bebac866fb" />

Akun kedua dengan alamat 0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2 berperan sebagai penerima token pada pengujian smart contract TinyCoin dan berhasil menerima 100 TNC dari akun pertama melalui fungsi transfer, yang menunjukkan bahwa mekanisme distribusi token ERC20 berjalan dengan baik.

<img width="1920" height="1080" alt="SETELAHTRANSFER" src="https://github.com/user-attachments/assets/2f0f7253-7df7-4f94-8624-309fab3b7762" />

Setelah proses transfer dilakukan pada akun pertama saldo berkurang menjadi 99800, yang mana itu artinya transferberhasil karena saldo pada akun pertama berkurang dan saldo aku kedua bertambah.

---
## 7. Jawaban Pertanyaan
- Pertanyaan 1:Apa fungsi utama ERC20 dalam ekosistem blockchain?
- Pertanyaan 2:Bagaimana mekanisme transfer token bekerja dalam kontrak ERC20?
- Pertanyaan 3: Apa risiko utama dalam implementasi smart contract dan bagaimana cara mitigasinya?
Jawab :
1. ERC20 merupakan standar teknis yang digunakan untuk membuat dan mengelola token pada blockchain Ethereum. Standar ini memastikan bahwa setiap token memiliki antarmuka dan fungsi yang seragam, seperti totalSupply, balanceOf, dan transfer, sehingga token dapat digunakan secara kompatibel di berbagai aplikasi, dompet digital, dan platform pertukaran. Dengan adanya standarisasi ini, pengembang tidak perlu membangun sistem token dari awal, sementara pengguna dapat dengan mudah menyimpan, mengirim, dan memperdagangkan token tanpa hambatan integrasi. Selain itu, ERC20 memungkinkan token merepresentasikan berbagai jenis aset digital, seperti mata uang kripto, token utilitas, maupun hak akses tertentu dalam sebuah sistem terdesentralisasi.
2. Mekanisme transfer token pada kontrak ERC20 dilakukan melalui fungsi transfer atau transferFrom. Ketika pengguna melakukan transfer, smart contract akan memverifikasi apakah saldo pengirim mencukupi untuk melakukan transaksi. Jika saldo mencukupi, jumlah token akan dikurangi dari alamat pengirim dan ditambahkan ke alamat penerima, kemudian transaksi tersebut dicatat dalam bentuk event pada blockchain. Proses ini dijalankan secara otomatis dan transparan oleh smart contract sehingga tidak memerlukan pihak ketiga sebagai perantara. Untuk skenario tertentu, seperti transaksi melalui platform pihak ketiga, mekanisme approve dan transferFrom digunakan agar pemilik token dapat memberikan izin kepada pihak lain untuk melakukan transfer dalam batas tertentu.
3. Implementasi smart contract memiliki beberapa risiko utama, seperti kesalahan pemrograman, celah keamanan, kesalahan konfigurasi saat deployment, serta penggunaan gas yang tidak efisien. Kesalahan logika dalam kode dapat menyebabkan kerugian finansial atau kegagalan fungsi kontrak, sementara celah keamanan dapat dimanfaatkan oleh pihak tidak bertanggung jawab. Risiko ini dapat diminimalkan dengan menggunakan library standar yang telah teruji, melakukan pengujian secara menyeluruh di testnet, menerapkan praktik pemrograman aman, serta melakukan audit kode sebelum kontrak digunakan secara luas. Selain itu, dokumentasi yang baik dan verifikasi kontrak juga penting untuk memastikan transparansi dan keandalan sistem.
   
---
## 8. Kesimpulan
Berdasarkan hasil praktik pembuatan dan pengujian smart contract TinyCoin (ERC20) menggunakan Remix IDE dengan lingkungan JavaScript VM (London), smart contract berhasil di-deploy dengan baik oleh akun pertama sebagai deployer. Akun tersebut secara otomatis menerima seluruh initial supply token melalui fungsi constructor, yang menunjukkan bahwa proses inisialisasi token berjalan sesuai dengan perancangan dan standar ERC20.

Pengujian fungsi transfer menunjukkan bahwa mekanisme distribusi token berfungsi dengan benar. Hal ini dibuktikan dengan berkurangnya saldo token pada akun pertama sebagai pengirim dan bertambahnya saldo token pada akun kedua sebagai penerima dengan jumlah yang sesuai. Perubahan saldo tersebut menandakan bahwa transaksi berhasil dieksekusi, sementara total supply token tetap konsisten setelah transaksi, sehingga smart contract TinyCoin telah memenuhi fungsi dasar token ERC20 dan layak digunakan sebagai implementasi token sederhana berbasis blockchain.

---
## 9. Daftar Pustaka
---
## 10. Commit Log
```
commit week15-tinycoin-erc20
Author: Resty Chonifatul Jannah <rstynad@gmail.com>
Date:   2026-01-27

    week15-tinycoin-erc20: TinyCoin ERC20 )
```
