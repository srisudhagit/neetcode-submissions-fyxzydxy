class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCnt = Counter(s)
        tCnt = Counter(t)
        return sCnt == tCnt
            
