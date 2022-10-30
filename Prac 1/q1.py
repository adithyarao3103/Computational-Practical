from math import exp, log10

def false_posi(f, x0, x1, err):
    if x1 < x0:
        raise Exception('The Input points x0 and x1 should be such that x0 < x1')
    if f(x0)*f(x1)>0:
        raise Exception('No roots exist between %.5f and %.5f' % (x0, x1))
    
    iters = 0

    accuracy = int(log10(int(10/err)))

    if abs(round(f(x0),)) == 0:
        return x0, iters
    if abs(round(f(x1),accuracy)) == 0:
        return x1, iters

    xold = x0

    while True:
        iters+=1
        xnew = x0 - f(x0)*((x1 - x0)/(f(x1) - f(x0)))
        if abs(round(f(xnew),accuracy)) == 0:
            return round(xnew,accuracy), iters
        if round(abs((xnew-xold)/xold) - err , accuracy) == 0:
            return round(xnew, accuracy), iters
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

root, iters = false_posi(fun,low,up,0.001)
print(root, ' converged after ', iters, ' iterations')
