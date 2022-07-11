# 543. Diameter of Binary Tree

Date Created: July 6, 2022 5:36 PM
Difficulty: Easy
Due Date: July 10, 2022
Status: Next Up
Week #: Week 2

# Description

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

**Example 1:**

![Untitled](https://assets.leetcode.com/uploads/2021/03/06/diamtree.jpg)

```
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
```

**Example 2:**

```
Input: root = [1,2]
Output: 1
```

# Solution

```python
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

```