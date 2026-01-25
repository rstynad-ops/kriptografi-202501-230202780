import random

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

