import math

def func_e(x, n):
    e_aprox = 0
    for i in range(n):
        e_aprox +=  + x**i/math.factorial(i)
    return e_aprox

x = 5
for i in range(1,20):
    e_aprox = func_e(x,i)
    e_exp = math.exp(x)
    e_error = abs(e_aprox - e_exp)
    if e_error < 1:
        break
    print(f'{i} terminos: Serie de taylor aproximada = {e_aprox}, exponente calcado = {e_exp}, error: {e_error}')