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

def f1(t,x,z):
    c = 5
    m = 20
    k = 20
    return -1*(k*x + c*z/m)

def f2(t,x,z):
    c = 40
    m = 20
    k = 20
    return -1*(k*x + c*z/m)

def f3(t,x,z):
    c = 200
    m = 20
    k = 20
    return -1*(k*x + c*z/m)

def g(t,x,z):
    return z

import matplotlib.pyplot as plt


ts, x1s = RK_sec(f1,g,1,0,0,15,0.01)
x2s = RK_sec(f2,g,1,0,0,15,0.01)[-1]
x3s = RK_sec(f3,g,1,0,0,15,0.01)[-1]


fig, axs = plt.subplots(3,constrained_layout = True)


axs[0].plot(ts, x1s)
axs[0].set_title("c = 5")
axs[1].plot(ts, x2s)
axs[1].set_title("c = 40")
axs[2].plot(ts, x3s)
axs[2].set_title("c = 200")


plt.show()
