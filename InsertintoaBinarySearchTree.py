class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def insertIntoBST(self, root, val):
		if val < root.val:
			if root.left == None:
				node = TreeNode(val)
				root.left = node
			else:
				self.insertIntoBST(root.left, val)
		if val > root.val:
			if root.right == None:
				node = TreeNode(val)
				root.right = node
			else:
				self.insertIntoBST(root.right, val)
		return root