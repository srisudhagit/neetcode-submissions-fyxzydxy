# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder = []

        def inorderTraversal(node):
            if node:
                inorderTraversal(node.left)
                inorder.append(node.val)
                inorderTraversal(node.right)

        inorderTraversal(root)

        return inorder[k-1]
        