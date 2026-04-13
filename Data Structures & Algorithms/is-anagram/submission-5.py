class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # this solution runs in O(n) time and O(n) space
        #sCnt = Counter(s)
        #tCnt = Counter(t)
        #return sCnt == tCnt

        # this solution runs in O(n) time and O(1) space
        if len(s) != len(t):
            return False
        
        freq = [0]*26

        for i in range(len(s)):
            freq[ord(s[i])-ord('a')] += 1
            freq[ord(t[i])-ord('a')] -= 1

        return all(x == 0 for x in freq)

            
