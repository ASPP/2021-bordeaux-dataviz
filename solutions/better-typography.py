import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 257, endpoint=True)
C, S = np.cos(X), np.sin(X)

fig = plt.figure(figsize=(8,3))
ax = plt.subplot()

ax.plot(X, C, marker="o", markevery=(0, 32), markerfacecolor="white",
        zorder=10, label="cosine")
ax.plot(X, S, marker="o", markevery=(0, 32), markerfacecolor="white",
        zorder=10, label="sine")

ax.set_xticks([-np.pi, -np.pi/2, np.pi/2, np.pi])
ax.set_xticklabels([r"$-\pi$", r"$-\frac{\pi}{2}$",
                    r"$+\frac{\pi}{2}$", r"$+\pi$"])
ax.set_yticks([-1,1])
ax.set_yticklabels([r"$-1$", r"$+1$"])

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
ax.legend(loc='upper left', frameon=False);
ax.set_title("Trigonometric functions", x=0.1)

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize("large")
    
plt.show()
