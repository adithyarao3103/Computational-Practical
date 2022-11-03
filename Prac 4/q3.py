from sympy import symbols, lambdify
from numpy import arange

def simpsons(y, limits):
    sum  = y[0] + y[-1]
    for i, ys in enumerate(y[1:-1]):
        if i%2 == 0:
            sum+= 2*ys
        else:
            sum+= 4*ys

    integral = (limits[1]-limits[0])*sum/(3*len(y))
    return(integral)

x, y, z = symbols('x y z')

fun = x**3 - 3*y*z

h = 0.01

lim1 = [-3,1]
points1 = arange(lim1[0], lim1[1]+h, h)

lim2 = [0,2]
points2 = arange(lim2[0], lim2[1]+h, h)

lim3 = [-2,2]
points3 = arange(lim3[0], lim3[1]+h, h)

int1 = lambdify(x, fun)
f1 = list(map(int1, points1))

int2 = lambdify(y, simpsons(f1, lim1))
f2 = list(map(int2, points2))

int3 = lambdify(z, simpsons(f2, lim2))
f3 = list(map(int3, points3))

int_fin = simpsons(f3, lim3)

print(int_fin)




