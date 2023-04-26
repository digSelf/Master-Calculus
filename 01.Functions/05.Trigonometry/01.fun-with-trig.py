import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(-np.pi, 2 * np.pi, 1000)

# sinx
plt.plot(theta, np.sin(theta), label=r'$f_1 = \sin\theta$')

# sin^2(x)
plt.plot(theta, np.sin(theta) ** 2, label=r'$f_2 = \sin^2\theta$')

# sin(x^2)
plt.plot(theta, np.sin(theta**2), label=r'$f_3 = \sin\theta^2$')

plt.legend()
plt.show()