class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left ,right = 0, len(heights)-1
        volume = maxVolume = 0

        while left < right:
            volume = min(heights[right],heights[left])*(right-left)
            maxVolume = max(volume,maxVolume)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return maxVolume
            
            