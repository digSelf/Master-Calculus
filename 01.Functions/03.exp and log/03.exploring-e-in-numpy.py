import matplotlib.pyplot as plt
import numpy as np

# domain_range = [-2, 2]
x = np.linspace(-2, 2)

y1 = np.exp(x) 
y2 = np.exp(x ** 2)
y3 = np.exp((-x) ** 2)
y4 = np.exp(-(x) ** 2)
y5 = np.exp(x) ** 2


plt.plot(x, y1, label=r'$e^x$')
plt.plot(x, y2, label=r'$e^{x^2}$')
plt.plot(x, y3, label=r'$e^{(-x)^2}$')
plt.plot(x, y4, label=r'$e^{-(x)^2}$')
plt.plot(x, y5, label=r'$(e^x)^2$')

plt.legend()
plt.grid()

plt.xlim((-2, 2))
plt.xlabel('x')
plt.ylabel('y = f(x)')

plt.show()