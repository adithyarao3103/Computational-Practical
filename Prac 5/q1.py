from numpy import arange

def RK_sec(f,g,y0,z0,x0,x1,h):
    x = arange(x0, x1+h, h)
    y = [y0]
    z = [z0]
    k1 = []
    k2 = []
    k3 = []
    k4 = []
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    for i in range(len(x)-1):
        k1.append(f(x[i], y[i], z[i]))
        l1.append(g(x[i], y[i], z[i]))

        k2.append(f(x[i] + h/2, y[i] + l1[i]*h/2, z[i] + k1[i]*h/2))
        l2.append(g(x[i] + h/2, y[i] + l1[i]*h/2, z[i] + k1[i]*h/2))

        k3.append(f(x[i] + h/2, y[i] + l2[i]*h/2, z[i] + k2[i]*h/2))
        l3.append(g(x[i] + h/2, y[i] + l2[i]*h/2, z[i] + k2[i]*h/2))

        k4.append(f(x[i] + h, y[i] + l3[i]*h, z[i] + k3[i]*h))
        l4.append(g(x[i] + h, y[i] + l3[i]*h, z[i] + k3[i]*h))

        z.append(z[i] + h*(k1[i] + 2*k2[i] + 2*k3[i] + k4[i])/6)
        y.append(y[i] + h*(l1[i] + 2*l2[i] + 2*l3[i] + l4[i])/6)
        
    return x, y



def f(x,y,z):
    return -1*(7*y + 0.5*z)

def g(x,y,z):
    return z


xs, ys = RK_sec(f,g,4,0,0,5,0.1)

import matplotlib.pyplot as plt

plt.plot(xs,ys)
plt.show()
