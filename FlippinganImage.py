class Solution(object):
	def flipAndInvertImage(self, A):
		return [[1-A[j][i] for i in range(len(A[j])-1, -1, -1)] for j in range(len(A))]

	#尼玛 一开始想的这样 但是没写对
	def flipAndInvertImage(self, A):
		return [[1^i for i in row[::-1]] for row in A]