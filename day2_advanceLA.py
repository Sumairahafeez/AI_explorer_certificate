import numpy as np

A = np.array([[1, 2], [3, 4]])
# calculating determinant of matrix
det_A = np.linalg.det(A)
print("Determinant of matrix A:\n", det_A)
# calculating inverse of matrix
inv_A = np.linalg.inv(A)
print("Inverse of matrix A:\n", inv_A)