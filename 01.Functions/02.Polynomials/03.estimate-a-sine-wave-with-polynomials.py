import numpy as np
import matplotlib.pyplot as plt

# the order of the polynomial
order = 10

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.zeros(len(x))

# print(y.shape)
# plot for each monomial with different order
z = np.zeros(len(x))
for n in range(1, order + 1):
    mono = (-1)**(n + 1) * x**(2 * n - 1)/ np.math.factorial(2 * n - 1) 

    z += mono
    plt.plot(x, mono, '--', linewidth=.8)

plt.plot(x,z,'k',linewidth=3,label=f'Sum over {order} terms')
plt.plot(x[::5],np.sin(x[::5]),'bo',markerfacecolor='w',linewidth=3,label='sin(x)')
# plt.scatter(x[::5], np.sin(x[::5]), marker='o', linewidths=3, label='sin(x)')

plt.legend()
plt.ylim((-5, 5))
plt.xlim((-6, 6))

plt.show()