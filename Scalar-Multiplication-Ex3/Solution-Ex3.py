# Elliptic curve: y^2 = x^3 + 497x + 1768 mod 9739

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

def on_curve(point):
    if point is None:  # this means it's infinty point
        return True
    x, y = point
    return (y*y - (x*x*x + a*x + b)) % p == 0


# -------------------------------
# Given point P
# -------------------------------
P = (2339, 2213)

# Compute Q = [7863]P
if __name__ == "__main__":
    Q = scalar_mult(7863, P)
    C = on_curve(Q)
    print(Q)
    print(C)