class Solution(object):
	def uncommonFromSentences(self, A, B):
		result = []
		dic = {}
		for word in A.split()+B.split():
			if word in dic:
				dic[word] += 1
			else:
				dic[word] = 1
		for word, count in dic.items():
			if count == 1:
				result.append(word)
		return result