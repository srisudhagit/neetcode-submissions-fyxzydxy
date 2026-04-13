class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minProdSofar = 1
        maxProdSofar = 1
        res = nums[0]

        for i in range(len(nums)):

            temp = maxProdSofar 

            maxProdSofar = max(nums[i], max(nums[i] * maxProdSofar, nums[i] * minProdSofar))
            minProdSofar = min(nums[i], min(nums[i] * temp , nums[i] * minProdSofar))
            res = max(res, maxProdSofar)

        
        return res

