class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        climbCache = [0]*(n+1)
        climbCache[1] = 1
        climbCache[2] = 2
        for i in range(3,n+1):
            climbCache[i] = climbCache[i-1] + climbCache[i-2]

        return climbCache[n]
        