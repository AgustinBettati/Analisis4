import math
from decimal import Decimal

# First method, obtained through pythons math library
print(Decimal(math.pi))


# Gauss-Legendre algorithm using float primitive type
def pi_gauss_legendre():
    a = 1.0
    b = 1 / math.sqrt(2)
    t = 0.25
    p = 1.0

    while True:
        x = (a + b) / 2.0
        y = math.sqrt(a * b)
        t = t - p * math.pow(a - x, 2)
        a = x
        b = y
        p = 2 * p

        if abs(a - b) < 0.00001:
            return math.pow(a + b, 2) / (4 * t)

print(pi_gauss_legendre())


# Gauss-Legendre using Decimal format.
def decimal_pi_gauss_legendre():
    a = Decimal(1.0)
    b = Decimal(1 / math.sqrt(2))
    t = Decimal(0.25)
    p = Decimal(1.0)

    while True:
        x = Decimal((a + b) / Decimal(2.0))
        y = Decimal(math.sqrt(a * b))
        t = t - p * ((a - x)**Decimal(2))
        a = x
        b = y
        p = 2 * p

        if abs(a - b) < 0.000000000000000000000000001:
            return Decimal( (a + b)**Decimal(2) / Decimal(4 * t))

print(decimal_pi_gauss_legendre())



# Spigot algorithm for n digits.
def pi_spigot(amt_of_digits):
    pi = ""
    k, a, b, a1, b1 = 2, 4, 1, 12, 4
    while amt_of_digits > 0:
        p, q, k = k * k, 2 * k + 1, k + 1
        a, b, a1, b1 = a1, b1, p * a + q * a1, p * b + q * b1
        d, d1 = a / b, a1 / b1
        while d == d1 and amt_of_digits > 0:
            if len(pi) == 1: pi += "."
            pi += str(int(d))
            amt_of_digits -= 1
            a, a1 = 10 * (a % b), 10 * (a1 % b1)
            d, d1 = a / b, a1 / b1

    return pi

print(pi_spigot(100))

