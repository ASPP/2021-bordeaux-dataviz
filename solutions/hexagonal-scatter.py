import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
X, Y = np.arange(32)-16., np.arange(32)-16.
X, Y = np.meshgrid(X,Y)
X[::2,:] += 0.5

V = np.abs(X**2 + Y**2)                   # Distance to center
V /= V.max()
M = np.abs(np.random.normal(0, V)) > 0.25 # Random mask
V = np.random.uniform((1-V)/2, (1-V))**2  # Random value / distance to center
V[M] = 1.5                                # Set mask    

fig = plt.figure(figsize=(8,8))
ax = plt.subplot(aspect=0.9)
ax.scatter(X, Y, 300, V, marker='h', cmap="hot", vmin=0, vmax=1);

plt.tight_layout()
plt.show()
