class Solution(object):
	def calPoints(self, ops):
		scores = []
		for i in range(len(ops)):
			if ops[i] == "+":
				scores.append(scores[-1]+scores[-2])
			elif ops[i] == "C":
				scores.pop()
			elif ops[i] == "D":
				scores.append(scores[-1]*2)
			else:
				scores.append(int(ops[i]))
		return sum(scores)
