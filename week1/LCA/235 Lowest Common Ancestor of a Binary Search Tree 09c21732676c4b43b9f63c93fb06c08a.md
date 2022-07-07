# 235. Lowest Common Ancestor of a Binary Search Tree

Date Created: July 2, 2022 10:05 AM
Difficulty: Easy
Due Date: July 7, 2022
Status: Completed
Week #: Week 1

# Description

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow **a node to be a descendant of itself**).”

**Example 1:**

![Untitled](235%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Search%20Tree%2009c21732676c4b43b9f63c93fb06c08a/Untitled.png)

```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

```

**Example 2:**

![Untitled](235%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Search%20Tree%2009c21732676c4b43b9f63c93fb06c08a/Untitled%201.png)

```
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

```

**Example 3:**

```
Input: root = [2,1], p = 2, q = 1
Output: 2
```

# Solution

```python
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
```