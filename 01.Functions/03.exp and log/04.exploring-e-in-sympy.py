import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

s_x = sym.var('beta')
expr = sym.exp(s_x) - sym.ln(s_x) - np.e

sym.plot(expr, (s_x, 0.001, 2.0), 
         xlim=(0.0, 2.0), xlabel='$\\beta$', ylabel='$y = f(\\beta)$',
         title=f'$f(\\beta) = e^\\beta - \\log(\\beta) - {np.e}$')

plt.show()
