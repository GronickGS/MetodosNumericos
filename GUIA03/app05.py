import math

def func_cos(x, n):
    cos_aprox = 0
    for i in range(n):
        coef = (-1)**i
        num = x**(2*i)
        denom = math.factorial(2**i)
        cos_aprox += (coef) * (num/denom)
    return cos_aprox

angulo_rad = (math.radians(45))
out = func_cos(angulo_rad, 5)
print(out)