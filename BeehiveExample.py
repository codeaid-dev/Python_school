import numpy as np
import matplotlib.pyplot as plt

universe = np.zeros((5, 6))

beehive = [[0, 1, 1, 0],
            [1, 0, 0, 1],
            [0, 1, 1, 0]]

universe[1:4, 1:5] = beehive

plt.imshow(universe, cmap='binary')
plt.show()
