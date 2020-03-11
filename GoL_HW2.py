import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Size of grid that increase row from example to show the toad pattern in center of the grid.
universe = 6

# Alive cells = "on"
alive = 1
# Dead cells = "off"
dead = 0
# list of values "on" and "off" used to populate the initial universe
vals = [alive, dead]
# set pattern of oscillator that is the toad.
#grid = np.random.choice(vals, universe*universe, p=[0.1, 0.9]).reshape(universe, universe)
grid = np.array([[0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]])
# Define a function to animate the cells in the universe
# animated_universe is a void function, but placeholder values *arg,
# **kwords necessary for matplotlib initial value (framerate)
def animated_universe(framenumber, *arg, **kwords):
    global grid
    #global animatedcount
    newGrid = grid.copy()
    for i in range(universe):
        for j in range(universe):
            total = (grid[i, (j-1)%universe] +
                    grid[i, (j+1)%universe] +
                    grid[(i-1)%universe, j] + grid[(i+1)%universe, j] +
                    grid[(i-1)%universe, (j-1)%universe] + grid[(i-1)%universe, (j+1)%universe] +
                    grid[(i+1)%universe, (j-1)%universe] + grid[(i+1)%universe, (j+1)%universe])/alive
            # Rules for a cell dying off or staying alive
            if grid[i, j] == alive:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = dead
            else:
                if total == 3:
                    newGrid[i, j] = alive
    grid = newGrid.copy()
    mat.set_data(grid)
    return mat

fig, ax = plt.subplots()
mat = ax.matshow(grid)
# interval : number, optional
# Delay between frames in milliseconds. Defaults to 200.
# save_count : int, optional
# The number of values from frames to cache.
ani = animation.FuncAnimation(fig, animated_universe, interval=60)
# use higher interval to observe oscillator
# ani = animation.FuncAnimation(fig, animated_universe, interval=60)
plt.show()
