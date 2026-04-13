class Solution:
    def climbStairs(self, n: int) -> int:
        climbCache = [0]*(n+1)
        climbCache[n] = 1
        climbCache[n-1] = 1
        for i in range(n-2,-1,-1):
            climbCache[i] = climbCache[i+1] + climbCache[i+2]

        return climbCache[0]
        