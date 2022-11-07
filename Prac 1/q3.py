from math import pi, isclose

def bisection(f, x0, x1, err):
    if x1 < x0:
        print('The Input points x0 and x1 should be such that x0 < x1')
        quit()
    if f(x0)*f(x1)>0:
        print(f'No roots exist between {x0} and {x1}')
        quit()

    accuracy = 1e-9

    if isclose(f(x0), 0, abs_tol=accuracy):
        return x0
    if isclose(f(x1), 0, abs_tol=accuracy):
        return x1

    xold = x0

    while True:
        xnew = (x0 + x1)/2
        if isclose(f(xnew), 0, abs_tol=accuracy):
            return xnew
        if isclose(abs((xnew-xold)/xold), err , abs_tol= accuracy):
            return xnew
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

root = bisection(fun,low,up,0.1/100)
print(root)
