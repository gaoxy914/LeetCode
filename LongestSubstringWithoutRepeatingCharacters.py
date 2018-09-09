class Solution(object):
	def lengthOfLongestSubstring(self, s):
		letter = {}
		length = 0
		maxlength = 0
		i = 0
		while(i < len(s)):
			if s[i] not in letter:
				length += 1
				letter[s[i]] = i
				i += 1
			else:
				i = letter[s[i]] + 1
				letter.clear()
				if length > maxlength:
					maxlength = length
				length = 0
		if length > maxlength:
			maxlength = length
		return maxlength

if __name__ == '__main__':
	solu = Solution()
	s = 'c'
	x = solu.lengthOfLongestSubstring(s)
	print x	
