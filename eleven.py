from utils import load

# grid = [[seat for seat in line] for line in load()]

# change = True

# while change:
# 	newGrid = [[grid[r][c] for c in range(len(grid[0]))] for r in range(len(grid))]
# 	# print(newGrid)

# 	change = False
# 	for row in range(len(grid)):
# 		for col in range(len(grid[0])):
# 			seats = [(row-1, col-1), (row-1, col), (row-1, col+1), (row, col-1), (row, col+1), (row+1, col-1), (row+1, col), (row+1, col+1)]
# 			if grid[row][col] == 'L':
# 				occupiedAdjacents = False
# 				for (r, c) in seats:
# 					if r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0]):
# 						if grid[r][c] == '#':
# 							occupiedAdjacents = True
# 							break

# 				if not occupiedAdjacents:
# 					newGrid[row][col] = '#'
# 					change = True


# 			elif grid[row][col] == '#':
# 				numberOccupied = 0
# 				for (r, c) in seats:
# 					if r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0]):
# 						if grid[r][c] == '#':
# 							numberOccupied += 1

# 				if numberOccupied >= 4:
# 					newGrid[row][col] = 'L'
# 					change = True

# 	grid = newGrid


# numberOccupied = 0
# for row in grid:
# 	for seat in row:
# 		if seat == '#':
# 			numberOccupied += 1

# print(numberOccupied)


## part 2
grid = [[seat for seat in line] for line in load()]

change = True

while change:
	newGrid = [[grid[r][c] for c in range(len(grid[0]))] for r in range(len(grid))]

	change = False
	for row in range(len(grid)):
		for col in range(len(grid[0])):
			seats = [(-1, -1), (-1, 0), (-1, +1), (0, -1), (0, +1), (+1, -1), (+1, 0), (+1, +1)]
			if grid[row][col] == 'L':
				occupiedVisibles = False
				for (r, c) in seats:
					dir1, dir2 = row + r, col + c
					while dir1 >= 0 and dir2 >= 0 and dir1 < len(grid) and dir2 < len(grid[0]) and grid[dir1][dir2] == '.':
						dir1 = dir1 + r
						dir2 = dir2 + c
					if dir1 >= 0 and dir2 >= 0 and dir1 < len(grid) and dir2 < len(grid[0]) and grid[dir1][dir2] == '#':
						occupiedVisibles = True
						break

				if not occupiedVisibles:
					newGrid[row][col] = '#'
					change = True


			elif grid[row][col] == '#':
				numberOccupied = 0
				for (r, c) in seats:
					dir1, dir2 = row + r, col + c
					while dir1 >= 0 and dir2 >= 0 and dir1 < len(grid) and dir2 < len(grid[0]) and grid[dir1][dir2] == '.':
						dir1 = dir1 + r
						dir2 = dir2 + c
					if dir1 >= 0 and dir2 >= 0 and dir1 < len(grid) and dir2 < len(grid[0]) and grid[dir1][dir2] == '#':
						numberOccupied += 1

				if numberOccupied >= 5:
					newGrid[row][col] = 'L'
					change = True

	grid = newGrid
	# print(grid)


numberOccupied = 0
for row in grid:
	for seat in row:
		if seat == '#':
			numberOccupied += 1

print(numberOccupied)






