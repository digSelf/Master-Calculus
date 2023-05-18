import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

sx = sym.var("x")
fsx = sym.cos(sx ** 2)
dfsx = sym.diff(fsx, sx)

x = np.linspace(-np.pi/2, 6*np.pi/7, 1000)
# fx = lambda x : np.cos(x**2)
fx = sym.lambdify(sx, fsx, 'numpy')
dfx = sym.lambdify(sx, dfsx, 'numpy')

global_slope = (fx(x[-1]) - fx(x[0])) / (x[-1] - x[0])

# get all possible solutions
# Biseaction: guess and verify
def bisection(f, a, c, err=1e-5):
    m = a 

    l, r = a, c
    while np.abs(f(m)) > err:
        m = (l + r) / 2
        if np.sign(f(m)) == np.sign(f(l)):
            l, r = m, r
        else:
            l, r = l, m
            
    return m 

# plot secant line
plt.plot(x, fx(x), label='f(x)')
plt.plot((x[0], x[-1]), (fx(x[0]), fx(x[-1])), 'o--', label='secant')

plt.axvline(x=x[0], ls=':')
plt.axvline(x=x[-1], ls=':')

# get real-number roots
problem = lambda x : dfx(x) - global_slope
intervals = [
    [-np.pi/2, 1],
    [1, 2],
    [2, 6*np.pi/7]
]
for i, rg in enumerate(intervals):
    l, r = rg
    b = bisection(problem, l, r)
    plt.scatter(b, fx(b), label=f'$b_{i}$')
    # plot the tangent line
    tangent_X = np.linspace(b - 1, b + 1)
    tangent_Y = dfx(b) * (tangent_X - b) + fx(b)
    plt.plot(tangent_X, tangent_Y, ls=':', c='k', label=f'$tangent_{i}$')
    
plt.legend()
plt.show()
