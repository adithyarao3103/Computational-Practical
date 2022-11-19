# To fin the value of the integral 0 to 1 x^2 using monte carlo integration

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

def monte_inte(f, N):
    '''Returns the Monte Carlo integration of function f calculated using N random numbers'''
    sum = 0
    random_nums = lcg(214013,2531011,2**32, n, seed = 38475)
    for randnum in random_nums:
        sum+=f(randnum)
    
    return sum/N

def fun(x):
    return x**2

n = 100000
integ = monte_inte(fun, n)
print(f'The integration of x^2 on [0,1] gives {integ}')


