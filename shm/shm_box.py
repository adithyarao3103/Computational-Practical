def RK(yi,ti,vi,h,yf,vf):
    k1 = yf(ti,yi, vi)
    l1 = vf(ti, yi, vi)

    k2 = yf(ti+h, yi + k1*h, vi+l1*h)
    l2 = vf(ti+h, yi + k1*h, vi+l1*h)

    return([yi + (k1+k2)*h/2, vi + (l1+l2)*h/2])

def yf(t,y,v):
    return v

def vf(t,y,v):
    return -k*y

#Initial values

from math import pi, cos, sin

box_angle = pi/100

ys = [-pi/6]
vs = [0]
ts = [0]
h = 0.1
m = 9.8
x = 9.8
k = (x/m)**(0.5)

xlim = abs(sin(ys[0])*1.5)

pes = [x*ys[0]**2/2]
kes = [m*vs[0]**2/2]
es = [pes[0]+kes[0]]

T = 100

for i in range(0,int(T/h)):
    if ys[i]>=box_angle:
        vs.append(-vs.pop())
        
    rkout = RK(ys[i],ts[i],vs[i],h,yf,vf)
    ys.append(rkout[0])
    vs.append(rkout[1])
    ts.append(ts[i]+h)

    pes.append(x*ys[i+1]**2/2)
    kes.append(m*vs[i+1]**2/2)
    es.append(pes[i+1]+kes[i+1])

import matplotlib.pyplot as plt

for i in range(len(ys)):
    plt.plot([0,sin(ys[i])],[1,1-cos(ys[i])])
    plt.plot(sin(ys[i]),1-cos(ys[i]), marker='o')
    plt.xlim(-xlim,xlim)
    plt.ylim(-0.25, 1.25)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.pause(0.000000001)
    plt.clf()

    #print(  (sin(ys[i])**2 + cos(ys[i])**2)**(0.5) )
    
    
#plt.plot(ts, es)
#plt.plot(ts,kes)
#plt.plot(ts,pes)

plt.show()


