import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 1000, 1000)
y = (1 + 1 / x) ** x

diffs = np.e - y

plt.plot(x, diffs, label=r'$e - (1 + \frac{1}{n})^n$')

plt.xlabel('n')
plt.ylabel('difference')
plt.grid()
plt.legend()

plt.show()