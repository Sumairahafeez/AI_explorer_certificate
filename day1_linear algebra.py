import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
# Matrix addition
C = A + B
# Matrix subtraction
D = A - B
print("Matrix addition:\n", C)
print("Matrix subtraction:\n", D)
# Matrix multiplication
E = np.dot(A, B)
print("Matrix multiplication:\n", E)
# Hands on exercise 
# Create a 3x3 matrix and find its determinant
F = np.array([[1,2,3],[4,5,6],[7,8,9]])
determinant = np.linalg.det(F)
print("Determinant of the matrix F:\n", determinant)
# implement matrix vector multiplication
G = np.array([[1, 2, 3], [4, 5, 6]])
v = np.array([1, 2, 3])
result = np.dot(G, v)
print("Matrix-vector multiplication result:\n", result)