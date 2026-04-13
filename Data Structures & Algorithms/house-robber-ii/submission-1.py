class Solution:
    def rob(self, nums: List[int]) -> int:

        def HouseRob(nums,i,j):
            a , b = 0, 0

            for num in nums[i:j+1]:
                temp = max(num+a, b)
                a = b
                b = temp
            
            return b

        if len(nums) < 2:
            return max(nums)
            
        leftIncluded = HouseRob(nums,0,len(nums)-2)
        rightIncluded = HouseRob(nums,1,len(nums)-1)

        return max(leftIncluded,rightIncluded)