import numpy as np
import matplotlib.pyplot as plt

fx = lambda x : x**2

N = 5
x = np.linspace(-1, 5, N)

fig = plt.figure(figsize=(5, 8))

plt.subplot(2, 1, 1)
plt.scatter(x, fx(x))
plt.plot(x, fx(x))
plt.title("Function")
# plt.show()

# calculate the slope series
y = fx(x)
result = []
plt.subplot(2, 1, 2)
for i in range(1, len(x)):
    delta_x = x[i] - x[i - 1]
    delta_y = y[i] - y[i - 1]
    plt.plot([x[i - 1], x[i]], [delta_y / delta_x] * 2)

plt.title("Segment slopes")

plt.tight_layout()
plt.show()