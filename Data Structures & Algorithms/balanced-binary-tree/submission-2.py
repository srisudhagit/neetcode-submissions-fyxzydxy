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
        if not node or self.isLeaf(root):
            return 0
        else:
            return 1 + max(self.height(node.left), self.height(node.right))


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root or self.isLeaf(root):
            return True
        else:
            isLeftBalanced = self.isBalanced(root.left)
            isRightBalanced = self.isBalanced(root.right)
            leftHeight = self.height(root.left)
            rightHeight = self.height(root.right)
            isRootBalanced = abs(self.height(root.left) - self.height(root.right)) <= 1
            print(root.val,isLeftBalanced, isRightBalanced, isRootBalanced, leftHeight, rightHeight)
            return  isLeftBalanced and isRightBalanced and isRootBalanced
        

    

        