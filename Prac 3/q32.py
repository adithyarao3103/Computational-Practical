# integral x^3 - 3yz, x=(-2,2), y=(0,1), z=(-3,1)
# I1 = integral -3 to 1 x^3
# I2 = integral -2 to 2 z
# I3 = integral 0 to 1 y
# I = I1 - 3*I2*I3

# The code isnt working so dont prefer this one

from numpy import arange

def simpsons(y, limits):
    sum  = y[0] + y[-1]
    for i in range(1,len(y)-1):
        if i%2 == 0:
            sum+= 2*y[i]
        else:
            sum+= 4*y[i]

    integral = (limits[1]-limits[0])*sum/(3*len(y))
    return(integral)

def fun1(x):
    return x**3

def fun2(z):
    return z

def fun3(y):
    return y



lim1 = [-3,1]
points1 = [-3, (-3+1)/2, 1]
x3 = []
for point in points1:
    x3.append(fun1(point))

lim2 = [-2,2]
points2 = [-2,0,2]
z = []
for point in points2:
    z.append(fun2(point))

lim3 = [0,1]
points3 = [0,0.5,1]
y = []
for point in points3:
    y.append(fun3(point))

I1 = simpsons(x3, lim1)
I2 = simpsons(z, lim2)
I3 = simpsons(y, lim3)

I = I1 - 3*I2*I3

print(f'The triple integral from Simpsons method is {I}')