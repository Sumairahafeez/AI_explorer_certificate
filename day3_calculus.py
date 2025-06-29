import numpy as np
import sympy as sp
# calculating derivative of a function
x = sp.symbols('x')
f = x**2 + 3*x + 2
derivative_f = sp.diff(f, x)
print("Derivative of f(x):", derivative_f)
# partial derivative of a function
# it measures how a function changes as one variable changes while keeping others constant
y = sp.symbols('y')
g = x**2 + y**2
partial_derivative_g_x = sp.diff(g, x)
partial_derivative_g_y = sp.diff(g, y)  
print("Partial derivative of g with respect to x:", partial_derivative_g_x)
print("Partial derivative of g with respect to y:", partial_derivative_g_y)
# gradient of a function it is a vector of partial derivatives
gradient_g = [partial_derivative_g_x, partial_derivative_g_y]
# gradient decent it is an optimization algorithm used to minimize a function
# it iteratively moves towards the minimum of the function by taking steps proportional to the negative of the gradient
# Implement gradient descent algorithm for linear regression
def gradient_descent(X,y,theta, alpha=0.01, iterations=1000):
   m = len(y)
   for _ in range (iterations):
      predictions = np.dot(X,theta)
      errors = predictions - y
      gradient = np.dot(X.T,errors) /m
      theta -= alpha * gradient
   return theta
# Example usage of gradient descent
X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y = np.array([1, 2, 2, 3])
theta = np.zeros(X.shape[1])
theta = gradient_descent(X, y, theta=theta, alpha=0.01, iterations=1000)
print("Optimized parameters (theta):", theta)