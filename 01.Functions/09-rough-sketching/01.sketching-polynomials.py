import numpy as np
import matplotlib.pyplot as plt

coefficients = np.random.randn(3) 
x = np.linspace(-5, 5)

print(coefficients)
y = coefficients[0] + coefficients[1] * x + coefficients[2] * (x** 2)

plt.plot(x, y)
plt.show()