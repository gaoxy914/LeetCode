class Solution(object):
	def longestPalindrome(self, s):
		p = [([0]*1000) for i in range(1000)]
		for i in range(len(s)):
			p[i][i] = 1
	
		for i in range(len(s)-1):
			if s[i] == s[i+1]:
				p[i][i+1] = 1

		for j in range(2, len(s)):
			for i in range(j-1):
				if s[i] == s[j]:
					p[i][j] = p[i+1][j-1]

		maxlength = 0
		start = 0
		end = 0
		for i in range(len(s)):
			for j in range(i, len(s)):
				if p[i][j] == 1 and (j-i+1) > maxlength:
					maxlength = j-i+1
					start = i
					end = j+1
		return s[start:end]

if __name__ == '__main__':
	solu = Solution()
	s = solu.longestPalindrome("abcba")
	print s