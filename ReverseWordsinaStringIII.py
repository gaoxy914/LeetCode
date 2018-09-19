class Solution(object):
	def reverseWords(self, s):
		result = ""
		for str in s.split(" "):
			result += str[::-1]
			result += " "
		result = result[:-1]
		return result

	# return ' '.join(list(e[::-1] for e in s.split()))