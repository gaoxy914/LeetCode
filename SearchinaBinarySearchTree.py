class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def searchBST(self, root, val):
		if root == None:
			return None
		if root.val == val:
			return root
		elif val < root.val:
			return self.searchBST(root.left, val)
		else:
			return self.searchBST(root.right, val)