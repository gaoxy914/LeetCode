class Solution(object):
	def toLowerCase(self, str):
		return str.lower()

	#但是这个题应该考的是ASCII码
	def toLowerCase(self, str):
		result = ""
		for character in str:
			ascii_value = ord(character)
			if ascii_value >= 65 and ascii_value <= 90:
				ascii_value += 32
			result += chr(ascii_value)
		return result
