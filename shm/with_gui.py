from tkinter import *
from tkinter.ttk import *
from math import pi, cos, sin
import matplotlib.pyplot as plt

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

def pendulum():
    global k
    ys = [float(entry_y.get())]
    vs = [float(entry_v.get())]
    h = float(entry_h.get())
    ts = [0]
    m = 9.8
    x = 9.8
    k = (x/m)**(0.5)
    xlim = 1

    T=float(entry_T.get())

    for i in range(0,int(T/h)):
        rkout = RK(ys[i],ts[i],vs[i],h,yf,vf)
        ys.append(rkout[0])
        vs.append(rkout[1])
        ts.append(ts[i]+h)



    for i in range(len(ys)):
        plt.plot([0,sin(ys[i])],[1,1-cos(ys[i])])
        plt.plot(sin(ys[i]),1-cos(ys[i]), marker='o')
        plt.xlim(-xlim,xlim)
        plt.ylim(-0.25, 2.25)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.pause(0.000000001)
        plt.clf()

def energy():
    global k
    ys = [float(entry_y.get())]
    vs = [float(entry_v.get())]
    h = float(entry_h.get())
    ts = [0]
    m = 9.8
    x = 9.8
    k = (x/m)**(0.5)
    
    pes = [x*ys[0]**2/2]
    kes = [m*vs[0]**2/2]

    es = [pes[0]+kes[0]]

    T=float(entry_T.get())

    for i in range(0,int(T/h)):
        rkout = RK(ys[i],ts[i],vs[i],h,yf,vf)
        ys.append(rkout[0])
        vs.append(rkout[1])
        ts.append(ts[i]+h)
        
        pes.append(x*ys[i+1]**2/2)
        kes.append(m*vs[i+1]**2/2)
        es.append(pes[i+1]+kes[i+1])

    plt.plot(ts, es)
    plt.plot(ts,kes)
    plt.plot(ts,pes)

    plt.show()




window = Tk()
info = Label(text = "Input Initial values")
info.pack()
label_h = Label(text = "Step Size:")
label_h.pack()
entry_h = Entry(width=50)
entry_h.pack()

label_y = Label(text = "Initial Position:")
label_y.pack()
entry_y = Entry(width=50)
entry_y.pack()

label_v = Label(text = "Initial velocity:")
label_v.pack()
entry_v = Entry(width=50)
entry_v.pack()

label_T = Label(text = "How long should it run:")
label_T.pack()
entry_T = Entry(width=50)
entry_T.pack()

Button(text = 'Plot Pendulum', command=pendulum).pack()
Button(text = 'Plot Energy', command=energy).pack()


window.mainloop()

