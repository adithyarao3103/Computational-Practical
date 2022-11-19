# To generate random numbers using lcg, ms and lfg methods and calculate pi from them.

def lcg(a, c, m, n, seed = 0):
    '''Generates n random numbers using LCG method, x_{i+1} = (a*x_{i} + c)%m'''
    nums = []
    x = seed
    if m<=0:
        print(f'm = {m} should be greater than zero')
        quit()
    if a>=m:
        print(f'a = {a} should be less than m = {m}')
        quit()
    if c>=m:
        print(f'c = {c} should be less than m = {m}')
        quit()
    
    for _ in range(n):
        x = (a*x + c)%m
        nums.append(float(x/m))

    return nums

def mid_square(n, seed = 1234):
    '''Generates n random numbers using mid square methd'''
    nums = []
    if len(str(seed)) != 4:
        print(f'The initial seed {seed} must be 4 digit number')
        quit()
    x = seed
    for i in range(n):
        x = str(x**2)
        if len(x) != 8:
            zeros = '0'*(8-len(x))
            x = zeros + x
        x = int(x[2:-2])
        nums.append(float(x/9999))

    return nums

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def xor(x,y):
    return x^y


def lfg(n, op, m = 256, j = 3, k = 7, seed = 8675309):
    '''Gnerates n random numbers using Lagged Fibonacci Generator method'''
    nums = []
    seed = str(seed)
    xs = []
    for entry in seed:
        xs.append(int(entry))
    for _ in range(n):
        x = abs(op(xs[-j], xs[-k])%m)
        xs = xs[1:]
        xs.append(x)
        # print(x)
        nums.append(float(x/m))

    return nums


def pi_from_lcg(n):
    count = 0
    xs = lcg(214013,2531011,2**32, n, seed = 38475)
    ys = lcg(214013,2531011,2**32, n, seed = 9856)
    for i in range(len(xs)):
        # print(num1, num2)
        if (xs[i]-0.5)**2 + (ys[i]-0.5)**2 <=0.5**2:
            count+=1
    pii = 4*count/n
    return pii


def pi_from_ms(n):
    count = 0
    xs = mid_square(n, seed=7777)
    ys = mid_square(n, seed=3333)
    for i in range(len(xs)):
        if (xs[i]-0.5)**2 + (ys[i]-0.5)**2 <=0.5**2:
            count+=1
    pii = 4*count/n
    return pii

def pi_from_lfg(n):
    count = 0
    xs = lfg(n,add)
    ys = lfg(n,subtract)
    for i in range(len(xs)):
        if (xs[i]-0.5)**2 + (ys[i]-0.5)**2 <=0.5**2:
            count+=1
    pii = 4*count/n
    return pii

from random import random

def pi_from_inbuilt(n):
    count = 0
    for _ in range(n):
        # print(num1, num2)
        if (random()-0.5)**2 + (random()-0.5)**2 <=0.5**2:
            count+=1
    pii = 4*count/n
    return pii

n=1000
pi_inbuilt = pi_from_inbuilt(n)
pi_lcg = pi_from_lcg(n)
pi_lfg = pi_from_lfg(n)
pi_ms = pi_from_ms(n)

print(f'Value of PI using linear congruential generator is {pi_lcg}')
print(f'Value of PI using midsquare is {pi_ms}')
print(f'Value of PI using lagged fibonacci generator is {pi_lfg}')
print(f'Value of PI using inbuilt random.random() is {pi_inbuilt}')
