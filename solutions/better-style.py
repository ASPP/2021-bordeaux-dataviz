import numpy as np
import matplotlib.pyplot as plt

def subplot(index, title):    
    ax = plt.subplot(2, 3, index, aspect=1)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_position(('data',0))
    ax.spines['left'].set_position(('data',0))
    ax.set_xlim(-4.5,4.5)
    ax.set_xticks([-4,-3,-2,-1,1,2,3,4])
    ax.plot(4.5, 0, ">k", clip_on=False)
    ax.set_ylim(-2.5,2.5)
    ax.set_yticks([-2,-1,1,2])
    ax.plot(0, 2.5, "^k", clip_on=False)
    ax.text(-4.5, 2, title, weight=600)
    ax.grid(linewidth=0.5, linestyle="--")
    return ax

fig = plt.figure(figsize=(10,4))
X = np.linspace (-4,4,200)

subplot(1, "y = cos(x)").plot(X, np.cos(X), "C1")
subplot(2, "y = sin(x)").plot(X, np.sin(X), "C1")
subplot(3, "y = tan(x)").plot(X, np.tan(X), "C1")
subplot(4, "y = cosh(x)").plot(X, np.cosh(X), "C1")
subplot(5, "y = sinh(x)").plot(X, np.sinh(X), "C1")
subplot(6, "y = tanh(x)").plot(X, np.tanh(X), "C1")

plt.tight_layout()
plt.show()
