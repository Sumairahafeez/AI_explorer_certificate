import numpy as np

A = np.array([[1, 2], [3, 4]])
# calculating determinant of matrix
det_A = np.linalg.det(A)
print("Determinant of matrix A:\n", det_A)
# calculating inverse of matrix
inv_A = np.linalg.inv(A)
print("Inverse of matrix A:\n", inv_A)
# eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues of matrix A:\n", eigenvalues)
print("Eigenvectors of matrix A:\n", eigenvectors)
# matrix decomposition
# a process of breaking a matrix to smaller components to analyze and solve problems
S,U,V = np.linalg.svd(A)
print("Singular values of matrix A:\n", S)
print("Left singular vectors of matrix A:\n", U)
print("Right singular vectors of matrix A:\n", V)
# Hands on exercise
# Use SVD to reduce dimensionality of a matrix
# Create a 4x4 matrix
F = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
# Perform SVD
F_S, F_U, F_V = np.linalg.svd(F)
# Reduce dimensionality by keeping only the first two singular values and vectors
F_reduced = np.dot(F_U[:2], np.diag(F_S[:2]))
print("Reduced matrix F:\n", F_reduced)