from math import pi, log10

def bisection(f, x0, x1, err):
    if x1 < x0:
        raise Exception('The Input points x0 and x1 should be such that x0 < x1')
    if f(x0)*f(x1)>0:
        raise Exception('No roots exist between %.5f and %.5f' % (x0, x1))
    
    iters = 0

    accuracy = int(log10(int(10/err)))

    if abs(round(f(x0),accuracy)) == 0:
        return x0, iters
    if abs(round(f(x1),accuracy)) == 0:
        return x1, iters

    xold = x0

    while True:
        iters+=1
        xnew = (x0 + x1)/2
        if abs(round(f(xnew),accuracy)) == 0:
            return round(xnew,accuracy), iters
        if round(abs((xnew-xold)/xold) - err , accuracy) == 0:
            return round(xnew, accuracy), iters
        if f(x0)*f(xnew)<0:
            x1 = xnew
        else:
            x0 = xnew
        xold = xnew

def vol_sphere(r):
    return 4*pi*r**3 / 3

r = 1.25
rho = 250
m = vol_sphere(r)*rho
g = 9.8
rho_w = 1000

down_force = g*m

def fun(h):
    return ((vol_sphere(r) - pi*h**2 *(3*r - h)/3 )*rho_w*g - down_force)

for i in range(0,100):
    low, up = i*2.5/100, (i+1)*2.5/100
    if fun(low)*fun(up) < 0:
        break

root, iters = bisection(fun,low,up,0.1/100)
print(root, ' converged after ', iters, ' iterations')