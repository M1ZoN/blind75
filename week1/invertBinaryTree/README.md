# 226. Invert Binary Tree

Date Created: July 1, 2022 5:26 PM
Difficulty: Easy
Due Date: July 3, 2022
Status: Completed
Week #: Week 1

# Description

Given the `root`
 of a binary tree, invert the tree, and return *its root*.

![Untitled](226%20Invert%20Binary%20Tree%205a3495ef0fae4f329653a5362d2863ad/Untitled.png)

```
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```

![Untitled](226%20Invert%20Binary%20Tree%205a3495ef0fae4f329653a5362d2863ad/Untitled%201.png)

```
Input: root = [2,1,3]
Output: [2,3,1]
```

# Solution

```python
# https://leetcode.com/problems/invert-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if root:
        if root.left or root.right:
            temp = root.left
            root.left = root.right
            root.right = temp

        invertTree(root.left)
        invertTree(root.right)

def printTree(root):
    if root:
        printTree(root.left)
        print(root.val, end=" ")
        printTree(root.right)

left1 = TreeNode(1)
left3 = TreeNode(3)
left2 = TreeNode(2, left1, left3)

right6 = TreeNode(6)
right9 = TreeNode(9)
right7 = TreeNode(7, right6, right9)

root = TreeNode(4, left2, right7)
printTree(root)

invertTree(root)

printTree(root)
```