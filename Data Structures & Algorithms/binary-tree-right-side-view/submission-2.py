# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        outputList = []
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            # print last element in each level
            rightEle = None
            while size:
                popEle = queue.popleft()
                if popEle:
                    rightEle = popEle.val
                    queue.append(popEle.left)
                    queue.append(popEle.right)
                size -= 1
            if rightEle:
                outputList.append(rightEle)

        return outputList
    

