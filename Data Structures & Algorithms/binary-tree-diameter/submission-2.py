# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isLeaf(self, node):
        return not node.left and not node.right

    def height(self, node):
        if not node:
            return 0
        else:
            return 1 + max(self.height(node.left), self.height(node.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root or self.isLeaf(root):
            return 0
        else:
            leftDiameter = self.diameterOfBinaryTree(root.left)
            rightDiameter = self.diameterOfBinaryTree(root.right)
            rootDiameter = self.height(root.left) + self.height(root.right)
            print(root.val, leftDiameter, rightDiameter, rootDiameter)
            return max(max(leftDiameter, rightDiameter), rootDiameter)
        
        