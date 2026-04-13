class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        retList = list()
        sortedList = sorted(nums)
        size = len(nums)
        for i,a in enumerate(sortedList):
            # we are not going to find any 3 sum after this point which can sum to 0 since all are +ve numbers
            if a > 0:
                break

            # skip the duplicates being in the same position
            # like [-2,-2,0,2,2] both -2 positions needed be evaluted since its going to be duplicate
            if i>0 and a == sortedList[i-1]:
                continue
            
            j,k = i+1,size-1
            while j < k:
                threeSum = a+sortedList[j]+sortedList[k]
                # if three sum is zero we found the triplet.
                if threeSum == 0:
                    retList.append([a,sortedList[j],sortedList[k]])
                    j += 1
                    k -= 1
                    # moving the 2nd position of the triplet to avoid duplicate entries
                    # eg : -2,-2,0,0,2,2 
                    # (-2,0,2) - position (0,2,5). once this is found we need to skip 0 at position 3. this loop does that.
                    while j < k and sortedList[j] == sortedList[j-1]:
                        j += 1

                elif threeSum > 0:
                    k -= 1
                else:
                    j += 1
                
        return retList
