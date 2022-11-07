from copy import deepcopy
import numpy as np

def gauss_inverse(A):

    if np.linalg.det(A) == 0:
        print('Singular matrix A, no inverse exist')
        quit()
        
    l = len(A)
    identity = np.eye(l)
    print('The solution has the following steps')
    for i in range(0,l):
        for j in range(l-1, -1, -1):
            if i!=j:
                coeff = A[j][i]/A[i][i]
                A[j] = np.subtract(A[j], np.multiply(coeff, A[i]))
                identity[j] = np.subtract(identity[j], np.multiply(coeff, identity[i]))
                print("R%d -> R%d - %0.5f x R%d" % (j+1, j+1, coeff, i+1))
                print(A)
                print(identity)
    for i in range(0,l):
        coeff = 1/A[i][i]
        A[i] = np.multiply(coeff, A[i])
        identity[i] = np.multiply(coeff, identity[i])
        print("R%d -> %0.5f x R%d" % (i+1, coeff, i+1))
        print(A)
        print(identity)

    return identity


A = np.array([[15.0,-3.0,-1.0],[-3.0,18.0,-6.0],[-4.0,-1.0,12.0]])
B = np.array([[3300.0],[1200.0],[2400.0]])

print("A = \n",A)

A_orig = deepcopy(A)

A_inv = gauss_inverse(A)

print("A^-1 = \n", A_inv)

X = np.dot(A_inv, B)

print(X)

X_orig = deepcopy(X)

X[0] += 10

B_prime = np.dot(A_orig, X)
print(B_prime)

print("Change in mass input of reactor 3 for a 10g/cm3 increase in c1 is = ", B_prime[-1] - B[-1])

B_dprime = np.array([[3300.0-700.0],[1200.0-350.0],[2400.0]])

X_prime = np.dot(A_inv, B_dprime)

print(X_prime)

print("With updated mass inputs, the concentration of reactor 3 will be reduced by ", X[-1] - X_prime[-1])

