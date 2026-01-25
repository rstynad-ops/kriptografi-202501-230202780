# Laporan Praktikum Kriptografi
Minggu ke-: 11 Topik: Secret Sharing  Nama:Resty Chonifatul jannah  NIM: 230202780  Kelas: 5 Ikrb  

---
## 1. Tujuan
1. Menjelaskan konsep Shamir Secret Sharing (SSS).
2. Melakukan simulasi pembagian rahasia ke beberapa pihak menggunakan skema SSS.
3. Menganalisis keamanan skema distribusi rahasia.

---
## 2. Dasar Teori
Shamir secret sharing (SSS) merupakan sebuah skema kriptografi yang diperkenalkan oleh Adi Shamir pada tahun 1979 untuk membagi sebuah rahasia (secret) menjadi beberapa bagian (sheres), sehingga rahasia hanya dapat direkontruksi jika minimal k atau bagian digabungkan, kurang dari k bagian tidak memberikan informasi apapun tentang rahasia.

Shamir secret shering bekerja berdasarkan prinsip interpolasi polinominal pada bidang hingga, yakni sebuah polinomial berderajat K - 1 dapat ditenteukan secara unik minimal K titik. Pada proses pembangkitan share, sebuah rahasia S ditempatkan sebagai konstanta dalam polinomial acak 
<img width="426" height="29" alt="image" src="https://github.com/user-attachments/assets/13dc1312-4a1f-4719-912e-43cf6b315a63" /> dimana koefisien lainya dipilih secara acak untuk menjaga keamanan. Selanjutnya, polinomial tersebut dievaluasi pada n nilai x yang berbeda untuk menghasilkan pasangan (xi​,f(xi​)) sebagai share yang kemudian dibagikan ke masing-masing pihak.sehingga rahasia hanya dapat direkontruksikan kembali apabila minimal k share digabungkan.

---
## 3. Alat dan Bahan
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- google chrome

---
## 4. Langkah Percobaan
1. Membuat file `secret_shering.py` di folder `praktikum/week11-secret shering/src/`.
2. Menyalin serta memodif kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python secret_shering.py`.
4. Membuat file` ` simulasi-manual.py pada folder praktikum/week11-secret-shering/src/.
5. Membuat folder Screenshots di folder praktikum/week11-secret-shering/src/.

---
## 5. Source Code
Langkah 1 - Implementasi shamir secret sharing
```import random

# ================================
# Konversi string <-> integer
# ================================
def string_to_int(text):
    return int.from_bytes(text.encode(), 'big')

def int_to_string(number):
    return number.to_bytes((number.bit_length() + 7) // 8, 'big').decode()

# ================================
# Bilangan prima besar
# ================================
PRIME = 2**521 - 1   # prime Mersenne (aman untuk text panjang)

# ================================
# Fungsi matematika
# ================================
def mod_inverse(a, p):
    return pow(a, -1, p)

def eval_polynomial(coeffs, x, p):
    result = 0
    for power, coef in enumerate(coeffs):
        result = (result + coef * pow(x, power, p)) % p
    return result

# ================================
# Split secret
# ================================
def split_secret(secret_text, k, n):
    secret_int = string_to_int(secret_text)

    if secret_int >= PRIME:
        raise ValueError("Secret terlalu besar untuk prime!")

    coeffs = [secret_int] + [random.randrange(1, PRIME) for _ in range(k - 1)]

    shares = []
    for x in range(1, n + 1):
        y = eval_polynomial(coeffs, x, PRIME)
        shares.append((x, y))

    return shares

# ================================
# Recover secret
# ================================
def recover_secret(shares):
    secret = 0

    for j, (xj, yj) in enumerate(shares):
        numerator = 1
        denominator = 1

        for m, (xm, _) in enumerate(shares):
            if m != j:
                numerator = (numerator * (-xm)) % PRIME
                denominator = (denominator * (xj - xm)) % PRIME

        lagrange = numerator * mod_inverse(denominator, PRIME)
        secret = (secret + yj * lagrange) % PRIME

    return int_to_string(secret)

# ================================
# MAIN PROGRAM
# ================================
if __name__ == "__main__":

    # Rahasia
    secret = "KriptografiUPB2025"

    # threshold dan jumlah share
    k = 3
    n = 5

    # Split
    shares = split_secret(secret, k, n)
    print("Shares:")
    for s in shares:
        print(s)

    # Recover dari 3 share pertama
    recovered = recover_secret(shares[:k])
    print("\nRecovered secret:", recovered)
```
Hasilnya :
```
Shares:
(1, 5938840902010934437079642070197563142370343085035538676431259023555433408502154596946454985755811523358595663950239968895105759390804902370333743074734052217)
(2, 728172919167650271862128911371161033761503851495249948379161674152775521359716343568949416606515481940174517269569874489259769228087801391538636994994503066)
(3, 4962389031861976649293162920764973325981788199809050044027098329348655888765653396235162214536475540676625494132438863247615542907909323658651916158970949781)
(4, 4911893919832694139408942500216213584492325529690328144586142070771988143924653650699974098222782589613355971755885219095929104430836181546525523984433278060)
(5, 576687583079802742209467649724881809293115841139084250056292898422772286836717106963385067665436628750365950139908942034200453796868375055159460471381487903)

Recovered secret: KriptografiUPB2025
```
Langkah 2 - Simulasi Manual (Tanpa Library)
```import random

# 1. Pilih bilangan prima p
P = 2089

# ----------------------------
# Fungsi bantu
# ----------------------------
def mod_inverse(a, p):
    return pow(a, -1, p)

def f(x, coeffs):
    """Hitung f(x) = a0 + a1*x + ... mod p"""
    result = 0
    for i, a in enumerate(coeffs):
        result = (result + a * (x ** i)) % P
    return result

# ----------------------------
# 2. Bangun polinomial
# ----------------------------
secret = 123
k = 3   # threshold
n = 5   # jumlah share

# a0 = secret, sisanya random
coeffs = [secret] + [random.randint(1, P-1) for _ in range(k-1)]

print("Koefisien polinomial:", coeffs)

# ----------------------------
# 3. Generate shares
# ----------------------------
shares = []
for x in range(1, n+1):
    y = f(x, coeffs)
    shares.append((x, y))

print("\nShares:")
for s in shares:
    print(s)

# ----------------------------
# 4. Rekonstruksi secret (Lagrange)
# ----------------------------
def recover_secret(selected_shares):
    secret = 0
    for j, (xj, yj) in enumerate(selected_shares):
        num = 1
        den = 1
        for m, (xm, _) in enumerate(selected_shares):
            if m != j:
                num = (num * (-xm)) % P
                den = (den * (xj - xm)) % P

        lj = num * mod_inverse(den, P)
        secret = (secret + yj * lj) % P

    return secret

selected = shares[:k]
print("\nShare yang dipakai:", selected)

recovered = recover_secret(selected)
print("Secret hasil rekonstruksi:", recovered)
```
Hasilnya:
```
Shares:
(1, 1395)
(2, 696)
(3, 115)
(4, 1741)
(5, 1396)

Share yang dipakai: [(1, 1395), (2, 696), (3, 115)]
Secret hasil rekonstruksi: 123
```
---
## 6. Hasil dan Pembahasan
Hasil eksekusi daari program secret_sharing.py:
<img width="1913" height="1020" alt="image" src="https://github.com/user-attachments/assets/b8aaef7f-cd37-49e3-8a11-15c0582c1c40" />
Pembahasan : Pada implementasi ini, secret dibentuk sebagai konstanta polinomial dan di kombinasikan dengan koefisien acak dalam operasi modulo bilangan prima. Setiap share merupakan pasangan nilai (x,f(x)) yang tidak mengungkapkan informasi rahasia secara langsung. Rekonstruksi secret dilakukan menggunakan interpolasi lagrange dengan minimal jumlah share sesuai threshold, sehingga nilai konstanta polinomial dapat dikembalikan secara tepat. Hasil pengujian menunjukan bahwa secret berhasil terkontruksi dengan benar ketike jumlah share mencukupi, dan tidak dapat diperoleh jika share kurang dari threshold.

Hasil eksekusi dari program shamir_manual.py:
<img width="1919" height="1019" alt="image" src="https://github.com/user-attachments/assets/1a18595a-a53e-4ccd-9ab9-21ae0ce027b9" /> 
Pembahasan : Pada program ini mengimplementasikan algoritma shamir secret sharing secara manual mengunakan polinomial modulo bilangan prima. Secret dijadikan sebagai konstanta polinomial, sedangkan koefisien lainnya dipilih secara acak untuk menjaga kerahassiaan data. Program menghasilakan beberapa share dalam bentuk pasangan (x,f(x)), dimana setiap share tidak dapat mengungkapkan secret secara mandiri. Proses rekontruksi dilakukan menggunakan metode intrpolasi lagrange dangan jumlah share minimal sesuai nilai threshold. Dimana hasil pengujian menunjukan bahwa secret dapat dikembalikan secara tepat ketika jumlah share mencukupi, sehingga membuktikan bahwa algoritma berjalan sesuai konsep matematis yang digunakan.

---
## 7. Jawaban Pertanyaan
- Pertanyaan 1:Apa keuntungan utama Shamir Secret Sharing dibanding membagikan salinan kunci secara langsung?
- Pertanyaan 2: Apa peran threshold (k) dalam keamanan secret sharing?
- Pertanyaan 3: Berikan satu contoh skenario nyata di mana SSS sangat bermanfaat.
Jawab:
1. Keuntungan utama dari Shamir secret sharing dibandingkan  membandingkan salinan kunci secara langsung yaitu tidak adanya single point of failure, karena kunci tidak pernah disimpan ataupun dibagikan secara utuh kepada sebelah pihak. Setiap share secara individual tidak memberikan informasi (sangat menjaga rahasia), sehingga jika satu atau beberapa pihak bocor atau disusupi, kunci akan tetap aman selama jumlah share yang bocor belum mencapai ambang batas.
2. Threshold(k) berperan sebagai batas minimum keamanan, yang mana jumlah shere yang harus digabungkan untuk merekontruksi rahasia. Nilai K menetukan keseimbangan antara keamanan da ketersediaan : semakin besar nilai K, semakin tinggi tingkat kamanannya karena lebih banyak pihak yang harus bekerja sama, namun jika terlalu besar dapat mengurangi keandalan sistem ketika beberapa share tidak tersedia.
3. Salah satu skenario dari penggunaan Shamir Secret Shering yaitu pada penyimpanan kunci dompet cryptocurerency (cold wallet), dimana kunnci privat dibagi ke beberapa pihak ataupun lokasi yang berbeda, serta hanya bisa digunakan ketika sejumlah pemegang share yang telah ditentukan bekerja sama, sehingga mengunrangi resiko pencurian, kehilangan,maupun penyalahgunaan kunci oleh satu pihak saja.
---
## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---
## 10. Commit Log
```

Author: Resty Chonifatul Jannah <rstynad@gmail.com>
Date:   2026-01-14

    week11-secret-sharing: Secret Shering (Shamir's Secret Shering )
```
