class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        currLen = maxLen = 0
        eleSet = set(nums)

        # finds the min ele in array to return longest consecutive sequence
        for i,num in enumerate(nums):
            if num-1 in eleSet:
                continue
            else:
                start = num
                currLen = 0
                while num in eleSet:
                    currLen += 1
                    num += 1
                if currLen > maxLen:
                    maxLen = currLen
        
        return maxLen


        

        