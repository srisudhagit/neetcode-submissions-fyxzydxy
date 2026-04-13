class Solution:

    def encode(self, strs: List[str]) -> str:
        retStrArray = []
        for string in strs:
            retStrArray.append(f"{len(string)}#{string}")
        return ''.join(retStrArray)

    def decode(self, s: str) -> List[str]:
        i = 0
        decodeStr = []

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            strlen = int(s[i:j])
            decodeStr.append(s[j+1:j+1+strlen])
            i = j + 1 + strlen 
        return decodeStr

