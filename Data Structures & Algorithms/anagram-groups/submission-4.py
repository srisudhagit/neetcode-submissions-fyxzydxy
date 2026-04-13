class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a dict of key values where key is 26 digit array frequency and values 
        # list of anagrams
        strAanagram = defaultdict(list)

        for string in strs:
            keysArray = [0] * 26
            for char in string:
                key = ord(char) - ord('a')
                keysArray[key] += 1

            strAanagram[tuple(keysArray)].append(string)

        
        return list(strAanagram.values())