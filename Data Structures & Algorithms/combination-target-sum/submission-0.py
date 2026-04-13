class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # use a decision tree based approach to find all possible combinations to make target sum
        finalList = []

        # create a recursive function to traverse decision tree
        # currPath show the tree brach, currList shows the level of the list and currSum shows the sum along the currPath
        def findAllComb(currPath, currList, currSum):
            if currSum == target:
                finalList.append(currPath)
                return 
            
            elif currSum > target:
                return

            else:
                for i,num in enumerate(currList):
                    findAllComb(currPath + [currList[i]], currList[i:],currSum+num)
            
        
        findAllComb([],nums,0)
        return finalList