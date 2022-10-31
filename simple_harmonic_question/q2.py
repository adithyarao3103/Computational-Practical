# ___ 

# Solve the equations for a pendulum of length l, mass m,with a wall placed at wall_pos and plot its kinetic energy, potential energy and total energy. Assume that the collision of the pendulum with the wall is completely elastic.

# ---


from math import pi, sin, cos, asin
from numpy import arange

def RK_sec(f,g,y0,z0,x0,x1,h, boundary):
    if y0>boundary and boundary>0:
        raise Exception('Initial pendulum position outside the box')
    if y0<boundary and boundary<0:
        raise Exception('Initial pendulum position outside the box')

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
        if boundary > 0 and y[i] >= boundary:
            z[i] = -z[i]
            
        if boundary < 0 and y[i] <= boundary:
            z[i] = -z[i]

        if boundary == 0 and y[0]< 0 and y[i]>=0:
            z[i] = -z[i]

        if boundary == 0 and y[0]> 0 and y[i]<=0:
            z[i] = -z[i]
        
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
        
    return x, y, z


g_grav = 9.81
l = 1

T = 100
h=0.01
in_angle = pi/4
in_vel = 0
wall_pos = -0.25



def f(t,theta,z):
    return -1*(g_grav*(sin(theta)/l))

def g(x,y,z):
    return z

theta_wall = asin(wall_pos/l)

ts, thetas, theta_dots = RK_sec(f, g, in_angle, in_vel, 0, T, h, theta_wall)

import matplotlib.pyplot as plt

# for i in range(len(ts)):
#     ax = plt.subplot(111, polar=True)
#     ax.plot(thetas[i], 1, marker='o')
#     ax.grid(False)
#     ax.set_theta_offset(-pi/2)
#     plt.pause(0.1)
#     plt.clf()

m = 1

ke = []
pe = []
te = []

for theta_dot in theta_dots:
    ke.append(m*l*l*theta_dot*theta_dot/2)

for theta in thetas:
    pe.append(m*g_grav*(l-l*cos(theta)))

for i in range(len(ke)):
    te.append(ke[i] + pe[i])



fig, axs = plt.subplots(2,constrained_layout = True)

for i in range(len(ts)):
    axs[0].plot(l*sin(thetas[i]),l-l*cos(thetas[i]), marker='o')
    axs[0].set_xlim(-l - 0.25,l + 0.25)
    axs[0].set_ylim(-0.25, 2*l + 0.25)
    axs[0].set_aspect('equal', adjustable='box')
    axs[1].plot(ts[:i], ke[:i], color="blue", label ="KE")
    axs[1].plot(ts[:i], pe[:i], color="red", label ="PE")
    axs[1].plot(ts[:i], te[:i], color='black', label = "TE")
    axs[1].legend(loc="upper left")

    plt.pause(0.001)
    axs[0].cla()
    axs[1].cla()