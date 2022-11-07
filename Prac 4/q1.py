def simpsons(y, limits):
    sum  = y[0] + y[-1]
    for i in range(1,len(y)-1):
        if i%2 == 0:
            sum+= 2*y[i]
        else:
            sum+= 4*y[i]

    integral = (limits[1]-limits[0])*sum/(3*len(y))
    return(integral)


rho = [4,3.95,3.89,3.8,3.6,3.41,3.3]
Ac = [100,103,106,110,120,133,150]

y = []
lim = [0, 10]

for i in range(len(rho)):
    y.append(rho[i]*Ac[i])

print(simpsons(y,lim))
