import math


def analyticSolution(time, initTemp, ambientTemp):
    return ambientTemp + math.exp(-0.25 * time) * (initTemp - ambientTemp)


def rk4(x0, y0, ambientTemp, xf, n):
    def f(temp):
        return -0.25 * (temp - ambientTemp)

    vx = [0] * (n + 1)
    vy = [0] * (n + 1)
    h = (xf - x0) / float(n)
    vx[0] = x0
    vy[0] = y = y0
    for i in range(1, n + 1):
        k1 = h * f(y)
        k2 = h * f(y + 0.5 * k1)
        k3 = h * f(y + 0.5 * k2)
        k4 = h * f(y + k3)
        vx[i] = x0 + i * h
        vy[i] = y = y + (k1 + k2 + k2 + k3 + k3 + k4) / 6
    return vy[n]
