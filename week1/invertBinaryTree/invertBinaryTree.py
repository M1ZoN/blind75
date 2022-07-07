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