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

from operator import add, sub, mul, xor

def lfg(n, op, m = 256, j = 3, k = 7, seed = 8675309):
    xs = [int(x) for x in str(seed)]
    ops = {'+':add, '-':sub, '*':mul, 'xor':xor}
    for _ in range(n):
        x = abs(ops[op](xs[-j], xs[-k])%m)
        xs = xs[1:]
        xs.append(x)
        # print(x)
        yield x/m
        

import matplotlib.pyplot as plt
from itertools import repeat
import numpy as np

def plot_random(args):
    (num1, num2, count) = args
    return[float(num1), float(num2)]

from multiprocessing import Pool 

if __name__ == '__main__':
    count = 0
    n = 1000000
    try:
        pool = Pool()                   
        vals = pool.map(plot_random, zip(lcg(214013,2531011,2**32, n, seed = 38475),lcg(214013,2531011,2**32, n, seed = 9856), repeat(count)))
    except Exception as e:
        print(e)
    finally:
        pool.close()
        pool.join()
        vals = np.array(vals)
        [xs, ys] = np.transpose(vals)
        plt.scatter(xs,ys)
        plt.show()