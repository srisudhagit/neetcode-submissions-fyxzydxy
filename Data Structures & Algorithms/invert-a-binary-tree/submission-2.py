# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isLeaf(self, node):
        return not node.left and not node.right

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or self.isLeaf(root):
            return root
        else:
            root.left, root.right = root.right, root.left

            self.invertTree(root.left)
            self.invertTree(root.right)
            return root

        