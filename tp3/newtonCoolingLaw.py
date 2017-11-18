import math


def analyticSolution(time, initTemp, ambientTemp):
    return ambientTemp + math.exp(-0.25*time)*(initTemp - ambientTemp)


# Toma la una f(tiempo, temp, ambientTemp) .. x0 y y0 son el tiempo y
# temperatura previa, xf es el instante t a calcular, y ambientTemp
def rk4(x0, y0, ambientTemp, xf, n):

    def f(time, temp):
        return -0.25 * (temp - ambientTemp)

    vx = [0] * (n + 1)
    vy = [0] * (n + 1)
    h = (xf - x0) / float(n)
    vx[0] = x = x0
    vy[0] = y = y0
    for i in range(1, n + 1):
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x + h, y + k3)
        vx[i] = x = x0 + i * h
        vy[i] = y = y + (k1 + k2 + k2 + k3 + k3 + k4) / 6
    return vy[n]





# t1 = rk4(0, 80, 50, 10, 10)
# print(t1)
# anat1 = analyticSolution(10, 80, 50)
# print(anat1)
#
# t2 = rk4(0, t1, 60, 10, 10)
# print(t2)
# anat2 = analyticSolution(10, anat1, 60)
# print(anat2)

