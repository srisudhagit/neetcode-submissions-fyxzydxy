class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            num_complement = target-num
            if num_complement in seen:
                return [seen[num_complement],i]
            seen[num] = i
        return []
        