class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsCounter = Counter(nums)
        topk_elements = numsCounter.most_common(k)
        
        return [num for num ,cnt in topk_elements]

        