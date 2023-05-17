import numpy as np
import matplotlib.pyplot as plt

# define the x-axis grid
dx = .01
x = np.arange(-np.pi, np.pi, dx)

# define the function
fx = .1 * (x**4) + np.exp(-(x**2)) + np.cos(x)

# compute the derivatives
dfx = np.diff(fx, n=1) / dx 
ddfx = np.diff(fx, n=2) / (dx**2)  # the second derivative need divide by dx^2
dddfx = np.diff(fx, n=3) / (dx**3)

_, axes = plt.subplots(4, 1)
axes[0].plot(x, fx)
axes[1].plot(x[:-1], dfx)
axes[2].plot(x[:-2], ddfx)
axes[3].plot(x[:-3], dddfx)

plt.show()