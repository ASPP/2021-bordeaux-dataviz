import numpy as np
import matplotlib.pyplot as plt

RGB = plt.imread("data/MonaLisa.jpg")
R,G,B = RGB[...,0], RGB[...,1], RGB[...,2]
L = 0.30*R+0.59*G+0.11*B

fig = plt.figure(figsize=(10,3))
ax = plt.subplot(1,5,1)
ax.imshow(RGB)
ax.set_xticks([])
ax.set_yticks([])

ax = plt.subplot(1,5,2)
ax.imshow(R, cmap="Reds_r")
ax.set_xticks([])
ax.set_yticks([])

ax = plt.subplot(1,5,3)
ax.imshow(G, cmap="Greens_r")
ax.set_xticks([])
ax.set_yticks([])

ax = plt.subplot(1,5,4)
ax.imshow(B, cmap="Blues_r")
ax.set_xticks([])
ax.set_yticks([])

ax = plt.subplot(1,5,5)
ax.imshow(L, cmap="cividis")
ax.set_xticks([])
ax.set_yticks([])

plt.tight_layout()
plt.show()
