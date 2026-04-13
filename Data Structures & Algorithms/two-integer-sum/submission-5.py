class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenDict = {}
        for i ,ele in enumerate(nums):
            reqEle = target-ele
            if reqEle in seenDict:
                return [seenDict[reqEle],i]
            seenDict[ele] = i
