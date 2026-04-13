class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])
        res = []

        for perm in perms:
            # because we are trying to add number increase the exisiting range
            for pos in range(len(perm)+1):
                perm_copy = perm.copy()
                perm_copy.insert(pos, nums[0])
                res.append(perm_copy)

        return res
