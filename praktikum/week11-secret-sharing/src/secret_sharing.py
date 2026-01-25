import random

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
