class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        runSum = nums[0]
        for i in range(1,len(nums),1):
            num = nums[i]
            runSum = max(runSum + num, num)
            maxSum = max(maxSum, runSum)
            
        return maxSum

        