import numpy as np

mat1 = [[1,2,3], [4,5,6], [7,8,9]]
mat2 = [[1,2,3], [4,5,6], [7,8,9]]

A = np.array(mat1)
B = np.array(mat2)

print(A + B)
print(A - B)
print(A * B)
print(A.T)