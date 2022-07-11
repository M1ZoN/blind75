# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    diameter = 0

    def util(self, root):
        if not root:
            return 0
        
        l_max = self.util(root.left)
        r_max = self.util(root.right)
        self.diameter = max(self.diameter, l_max + r_max)
        return 1 + max(l_max, r_max)

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.util(root)
        return self.diameter

r4 = TreeNode(4)
r5 = TreeNode(5)
r2 = TreeNode(2, r4, r5)
r3 = TreeNode(3)
root = TreeNode(1, r2, r3)

Solution.diameterOfBinaryTree(root)
