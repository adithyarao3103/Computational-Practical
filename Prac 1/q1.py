from math import isclose, exp

def false_posi(f, x0, x1, err):
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
        xnew = x0 - f(x0)*((x1 - x0)/(f(x1) - f(x0)))
        if isclose(f(xnew), 0, abs_tol=accuracy):
            return xnew
        if isclose(abs((xnew-xold)/xold), err , abs_tol= accuracy):
            return xnew
        if f(x0)*f(xnew)<0:
            x1 = xnew
        else:
            x0 = xnew
        xold = xnew


def fun(x):
    return((1 - exp(-15*9/x))*9.8*x/15 -35)

for i in range(1,50):
    low, up = i*2, (i+1)*2
    if fun(low)*fun(up) < 0:
        break

root = false_posi(fun,low,up,0.001)
print(root)

