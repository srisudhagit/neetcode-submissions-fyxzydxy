# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # preorder gives us root
        root = TreeNode(preorder[0])
        # identify root position in inorder to seperate left and right tree using lengths
        indexOfRootinInorder = inorder.index(preorder[0])
        # 0 to midOrder gives us left subtree of root and midOrder+1 to right gives us right subtree
        root.left = self.buildTree(preorder[1:indexOfRootinInorder+1], inorder[0:indexOfRootinInorder])
        root.right = self.buildTree(preorder[indexOfRootinInorder+1:], inorder[indexOfRootinInorder+1:])

        return root