import matplotlib.pyplot as plt

plt.plot([-1, 3], [1, 6], 'o')
plt.plot([-1, 3], [1, 6], color='k')

slope = (6 - 1) / (3 - (-1))

plt.title(f"the slope is {slope}")
plt.show()