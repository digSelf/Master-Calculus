import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

# import signal to find peaks
from scipy.signal import find_peaks

sx = sym.var("x")
fsx = sym.cos(sx ** 2)
dfsx = sym.diff(fsx, sx)

x = np.linspace(-np.pi/2, 6*np.pi/7, 1000)
# fx = lambda x : np.cos(x**2)
fx = sym.lambdify(sx, fsx, 'numpy')
dfx = sym.lambdify(sx, dfsx, 'numpy')

global_slope = (fx(x[-1]) - fx(x[0])) / (x[-1] - x[0])

# get real-number roots
problem = lambda x : dfx(x) - global_slope
gridSearch = problem(x)

peaks = find_peaks(-np.abs(gridSearch))[0]
for i, xx in enumerate(peaks):
    b = x[xx]
    plt.scatter(b, fx(b), label=f'$b_{i}$')
    # plot the tangent line
    tangent_X = np.linspace(b - .5, b + .5)
    tangent_Y = dfx(b) * (tangent_X - b) + fx(b)
    plt.plot(tangent_X, tangent_Y, ls=':', c='k', label=f'$tangent_{i}$')

# plot secant line
plt.plot(x, fx(x), label='f(x)')
plt.plot((x[0], x[-1]), (fx(x[0]), fx(x[-1])), 'o--', label='secant')

plt.axvline(x=x[0], ls=':')
plt.axvline(x=x[-1], ls=':')
    
plt.legend()
plt.show()
