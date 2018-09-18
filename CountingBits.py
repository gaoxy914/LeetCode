class Solution(object):
	def countBits(self, num):
		result = []
		for number in range(num+1):
			result.append("{0:b}".format(number).count('1'))
		return result

if __name__ == '__main__':
	print("{0:b}".format(12).count('1'))