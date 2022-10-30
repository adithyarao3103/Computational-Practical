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

        

A = np.array([[2.0,-6.0,-1.0],[-3.0,-1.0,7.0],[-8.0,1.0,-2.0]])
B = np.array([[-38.0],[-34.0],[-20.0]])

print("A = \n",A)
print("B = \n",B)

X = gauss_elem(A, B, show_steps = False)

print("The roots are \n", X)

print("Verification --> A.X - B = \n" , np.subtract(np.dot(A,X), B))