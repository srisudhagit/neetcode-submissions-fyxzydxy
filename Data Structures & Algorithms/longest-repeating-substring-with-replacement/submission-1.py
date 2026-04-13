class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freMap = {}
        maxLen = 0
        l = r = 0
        for r in range(len(s)):
            freMap[s[r]] = freMap.get(s[r],0) + 1


            if (r-l+1) - max(freMap.values()) > k:
                freMap[s[l]] -= 1
                l += 1

            maxLen = max(maxLen,r-l+1)

        return maxLen
            

        