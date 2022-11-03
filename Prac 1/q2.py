from math import isclose, exp

def bisection(f, x0, x1, err):
    if x1 < x0:
        raise Exception('The Input points x0 and x1 should be such that x0 < x1')
    if f(x0)*f(x1)>0:
        raise Exception(f'No roots exist between {x0} and {x1}')
    
    iters = 0

    accuracy = 1e-9

    if isclose(f(x0), 0, abs_tol=accuracy):
        return x0, iters
    if isclose(f(x1), 0, abs_tol=accuracy):
        return x1, iters

    xold = x0

    while True:
        iters+=1
        xnew = (x0 + x1)/2
        if isclose(f(xnew), 0, abs_tol=accuracy):
            return xnew, iters
        if isclose(abs((xnew-xold)/xold), err , abs_tol= accuracy):
            return xnew, iters
        if f(x0)*f(xnew)<0:
            x1 = xnew
        else:
            x0 = xnew
        xold = xnew


def fun(x):
    return((1 - exp(-x*3.9/80))*9.8*80/x -35)
    

root, iters = bisection(fun,3,5,5/100)
print(root, ' converged after ', iters, ' iterations')

print('Value of function at %0.5f is %0.5f' % (root, fun(root)))