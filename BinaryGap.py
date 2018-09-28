class Solution(object):
	def binaryGap(self, N):
		b = "{0:b}",format(N)
		dis = [0]
		last = -1
		print(b)
		for i in range(len(b)):
			if b[i] == '1':
				print(last)
				if last != -1:
					dis.append(i-last)
				last = i
		return max(dis)
