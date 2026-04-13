class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # formula is maxarea = (j-i)*min(heights[i],heights[j])

        i,j = 0,len(heights)-1
        currArea,maximumArea = 0,0
        while i<j:
            currArea = (j-i) * min(heights[i],heights[j])
            maximumArea = max(maximumArea,currArea)
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        
        return maximumArea
