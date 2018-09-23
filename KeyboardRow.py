class Solution(object):
	def findWords(self, words):
		q = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
		a = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
		z = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
		result = []
		for x in words:
			lowerx = x.lower()
			flag = True
			if lowerx[0] in q:
				for c in lowerx:
					if c not in q:
						flag = False
						break
			if lowerx[0] in a:
				for c in lowerx:
					if c not in a:
						flag = False
						break
			if lowerx[0] in z:
				for c in lowerx:
					if c not in z:
						flag = False
						break
			if flag:
				result.append(x)
		return result

class Solution:
    def findWords(self, words):
        return [w for w in words if any(not set(w.lower()) - row for row in (set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")))]