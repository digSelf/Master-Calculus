import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

plt.rc('font',family='Times New Roman')

# The function: f(x) = -x^4 + 3x^3 + x^2
domain = [-2.0, 2.0]

# crate a symbolic variable
beta = sym.var('beta')

# define the function
expr = -beta**4 + 3 * beta**3 + beta**2

# convert sympy into numpy 
f = sym.lambdify(beta, expr, modules='numpy')
x = np.linspace(domain[0], domain[-1]) 
y = f(x)

# plot the figure
plt.plot(x, y, label='$f(\\beta) = -\\beta^4 + 3\\beta^3 + \\beta^2$')
plt.legend()

plt.grid()
plt.xlim(domain[0], domain[-1])

plt.xlabel('$\\beta$')
plt.ylabel('$y = f(\\beta)$')

plt.show()