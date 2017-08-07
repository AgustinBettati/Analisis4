from decimal import Decimal

lista = [1, 4, 3]

lista.append(5)

for x in lista:
    print(x)


def biggestNumber():
    a = input("Enter a number:")
    b = input("Another: ")
    c = input("Last number: ")
    if a > b:
        if a > c:
            return a
        return c

    elif b > c:
        return b
    return c


def isPrimeNumber():
    number = int(input("Verify if your number is prime: "))
    for x in range(2, number):
        if number % x == 0:
            return False
    return True

print(isPrimeNumber())