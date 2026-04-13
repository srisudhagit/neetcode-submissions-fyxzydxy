class Solution:
    def rob(self, nums: List[int]) -> int:

        def HouseRob(nums):
            size = len(nums)
            dp = [0]*size
            if size <= 2:
                return max(nums)
            dp[size-1] = nums[size-1]
            dp[size-2] = max(nums[size-2],dp[size-1])
            for i in range(size-3 , -1, -1):
                dp[i] = max(dp[i+1], nums[i]+dp[i+2])

            return dp[0]

        if len(nums) < 2:
            return max(nums)
            
        leftIncluded = HouseRob(nums[0:len(nums)-1])
        rightIncluded = HouseRob(nums[1:len(nums)])

        return max(leftIncluded,rightIncluded)