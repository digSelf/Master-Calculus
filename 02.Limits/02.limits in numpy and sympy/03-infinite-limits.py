import sympy as sym
import matplotlib.pyplot as plt
import numpy as np

sx = sym.var('x')
fsx = 1 / (sx - 2)**2

# plot the function
fx = sym.lambdify(sx, fsx, 'numpy')
domain = np.linspace(0, 4, 500)

plt.ylim((0, 100))
plt.plot(domain, fx(domain))
plt.axvline(x=2.0, linestyle='--')

plt.show()

# compute the limits
# from the left
left_limit = sym.limit(fsx, sx, 2, dir='-')
sym.pprint(f"Limit as x->2 from the left: {left_limit}")

# from the right
right_limit = sym.limit(fsx, sx, 2, dir='+')
sym.pprint(f"Limit as x->2 from the left: {right_limit}")

# from the both side
limit = sym.limit(fsx, sx, 2, dir='+-')
sym.pprint(f"Limit as x-> 2 (two-sided): {limit}")