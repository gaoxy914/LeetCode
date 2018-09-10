class Solution(object):
	#O(n^2)
	def numJewelsInStones(self, J, S):
		count = 0
		for i in range(len(J)):
			for j in range(len(S)):
				if S[j] == J[i]:
					count += 1
		return count

	def numJewelsInStones(self, J, S):
		count = 0
		for stone in S:
			if stone in J:
				count += 1
		return count

	#O(n)
	def numJewelsInStones(self, J, S):
		exist = [0] * 256
		for stone in J:
			exist[ord(stone)] = 1
		count = 0
		for stone in S:
			if exist[ord(stone)]:
				count += 1
		return count




if __name__ == '__main__':
 	solu = Solution()
 	J = "aA"
 	S = "aAAbbbb"
 	x = solu.numJewelsInStones(J, S)
 	print x

