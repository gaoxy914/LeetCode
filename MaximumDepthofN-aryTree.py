class Node(object):
	def __init__(self, val, children):
		self.val = val
		self.children = children

class Solution(object):
	def maxDepth(self, root):

		def dfs(root):
			d = []
			if root.children:
				for node in root.children:
					d.append(dfs(node))
				result = max(d) + 1
			else:
				result = 1
			return result
		if root == None:
			return 0
		return dfs(root)
		