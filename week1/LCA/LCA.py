# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def util(self, root: 'TreeNode', myHash, parentVal):
        if not myHash and root:
            myHash[root.val] = [root.val]
        elif myHash[parentVal] and root:
            myHash[root.val] =[root.val] + myHash[parentVal]
        if root.left:
            self.util(root.left, myHash, root.val)
        if root.right:
            self.util(root.right, myHash, root.val)

    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        myHash = {}
        self.util(root, myHash, root.val)
        found = False
        i = 0
        print(myHash[p])
        while i < len(myHash[p]) and not found:
            if myHash[p][i] in myHash[q]:
                res = myHash[p][i]
                found = True
            i += 1
        
        resNode = TreeNode(res)
        return resNode


a = Solution()

root = TreeNode(6)
node2 = TreeNode(2)
node8 = TreeNode(8)
node0 = TreeNode(0)
node4 = TreeNode(4)
node7 = TreeNode(7)
node9 = TreeNode(9)
node3 = TreeNode(3)
node5 = TreeNode(5)

root.left = node2
root.right = node8

node2.left = node0
node2.right = node4

node8.left = node7
node8.right = node9

node4.left = node3
node4.right = node5

print(a.lowestCommonAncestor(root, 2, 8).val)