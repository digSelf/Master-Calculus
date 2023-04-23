import sympy as sym
import matplotlib.pyplot as plt

plt.rc('font',family='Times New Roman')

# The function: f(x) = -x^4 + 3x^3 + x^2
domain = [-2.0, 2.0]

# crate a symbolic variable
beta = sym.var('beta')

# define the function
expr = -beta**4 + 3 * beta**3 + beta**2

# use sympy's plotting engine
sym.plot(expr, (beta, domain[0], domain[-1]), xlabel="$\\beta$", ylabel=None, 
         title='$f(\\beta) = -\\beta^4 + 3\\beta^3 + \\beta^2$')

plt.show()