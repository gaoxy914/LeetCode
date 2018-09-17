class Solution(object):
	def complexNumberMultiply(self, a, b):
		anum = a.split('+')
		bnum = b.split('+')
		c = int(anum[0])
		d = int(anum[1].strip('i'))
		e = int(bnum[0])
		f = int(bnum[1].strip('i'))
		g = c*e - d*f
		h = c*f + d*e
		return str(g)+'+'+str(h)+'i'

if __name__ == '__main__':
	a = "1+1i"
	print(a.split('+')[1].strip('i'))