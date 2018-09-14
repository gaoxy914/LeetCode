class Solution(object):
	def findAndReplacePattern(self, words, pattern):
		code = self.word2code(pattern)
		return [word for word in words if self.word2code(word) == code]		

	def word2code(self, word):
		exist = {}
		code = ""
		number = 0
		for character in word:
			if character not in exist:
				exist[character] = number
				number += 1
			code += str(exist[character])
		return code

if __name__ == '__main__':
	words = ["abc","deq","mee","aqq","dkd","ccc"]
	pattern = "abb"
	solu = Solution()
	x = solu.findAndReplacePattern(words, pattern)
	print(x)