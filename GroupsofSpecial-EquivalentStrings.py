class Solution(object):
	def numSpecialEquivGroups(self, A):
		result = []
		for line in A:
			odd = [0] * 26
			even = [0] * 26
			for i in range(len(line)):
				if i % 2:
					odd[ord(line[i]) - ord('a')] += 1
				else:
					even[ord(line[i]) - ord('a')] += 1
			res = str(odd) + str(even)
			if res not in result:
				result.append(res)
		return len(result)

if __name__ == '__main__':
	a = ["a","b","c","a","c","c"]
	solu = Solution()
	x = solu.numSpecialEquivGroups(a)
	print(x)
