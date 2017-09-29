import math

def newton_raphson(x, f, derivativef, cota, max, iteration):
    newX = x - (f(x)/derivativef(x))
    if iteration == max or abs(x-newX) < cota:
        return newX

    return newton_raphson(newX, f, derivativef, cota, max, (iteration + 1))



def normal_function(x):
    return math.pow(x,2) -3

def derivative_function(x):
    return 2*x


print(newton_raphson(2, normal_function, derivative_function, 0.00001, 100, 0))
