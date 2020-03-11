import numpy as np
import matplotlib.pyplot as plt

# Size of grid that increase row from example to show the toad pattern in center of the grid.
universe = np.zeros((6, 6))

# set pattern of oscillator that is the toad.
toad = [[0, 0, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [0, 1, 0, 0]]

# slice below to put the toad pattern in center.
universe[1:5, 1:5] = toad

plt.imshow(universe, cmap='binary')
plt.show()
