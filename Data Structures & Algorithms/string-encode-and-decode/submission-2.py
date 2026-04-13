class Solution:

    def encode(self, strs: List[str]) -> str:
        retStr = []
        for string in strs:
            retStr.append(f"{len(string)}#{string}")
        return "".join(retStr)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return[]
        strs = []
        i = j = 0
        while j < len(s):
            
            # find the # to get the length(i to j-1) and array (j+1 to j+length)
            while s[j] != "#":
                j += 1
            
            currlen = int(s[i:j])
            currString = s[j+1:j+1+currlen]
            strs.append(currString)
            
            i = j = j+int(currlen)+1

        return strs
