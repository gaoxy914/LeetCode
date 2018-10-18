class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        if root.val < L:
            if root.right:
                root = self.trimBST(root.right, L, R)
            else:
                root = None
        elif root.val > R:
            if root.left:
                root = self.trimBST(root.left, L, R)
            else:
                root = None
        else:
            if root.left:
                root.left = self.trimBST(root.left, L, R)
            if root.right:
                root.right = self.trimBST(root.right, L, R)
        return root
