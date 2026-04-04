# Least Squares Method

The least squares method is used when a system of equations has no exact solution and we want the "best" approximate one. Instead of solving

$$
Ax = b
$$

exactly, we choose $x$ so that the error

$$
r = b - Ax
$$

is as small as possible.

## Main Idea

Least squares minimizes the sum of squared residuals:

$$
\min_x \|Ax - b\|^2
$$

This means we look for the vector $x$ that makes the prediction $Ax$ as close as possible to $b$.

## Normal Equations

The least-squares solution satisfies the normal equations:

$$
A^T A x = A^T b
$$

If $A^T A$ is invertible, then

$$
x = (A^T A)^{-1}A^T b
$$

## Geometric Interpretation

The vector $Ax$ is the projection of $b$ onto the column space of $A$. The residual vector

$$
r = b - Ax
$$

is orthogonal to every column of $A$, which is why

$$
A^T(b - Ax) = 0
$$

leads to the normal equations.

## Why Squared Error?

Squaring errors:

- makes all errors nonnegative
- penalizes large errors more heavily
- gives a smooth objective that is easy to optimize

## Common Use Cases

- linear regression
- data fitting
- overdetermined systems
- trend estimation from noisy observations

## Summary

Least squares finds the approximation $x$ that minimizes the squared difference between $Ax$ and $b$. In linear algebra, it gives the best approximate solution to an inconsistent system, and in statistics it forms the basis of linear regression.
