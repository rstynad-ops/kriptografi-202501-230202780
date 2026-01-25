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

# Prime besar (harus > secret)
PRIME = 208351617316091241234326746312124448251235562226470491514186331217050270460481

# -----------------------------
# Fungsi matematika dasar
# -----------------------------
def mod_inverse(a, p):
    return pow(a, -1, p)

def eval_polynomial(coeffs, x, p):
    result = 0
    for power, coef in enumerate(coeffs):
        result = (result + coef * pow(x, power, p)) % p
    return result

# -----------------------------
# Membuat shares
# -----------------------------
def split_secret(secret, n, k):
    """
    secret : angka rahasia
    n      : jumlah share
    k      : threshold minimal untuk recovery
    """
    coeffs = [secret] + [random.randrange(1, PRIME) for _ in range(k - 1)]

    shares = []
    for x in range(1, n + 1):
        y = eval_polynomial(coeffs, x, PRIME)
        shares.append((x, y))
    return shares

# -----------------------------
# Recover secret
# -----------------------------
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
        secret = (PRIME + secret + (yj * lagrange)) % PRIME
    return secret

# -----------------------------
# CONTOH PEMAKAIAN
# -----------------------------
if __name__ == "__main__":
    secret = 123456789
    n = 5   # jumlah share
    k = 3   # minimal share untuk recover

    print("Secret asli:", secret)

    shares = split_secret(secret, n, k)

    print("\nShares:")
    for s in shares:
        print(s)

    print("\nAmbil 3 shares pertama untuk recover:")
    recovered = recover_secret(shares[:k])
    print("Secret hasil recovery:", recovered)

```
Hasilnya :
```
Langkah2_Simulasi Manual (Tanpa Library)
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
