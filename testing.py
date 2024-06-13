
import numpy as np
resolution = 32

grid =  np.empty(shape=(resolution,resolution))
grid.fill(1)
grid[1][0] = 3
print("error")
grid[(0,0)] = 3

print(grid[(1,0)])
print(grid)
