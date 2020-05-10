import numpy as np
import io

def pos_in_grid(val, grid):

	pos = sum( [1 if x <= val else 0 for x in grid[:-1] ] ) -1
	pos = 0 if pos == -1 else pos
	return pos



def data2grid( filename, res_x, res_y ):

	with open("example_001.csv","r") as fp:
		x_data, y_data = np.loadtxt(fp, delimiter=' ', usecols=(0,1), unpack = True)

	x_grid = np.linspace( min(x_data), max(x_data), res_x )
	y_grid = np.linspace( min(y_data), max(y_data), res_y )

	grid = np.zeros((res_x, res_y))

	for x,y in zip(x_grid, y_grid):
		i = pos_in_grid(x, x_grid)
		j = pos_in_grid(y, y_grid)
		grid[i][j] += 1

	return grid





if __name__ == "__main__":

	grid = data2grid(1,10,10)
	print(grid)
	print( pos_in_grid(2.2,[0,1,2,3,4,5]) )
