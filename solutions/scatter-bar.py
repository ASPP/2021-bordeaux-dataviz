import numpy as np
import matplotlib.pyplot as plt

n = 50
X = np.arange(0,10)
Y = np.zeros((len(X),n));
for i in range(len(X)):
    Y[i] = np.abs(np.random.normal(np.random.uniform(1,2),
                            np.random.uniform(0.1,0.5), n))

fig = plt.figure(figsize=(10,3))
ax = plt.subplot();

ax.bar(X, Y.mean(axis=1), color="C0")
for i in range(len(X)):
    ax.scatter(np.random.uniform(X[i]-0.1, X[i]+0.1, n), Y[i],
               s = 30, facecolor="C0", edgecolor="white",
               zorder=10, alpha=0.75)

ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_xticks(X)
ax.set_yticks([])

plt.tight_layout()
plt.show()
