class Solution(object):
	def uniqueMorseRepresentations(self, words):
		morsecode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
		result = []
		for word in words:
			str = ""
			for character in word:
				str += morsecode[ord(character)-ord('a')]
			if str not in result:
				result.append(str)
		return len(result)



if __name__ == '__main__':
	words = ["gin", "zen", "gig", "msg"]
	solu = Solution()
	x = solu.uniqueMorseRepresentations(words)
	print x