def newton_raphson(f, df, x, n_iter):
    ers = []
    for i in range(0, n_iter):
        old = x
        x = x  - f(x)/df(x)
        ers.append(100*(old - x)/old)

    return x0, ers

from sympy import *
from math import pi

h = symbols('h')

R = 4
x0 = 2
n_iters = 3

f = pi*h**2 *(3*R - h)/3 - 50

df = f.diff()

f = lambdify(h,f)
df = lambdify(h,df)

root, errors = newton_raphson(f,df,x0,n_iters)

print(root)
print(errors)

