class Solution(object):
	def spiralMatrixIII(self, R, C, r0, c0):
		result = [[r0, c0]]
		x, y, n, i = 0, 1, 0, 0
		while len(result) < R*C:
			r0, c0, i = r0 + x, c0 + y, i + 1
			if 0 <= r0 < R and 0 <= c0 < C:
				result.append([r0, c0])
			if i == n//2 + 1:
				x , y, n, i = y, -x, n + 1, 0
		return result


if __name__ == '__main__':
	solu = Solution()
	x = solu.spiralMatrixIII(1, 4, 0, 0)
	print(x)