def simpsons(y, limits):
    sum  = y[0] + y[-1]
    for i, ys in enumerate(y[1:-1]):
        if i%2 == 0:
            sum+= 2*ys
        else:
            sum+= 4*ys

    integral = (limits[1]-limits[0])*sum/(3*len(y))
    return(integral)


rho = [4,3.95,3.89,3.8,3.6,3.41,3.3]
Ac = [100,103,106,110,120,133,150]

lim = [0, 10]

y=[rho_val*Ac_val for (rho_val, Ac_val) in zip(rho, Ac)]

print(simpsons(y,lim))

