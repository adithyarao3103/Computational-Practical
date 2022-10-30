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

k1 = 150.0
k2 = 50.0
k3 = 75.0
k4 = 225.0

g = 9.81

A = np.array([[k1 + k2, -1*k2, 0, 0 ],[-1*k2, k2+k3, -1*k3, 0],[0, -1*k3, k3 + k4, -1*k4], [0,0,-1*k4, k4]])
B = np.array([[0.0],[0.0],[0.0],[2000.0*g]])

print("A = \n",A)
print("B = \n",B)

X = gauss_elem(A, B, show_steps = False)

print("The roots are \n", X)

