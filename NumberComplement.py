class Solution(object):
	def findComplement(self, num):
		number = ""
		for i in "{0:b}".format(num):
			number += str(int(i)^1)
		return int(number, 2)