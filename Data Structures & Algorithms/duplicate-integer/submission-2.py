class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numFreqcnt = Counter(nums)
        for k,v in numFreqcnt.items():
            if v > 1:
                return True
        return False

        