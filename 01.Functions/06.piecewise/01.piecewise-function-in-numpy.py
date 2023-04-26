import numpy as np
import matplotlib.pyplot as plt

# The domain is [-3, 5]
x = np.linspace(-3, 5)

# The pieces
f1 = 0 * x * (x < 0)
f2 = -2 * x * ((x >= 0) & (x < 3))
f3 = 0.1 * (x ** 3) * (x >= 3)

# The function composited by the above pieces
f = f1 + f2 + f3
plt.plot(x, f)
plt.show()
