import math


def analyticSolution(time, initTemp, ambientTemp):
    return ambientTemp + math.exp(-0.25*time)*(initTemp - ambientTemp)


def rk4(f, x0, y0, xf, n):
    vx = [0] * (n + 1)
    vy = [0] * (n + 1)
    h = (xf - x0) / float(n)
    vx[0] = x = x0
    vy[0] = y = y0
    for i in range(1, n + 1):
        ambientTemp = 50
        k1 = h * f(x, y, ambientTemp)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1, ambientTemp)
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2, ambientTemp)
        k4 = h * f(x + h, y + k3, ambientTemp)
        vx[i] = x = x0 + i * h
        vy[i] = y = y + (k1 + k2 + k2 + k3 + k3 + k4) / 6
    return vx, vy


def f(time, temp, ambientTemp):
    return -0.25*(temp - ambientTemp)



vx, vy = rk4(f, 0, 80, 10, 100)
for x, y in list(zip(vx, vy)):
    print("%4.1f %10.5f %+12.4e" % (x, y, y - (4 + x * x) ** 2 / 16))

print(analyticSolution(10, 80, 50))

