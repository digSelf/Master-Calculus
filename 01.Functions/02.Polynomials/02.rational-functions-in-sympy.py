import matplotlib.pyplot as plt
import sympy as sym

# create a symbolic variable
x = sym.var('x')

# define the function
expr = (x**2 - 2*x) / (x**2 - 4)

# calculate
domain = [-5, 5]
sym.plot(expr, (x, domain[0], domain[-1]), 
         xlim=[domain[0], domain[-1]],
         ylim=[-10, 10],
         title=f'$y = f({sym.latex(expr)})$',
         ylabel=None)

plt.show()

