# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getLargest(self, node):
        if node.right == None:
            return node
        return self.getLargest(node.right)

    def getSmallest(self, node):
        if node.left == None:
            return node
        return self.getSmallest(node.left)
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        largestLeft = self.getLargest(root.left) if root.left else None
        smallestRight = self.getSmallest(root.right) if root.right else None

        if largestLeft and largestLeft.val >= root.val:
            return False
        if smallestRight and smallestRight.val <= root.val:
            return False

        return self.isValidBST(root.left) and self.isValidBST(root.right)
        


        