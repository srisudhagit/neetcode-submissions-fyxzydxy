class Solution:
    def longestPalindrome(self, s: str) -> str:
        longPalin = s[0]
        longLen = 1
        i = 0
        # finding odd length palindrome 
        while i < len(s):
            center = i
            # Odd length
            hop = 0
            while center-hop >= 0 and center+hop < len(s) and s[center-hop] == s[center+hop]:
                currLen = 1 + 2 * hop
                if currLen > longLen:
                    longLen = currLen
                    longPalin = s[center-hop:center+hop+1]
                hop += 1
            
            # Even length
            hop = 0
            while center-hop >= 0 and center+hop+1 < len(s) and s[center-hop] == s[center+hop+1]:
                currLen = 2 + 2 * hop
                if currLen > longLen:
                    longLen = currLen
                    longPalin = s[center-hop:center+hop+2]
                hop += 1
            i += 1

        return longPalin
