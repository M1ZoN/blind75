# https://leetcode.com/problems/balanced-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def util(self, root):
        if not root:
            return 0
        
        final_dp = 0
        stack = []
        stack.append((root, 1))
        
        while stack:
            node, dp = stack.pop()

            if dp > final_dp:
                final_dp = dp
            
            if node.left:
                stack.append((node.left, dp + 1))

            if node.right:
                stack.append((node.right, dp + 1))
        return final_dp
        
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            
            if (abs(self.util(node.left) - self.util(node.right)) > 1):
                return False
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return True

root = TreeNode(1)
node2 = TreeNode(2)
node22 = TreeNode(2)
node3 = TreeNode(3)
node33 = TreeNode(3)
node4 = TreeNode(4)
node44 = TreeNode(4)

root.left = node2
root.right = node22

node2.left = node3
node2.right = node33

node3.left = node4
node3.right = node44

a = Solution()
print(a.isBalanced(root))
