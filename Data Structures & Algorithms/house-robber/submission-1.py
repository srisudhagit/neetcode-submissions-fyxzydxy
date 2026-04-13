class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [0] * size
        if size >= 2:
            dp[size-1] = nums[size-1]
            dp[size-2] = max(nums[size-2], nums[size-1])
        else:
            return sum(nums)

        for i in range(size-3, -1, -1):
            dp[i] = max(nums[i] + dp[i+2], dp[i+1])

        return dp[0]