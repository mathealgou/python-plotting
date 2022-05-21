import matplotlib.pyplot as plt
import numpy as np

plt.style.use('classic')

# make data:
np.random.seed(3)
#x = 0.5 + np.arange(8)
x = ["a", "b", "c", "d", "e", "f", "g", "h"]
y = np.random.uniform(2, 7, len(x))

# plot
fig, ax = plt.subplots()

ax.bar(x, y, width=1, edgecolor="black", linewidth=0.7, color="white")


# xlim and ylim: set the limits of the axes
# xticks and yticks: set the labels of the axes, in this case,[1,2,3,4,5,6,7,]
ax.set(xlim=(0, 8), xticks=np.arange(-1, 7),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
