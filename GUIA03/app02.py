import math

def func_e(x, n):
    e_aprox = 0
    for i in range(n):
        e_aprox +=  + x**i/math.factorial(i)
    return e_aprox

out = func_e(2,10)
print(out)