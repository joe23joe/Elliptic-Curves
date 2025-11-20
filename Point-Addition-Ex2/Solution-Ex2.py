# The elliptic curve parameters of: y^2 = x^3 + a*x + b
a = 497
b = 1768
p = 9739

# -------------------------------
# 1. MODULAR INVERSE
# -------------------------------
# Needed because the slope m = (y2 - y1) / (x2 - x1)
# Division mod p = multiply by modular inverse
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

def on_curve(point):
    if point is None:  # this means it's infinty point
        return True
    x, y = point
    return (y*y - (x*x*x + a*x + b)) % p == 0

# -------------------------------
# 3. INPUT POINTS
# -------------------------------
P = (493, 5564)
Q = (1539, 4742)
R = (4403, 5202)

# -------------------------------
# 4. COMPUTE S = P + P + Q + R
# -------------------------------
if __name__ == "__main__":
    S = add(add(add(P, P), Q), R)
    print(S)
    print(on_curve(S))