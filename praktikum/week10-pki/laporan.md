# Laporan Praktikum Kriptografi
Minggu ke-: 10 Topik:Publik Key Infrastructure(PKI & Certificate Authority)  Nama: Resty Chonifatul Jannah NIM: 230202780 Kelas: 5 Ikrb 

---
## 1. Tujuan
1. Membuat sertifikat digital sederhana.
2. Menjelaskan peran Certificate Authority (CA) dalam sistem PKI.
3. Mengevaluasi fungsi PKI dalam komunikasi aman (contoh: HTTPS, TLS).
   
---
## 2. Dasar Teori
Public Key Infrastructure (PKI) merupakan sebuah kerangka kerja keamanan yang menggunakan kriptografi kunci publik (asimetris) untuk menjamin kerahasian, integritas, autentikasi, juga non-repudiation dalam komunikasi digital. PKI mengelola proses pembuatan, distribusi, penyimpanan, validasi, dan pencabutan sertifikat digital. PKI bekerja dengan memanfaatkan pasangan kuci publik dan kunci privat, yang mana kunci publik digunakan untuk enkripsi dan verifikasi tanda tanga digital, sedangkan kunci privat digunakan untuk deskripsi dan pembuatan tanda tangan digital. PKI banyak diterapkan pada sistem SSL/TLS (HTTPS), email aman,VPN, dan keamanan IoT
Komponen utama PIK : 
- Certificate Authority (CA)
- Registration Authority (RA)
- Sertifikat digital
- Repository sertifikat
- Certificate Revocation List (CRL) atau OCSP

Certificate Authority (CA) adalah pihak ketiga tepercaya dalam sistem PKI yang bertugas untuk memverifikasi identitas pengguna atau sistem serta menerbitkan sertifikat digital. Sertifikat digital yang diterbitkan CA mengaitkan identitas pemilik dengan kunci publiknya dan ditandatangani menggunakan kunci privat CA. Certificate Authority (CA) berperan sebagai akar kepercayaan (trust anchor). Jika dertifikat tidak lagi valid atau terjadi pelanggaran keamanan,Ca dapat mencabut sertifikat tersebut melalui CRL atau Online Certificate Status
Protocol (OCSP). Kepercayaan pada komunikasi digital sangat bergantung pada kredibilitas CA.
PKI ialah sistem manajemen keamanan secara keseluruhan, sedaangkan CA adalah komponen inti PIK yang menjamin keabsahan identitas dan kunci publik. Tanpa CA, PKI tidak dapat membangun kepercayaan antara entitas dalam jarian terbuka.

---
## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Google chrome

---
## 4. Langkah Percobaan
1. Membuat file `pki_cert.py` di folder `praktikum/week10-pki/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python pki_cert.py`.
4. Menjawab pertanyaan diskusi
 
---
## 5. Source Code
      Code python dengan file pki_cert.py :
```from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta

# Generate key pair
key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Buat subject & issuer (CA sederhana = self-signed)
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"ID"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UPB Kriptografi"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"example.com"),
])

# Buat sertifikat
cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.utcnow())
    .not_valid_after(datetime.utcnow() + timedelta(days=365))
    .sign(key, hashes.SHA256())

```# Simpan Sertifikat
with open("cert.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

print("Sertifikat digital berhasil dibuat: cert.pem")
```
---
## 6. Hasil dan Pembahasan
Hasil eksekusi program python pki_cert.py :

<img width="1920" height="1080" alt="hasil pki" src="https://github.com/user-attachments/assets/55e1692b-cea7-435a-9266-e87c17520808" />

Pejelasan :

Program pki_cert.py berhasil mengimplementasikan konsep Public Key Infrastructure (PKI) dengan membuat sertifikat digital X.509 self-signed menggunakan algoritma RSA 2048-bit dan hash SHA-256. Program ini menghasilkan pasangan kunci publik dan privat, menetapkan identitas sertifikat (subject dan issuer yang sama), mengatur masa berlaku sertifikat selama satu tahun, lalu menandatangani sertifikat menggunakan kunci privat sebelum menyimpannya dalam format PEM (cert.pem). Hasil eksekusi menunjukkan bahwa sertifikat berhasil dibuat tanpa kesalahan fatal, sehingga dapat digunakan untuk keperluan simulasi keamanan, praktikum kriptografi, dan pembelajaran dasar PKI.

---
## 7. Jawaban Pertanyaan
- Pertanyaan 1: Apa fugsi utama Certificate Authority (CA)?
- Pertanyaan 2: Mengapa self-signed certificate tidak cukup untuk sistem produksi?
- Pertanyaan 3: Bagaimana PKI mencegah serangan MITM dalam komunikasi TSL/HTTPS?
Jawab :
1. Certificate Authority (CA) berfungsi sebagai pihak tepercaya yang menerbitkan dan memverifikasi sertifikat digital, CA memeastikan bahwa identitas pemilik sertifikat (seperti website atau server) benar-benar valid dan sesuai dengan kunci publik yang digunakan. Dengan adanya CA, pengguna dapat mempercayai bahwa komunikasi dilakukan dengan pihak yang sah, bukan pihak palsu.
2. self-signed certificate ditandatangai oleh pemiliknya sendiri tanpa verifikasi dari pihak ketiga tepertcaya. Akibatnya,browser atau aplikasi tidak dapat memastikan keaslian identitas server dan akan menampilkan peringatan keamanan. Dalam sistem produksi, hal ini beresiko karena sertifikat tersebut mudah dipalsukan dan tidak memberikan tingkat kepercayaan yang cukup untuk melindungi komunikasi pengguna.
3. Public Key Infrastructure (PKI) mencegah serangan Man-in-the-Middle dengan menggunakan sertifikat digital yang diverivikasi oleh CA. saat koneksi TSL atau HTTPS dibuat, klien akan memeriksa keabsahan sertifikat server, termasuk tanda tangan Ca dan masa berlakunya. Jika sertifikat valid, klien dan server melakukan pertukaran kunci secara aman untuk mengenkripsikan data, sehingga pihak ketiga tidak dapat menyadap atau memodifikasi komunikasi 
---
## 8. Kesimpulan

Berdasarkan praktikum yang telah dilakukan, dapat disimpulkan bahwa Public Key Infrastructure (PKI) merupakan sistem penting dalam menjaga keamanan komunikasi digital melalui penggunaan kriptografi kunci publik. Dalam praktikum ini, pembuatan sertifikat digital X.509 self-signed berhasil dilakukan menggunakan bahasa pemrograman Python dengan algoritma RSA 2048-bit dan hash SHA-256. Sertifikat yang dihasilkan menunjukkan bagaimana identitas dan kunci publik dapat diikat secara kriptografis.

Selain itu, praktikum ini juga memperjelas peran Certificate Authority (CA) sebagai pihak tepercaya yang menjamin keabsahan identitas dalam sistem PKI. Walaupun sertifikat self-signed cukup untuk simulasi dan pembelajaran, sertifikat tersebut belum layak digunakan pada sistem produksi karena tidak diverifikasi oleh CA resmi. Dengan demikian, PKI terbukti berperan penting dalam mencegah serangan keamanan seperti Man-in-the-Middle (MITM) dan memastikan komunikasi yang aman pada protokol TLS/HTTPS.

---
## 10. Commit Log
```
commit week10-pki
Author: Resty Chonifatul jannah <230202780>
Date:   2026-01-01

    week10-pki: Public Key Infrastructure (PKI & Certificate Authority)
```
