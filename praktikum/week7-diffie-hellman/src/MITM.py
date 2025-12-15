import random

# parameter publik
p = 23  # bilangan prima
g = 5   # generator

# private key Alice, Bob, dan Eve
a = random.randint(1, p-1)  # secret Alice
b = random.randint(1, p-1)  # secret Bob
e = random.randint(1, p-1)  # secret Eve

# public key asli
A = pow(g, a, p)  # public Alice
B = pow(g, b, p)  # public Bob

# public key Eve
E = pow(g, e, p)

# =========================
# SERANGAN MITM OLEH EVE
# =========================
# Eve mencegat dan mengganti public key
# - Alice menerima public key Eve (bukan Bob)
# - Bob menerima public key Eve (bukan Alice)

# Alice menghitung kunci bersama (dengan Eve)
shared_Alice = pow(E, a, p)

# Bob menghitung kunci bersama (dengan Eve)
shared_Bob = pow(E, b, p)

# Eve menghitung kedua kunci
shared_Eve_with_Alice = pow(A, e, p)
shared_Eve_with_Bob   = pow(B, e, p)

# =========================
# OUTPUT
# =========================
print("Kunci Alice (mengira dengan Bob) :", shared_Alice)
print("Kunci Bob   (mengira dengan Alice):", shared_Bob)

print("\nKunci Eve dengan Alice :", shared_Eve_with_Alice)
print("Kunci Eve dengan Bob   :", shared_Eve_with_Bob)
