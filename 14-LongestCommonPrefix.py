class Solution(object):
	def longestCommonPrefix(self, strs):
		result = ''
		if strs == []:
			return result
		for i in range(len(strs[0])):
			for j in range(len(strs)):
				if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
					return result
			result += strs[0][i]
		return result

if __name__ == '__main__':
	strs = ['abcd', 'abc', 'abd']
	print Solution().longestCommonPrefix(strs)