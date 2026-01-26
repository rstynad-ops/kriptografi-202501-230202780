import hashlib

# Password asli (simulasi korban)
password_asli = "password"

# Hash MD5 dari password
target_hash = hashlib.md5(password_asli.encode()).hexdigest()

print("Hash yang bocor:", target_hash)
print("-" * 40)

# Baca dictionary dan tebak password
with open("dictionary.txt", "r") as file:
    for kata in file:
        kata = kata.strip()
        hash_kata = hashlib.md5(kata.encode()).hexdigest()
        print("Mencoba:", kata)

        if hash_kata == target_hash:
            print("\n✅ Password ditemukan:", kata)
            break
