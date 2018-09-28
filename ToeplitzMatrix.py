class Solution(object):
	def isToeplitzMatrix(self, matrix):
		flag = True
		x = 0
		y = 0
		while x < len(matrix) and flag:
			i = x
			j = y
			cur = matrix[x][y]
			while i < len(matrix) and j < len(matrix[0]) and flag:
				if matrix[i][j] != cur:
					flag = False
				i += 1
				j += 1
			x += 1
		x = 0
		y = 0
		while y < len(matrix[0]) and flag:
			i = x
			j = y
			cur = matrix[x][y]
			while i < len(matrix) and j < len(matrix[0]) and flag:
				if matrix[i][j] != cur:
					flag = False
				j += 1
				i += 1
			y += 1
		return flag

if __name__ == '__main__':
	solu = Solution()
	matrix = [
  [1,2],
  [2,2]
]
	x = solu.isToeplitzMatrix(matrix)
	print(x)