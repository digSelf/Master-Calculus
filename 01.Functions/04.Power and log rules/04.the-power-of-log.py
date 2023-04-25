import numpy as np
import matplotlib.pyplot as plt

# random generate series
x = np.random.rand(50)
y = np.random.rand(50)

# demonstrate ln(xy) = lnx + lny
z = np.around(np.log(x * y) - np.log(x) - np.log(y), 5)
x = np.arange(1, len(z) + 1)

plt.plot(x, z, label=r"$\ln{xy} - \ln x - \ln y$")

# demonstrate ln(x/y) = lnx - lny
z = np.around(np.log(x/y) - np.log(x) + np.log(y))
plt.plot(x, z, label=r'$\ln{\frac{x}{y}} - \ln x + \ln y$')

# demonstrate ln(x^y) = ylnx
z = np.around(np.log(x**y) - y * np.log(x))
plt.plot(x, z, label=r'$\ln{x^y} - y\ln x$')

plt.legend()
plt.show()