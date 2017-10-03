import numpy as np

def coef(x, y):
    '''x : array of data points
       y : array of f(x)  '''
    x.astype(float)
    y.astype(float)
    n = len(x)
    result = []

    for i in range(n):
        result.append(0)

    for k in range(0, n, 1):
        result[k] = y[k]

        s = 0.0
        for i in range(0,k,1):
            multiplication = 1.0
            for j in range(0, i, 1):
                multiplication *= (x[k] - x[j])

            s += multiplication * result[i]

        result[k] -= s

        for j in range(0,k, 1):
            result /= (x[k] - x[j])

    return np.array(result) # return an array of coefficient

def eval(a, x, r):

     # ''' a : array returned by function coef()
     #    x : array of data points
     #    r : the node to interpolate at  '''

    x.astype(float)
    n = len(a)
    temp = a[0]
    for i in range(1 , n, 1):
        multiplicadora = a[i]
        for j in range(0, i,1):
            multiplicadora *= (r - x[j])

    return temp # return the y_value interpolation

print ( coef(np.arange(10,15,1),np.arange(35,40,1) ) )

# print( eval( coef(np.arange(4,6,1),np.arange(4,6,1)) ,np.arange(4,6,1), 5.5) )