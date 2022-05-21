# Sine wave example

from matplotlib import pyplot as plt
import numpy as np

# Linear array of values going from 0 to 2pi with 200 steps
x = np.linspace(0, 2 * np.pi, 200)

# The Y array is the sine of the X array, in other words,
# any value in Y is the sine of the corresponding value in X
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
