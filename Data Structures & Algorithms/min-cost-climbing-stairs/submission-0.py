class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*(len(cost))
        lastInd = len(cost) - 1
        dp[lastInd] = cost[lastInd]
        dp[lastInd - 1] = min(cost[lastInd-1], cost[lastInd-1]+dp[lastInd])
        for i in range(lastInd-2,-1,-1):
            dp[i] = min(cost[i]+dp[i+2] , cost[i]+dp[i+1])

        return min(dp[0], dp[1])
        