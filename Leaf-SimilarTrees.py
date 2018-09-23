class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def leafSimilar(self, root1, root2):

		def getLeaves(root, result):
			if root.left:
				getLeaves(root.left, result)
			if root.right:
				getLeaves(root.right, result)
			if not root.left and not root.right:
				result.append(root.val)

		leaves1 = []
		leaves2 = []
		getLeaves(root1, leaves1)
		getLeaves(root2, leaves2)
		return leaves1 == leaves2