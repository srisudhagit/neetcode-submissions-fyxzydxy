class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we use defaultdict to avoid key errors 
        # and initialize non-present keys with default values
        groups = defaultdict(list)

        for string in strs:
            # since words have limited 26 alphabets, we form 26 char freq and use it as key
            key = "".join(sorted(string))
            groups[key].append(string)

        return list(groups.values())


