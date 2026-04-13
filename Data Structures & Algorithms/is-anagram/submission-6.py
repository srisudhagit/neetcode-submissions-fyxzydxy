class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fremap1 = {}

        for char in s:
            fremap1[char] = fremap1.get(char,0) + 1

        for char in t:
            fremap1[char] = fremap1.get(char,0) - 1

        return all(v == 0 for v in fremap1.values())