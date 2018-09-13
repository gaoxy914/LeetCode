class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution(object):
	def constructMaximumBinaryTree(self, nums):
		maxNumber = max(nums)
		index = nums.index(maxNumber)
		node = TreeNode(maxNumber)
		if len(nums[:index]) > 0:
			node.left = self.constructMaximumBinaryTree(nums[:index])
		if len(nums[index+1:]) > 0:
			node.right = self.constructMaximumBinaryTree(nums[index+1:])
		return node
