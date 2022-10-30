from math import pi, sin, cos

y0 = -pi/100
t0 = 0
z0 = 0
h = 0.01
k = 0.01

ys = [y0]
zs = [z0]

for i in range(0, int(10/h)):
    k1 = zs[i]
    l1 = -k*ys[i]

    k2 = zs[i] + l1*h/2
    l2 = -k*ys[i] + k1*h/2

    k3 = zs[i] + l2*h/2
    l3 = ys[i] + k2*h/2

    k4 = zs[i] + l3*h   
    l4 = ys[i] + k3*h

    ys.append(ys[i] + (k1 + 2*k2 + 2*k3 + k4)*h/6)
    zs.append(zs[i] + (l1 + 2*l2 + 2*l3 + l4)*h/6)

xs = []
yps = []

for y in ys:
    xs.append(sin(y))
    yps.append(1 - cos(y))

import matplotlib.pyplot as plt 
from time import sleep
from matplotlib.animation import FuncAnimation 

fig = plt.figure() 

axis = plt.axes(xlim =(0, 4), ylim =(-2, 2))

def init(): 
    line.set_data([], [])
    return line,

line, = axis.plot([], [], lw = 3) 
def animate(i):
    line.set_data(xs, yps)
      
    return line,

anim = FuncAnimation(fig, animate, init_func = init, frames = 200, interval = 20, blit = True)

anim.save('basic_animation.mpeg', fps=30)




