from math import pi, sin, cos

y0 = -pi/200
t0 = 0
z0 = 0
h = 0.001
k = 100

ys = [y0]
zs = [z0]

for i in range(0, int(100/h)):
    k1 = zs[i]
    l1 = -k*ys[i]

    k2 = zs[i] + l1*h
    l2 = -k*ys[i] + k1*h

    ys.append(ys[i] + (k1 + k2)*h/2)
    zs.append(zs[i] + (l1 + l2)*h/2)

xs = []
yps = []

for y in ys:
    xs.append(sin(y))
    yps.append(1 - cos(y))
    

import matplotlib.pyplot as plt 

for i in range(len(ys)):
    plt.xlim(-0.02, 0.02)
    plt.ylim(0, 0.00014)
    plt.plot(xs[i], yps[i], marker = 'o')
    plt.pause(0.0000001)
    plt.clf()

plt.show()

# plt.plot(xs,yps)
# plt.show()



