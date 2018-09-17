class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def allPossibleFBT(self, N):
		if N == 1:
			return [TreeNode(0)]
		result = []
		N -= 1
		for i in range(1, N, 2):
			left = self.allPossibleFBT(i)
			right = self.allPossibleFBT(N-i)
			for ltree in left:
				for rtree in right:
					root = TreeNode(0)
					root.left = ltree
					root.right = rtree
					result.append(root)
		return result

if __name__ == '__main__':
	solu = Solution()
	x = solu.allPossibleFBT(7)
	print(x)
