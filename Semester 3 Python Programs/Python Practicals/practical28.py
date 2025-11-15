import numpy as np
A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[7, 8, 9],
              [1, 2, 3]])
print("Matrix A:\n", A)
print("\nMatrix B:\n", B)

add_result = A + B
print("\nMatrix Addition (A + B):\n", add_result)

sub_result = A - B
print("\nMatrix Subtraction (A - B):\n", sub_result)

mul_result = A * B
print("\nElement-wise Multiplication (A * B):\n", mul_result)

matmul_result = A.dot(B.T) 
print("\nMatrix Multiplication (A × Bᵀ):\n", matmul_result)

transpose_A = A.T
print("\nTranspose of Matrix A:\n", transpose_A)
print("\nApurva Kumar, 04814902024")