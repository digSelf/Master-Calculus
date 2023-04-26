import sympy as sym
import numpy as np
import matplotlib.pyplot as plt

# In sympy
sx = sym.var('x')
fsx = 3 / (1 - sx ** 2) 

# get the continuous domain 
# The sympy.Interval generate a interval
interval = sym.calculus.util.continuous_domain(fsx, sx, sym.Interval(-2, 2))
sym.pprint(interval)

# Print singularities for the function with a given variable.
sym.pprint(sym.singularities(fsx, sx))

sym.plot(fsx, (sx, -2, 2), xlim=(-2, 2), ylim=(-20, 20))

# In numpy
x = np.linspace(-2, 2, 1000)
fx = 3 / (1 - x ** 2)

plt.plot(x, fx, color='k')
plt.xlim((-2, 2))
plt.ylim((-20, 20))

plt.show()

