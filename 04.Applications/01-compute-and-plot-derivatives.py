import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def compute(fsx, sx, l, r):
    dfsx = sym.diff(fsx, sx)
    ddfsx = sym.diff(fsx, sx, 2)
    
    fsx_lam = sym.lambdify(sx, fsx)
    dfs_lam = sym.lambdify(sx, dfsx)
    ddfsx_lam = sym.lambdify(sx, ddfsx) 
    
    # get critical points by numerical  
    x = np.linspace(l, r, 1000)
    ids = find_peaks(-np.abs(dfs_lam(x)))[0]

    points = x[ids]
    return fsx_lam, dfs_lam, ddfsx_lam, points
    

sx = sym.var("x")
fsx = sx**4 - 8 * sx**2

l, r = -3, 3
f, df, ddf, ps = compute(fsx, sx, l, r)

x = np.linspace(l, r, 1000)
plt.plot(x, f(x), label='f(x)')
plt.plot(x, df(x), label='df(x)')
plt.plot(x, ddf(x), label='$d^2f(x)$')

plt.scatter(ps, f(ps), label='f(p)')
plt.scatter(ps, df(ps), label='df(p) = 0')
plt.scatter(ps, ddf(ps), label='$d^2f(p)$')

plt.axhline(y=0, ls='--', c=(.7, .7, .7))

plt.legend()
plt.show()

