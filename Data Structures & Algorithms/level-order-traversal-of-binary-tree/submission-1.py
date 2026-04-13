# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        outputList = []
        bfsQueue = deque()
        bfsQueue.append(root)
        while bfsQueue:
            size = len(bfsQueue)
            levelArr = []
            while size > 0:
                popEle = bfsQueue.popleft()
                size -= 1
                if popEle:
                    bfsQueue.append(popEle.left)
                    bfsQueue.append(popEle.right)
                    levelArr.append(popEle.val)

            if levelArr:
                outputList.append(levelArr)

        return outputList

            

        