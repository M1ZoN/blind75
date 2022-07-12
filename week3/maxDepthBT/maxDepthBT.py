# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def util(self, root):
        if not root:
            return 0

        lMax = self.util(root.left)
        rMax = self.util(root.right)

        return max(lMax, rMax) + 1


    def maxDepth(self, root: TreeNode) -> int:
        return self.util(root)

a = Solution()

n1 = TreeNode(9)
n2 = TreeNode(15)
n3 = TreeNode(7)
n4 = TreeNode(20, n2, n3)
r = TreeNode(3, n1, n4)

a.maxDepth(r)