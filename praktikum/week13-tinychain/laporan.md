# Laporan Praktikum Kriptografi
Minggu ke-: 13 Topik: Tinychain-Proof of work (PoW)  Nama: Resty Chonifatul Jannah NIM: 230202780 Kelas: 5 ikrb 

---
## 1. Tujuan
1. Menjelaskan peran hash function dalam blockchain.
2. Melakukan simulasi sederhana Proof of Work (PoW).
3. Menganalisis keamanan cryptocurrency berbasis kriptografi.
   
---
## 2. Dasar Teori
Hasd funcation adalah fungsi kriptogarfi yang mengubah data dengan panjang berapa pun menjadi nilai hash yang berdimensi tetap dan bersifat satu arah, sehingga hasil hash tidak dapat dikembalikan ke dalam bentuk data aslinya. Hash memilki sifat derterministrik, dimana input yang sama akan menghasilkan otput yang sama, dan akan sangat sensitif terhadap perubahan kecil pda input sehingga mampu mendeteksi perubahan data. Oleh karena itu, hash funcation banyak digunakan untuuk menjaga integritas data, autentikasi, ttanda tanga  digital, penyimpanan password, dan berbagai keamanan informasi lainya.

Sementara itu, Proof of Work (PoW) merupakan mekanisme konsensus dalam teknologi blockhain yang mengharuskan komputer untuk melakukan proses perhitungan hash secara berulang untuk menemukan nilai tertentu yang memenuhi tingkat kesulitan jaringan sebagai bukti krtja.Proses ini membutuhkan daya komputasi dan juga energi yang besar, sehingga mempersulit pihak tidak bertanggung jawab untuk melakuakan pemalsuan transaksi atau mengubah data. Dengan kombinasi hash funcation dan PoW, sistem digital dapat menjamin keamanan, keabshan transaksi, serta kepercayaan antar pengguna dalam lingkungan terdistribusi.

---
## 3. Alat dan Bahan
- Python 3.11 
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---
## 4. Langkah Percobaan
1. Membuat file tinychain.py di folder praktikum/week13-tinychain/src/.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah python tinychain.py.
4. Mengerjakan laporan.md
5. Membuat file hasil.png di folder praktikum/week13-tinychain/sreenshoots/

---
## 5. Source Code
Langkah 1 & 2 - membuat block chain

```import hashlib
import time

# =========================
# Class Block
# =========================
class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.timestamp = timestamp or time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = (
            str(self.index)
            + str(self.timestamp)
            + str(self.data)
            + str(self.previous_hash)
            + str(self.nonce)
        )
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"✅ Block mined: {self.hash}")


# =========================
# Class Blockchain
# =========================
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)


# =========================
# Uji coba blockchain
# =========================
my_chain = Blockchain()

print("⛏️ Mining block 1...")
my_chain.add_block(Block(1, "", "Transaksi A → B: 10 Coin"))

print("⛏️ Mining block 2...")
my_chain.add_block(Block(2, "", "Transaksi B → C: 5 Coin"))

print("\n📦 Isi Blockchain:")
for block in my_chain.chain:
    print("----------------------------")
    print("Index :", block.index)
    print("Data  :", block.data)
    print("Hash  :", block.hash)
    print("Prev  :", block.previous_hash)

```
Hasilnya :
```
⛏️ Mining block 1...
✅ Block mined: 00003645d5e4f98e99de9010a4ba19a80c302141361a53a3a136d7b811a37b6b
⛏️ Mining block 2...
✅ Block mined: 0000afa62e9bbc98ce1dc959572485fedbab41206d1d7762012b929f5f63d97d

📦 Isi Blockchain:
----------------------------
Index : 0
Data  : Genesis Block
Hash  : a1995739a07a48a5a38d4677b460ce4f2b48ab9fe40954b268222f84ccc1a3d1
Prev  : 0
2012b929f5f63d97d
Prev  : 00003645d5e4f98e99de9010a4ba19a80c302141361a53a3a136d7b811a37b6b
```
Langkah 3 - Analisis Proof of Work (PoW)
pada program ini, proses PoW dilakukan melalui fungsi mine_block(), dimana sistem mencari nilai hash yang emmenuhi syarat tingkat kesulitan (difficulty), yaitu diawali dengan sejumlah angka nol, proses ini dilakukan dengan cara mengubah nilai nonce secara terus menerus serta menghitung ulang hash menggunakan algoritma SHA-256 hingga ditemukan hast yang sesuai. Setiap percobaan menghasilkan nilai hash yang berbeda, sehingga diperlukan banyak iterasi sebelum memperoleh hasil yang valis. Semakin besar nilai difficlty, semakin banyak kombinasi nonce yang has=rus dicoba, sehingga waktu komputasi menjadi lebih lama. proses ini menunjukan bahwa penbuatan satu blok membutuhkan usaha nyata (work) dari komputer.

---
## 6. Hasil dan Pembahasan
Hasil eksekusi program tinychain:
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/fd35a057-9c72-42ec-b7d3-a276df7374dd" />

Berdasarkan hasil eksekusi program yang telah dilakukan, terlihat bahwa proses mining telah berhasi menghasilkan hash yang diawali dengan empat angka nol, sesuai dengan nilai difficulty yang diterapkan. proses ini membutuhkan percobaan berulangkali dengan menaikan nilai nonce hingga diperoleh hash yang memenuhi kriteria tersebut. Waktu yang dibutuhkan untuk menemukan hash yang valid bergantung pada tingkat difficulty yang digunakan.

Namun pada awal pembuatan program, sempat terjadi error yang menyebabkan kode tidak bisa dijalankan. Error terjadi karena kesalahan penulisan kode deklarasi untuk kelas Blockchain yang berada pada baris yang sama dengan perintah print(). Setelah error berhasil diatasi, program dapat berjalan kembali tanpa kendala.

---
## 7. Jawaban Pertanyaan
- Pertanyaan 1: Mengapa fungsi hash sangat penting dalam blockchain?
- Pertanyaan 2: Bagaimana Proof of Work mencegah double spending?
- Pertanyaan 3: Apa kelemahan dari PoW dalam hal efisiensi energi?
Jawab :
1. Karene berfungsi untuk menjaga integritas dan keamanan data. Setiap blok memiliki hash unik yang dihasilkan dari isis blok tersebut. Jika data dalam blok diubah sedikit saja, maka nilai hash akan berubah secara signifikan, sehingga manipulasi dapat terdeteksi dengan menudah. Selain itu, hash juga menghubungkan satu blok dengan blok sebelumnya melalui previous hash, sehingga membentuk rantai yang aman dan sulit dipalsukan.
2. memastikan bahwa setiap transaksi harus diverifikasi dan dimasukan ke dalam blok yang telah melalui proses mining. proses mining membutuhkan waktu dan daya konputasi yang besar, sehingga tidak memungkinkan satu pihak memalsukan transaksi secara cepat untuk membelanjakan aset sama dua kali. Setelah transaksi tercatat di blockchain serta dikonfirmasi oleh jaringan, data tersebut sulit siubah karena memerlukan pengulangan proses mining pada seluruh bloh berikutnya.
3. Kelemahan utama Proof of work yaitu tingginya konsumsi energi karena proses mining memerlukan perhitungan hash secara terus-menerus oleh banyak komputer. Semakin tinggi tingkat kesulitan jaringan , semakin besar pula daya listrik dan perangkat keras yang dibutuhkan. Hal ini menyebabkan biaya operasional yang tinggi serta berdampak pada tingkat lingkungan, sehingga PoW dinilai kurang efisien dibandingkan metode konsensus lain yang lebih hemat energi.
   
---
## 8. Kesimpulan
Berdasarkan percobaan, fungsi hash dan mekanisme Proof of Work terbukti mampu menjaga integritas data dan keamanan blockchain melalui proses mining yang membutuhkan perhitungan komputasi. Semakin tinggi tingkat *difficulty*, semakin lama waktu yang diperlukan untuk menemukan hash yang valid. Hal ini menunjukkan bahwa blockchain sulit dimanipulasi karena setiap perubahan data memerlukan usaha komputasi yang besar.

---
## 10. Commit Log
```
commit week13-tinychain
Author: Resty Chonifatul Jannah <rstynad.gmail.com>
Date:   2026-01-26

   week13-tinychain: TinyChain – Proof of Work (PoW)
```
