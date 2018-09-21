class Node(object):
	def __init__(self, val, children):
		self.val = val
		self.children = children

class Solution(object):
	def postorder(self, root):
		result = []
		if root != None:
			res = []
			for node in root.children:
				res += self.postorder(node)
			result += res
			result.append(root.val)
		return result

class Solution(object):
	def postorder(self, root):
		stack = [root]
		output = []
		if not root:
			return output
		while stack:
			node = stack.pop()
			output.append(node.val)
			stack.extend(node.children)
		return output[::-1]