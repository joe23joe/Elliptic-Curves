from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Curve: y^2 = x^3 + 497x + 1768 mod 9739
p = 9739
a = 497
b = 1768

# -------------------------------
# 1. Modular inverse (needed for slope calculation)
# -------------------------------
def inv_mod(x):
    return pow(x, p - 2, p)

# -------------------------------
# 2. ELLIPTIC CURVE POINT ADDITION
# -------------------------------
def add(P, Q):

    # First: we will check if P or Q is point of infinte because if that's true then the addition will do nothing (Identity point)
    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    # second: here we check if the points are inverse to each other (forms perfect vertical line) 
    if x1 == x2 and (y1 + y2) % p == 0:
        return None

    # Third: we check if both points are equal to calculate the slope
    if P == Q:
        # Slope m = (3x₁² + a) / (2y₁)
        m = (3 * x1 * x1 + a) * inv_mod(2 * y1) % p

    else:
        # forth: we check if both points are unequal
        # Slope m = (y₂ - y₁) / (x₂ - x₁)
        m = (y2 - y1) * inv_mod(x2 - x1) % p

    # Equation for resulting point:
    # x₃ = m² - x₁ - x₂
    x3 = (m * m - x1 - x2) % p

    # y₃ = m(x₁ - x₃) - y₁
    y3 = (m * (x1 - x3) - y1) % p

    return (x3, y3)

# -------------------------------
# 3. Scalar multiplication using double-and-add
# -------------------------------
def scalar_mult(k, P):
    result = None      # Starts at identity point O
    current = P        # Current multiple of P

    while k > 0:
        if k & 1:          # If the last bit is 1 → add current
            result = add(result, current)
        current = add(current, current)  # Double each step
        k >>= 1                           # Shift bits
    return result

# ------------------------------
# 1. Recover y-coordinate from x using p ≡ 3 mod 4 trick
# ------------------------------
xQA = 4726
y2 = (xQA**3 + a*xQA + b) % p
# y = ± y2^((p+1)//4) mod p
yQA = pow(y2, (p+1)//4, p)   # take one solution
QA = (xQA, yQA)

# ------------------------------
# 2. Secret nB
# ------------------------------
nB = 6534

# ------------------------------
# 3. Compute shared secret S = [nB] QA
# ------------------------------
S = scalar_mult(nB, QA)
print("Shared secret S =", S)
shared_secret = S[0]

# ------------------------------
# 4. Use x-coordinate of S as key
# ------------------------------
import hashlib
x_str = str(S[0])
key = hashlib.sha1(x_str.encode()).hexdigest()
print("SHA1(x) =", key)

# DECRYPTING

# Ciphertext data
iv = 'cd9da9f1c60925922377ea952afc212c'
ciphertext = 'febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8'

# Decrypt function
def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))

def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)
    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

print(decrypt_flag(shared_secret, iv, ciphertext))
