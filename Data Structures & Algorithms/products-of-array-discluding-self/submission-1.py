class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preProd, sufProd, retArr = [],  [],  []

        currProd = 1
        for num in nums:
            preProd.append(currProd)
            currProd *= num

        currProd = 1
        for num in reversed(nums):
            sufProd.append(currProd)
            currProd *= num

        sufProd.reverse()

        for i,_ in enumerate(nums):
            retArr.append(preProd[i]*sufProd[i])

        return retArr