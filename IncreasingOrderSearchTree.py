class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        slef.right = None

class Solution(object):
    def increasingBST(self, root):
        def inorder(root, numbers):
            if root.left != None:
                inorder(root.left, numbers)
            numbers.append(root.val)
            if root.right != None:
                inorder(root.right, numbers)
        numbers = []
        inorder(root, numbers)
        newroot = TreeNode(numbers[0])
        temp = newroot
        for i in range(1, len(numbers)):
            temp.right = TreeNode(numbers[i])
            temp = temp.right
        return newroot
