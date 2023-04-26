import numpy as np
import matplotlib.pyplot as plt

f = [0] * 3

x0 = np.linspace(-3, 0, endpoint=False) 
f[0] = x0, x0 * 0, r'Piece 1'

x1 = np.linspace(0, 3, endpoint=False) 
f[1] = x1, -2 * x1 , r'Piece 2'

x2 = np.linspace(3, 5) 
f[2] = x2, 0.1 * (x2 ** 3), r'Piece 3'

for xx, func, label in f:
    plt.plot(xx, func, label=label)

plt.legend()
plt.show()