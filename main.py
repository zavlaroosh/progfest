import matplotlib.pyplot as plt
import numpy as np

delta = []
x = 0
while x <= 10:
    delta.append(x*(np.pi))
    x += 0.1
phis = []

for i in delta:
    phi = np.arctan(((1 - (0.95 ** 2) * np.sin(i)) / ((2 * 0.95) + ((1 + (0.95 ** 2)) * np.cos((i))))))
    phis.append(phi)

y = phis
x = delta

plt.plot(x,y)
plt.show()


