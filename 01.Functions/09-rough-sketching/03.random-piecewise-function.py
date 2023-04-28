import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

sx = sym.var('x')

neg_range_fsx = [sx, sx ** 2, sx ** 3]
pos_range_fsx = [sym.ln(sx), sym.sqrt(sx)]

nloc = np.random.choice(np.arange(len(neg_range_fsx)))
ploc = np.random.choice(np.arange(len(pos_range_fsx)))

fsx = sym.Piecewise((neg_range_fsx[nloc], sx <= 0),
              (pos_range_fsx[ploc], sx > 0))

sym.pprint(fsx)
sym.plot(fsx, ylim=(-5, 5))
