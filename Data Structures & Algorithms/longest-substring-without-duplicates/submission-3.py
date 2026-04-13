class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        currlen = maxlen = 0
        charset = set()
        while right < len(s):
            char = s[right]
            if char not in charset:
                charset.add(char)
                currlen = right-left+1
                maxlen = max(currlen,maxlen)
                right += 1
            else:
                charset.remove(s[left])
                currlen -= 1
                left += 1
            
        return maxlen

            