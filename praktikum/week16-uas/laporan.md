# Laporan Praktikum Kriptografi
Minggu ke-: 16 Topik: UAS KRIPTOGRAFI EDUTOKEN Nama: Resty Chonifatul Jannah  NIM: 230202780 Kelas:5 Ikrb 

---
## 1. Tujuan
Tujuan dikembangkanya EduToken dengan tujuan sebagai berikut:

1. Mengimplementasikan konsep kriptografi dalam aplikasi pembelajaran berbasis web blockchain untuk memeberikan pemehaman praktis kepada pengguna.
2. Mengembangkan platform pembelajaran interaktif yang mengintegrasikan materi kriptografi, kuis, dan sistem reward token digital.
3. Menerapkan teknologi blockchain Etherum melalui smart contract ERC-20 serta penggunaan MetaMaks pada jaringan Sepolia Tesnet.
4. Mendemontrasikan penerapan protokol keamanan, termasuk hashing, autentikasi, integritas data, dan transaksi token digital.
   
---
## 2. Dasar Teori
Teknologi blockchain merupakan teknologi terdistribusi yang menawarkan transparansi, keamanan, dan desentralisasi dalam pencatatan data. Dalam bidang pendidikan, blockchain berpotensi digunakan sebagai sistem pendukung pembelajaran, salah satunya melalui mekanisme reward berbasis token digital untuk meningkatkan motivasi dan partisipasi mahasiswa.

Kriptografi merupakan komponen utama dalam blockchain yang berfungsi untuk menjaga keamanan data dan transaksi. Konsep kriptografi seperti hashing, enkripsi, dan digital signature menjadi dasar dalam pengamanan sistem blockchain. Namun, pembelajaran kriptografi sering dianggap sulit karena bersifat abstrak dan kurang aplikatif.

EduToken merupakan platform pembelajaran yang mengintegrasikan konsep kriptografi dengan teknologi blockchain Ethereum. Melalui smart contract ERC-20 yang dikembangkan menggunakan Solidity dan dijalankan pada jaringan Sepolia Testnet, mahasiswa dapat memperoleh token digital sebagai reward setelah menyelesaikan kuis. Implementasi ini memberikan pengalaman langsung dalam memahami mekanisme smart contract, transaksi token, serta keamanan blockchain tanpa biaya transaksi nyata.

---
## 3. Alat dan Bahan
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Remix IDE
- Akun MetaMaks
- Onrender
- Fron End Menggunakan HTML, CSS, JavaScript
- Smart contract menggunakan solidity
- Network menggunakan Ethereum Sepolia

---
## 4. Langkah Percobaan

1. Login Website EduToken
   <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/b0e89c61-50a6-47f7-a4e9-e6a0832d1e9c" />

   - Masuk ke website Edutoken dengan membuka link ini https://edutoken-crypto.onrender.com
   - login dengan mengisi kolom username dan password yang sebelumya sudah dibuat.
2. Tampilan menu dasboard Edutoken
   <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/90dba3d5-e467-4f2a-863c-fc5ff494cdf8" />

   -tampilan setelah pengguna berhasil login akan masuk ke dalam menu dashboard pada EduToken.
3. Tampilan Menu Materi & Kuis
   <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/87af8399-553f-4361-aaa4-624f193ac32b" />

   - Menu Materi dan Kuis berada tepat dibawah menu Dashboard, pengguna dapat mencoba  mengerjakan kuis dengan meng klik botton "Mulai  kuis  1"
   - Untuk kuis selanjutnya dapat diakses setelah token memilki nilai yang cukup banyak.
 4. Tampialan Quiz
    <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/dba12a71-cb88-43b8-a5a1-fffbf6c83bf8" />

    -Dalam mengerjakan kuis terdaapat 5 pertanyaan dengan durasi 20 detik pengerjaan untuk masing-masing soal.

 5. Tampilan Klaim Token    
    <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c8c59b18-d452-4614-bfc8-908ff43fbd04" />

-Setelah selesai mengerjakan kuiz lalu klik klaim token dan akan terhubung ke akun metamask. Sebelum otomatis terhubung, masing-masing pengguna harus menautkan akun metamask terlebih dahulu menggunakan smart contract EduToken.

6. Tampilan Konfirmasi Klaim Token pada metamaks
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/724b0e12-2472-424c-bea8-1f18df3382bd" />

-Lalu pada bagian pop up Metamaks klik confirm supaya token dapat di klaim.

7.Tampilan Notifikasi Berhasil klaim Token
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/672236da-f17b-4a30-b413-f79304d3b2ea" />

-Setelah berhasil terkirim maka akan muncul notifikasi di web dan di MetaMaks.

8. Transaksi atau klaim token akan tercatat di Sepolia Transaction Hash:
   <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/7b517fdd-fe3b-4ab4-9444-4a6b835b2211" />
9. Tampelan Menu Info Token dan Transfer
    <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c753df52-a586-4e36-b40a-4dd76fff7c31" />

    - Pada menu ini terdapat informasi jumlah token dan menu transfer
    - Jika ingin melakukan transfer masukan alamat wallet teman dan masukan jumlah token yang akan di transfer lalu klik kirim token.
      
10. Kirim token ke teman lewat web EduToken
    <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/433beab2-10d9-44ae-b4b3-8e8255d24846" />

    - Setelah memilih kirim token akan muncul pop up metamask untuk persetujuan dan klik confirm supaya transfer token berhasil dilakukan.

11. Notifikasi Berhasil
    <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/818ac29c-e1f2-4e9f-ae82-2c5f1d028a19" />

    - Setelah melakukan konfirmasi EduToken akan memberikan notifikasi bahwa token berhasil di kirim.

13. Menu profil
    <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/6d601950-5d99-470d-a4d4-0f497002dd94" />

    - Pada menu profil terdapat informasi tentang username pengguna, jumlah token dan riwayat aktivitas belajar.
    - 
---
## 5. Source Code
---

## 6. Hasil dan Pembahasan
Berdasarkan praktikum yang telah dilakukan, sistem EduToken berhasil diimplementasikan dan berjalan sesuai dengan tujuan. Pengguna dapat login, menghubungkan wallet MetaMask, mengakses materi, mengerjakan kuis, serta menerima reward berupa token EDU yang berhasil dikirim ke wallet melalui transaksi blockchain pada jaringan Ethereum Sepolia Testnet. Hasil praktikum menunjukkan bahwa integrasi aplikasi web dengan blockchain berjalan dengan baik, serta penerapan konsep kriptografi seperti kriptografi asimetris, fungsi hash, dan digital signature dapat diamati secara langsung. Melalui praktikum ini, mahasiswa memperoleh pemahaman yang lebih nyata mengenai penerapan kriptografi, meskipun sistem masih memiliki keterbatasan karena berjalan pada jaringan testnet dan bergantung pada keamanan wallet pengguna.

Berikut merupakan kelebihan dan kekurangan sistem EduToken :
Kelebihan Sistem :
Menggunakan teknologi blockchain yang bersifat transparan dan immutable.
Distribusi token dilakukan melalui smart contract ERC-20, sehingga lebih aman dan terotomatisasi.
Keamanan transaksi terjamin dengan penerapan kriptografi asimetris, fungsi hash, dan digital signature.
Private key tidak disimpan di server, karena dikelola langsung oleh MetaMask.
Sistem reward berbasis token meningkatkan interaktivitas dan motivasi belajar pengguna.
Memberikan pengalaman pembelajaran kriptografi secara praktis dan aplikatif.
Kekurangan Sistem
Sistem masih berjalan pada jaringan testnet (Sepolia) sehingga belum digunakan di lingkungan produksi.
Keamanan akun sangat bergantung pada kesadaran pengguna dalam menjaga private key wallet.
Smart contract belum melalui audit keamanan secara mendalam.
Skalabilitas sistem masih terbatas dan belum mendukung untuk digunakan oleh banyak pengguna secara bersamaan.
Ketergantungan pada koneksi internet dan ekstensi MetaMask di sisi pengguna.

---
## 7. Jawaban Pertanyaan

---
## 8. Kesimpulan
Berdasarkan seluruh tahapan perancangan, pengembangan, dan pengujian yang telah dilakukan, sistem EduToken berhasil diimplementasikan sebagai Learning Management System (LMS) interaktif yang terintegrasi dengan teknologi blockchain Ethereum berbasis ERC-20 pada jaringan Sepolia Testnet. Penerapan prinsip kriptografi seperti kriptografi asimetris, hashing Keccak-256, dan tanda tangan digital ECDSA terbukti mampu menjaga keamanan, autentikasi, serta integritas transaksi token EDU. Selain itu, penggunaan token sebagai bentuk gamifikasi pembelajaran menunjukkan bahwa teknologi blockchain dapat menjembatani konsep kriptografi yang bersifat teoritis dengan penerapan Web3 yang lebih praktis dan aplikatif.

---

## 9. Daftar Pustaka
 
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---
## 10. Commit Log
```
commit week16- UAS KRIPTOGRAFI EDUTOKEN
Author: Resty Chonifatul Jannah <rstynad@gmail.com
Date:   2026-01-26

    week16-UAS EduToken: UAS KRIPTOGRAFI EDUTOKEN
```
