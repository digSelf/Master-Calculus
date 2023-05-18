import numpy as np
import matplotlib.pyplot as plt
import sympy as sym



# solve the MVT
def solveMVT(fsx, sx, a, c):
    global_slope = (fsx.subs(sx, c) - fsx.subs(sx, a)) / (c - a)
    dfsx = sym.diff(fsx, sx)

    rs = np.array(sym.solve(sym.Eq(dfsx, global_slope), sx)).astype(np.float64)
    
    return rs[np.bitwise_and(a < rs, rs < c)] 

def makePlot(fsx, sx, a, c):
    # solve the MVT
    bs = solveMVT(fsx, sx, a, c) 

    # lambdify the expressions
    fx_lam = sym.lambdify(sx, fsx, 'numpy')
    dfx_lam = sym.lambdify(sx, sym.diff(fsx, sx), 'numpy')
    
    # get the function values 
    xx = np.linspace(a - 2, c + 2, 1000)
    
    # plot the function
    plt.plot(xx, fx_lam(xx), label='f(x)')
    
    # plot the secant line
    plt.plot([a, c], [fx_lam(a), fx_lam(c)], 'o--', color=(.7, .7, .7), label='secant')
    plt.axvline(x=a, ls=':')
    plt.axvline(x=c, ls=':')
    
    # plot b and the tangent line
    for i, b in enumerate(bs):
        # plot the point b
        plt.scatter(b, fx_lam(b), label=f'$b_{i}$')

        # plot the tangent line
        tangent_X = np.linspace(b - 1, b + 1)
        tangent_Y = dfx_lam(b) * (tangent_X - b) + fx_lam(b)
        plt.plot(tangent_X, tangent_Y, ls=':', c='k', label=f'$tangent_{i}$')
    
    plt.xlim((a - 1, c + 1))
    plt.ylim((-10, 10))
    plt.legend()
    plt.title(f"$f(x) = {sym.latex(fsx)}$")    

    plt.show() 

if __name__ == '__main__':
    sx = sym.var("x")
    fsx = 2*sx**3 - 3*sx**2 + 1
    sx_interval = [-1, 2]
    makePlot(fsx, sx, sx_interval[0], sx_interval[1])

    sy = sym.var("theta")
    gsy = sym.sin(sy)
    sy_interval = [0, 1.8 * np.pi]
    makePlot(gsy, sy, sy_interval[0], sy_interval[1])
