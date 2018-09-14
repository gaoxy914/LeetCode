class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def pruneTree(self, root):
		if root.left != None:
			root.left = self.pruneTree(root.left)
		if root.right != None:
			root.right = self.pruneTree(root.right)
		if root.left == None and root.right == None and root.val == 0:
			root = None
		return root