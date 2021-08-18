import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

T = np.linspace(0,2*np.pi,512, endpoint = False)
X, Y = 1.01 + np.cos(T), 1.01 + np.sin(T)

fig = plt.figure(figsize=(10,3))

ax = plt.subplot(1, 3, 1, aspect=1);
ax.plot(X,Y, color="black")
ax.set_xticks([0,1,2])
ax.xaxis.set_major_locator(MultipleLocator(1.0));
ax.xaxis.set_minor_locator(MultipleLocator(0.1));
ax.set_yticks([0,1,2])
ax.yaxis.set_major_locator(MultipleLocator(1.0));
ax.yaxis.set_minor_locator(MultipleLocator(0.1));
ax.grid(True, "major", linewidth=0.75);
ax.grid(True, "minor", linewidth=0.50, linestyle=":");

ax = plt.subplot(1, 3, 2, aspect=1, xscale="log", yscale="log");
ax.plot(X,Y, color="black")
ax.grid(True, "major", linewidth=0.75);
ax.grid(True, "minor", linewidth=0.50, linestyle=":");

ax = plt.subplot(1, 3, 3, aspect=1);
ax.plot(2+np.log10(X), 2+np.log10(Y), color="black")
ax.set_xticks([0,1,2])
ax.xaxis.set_major_locator(MultipleLocator(1.0));
ax.xaxis.set_minor_locator(MultipleLocator(0.1));
ax.set_yticks([0,1,2])
ax.yaxis.set_major_locator(MultipleLocator(1.0));
ax.yaxis.set_minor_locator(MultipleLocator(0.1));
ax.grid(True, "major", linewidth=0.75);
ax.grid(True, "minor", linewidth=0.50, linestyle=":");


plt.tight_layout()
plt.show()
