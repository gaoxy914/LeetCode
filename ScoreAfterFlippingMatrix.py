class Solution(object):
	def matrixScore(self, A):
		def score(list):
			score = 0
			n = len(list)
			for i in range(n):
				score += (list[i] * 2 ** (n-1-i))
			return score
		
		def score2(list):
			score = 0
			for i in list:
				score += i
			return score

		def reverse(list):
			return [i^1 for i in list]

		def col(A, i):
			return [A[j][i] for j in range(len(A))]

		for i in range(len(A)):
			rev = reverse(A[i])
			if score(A[i]) < score(rev):
				A[i] = rev
		for j in range(len(A[0])):
			rev = reverse(col(A, j))
			if score2(col(A, j)) < score2(rev):
				for i in range(len(A)):
					A[i][j] = rev[i]
		sum = 0
		for row in A:
			sum += score(row)
		return sum

if __name__ == '__main__':
	A = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
	solu = Solution()
	x = solu.matrixScore(A)
	print(x)