import numpy as np
import matplotlib.pyplot as plt

from scipy.signal import find_peaks

step = 1000
x = np.linspace(-2, 2, step)
# x = np.arange(-1.5, 1, step=dx)
fx = x**2 + x**3

_, axes = plt.subplots(2, 1)
axes[0].plot(x, fx, label='function')

axes[0].set_ylim((-1, 1))
axes[0].set_title("The function")
axes[0].legend()

dx = (2 - (-2)) / (step - 1)
dfx = np.diff(fx) / dx
axes[1].plot(x[:-1], dfx, label='derivative')
axes[1].legend()
axes[1].set_title("its derivative")
axes[1].set_ylim((-1, 1))
axes[1].axhline(linestyle='--', color='r')

plt.tight_layout()
plt.show()

# find local minimum of abs(dfx)
temp = np.abs(dfx)
# because of the function is to find the peak of a given sequence, so we need to negate the sign 
# of np.abs(dfx)
peaks, _ = find_peaks(-temp)
print(peaks)

plt.plot(x[:-1], dfx)
plt.plot(x[peaks], dfx[peaks], "x")
plt.axhline(linestyle='--', color='r')

plt.ylim((-1, 1))

plt.tight_layout()

plt.show()

