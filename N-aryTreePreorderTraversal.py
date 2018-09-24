class Node(object):
	def __init__(self, val, children):
		self.val = val
		self.children = children

class Solution(object):
	def preorder(self, root):
		result = []
		if not root:
			return result
		stack = [root]
		while stack:
			node = stack.pop()
			result.append(node.val)
			if node.children:
				stack.extend(node.children[::-1])
		return result