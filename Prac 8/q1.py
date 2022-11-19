# To simulate the radioactive decay of particles using random numbers

from time import time
import matplotlib.pyplot as plt

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

n_parent = 100
check = True
threshold = 0.3
t = 0
t_half = 0.693/threshold
n_parent_nucs = [n_parent]
while check:
    count = 0
    for randnum in lcg(214013, 2531011, 2**32, n_parent, seed = int(time())):
        if randnum>threshold:
            count += 1

    n_parent = count
    n_parent_nucs.append(n_parent)
    t += 1
    
    if n_parent == 0:
        check = False

    if t>20:
        print('Too long loop.')
        break

for i in range(len(n_parent_nucs)):
    print(f'{i}\t{n_parent_nucs[i]}\t{n_parent_nucs[0]-n_parent_nucs[i]}\n')

n_daughter_nucs = []

for i in range(len(n_parent_nucs)):
    n_daughter_nucs.append(n_parent_nucs[0] - n_parent_nucs[i])

times = range(t+1)

plt.plot(times, n_parent_nucs, label="Parent nuclei")
plt.plot(times, n_daughter_nucs, label="Daughter nuclei")
plt.legend(loc='upper left')
plt.xlabel('t')
plt.ylabel('n')
plt.show()