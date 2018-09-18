class Solution(object):
	def numberOfLines(self, widths, S):
		line = 0
		lastLine = 0
		for c in S:
			index = ord(c) - ord('a')
			lastLine += widths[index]
			if lastLine > 100:
				line += 1
				lastLine = widths[index]
		if lastLine > 0:
			line += 1
		return [line, lastLine]