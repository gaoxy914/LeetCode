class Solution(object):
	def projectionArea(self, grid):
		n = len(grid)
		number = [max(row) for row in grid]
		up = 0
		for j in range(n):
			maximum = 0
			for i in range(n):
				if grid[i][j] != 0:
					up += 1
				if grid[i][j] > maximum:
					maximum = grid[i][j]
			number.append(maximum)
		number.append(up)
		return sum(number)

	#zip(*A)
	def projectionArea(self, grid):
		return (len(grid) ** 2 - sum(grid, []).count(0) + sum(max(row) for row in grid) + sum(max(col) for col in zip(*grid)))