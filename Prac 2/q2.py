        # ---
        #  |                                      |       |       |
        #  |                                      |  x1   |       |
        # |O| 2kg -> 7.5g = k (x1)                        |       |
        #  |                                              |       |
        #  |                                              |   x2  |
        # |O| 3kg -> 5.5g = k (x2 - x1)                           |   
        #  |                                                      |
        #  |                                                      |
        # |O| 2.5kg -> 2.5g = k (x3 - x2)                         |   x3

# Therefore the system of equations is 

#      x1 + 0x2 + 0x3= 7.5g/k
#     -x1 + x2 + 0x3 = 5.5g/k 
#     0x1 -x2 + x3 = 2.5g/k

import numpy as np

def gauss_elem(A,B, show_steps):
    
    if np.linalg.det(A) == 0:
        raise Exception('Singular matrix A, no solutions for the system of equations')
        
    l = len(A)
    for i in range(0,l):
        for j in range(l-1, i, -1):
            coeff = A[j][i]/A[i][i]
            A[j] = np.subtract(A[j], np.multiply(coeff, A[i]))
            B[j] = np.subtract(B[j], np.multiply(coeff, B[i]))
            if show_steps:
                print("R%d -> R%d - %0.5f x R%d" % (j+1, j+1, coeff, i+1))
                print(A)
                print(B)

    X = np.zeros(l)

    for i in range(0,l):
        sum = B[l-i-1][0]
        for j in range(l-1,l-i-1,-1):
            sum -= A[l-i-1][j]*X[j]
        sum /= A[l-i-1][l-i-1]

        X[l-i-1] = sum

    return np.transpose([X])

k = 10
g = 9.81

A = np.array([[1.0,0.0,0.0],[-1.0,1.0,0.0],[0.0,-1.0,1.0]])
B = np.array([[7.5*g/k],[5.5*g/k],[2.5*g/k]])

print("A = \n",A)
print("B = \n",B)

X = gauss_elem(A, B, show_steps = False)

print("The roots are \n", X)

