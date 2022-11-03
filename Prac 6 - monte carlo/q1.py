def lcg(a, c, m, n, seed = 0):
    x = seed
    if m<=0:
        raise ValueError(f'm = {m} should be greater than zero')
    if a>=m:
        raise ValueError(f'a = {a} should be greater than m = {m}')
    if c>=m:
        raise ValueError(f'c = {c} should be greater than m = {m}')
    
    for _ in range(n):
        x = (a*x + c)%m
        yield x/m



def mid_square(n, seed = 1234):
    if len(str(seed)) != 4:
        raise ValueError(f'The initial seed {seed} must be 4 digit number')
    x = seed
    for _ in range(n):
        x = str(x**2)
        if len(x) != 8:
            zeros = '0'*(8-len(x))
            x = zeros + x
        x = int(x[2:-2])
        yield x/9999


def monte_carlo_lcg():
    count = 0
    n = 1000000
    for num1, num2 in zip(lcg(214013,2531011,2**32, n, seed = 38475),lcg(214013,2531011,2**32, n, seed = 9856)):
        # print(num1, num2)
        if (num1-0.5)**2 + (num2-0.5)**2 <=0.5**2:
            count+=1
    pii = 4*count/n
    print(f'Value of PI using lcg is {pii}')

def monte_carlo_ms():
    count = 0
    n = 1000000
    for num1, num2 in zip(mid_square(n, seed=7384),mid_square(n, seed=9986)):
        # print(num1, num2)
        if (num1-0.5)**2 + (num2-0.5)**2 <=0.5**2:
            count+=1
    pii = 4*count/n
    print(f'Value of PI using midsquare is {pii}')

from random import random

def monte_carlo_inbuilt():
    count = 0
    n = 1000000
    for _ in range(n):
        # print(num1, num2)
        if (random()-0.5)**2 + (random()-0.5)**2 <=0.5**2:
            count+=1
    pii = 4*count/n
    print(f'Value of PI using inbuilt random() is {pii}')

from multiprocessing import Process

if __name__ == '__main__':
    Process(target=monte_carlo_lcg).start()
    Process(target=monte_carlo_ms).start()
    Process(target=monte_carlo_inbuilt).start()
