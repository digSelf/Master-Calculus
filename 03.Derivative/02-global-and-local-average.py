import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 5, 50)
fx = lambda x: x ** 2

y = fx(x)
plt.plot(x, y, 'o-')
plt.show()

global_average_slope = (y[-1] - y[0]) / (x[-1] - x[0])

slopes = np.zeros(len(y) - 1)
# for each segment
for i in range(len(x) - 1):
    slopes[i] = (y[i + 1] - y[i]) / (x[i + 1] - x[i])

local_average_slope = np.mean(slopes)
print(f"global average slope: {global_average_slope: .2f}\tlocal average slope: {local_average_slope : .2f}")
