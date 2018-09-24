class Solution(object):
	def customSortString(self, S, T):
		dic = {}
		position = 0
		for s in S:
			dic[s] = position
			for t in T:
				if t == s:
					position += 1
		l = ['@'] * len(T)
		n = len(T) - 1
		for t in T:
			if t in dic:
				l[dic[t]] = t
				dic[t] += 1
			else:
				l[n] = t
				n -= 1
		return ''.join(l)