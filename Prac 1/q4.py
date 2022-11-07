def newton_raphson(f, df, x, n_iter):
    ers = []
    xs = [x]
    for _ in range(0, n_iter):
        xs.append(xs[-1] - f(xs[-1])/df(xs[-1]))
        ers.append(100*(xs[-2] - xs[-1])/xs[-2])

    return xs, ers

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

print(f'roots: {root}')
print(f'errors: {errors}')
