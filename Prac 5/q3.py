# ---

# V = pi H^2 (3R - H)/3

# Q = dV/dt = pi/3 ( 2H (3R - H) - H^2 ) dH/dt = CA (2 g H)^1/2

# dH/dt = 3 C A (2 g H)^1/2 / pi (2H (3R - H) - H^2)

# ---

import matplotlib.pyplot as plt
from math import pi

def RK_first(f,y0,x0,h):
    x = [x0]
    y = [y0]
    k1 = []
    k2 = []
    k3 = []
    k4 = []
    i=0
    while True:
        if y[i] <= 0:
            return x[i], x, y

        k1.append(f(x[i], y[i]))

        k2.append(f(x[i] + h/2, y[i] + k1[i]*h/2))

        k3.append(f(x[i] + h/2, y[i] + k2[i]*h/2))

        k4.append(f(x[i] + h, y[i] + k3[i]*h))

        x.append(x[i] + h)
        y.append(y[i] + h*(k1[i] + 2*k2[i] + 2*k3[i] + k4[i])/6)

        i+=1
        

def f(t,H):
    C = 0.55
    A = pi*(3/200)**2
    g = 9.81
    R = 3
    return -3*C*A*(2*g*abs(H))**(0.5)/(pi* (2*H*(3*R - H) - H**2))


end, t, H = RK_first(f, 2.75, 0, 1)

print(end)


plt.plot(t,H)
plt.show()
