# 110. Balanced Binary Tree

Date Created: July 2, 2022 10:15 AM
Difficulty: Easy
Due Date: July 8, 2022
Status: Completed
Week #: Week 1

# Description

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

> a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
> 

**Example 1:**

![Untitled](110%20Balanced%20Binary%20Tree%20cfcd2fd021094e5b95deeb69ba6a0c8d/Untitled.png)

```
Input: root = [3,9,20,null,null,15,7]
Output: true

```

**Example 2:**

![Untitled](110%20Balanced%20Binary%20Tree%20cfcd2fd021094e5b95deeb69ba6a0c8d/Untitled%201.png)

```
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

```

**Example 3:**

```
Input: root = []
Output: true

```

# Solution

```python
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
```