import math
from decimal import Decimal

# First method, obtained through pythons math library
print(Decimal(math.pi))


# Second method, obtained through Gauss-Legendre algorithm using float primitive type
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



