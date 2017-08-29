import math
def newton_raphson(x,f, derivativef, cota,max, iteratation):
    newX = x - (f(x)/derivativef(x))
    if (iteratation == max or (abs(x-newX) < cota)):
        return newX

    return newton_raphson(newX,f,derivativef,cota, max, (iteratation+1))



def normal_function(x):
    return x - math.pow(math.e,-x)

def derivative_function(x):
    return 1 + math.pow(math.e,-x)


print(newton_raphson(0, normal_function, derivative_function, 0.0003, 10, 0))
