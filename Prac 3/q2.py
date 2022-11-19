def simpsons(y, limits):
    sum  = y[0] + y[-1]
    for i in range(1,len(y)-1):
        if i%2 == 0:
            sum+= 2*y[i]
        else:
            sum+= 4*y[i]

    integral = (limits[1]-limits[0])*sum/(3*len(y))
    return(integral)

def fun(x):
    return 5 + 0.25*x**2

limits = [0,11]
points = range(limits[0], limits[1] + 1)

ys = []

for point in points:
    ys.append(fun(point))

print(simpsons(ys, limits))

