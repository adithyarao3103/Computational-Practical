# To generate random numbers using LCG, MidSquare and LFG method

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


n = 100

random_lcg = lcg(214013,2531011,2**32, n, seed = 38475)
random_ms = mid_square(n, seed=7777)
random_lfg = lfg(n,add)

print('LCG \t\t\t\t MID SQUARE \t\t\t LFG\n')
for i in range(n):
    print(f'{random_lcg[i]} \t\t {random_ms[i]} \t\t {random_lfg[i]}\n')
