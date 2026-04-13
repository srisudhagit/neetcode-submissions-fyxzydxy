class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        runSum = nums[0]
        for i in range(1,len(nums),1):
            num = nums[i]
            if runSum + num < num:
                runSum = num
            else:
                runSum = runSum + num
            maxSum = max(maxSum, runSum)
            
        return maxSum

        