class Solution(object):
	def selfDividingNumbers(self, left, right):
		reuslt = []
		for number in range(left, right+1):
			x = str(number)
			flag = True
			for i in x:
				if i == '0' or number % int(i) != 0:
					flag = False
					break
			if flag : reuslt.append(number)
		return reuslt