class Solution(object):
	def maxIncreaseKeepingSkyline(self, grid):
		length = len(grid)
		top = [0] * length
		left = [0] * length
		for i in range(length):
			left[i] = max(grid[i])
			for j in range(length):
				top[i] = max(top[i], grid[j][i])
		maximum = 0
		for i in range(length):
			for j in range(length):
				maximum += min(top[j], left[i]) - grid[i][j]
		return maximum

if __name__ == '__main__':
	solu = Solution()
	grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
	x = solu.maxIncreaseKeepingSkyline(grid)
	print x