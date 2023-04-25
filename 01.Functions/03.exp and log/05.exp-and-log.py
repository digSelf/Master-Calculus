import matplotlib.pyplot as plt
import numpy as np

# domain: [-4, 4]
x = np.linspace(-4, 4, 500)

y1 = np.exp(x)

x2 = x[x > 0]
y2 = np.log(x2)  

y3 = np.exp(y2)
y4 = np.log(y1)

plt.plot(x, y1, label='$e^x$')
plt.plot(x2, y2, label=r'$\ln(x)$')
plt.plot(x2[::20], y3[::20], 'ro', markerfacecolor='w', markeredgewidth=1.5, label=r'$e^{\log(x)}$')
plt.plot(x, y4, label=r'$\ln(e^x)$')

plt.legend()
plt.ylim((-4, 4))
plt.xlim((-4, 4))
plt.grid()

plt.show()