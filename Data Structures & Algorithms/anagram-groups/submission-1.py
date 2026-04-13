class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #choosing defaultdict as it sets default values for missing keys
        groups = defaultdict(list)

        for string in strs:
            #create a key with a string of sorted characters in a input string
            #use this key to add anagrams to dict
            key = ''.join(sorted(string))
            groups[key].append(string)

        return list(groups.values())