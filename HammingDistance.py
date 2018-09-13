class Solution(object):
	def hammingDistance(self, x, y):
		binaryx = "{0:b}".format(x)
		binaryy = "{0:b}".format(y)
		binaryx = binaryx[::-1]
		binaryy = binaryy[::-1]
		lenx = len(binaryx)
		leny = len(binaryy)
		difference = 0
		for i in range(min(lenx, leny)):
			if binaryx[i] != binaryy[i]:
				difference += 1
		if lenx > leny:
			for number in binaryx[leny:]:
				if number == '1':
					difference += 1
		if leny > lenx:
			for number in binaryy[lenx:]:
				if number == '1':
					difference += 1
		return difference

	#位运算
	def hammingDistance(self, x, y):
		n = x ^ y
		i = 1
		while n:
			i += n & 1
			z = z >> 1
		return i
