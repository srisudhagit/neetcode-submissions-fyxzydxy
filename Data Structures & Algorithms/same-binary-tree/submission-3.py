# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isLeaf(self, node):
        return not node.left and not node.right

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif (not p and q) or (p and not q) or (self.isLeaf(p) and not self.isLeaf(q)) or (not self.isLeaf(p) and self.isLeaf(q)):
            return False                            
        elif p.val == q.val and self.isLeaf(p) and self.isLeaf(q):
            return True
        else:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



            
